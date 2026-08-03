from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class PrototypeIterationGuidanceTests(unittest.TestCase):
    def test_process_defines_bounded_operation_modes_and_timeout_audit(self):
        chapter = read("skills/reason-about-unreal-development/references/01-development-process.md")
        for phrase in (
            "## Bounded prototype iteration",
            "BOUNDED_PROTO_EDIT",
            "Bounded edit",
            "Diagnostic audit",
            "Promotion review",
            "Maintenance rebuild",
            "operation_verdict",
            "promotion_verdict",
            "NOT_RUN_BY_CONTRACT",
            "protected",
            "120 seconds",
            "read-only state audit",
            "PENDING_EVIDENCE",
        ):
            self.assertIn(phrase, chapter)

    def test_domain_and_ai_skills_repeat_the_latency_guard(self):
        world_skill = read("skills/design-unreal-worlds-and-levels/SKILL.md")
        ai_chapter = read("skills/guide-unreal-ai-development/references/15-ai-assisted-development.md")
        for text in (world_skill, ai_chapter):
            self.assertIn("wall-clock budget", text)
            self.assertIn("read-only state", text)
            self.assertIn("per-item", text)

    def test_bounded_path_is_exposed_by_runtime_skills_and_automation_guidance(self):
        world_skill = read("skills/design-unreal-worlds-and-levels/SKILL.md")
        automation_skill = read("skills/design-unreal-automation-and-pcg/SKILL.md")
        validation_skill = read("skills/validate-unreal-production/SKILL.md")
        for phrase in (
            "BOUNDED_PROTO_EDIT",
            "compact protected snapshot",
            "four-corner grounding",
            "promotion_verdict",
            "NOT_RUN_BY_CONTRACT",
        ):
            self.assertIn(phrase, world_skill)
        for phrase in (
            "compact inspect",
            "in-memory postcondition",
            "persistence re-read",
            "optional/default fields",
            "promotion_verdict",
        ):
            self.assertIn(phrase, automation_skill)
        for phrase in (
            "operation_verdict",
            "promotion_verdict",
            "NOT_RUN_BY_CONTRACT",
            "Direct Landscape",
        ):
            self.assertIn(phrase, validation_skill)

    def test_canonical_guidance_defines_the_fast_transaction_and_protected_exits(self):
        process = read("skills/reason-about-unreal-development/references/01-development-process.md")
        world = read("skills/design-unreal-worlds-and-levels/references/04-world-level-design.md")
        automation = read("skills/design-unreal-automation-and-pcg/references/08-automation-python.md")
        for text in (process, world, automation):
            self.assertIn("BOUNDED_PROTO_EDIT", text)
            self.assertIn("in-memory postcondition", text)
            self.assertRegex(text, r"persistence (?:re-read|verify|read)")
            self.assertIn("protected", text)
        self.assertIn("Landscape", world)
        self.assertIn("zone markers", world)
        self.assertIn("capture", automation)
        self.assertIn("optional fields", automation)

    def test_validation_and_pipeline_separate_workflow_release_from_promotion(self):
        validation = read("skills/validate-unreal-production/references/12-validation-testing-debugging.md")
        pipeline = read("skills/validate-unreal-production/references/13-production-pipeline.md")
        case = read("skills/analyze-unreal-development-cases/references/16-case-studies.md")
        self.assertIn("Operation health and gate-state semantics", validation)
        self.assertIn("Workflow release versus content promotion", pipeline)
        self.assertIn("unbounded prototype loops", case)

    def test_case_study_records_anonymized_bounded_edit_evidence(self):
        case = read("skills/analyze-unreal-development-cases/references/16-case-studies.md")
        for phrase in (
            "gate narrowing",
            "BOUNDED_PROTO_EDIT",
            "target-specific four-corner",
            "operation_verdict",
            "promotion_verdict",
        ):
            self.assertIn(phrase, case)
        for forbidden in ("CodexMiniArena", "WORKFLOW_RELEASED", "MCP tool boundary"):
            self.assertNotIn(forbidden, case)

    def test_case_study_does_not_embed_project_identity_or_tool_contract(self):
        case = read("skills/analyze-unreal-development-cases/references/16-case-studies.md")
        self.assertNotIn("CodexMiniArena", case)
        self.assertNotIn("WORKFLOW_RELEASED", case)
        self.assertNotIn("MCP tool boundary", case)


if __name__ == "__main__":
    unittest.main()
