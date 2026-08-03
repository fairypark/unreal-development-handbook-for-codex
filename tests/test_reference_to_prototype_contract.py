from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from validate_reference_to_prototype_contract import validate_contract  # noqa: E402


SCHEMA_PATH = (
    ROOT
    / "skills"
    / "design-unreal-worlds-and-levels"
    / "references"
    / "reference-to-prototype-translation.schema.json"
)
TEMPLATE_PATH = (
    ROOT
    / "skills"
    / "design-unreal-worlds-and-levels"
    / "references"
    / "reference-to-prototype-translation.template.json"
)


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


class ReferenceToPrototypeContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = load(SCHEMA_PATH)
        cls.template = load(TEMPLATE_PATH)

    def test_schema_local_refs_resolve(self):
        self.assertEqual(
            self.schema["$schema"], "https://json-schema.org/draft/2020-12/schema"
        )
        definitions = self.schema["$defs"]

        def walk(value):
            if isinstance(value, dict):
                reference = value.get("$ref")
                if isinstance(reference, str) and reference.startswith("#/$defs/"):
                    self.assertIn(reference.removeprefix("#/$defs/"), definitions)
                for child in value.values():
                    walk(child)
            elif isinstance(value, list):
                for child in value:
                    walk(child)

        walk(self.schema)

    def test_schema_is_valid_draft_2020_12_when_engine_is_available(self):
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            self.skipTest("jsonschema is not installed; semantic validation still runs")

        Draft202012Validator.check_schema(self.schema)

    def test_execution_contract_entry_points_reference_stage_2a(self):
        entry_points = [
            ROOT / "skills" / "design-unreal-worlds-and-levels" / "SKILL.md",
            ROOT
            / "skills"
            / "design-unreal-worlds-and-levels"
            / "references"
            / "04-world-level-design.md",
            ROOT / "skills" / "validate-unreal-production" / "SKILL.md",
            ROOT
            / "skills"
            / "validate-unreal-production"
            / "references"
            / "12-validation-testing-debugging.md",
            ROOT / "skills" / "guide-unreal-ai-development" / "SKILL.md",
            ROOT
            / "skills"
            / "guide-unreal-ai-development"
            / "references"
            / "15-ai-assisted-development.md",
        ]

        for entry_point in entry_points:
            with self.subTest(entry_point=entry_point):
                text = entry_point.read_text(encoding="utf-8")
                self.assertIn("Stage 2a", text)

    def test_documented_contract_assets_exist(self):
        documented_assets = [
            SCHEMA_PATH,
            TEMPLATE_PATH,
            ROOT / "scripts" / "validate_reference_to_prototype_contract.py",
        ]
        for asset in documented_assets:
            with self.subTest(asset=asset):
                self.assertTrue(asset.is_file())

    def test_generic_template_is_valid_but_locked(self):
        self.assertEqual(validate_contract(self.template, self.schema), [])
        self.assertEqual(self.template["gate"]["status"], "PENDING_EVIDENCE")
        self.assertFalse(self.template["gate"]["broad_placement_authorized"])
        self.assertEqual(
            self.template["dependent_strata_strategy"]["consideration_status"],
            "CONSIDERED",
        )

    def test_video_distance_strategy_requires_explicit_record(self):
        candidate = copy.deepcopy(self.template)
        candidate["dependent_strata_strategy"] = {
            "applicability": "APPLICABLE",
            "consideration_status": "CONSIDERED",
            "selected_mode": "VIDEO_DISTANCE_EXCLUSION",
            "decision_reason": "Stable hardscape output must control grass clearance.",
            "source_authority": "FINAL_HARDSCAPE_BOUNDS",
            "dependency_order": ["GENERATE_ROCKS", "GENERATE_GRASS"],
            "units": "CENTIMETERS",
            "clearance": 20,
            "transition_band": 15,
            "validation_method": "FINAL_MESH_BOUNDS_GAP",
            "source_version": "ROCKS-1.0.0",
            "generation_version": "PCG-1.0.0",
            "target_platform": "PC",
            "evidence_ids": [],
            "rejected_modes": ["MASK_OTHER", "DIRECT_AUTHORED"],
            "status": "PASS",
        }

        self.assertEqual(validate_contract(candidate, self.schema), [])

        candidate["dependent_strata_strategy"]["source_authority"] = "NONE"
        errors = validate_contract(candidate, self.schema)
        self.assertTrue(
            any("final or conservative hardscape footprint authority" in error for error in errors),
            errors,
        )

    def test_broad_placement_requires_strategy_gate_pass(self):
        candidate = self._post_mutation_candidate()
        candidate["dependent_strata_strategy"]["applicability"] = "APPLICABLE"
        candidate["dependent_strata_strategy"]["selected_mode"] = "PENDING_EVIDENCE"
        candidate["dependent_strata_strategy"]["source_authority"] = "NONE"
        candidate["dependent_strata_strategy"]["validation_method"] = "PENDING_EVIDENCE"
        candidate["dependent_strata_strategy"]["status"] = "PENDING_EVIDENCE"

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("broad placement requires dependent_strata_strategy status PASS" in error for error in errors),
            errors,
        )

    def test_non_pass_gate_cannot_authorize_broad_placement(self):
        candidate = copy.deepcopy(self.template)
        candidate["gate"]["broad_placement_authorized"] = True

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("non-PASS Stage 2a status" in error for error in errors), errors
        )

    def test_implementation_requirement_must_trace_to_prototype(self):
        candidate = copy.deepcopy(self.template)
        candidate["prototype_elements"] = [
            element
            for element in candidate["prototype_elements"]
            if element["prototype_element_id"] != "PROTO-TERRAIN-TERRACE"
        ]
        candidate["integrity"]["all_implementation_requirements_traced"] = False
        candidate["integrity"]["orphan_requirement_ids"] = [
            "REQ-ELEVATION-001"
        ]

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("implementation requirements without prototype trace" in error for error in errors),
            errors,
        )

    def test_actor_count_metric_cannot_substitute_for_spatial_audit(self):
        candidate = self._post_mutation_candidate()
        candidate["deviation_records"][0]["requirement_results"][0][
            "metric"
        ] = "ACTOR_COUNT"

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("exceeds OVERVIEW_MACRO authority" in error for error in errors), errors
        )

    def test_post_mutation_failure_requires_lock_and_reopening(self):
        candidate = self._post_mutation_candidate()
        result = candidate["deviation_records"][0]["requirement_results"][0]
        result["verdict"] = "FAIL"
        candidate["deviation_records"][0]["overall_status"] = "FAIL"
        candidate["deviation_records"][0]["reopens_stage"] = "4_TERRAIN_MACRO"
        candidate["post_mutation_audit"]["audit_status"] = "FAIL"
        candidate["integrity"]["post_mutation_audit_state"] = "FAIL"

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("broad placement must remain locked" in error for error in errors), errors
        )

        candidate["gate"].update(
            {
                "status": "FAIL",
                "broad_placement_authorized": False,
                "blocked_reasons": [
                    "REQ-ELEVATION-001 exceeded tolerance; Stage 4 reopened."
                ],
            }
        )
        self.assertEqual(validate_contract(candidate, self.schema), [])

    def _post_mutation_candidate(self):
        candidate = copy.deepcopy(self.template)
        candidate["lifecycle_phase"] = "POST_MUTATION_AUDIT"
        candidate["gate"].update(
            {
                "status": "PASS",
                "broad_placement_authorized": True,
                "approver": "DESIGNATED_APPROVER",
                "decision_at": "2026-01-01T00:00:00Z",
                "blocked_reasons": [],
            }
        )
        candidate["post_mutation_audit"] = {
            "batch_id": "BATCH-TERRAIN-001",
            "prototype_version": "0.2.0",
            "changed_prototype_element_ids": [
                "PROTO-TERRAIN-TERRACE"
            ],
            "required_requirement_ids": [
                "REQ-ELEVATION-001"
            ],
            "audit_status": "PASS"
        }
        candidate["integrity"]["post_mutation_audit_state"] = "PASS"
        candidate["deviation_records"] = [
            {
                "deviation_id": "DEVIATION-TERRAIN-001",
                "comparison_class": "OVERVIEW_MACRO",
                "camera_id": "CAM-OVERVIEW-001",
                "fixed_condition_id": "COND-OVERVIEW-001",
                "source_artifact_ids": [
                    "SRC-ELEVATION-001"
                ],
                "plan_version": "1.0.0",
                "contract_version": "0.1.0",
                "prototype_version": "0.2.0",
                "reference_evidence_id": "EVIDENCE-REFERENCE-001",
                "plan_evidence_id": "EVIDENCE-PLAN-001",
                "prototype_evidence_id": "EVIDENCE-PROTOTYPE-001",
                "requirement_results": [
                    {
                        "requirement_id": "REQ-ELEVATION-001",
                        "zone_ids": [
                            "ZONE-ALPHA"
                        ],
                        "metric": "HEIGHT_BANDS",
                        "planned": "2.0m to 5.0m relative rise",
                        "observed": "3.0m relative rise",
                        "allowed_deviation": "Within the approved range",
                        "evidence_ids": [
                            "EVIDENCE-REFERENCE-001",
                            "EVIDENCE-PLAN-001",
                            "EVIDENCE-PROTOTYPE-001"
                        ],
                        "verdict": "PASS",
                        "reviewer": "DESIGNATED_REVIEWER"
                    }
                ],
                "overall_status": "PASS",
                "baseline_deviation_id": None,
                "reopens_stage": None
            }
        ]
        return candidate


if __name__ == "__main__":
    unittest.main()
