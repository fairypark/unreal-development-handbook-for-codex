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
            "Bounded edit",
            "Diagnostic audit",
            "Promotion review",
            "Maintenance rebuild",
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

    def test_validation_and_pipeline_separate_workflow_release_from_promotion(self):
        validation = read("skills/validate-unreal-production/references/12-validation-testing-debugging.md")
        pipeline = read("skills/validate-unreal-production/references/13-production-pipeline.md")
        case = read("skills/analyze-unreal-development-cases/references/16-case-studies.md")
        self.assertIn("Operation health and gate-state semantics", validation)
        self.assertIn("Workflow release versus content promotion", pipeline)
        self.assertIn("unbounded prototype loops", case)

    def test_case_study_does_not_embed_project_identity_or_tool_contract(self):
        case = read("skills/analyze-unreal-development-cases/references/16-case-studies.md")
        self.assertNotIn("CodexMiniArena", case)
        self.assertNotIn("WORKFLOW_RELEASED", case)
        self.assertNotIn("MCP tool boundary", case)


if __name__ == "__main__":
    unittest.main()
