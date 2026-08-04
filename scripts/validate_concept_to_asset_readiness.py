#!/usr/bin/env python3
"""Validate a Concept-to-Asset Readiness Contract.

The JSON Schema owns portable shape validation. This script adds referential,
readiness-state, authorization, coverage, and staged-gate semantics that are
awkward to express in JSON Schema alone. Semantic checks use only the Python
standard library; JSON Schema validation runs when ``jsonschema`` is installed.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = (
    ROOT
    / "skills"
    / "design-unreal-content-architecture"
    / "references"
    / "concept-to-asset-readiness.schema.json"
)

ACQUIRED_OR_LATER = {
    "ACQUIRED_TO_STAGING",
    "REPRESENTATIVE_APPROVED",
    "PRODUCTION_APPROVED",
}
REPRESENTATIVE_READY_STATES = {
    "REPRESENTATIVE_APPROVED",
    "PRODUCTION_APPROVED",
}
EXTERNAL_AUTHORIZATION_TYPES = {
    "NEW_MARKETPLACE",
    "OUTSOURCE",
}
TERMINAL_ACTION_STATES = {
    "PASS",
    "NOT_APPLICABLE",
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
            errors.append(f"duplicate {label} identifier: {identifier}")
            continue
        indexed[identifier] = record
    return indexed


def _check_refs(
    values: Any, known: set[str], label: str, errors: list[str]
) -> set[str]:
    valid: set[str] = set()
    for value in _require_list(values, label, errors):
        if not isinstance(value, str):
            errors.append(f"{label} contains a non-string reference")
        elif value not in known:
            errors.append(f"{label} references unknown identifier: {value}")
        else:
            valid.add(value)
    return valid


def _declared_set(value: Any, label: str, errors: list[str]) -> set[str]:
    declared: set[str] = set()
    for item in _require_list(value, label, errors):
        if isinstance(item, str):
            declared.add(item)
        else:
            errors.append(f"{label} contains a non-string identifier")
    return declared


def _check_integrity_set(
    integrity: dict[str, Any], key: str, expected: set[str], errors: list[str]
) -> None:
    declared = _declared_set(integrity.get(key), f"integrity.{key}", errors)
    if declared != expected:
        errors.append(
            f"integrity.{key} must exactly match computed values: {sorted(expected)}"
        )


def _gate_base_checks(
    label: str,
    gate: dict[str, Any],
    demand_ids: set[str],
    candidate_ids: set[str],
    errors: list[str],
) -> tuple[set[str], set[str]]:
    scope_demands = _check_refs(
        gate.get("scope_demand_ids"), demand_ids, f"gates.{label}.scope_demand_ids", errors
    )
    scope_candidates = _check_refs(
        gate.get("scope_candidate_ids"),
        candidate_ids,
        f"gates.{label}.scope_candidate_ids",
        errors,
    )
    status = gate.get("status")
    authorized = gate.get("authorized")
    if status == "PASS":
        if authorized is not True:
            errors.append(f"{label} PASS must explicitly set authorized true")
        if not gate.get("approver") or not gate.get("decision_at"):
            errors.append(f"{label} PASS requires approver and decision_at")
        if gate.get("blocked_reasons"):
            errors.append(f"{label} PASS cannot retain blocked_reasons")
    elif authorized is not False:
        errors.append(f"non-PASS {label} must keep authorized false")
    return scope_demands, scope_candidates


def validate_contract(contract: Any, schema: dict[str, Any]) -> list[str]:
    errors = schema_errors(contract, schema)
    contract = _require_mapping(contract, "$", errors)

    source = _require_mapping(contract.get("source_context"), "$.source_context", errors)
    source_requirement_ids = set(
        value
        for value in _require_list(
            source.get("source_requirement_ids"),
            "$.source_context.source_requirement_ids",
            errors,
        )
        if isinstance(value, str)
    )
    source_zone_ids = set(
        value
        for value in _require_list(
            source.get("zone_ids"), "$.source_context.zone_ids", errors
        )
        if isinstance(value, str)
    )

    demands = _index_unique(
        _require_list(contract.get("asset_demands"), "$.asset_demands", errors),
        "demand_id",
        "asset_demands",
        errors,
    )
    candidates = _index_unique(
        _require_list(contract.get("candidates"), "$.candidates", errors),
        "candidate_id",
        "candidates",
        errors,
    )
    coverage = _index_unique(
        _require_list(contract.get("demand_coverage"), "$.demand_coverage", errors),
        "demand_id",
        "demand_coverage",
        errors,
    )
    actions = _index_unique(
        _require_list(
            contract.get("acquisition_actions"), "$.acquisition_actions", errors
        ),
        "action_id",
        "acquisition_actions",
        errors,
    )

    demand_ids = set(demands)
    candidate_ids = set(candidates)

    valid_candidate_demand_refs: dict[str, set[str]] = {}
    for demand_id, demand in demands.items():
        _check_refs(
            demand.get("source_requirement_ids"),
            source_requirement_ids,
            f"asset_demands[{demand_id}].source_requirement_ids",
            errors,
        )
        _check_refs(
            demand.get("zone_ids"),
            source_zone_ids,
            f"asset_demands[{demand_id}].zone_ids",
            errors,
        )
        quantity = _require_mapping(
            demand.get("quantity_model"),
            f"asset_demands[{demand_id}].quantity_model",
            errors,
        )
        instance_range = _require_mapping(
            quantity.get("expected_instances"),
            f"asset_demands[{demand_id}].quantity_model.expected_instances",
            errors,
        )
        minimum = instance_range.get("min")
        maximum = instance_range.get("max")
        if isinstance(minimum, int) and isinstance(maximum, int) and minimum > maximum:
            errors.append(
                f"asset demand {demand_id} expected_instances min exceeds max"
            )

    for candidate_id, candidate in candidates.items():
        candidate_demands = _check_refs(
            candidate.get("demand_ids"),
            demand_ids,
            f"candidates[{candidate_id}].demand_ids",
            errors,
        )
        valid_candidate_demand_refs[candidate_id] = candidate_demands

        entitlement = _require_mapping(
            candidate.get("entitlement"), f"candidates[{candidate_id}].entitlement", errors
        )
        acquisition = _require_mapping(
            candidate.get("acquisition"), f"candidates[{candidate_id}].acquisition", errors
        )
        license_record = _require_mapping(
            candidate.get("license"), f"candidates[{candidate_id}].license", errors
        )
        compatibility = _require_mapping(
            candidate.get("compatibility"),
            f"candidates[{candidate_id}].compatibility",
            errors,
        )
        evaluation = _require_mapping(
            candidate.get("evaluation"), f"candidates[{candidate_id}].evaluation", errors
        )

        provider_type = candidate.get("provider_type")
        readiness = candidate.get("readiness_state")
        entitlement_status = entitlement.get("status")
        acquisition_status = acquisition.get("status")

        if entitlement_status in {"PROJECT_OWNED", "CONFIRMED"}:
            if not entitlement.get("evidence_id") or not entitlement.get("checked_at"):
                errors.append(
                    f"candidate {candidate_id} verified entitlement requires evidence_id and checked_at"
                )
        if provider_type == "OWNED_MARKETPLACE" and readiness not in {
            "DISCOVERED",
            "REJECTED",
            "BLOCKED",
        }:
            if entitlement_status != "CONFIRMED":
                errors.append(
                    f"owned-marketplace candidate {candidate_id} requires confirmed entitlement"
                )
        if provider_type == "NEW_MARKETPLACE" and readiness not in {
            "DISCOVERED",
            "REJECTED",
            "BLOCKED",
        }:
            if entitlement_status != "CONFIRMED":
                errors.append(
                    f"new-marketplace candidate {candidate_id} cannot advance without confirmed entitlement"
                )

        if provider_type in EXTERNAL_AUTHORIZATION_TYPES and acquisition_status in {
            "AUTHORIZED",
            "ACQUIRED_TO_STAGING",
        }:
            if not acquisition.get("authorization_reference"):
                errors.append(
                    f"external candidate {candidate_id} requires an authorization_reference"
                )

        if readiness in {
            "OWNERSHIP_VERIFIED",
            "ACQUIRED_TO_STAGING",
            "REPRESENTATIVE_APPROVED",
            "PRODUCTION_APPROVED",
        } and entitlement_status == "UNCONFIRMED":
            errors.append(
                f"candidate {candidate_id} cannot use readiness {readiness} with unconfirmed entitlement"
            )

        if readiness in ACQUIRED_OR_LATER:
            if acquisition_status not in {"NOT_REQUIRED", "ACQUIRED_TO_STAGING"}:
                errors.append(
                    f"candidate {candidate_id} readiness {readiness} requires acquisition to staging or a declared NOT_REQUIRED path"
                )
            if not acquisition.get("staging_locator"):
                errors.append(
                    f"candidate {candidate_id} readiness {readiness} requires a staging_locator"
                )

        if readiness in REPRESENTATIVE_READY_STATES:
            if license_record.get("status") not in {"VERIFIED", "NOT_APPLICABLE"}:
                errors.append(
                    f"candidate {candidate_id} readiness {readiness} requires resolved license evidence"
                )
            if compatibility.get("status") != "PASS":
                errors.append(
                    f"candidate {candidate_id} readiness {readiness} requires compatibility PASS"
                )
            if evaluation.get("status") != "PASS" or not evaluation.get("evidence_ids"):
                errors.append(
                    f"candidate {candidate_id} readiness {readiness} requires evaluated evidence and PASS"
                )

        if readiness == "PRODUCTION_APPROVED" and not candidate.get(
            "production_evidence_ids"
        ):
            errors.append(
                f"production-approved candidate {candidate_id} requires production_evidence_ids"
            )
        if readiness in {"REJECTED", "BLOCKED"} and not candidate.get(
            "rejection_reason"
        ):
            errors.append(f"candidate {candidate_id} {readiness} requires a reason")

    action_ids_by_demand: dict[str, set[str]] = {demand_id: set() for demand_id in demands}
    for action_id, action in actions.items():
        action_demands = _check_refs(
            action.get("demand_ids"),
            demand_ids,
            f"acquisition_actions[{action_id}].demand_ids",
            errors,
        )
        for demand_id in action_demands:
            action_ids_by_demand[demand_id].add(action_id)
        candidate_id = action.get("candidate_id")
        if candidate_id is not None:
            if candidate_id not in candidates:
                errors.append(
                    f"acquisition action {action_id} references unknown candidate {candidate_id}"
                )
            else:
                unsupported = action_demands - valid_candidate_demand_refs[candidate_id]
                if unsupported:
                    errors.append(
                        f"acquisition action {action_id} binds candidate {candidate_id} to unsupported demands: {sorted(unsupported)}"
                    )

    selected_candidate_ids: set[str] = set()
    for demand_id, decision in coverage.items():
        if demand_id not in demands:
            errors.append(f"demand_coverage references unknown demand: {demand_id}")
            continue
        selected = _check_refs(
            decision.get("selected_candidate_ids"),
            candidate_ids,
            f"demand_coverage[{demand_id}].selected_candidate_ids",
            errors,
        )
        selected_candidate_ids.update(selected)
        for candidate_id in selected:
            if demand_id not in valid_candidate_demand_refs[candidate_id]:
                errors.append(
                    f"coverage for {demand_id} selects candidate {candidate_id} that does not declare the demand"
                )

        status = decision.get("status")
        if status == "PLANNED_GAP":
            if selected:
                errors.append(f"planned gap {demand_id} cannot select a candidate")
            if not decision.get("gap_reason") or not action_ids_by_demand[demand_id]:
                errors.append(
                    f"planned gap {demand_id} requires a gap reason and at least one planned action"
                )
        elif status == "CANDIDATE_IDENTIFIED" and not selected:
            errors.append(f"candidate-identified demand {demand_id} requires a candidate")
        elif status == "REPRESENTATIVE_READY":
            if not selected or any(
                candidates[candidate_id].get("readiness_state")
                not in REPRESENTATIVE_READY_STATES
                for candidate_id in selected
            ):
                errors.append(
                    f"representative-ready demand {demand_id} requires only representative- or production-approved candidates"
                )
        elif status == "PRODUCTION_READY":
            if not selected or any(
                candidates[candidate_id].get("readiness_state")
                != "PRODUCTION_APPROVED"
                for candidate_id in selected
            ):
                errors.append(
                    f"production-ready demand {demand_id} requires only production-approved candidates"
                )
        elif status == "WAIVED":
            if selected:
                errors.append(f"waived demand {demand_id} cannot select candidates")
            if not isinstance(decision.get("waiver"), dict):
                errors.append(f"waived demand {demand_id} requires waiver evidence")
        elif status == "BLOCKED" and not decision.get("gap_reason"):
            errors.append(f"blocked demand {demand_id} requires a gap reason")
        if status != "WAIVED" and decision.get("waiver") is not None:
            errors.append(f"non-waived demand {demand_id} cannot retain waiver evidence")

    uncovered_demand_ids = demand_ids - set(coverage)
    extra_coverage_ids = set(coverage) - demand_ids
    if extra_coverage_ids:
        errors.append(f"coverage contains unknown demands: {sorted(extra_coverage_ids)}")

    gates = _require_mapping(contract.get("gates"), "$.gates", errors)
    asset_plan_gate = _require_mapping(
        gates.get("asset_plan_ready"), "$.gates.asset_plan_ready", errors
    )
    visual_gate = _require_mapping(
        gates.get("visual_slice_ready"), "$.gates.visual_slice_ready", errors
    )
    production_gate = _require_mapping(
        gates.get("production_dressing_ready"),
        "$.gates.production_dressing_ready",
        errors,
    )

    plan_scope_demands, plan_scope_candidates = _gate_base_checks(
        "ASSET_PLAN_READY", asset_plan_gate, demand_ids, candidate_ids, errors
    )
    visual_scope_demands, visual_scope_candidates = _gate_base_checks(
        "VISUAL_SLICE_READY", visual_gate, demand_ids, candidate_ids, errors
    )
    production_scope_demands, production_scope_candidates = _gate_base_checks(
        "PRODUCTION_DRESSING_READY", production_gate, demand_ids, candidate_ids, errors
    )

    active_demands = {
        demand_id
        for demand_id, demand in demands.items()
        if demand.get("status") != "WAIVED"
    }
    visual_required = {
        demand_id
        for demand_id, demand in demands.items()
        if demand.get("required_for_visual_slice") is True
        and demand.get("status") != "WAIVED"
    }
    production_required = {
        demand_id
        for demand_id, demand in demands.items()
        if demand.get("required_for_production_dressing") is True
        and demand.get("status") != "WAIVED"
    }

    if asset_plan_gate.get("status") == "PASS":
        if not active_demands <= plan_scope_demands:
            errors.append("ASSET_PLAN_READY scope must include every active demand")
        for demand_id in active_demands:
            strategy = _require_mapping(
                demands[demand_id].get("sourcing_strategy"),
                f"asset_demands[{demand_id}].sourcing_strategy",
                errors,
            )
            decision = coverage.get(demand_id, {})
            if strategy.get("mode") == "UNDECIDED":
                errors.append(f"ASSET_PLAN_READY cannot pass with undecided demand {demand_id}")
            if decision.get("status") in {None, "UNPLANNED", "BLOCKED"}:
                errors.append(
                    f"ASSET_PLAN_READY cannot pass with unplanned or blocked demand {demand_id}"
                )

    if visual_gate.get("status") == "PASS":
        if not visual_required <= visual_scope_demands:
            errors.append("VISUAL_SLICE_READY scope omits required visual-slice demands")
        for demand_id in visual_required:
            status = coverage.get(demand_id, {}).get("status")
            if status not in {"REPRESENTATIVE_READY", "PRODUCTION_READY", "WAIVED"}:
                errors.append(
                    f"VISUAL_SLICE_READY requires representative coverage for {demand_id}"
                )
        expected_visual_candidates = {
            candidate_id
            for demand_id in visual_scope_demands
            for candidate_id in coverage.get(demand_id, {}).get(
                "selected_candidate_ids", []
            )
        }
        if not expected_visual_candidates <= visual_scope_candidates:
            errors.append("VISUAL_SLICE_READY scope omits selected candidates")
        for action in actions.values():
            if (
                action.get("candidate_id") in visual_scope_candidates
                and action.get("due_before_gate")
                in {"ASSET_PLAN_READY", "VISUAL_SLICE_READY"}
                and action.get("status") not in TERMINAL_ACTION_STATES
            ):
                errors.append(
                    f"VISUAL_SLICE_READY has incomplete action {action.get('action_id')}"
                )

    if production_gate.get("status") == "PASS":
        if not production_required <= production_scope_demands:
            errors.append(
                "PRODUCTION_DRESSING_READY scope omits required production demands"
            )
        for demand_id in production_required:
            status = coverage.get(demand_id, {}).get("status")
            if status not in {"PRODUCTION_READY", "WAIVED"}:
                errors.append(
                    f"PRODUCTION_DRESSING_READY requires production coverage for {demand_id}"
                )
        expected_production_candidates = {
            candidate_id
            for demand_id in production_scope_demands
            for candidate_id in coverage.get(demand_id, {}).get(
                "selected_candidate_ids", []
            )
        }
        if not expected_production_candidates <= production_scope_candidates:
            errors.append("PRODUCTION_DRESSING_READY scope omits selected candidates")
        for action in actions.values():
            if (
                action.get("candidate_id") in production_scope_candidates
                and action.get("status") not in TERMINAL_ACTION_STATES
            ):
                errors.append(
                    f"PRODUCTION_DRESSING_READY has incomplete action {action.get('action_id')}"
                )

    orphan_candidate_ids = {
        candidate_id
        for candidate_id, refs in valid_candidate_demand_refs.items()
        if not refs
    }
    unresolved_license_candidate_ids = {
        candidate_id
        for candidate_id in selected_candidate_ids
        if candidates[candidate_id].get("readiness_state") not in {"REJECTED", "BLOCKED"}
        and _require_mapping(
            candidates[candidate_id].get("license"),
            f"candidates[{candidate_id}].license",
            errors,
        ).get("status")
        not in {"VERIFIED", "NOT_APPLICABLE"}
    }
    unresolved_compatibility_candidate_ids = {
        candidate_id
        for candidate_id in selected_candidate_ids
        if candidates[candidate_id].get("readiness_state") not in {"REJECTED", "BLOCKED"}
        and _require_mapping(
            candidates[candidate_id].get("compatibility"),
            f"candidates[{candidate_id}].compatibility",
            errors,
        ).get("status")
        != "PASS"
    }
    unauthorized_external_candidate_ids = {
        candidate_id
        for candidate_id in selected_candidate_ids
        if candidates[candidate_id].get("provider_type")
        in EXTERNAL_AUTHORIZATION_TYPES
        and _require_mapping(
            candidates[candidate_id].get("acquisition"),
            f"candidates[{candidate_id}].acquisition",
            errors,
        ).get("status")
        not in {"AUTHORIZED", "ACQUIRED_TO_STAGING"}
    }
    non_production_ready_demand_ids = {
        demand_id
        for demand_id in production_required
        if coverage.get(demand_id, {}).get("status")
        not in {"PRODUCTION_READY", "WAIVED"}
    }

    integrity = _require_mapping(contract.get("integrity"), "$.integrity", errors)
    _check_integrity_set(
        integrity, "orphan_candidate_ids", orphan_candidate_ids, errors
    )
    _check_integrity_set(
        integrity, "uncovered_demand_ids", uncovered_demand_ids, errors
    )
    _check_integrity_set(
        integrity,
        "unresolved_license_candidate_ids",
        unresolved_license_candidate_ids,
        errors,
    )
    _check_integrity_set(
        integrity,
        "unresolved_compatibility_candidate_ids",
        unresolved_compatibility_candidate_ids,
        errors,
    )
    _check_integrity_set(
        integrity,
        "unauthorized_external_candidate_ids",
        unauthorized_external_candidate_ids,
        errors,
    )
    _check_integrity_set(
        integrity,
        "non_production_ready_demand_ids",
        non_production_ready_demand_ids,
        errors,
    )

    if visual_gate.get("status") == "PASS":
        if unresolved_license_candidate_ids & visual_scope_candidates:
            errors.append("VISUAL_SLICE_READY cannot pass with unresolved licenses")
        if unresolved_compatibility_candidate_ids & visual_scope_candidates:
            errors.append("VISUAL_SLICE_READY cannot pass with unresolved compatibility")
        if unauthorized_external_candidate_ids & visual_scope_candidates:
            errors.append(
                "VISUAL_SLICE_READY cannot pass with unauthorized external candidates"
            )
    if production_gate.get("status") == "PASS":
        if unresolved_license_candidate_ids & production_scope_candidates:
            errors.append(
                "PRODUCTION_DRESSING_READY cannot pass with unresolved licenses"
            )
        if unresolved_compatibility_candidate_ids & production_scope_candidates:
            errors.append(
                "PRODUCTION_DRESSING_READY cannot pass with unresolved compatibility"
            )
        if unauthorized_external_candidate_ids & production_scope_candidates:
            errors.append(
                "PRODUCTION_DRESSING_READY cannot pass with unauthorized external candidates"
            )

    return sorted(set(errors))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a Concept-to-Asset Readiness Contract."
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
