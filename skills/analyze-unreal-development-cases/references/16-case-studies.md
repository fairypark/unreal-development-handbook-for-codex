# 16 — Case Studies

## Purpose

Convert real Unreal outcomes, failures, migrations, optimizations, and production incidents into evidence-backed applied reasoning without turning anecdotes into universal recipes.

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

## Evidence discipline

Separate facts from interpretation and confidence. Do not infer causality from chronology alone. Remove credentials, private paths, user data, proprietary asset names, and exact project coordinates unless essential and explicitly authorized.

## Related topics

Every chapter may contribute cases. Link each case to the decisions it tests rather than collecting detached tutorials.
