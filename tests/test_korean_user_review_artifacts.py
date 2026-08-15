from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


class KoreanUserReviewArtifactTests(unittest.TestCase):
    def test_every_plugin_skill_requires_a_separate_korean_review_version(self):
        skill_files = sorted(SKILLS.glob("*/SKILL.md"))
        self.assertGreater(len(skill_files), 0)

        required_phrases = (
            "## Prepare Korean user-review versions",
            "Korean-language version as a separate artifact",
            "concept images, floor plans and layout drawings",
            "Localize decision-bearing visual text",
            "separate Korean review sheet",
            "Do not mark the handoff complete until the Korean version is reviewable",
        )

        for skill_file in skill_files:
            content = skill_file.read_text(encoding="utf-8")
            with self.subTest(skill=skill_file.parent.name):
                for phrase in required_phrases:
                    self.assertIn(phrase, content)


if __name__ == "__main__":
    unittest.main()
