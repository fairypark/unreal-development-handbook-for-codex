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

## Mutation boundary and promotion

Treat an agent-driven project change as a promotion pipeline, not as a successful tool call. An agent may be capable of changing the project without having the authority to approve that change. Make the boundary between observation, mutation, evaluation, and promotion explicit:

| Stage | Required contract | Stop or recovery condition |
| --- | --- | --- |
| Observe and reference | Identify the goal, baseline, relevant assets and settings, constraints, and missing evidence. | Stop when scope or baseline is ambiguous. |
| Plan and review | State the intended changes, risks, postconditions, owner, and rollback target before mutation. | Escalate when the plan changes authority, security, or production scope. |
| Isolate and mutate | Use a sandbox, branch, disposable project copy, or another recoverable boundary; serialize stateful editor mutations. | Do not mutate the main project when the change is exploratory, broad, or not yet approved. |
| Verify postconditions | Preserve the exact changed assets/configuration/generated outputs and check saved state, behavior, performance, and warnings. | Stop on a partial, ambiguous, or transport-only success. |
| Evaluate and promote | Use a read-only evaluator with raw artifacts and a neutral rubric; record explicit approval and the promotion target. | Reject, revise, or roll back when evidence conflicts or approval is missing. |

Isolation does not replace source control or provenance. Retain the baseline, the exact change set, generated outputs, validation evidence, and the person or agent responsible for promotion. A sandbox, successful API response, or “no error” result is not evidence that the intended project state was reached.

Treat local or remote editor-control boundaries as security decisions. In-editor code execution, broad asset mutation, and access to project or production data are privileged capabilities. Before connecting an agent, decide where it may listen, who may invoke it, what it may read or mutate, and how access is revoked. Do not expose a control boundary merely because a workflow is convenient.

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
- Read-only defaults, mutation authority, and the promotion target are explicit.
- The mutation environment, baseline, changed-file scope, provenance, and rollback path are recorded.
- Each mutation batch has observable postconditions; tool or transport success is not used as the verdict.
- Stateful editor mutations are serialized and verified before the next dependent mutation.
- The builder cannot rewrite or self-approve required evidence.
- Inputs, outputs, and Tool results are inspectable.
- Reproduction does not depend on private hidden context.
- Failure and recovery paths have been exercised.
- The workflow remains useful when the model or Tool stack changes.

## Common mistakes

- Letting an agent explore by mutating the main project or shared world.
- Treating a sandbox as approval, or treating a successful tool response as proof of the intended result.
- Allowing overlapping stateful editor mutations that make ordering and recovery ambiguous.
- Merging generated assets or configuration without preserving their source, version, owner, and validation evidence.

## Research basis and further reading

- [Epic Games: Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor) — current editor-agent integration guidance; availability, APIs, and data formats are version-dependent, so use it as an example of a control boundary rather than a permanent contract.
- [Epic Games: Working with PCG and LLMs Using Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/working-with-pcg-and-llms-using-unreal-mcp-in-unreal-engine?lang=en-US) — grounds agent context in project references and favors planning, review, and incremental supervision.
- [Epic Games: Unreal Engine 5.8 Release Notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) — describes Sandbox workspaces as isolated areas whose changes can be selectively persisted; treat this as a dated feature reference, not a replacement for project review and source control.

## Related topics

Philosophy; Automation & Python; Validation, Testing & Debugging; Production Pipeline; Team Collaboration & Source Control.
