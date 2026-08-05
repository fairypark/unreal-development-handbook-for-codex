from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "design-unreal-automation-and-pcg" / "SKILL.md"
CHAPTER = (
    ROOT
    / "skills"
    / "design-unreal-automation-and-pcg"
    / "references"
    / "09-procedural-systems-pcg.md"
)
WORLD_SKILL = ROOT / "skills" / "design-unreal-worlds-and-levels" / "SKILL.md"
WORLD_CHAPTER = (
    ROOT
    / "skills"
    / "design-unreal-worlds-and-levels"
    / "references"
    / "04-world-level-design.md"
)


class PcgGuidanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.chapter = CHAPTER.read_text(encoding="utf-8")
        cls.world_skill = WORLD_SKILL.read_text(encoding="utf-8")
        cls.world_chapter = WORLD_CHAPTER.read_text(encoding="utf-8")

    def test_skill_requires_dependent_strata_contract_and_final_separation(self):
        self.assertIn("Dependent-Strata Strategy Gate", self.skill)
        self.assertIn("VIDEO_DISTANCE_EXCLUSION", self.skill)
        self.assertIn("CONSIDERED", self.skill)
        self.assertIn("source footprint, clearance band, and dependency order", self.skill)
        self.assertIn("minimum separation after final transforms", self.skill)

    def test_chapter_covers_hardscape_exclusion_as_a_durable_pattern(self):
        for required in (
            "Hardscape-to-ground-cover exclusion",
            "final hardscape footprint as the exclusion authority",
            "center-to-center distance alone can under-exclude",
            "inner exclusion radius",
            "minimum source-to-target separation",
            "tutorial's numeric default",
            "source-to-target separation",
            "decision order",
            "rejected alternatives",
            "PENDING_EVIDENCE",
        ):
            self.assertIn(required, self.chapter)

    def test_chapter_rejects_unverified_nanite_culling_assumptions(self):
        for required in (
            "Version-sensitive rendering and culling decisions",
            "view-specific distance culling as unsupported",
            "target hardware",
            "fallback",
            "Assuming Nanite automatically replaces distance culling",
        ):
            self.assertIn(required, self.chapter)

    def test_chapter_keeps_current_engine_details_in_research_context(self):
        for required in (
            "PCG Node Reference",
            "Nanite Virtualized Geometry",
            "Cull Distance Volumes",
        ):
            self.assertIn(required, self.chapter)

    def test_chapter_connects_ue58_manual_edit_to_override_lifecycle(self):
        for required in (
            "UE 5.8's PCG Manual Edit and Data Override System",
            "delta layer over a versioned procedural base",
            "stable target identity or mapping policy",
            "orphaned or conflicting",
            "source-control behavior",
            "Experimental",
        ):
            self.assertIn(required, self.chapter)

    def test_level_work_routes_dependent_strata_before_first_mutation(self):
        for text in (self.world_skill, self.world_chapter):
            self.assertIn("Dependent-Strata Strategy Gate", text)
            self.assertIn("before the first relevant generator", text)
        self.assertIn("VIDEO_DISTANCE_EXCLUSION", self.world_chapter)


if __name__ == "__main__":
    unittest.main()
