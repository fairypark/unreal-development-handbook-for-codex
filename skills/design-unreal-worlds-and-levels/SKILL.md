---
name: design-unreal-worlds-and-levels
description: Design, scope, or review Unreal worlds, levels, and environments through player experience, spatial composition, routes, terrain, streaming, environmental storytelling, gameplay space, content readiness, production constraints, and validation. Use for new maps, open worlds, environment plans, level-quality recovery, concept-to-production decisions, or a declared BOUNDED_PROTO_EDIT on an accepted prototype. Do not use for an undeclared isolated Actor operation.
---

# Design Unreal Worlds and Levels

Design a playable place rather than a camera-facing diorama. Convert the request into observable spatial and production targets before building.

## Load the Handbook chapter

Read [04-world-level-design.md](references/04-world-level-design.md) for every world, level, or environment design or review. Use its brief, representative-slice, terrain, contact, 360-degree continuity, and validation guidance before handing work to an Editor execution layer.

## Classify an accepted-prototype patch before broad gates

Classify an edit as `BOUNDED_PROTO_EDIT` before applying the broad staged workflow when it changes only an already accepted prototype inside the current level: explicit existing Actor IDs, a local transform or scale, or an explicit named deletion. It must have a declared local envelope, target allowlist, change and wall-clock budget, save intent, rollback path, and compact protected snapshot; when no budget is supplied, use the 120-second recommended target. Use the existing stage record, accepted Area Composition Plan, Stage 2a translation decision, zone-marker inventory, and Landscape/grounding evidence as predecessor evidence only when their assumptions and protected scope are unchanged. This is a fast operation mode, not a promotion or Stage 2a bypass: it may reuse those gates but must not silently turn them into new approval.

Keep the full workflow for new content, broad or wildcard edits, ambiguous ownership, or any direct change to Landscape, water or drainage, bridges, zone markers, authoritative routes or navigation, streaming, camera/playable composition, or other plan-owned systems. A building move over Landscape remains bounded only when the target-specific four-corner grounding check is available; center or average height is not a substitute. Report a local `operation_verdict` separately from the unchanged `promotion_verdict`; capture, PIE, and broad visual review can be `NOT_RUN_BY_CONTRACT` when outside scope. If a protected or plan-owned system is touched, assumptions change, the baseline is dirty or unclear, the operation exceeds its budget, or transport leaves an ambiguous/partial state, exit the fast path and return a read-only state audit to the normal stage gates.

## Enforce the staged workflow

For every AI-led level, world, environment, terrain, route, POI, or map-wide dressing task that is new, broad, or plan-affecting, treat the chapter's **Mandatory AI execution contract** and numbered concept-to-production workflow as binding. Before any Editor or coding handoff, create or update an inspectable workflow record, identify the current stage and predecessor evidence, and define the stage's postconditions, approver, and rollback target. Work only within the current stage, record `PASS`, `FAIL`, `PENDING_EVIDENCE`, or `INVALID_EVIDENCE`, and advance only after `PASS` plus the required promotion decision. Stop on missing or failed evidence; do not silently skip or combine stages, and reopen an earlier stage when a later change invalidates its assumptions. In particular, Stage 2 `PASS` does not authorize prototype placement by itself: Stage 2a **Reference-to-Prototype Translation Gate** must have a machine-readable source registry, zone-level quantitative contract, planned traceability entries, and an explicit placement decision before the first content-bearing prototype mutation. When dependent strata such as rocks or hardscape plus grass or ground cover are in scope, Stage 2a must also carry a `Dependent-Strata Strategy Gate` decision before the first relevant generator or foliage mutation; invoke the PCG design Skill for that decision and do not infer a method from tool success. For small or disposable work, adjacent stages may be combined only when declared before mutation and each stage's question and evidence remains explicit. A declared `BOUNDED_PROTO_EDIT` follows the bounded entry/exit contract above and preserves the current stage record; it is not a new stage or a silent promotion.

Before any prototype mutation, also apply the chapter's bounded iteration
contract: classify the operation as a bounded edit, read-only diagnostic audit,
explicit promotion review, or separately confirmed maintenance rebuild; set a
change and wall-clock budget; batch discovery and validation; and define
preconditions, postconditions, save policy, and rollback. A short level request
must not silently invoke a broad builder, per-item dispatch chain, or blind
evidence retry. On timeout or ambiguous transport, stop for a read-only state
audit before resuming or rolling back.

## Create the level brief

1. Define player fantasy, emotional tone, setting, scale, route, and target platform.
2. Define the fun thesis: core pleasure, repeated verbs, player questions, meaningful choices, risks, rewards, and intended emotional rhythm.
3. Identify the POI hierarchy and experience-density hypothesis, including approach, reveal or refusal, interaction, payoff, and next hook.
4. Identify the risk-covering set of arrival, reverse, lateral, waterway/axis, elevated, and other overview relationships required to understand the whole space; assign stable camera IDs rather than relying on one hero overview.
5. Record the player tracking-camera height above local ground and FOV for early static scale checks, plus the intended runtime camera rig and its Stage 5 validation source when known.
6. Describe focal hierarchy, reveal order, optional loops, boundaries, sightlines, and expansion directions.
7. Assign terrain height-band roles, traversal transitions, water and drainage logic, architecture vocabulary, ecology strata, and material palette.
8. Record streaming, performance, content, schedule, and collaboration constraints.
9. State construction provenance and allowed reuse.

## Gate production scale

- Treat the concept review and annotated top-down plan as intent and spatial gates, not as disposable presentation documents.
- Between concept review and any cube or graybox prototype, create, version, and record an **Area Composition Plan**. It must show zone boundaries and stable IDs, terrain elevations and steps, primary circulation, rivers and bridges, building footprints and typology hierarchy, and a risk-covering set of fixed overview cameras with stable IDs and declared relationships. Cover arrival, reverse, lateral, waterway/axis, elevation, and any project-specific blind spots with the smallest sufficient set rather than one hero overview or a universal camera count. Do not create the first cube blockout or begin broad asset placement while this artifact or its review state is missing.
- After the Area Composition Plan passes, complete Stage 2a before placing content-bearing prototype geometry. Inventory every concept image, plan, elevation, and reference with version, approval, authority scope, and priority; extract zone-level ranges for density, building and roof masses, typology mix, footprint occupancy, frontage continuity, spacing, route widths, elevation changes, water and bridges, preserved shade and voids, hierarchy, and prohibited silhouettes. Resolve source conflicts instead of averaging them silently.
- Use the machine-readable [Reference-to-Prototype Translation Contract schema](references/reference-to-prototype-translation.schema.json) and [template](references/reference-to-prototype-translation.template.json), or a project-equivalent format that preserves the same required fields and semantics. Every prototype array, architecture proxy group, route, water or bridge proxy, reserved void, and terrain change must have a stable trace entry back to the approved source requirement it implements. Missing quantitative contracts, unresolved source authority, unmapped placement groups, or a non-`PASS` decision keep broad placement locked.
- Assign every major zone a stable ID, display name, role, bounds or anchor, and semantic color before prototyping. Keep inspectable zone markers visible from the first prototype mutation through the completed production-asset placement gate; retire them only in a recorded cleanup step after the zone inventory and final placement evidence pass.
- Give every zone marker a numeric ID and an ASCII fallback in addition to any localized display name, and keep that fallback readable when the active local font cannot render the localized text.
- For typology-critical spaces, approve the spatial sequence and hierarchy rather than size alone. A palace must read through the gate -> outer court -> middle gate -> central courtyard -> main hall axis and courtyard hierarchy; a fortress- or castle-like silhouette is a hard failure.
- Prove a cheap POI or encounter unit that demonstrates the fun thesis before broad blockout or final-content commitment; for a small level this may be combined with the blockout, but the evidence remains explicit.
- Complete a playable blockout gate before map-wide dressing, then prove a representative visual feasibility slice before committing the broader asset budget.
- Confirm that available assets and systems can support the selected direction at final scale.
- Prove a representative playable slice before broad duplication or dressing.
- Validate terrain and route structure before using architecture or props to hide spatial weakness.
- Keep camera authority stage-specific. In the Area Composition Plan and terrain/macro prototype, use the fixed overview set as the primary diagnostic for whole-area composition, zone distribution, footprint, density, terrain relief, axes, water/bridge relationships, and coverage; label every overview `DIAGNOSTIC_ONLY` and never use it to approve player visibility, scale, readability, or typology. Use static cameras at the recorded player height and FOV only as auxiliary checks that can reject gross building-scale, route-width, slope, or occlusion failures; do not fine-tune player-view composition or detail at this stage.
- At Stage 5 Playable Blockout, require the representative player controller and actual runtime camera rig—for example, `BP_ThirdPersonCharacter` and its `FollowCamera`/SpringArm chain—to validate authoritative gameplay-camera behavior, including boom length, socket or shoulder offset, pitch, and SpringArm collision or retraction where applicable. From Stage 6 Visual Feasibility onward, judge player readability, asset density, and visual composition from that runtime rig; fixed prototype cameras and overviews remain supporting diagnostics only.
- For outdoor map level-design prototypes, use a minimal Landscape terrain as the actual playable floor by default; use another floor only when a specific user or stakeholder request explicitly overrides that default.
- Treat the 40-second interval as a calibrated open-world exploration heuristic, never as a universal spacing law or a reason to fill intentional quiet with low-value content.
- Use functional audio and collision proxies early when they affect navigation or interaction; reserve final authoring and full collision auditing for the later integration and polish passes.
- Scale approved systems and decision patterns, not merely Actor counts.
- Finish reverse views, boundaries, contacts, and reachable directions as deliberately as hero views.

## Validate the level

Define evidence for the fun thesis, POI purpose and flow, experience density, tension and release, player choice, spatial readability, traversal, collision, contact, environmental coherence, streaming, performance, and representative views. Preserve same-condition reference/plan/prototype deviation records after every composition-changing prototype batch. Overview evidence may approve only its assigned macro metrics; player distance, occlusion, route continuity, and perceived hierarchy require the stage-authorized runtime rig. Validate zone distribution, preserved shade and voids, hierarchy, frontage and path continuity rather than accepting aggregate Actor-count parity. Treat a single hard failure as blocking even when averages are favorable. Compare failed repairs from fixed conditions, change one major variable, and preserve reusable lessons without copying project-specific coordinates or asset accidents.

Keep Editor execution separate. Use available Unreal Editor skills for Landscape, PCG, Foliage, materials, lighting, collision, capture, and save operations only after the brief and gates are explicit.
