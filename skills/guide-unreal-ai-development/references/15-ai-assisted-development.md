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

## Reference-grounded context for complex procedural work

For graph-, attribute-, and data-rich work, establish a reference set before
planning mutation. Prefer approved project examples, the current graph or
asset authority, the target engine/build documentation, and a known-good
baseline over a first-principles reconstruction from memory. Record
`reference_ids`, version and authority scope, why each reference was selected,
the relevant context slice, unresolved unknowns, and the questions a reviewer
must answer.

Acquire context through a bounded ladder and stop as soon as the current
decision is supported:

1. Use explicit user targets, Editor selection, named assets, and the current
   authoritative state.
2. Reuse approved project examples and known-good baselines with compatible
   responsibility and version scope.
3. Use semantic or indexed search to identify candidates, then inspect the
   selected source directly.
4. Perform bounded discovery only for named unknowns that block the plan.
5. Use temporary inspection scripts only when supported observation surfaces
   cannot answer the question; remove or promote them deliberately afterward.

For reusable systems, prefer an exact approved example, then duplicate and
adapt the closest compatible example, and create a new system only when no
suitable reference exists. Record material divergence from the example and
revalidate the affected assumptions. Search rank, semantic similarity, and
retrieval success identify candidates; they do not grant source authority or
prove compatibility.

Large graphs and datasets should be supplied as bounded, structured summaries
with the identities and relationships needed for the current decision. Do not
let truncation, a semantic search hit, or context-retrieval success stand in
for evidence. Before mutation, state the intended changes, postconditions,
risks, and rollback target; execute in incremental, reviewable batches and
stop when no relevant reference exists or the remaining context is ambiguous.
The durable rule is reference-grounded planning and supervision, not a
particular model, prompt, Editor integration, or transport.

## Bounded AI task contract and latency guard

Before a prototype or Editor mutation, the agent must write down a compact
task contract: intent, current stage, target world or system, operation mode,
allowed mutation scope, change and wall-clock budgets, preconditions,
postconditions, save policy, evidence class, rollback target, and stop
conditions. For ordinary prototype work, default to a bounded edit; use a
read-only diagnostic audit, an explicit promotion review, and a separately
confirmed maintenance mode for broad rebuilds. Project-specific names may
differ, but the boundaries must remain visible.

The agent should discover the required execution surface once per bounded task,
batch inventory and validation work, serialize stateful mutations, and verify
the resulting state before starting a dependent operation. It must track
setup, tool discovery, wait, mutation, verification, and background time. A
short user request must not silently expand into a map-wide builder, per-item
round trips, repeated tool discovery, or blind evidence retries.

When a task times out or returns an ambiguous result, the agent must stop and
perform a read-only state audit. It may then resume from a verified checkpoint,
roll back the verified target, or report the task as blocked; it may not infer
that no mutation occurred and immediately repeat the same request. If the
available execution surface cannot invoke the proposed adapter, report that
live execution is untested rather than treating compilation, static schema
validation, or a successful transport call as equivalent evidence.

## Domain workflow compliance

A domain chapter's explicit workflow is part of the AI's execution contract. For level, world, environment, terrain, route, POI, or map-wide dressing work, load Chapter 04 and follow its **Mandatory AI execution contract** and numbered concept-to-production stages in order. Do not substitute a Tool sequence, screenshot, generated asset, or post-hoc summary for a stage's required evidence.

Before mutation, classify the work as a disposable experiment or production-intended change, identify the current stage and approved predecessor artifact, and record the stage objective, allowed mutations, postconditions, approver, and rollback target. For composition work, Area Composition Plan `PASS` advances only to Stage 2a Reference-to-Prototype Translation. The agent must not place content-bearing prototype geometry until a machine-readable source and authority registry, zone-level quantitative contract, traceability map for every planned array/proxy group/path/terrain change, camera-specific tolerances, and explicit broad-placement decision pass. It must then create Stage 2b Concept-to-Asset Readiness from those approved requirements: `ASSET_PLAN_READY` before the Experience Prototype, `VISUAL_SLICE_READY` before the representative slice, and `PRODUCTION_DRESSING_READY` before production meshing or dressing. During execution, keep mutations within the current stage and report its status as `PASS`, `FAIL`, `PENDING_EVIDENCE`, or `INVALID_EVIDENCE`. Advance only when the evidence is complete and promotion is explicitly recorded. Missing evidence, failed tests, absent feedback, or transport-only success blocks promotion and requires a stop, a return to the responsible stage, or an explicit request for what is missing.

For asset supply work, distinguish a discovered listing, ownership-confirmed library entry, acquired or staged package, representative approval, and production approval. Search project-native and ownership-confirmed content before proposing new acquisition. Never infer purchase, download, install, migration, plugin enablement, outsourcing, upload, or payment authority from an asset request, design approval, marketplace result, or readiness gate. Keep credentials, cookies, payment data, and private tokens out of contract records, and preserve rejected candidates and supply failures so the concept, plan, budget, or schedule can be reopened deliberately.

After each composition-changing prototype batch, treat the translation contract as a live audit rather than a one-time permit. Preserve fixed-condition reference/plan/prototype comparisons, keep overview macro diagnostics separate from actual runtime player-camera distance, enclosure, occlusion, route, scale, and readability evidence, and lock the next broad batch while the audit is pending or failed. If any zone distribution, shade or intentional void, hierarchy, frontage, path continuity, or prohibited silhouette leaves tolerance, preserve the failed candidate and reopen the earliest responsible stage; matching total Actor count does not authorize promotion.

Small or disposable level work may combine adjacent Chapter 04 stages in one reversible pass only when the combination is declared before mutation and every stage's decision question, evidence, and recovery path remains inspectable. A combined stage is not a skipped stage. If a later change invalidates an accepted level assumption, reopen the affected stage, retain the previous baseline, and re-run dependent stages before continuing.

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

### Builder self-check feedback loop

Within the mutation stage, use a short feedback loop:

`observe -> plan -> mutate -> builder self-inspect -> correct -> verify postconditions -> independent evaluate -> promote`

Builder self-inspection should re-read the exact changed state and may use
screenshots, logs, counts, bounds, warnings, or targeted runtime checks to find
obvious defects before spending independent-review effort. It is part of
construction quality control, not an acceptance gate. A screenshot can expose
visible orientation, composition, or contact problems under its capture
conditions, but it cannot by itself prove occluded geometry, collision,
navigation, persistence, regeneration, packaged behavior, performance, or a
different gameplay viewpoint.

The builder may correct failures it discovers, but must preserve the changed
evidence and repeat the applicable postconditions. It cannot convert its own
capture or explanation into independent approval. If no independent evaluator
is available, record a separate, explicitly labelled self-review and leave any
independence-dependent promotion `PENDING_EVIDENCE` or `PENDING_APPROVAL`.

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

Organize an agent-facing development surface into four responsibilities. The
names may vary, but their knowledge and authority boundaries should remain
distinct:

| Layer | Owns | Must not be mistaken for |
| --- | --- | --- |
| Toolset or capability surface | A discoverable, versioned group of related observation and mutation interfaces, with access and capability boundaries. | A domain workflow, approval policy, or complete engine mirror. |
| Primitive | The smallest useful typed inspection or action, with units, side effects, structured results, postconditions, and recoverable errors. | User intent, composition judgment, or evidence that a larger task passed. |
| Example | A project-approved, versioned instance that shows valid assets, graph structure, data relationships, and expected output under known conditions. | A universal template, durable rule, or automatic permission to copy unchanged. |
| Skill | Durable intent, decision sequence, constraints, stop conditions, evidence requirements, and routing to detailed references. | A cache of current project state, exhaustive API inventory, hidden prompt, or substitute for observation. |

Observation interfaces own current runtime and project truth. Examples own
approved concrete patterns. Skills own durable reasoning that cannot be safely
inferred from schemas or current state. Keep one authority for each fact: do not
copy dynamic asset lists, tool inventories, coordinates, or version-sensitive
API details into durable skill prose when they can be discovered or linked.
Keep skill instructions concise and colleague-readable, and load detailed
references only when the task reaches their responsibility.

Expose small typed composable operations rather than mirroring Unreal
internals. Provide get, list, or inspect parity for mutation so the agent can
plan and verify without changing state. Errors should distinguish empty valid
results, unsupported capabilities, invalid inputs, partial state, timeout, and
cancellation, and should name a safe observation or recovery action.

Discover tools progressively: load a minimal capability catalog, select the
responsible Toolset, and then load only the needed operation schemas. Cache
descriptions within their declared task or session scope and refresh them when
the engine, integration, project capabilities, or version changes. Runtime tool
search is a useful current implementation pattern, not a durable dependency or
source of approval authority.

## Validation checklist

- Roles, authority, and stop conditions are explicit.
- Read-only defaults, mutation authority, and the promotion target are explicit.
- The mutation environment, baseline, changed-file scope, provenance, and rollback path are recorded.
- Each mutation batch has observable postconditions; tool or transport success is not used as the verdict.
- Stateful editor mutations are serialized and verified before the next dependent mutation.
- The builder cannot rewrite or self-approve required evidence.
- The applicable domain workflow is loaded, the current stage is explicit, and no downstream stage began before its predecessor gate passed.
- Complex graph or data work has a recorded reference set, authority/version scope, bounded context selection, and reviewer questions before mutation.
- Context acquisition stopped at the lowest-cost trustworthy rung; semantic or indexed search hits were inspected against an authoritative source before use.
- Existing approved examples were reused or adapted before creating a new system, and material divergence was recorded and revalidated.
- The plan names intended changes, postconditions, risks, and rollback before mutation; execution is incremental and stops on ambiguous or missing context.
- For level composition, Stage 2a passed before the first content-bearing prototype mutation; source authority, quantitative zone contracts, prototype trace IDs, comparison conditions, tolerances, and the placement decision are machine-readable and versioned.
- For concept-led asset supply, `ASSET_PLAN_READY`, `VISUAL_SLICE_READY`, and `PRODUCTION_DRESSING_READY` are independently scoped and versioned; demand, ownership or provenance, acquisition authority, license, compatibility, dependencies, total cost, exact candidates, evidence, fallback, and rollback remain inspectable.
- Each composition-changing batch has a same-condition deviation audit, and the builder cannot use aggregate Actor count or overview-only player claims to self-approve drift.
- Combined or reopened stages are documented with their evidence, approval, baseline, and recovery path.
- Inputs, outputs, and Tool results are inspectable.
- Toolset, primitive, example, and Skill responsibilities have one declared owner each and do not duplicate dynamic or version-sensitive knowledge.
- Mutation interfaces have non-mutating observation parity, structured failure semantics, and bounded progressive discovery.
- Builder self-inspection is preserved as construction evidence and is not used as independent acceptance or promotion authority.
- Reproduction does not depend on private hidden context.
- Failure and recovery paths have been exercised.
- The workflow remains useful when the model or Tool stack changes.

## Common mistakes

- Letting an agent explore by mutating the main project or shared world.
- Treating a level-design workflow as optional guidance, or using a successful tool call as permission to skip a stage.
- Treating Area Composition Plan approval as prototype-placement authority, or reconstructing the missing Stage 2a translation contract after broad placement.
- Treating a listing as ownership, an entitlement or download as compatibility, a staged package as representative proof, a Visual Slice as production authority, or a design gate as permission for an external acquisition.
- Treating a sandbox as approval, or treating a successful tool response as proof of the intended result.
- Building a complex PCG graph from memory without approved project references, or treating a search hit, truncated context, or semantic match as sufficient evidence.
- Starting broad discovery or temporary scripting before checking explicit targets, current selection, and approved project examples.
- Copying a near-match example without recording the changed assumptions and revalidating its output.
- Sending an entire graph or dataset without a bounded structured context slice, then allowing missing relationships or ambiguous authority to be hidden by automation.
- Combining Toolset, primitive, example, and Skill knowledge into one opaque prompt or broad endpoint whose state, version, and approval authority cannot be inspected.
- Treating a builder screenshot or screenshot-guided correction loop as independent acceptance.
- Allowing overlapping stateful editor mutations that make ordering and recovery ambiguous.
- Merging generated assets or configuration without preserving their source, version, owner, and validation evidence.

## Research basis and further reading

- [AI-assisted Unreal world-building demonstration](https://www.youtube.com/watch?v=lDf_y-YPELo) - a capability demonstration used to identify candidate responsibility layers, context reuse, procedural lifetimes, and builder self-checks; it is not production-outcome evidence.
- [Epic Games: `UAgentSkill`](https://dev.epicgames.com/documentation/unreal-engine/API/Plugins/ToolsetRegistry/UAgentSkill?lang=en-US) - a version-sensitive implementation example for registering agent guidance; inheritance and API details are not the durable Skill contract.
- [Epic Games: Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor) — current editor-agent integration guidance; availability, APIs, and data formats are version-dependent, so use it as an example of a control boundary rather than a permanent contract.
- [Epic Games: Working with PCG and LLMs Using Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/working-with-pcg-and-llms-using-unreal-mcp-in-unreal-engine?lang=en-US) — grounds agent context in project references and favors planning, review, and incremental supervision.
- [Epic Games: Unreal Engine 5.8 Release Notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) — describes Sandbox workspaces as isolated areas whose changes can be selectively persisted; treat this as a dated feature reference, not a replacement for project review and source control.

## Related topics

Philosophy; World & Level Design; Automation & Python; Procedural Systems & PCG; Validation, Testing & Debugging; Production Pipeline; Team Collaboration & Source Control.
