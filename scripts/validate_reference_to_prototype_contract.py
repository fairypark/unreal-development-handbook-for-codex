#!/usr/bin/env python3
"""Validate the Stage 2a Reference-to-Prototype Translation Contract.

The JSON Schema owns portable shape validation. This script adds referential and
gate semantics that are awkward to express in JSON Schema alone. It uses the
``jsonschema`` package when available, but its semantic checks require only the
Python standard library.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = (
    ROOT
    / "skills"
    / "design-unreal-worlds-and-levels"
    / "references"
    / "reference-to-prototype-translation.schema.json"
)

OVERVIEW_METRICS = {
    "BUILT_FOOTPRINT_OCCUPANCY",
    "ZONE_DENSITY_DISTRIBUTION",
    "BUILDING_MASS_COUNT",
    "ROOF_MASS_COUNT",
    "TYPOLOGY_MIX",
    "FRONTAGE_CONTINUITY",
    "BUILDING_GAPS",
    "HEIGHT_BANDS",
    "WATER_BRIDGE_RELATIONSHIP",
    "SHADE_PRESERVATION",
    "VOID_PRESERVATION",
    "HIERARCHY",
    "PATH_CONTINUITY",
    "PROHIBITED_SILHOUETTE",
}

PLAYER_METRICS = {
    "PERCEIVED_DISTANCE",
    "ENCLOSURE",
    "OCCLUSION_REVEAL",
    "ROUTE_CONTINUITY",
    "LANDMARK_HIERARCHY",
    "CLEARANCE",
    "RECOVERY",
    "PLAYER_SCALE_READABILITY",
}

REQUIRED_ZONE_FIELDS = {
    "built_footprint_occupancy",
    "mass_counts",
    "typology_mix",
    "frontage_continuity",
    "building_gaps",
    "route_widths",
    "elevation_transitions",
    "water_and_bridges",
    "shaded_spaces",
    "intentional_voids",
    "hierarchy",
    "prohibited_silhouettes",
}

SCHEMA_VERSION = "1.1.0"
DEPENDENT_STRATA_MODES = {
    "VIDEO_DISTANCE_EXCLUSION",
    "MASK_OTHER",
    "DIRECT_AUTHORED",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _path(parts: Iterable[Any]) -> str:
    rendered = "$"
    for part in parts:
        rendered += f"[{part}]" if isinstance(part, int) else f".{part}"
    return rendered


def schema_errors(instance: Any, schema: dict[str, Any]) -> list[str]:
    """Use Draft 2020-12 validation when jsonschema is installed."""

    try:
        from jsonschema import Draft202012Validator  # type: ignore
    except ImportError:
        return []

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    return [f"schema {_path(error.path)}: {error.message}" for error in errors]


def _require_mapping(value: Any, label: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return {}
    return value


def _require_list(value: Any, label: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        errors.append(f"{label} must be an array")
        return []
    return value


def _index_unique(
    records: list[Any], key: str, label: str, errors: list[str]
) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for position, raw_record in enumerate(records):
        record = _require_mapping(raw_record, f"{label}[{position}]", errors)
        identifier = record.get(key)
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"{label}[{position}].{key} must be a non-empty string")
            continue
        if identifier in indexed:
            errors.append(f"duplicate {label} id: {identifier}")
            continue
        indexed[identifier] = record
    return indexed


def _check_refs(
    values: Any, valid: set[str], label: str, errors: list[str], *, allow_empty: bool = False
) -> set[str]:
    references = _require_list(values, label, errors)
    if not references and not allow_empty:
        errors.append(f"{label} must not be empty")
    result: set[str] = set()
    for reference in references:
        if not isinstance(reference, str) or not reference:
            errors.append(f"{label} contains a non-string or empty id")
            continue
        if reference in result:
            errors.append(f"{label} contains duplicate id {reference}")
        result.add(reference)
        if reference not in valid:
            errors.append(f"{label} references unknown id {reference}")
    return result


def _walk_requirement_refs(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "requirement_ids" and isinstance(child, list):
                found.update(item for item in child if isinstance(item, str))
            else:
                found.update(_walk_requirement_refs(child))
    elif isinstance(value, list):
        for child in value:
            found.update(_walk_requirement_refs(child))
    return found


def _walk_ranges(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        if set(value) == {"min", "max"}:
            minimum = value.get("min")
            maximum = value.get("max")
            if isinstance(minimum, (int, float)) and isinstance(maximum, (int, float)):
                if minimum > maximum:
                    errors.append(f"{path}: min {minimum} exceeds max {maximum}")
        for key, child in value.items():
            _walk_ranges(child, f"{path}.{key}", errors)
    elif isinstance(value, list):
        for position, child in enumerate(value):
            _walk_ranges(child, f"{path}[{position}]", errors)


def _check_ratio_range(value: Any, label: str, errors: list[str]) -> None:
    target = value.get("target") if isinstance(value, dict) else None
    if not isinstance(target, dict):
        errors.append(f"{label}.target must be an object")
        return
    minimum = target.get("min")
    maximum = target.get("max")
    if not all(isinstance(item, (int, float)) for item in (minimum, maximum)):
        errors.append(f"{label}.target must contain numeric min and max")
        return
    if minimum < 0 or maximum > 1:
        errors.append(f"{label}.target must remain within the 0..1 ratio range")


def validate_contract(contract: Any, schema: dict[str, Any] | None = None) -> list[str]:
    errors: list[str] = []
    contract = _require_mapping(contract, "$", errors)
    if not contract:
        return errors

    required_top_level = {
        "schema_version",
        "contract_id",
        "contract_version",
        "work_class",
        "scope",
        "lifecycle_phase",
        "gate",
        "dependent_strata_strategy",
        "area_composition_plan",
        "source_artifacts",
        "source_requirements",
        "source_conflicts",
        "zones",
        "prototype_elements",
        "camera_contract",
        "post_mutation_audit",
        "deviation_records",
        "integrity",
    }
    missing = sorted(required_top_level - set(contract))
    if missing:
        errors.append(f"missing top-level fields: {', '.join(missing)}")

    if schema is not None:
        errors.extend(schema_errors(contract, schema))

    if contract.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")

    gate = _require_mapping(contract.get("gate"), "$.gate", errors)
    strategy = _require_mapping(
        contract.get("dependent_strata_strategy"),
        "$.dependent_strata_strategy",
        errors,
    )
    plan = _require_mapping(
        contract.get("area_composition_plan"), "$.area_composition_plan", errors
    )
    integrity = _require_mapping(contract.get("integrity"), "$.integrity", errors)
    audit = _require_mapping(
        contract.get("post_mutation_audit"), "$.post_mutation_audit", errors
    )

    strategy_applicability = strategy.get("applicability")
    strategy_mode = strategy.get("selected_mode")
    strategy_status = strategy.get("status")
    if strategy.get("consideration_status") != "CONSIDERED":
        errors.append(
            "dependent_strata_strategy.consideration_status must be CONSIDERED"
        )
    if strategy_applicability == "NOT_APPLICABLE":
        if strategy_mode != "NOT_APPLICABLE":
            errors.append(
                "NOT_APPLICABLE dependent-strata strategy must select NOT_APPLICABLE"
            )
        if strategy.get("source_authority") != "NONE":
            errors.append(
                "NOT_APPLICABLE dependent-strata strategy must use source_authority NONE"
            )
        if strategy.get("validation_method") != "NOT_APPLICABLE":
            errors.append(
                "NOT_APPLICABLE dependent-strata strategy must use validation_method NOT_APPLICABLE"
            )
        if strategy_status != "PASS":
            errors.append(
                "NOT_APPLICABLE dependent-strata strategy must have status PASS"
            )
    elif strategy_applicability == "APPLICABLE":
        if strategy_mode == "NOT_APPLICABLE":
            errors.append(
                "APPLICABLE dependent-strata strategy cannot select NOT_APPLICABLE"
            )
        if strategy.get("validation_method") == "NOT_APPLICABLE":
            errors.append(
                "APPLICABLE dependent-strata strategy cannot use validation_method NOT_APPLICABLE"
            )
        if strategy_mode == "VIDEO_DISTANCE_EXCLUSION":
            if strategy.get("source_authority") not in {
                "FINAL_HARDSCAPE_BOUNDS",
                "RECORDED_CONSERVATIVE_FOOTPRINT",
            }:
                errors.append(
                    "VIDEO_DISTANCE_EXCLUSION requires a final or conservative hardscape footprint authority"
                )
            if strategy.get("validation_method") != "FINAL_MESH_BOUNDS_GAP":
                errors.append(
                    "VIDEO_DISTANCE_EXCLUSION requires FINAL_MESH_BOUNDS_GAP validation"
                )
        if strategy_mode in DEPENDENT_STRATA_MODES:
            rejected_modes = set(strategy.get("rejected_modes", []))
            missing_rejections = sorted(DEPENDENT_STRATA_MODES - {strategy_mode} - rejected_modes)
            if missing_rejections:
                errors.append(
                    "dependent_strata_strategy.rejected_modes must record rejected alternatives: "
                    + ", ".join(missing_rejections)
                )
        if strategy_status == "PASS" and strategy_mode == "PENDING_EVIDENCE":
            errors.append(
                "PENDING_EVIDENCE dependent-strata mode cannot have strategy status PASS"
            )
        if strategy_status == "PASS" and strategy.get("validation_method") == "PENDING_EVIDENCE":
            errors.append(
                "PENDING_EVIDENCE validation cannot have strategy status PASS"
            )
    else:
        errors.append(
            "dependent_strata_strategy.applicability must be APPLICABLE or NOT_APPLICABLE"
        )

    sources = _index_unique(
        _require_list(contract.get("source_artifacts"), "$.source_artifacts", errors),
        "source_id",
        "source_artifacts",
        errors,
    )
    requirements = _index_unique(
        _require_list(
            contract.get("source_requirements"), "$.source_requirements", errors
        ),
        "requirement_id",
        "source_requirements",
        errors,
    )
    conflicts = _index_unique(
        _require_list(contract.get("source_conflicts"), "$.source_conflicts", errors),
        "conflict_id",
        "source_conflicts",
        errors,
    )
    zones = _index_unique(
        _require_list(contract.get("zones"), "$.zones", errors),
        "zone_id",
        "zones",
        errors,
    )
    elements = _index_unique(
        _require_list(
            contract.get("prototype_elements"), "$.prototype_elements", errors
        ),
        "prototype_element_id",
        "prototype_elements",
        errors,
    )
    deviations = _index_unique(
        _require_list(
            contract.get("deviation_records"), "$.deviation_records", errors
        ),
        "deviation_id",
        "deviation_records",
        errors,
    )

    if plan.get("status") != "PASS" or gate.get("stage2_plan_status") != "PASS":
        errors.append("Stage 2 Area Composition Plan must be PASS before Stage 2a")

    controlling_by_scope_and_zone: dict[tuple[str, str], list[tuple[int, str]]] = (
        defaultdict(list)
    )
    for source_id, source in sources.items():
        authority_entries = _require_list(
            source.get("authority"), f"source_artifacts[{source_id}].authority", errors
        )
        for authority in authority_entries:
            authority = _require_mapping(
                authority, f"source_artifacts[{source_id}].authority[]", errors
            )
            authority_zones = _check_refs(
                authority.get("zone_ids"),
                set(zones),
                f"source_artifacts[{source_id}].authority[].zone_ids",
                errors,
            )
            if authority.get("controlling") is True:
                if source.get("approval_status") != "APPROVED" or not source.get(
                    "approved_by"
                ):
                    errors.append(
                        f"controlling source {source_id} must be APPROVED with an approver"
                    )
                scope = authority.get("scope")
                priority = authority.get("priority")
                if isinstance(scope, str) and isinstance(priority, int):
                    for zone_id in authority_zones:
                        controlling_by_scope_and_zone[(scope, zone_id)].append(
                            (priority, source_id)
                        )

    for (scope, zone_id), entries in controlling_by_scope_and_zone.items():
        minimum_priority = min(priority for priority, _ in entries)
        top = [source_id for priority, source_id in entries if priority == minimum_priority]
        if len(top) > 1:
            errors.append(
                f"authority scope {scope} in zone {zone_id} has multiple top-priority controlling sources: {top}"
            )

    unresolved_conflicts = []
    for conflict_id, conflict in conflicts.items():
        _check_refs(
            conflict.get("source_ids"),
            set(sources),
            f"source_conflicts[{conflict_id}].source_ids",
            errors,
        )
        controlling = conflict.get("controlling_source_id")
        if controlling is not None and controlling not in sources:
            errors.append(
                f"source_conflicts[{conflict_id}].controlling_source_id is unknown: {controlling}"
            )
        if conflict.get("status") == "UNRESOLVED":
            unresolved_conflicts.append(conflict_id)
        elif not controlling:
            errors.append(f"resolved conflict {conflict_id} requires a controlling source")

    requirement_to_elements: dict[str, set[str]] = defaultdict(set)
    for requirement_id, requirement in requirements.items():
        _check_refs(
            requirement.get("source_artifact_ids"),
            set(sources),
            f"source_requirements[{requirement_id}].source_artifact_ids",
            errors,
        )
        _check_refs(
            requirement.get("zone_ids"),
            set(zones),
            f"source_requirements[{requirement_id}].zone_ids",
            errors,
        )

    zone_requirement_refs: set[str] = set()
    for zone_id, zone in zones.items():
        missing_zone_fields = sorted(REQUIRED_ZONE_FIELDS - set(zone))
        if missing_zone_fields:
            errors.append(
                f"zone {zone_id} is missing contracts: {', '.join(missing_zone_fields)}"
            )
        references = _walk_requirement_refs(zone)
        zone_requirement_refs.update(references)
        for reference in references:
            if reference not in requirements:
                errors.append(f"zone {zone_id} references unknown requirement {reference}")
        _check_ratio_range(
            zone.get("built_footprint_occupancy"),
            f"zones[{zone_id}].built_footprint_occupancy",
            errors,
        )
        _check_ratio_range(
            zone.get("frontage_continuity"),
            f"zones[{zone_id}].frontage_continuity",
            errors,
        )
        for position, typology in enumerate(zone.get("typology_mix", [])):
            share_range = typology.get("share_range") if isinstance(typology, dict) else None
            if isinstance(share_range, dict):
                minimum = share_range.get("min")
                maximum = share_range.get("max")
                if not all(
                    isinstance(item, (int, float)) for item in (minimum, maximum)
                ) or minimum < 0 or maximum > 1:
                    errors.append(
                        f"zones[{zone_id}].typology_mix[{position}].share_range must remain within 0..1"
                    )

    for element_id, element in elements.items():
        _check_refs(
            element.get("zone_ids"),
            set(zones),
            f"prototype_elements[{element_id}].zone_ids",
            errors,
        )
        element_requirements = _check_refs(
            element.get("requirement_ids"),
            set(requirements),
            f"prototype_elements[{element_id}].requirement_ids",
            errors,
        )
        for requirement_id in element_requirements:
            requirement_to_elements[requirement_id].add(element_id)

        realization = _require_mapping(
            element.get("realization"),
            f"prototype_elements[{element_id}].realization",
            errors,
        )
        if element.get("lifecycle_state") == "REALIZED":
            if not realization.get("system"):
                errors.append(f"realized element {element_id} requires realization.system")
            identifiers = realization.get("identifiers")
            if not isinstance(identifiers, list) or not identifiers:
                errors.append(f"realized element {element_id} requires realization.identifiers")
            if realization.get("member_count") is None:
                errors.append(f"realized element {element_id} requires member_count")
        member_keys = realization.get("member_keys")
        member_count = realization.get("member_count")
        if isinstance(member_keys, list) and member_keys and isinstance(member_count, int):
            if len(member_keys) != member_count:
                errors.append(
                    f"element {element_id} member_count {member_count} does not match {len(member_keys)} member_keys"
                )

    missing_zone_bindings = sorted(set(requirements) - zone_requirement_refs)
    if missing_zone_bindings:
        errors.append(
            "source requirements absent from all zone contracts: "
            + ", ".join(missing_zone_bindings)
        )

    orphan_implementation_requirements = sorted(
        requirement_id
        for requirement_id, requirement in requirements.items()
        if requirement.get("trace_policy") == "IMPLEMENTATION_AND_VALIDATION"
        and not requirement_to_elements.get(requirement_id)
    )
    if orphan_implementation_requirements:
        errors.append(
            "implementation requirements without prototype trace: "
            + ", ".join(orphan_implementation_requirements)
        )

    camera_contract = _require_mapping(
        contract.get("camera_contract"), "$.camera_contract", errors
    )
    overview_cameras = _index_unique(
        _require_list(
            camera_contract.get("overview_cameras"),
            "$.camera_contract.overview_cameras",
            errors,
        ),
        "camera_id",
        "overview_cameras",
        errors,
    )
    static_cameras = _index_unique(
        _require_list(
            camera_contract.get("static_player_height_proxies"),
            "$.camera_contract.static_player_height_proxies",
            errors,
        ),
        "camera_id",
        "static_player_height_proxies",
        errors,
    )
    runtime_camera = _require_mapping(
        camera_contract.get("runtime_player_camera"),
        "$.camera_contract.runtime_player_camera",
        errors,
    )
    runtime_camera_id = runtime_camera.get("camera_id")
    camera_ids = set(overview_cameras) | set(static_cameras)
    if isinstance(runtime_camera_id, str):
        if runtime_camera_id in camera_ids:
            errors.append(f"duplicate camera id across authority classes: {runtime_camera_id}")
        camera_ids.add(runtime_camera_id)
    if not overview_cameras:
        errors.append("at least one DIAGNOSTIC_ONLY overview camera is required")
    for camera_id, camera in overview_cameras.items():
        if camera.get("authority") != "DIAGNOSTIC_ONLY":
            errors.append(f"overview camera {camera_id} must be DIAGNOSTIC_ONLY")
        invalid_metrics = set(camera.get("covered_metrics", [])) - OVERVIEW_METRICS
        if invalid_metrics:
            errors.append(
                f"overview camera {camera_id} claims non-macro metrics: {sorted(invalid_metrics)}"
            )
    invalid_player_metrics = set(runtime_camera.get("required_metrics", [])) - PLAYER_METRICS
    if invalid_player_metrics:
        errors.append(
            f"runtime player camera claims invalid metrics: {sorted(invalid_player_metrics)}"
        )

    lifecycle_phase = contract.get("lifecycle_phase")
    audit_status = audit.get("audit_status")
    integrity_audit_status = integrity.get("post_mutation_audit_state")
    if audit_status != integrity_audit_status:
        errors.append(
            "post_mutation_audit.audit_status must equal integrity.post_mutation_audit_state"
        )

    if lifecycle_phase == "PRE_PLACEMENT":
        if audit_status != "NOT_STARTED":
            errors.append("PRE_PLACEMENT contracts must use audit_status NOT_STARTED")
        if deviations:
            errors.append("PRE_PLACEMENT contracts must not contain deviation records")
    elif lifecycle_phase == "POST_MUTATION_AUDIT":
        if not audit.get("batch_id") or not audit.get("prototype_version"):
            errors.append("POST_MUTATION_AUDIT requires batch_id and prototype_version")
        changed_ids = _check_refs(
            audit.get("changed_prototype_element_ids"),
            set(elements),
            "post_mutation_audit.changed_prototype_element_ids",
            errors,
        )
        required_ids = _check_refs(
            audit.get("required_requirement_ids"),
            set(requirements),
            "post_mutation_audit.required_requirement_ids",
            errors,
        )
        changed_requirement_ids = {
            requirement_id
            for element_id in changed_ids
            for requirement_id in elements[element_id].get("requirement_ids", [])
        }
        missing_audit_scope = sorted(changed_requirement_ids - required_ids)
        if missing_audit_scope:
            errors.append(
                "post-mutation audit omits requirements of changed elements: "
                + ", ".join(missing_audit_scope)
            )
        if not deviations:
            errors.append("POST_MUTATION_AUDIT requires deviation_records")
    else:
        errors.append(f"unknown lifecycle_phase: {lifecycle_phase}")

    covered_audit_requirements: set[str] = set()
    any_failed_deviation = False
    for deviation_id, deviation in deviations.items():
        comparison_class = deviation.get("comparison_class")
        camera_id = deviation.get("camera_id")
        if comparison_class == "OVERVIEW_MACRO":
            if camera_id not in overview_cameras:
                errors.append(
                    f"deviation {deviation_id} uses non-overview camera {camera_id} for OVERVIEW_MACRO"
                )
            allowed_metrics = OVERVIEW_METRICS
        elif comparison_class == "RUNTIME_PLAYER":
            if camera_id != runtime_camera_id:
                errors.append(
                    f"deviation {deviation_id} uses camera {camera_id} instead of runtime camera {runtime_camera_id}"
                )
            allowed_metrics = PLAYER_METRICS
        else:
            errors.append(f"deviation {deviation_id} has invalid comparison_class")
            allowed_metrics = set()

        _check_refs(
            deviation.get("source_artifact_ids"),
            set(sources),
            f"deviation_records[{deviation_id}].source_artifact_ids",
            errors,
        )
        if deviation.get("plan_version") != plan.get("version"):
            errors.append(f"deviation {deviation_id} does not use the active plan version")
        if deviation.get("contract_version") != contract.get("contract_version"):
            errors.append(
                f"deviation {deviation_id} does not use the active contract version"
            )
        if lifecycle_phase == "POST_MUTATION_AUDIT" and deviation.get(
            "prototype_version"
        ) != audit.get("prototype_version"):
            errors.append(
                f"deviation {deviation_id} does not use the active prototype version"
            )

        results = _require_list(
            deviation.get("requirement_results"),
            f"deviation_records[{deviation_id}].requirement_results",
            errors,
        )
        result_verdicts: list[str] = []
        for position, result in enumerate(results):
            result = _require_mapping(
                result,
                f"deviation_records[{deviation_id}].requirement_results[{position}]",
                errors,
            )
            requirement_id = result.get("requirement_id")
            if requirement_id not in requirements:
                errors.append(
                    f"deviation {deviation_id} references unknown requirement {requirement_id}"
                )
            elif isinstance(requirement_id, str):
                covered_audit_requirements.add(requirement_id)
            _check_refs(
                result.get("zone_ids"),
                set(zones),
                f"deviation_records[{deviation_id}].requirement_results[{position}].zone_ids",
                errors,
            )
            metric = result.get("metric")
            if metric not in allowed_metrics:
                errors.append(
                    f"deviation {deviation_id} metric {metric} exceeds {comparison_class} authority"
                )
            verdict = result.get("verdict")
            if isinstance(verdict, str):
                result_verdicts.append(verdict)

        overall = deviation.get("overall_status")
        if "FAIL" in result_verdicts and overall != "FAIL":
            errors.append(
                f"deviation {deviation_id} must be FAIL when a requirement result fails"
            )
        if result_verdicts and all(value == "PASS" for value in result_verdicts):
            if overall != "PASS":
                errors.append(
                    f"deviation {deviation_id} must be PASS when every result passes"
                )
        if overall == "FAIL":
            any_failed_deviation = True
            if not deviation.get("reopens_stage"):
                errors.append(f"failed deviation {deviation_id} must reopen a stage")

    if lifecycle_phase == "POST_MUTATION_AUDIT":
        required_ids = set(audit.get("required_requirement_ids", []))
        missing_results = sorted(required_ids - covered_audit_requirements)
        if missing_results:
            errors.append(
                "post-mutation audit lacks deviation results for: "
                + ", ".join(missing_results)
            )
        if any_failed_deviation and audit_status != "FAIL":
            errors.append("a failed deviation requires post_mutation_audit status FAIL")

    gate_status = gate.get("status")
    placement_authorized = gate.get("broad_placement_authorized")
    if gate_status == "PASS":
        if placement_authorized is not True:
            errors.append("Stage 2a PASS must explicitly authorize broad placement")
        if not gate.get("approver") or not gate.get("decision_at"):
            errors.append("Stage 2a PASS requires approver and decision_at")
        if gate.get("blocked_reasons"):
            errors.append("Stage 2a PASS cannot retain blocked_reasons")
    elif placement_authorized is not False:
        errors.append("non-PASS Stage 2a status must keep broad placement locked")

    source_integrity = not unresolved_conflicts and all(
        source.get("approval_status") == "APPROVED"
        for source in sources.values()
        if any(
            authority.get("controlling") is True
            for authority in source.get("authority", [])
            if isinstance(authority, dict)
        )
    )
    expected_integrity = {
        "all_sources_resolved": source_integrity,
        "all_zone_contracts_complete": all(
            REQUIRED_ZONE_FIELDS <= set(zone) for zone in zones.values()
        ),
        "all_implementation_requirements_traced": not orphan_implementation_requirements,
        "all_placement_groups_mapped": all(
            element.get("zone_ids") and element.get("requirement_ids")
            for element in elements.values()
        ),
    }
    for key, expected in expected_integrity.items():
        if integrity.get(key) is not expected:
            errors.append(f"integrity.{key} must be {str(expected).lower()}")

    declared_orphans = set(integrity.get("orphan_requirement_ids", []))
    if declared_orphans != set(orphan_implementation_requirements):
        errors.append(
            "integrity.orphan_requirement_ids must exactly match computed implementation orphans"
        )
    computed_unmapped_elements = {
        element_id
        for element_id, element in elements.items()
        if not element.get("zone_ids") or not element.get("requirement_ids")
    }
    if set(integrity.get("unmapped_prototype_element_ids", [])) != computed_unmapped_elements:
        errors.append(
            "integrity.unmapped_prototype_element_ids must exactly match computed unmapped elements"
        )

    if placement_authorized is True:
        for key in (
            "all_sources_resolved",
            "all_zone_contracts_complete",
            "all_implementation_requirements_traced",
            "all_placement_groups_mapped",
        ):
            if integrity.get(key) is not True:
                errors.append(f"broad placement requires integrity.{key} true")
        if unresolved_conflicts:
            errors.append("broad placement cannot be authorized with unresolved conflicts")
        if strategy_status != "PASS":
            errors.append(
                "broad placement requires dependent_strata_strategy status PASS"
            )
        if lifecycle_phase == "POST_MUTATION_AUDIT" and audit_status != "PASS":
            errors.append(
                "broad placement must remain locked until the post-mutation audit passes"
            )

    _walk_ranges(contract, "$", errors)
    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a Reference-to-Prototype Translation Contract."
    )
    parser.add_argument("contract", type=Path, help="Contract JSON file")
    parser.add_argument(
        "--schema", type=Path, default=DEFAULT_SCHEMA, help="JSON Schema path"
    )
    args = parser.parse_args()

    try:
        schema = load_json(args.schema)
        contract = load_json(args.contract)
    except (OSError, json.JSONDecodeError) as error:
        print(f"INVALID: {error}", file=sys.stderr)
        return 2

    errors = validate_contract(contract, schema)
    if errors:
        print(f"INVALID: {args.contract}", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"VALID: {args.contract}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
