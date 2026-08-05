from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class HandbookImprovementTests(unittest.TestCase):
    def test_mesh_terrain_review_precedes_broad_landscape_guidance(self):
        chapter = read(
            "skills/design-unreal-worlds-and-levels/references/04-world-level-design.md"
        )
        skill = read("skills/design-unreal-worlds-and-levels/SKILL.md")
        for text in (chapter, skill):
            self.assertIn("Terrain Representation Review", text)
            self.assertIn("Mesh Terrain", text)
        for state in (
            "PENDING_EVIDENCE",
            "NOT_SUPPORTED",
            "LANDSCAPE_RECOMMENDED",
            "MESH_TERRAIN_RECOMMENDED",
            "USER_DECISION_REQUIRED",
        ):
            self.assertIn(state, chapter)
        self.assertLess(
            chapter.index("### Terrain representation review"),
            chapter.index("### 4. Terrain and macro blockout"),
        )
        self.assertIn("support is evidence for comparison, not permission to select it", skill)
        self.assertIn("Broad terrain mutation remains locked", chapter)

    def test_bidirectional_terrain_pcg_contract_is_routed(self):
        chapter = read(
            "skills/design-unreal-automation-and-pcg/references/09-procedural-systems-pcg.md"
        )
        skill = read("skills/design-unreal-automation-and-pcg/SKILL.md")
        for phrase in (
            "Bidirectional terrain and PCG data flow",
            "immutable source snapshot",
            "query/read layer",
            "separate write layer",
            "sub-priority",
            "original source",
            "positions or equivalent",
            "feedback loop",
            "idempotent",
            "save/reopen persistence",
        ):
            self.assertIn(phrase, chapter)
        self.assertIn("Bidirectional terrain and PCG data flow", skill)

    def test_ai_guidance_requires_reference_grounded_incremental_context(self):
        chapter = read(
            "skills/guide-unreal-ai-development/references/15-ai-assisted-development.md"
        )
        skill = read("skills/guide-unreal-ai-development/SKILL.md")
        for phrase in (
            "Reference-grounded context for complex procedural work",
            "reference_ids",
            "bounded, structured summaries",
            "incremental, reviewable batches",
            "context-retrieval success",
        ):
            self.assertIn(phrase, chapter)
        self.assertIn("reference-grounded context set", skill)
        self.assertIn("incremental reviewable batches", skill)

    def test_production_guidance_separates_runtime_and_host_target_identity(self):
        performance = read(
            "skills/validate-unreal-production/references/11-performance-scalability.md"
        )
        pipeline = read(
            "skills/validate-unreal-production/references/13-production-pipeline.md"
        )
        validation_skill = read("skills/validate-unreal-production/SKILL.md")
        for text in (performance, pipeline):
            for phrase in (
                "runtime architecture",
                "authoring/build-host architecture",
                "SDK/GDK",
                "plugin",
                "ABI",
                "ARM64",
                "ARM64EC",
            ):
                self.assertIn(phrase, text)
        for phrase in (
            "Architecture-specific target note",
            "UE 5.8, 2026-08-05",
            "Editor is not supported",
            "April",
            "GDK",
        ):
            self.assertIn(phrase, pipeline)
        self.assertIn("Chapter 04's Terrain Representation Review", validation_skill)


if __name__ == "__main__":
    unittest.main()
