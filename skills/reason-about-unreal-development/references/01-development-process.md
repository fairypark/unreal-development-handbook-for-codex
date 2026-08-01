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
| Spatial plan | Can the space and its responsibilities be understood before construction? | Annotated top-down or node map, zones, primary route, optional loops, focal hierarchy, landmarks, major reveals, boundaries, and known risks. | Revise the plan; do not hide uncertainty with detail. |
| Experience prototype | Does the proposed fun exist in one cheap, playable unit? | A POI or encounter prototype with an approach, reveal, player choice or verb, outcome or reward, and a next hook, tested with placeholders. | Return to the fun thesis or spatial plan; do not build the whole route to discover that the unit is empty. |
| Playable blockout | Does the space work as a game? | Runtime playtest with representative movement, scale, collision, route, sightlines, landmarks, pacing, and boundary behavior. | Return to the plan or blockout and retest from comparable conditions. |
| Visual feasibility slice | Can the visual target be produced consistently and within budget? | A small representative segment using real or representative asset families, materials, lighting, contacts, collision, audio intent, and target performance conditions. | Repair the visual language, asset kit, or pipeline; do not scale map-wide production. |
| Production content | Can the approved pattern scale without changing the design? | Content coverage, provenance, repeatable placement, ownership, integration checks, and a deviation log for each zone or chunk. | Stop scaling and reopen the affected design or feasibility gate. |
| Finish and release | Does the complete level meet player, quality, technical, and recovery targets? | Final traversal, visual, audio, collision, performance, persistence, packaging, and recovery evidence. | Return to the failing subsystem rather than applying unrelated polish. |

The purpose of a gate is not to prevent change. It is to make the cost and meaning of change explicit. A promotion records what is currently accepted, what remains risky, who can approve the next commitment, and which earlier gate must reopen when a later change invalidates its assumptions.

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
