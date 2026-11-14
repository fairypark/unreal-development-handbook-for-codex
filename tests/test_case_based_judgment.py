from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/prepare_judgment_exercise.py'
spec = importlib.util.spec_from_file_location('prepare_judgment_exercise', SCRIPT)
exercise = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exercise)


class JudgmentExerciseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pack = json.loads(exercise.PACK.read_text(encoding='utf-8'))

    def test_public_pack_has_complete_distinct_context_pairs(self):
        exercise.validate_pack(self.pack)
        self.assertEqual(len(self.pack['scenarios']), 14)
        self.assertEqual(len({item['pair'] for item in self.pack['scenarios']}), 7)
        self.assertFalse(self.pack['held_out'])

    def test_participant_export_cannot_leak_assessor_fields(self):
        result = exercise.participant_exercise(self.pack)
        self.assertEqual(set(result), {'evidence_class', 'language', 'instruction', 'questions'})
        self.assertTrue(all(set(q) == {'id', 'prompt'} for q in result['questions']))
        self.assertEqual({q['id'] for q in result['questions']}, {s['id'] for s in self.pack['scenarios']})
        self.assertNotIn('review_guidance', json.dumps(result))
        self.assertNotIn('red_flags', json.dumps(result))

    def test_korean_export_has_the_matching_question_for_every_identity(self):
        result = exercise.participant_exercise(self.pack, language='ko', seed=9)
        expected = {s['id']: s['prompt_ko'] for s in self.pack['scenarios']}
        self.assertEqual({q['id']: q['prompt'] for q in result['questions']}, expected)
        self.assertEqual(result['language'], 'ko')

    def test_shuffle_is_reproducible_without_mutating_the_assessor_pack(self):
        before = deepcopy(self.pack)
        one = exercise.participant_exercise(self.pack, seed=3)
        self.assertEqual(one, exercise.participant_exercise(self.pack, seed=3))
        self.assertNotEqual(one['questions'], exercise.participant_exercise(self.pack, seed=12)['questions'])
        self.assertEqual(self.pack, before)

    def test_invalid_identity_pair_or_evidence_claim_is_rejected(self):
        mutations = [
            lambda p: p.update(held_out=True),
            lambda p: p['scenarios'][1].update(id=p['scenarios'][0]['id']),
            lambda p: p['scenarios'].pop(),
            lambda p: p['scenarios'][0]['review_guidance'].update(acceptable_ko=[]),
            lambda p: p['scenarios'][0].update(review_guidance=None),
            lambda p: p['scenarios'].__setitem__(0, None),
        ]
        for mutation in mutations:
            candidate = deepcopy(self.pack)
            mutation(candidate)
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                exercise.participant_exercise(candidate)

    def test_cli_writes_a_standalone_question_file_and_protects_its_source(self):
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            source = folder / 'source.json'
            source.write_text(json.dumps(self.pack), encoding='utf-8')
            output = folder / 'questions.json'
            good = subprocess.run([sys.executable, str(SCRIPT), '--source', str(source), '--output', str(output), '--language', 'ko'], capture_output=True, text=True)
            self.assertEqual(good.returncode, 0, good.stderr)
            self.assertEqual(json.loads(output.read_text(encoding='utf-8')), exercise.participant_exercise(self.pack, language='ko'))
            raw = source.read_bytes()
            bad = subprocess.run([sys.executable, str(SCRIPT), '--source', str(source), '--output', str(source)], capture_output=True, text=True)
            self.assertNotEqual(bad.returncode, 0)
            self.assertEqual(source.read_bytes(), raw)

    def test_export_preserves_assessor_pack_through_a_hard_link(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'assessor.json'
            source.write_text(json.dumps(self.pack), encoding='utf-8')
            alias = Path(folder) / 'alias.json'
            try:
                alias.hardlink_to(source)
            except OSError as error:
                self.skipTest(f'Temporary filesystem does not support hard links: {error}')
            before = source.read_bytes()
            result = subprocess.run(
                [sys.executable, str(SCRIPT), '--source', str(source), '--output', str(alias)],
                capture_output=True, text=True,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('must not overwrite', result.stderr)
            self.assertEqual(source.read_bytes(), before)


class JudgmentTeachingRoutingTests(unittest.TestCase):
    def test_first_priority_precedes_the_charter_mission(self):
        text = (ROOT / 'PROJECT_CHARTER.md').read_text(encoding='utf-8')
        self.assertLess(text.index('## First priority:'), text.index('## Project Mission'))
        text = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        self.assertLess(text.index('## First priority:'), text.index('## Required reasoning sequence'))

    def test_all_domain_chapters_teach_a_distinct_early_contrast(self):
        chapters = sorted((ROOT / 'skills').glob('*/references/[0-9][0-9]-*.md'))
        self.assertEqual(len(chapters), 17)
        contrasts = []
        for path in chapters:
            text = path.read_text(encoding='utf-8')
            with self.subTest(chapter=path.name):
                start = text.index('## Decision contrast:')
                headings = re.findall(r'^## (.+)$', text, re.MULTILINE)
                self.assertTrue(headings[headings.index('Purpose') + 1].startswith('Decision contrast:'))
                section = text[start:text.index('\n## ', start + 4)]
                for component in ('**Evidence class:**', '**Situation.**', '**Choice and reason.**', '**When the choice changes.**', '**Smallest useful test.**'):
                    self.assertIn(component, section)
                self.assertIn('constructed teaching scenario', section)
                self.assertNotIn('## Recommended workflow', text[:start])
                contrasts.append(section)
        self.assertEqual(len(set(contrasts)), 17)

    def test_every_runtime_skill_routes_to_first_principle_before_other_instructions(self):
        skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
        self.assertEqual(len(skills), 9)
        for path in skills:
            text = path.read_text(encoding='utf-8')
            with self.subTest(skill=path.parent.name):
                first_section = next(line for line in text.splitlines() if line.startswith('## '))
                self.assertEqual(first_section, '## First priority: contextual judgment from cases')
                self.assertIn('00-philosophy.md#learn-judgment-from-cases-first', text)
                link = 'references/00-philosophy.md' if path.parent.name == 'reason-about-unreal-development' else '../reason-about-unreal-development/references/00-philosophy.md'
                self.assertTrue((path.parent / link).resolve().is_file())


if __name__ == '__main__':
    unittest.main()
