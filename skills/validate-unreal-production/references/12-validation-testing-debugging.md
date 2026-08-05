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

## Operation health and gate-state semantics

Content correctness and workflow health are separate dimensions. A batch may
leave valid content while still failing its operational contract because it
used an unbounded number of calls, exceeded its time budget, lost its session
state, or cannot prove what happened. Record both verdicts and do not convert a
transport success into a content or promotion pass.

Use gate states consistently:

| State | Meaning | Required action |
| --- | --- | --- |
| `PASS` | The named criteria and evidence are complete under the stated conditions. | Continue only to the explicitly authorized next gate. |
| `FAIL` | A criterion or hard failure is contradicted. | Preserve the result, repair the responsible cause, or roll back. |
| `PENDING_EVIDENCE` | The result may be valid, but required evidence, review, or persistence has not yet been supplied. | Stop promotion; collect the named evidence or request the missing decision. |
| `INVALID_EVIDENCE` | The evidence cannot be used because its condition, authority, comparison, or capture integrity is invalid. | Repair the evidence condition before changing the product or repeating capture. |
| `PENDING_APPROVAL` | Required evidence exists, but the designated reviewer or approver has not completed the decision. | Keep mutation and promotion locked. |

For prototype automation, treat a time-budget breach, ambiguous response, or
unclassified partial batch as an operational `FAIL` until a read-only audit
proves a narrower state. Do not issue a blind retry. Record setup, discovery,
wait, mutation, verification, and background-maintenance time separately; if
the same task repeatedly spends more time in orchestration than in the named
change, change the workflow boundary before changing the content.

### Local operation verdict versus promotion verdict

Every bounded prototype operation records two independent results. The
`operation_verdict` answers whether the declared target allowlist, protected
scope, target postconditions, and save persistence passed. The
`promotion_verdict` answers whether a separately requested stage or production
promotion passed; it remains `unchanged` for an ordinary local edit. A
successful local operation therefore cannot silently become a level approval.

For `BOUNDED_PROTO_EDIT`, use a compact structural evidence package: exact
changed/deleted IDs, before/after Transforms, protected references or digests,
warnings, save state, elapsed/call counts, rollback status, and checks not run.
Visual capture, PIE, independent review, full Landscape inventory, and broad
Area Composition Plan or Translation review may be
`NOT_RUN_BY_CONTRACT` when their questions are outside the declared scope.
That state is neither `PASS` nor an operational failure; it is a truthful
boundary on what the operation did not attempt to prove.

Direct mutation of Landscape, water/stream, bridges, zone markers/registry,
fixed cameras, streaming boundaries, authoritative routes, or
Navigation/collision sources exits the fast path. A building move over
Landscape may remain local only when the target-specific four-corner grounding
postcondition is available and passes; a center trace, average, or incomplete
corner result is not sufficient.

## Gate contract for level work

For a level or environment, make the promotion sequence explicit rather than treating approval as a single late event:

`BOUNDED_PROTO_EDIT` is an operation envelope within the current stage, not an
additional promotion gate. Reuse the current Area Composition Plan,
Reference-to-Prototype Translation, and stage evidence only while their
assumptions remain unchanged. Reopen the earliest responsible gate when the
edit changes a plan-owned route, terrain, water/bridge relationship, zone
marker, typology-critical hierarchy, fixed-camera coverage, runtime
collision/navigation behavior, or recorded composition tolerance.

| Gate | What it must prove | Typical hard failures |
| --- | --- | --- |
| Direction | The concept and written brief preserve the intended player experience, priorities, and non-goals. | Contradictory intent, missing decision owner, or unresolved scope that would change the layout. |
| Area Composition Plan | Before the first cube or broad asset placement, a versioned record assigns zone boundaries and stable IDs, terrain elevations and steps, primary circulation, rivers and bridges, building footprints and typology hierarchy, and a stable-ID `DIAGNOSTIC_ONLY` overview-camera set. Its coverage matrix closes arrival, reverse, lateral, waterway/axis, elevation, and project-specific spatial risks with the smallest sufficient set, and records auxiliary player-height/FOV proxies plus the planned runtime-rig source. | Missing or retrospective plan; unreadable relationships; absent route, elevation, water crossing, footprint, camera authority, or coverage; reliance on one hero overview or an arbitrary camera count; typology approved by size alone; or an unowned critical dependency. |
| Reference-to-Prototype Translation | After the Area Composition Plan passes and before content-bearing prototype placement, a machine-readable contract records source versions, approval and authority; zone-level density, mass, typology, occupancy, frontage, spacing, route, elevation, water/bridge, shade/void, hierarchy, and silhouette requirements; planned trace entries; camera-specific comparisons; tolerances; hard failures; and an explicit placement decision. | Unresolved source conflict; qualitative-only target; missing or invalid schema; unmapped proxy group, path, void, or terrain change; empty tolerance; Actor-count-only approval; or broad placement without contract `PASS`. |
| Concept-to-Asset Readiness | After Stage 2a, a machine-readable contract traces functional asset-family demand to approved sources and zones; records project and ownership-confirmed inventory, candidates, supply routes, authorization, license, compatibility, dependencies, total integration cost, evidence, fallback, and exact versions; and separates `ASSET_PLAN_READY`, `VISUAL_SLICE_READY`, and `PRODUCTION_DRESSING_READY`. | Public listing treated as ownership; acquired pack treated as production-ready; missing family coverage or transition pieces; unauthorized external action; unresolved license, compatibility, dependency, or cost; Visual Slice used to authorize map-wide dressing; or an unapproved concept substitution. |
| Experience prototype | A cheap POI or encounter unit demonstrates the fun thesis through approach, reveal or refusal, player choice or verb, outcome or reward, and a next hook. | The player can traverse the unit but has no meaningful question, choice, payoff, or reason to continue; repeated beats are uninteresting or obstruction feels arbitrary. |
| Playable blockout | Runtime movement through the rough space is readable, traversable, and representative of the intended pacing through the representative player controller and actual runtime camera rig, including project-relevant boom, offset, pitch, collision, and retraction behavior. | Static height/FOV proxy offered as authoritative evidence; broken traversal; misleading landmarks; camera-rig or capsule failure; inaccessible objective; boundary leak; or unacceptable wrong-turn pattern. |
| Visual feasibility | A small representative slice can meet the target visual language, asset quality, asset density, player-facing composition, and technical budget together when judged through the Stage 5-approved runtime camera rig. | Overview- or proxy-camera approval; hero-only success; inconsistent materials or scale; unusable asset kit; unverified contacts or collision; or budget failure. |
| Production | The approved pattern scales across ordinary and focal areas without silently changing the design contract. | Repeated contact or readability failures, untracked deviations, missing ownership, or dependency and integration failure. |
| Release | The complete level satisfies functional, visual, audio, collision, performance, persistence, packaging, and recovery requirements. | Any blocking hard failure, stale or invalid evidence, unrecoverable build state, or unresolved production blocker. |

The exact gate names may differ by project, but the Area Composition Plan, Reference-to-Prototype Translation Gate, and Concept-to-Asset Readiness decisions must remain distinct and recorded. Plan `PASS` advances only to translation; translation `PASS` plus an explicit placement decision releases content-bearing prototype mutation. `ASSET_PLAN_READY` permits cheap prototype work with planned supply gaps, while `VISUAL_SLICE_READY` and `PRODUCTION_DRESSING_READY` separately authorize the exact representative and production scopes. The invariant is that each gate retires the risk that would become more expensive at the next stage. User or stakeholder approval records product intent; it does not waive runtime, license, acquisition authority, performance, dependency, or recovery evidence.

Use the [Reference-to-Prototype Translation Contract schema](../../design-unreal-worlds-and-levels/references/reference-to-prototype-translation.schema.json) and [template](../../design-unreal-worlds-and-levels/references/reference-to-prototype-translation.template.json), or validate a project equivalent against the same semantic requirements. The pre-placement contract and every post-mutation audit must remain linked by stable source-requirement, zone, prototype-element, camera, and evidence IDs.

Use the [Concept-to-Asset Readiness Contract schema](../../design-unreal-content-architecture/references/concept-to-asset-readiness.schema.json) and [template](../../design-unreal-content-architecture/references/concept-to-asset-readiness.template.json), or a project equivalent. Validate one coverage decision per demand, demand-to-candidate traceability, entitlement or provenance, external authorization, license, compatibility, dependencies, representative and production evidence, exact selected versions, gate scope, and reopening behavior. Discovery, ownership, acquisition, staging, representative approval, and production approval are different evidence classes.

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

For a `BOUNDED_PROTO_EDIT` that does not change those plan-owned assumptions,
use the cheapest credible local checks: one compact target/protected snapshot,
one bounded mutation, target and protected postconditions, and saved-state
persistence. Do not attach a fixed-camera capture, full visual review, PIE, or
independent review merely because the level contains visual content. If the
target changes route, collision, navigation, bridge approach, water bank,
playable surface, or building support, reclassify the operation and run the
relevant higher-cost evidence instead of using the time budget to waive it.

For a composition-changing prototype batch, set the translation contract to `POST_MUTATION_AUDIT` and withhold the next broad batch until reference/plan/prototype deviations are recorded. Compare fixed overviews under the same transform, crop, projection, resolution, and measurement basis for their assigned macro metrics. Beginning at Playable Blockout, separately compare route samples through the actual runtime rig for perceived distance, enclosure, occlusion and reveal, route continuity, hierarchy, clearance, and recovery. An out-of-tolerance zone, lost shaded or empty space, hierarchy reversal, path discontinuity, or prohibited silhouette reopens the earliest responsible gate even when the total Actor count matches.

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

## Builder self-inspection and AI-assisted spatial evidence

Builder self-inspection is an inner quality loop, not an acceptance role:

`mutate -> re-read changed state -> inspect -> correct -> repeat postconditions`

The builder may use a screenshot, viewport capture, log, count, bounds query,
warning scan, or targeted runtime check to find visible and structural defects
before review. Bind each artifact to its capture conditions and the exact
changed state. Record corrections and repeat the failed check; do not silently
replace the first candidate with a cleaner image. When independent acceptance
is required, the evaluator remains read-only and receives the raw before,
failed, corrected, and final evidence without the builder's intended verdict.
When independence is unavailable, label the result as self-review and leave the
dependent promotion pending.

A screenshot can support only what is visible from that viewpoint and state.
It cannot alone prove occluded geometry, back-side contact, collision,
navigation, save/reopen persistence, regeneration, packaged behavior,
performance, or viewpoints it did not capture. Screenshot-guided correction is
therefore construction evidence rather than production approval.

For AI-assisted placement or procedural generation, validate one
representative batch before scaling and classify at least these spatial failure
signatures:

- pivot or origin mismatch;
- local-axis or orientation mismatch;
- overlap or insufficient separation under final transformed mesh bounds;
- incomplete terrain contact or grounding;
- gameplay, navigation, camera, or maintenance-clearance violation.

Use stable output identity, final Transform, resolved asset bounds, contact
samples, and declared clearance envelopes as structural evidence. Center-point
distance, aggregate count, semantic search confidence, and a favorable image
are not equivalent substitutes. A human move, rotation, deletion, or
replacement becomes a tracked authored exception or a correction to the
responsible generator; it cannot retroactively pass the original candidate.
Chapter 09 owns the generation-lifetime, regeneration, and override-provenance
contract.

## Evidence integrity

Use stable, comparable conditions and preserve baseline, candidate, and accepted evidence separately. Bind evidence to the relevant world, configuration, viewpoint, time, version, camera ID, evidence class, and stage authority. For Stages 2–4, preserve the overview-set coverage matrix and bind auxiliary player-height checks to the recorded height above local ground and FOV; accept those static proxies only as gross plausibility checks. At Stage 5 and later, bind gameplay-camera evidence to the representative player controller, actual runtime camera-rig asset or class, configuration version, and project-relevant boom, offset, pitch, collision, and retraction state. From Visual Feasibility onward, accept player readability, asset-density, and visual-composition decisions only from that runtime rig. Reject stale, undersized, overlay-contaminated, unsettled, mismatched, silently overwritten, or authority-mismatched evidence. Overview-only evidence is always invalid as player visibility, scale, readability, or typology proof, even though the overview set is the primary macro-composition diagnostic during prototyping.

Bind reference-to-prototype evidence additionally to the source artifact and crop, source requirement, Area Composition Plan, translation contract, zone, prototype element, measurement basis, allowed deviation, and realized prototype versions. Reject trace-orphaned evidence even when its image is otherwise usable, and preserve the previous same-camera comparison instead of silently overwriting it.

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
- Letting Area Composition Plan `PASS` authorize prototype placement before a valid source registry, zone-level quantitative contract, traceability map, tolerances, and explicit Stage 2a placement decision exist.
- Passing reference fidelity from total Actor count while distribution, footprint, frontage, gaps, preserved shade or voids, hierarchy, route continuity, water/bridge relationships, or silhouette fails.
- Comparing a changed prototype from a new camera, omitting the reference or plan version, or overwriting the last accepted same-condition deviation record.
- Treating an early static player-height/FOV proxy as an exact runtime rig, fine-tuning prototype detail to it, or carrying its approval authority into Stage 5 or the Visual Feasibility Slice.
- Treating test transport success as test outcome success.
- Treating a command, graph, or batch completion message as proof that the intended state and postconditions exist.
- Treating a builder screenshot, screenshot-guided correction, or self-review as independent acceptance.
- Scaling AI-assisted spatial output after checking only centers, counts, or one favorable view instead of final transformed bounds, grounding, and clearance.
- Silently baking a human correction into generated output and using the corrected result as evidence that the original candidate passed.
- Treating `operation_verdict: PASS` as `promotion_verdict: PASS`, or treating `NOT_RUN_BY_CONTRACT` as hidden evidence.
- Replaying the Area Composition Plan, fixed-camera, or PIE gates for an unchanged local prototype edit while failing to detect a route, bridge, zone, or Landscape touch.
- Allowing an explicit target delete to expand into wildcard cleanup or a broad rebuild.
- Repeating a failed iteration without recording a changed cause hypothesis, invariant, or detection rule.
- Reporting “not observed” as “not reproducible” when the same test conditions were not repeated.
- Overwriting failed audits or evidence.

## Related topics

Development Process; Procedural Systems & PCG; Rendering; Performance & Scalability; Production Pipeline; AI-Assisted Development; Case Studies.
