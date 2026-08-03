# 01 — Development Process

## Purpose

Turn an Unreal request into a traceable sequence of decisions, implementation, verification, and learning.

## Recommended workflow

1. **Intent:** State the desired experience or production outcome.
2. **Context:** Inspect the current project, existing systems, content, platform, and team state.
3. **Requirements:** Separate mandatory behavior from preferences.
4. **Constraints:** Record performance, schedule, compatibility, content, collaboration, and recovery limits.
5. **Design:** Compare viable boundaries, data flow, lifecycle, spatial structure, and implementation options.
6. **Validation strategy:** Define evidence, test conditions, hard failures, and promotion gates.
7. **Implementation:** Select the smallest appropriate technology and execute in reversible increments.
8. **Verification:** Compare actual evidence with the original intent and record remaining risks.

## Iteration and commitment

Iteration should be fastest where uncertainty is high and changes are reversible. Commitment should slow down when a change becomes expensive to undo. This is not a rigid waterfall: it is a sequence of evidence gates around an expanding commitment ladder.

| Stage | Primary question | Minimum evidence | If the gate fails |
| --- | --- | --- | --- |
| Direction brief | Are we making the intended experience? | Player fantasy, fun thesis, core verbs, intended emotional rhythm, references or concept art, non-goals, constraints, and explicit acceptance questions. | Revise the brief or references before building the level. |
| Spatial plan | Can the space and its responsibilities be understood before construction? | Annotated top-down or node map, zones, primary route, optional loops, focal hierarchy, landmarks, major reveals, boundaries, known risks, and a stable-ID `DIAGNOSTIC_ONLY` overview-camera set whose smallest sufficient coverage spans arrival, reverse, lateral, waterway/axis, elevation, and project-specific relationships. Record player-camera height/FOV for auxiliary early scale checks and identify the planned runtime-rig source. | Revise the plan; do not hide uncertainty with detail or one hero overview. |
| Experience prototype | Does the proposed fun exist in one cheap, playable unit? | A POI or encounter prototype with an approach, reveal, player choice or verb, outcome or reward, and a next hook, tested with placeholders. | Return to the fun thesis or spatial plan; do not build the whole route to discover that the unit is empty. |
| Playable blockout | Does the space work as a game? | Runtime playtest with the representative player controller and actual runtime camera rig, covering movement, scale, camera behavior, collision, route, sightlines, landmarks, pacing, and boundary behavior. | Return to the plan or blockout and retest from comparable conditions. |
| Visual feasibility slice | Can the visual target be produced consistently and within budget? | A small representative segment using real or representative asset families, materials, lighting, contacts, collision, audio intent, target performance conditions, and the approved runtime rig for player readability, asset density, and composition. | Repair the visual language, asset kit, or pipeline; do not scale map-wide production. |
| Production content | Can the approved pattern scale without changing the design? | Content coverage, provenance, repeatable placement, ownership, integration checks, and a deviation log for each zone or chunk. | Stop scaling and reopen the affected design or feasibility gate. |
| Finish and release | Does the complete level meet player, quality, technical, and recovery targets? | Final traversal, visual, audio, collision, performance, persistence, packaging, and recovery evidence. | Return to the failing subsystem rather than applying unrelated polish. |

The purpose of a gate is not to prevent change. It is to make the cost and meaning of change explicit. A promotion records what is currently accepted, what remains risky, who can approve the next commitment, and which earlier gate must reopen when a later change invalidates its assumptions.

## Bounded prototype iteration

A prototype request is not a smaller production build. It is an experiment with
a deliberately narrow change surface. Before any Editor mutation, create a
task-scoped iteration contract that records the current world or system, the
unknown being tested, the current stage, the allowed scope, the maximum change
count or other bounded resource, the wall-clock budget, the save policy,
preconditions, postconditions, evidence class, owner or approver, and rollback
target.

Use explicit operation modes so that a short request cannot inherit the
behavior of a broad builder:

| Mode | Responsibility | Default boundary | What it does not prove |
| --- | --- | --- | --- |
| Bounded edit | Apply one small, reversible change to existing named content or state. | Transform or data changes within a declared batch; explicit deletion of named existing targets is allowed only under the `BOUNDED_PROTO_EDIT` contract; no implicit spawn, wildcard delete, broad rebuild, or save. | It does not prove the whole level, visual quality, or production readiness. |
| Diagnostic audit | Read one batched snapshot and diagnose the current state. | One scoped inventory and local validation pass; no mutation. | A diagnostic pass does not approve promotion. |
| Promotion review | Evaluate an explicit evidence package against a gate. | Requires explicit confirmation, structural checks, and the required independent or designated review. | It does not silently rebuild, recapture invalid evidence, or retry until a pass appears. |
| Maintenance rebuild | Reconstruct or migrate a broad disposable state. | Separate task, explicit confirmation, checkpoint, and recovery plan. | It is never the default implementation of an ordinary prototype edit. |

For a normal prototype iteration, use the bounded-edit mode unless the contract
shows that a different mode is required. An explicit delete of an existing,
uniquely identified prototype Actor may remain bounded when it is part of the
user's allowlist, has no protected parent or dependent output, and does not
change an authoritative route, water/bridge relationship, zone marker,
Landscape, or other plan-owned responsibility. Creation, wildcard or broad
deletion, terrain rewriting, broad layout regeneration, and production-asset
replacement must be reclassified rather than expanding a patch implicitly.
A project may assign local names to these modes, but the names must not change
their separation of responsibility.

### `BOUNDED_PROTO_EDIT`: existing approved prototype hot path

`BOUNDED_PROTO_EDIT` is an operation mode inside the current staged workflow,
not a new production stage and not a promotion shortcut. Use it only for an
existing prototype baseline when the user names the exact targets and asks for
a local edit, such as a small Transform change or an explicit deletion of
existing prototype Actors. The operation must record:

- the current world, level, stage, baseline revision, and allowed target IDs;
- the allowed operation kinds, local zone or envelope, maximum changed-item
  count, wall-clock budget, save policy, and rollback target;
- compact protected references or digests for Landscape, water/stream,
  bridges, zone markers/registry, authoritative route or Navigation/collision
  sources, and fixed cameras or streaming boundaries when applicable;
- preconditions, target postconditions, persistence evidence, and the checks
  intentionally not run by this operation.

The initial default may target one level and up to eight explicitly named
existing Actors, but count is only a bound, not proof of safety. The operation
must fail closed when target ownership, protected scope, route semantics,
parent/child relationships, or the saved baseline are ambiguous. A building
move over Landscape may use a target-specific four-corner grounding
postcondition; it must not trigger a full Landscape inventory, and it must not
replace the four-corner rule with a center trace or average.

Use 120 seconds as the recommended wall-clock target for this local path when
the user has not supplied another budget. The user or project may set a
different explicit budget, but it covers discovery, queue or game-thread wait,
mutation, verification, save, and persistence re-read as one operation. On
budget expiry, stop before capture, broad review, or a retry and perform the
read-only state audit required below.

Use this order where the execution surface permits it:

`classify → compact inspect → local precondition check → one serialized transaction → in-memory postcondition → save → persistence re-read`

Saving before the in-memory postcondition is acceptable only when a compound
transaction enforces the same preconditions and postconditions and can roll
back on failure. Keep the game-thread work serialized. Cache the task-scoped
execution surface and schema rather than rediscovering it for every Actor, and
return a compact structural result rather than a viewport image for a
Transform-only edit.

Record two verdicts. `operation_verdict` reports whether the named edit,
protected-scope comparison, target postconditions, and save persistence passed.
`promotion_verdict` remains `unchanged` unless a separate promotion review is
requested and completed. A skipped camera capture, PIE run, independent visual
review, or broad Area Composition Plan/Translation review is
`NOT_RUN_BY_CONTRACT`, not a hidden `PASS` and not an operation failure when
those questions are outside the declared scope.

Reuse an accepted Area Composition Plan, Translation Contract, and current
stage without rerunning them only when their assumptions remain unchanged and
the protected snapshot is stable. Reopen the earliest responsible gate when a
target changes terrain, water, a bridge approach, an authoritative route,
zone-marker identity, typology-critical hierarchy, fixed-camera coverage,
runtime collision/navigation, or a declared composition tolerance. Gate reuse
means “the old decision still governs”; it never turns an unrecorded or
`UNKNOWN` baseline into `PASS`.

The fast path is a scope-risk reduction, not a safety removal. When its
preconditions cannot be established, when a protected system is touched, or
when the budget/transport state becomes ambiguous, exit before further
mutation, run a read-only state audit, and reclassify the work.

Keep the hot path bounded: initialize or discover the approved execution
surface once per task, read the relevant inventory once, validate the request
locally, perform one serialized transaction, verify the in-memory postcondition,
save only under the declared save policy, and re-read persistence once. Avoid
one tool round-trip per Actor or per property when a local batch can establish
the same postcondition.
Record setup, discovery, queue or game-thread wait, mutation, verification, and
background maintenance time separately. A time budget covers the whole
operation, not only the final setter call.

When a batch times out, returns an empty or ambiguous result, or exceeds its
budget, do not retry the same mutation. First run a read-only state audit and
classify the result as complete, partial, duplicated, unchanged, recoverable,
retired, or unknown. Then resume from a verified checkpoint, roll back the
verified target, or reopen the responsible gate. Preserve the baseline and the
failed attempt so that a later repair remains comparable.

Releasing this bounded workflow is separate from promoting the level or system
it operates on. A workflow may be released with its tests and guardrails
passing while the content remains `PENDING_EVIDENCE` or `INVALID_EVIDENCE`.
Report those states separately instead of calling a fast tool path a successful
production result.

## Experience hypothesis before spatial scale

A level can be readable, traversable, and visually consistent yet still fail to hold attention. Treat fun as a design hypothesis that must be made observable before broad layout or final content. The hypothesis is project- and genre-specific: exploration may depend on curiosity and voluntary discovery, while combat, stealth, puzzle, social, or narrative spaces may depend on different verbs and rewards.

Record at least:

- **Core pleasure:** what the player should enjoy doing repeatedly;
- **Repeated verbs:** the actions the space should invite, vary, and escalate;
- **Player question:** what the player wonders, pursues, or chooses to defer;
- **Agency and risk:** meaningful choices, uncertainty, cost, and recovery;
- **Reward and next hook:** what pays off the effort and what invites the next decision;
- **Emotional rhythm:** the intended sequence of curiosity, challenge, tension, release, and rest;
- **Failure hypothesis:** where boredom, confusion, repetition, or arbitrary frustration is most likely;
- **Evidence:** the smallest prototype or playtest observation that could disprove the hypothesis.

Do not reduce fun to a single score or infer it from visual quality alone. A functional graybox is valuable when it exposes a weak verb, missing choice, absent payoff, or broken rhythm while the cost of change is still low.

## Exploration mode and production mode

Use an exploration loop while the level's direction is still uncertain:

- prefer disposable primitives, rough terrain, temporary materials, and placeholder cues;
- test the player experience in runtime rather than inferring it from an editor camera;
- allow divergence from the plan when playtest evidence disproves an assumption;
- preserve failed iterations and the reason they were rejected.

Switch to a production loop only when the evidence supports the commitment:

- the intended player experience and scope are explicit;
- at least one representative POI or experience unit demonstrates the intended question, choice, tension, payoff, and next hook with cheap content;
- the playable blockout passes its hard traversal and readability checks;
- a representative visual slice reproduces the target look across more than one required view;
- asset families, materials, lighting, collision, audio integration, performance budgets, and ownership have viable rules;
- the user or designated approver has accepted the evidence package and its known limitations.

Confidence is therefore an outcome of repeatable evidence, not a feeling produced by one attractive screenshot. A short level can be production-ready while a larger level remains exploratory; promote only the smallest unit that has actually been proved.

## Review and promotion contract

Every intentional pause should answer the same questions:

1. What decision is being reviewed?
2. What is fixed for the next stage, and what is still allowed to change?
3. Which observations or measurements constitute success?
4. Who provides evidence, who reviews it, and who approves promotion?
5. What happens if the gate fails, including the rollback target and retained artifacts?

Use explicit states such as `PASS`, `FAIL`, `PENDING_EVIDENCE`, and `INVALID_EVIDENCE`. User approval is valuable product input, but it does not replace runtime evidence, performance evidence, or a clear record of what was approved. A later change may reopen an earlier gate when it alters the assumptions that gate established.

## Clarification policy

Ask only when a missing choice would materially change the result, create significant risk, or require new authority. Otherwise state a reversible assumption and proceed. Preserve assumptions in the final decision record so they can be corrected without reconstructing the work.

## Representative proof before scale

Before broad production, prove the riskiest representative slice of the work. It may be a gameplay loop, one network transition, a representative environment segment, an asset migration sample, a build target, or a procedural pattern. The slice must exercise the important boundaries and use final or representative conditions.

Do not scale a slice that passes only because it omits the difficult content, platform, lifecycle, or recovery case.

For level production, this usually means proving one playable route segment that includes a meaningful terrain transition, a POI or encounter with a player choice and payoff, a landmark, a boundary or reverse view, the intended player camera, and the asset families that will dominate the final map. A beautiful hero camera that omits traversal, decisions, contacts, repetition, or performance is not representative proof.

## Iteration by cause

For each failed gate:

1. Name the weakest observable outcome.
2. Identify the likely system-level cause.
3. Preserve a comparable baseline.
4. Change one major variable.
5. Repeat the same test.
6. Keep or revert based on evidence.
7. Record the transferable lesson and its limits.

After repeated failure of the same architecture or composition, require a documented reset rather than another polish pass.

## Recovery and completion

Plan checkpoints before bulk or difficult-to-reverse changes. Completion requires saved and persistent results, representative runtime behavior, acceptable warnings, viable performance, verified dependencies, and a truthful report of unresolved limitations.

## Common mistakes

- Implementing while requirements are still changing invisibly.
- Using a prototype's speed as proof of production suitability.
- Treating visual spectacle, traversal success, or difficulty as proof that the intended fun exists.
- Retrying a timed-out batch before checking partial results.
- Advancing because an individual command passed while the complete decision package is incomplete.
- Erasing failed iterations and losing causal evidence.

## Related topics

Philosophy; Project & System Architecture; World & Level Design; Validation, Testing & Debugging; Production Pipeline; Case Studies.
