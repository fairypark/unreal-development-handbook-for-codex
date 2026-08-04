from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from validate_concept_to_asset_readiness import validate_contract  # noqa: E402


SKILL_ROOT = ROOT / "skills" / "design-unreal-content-architecture"
SCHEMA_PATH = SKILL_ROOT / "references" / "concept-to-asset-readiness.schema.json"
TEMPLATE_PATH = SKILL_ROOT / "references" / "concept-to-asset-readiness.template.json"


def load(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


class ConceptToAssetReadinessTests(unittest.TestCase):
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

    def test_documented_assets_exist(self):
        documented_assets = [
            SCHEMA_PATH,
            TEMPLATE_PATH,
            ROOT / "scripts" / "validate_concept_to_asset_readiness.py",
        ]
        for asset in documented_assets:
            with self.subTest(asset=asset):
                self.assertTrue(asset.is_file())

    def test_plugin_entry_points_reference_stage_2b(self):
        entry_points = [
            ROOT / "README.md",
            ROOT
            / "skills"
            / "reason-about-unreal-development"
            / "references"
            / "01-development-process.md",
            ROOT / "skills" / "design-unreal-worlds-and-levels" / "SKILL.md",
            ROOT
            / "skills"
            / "design-unreal-worlds-and-levels"
            / "references"
            / "04-world-level-design.md",
            SKILL_ROOT / "SKILL.md",
            SKILL_ROOT / "references" / "05-content-asset-architecture.md",
            ROOT / "skills" / "validate-unreal-production" / "SKILL.md",
            ROOT
            / "skills"
            / "validate-unreal-production"
            / "references"
            / "12-validation-testing-debugging.md",
            ROOT
            / "skills"
            / "validate-unreal-production"
            / "references"
            / "13-production-pipeline.md",
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
                self.assertIn("Concept-to-Asset Readiness", text)

    def test_template_is_valid_but_all_gates_are_locked(self):
        self.assertEqual(validate_contract(self.template, self.schema), [])
        for gate in self.template["gates"].values():
            self.assertEqual(gate["status"], "PENDING_EVIDENCE")
            self.assertFalse(gate["authorized"])
        self.assertEqual(
            self.template["integrity"]["unresolved_compatibility_candidate_ids"],
            ["CANDIDATE-PROJECT-KIT-001"],
        )
        self.assertEqual(
            self.template["integrity"]["unresolved_license_candidate_ids"],
            ["CANDIDATE-PROJECT-KIT-001"],
        )

    def test_asset_plan_can_pass_without_pretending_assets_are_ready(self):
        candidate = copy.deepcopy(self.template)
        candidate["gates"]["asset_plan_ready"].update(
            {
                "status": "PASS",
                "authorized": True,
                "approver": "DESIGNATED-APPROVER",
                "decision_at": "2026-01-01T00:00:00Z",
                "blocked_reasons": [],
            }
        )

        self.assertEqual(validate_contract(candidate, self.schema), [])
        self.assertEqual(
            candidate["demand_coverage"][0]["status"], "CANDIDATE_IDENTIFIED"
        )
        self.assertFalse(candidate["gates"]["visual_slice_ready"]["authorized"])

    def test_public_listing_or_download_does_not_prove_ownership(self):
        candidate = copy.deepcopy(self.template)
        asset = candidate["candidates"][0]
        asset["provider_type"] = "NEW_MARKETPLACE"
        asset["entitlement"] = {
            "status": "UNCONFIRMED",
            "evidence_id": None,
            "checked_at": None,
        }
        asset["acquisition"] = {
            "status": "ACQUIRED_TO_STAGING",
            "authorization_reference": "AUTH-ACQUISITION-001",
            "acquired_at": "2026-01-01T00:00:00Z",
            "staging_locator": "STAGING-PACKAGE-001",
        }
        asset["readiness_state"] = "ACQUIRED_TO_STAGING"

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("cannot advance without confirmed entitlement" in error for error in errors),
            errors,
        )

    def test_external_acquisition_requires_explicit_authorization_record(self):
        candidate = copy.deepcopy(self.template)
        asset = candidate["candidates"][0]
        asset["provider_type"] = "NEW_MARKETPLACE"
        asset["entitlement"] = {
            "status": "CONFIRMED",
            "evidence_id": "EVIDENCE-ENTITLEMENT-001",
            "checked_at": "2026-01-01T00:00:00Z",
        }
        asset["acquisition"] = {
            "status": "ACQUIRED_TO_STAGING",
            "authorization_reference": None,
            "acquired_at": "2026-01-01T00:00:00Z",
            "staging_locator": "STAGING-PACKAGE-001",
        }
        asset["readiness_state"] = "ACQUIRED_TO_STAGING"

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("requires an authorization_reference" in error for error in errors),
            errors,
        )

    def test_visual_slice_gate_rejects_discovered_candidate(self):
        candidate = copy.deepcopy(self.template)
        candidate["gates"]["visual_slice_ready"].update(
            {
                "status": "PASS",
                "authorized": True,
                "approver": "DESIGNATED-APPROVER",
                "decision_at": "2026-01-01T00:00:00Z",
                "blocked_reasons": [],
            }
        )

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("requires representative coverage" in error for error in errors),
            errors,
        )
        self.assertTrue(
            any("unresolved compatibility" in error for error in errors), errors
        )

    def test_production_ready_contract_can_pass_all_gates(self):
        candidate = self._production_ready_candidate()

        self.assertEqual(validate_contract(candidate, self.schema), [])

    def test_production_gate_rejects_unresolved_license(self):
        candidate = self._production_ready_candidate()
        candidate["candidates"][0]["license"]["status"] = "PENDING"
        candidate["candidates"][0]["license"]["license_name_or_id"] = (
            "PENDING-LICENSE-REVIEW"
        )
        candidate["integrity"]["unresolved_license_candidate_ids"] = [
            "CANDIDATE-PROJECT-KIT-001"
        ]

        errors = validate_contract(candidate, self.schema)

        self.assertTrue(
            any("requires resolved license evidence" in error for error in errors),
            errors,
        )
        self.assertTrue(
            any("cannot pass with unresolved licenses" in error for error in errors),
            errors,
        )

    def _production_ready_candidate(self):
        candidate = copy.deepcopy(self.template)
        asset = candidate["candidates"][0]
        asset["compatibility"] = {
            "status": "PASS",
            "engine_versions": ["PROJECT-ENGINE-VERSION"],
            "target_platforms": ["PC"],
            "required_plugins": [],
            "dependency_ids": [],
            "integration_risks": [],
            "evidence_ids": ["EVIDENCE-COMPATIBILITY-001"],
        }
        asset["license"] = {
            "status": "VERIFIED",
            "license_name_or_id": "PROJECT-PROVENANCE-REVIEWED",
            "terms_version_or_acquired_at": "2026-01-01T00:00:00Z",
            "intended_scope": "Use within the declared project scope.",
            "restrictions": [],
            "evidence_id": "EVIDENCE-LICENSE-001",
        }
        asset["evaluation"] = {
            "status": "PASS",
            "visual_fit": "PASS",
            "scale_and_pivot": "PASS",
            "family_completeness": "PASS",
            "materials": "PASS",
            "collision_and_navigation": "PASS",
            "lod_nanite_and_performance": "PASS",
            "reverse_side_and_contacts": "PASS",
            "ordinary_repetition": "PASS",
            "evidence_ids": ["EVIDENCE-REPRESENTATIVE-001"],
        }
        asset["readiness_state"] = "PRODUCTION_APPROVED"
        asset["production_evidence_ids"] = ["EVIDENCE-PRODUCTION-001"]

        candidate["demand_coverage"][0].update(
            {
                "status": "PRODUCTION_READY",
                "gap_reason": None,
                "evidence_ids": [
                    "EVIDENCE-REPRESENTATIVE-001",
                    "EVIDENCE-PRODUCTION-001",
                ],
            }
        )
        candidate["acquisition_actions"][0]["status"] = "PASS"
        candidate["acquisition_actions"][0]["evidence_ids"] = [
            "EVIDENCE-REPRESENTATIVE-001"
        ]

        for gate in candidate["gates"].values():
            gate.update(
                {
                    "status": "PASS",
                    "authorized": True,
                    "approver": "DESIGNATED-APPROVER",
                    "decision_at": "2026-01-01T00:00:00Z",
                    "blocked_reasons": [],
                }
            )

        candidate["integrity"].update(
            {
                "unresolved_compatibility_candidate_ids": [],
                "unresolved_license_candidate_ids": [],
                "non_production_ready_demand_ids": [],
            }
        )
        return candidate


if __name__ == "__main__":
    unittest.main()
