"""Export calibration questions without assessor guidance; never grade reasoning."""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import random

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / 'skills/validate-unreal-production/references/judgment-scenarios.v1.json'
DIMENSIONS = ('intent_and_failure_scale', 'causal_reasoning', 'alternatives_and_tradeoffs',
              'context_transfer', 'discriminating_validation', 'scope_and_authority')


def validate_pack(pack: dict) -> None:
    if not isinstance(pack, dict) or (
        pack.get('schema_version') != 1
        or pack.get('evidence_class') != 'constructed_calibration_scenarios'
        or pack.get('held_out') is not False
    ):
        raise ValueError('This exporter accepts explicitly labeled public calibration material only.')
    if pack.get('dimensions') != list(DIMENSIONS):
        raise ValueError('Assessment dimensions are incomplete or out of order.')
    scenarios = pack.get('scenarios')
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError('Nonempty scenarios are required.')
    ids = set()
    pairs = defaultdict(list)
    for item in scenarios:
        if not isinstance(item, dict):
            raise ValueError('Each scenario must be an object.')
        for field in ('id', 'pair', 'prompt', 'prompt_ko'):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f'Missing scenario field: {field}')
        if item['id'] in ids:
            raise ValueError('Duplicate scenario identity.')
        ids.add(item['id'])
        pairs[item['pair']].append(item)
        guidance = item.get('review_guidance')
        if not isinstance(guidance, dict):
            raise ValueError('Each scenario needs assessor guidance.')
        for field in ('acceptable', 'acceptable_ko', 'red_flags', 'red_flags_ko'):
            values = guidance.get(field)
            if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
                raise ValueError(f'Missing assessor guidance: {field}')
        if len(guidance['acceptable']) != len(guidance['acceptable_ko']) or len(guidance['red_flags']) != len(guidance['red_flags_ko']):
            raise ValueError('Paired Korean guidance must cover the same decisions.')
    for items in pairs.values():
        if len(items) != 2:
            raise ValueError('Each context pair must contain exactly two scenarios.')
        first, second = items
        if any(first[field].strip() == second[field].strip() for field in ('prompt', 'prompt_ko')):
            raise ValueError('A context pair cannot repeat an identical question.')


def participant_exercise(pack: dict, language: str = 'en', seed: int = 0) -> dict:
    validate_pack(pack)
    if language not in ('en', 'ko'):
        raise ValueError('Language must be en or ko.')
    instruction = ('Choose the next action, explain why it fits, compare one viable alternative and its cost, '
                   'state a condition that changes your choice, and propose the smallest useful test. '
                   'Respect the authorized scope and distinguish observation from hypothesis.')
    if language == 'ko':
        instruction = '다음 행동과 적합한 이유, 실행 가능한 대안 하나와 비용, 선택을 바꾸는 조건, 가장 작은 유효 시험을 설명하라. 승인 범위를 존중하고 관찰과 가설을 구분하라.'
    key = 'prompt_ko' if language == 'ko' else 'prompt'
    questions = [{'id': item['id'], 'prompt': item[key]} for item in pack['scenarios']]
    random.Random(seed).shuffle(questions)
    return {'evidence_class': 'public_calibration_exercise_not_held_out',
            'language': language, 'instruction': instruction, 'questions': questions}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=PACK)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--language', choices=('en', 'ko'), default='en')
    parser.add_argument('--seed', type=int, default=0)
    args = parser.parse_args(argv)
    try:
        pack = json.loads(args.source.read_text(encoding='utf-8'))
        exercise = participant_exercise(pack, args.language, args.seed)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    encoded = json.dumps(exercise, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        protected_packs = (args.source, PACK)
        if args.output.exists() and any(path.exists() and args.output.samefile(path) for path in protected_packs):
            parser.error('The participant export must not overwrite the assessor pack.')
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding='utf-8')
    else:
        print(encoded, end='')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
