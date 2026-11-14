# 16 — Case Studies

## Purpose

Convert real Unreal outcomes, failures, migrations, optimizations, and production incidents into evidence-backed applied reasoning without turning anecdotes into universal recipes.

## Decision contrast: A useful lesson needs a supported mechanism and a limit

**Evidence class:** constructed teaching scenario; no measured production outcome is claimed.

**Situation.** A before/after scene improves after geometry, materials, distribution, and lighting all change. A second small trial changes only one material under comparable conditions.

**Choice and reason.** The broad result can support a scoped outcome and several causal hypotheses. The narrower trial can support a more specific material explanation within its conditions. Retain both, with their evidence classes and uncertainty.

**When the choice changes.** Even a controlled local comparison does not prove whole-project performance or universal parameter values. A well-explained failed experiment can teach a better decision than a flattering but untraceable success story.

**Smallest useful test.** Separate observation from interpretation, name competing causes, and propose a counterexample. Test the extracted decision on a changed-context exercise before turning it into general guidance.

## Admission criteria

A case belongs here only when it records:

- original intent and stakeholders;
- project context and constraints;
- alternatives and trade-offs;
- selected decision and factual implementation scope;
- predefined or reconstructable success criteria;
- evidence, outcomes, failures, and side effects;
- recovery or rollback where applicable;
- transferable lessons and limits.

If evidence is missing, publish an investigation note or candidate case rather than a completed case study.

## Case structure

1. **Problem and intent** — what outcome mattered and why.
2. **Context and constraints** — platform, scale, schedule, content, team, compatibility, and risk.
3. **Initial state** — relevant architecture, assets, workflow, and baseline evidence.
4. **Alternatives** — options considered and reasons for rejection.
5. **Decision** — selected design and expected trade-offs.
6. **Implementation scope** — factual changes without Tool tutorial detail.
7. **Validation** — comparable evidence and hard failures.
8. **Outcome** — improvements, regressions, cost, and unresolved risk.
9. **Recovery and follow-up** — rollback, repair, or future research.
10. **Lessons** — cause-level rules, applicability, and non-applicability.

## Candidate patterns requiring evidence

Use retained cases alongside the decision contrasts at the start of each domain chapter. Before reading a case's decision, ask what matters, which alternative seems appropriate, and what evidence would change that choice. After reading, compare the reasoning rather than memorize the selected implementation. Change one important condition and explain whether the recommendation still applies.

An observed failure can be useful before its recovery is proved. Keep the failed outcome, causal hypotheses, proposed repair, and verified recovery separate. A constructed contrast can teach an option that has not been executed, but must remain labeled as a teaching scenario. Neither status grants production authority.

The migrated Editor guidance suggests useful future cases, but these remain candidates until source artifacts are preserved:

- A flat environment that dressing could not repair, followed by a terrain and route reset.
- Uniform procedural scatter replaced by layered ecology and explicit exclusions.
- Collision repaired without deleting visually approved placement.
- A weak representative slice blocked before map-wide scaling.
- Overlapping procedural candidates invalidating a comparison.
- Fog or lighting polish failing to solve missing midground composition.
- A reused production asset requiring revalidation in a new project context.

## Investigation note: unbounded prototype loops and dispatch amplification

**Status:** evidence-backed workflow case; the workflow was released, but the
level itself remained `PENDING_EVIDENCE`. The case records a transferable
process correction, not a claim that the level passed production promotion.

### Problem and intent

In a small level-design prototype, a seemingly narrow instruction could take
approximately thirty minutes to reach a trustworthy result. The intent was to
make the next spatial experiment cheap enough to repeat: a designer should be
able to test one hypothesis, inspect the result, and decide whether to keep,
repair, or discard it without triggering a full rebuild or an evidence loop.

### Context and initial state

The project combined a live Unreal Editor, a remote or in-process execution
boundary, a large existing level, a destructive blockout builder, fixed-camera
evidence, and background Derived Data Cache maintenance. The initial
interaction pattern
mixed tool discovery, per-item inspection, broad mutation, structural checks,
capture attempts, and retries in one task. A representative log window
contained dozens of individual dispatches, repeated tool descriptions, and a
long gap without a trustworthy state transition. Map saves themselves were
short, while background cache scanning and evidence settling were separate
sources of delay.

### Cause analysis and alternatives

The dominant process causes were dispatch amplification, an unbounded mutation
boundary, and failure to distinguish diagnosis from promotion. A full rebuild
was too destructive for ordinary prototype iteration; repeated per-item calls
were too expensive for a bounded batch; and retrying unsettled evidence could
not repair the evidence condition. Background cache work was a secondary
environment cost, not a reason to rerun the content mutation.

The alternatives were to increase timeouts, retry the existing sequence, or
make the editor faster. Those options would have hidden partial state and
preserved the same failure mode. The selected alternative was to redesign the
loop around bounded edit, diagnostic audit, promotion review, and separately
confirmed maintenance-rebuild responsibilities.

### Decision and implementation scope

The corrective design introduced a machine-readable iteration contract,
bounded mutation and diagnostic responsibilities, explicit preconditions and
postconditions, transactional or checkpoint-based recovery, and a separate
confirmation path for broad reconstruction. Tool discovery and diagnostics
were batched where the execution surface allowed it. The workflow record also
captured elapsed time, call-count, redundancy, rollback, persistence, and
evidence states so that process health and content correctness could be judged
separately.

### Validation and outcome

The corrective workflow passed its policy, contract, and regression checks,
and a live read-only audit confirmed that the target state was not mutated by
the workflow release. Content promotion remained `PENDING_EVIDENCE` because
fixed-condition visual evidence and the designated review were incomplete.
The workflow was not claimed as live-executed when the available execution
surface could not invoke the proposed adapter.

### Transferable lessons

1. Prototype speed is a property of the whole decision loop, not the setter or
   builder alone. Bound discovery, mutation, verification, and recovery before
   optimizing code.
2. A default patch path must be structurally incapable of becoming a broad
   rebuild. Destructive maintenance operations need a separate confirmation and
   checkpoint.
3. One scoped inventory plus local validation and one postcondition audit is
   usually more reliable than a chain of per-item calls, provided the batch is
   bounded and reversible.
4. A diagnostic audit can report a healthy structure without granting visual or
   production approval. Workflow release and content promotion are separate
   decisions.
5. A timeout is a state-classification event. Audit before retrying, preserve
   the baseline, and record whether the lesson belongs to the project or is a
   durable handbook rule.

### Applicability and limits

These rules apply to editor automation, procedural blockouts, asset-placement
experiments, and other stateful prototype loops. They do not prescribe MCP,
Python, a fixed Actor count, or a universal time limit. Large intentional
rebuilds may still be appropriate when their design gate, checkpoint,
execution surface, and recovery evidence are explicit. Background shader or
cache maintenance may remain a separate environment bottleneck and should be
measured rather than misattributed to the mutation itself.

## Investigation note: gate narrowing for a bounded edit on an accepted prototype

**Status:** evidence-backed process note based on an operator-reported local
prototype edit; the level outcome has no independent visual or runtime
promotion evidence. The note proposes a reusable operation contract and does
not claim that the affected level passed production promotion.

### Problem and intent

An already accepted environment prototype required a small local change: remove
four existing prototype Actors near a stair landing, move one existing mass to
the landing, and save. The request explicitly preserved the Landscape,
waterway, bridge connections, zone markers, and the rest of the accepted
layout. The intended outcome was an immediately usable next prototype state,
not a new layout review or a production-quality decision.

### Context and initial state

The current stage and prototype baseline were already accepted for the user's
ongoing iteration. The requested changes were limited to existing named
content, but the execution path inherited broad level-design responsibilities:
re-reading long guidance, interpreting an Area Composition Plan gate,
discovering and describing execution capabilities repeatedly, collecting a
large viewport and label inventory, and performing broad Landscape/grounding
preservation checks. The reported edit itself took roughly ten minutes to
complete; the precise contribution of each orchestration step was not
independently measured.

The semantic role of the two roads was an important unresolved boundary. If
they were visual prototype masses, they could belong to a local edit. If they
were the authoritative route graph, traversal surface, or bridge connection,
their deletion would change a plan-owned responsibility and require gate
reopening.

### Alternatives and trade-offs

- **Replay the full level workflow:** preserved the strongest broad evidence,
  but spent a disproportionate amount of time on risks the request explicitly
  excluded and delayed the next experiment.
- **Skip all gates and mutate by visual selection:** minimized latency, but
  could delete a route, marker, bridge, or terrain-dependent building without
  proving ownership or recovery.
- **Classify a `BOUNDED_PROTO_EDIT`:** reuse the accepted stage while its
  assumptions remain unchanged; inspect explicit targets and protected
  references once, apply one bounded transaction, verify local postconditions,
  save, and keep promotion unchanged. This was selected because it preserves
  scope-specific safety while removing unrelated evidence work.

### Decision and implementation scope

The durable correction is an explicit operation mode inside the staged
workflow, not a new stage. Entry requires a known baseline, an exact target
allowlist, a declared local envelope, a time and change budget, a save and
rollback policy, and a compact protected snapshot. Explicit deletion is
allowed only for named existing targets; wildcard cleanup, spawning,
regeneration, shared-source changes, and broad layout mutation remain outside
the mode.

The hot path is:

`classify → compact inspect → preconditions → serialized mutation → in-memory postcondition → save → persistence re-read`

Landscape, water/stream, bridge, zone-marker, fixed-camera, streaming,
authoritative-route, and Navigation/collision-source mutation exits the mode.
A building moved over Landscape may use a target-specific four-corner support
check, but a center trace or partial grounding result cannot substitute for
the existing grounding contract.

### Validation and outcome

The minimum evidence package contains the exact target identity and expected
pre-state, the unchanged protected snapshot, exact deleted/changed IDs,
before/after Transform, warnings, save persistence, and the list of checks not
run. For the reported edit this corresponds to four explicit deletions, one
mass Transform, a saved level, and a key Transform re-read.

The full visual review, fixed-camera capture, PIE, independent visual review,
and broad plan/translation reconsideration remain outside the operation unless
the user requests promotion or the semantic impact triggers reclassification.
The correct result is therefore `operation_verdict: PASS` only for the local
postconditions, with `promotion_verdict: unchanged`; it is not a level-wide
visual or runtime approval.

### Recovery and follow-up

If target identity, route role, protected scope, dirty save state, grounding
support, or schema capability is ambiguous, exit before mutation. If the
operation times out or returns an empty or partial result, audit the current
state before retrying and classify it as complete, partial, duplicated,
unchanged, recoverable, or unknown. Preserve the accepted baseline and failed
candidate. Measure classification, discovery, wait, mutation, verification,
save, background, call-count, redundancy, capture, and rollback time
separately.

### Transferable lessons

1. A short request needs an operation classifier before it needs a broader
   evidence package; otherwise valid production gates become accidental
   latency.
2. Gate reuse is conditional on unchanged assumptions. It does not turn an
   unknown baseline into `PASS` and does not grant promotion.
3. Explicit existing-Actor deletion can be bounded, but only with stable
   identity, ownership, protected-scope checks, and an exact changed-ID
   postcondition. A count or visual selection is not enough.
4. Direct protection and local contact validation have different scopes:
   preserving Landscape does not require a whole-map grounding inventory, but
   moving a building still requires its applicable four-corner support proof.
5. Compact structural evidence and deferred capture make a small edit faster;
   they do not replace visual, runtime, or independent evidence when those
   decisions are in scope.

### Applicability and limits

This rule applies to explicit local edits of existing prototype content when
the spatial responsibilities and protected references are inspectable. It
does not apply to a route-authority change, terrain or water/bridge mutation,
zone-marker lifecycle change, cross-zone composition change, generated-system
regeneration, shared-asset replacement, or a request to promote a level.
Project-specific budgets and item caps may differ; the semantic boundary and
fail-closed behavior must remain.

### Evidence gaps and follow-up research

The source report did not include a per-call timing trace, a machine-readable
protected snapshot, a target grounding receipt, or independent visual/runtime
evidence. Implement the contract against a synthetic fixture and verify that
the same target edit completes within the project budget, that protected
mutations exit before saving, that timeout recovery creates no duplicate, and
that omitted visual/PIE checks cannot be interpreted as promotion evidence.

## Investigation note: route-first blockout and spline pilot

**Status:** candidate case; the level was paused before the spline-backed route received its final independent visual gate. The note is useful for decision learning, but it is not a claim that the final route or level was approved.

### Problem and intent

The goal was to build a dense hillside settlement in which architecture framed purposeful pedestrian circulation rather than blocking it. The first production impulse was to retain existing buildings and add readable route prototypes around them. The intended outcome was a route system that could guide layout, later dressing, procedural exclusions, and traversal validation without repeatedly rediscovering the same conflicts.

### Context and initial state

The level already contained terrain, buildings, walls, props, prototype guides, and authored natural content. A broad route prototype was introduced after much of the architectural layout existed. It used many independent visual route segments and sampled terrain height, but its topology, surface authority, and continuous-clearance contract were not sufficiently explicit. The prototype was later found to cross cliffs, buildings, and spaces that did not support human circulation.

### Alternatives and trade-offs

- Keep the route strips and move or hide whatever they intersected. This was fast but preserved a weak spatial premise and made the route depend on ad hoc exceptions.
- Fit the route around the existing architecture. This protected sunk layout work but made circulation secondary and produced blocked or implausible connections.
- Reset the route as named connections with an inspectable centerline or graph, then revalidate architecture against it. This required reopening layout decisions but gave route topology, ownership, and validation a stable authority.

The third option was selected. A spline was tested as one possible centerline representation, not as a universal replacement for stairs, landings, or terrain-transition modules.

### Implementation and validation

The broad route was retired after review. A smaller market-scale route was then authored with named connections and a declared width and clearance envelope. Exact bounds and a conservative swept-corridor audit found blockers in the initial candidate. Relevant architecture, boundary elements, and props were moved to recoverable states or repositioned, and the same audit later reported no active blockers under that envelope.

A spline pilot was subsequently created for two open route branches and tagged for route ownership and procedural exclusion. The pilot proved that a continuous source could carry ordered points, branch identity, and downstream metadata. It did not by itself create a production walkway: the clean fixed-camera capture did not show the debug line as a readable route surface, while temporary guide geometry dominated the review image. No independent visual gate was run after that pilot because the work was intentionally paused.

### Outcome, recovery, and evidence gaps

The work established a better route data direction and exposed the need to move architecture when it violates the circulation contract. It did not complete the level or prove that a spline-backed route was visually or runtime ready. Recovery maps and hidden or recoverable states preserved earlier layout options, while destructive natural-content cleanup and later route repairs remained separate decisions.

Remaining evidence gaps include runtime capsule traversal, the actual production visual carrier for the route, steep terrain transitions, stairs and landings, and independent review of the same fixed cameras after the spline pilot. These gaps prevent promotion from candidate experiment to approved production system.

### Transferable lessons

1. A route is a spatial contract with named topology, width, grade, clearance, surface ownership, and consumers—not a set of decorative strips.
2. Endpoint height matching and non-overlapping bounds are useful filters, but continuous corridor, headroom, intermediate surface, and runtime traversal checks are required for approval.
3. Route intent data, review visualization, and the playable surface must be named separately. A spline debug line, semantic material, or exclusion mask proves only the responsibility it actually implements.
4. When a failure repeats, record the symptom, cause or confidence-labelled hypothesis, false assumption, changed invariant, new detection rule, same-condition recheck, and recurrence status. If no new rule or hypothesis changes, the next iteration is not learning.
5. After the same failure signature survives two iterations, reset or replace the responsible system instead of adding cosmetic exceptions.

### Applicability and limits

These lessons apply to dense environment layout, route-coupled PCG, editor automation, and any workflow in which independently authored spatial systems can invalidate one another. They do not require splines, Landscape, PCG, or a particular Unreal tool. They should not be used to force every path into one continuous curve or to reject intentional non-walkable visual lines, cinematic paths, or authored traversal modules that declare different contracts.

### Follow-up research

Validate a reusable route contract across at least one additional environment and compare spline, typed segment graph, and authored module representations for stairs, switchbacks, branching, mask generation, runtime traversal, and fixed-camera review. Keep this case pending until those results and the missing visual and runtime evidence are available.

## Investigation note: layered AI-assisted world building demonstration

**Status:** `PENDING_EVIDENCE` candidate case based on a public capability
demonstration. It is not a completed production case, a comparative benchmark,
or evidence that AI-generated world building reduced total project cost.

### Problem and intent

The demonstration explored whether an AI assistant could shorten Unreal world
building iteration while a technical artist retained intent, correction, and
approval authority. The interesting design question is not whether the agent
could invoke an Editor operation. It is whether operational interfaces,
reusable procedural units, project examples, and durable guidance could be
combined without hiding authorship, state, failure, or maintenance cost.

### Observed scope and evidence

The video showed several capability slices: furnishing a small interior from
described intent and retrieved assets; assembling a larger city-and-park result
through a retained procedural graph; producing bounded one-off procedural
results; applying reusable biome and lighting guidance; and using captured
images to identify and correct visible output. It also discussed extending the
agent-facing surface through grouped capabilities and reusable guidance.

These observations support only that the demonstrated workflow produced and
iterated visible Editor results under the shown conditions. They do not expose
a stable baseline, complete operation trace, reproducible test package, or
production acceptance record. The demonstrated implementation terminology is
version-sensitive; the durable candidate model is the separation of Toolset or
capability surface, primitive, approved example, and Skill responsibilities.

### Candidate decisions and trade-offs

Two decisions deserve controlled follow-up rather than immediate adoption:

1. Acquire context from explicit targets and approved project examples before
   semantic search, bounded discovery, or temporary inspection scripts. This
   may reduce reconstruction error and orchestration cost, but it could also
   reproduce stale example assumptions unless authority and version scope are
   checked.
2. Choose persistent parametric, instant one-off, or direct-authored output
   from the expected regeneration and ownership need. A retained graph may
   improve tuning and repeatability but add maintenance; a one-off result may
   reduce setup but still creates provenance, cleanup, and rollback debt once
   saved.

The video's image-guided correction loop is best treated as builder
self-inspection. It may reduce obvious visible defects before review, but it
does not provide independent visual approval or structural, runtime,
persistence, performance, and regeneration evidence.

### Observed failure signals

The interior sequence exposed placement errors that required human correction,
including orientation, overlap, and spatial-fit problems. Those symptoms are
consistent with unresolved pivot, local-axis, final-bounds, grounding, and
clearance assumptions, but the available evidence does not establish one root
cause or a failure rate. The corrections demonstrate the value of a short
human-in-the-loop feedback cycle; they do not retroactively validate the
original generated candidates.

### Evidence gaps

Promotion to a completed case requires, at minimum:

- a versioned baseline, exact task contracts, selected context, operation
  schemas, model/client/integration configuration, and complete tool traces;
- repeated-run success, failure, retry, cancellation, and recovery rates,
  including ambiguous or partial-state audits;
- comparable manual and assisted authoring time, review time, dispatch count,
  token or context cost, compute cost, and maintenance effort;
- exact changed assets and outputs, save/reopen persistence, source-control
  behavior, ownership, cleanup, rollback, and security boundary evidence;
- persistent-graph regeneration after source and parameter changes, plus
  one-off output deletion, orphan detection, and manual-override behavior;
- final transformed-bounds, grounding, collision, navigation, camera,
  streaming, memory, frame-time, and packaged/runtime validation;
- independent visual and gameplay review under stable comparable conditions;
- team outcomes such as handoff clarity, review burden, defect escape,
  reproducibility, and long-term update cost.

### Candidate lessons, applicability, and follow-up

The evidence justifies hypotheses, not universal lessons: layered responsibility
may make agent behavior easier to extend and inspect; approved examples may be
better operational ground truth than reconstruction from memory; explicit
artifact lifetime may prevent one-off output from becoming ownerless debt; and
builder self-checks may shorten the correction loop when kept separate from
acceptance.

Test these hypotheses on one bounded interior task and one persistent
procedural task using the same baseline, acceptance rubric, and runtime build.
Compare a manual workflow, an example-grounded assisted workflow, and an
assisted workflow without a compatible example. Preserve failed candidates and
measure total decision-loop cost rather than only generation time. Keep this
case `PENDING_EVIDENCE` until repeatability, persistence, performance,
independent review, and maintenance evidence close the gaps above.

### Sources

- [AI-assisted Unreal world-building demonstration](https://www.youtube.com/watch?v=lDf_y-YPELo) - observed capability and workflow source.
- [Epic Games: Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor) - dated implementation context for capability discovery, grouped tool interfaces, execution boundaries, and structured results.
- [Epic Games: Working with PCG and LLMs Using Unreal MCP](https://dev.epicgames.com/documentation/unreal-engine/working-with-pcg-and-llms-using-unreal-mcp-in-unreal-engine?lang=en-US) - dated guidance for reference-grounded PCG assistance and incremental supervision.

## Case: recovering a meadow through source capability and coupled ground cover

**Status:** completed within an Editor-level environment scope in UE 5.8. Independent visual review, saved-state checks, and one local PIE route were recorded. Cook, packaged runtime, target-platform performance, wind, and clean-project reuse were not established. The source project retains the raw images and engine records; they are not bundled with this Handbook. See the paired [Korean review](meadow-reuse-review.ko.md).

### Intent, initial state, and alternatives

A meadow with a freestanding rock landmark, shallow creek, open paths, and layered vegetation needed coherent close-range surfaces and readable depth. Early grass read as repeated catalog clumps or flat strands, exposed ground read as a green sheet, and a cliff-oriented rock source revealed open reverse surfaces when tilted into a freestanding role.

Increasing density, repeatedly adjusting color, or concealing the defects with lighting would preserve the source-role mismatch. Reopening the entire concept would discard already accepted terrain, routes, and water relationships. The selected approach isolated the failing source or visual system while freezing accepted systems and comparison cameras.

### Decisions and implementation scope

- Replace the incompatible landmark source with a closed source that supports the required reverse views, then revalidate its assembly and footprint.
- Test three task-authored curved grass sources at the intended scale range and multiple directions, then test surface response on a small set of existing positions before converting the representative slices.
- Connect substrate blending and vegetation placement to a common colony-field definition, preserving route, water, and hardscape exclusions. Correct a tint operation that also affected exposed dirt. Numerical parity between the offline and shader implementations was not independently established.
- Separate shape and material findings. After geometry passed, change only material response on the same small trial and repeat relevant scene views.
- After broad expansion revealed evenly spaced tree rows, change only the broad tree distribution into asymmetric groups and accents. Preserve the accepted ground cover and other visual systems.

### Evidence and outcome

| Retained record | Observation | Supported conclusion |
| --- | --- | --- |
| Source review v9 → v10 | Shape remained suitable; material was initially 2/5. A material-only comparison at the same 36 positions later met the applicable 4/5 floor. | Shape and surface approval need separate scopes; accepted shape evidence can be reused for a surface-only repair. |
| Combined representative slices v12 | The slices passed all applicable visual categories at 4/5 or above. The total of 2,762 ecology instances was retained across repair, although source geometry, placement distribution, and some root positions changed. | Instance-count growth was not required for this result; equal counts do not establish equal geometry cost or isolate a single cause. |
| Broad review v13 → v14 | Tree distribution scored 2/5 and distance depth 3/5. After a bounded repair of 57 trees, both met 4/5. Other approved visual systems were frozen. | A local slice does not retire whole-level repetition risk; the failure needed composition repair. |
| Final review v15 | Visual regression and saved reload passed; a 17-waypoint local walk recorded 336 samples with no falling samples. | The declared Editor-level result passed; this does not establish package, platform, or performance readiness. |

The source records are summarized as observations, not a controlled benchmark. In particular, the combined ground-cover repair changed several inputs over successive passes; its individual causal contributions and total time savings were not measured.

### Transferable decisions and limits

Use source capability checks to stop an unproductive placement loop; couple substrate and placement through explicit spatial data when the concept needs continuity; narrow revalidation to the affected dependency scope while retaining scene regression; and inspect repetition again after expansion. Archive approved sources with their dependency class and evidence so future work can start from inspectable candidates.

Do not standardize the scene's blend ratios, transmission values, light settings, mesh representation, or capture workaround. The generated blades have no validated wind behavior or target-platform cost. A reusable collection needs a separate dependency and copy audit, and every new scene still needs its own visual comparison. These lessons refine Chapters 05, 09, and 10; they do not add a universal production gate or authorize asset redistribution.

## Investigation note: local verification without a convincing whole world

**Status:** observed failure with an untested recovery direction. The operator retained the user-provided whole-world panorama, local capture packets, save records, and failed visual reviews. Those project records are not bundled or redistributed with this Handbook. This note reports the qualitative failure; it is not a controlled comparison or a completed recovery case. See the paired [Korean case review](sparse-world-judgment-review.ko.md).

### Intent and observed result

The request was to use a large existing map for an environment explored and appreciated on foot. Actual assets were placed in several small areas, with substantial effort spent on local grounding, supports, material edges, and fixed-view review. The whole-world panorama still showed a small central settlement, tiny remote groups, broad empty travel space, and little intermediate structure. The requester rejected the result and questioned whether the blockout had been meaningfully completed.

Local save and contact evidence existed. Several visual candidates also remained explicitly failed. Neither the successful local checks nor the existence of blockout proxies established that the global layout, perceived travel distance, settlement hierarchy, or connected walking experience had passed. The observed failure belongs to the delivered scope even when no whole-world success was formally claimed.

The retained records also include a prior blockout-stage `PASS` and limited actual-player route checks. That approval authorized only bounded visual slices and explicitly withheld broad dressing and whole-level approval. It would therefore be inaccurate to record that no blockout or review ever occurred. The failure concerns the adequacy and scope of the observation, the interpretation of that approval, and the later decision to keep repairing local systems while the intended global result remained weak. The record does not establish that all earlier evidence was invalid or that the reviewer acted dishonestly.

### Explanations and alternatives

The evidence is consistent with a mismatch between world scale and authored experience, insufficient macro-layout validation, and prolonged local repair at the wrong decision scale. It does not isolate their individual contribution or prove that the Handbook alone caused the behavior. The relevant principles were already present; applying and testing them was also a failure.

Three possible responses have different purposes:

- More small props can improve local detail once the larger place works, but do not by themselves establish destination hierarchy or shorten unintentional empty travel.
- Better materials and support geometry can fix visible local defects, but cannot determine whether several distant places form a coherent journey.
- Reopening macro composition and the playable blockout can compare substantial destination groups, terrain framing, intermediate experiences, and intentional quiet at the requested scale. This was the proposed recovery direction; its success had not been established.

### Why the proposed recovery is worth testing

The next experiment should act on the relationships that the rejected overview and walking intent put in doubt. Preserve useful work and compare reversible macro alternatives under ordinary whole-world and player views. Ask whether the destination promises, approach choices, meaningful changes, and arrival payoffs become legible before committing more art. The original full-map request does not imply filling every surface, reducing the world without agreement, or imposing one fixed encounter interval.

A quiet desert, a vehicle route, and a compact walking settlement can need very different distributions. A successful repair would need evidence from this intended experience; the proposed choice is not a universal instruction to make all worlds denser.

### Transferable lesson and unresolved proof

Use local evidence for local claims and whole-system evidence for whole-system decisions. When local repairs repeatedly leave the main failure unchanged, reopen diagnosis at the scale of that failure rather than make another procedural requirement. A Handbook contribution should help the next reader identify that priority and explain its mechanism and limits.

The case does not establish a recovered level, optimal density, a preferred terrain representation, quantified improvement, or causal superiority of a new editorial approach. Test the proposed teaching through unfamiliar [judgment exercises](../../validate-unreal-production/references/judgment-evaluation.md) and the eventual level through its own blockout and production evidence.

## Case: An inspectable PCG learning fixture is not a production starter

**Evidence class and scope:** observed Editor learning diagnostic, with retained
technical snapshots and a scoped independent visual recovery. The operator
retained the source evidence on 2026-10-25; those project records and images are
not bundled or redistributed here. This is not a controlled speed benchmark,
runtime test, or production-environment approval. The paired
[Korean review](pcg-learning-reuse.ko.md) covers the case and chapter additions.

### Intent, context, and alternatives

The requester prioritized understanding Electric Dreams-inspired PCG
relationships over a finished jungle. An accepted four-cell distribution and
exclusion comparison was preserved while a new non-partitioned fixture added
hierarchy, aim, and multi-point support comparisons. The target Editor build
was UE 5.8.3; primitive meshes and explicit query-source surfaces kept the
mechanisms inspectable.

Rebuilding the whole sample would have introduced unrelated content and
dependencies. Immediately dressing a forest would have made rule errors hard
to separate from art direction. The selected approach reconstructed only the
needed relationships, isolated an owned support-filter copy, validated data
before spawning, and required fixed-view teaching clarity afterward. This
traded production realism for cheaper discriminating observations; the fixture
could not retire a real environment's scene or runtime risks.

### Observations and recovery

| Observation | Decision supported | Limit |
| --- | --- | --- |
| Parent variation changed descendant transforms; removing a required parent reduced visible members from 9 to 6. | Preserve explicit relative-transform and dependency semantics rather than scatter related parts independently. | The tested primitive assembly was not a production asset family. |
| Eight control glyphs and eight target-driven glyphs used a declared local axis; target variation changed both the aim and marker. | Declare mesh-axis and coordinate conventions before choosing an orientation operation. | Another mesh may require another axis; this does not choose a universal look-at operation. |
| Center samples admitted three support cases while four-corner sampling admitted only flat and ramp cases. The step had a 60 cm residual against a 5 cm fixture threshold. Permissive height tolerance or shorter sample spacing admitted it again. | Match samples and tolerance to the support footprint; retain a known failure to expose under-sampling. | These fixture dimensions and thresholds are not reusable defaults or complete proof for arbitrary shapes. |
| A query produced three records with invalid density/hit identity and unprojected height. Inspecting the target build's query semantics and matching the source filter restored valid hits. | Inspect actual hit state and consumer semantics, not count alone; change the failing query before changing known surfaces. | The engine-specific filter correction is not a rule for every trace or engine version. |
| Intended material overrides existed for thirteen spawners, but seven generated components lacked them. After a bounded output-configuration refresh, the colors appeared while instance matrices stayed unchanged. | Compare intended configuration with actual generated resources before repairing lighting or geometry. | Cache reuse is a plausible explanation, not an isolated causal result; the incidental refresh action is not a universal invalidation recipe. |
| The first visual review scored hierarchy and aim 2/5, support 3/5, and annotation 1/5. The intentional center-only failure could look like a success. | A diagnostic must visibly explain its contrast, even when its mathematics is correct. | Debug colors and explanatory signs are appropriate to the learning role, not an art-direction prescription. |

The repair changed the owned diagnostic presentation while preserving points,
source fixtures, lights, and eight comparison cameras. Hierarchy groups,
control/aimed/target roles, center-only false positive, and corner-hit markers
became legible. The independent reviewer then scored every applicable visual
category at least 4/5 for the Editor learning scope. Distant overview text and
some edge text remained nonblocking limitations covered by local fixed views.

### Technical evidence and unresolved scope

Thirteen managed resources contained 232 instances: 227 main outputs including
one target marker, plus five separate diagnostic objects. Actual world matrices
matched validated data across two generations and a real saved reopen, both
before and after presentation repair. The reopened state was retained before
regeneration. Generated outputs had no collision, navigation influence, or
overlap events; only the declared source fixtures provided query collision.
Protected original content was unchanged in the retained checks.

The operator's evidence set includes `S1-data-validation.json`,
`S2-output-validation.json`, failed and accepted `independent-S2-review`
records, raw generation/reopen snapshots, and eight fixed-camera images with
capture and handoff-verification records. The repeated world-matrix digest was
`8a9a4947149777242f2c24fa71cd0fc961f4f1a66999bf60c5330adfe3fc6063`.
The Handbook reports the retained observations; it does not independently
re-run the Editor or distribute those project assets.

Whole-sample Blueprint implementation equivalence, PIE, runtime scheduling,
performance, packaging, integration with real environment assets, and total
authoring-time savings were not established. Reference branches had not been
extracted into a general production subgraph library.

### Transferable decisions and changed-context checks

Reuse the relation, expected variation, failure signal, and verification
boundary. Replace context-specific axes, footprints, sources, parameters, and
ownership. Keep historical builders distinct from safe next-task operations;
keep archive rechecks non-destructive and distinct from new approval. Existing
automation, procedural, and evidence principles already cover these choices;
the case does not introduce another mandatory gate or document.

Before generalizing, use two constructed questions: would a mesh with a
different forward axis still satisfy the aim contract, and would a valid center
with one unsupported corner satisfy this support responsibility? Change the
recommendation when the responsibility changes—for example, a narrow anchor
may not require the broad support test. These questions discriminate the rule
from memorized settings; no held-out judgment improvement or speed gain has
been measured.

### Connections

[Automation reuse](../../design-unreal-automation-and-pcg/references/08-automation-python.md#reuse-a-validation-contract-without-replaying-historical-mutations),
[procedural transfer](../../design-unreal-automation-and-pcg/references/09-procedural-systems-pcg.md#reuse-a-proved-relationship-not-a-fixture-configuration),
and [evidence claims](../../validate-unreal-production/references/12-validation-testing-debugging.md#archive-validity-and-diagnostic-readability-are-separate-claims).

## Evidence discipline

Separate facts from interpretation and confidence. Do not infer causality from chronology alone. Remove credentials, private paths, user data, proprietary asset names, and exact project coordinates unless essential and explicitly authorized.

## Related topics

Every chapter may contribute cases. Link each case to the decisions it tests rather than collecting detached tutorials.
