# Evaluating whether the handbook improves judgment

## Claim and evidence

The handbook's first priority is better contextual judgment. Keep three claims separate:

| Claim | Useful evidence | What it cannot establish |
| --- | --- | --- |
| The teaching package is structurally sound | Valid links, complete contrasts, runnable exercises, preserved contracts and passing regression tests | That a reader understood the mechanism or chose better |
| A reader transfers a decision to an unfamiliar context | Comparable responses, changed-context problems, neutral assessment of reasoning and test choice | That the resulting Unreal work is good or production-ready |
| The decision improves the actual outcome | A scoped prototype or production experiment with relevant player, visual, technical, and recovery evidence | Universal superiority across projects or attribution to one teaching change without controls |

This evaluation introduces no new runtime production gate. Use it when assessing editorial changes or learning, not as an obligatory ceremony for each local task. The paired [Korean review](judgment-evaluation.ko.md) covers the same procedure.

## Calibration material and protected assessment

The public exercise contains fourteen constructed scenarios in seven pairs. They cover travel and destination spacing, shared state ownership, visual diagnosis, GPU and CPU cost, release scope, before/after comparisons, and save compatibility on rollback. In the rollback pair, only the previous build's ability to read the current save changes. Ask what that changes about the recovery plan and what evidence of player progress each path still needs. [Calibration scenarios](judgment-scenarios.v1.json)

The pack is published alongside the handbook. It is not a held-out benchmark and must not be described as unseen evidence of learning. Review guidance belongs to the assessor; the exercise preparation script exports only questions and a neutral response instruction. Author genuinely new, private-to-the-assessor scenarios for a transfer study after the teaching material is fixed. Do not put private project information, credentials, or user transcripts in them.

## Comparison procedure

1. Freeze the candidate Handbook revision, the comparison revision, the question set, scoring dimensions, resource budget, model or participant configuration, and assessor instructions. Record other context differences.
2. Obtain responses under comparable conditions with and without the candidate material or between revisions. Keep independent sessions where earlier answers could leak into the comparison. Separate model-to-model differences from a Handbook revision effect.
3. Ask for the important decision, its reason, a viable alternative and cost, the condition that changes the recommendation, the smallest discriminating test, and relevant authority limits. A short justified answer is preferable to an elaborate workflow that misses the problem.
4. Randomize response order and conceal revision labels from the assessor where feasible. Preserve original responses and assessor reasoning. Do not reveal a desired verdict or let the author convert a failed assessment into a pass.
5. Check both changed-context pairs and unfamiliar problems. A recommendation can stay the same if the explanation shows why the changed condition is irrelevant; a forced answer flip is not the objective.
6. Report failures as well as improvements, sample size, cost, remaining uncertainty, and whether the task was calibration or protected transfer. Use independent review when a credible improvement claim depends on it; otherwise label author self-checks explicitly.

## Assessment dimensions

Score each dimension from 0 to 2 for a compact exploratory review: 0 = absent or materially wrong, 1 = plausible but incomplete, 2 = specific to the evidence and context. These are teaching-assessment scores, not the existing visual-production rubric or a new promotion threshold.

- **Intent and failure scale:** identifies the unsatisfied outcome and the scale of the decision.
- **Causal reasoning:** connects observations to plausible mechanisms, competing explanations, and uncertainty.
- **Alternatives and trade-offs:** compares a feasible alternative with its relevant cost or limitation.
- **Context transfer:** identifies a condition that changes the choice or explains why a stated change does not.
- **Discriminating validation:** proposes an observation capable of falsifying the recommendation at an appropriate cost.
- **Scope and authority:** preserves safety, ownership, evidence limits, and the user's actual authorization.

Do not give credit for merely using phrases such as "case-based reasoning", quoting a checklist, proposing more agents, or generating more paperwork. Do not mechanically keyword-score free-text answers. Reviewers can accept multiple designs when their reasoning fits the evidence. Treat invented outcomes, concealed hard failures, or unauthorized destructive action as explicit failures rather than hiding them in an average.

## Preparing a calibration exercise

From the repository root, run `python scripts/prepare_judgment_exercise.py --output .tmp/judgment-questions.json`. The script validates the pack and exports a stable shuffled question set without review guidance. It does not contact an AI service, execute Unreal, or grade judgment. Keep the complete pack separate from the participant input when using it for calibration.

Structural tests validate the pack, its answer separation, and Handbook routing. They are not an AI behavior trial. Until comparable responses and assessment are recorded, report **judgment improvement: NOT_ESTABLISHED**. Until the actual project experiment passes, report **production improvement: NOT_ESTABLISHED**.
