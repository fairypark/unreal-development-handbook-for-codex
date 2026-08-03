# 12 — Validation, Testing & Debugging

## Purpose

Define a shared quality system that distinguishes successful execution, correct behavior, production readiness, and trustworthy evidence.

## Intent

Make success falsifiable before implementation. Diagnose failures by cause and preserve enough evidence to compare, recover, and prevent regression.

## Validation strategy

1. Convert intent and requirements into observable criteria.
2. Define test conditions, configuration, data, platform, and baseline.
3. Separate hard failures from scored qualities and acceptable warnings.
4. Assign who produces evidence, who reviews it, and who approves promotion.
5. Define gate states such as `PASS`, `FAIL`, `PENDING_EVIDENCE`, and `INVALID_EVIDENCE`.
6. Require topic-specific checks in addition to the shared validation system.

## Gate contract for level work

For a level or environment, make the promotion sequence explicit rather than treating approval as a single late event:

| Gate | What it must prove | Typical hard failures |
| --- | --- | --- |
| Direction | The concept and written brief preserve the intended player experience, priorities, and non-goals. | Contradictory intent, missing decision owner, or unresolved scope that would change the layout. |
| Area Composition Plan | Before the first cube or broad asset placement, a versioned record assigns zone boundaries and stable IDs, terrain elevations and steps, primary circulation, rivers and bridges, building footprints and typology hierarchy, and a stable-ID `DIAGNOSTIC_ONLY` overview-camera set. Its coverage matrix closes arrival, reverse, lateral, waterway/axis, elevation, and project-specific spatial risks with the smallest sufficient set, and records auxiliary player-height/FOV proxies plus the planned runtime-rig source. | Missing or retrospective plan; unreadable relationships; absent route, elevation, water crossing, footprint, camera authority, or coverage; reliance on one hero overview or an arbitrary camera count; typology approved by size alone; or an unowned critical dependency. |
| Experience prototype | A cheap POI or encounter unit demonstrates the fun thesis through approach, reveal or refusal, player choice or verb, outcome or reward, and a next hook. | The player can traverse the unit but has no meaningful question, choice, payoff, or reason to continue; repeated beats are uninteresting or obstruction feels arbitrary. |
| Playable blockout | Runtime movement through the rough space is readable, traversable, and representative of the intended pacing through the representative player controller and actual runtime camera rig, including project-relevant boom, offset, pitch, collision, and retraction behavior. | Static height/FOV proxy offered as authoritative evidence; broken traversal; misleading landmarks; camera-rig or capsule failure; inaccessible objective; boundary leak; or unacceptable wrong-turn pattern. |
| Visual feasibility | A small representative slice can meet the target visual language, asset quality, asset density, player-facing composition, and technical budget together when judged through the Stage 5-approved runtime camera rig. | Overview- or proxy-camera approval; hero-only success; inconsistent materials or scale; unusable asset kit; unverified contacts or collision; or budget failure. |
| Production | The approved pattern scales across ordinary and focal areas without silently changing the design contract. | Repeated contact or readability failures, untracked deviations, missing ownership, or dependency and integration failure. |
| Release | The complete level satisfies functional, visual, audio, collision, performance, persistence, packaging, and recovery requirements. | Any blocking hard failure, stale or invalid evidence, unrecoverable build state, or unresolved production blocker. |

The exact gate names may differ by project, but the Area Composition Plan must remain a distinct, recorded gate between concept direction and prototype geometry. The invariant is that each gate retires the risk that would become more expensive at the next stage. User or stakeholder approval records product intent; it does not waive runtime, performance, dependency, or recovery evidence.

For typology-critical spaces, define hard failures before blockout. A palace is not approved by approximate building size: its gate -> outer court -> middle gate -> central courtyard -> main hall axis and courtyard hierarchy must read from gameplay views. A fortress- or castle-like silhouette is a hard failure. Use zone markers with a numeric ID plus ASCII fallback throughout prototype and production placement so missing localized glyphs cannot erase the evidence label.

## Cost-aware validation

Use the cheapest credible test for each unknown, then increase fidelity only when the result justifies it. A paper plan can expose a missing zone relationship; a graybox can expose scale and wayfinding; a representative visual slice can expose asset, material, lighting, pipeline, and performance risk. Map-wide final dressing is the wrong instrument for discovering any of those problems.

When a gate fails:

1. Name the weakest observable outcome and the evidence that shows it.
2. Identify the earliest responsible assumption or system.
3. Preserve the accepted baseline and failed candidate.
4. Change one major variable or one coherent cause family, or reopen the documented gate.
5. Repeat the same test conditions before judging the repair.

Do not spend a later-stage budget to defend an earlier-stage decision. If the visual feasibility slice fails, repair the kit or visual rules before dressing the map. If dressing reveals a route problem, return to the blockout instead of accumulating decorative exceptions.

## Experience validation

Validate the level's fun hypothesis as a sequence of observable player experiences, not as a late opinion about whether the map feels good. The appropriate evidence depends on the genre, but it should show that the intended verbs, choices, tension, and rewards are present while the content is still cheap to change.

Use a POI or encounter unit as the smallest credible test:

`approach → question or reveal/refusal → player choice or repeated verb → interaction/encounter → outcome or reward → exit/next hook`

Collect a mixed evidence package:

- **Behavioral evidence:** time to the next meaningful change, route choice, looking or investigating, voluntary deferral and return, interaction or encounter completion, abandonment, and behavior after the reward;
- **Qualitative evidence:** whether players can state what they were curious about, what they expected, when anticipation became tension, whether the payoff felt earned, and where they felt bored, confused, or arbitrarily blocked;
- **Design evidence:** whether each beat supports the fun thesis and whether the sequence offers meaningful variation rather than only more objects, enemies, distance, or difficulty.

Treat the 40-second interval as a hypothesis for suitable open-world exploration contexts. Report the actual distribution of time to meaningful change and explain intentional quiet sections instead of forcing a uniform interval. A long stretch is acceptable when it creates scale, recovery, contrast, anticipation, or a chosen detour; it is a failure when it is merely unexamined travel.

Hard failures include a POI with no discernible purpose or payoff, repeated identical beats, unintentional empty travel, a reveal that never resolves, a reward disconnected from the player's effort, mandatory obstruction with no meaningful choice, or final assets being used to disguise an unvalidated experience unit. When a test fails, return to the fun thesis, POI plan, or blockout before expanding content.

## Testing layers

- Static structure, schema, dependency, and naming checks.
- Unit or domain tests for deterministic logic.
- Integration tests for boundaries, lifecycle, data flow, and services.
- Asset, Blueprint, build, and automation tests.
- PIE or runtime scenarios for representative behavior and traversal.
- Experience and playtest evidence for the fun thesis, POI flow, meaningful-change timing, player choice, tension, and payoff.
- Visual evidence for rendering, composition, contact, and continuity.
- Iteration records distinguish symptoms, causes or hypotheses, false assumptions, changed invariants, new checks, same-condition evidence, and recurrence status.
- Spatial audits classify active, unapproved, hidden-recoverable, and retired content separately rather than merging their results.
- Performance and scalability measurements under representative load.
- Cook, package, clean-environment, migration, and recovery checks.

## Evidence integrity

Use stable, comparable conditions and preserve baseline, candidate, and accepted evidence separately. Bind evidence to the relevant world, configuration, viewpoint, time, version, camera ID, evidence class, and stage authority. For Stages 2–4, preserve the overview-set coverage matrix and bind auxiliary player-height checks to the recorded height above local ground and FOV; accept those static proxies only as gross plausibility checks. At Stage 5 and later, bind gameplay-camera evidence to the representative player controller, actual runtime camera-rig asset or class, configuration version, and project-relevant boom, offset, pitch, collision, and retraction state. From Visual Feasibility onward, accept player readability, asset-density, and visual-composition decisions only from that runtime rig. Reject stale, undersized, overlay-contaminated, unsettled, mismatched, silently overwritten, or authority-mismatched evidence. Overview-only evidence is always invalid as player visibility, scale, readability, or typology proof, even though the overview set is the primary macro-composition diagnostic during prototyping.

When independent acceptance matters, keep the evaluator read-only and withhold the builder's intended verdict or persuasive self-assessment. A focused target pass closes only that target; unresolved hard failures continue to block full acceptance.

## Cause-based debugging

Name the weakest observable system, form a testable cause hypothesis, change one major variable or one coherent cause family, repeat the same test, and keep or revert based on evidence. Fix invalid evidence before changing the product. After repeated failure of one architecture or composition, require a documented reset rather than cosmetic iteration. A cause family may require coordinated changes—for example, moving several blockers that share one route-clearance failure—but unrelated systems should not be changed in the same iteration.

### Iteration learning record

Every non-trivial iteration should leave a short, comparable record:

- observed symptom and its measurable evidence;
- confirmed root cause, or a clearly labelled hypothesis with confidence;
- the previous assumption that proved false or incomplete;
- the system and observable invariant changed;
- the new detection rule, validation query, or automation postcondition added;
- the same-condition recheck method and evidence;
- whether the symptom recurred, did not recur, or was not yet tested;
- the next prevention rule, remaining risk, and whether the lesson is a project rule or a handbook candidate.

“Did not recur” is valid only when the same relevant camera, runtime, data, and validator conditions were repeated. “Not yet tested” must remain distinct from success. If the same failure signature survives two iterations without a new cause hypothesis, invariant, or validation rule, pause the loop and reset or replace the responsible system instead of repeating cosmetic changes.

## Definition of done

Require functional correctness, maintainability, production readiness, performance viability, edge-case behavior, persistence, recovery, acceptable warnings, saved state, experience evidence appropriate to the design, and truthful reporting of limitations. No collection of individually passing commands may substitute for the complete decision package.

## Common mistakes

- Defining success after seeing the result.
- Calling a level fun because it is beautiful, traversable, difficult, or full of content without testing the intended player experience.
- Measuring density only by object count or applying a fixed interval without accounting for movement, genre, intentional quiet, or player choice.
- Testing the whole map while skipping the smaller POI or encounter unit that actually produces the proposed fun.
- Averaging away a failed category.
- Using new camera or test conditions to hide regression.
- Using a high overview camera to approve player visibility or spatial readability.
- Using one attractive overview instead of a stable-ID set that covers the macro relationships and risks named by the plan.
- Treating an early static player-height/FOV proxy as an exact runtime rig, fine-tuning prototype detail to it, or carrying its approval authority into Stage 5 or the Visual Feasibility Slice.
- Treating test transport success as test outcome success.
- Treating a command, graph, or batch completion message as proof that the intended state and postconditions exist.
- Repeating a failed iteration without recording a changed cause hypothesis, invariant, or detection rule.
- Reporting “not observed” as “not reproducible” when the same test conditions were not repeated.
- Overwriting failed audits or evidence.

## Related topics

Development Process; Rendering; Performance & Scalability; Production Pipeline; AI-Assisted Development; Case Studies.
