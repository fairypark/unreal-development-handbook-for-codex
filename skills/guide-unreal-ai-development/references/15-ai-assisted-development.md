# 15 — AI-Assisted Development

## Purpose

Use AI agents as bounded development participants whose reasoning, mutations, evidence, and approvals remain inspectable and recoverable.

## Intent

Gain speed and coverage without allowing automation confidence, Tool success, hidden context, or self-approval to replace professional engineering judgment.

## Role design

Define each agent's objective, allowed reads and mutations, decision authority, stop conditions, required evidence, and escalation boundary. Separate builder, read-only evaluator, and final approver when independence matters. Keep human approval for destructive, external, high-risk, legal, financial, security, or policy-sensitive actions.

## Context and constraints

Provide goals, project state, requirements, assumptions, constraints, success criteria, and production concerns. Prefer project-owned durable knowledge for naming, folders, ownership, setup, and canonical workflows. Avoid fixed Tool inventories when runtime discovery can provide them.

Keep reusable principles free of private paths, map coordinates, asset-pack anecdotes, credentials, model-specific orchestration, and temporary workarounds.

## Evidence and independent evaluation

Give evaluators raw artifacts, the applicable rubric, previous comparable evidence when needed, and neutral factual change scope. Withhold intended verdicts, builder scores, persuasive completion narratives, and suspected answers. Keep evaluators read-only and preserve failed decisions.

If independent review is unavailable, perform a separate self-review pass and label it honestly. Do not claim equivalent independence.

## Failure containment

- Use reversible increments and source-control checkpoints.
- Serialize stateful Editor mutations.
- Verify complete results before continuing.
- Treat arbitrary in-editor code execution as privileged.
- Stop on ambiguous failure rather than compounding changes.
- Require postconditions for project state, assets, behavior, performance, persistence, and recovery.
- Prevent automation from inventing evidence, hashes, transforms, or passing verdicts.

## Agent-facing tools and skills

Expose small typed composable operations rather than mirroring Unreal internals. Store in skills only durable project knowledge that tools cannot infer. Keep skill instructions concise, describe workflow and constraints, and load detailed references only when relevant.

## Validation checklist

- Roles, authority, and stop conditions are explicit.
- The builder cannot rewrite or self-approve required evidence.
- Inputs, outputs, and Tool results are inspectable.
- Reproduction does not depend on private hidden context.
- Failure and recovery paths have been exercised.
- The workflow remains useful when the model or Tool stack changes.

## Related topics

Philosophy; Automation & Python; Validation, Testing & Debugging; Team Collaboration & Source Control.
