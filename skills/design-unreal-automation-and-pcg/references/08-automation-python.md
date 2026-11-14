# 08 — Automation & Python

## Purpose

Make repeated Unreal work reproducible, observable, reversible, and safe across projects and production stages. Treat Python as one implementation option rather than the durable center of automation design.

## Decision contrast: Automate a known experiment rather than multiply uncertainty

**Evidence class:** constructed teaching scenario; no measured production outcome is claimed.

**Situation.** A designer needs either one uncertain placement decision or a repeatable change to many already classified objects.

**Choice and reason.** Keep the uncertain trial small enough to inspect directly. Once the rule and recovery boundary are understood, a bounded batch can amortize dispatch cost and make the repeated work consistent.

**When the choice changes.** Automation can multiply a wrong rule faster. A huge batch without per-target postconditions is not justified by fewer calls; manually repeating a proved deterministic operation can also waste the iteration budget.

**Smallest useful test.** Test one representative and one edge case, then verify the bounded batch and protected state. Include discovery, waiting, verification, and recovery in the cost comparison.

## When to automate

The retained [dispatch-amplification investigation](../../analyze-unreal-development-cases/references/16-case-studies.md#investigation-note-unbounded-prototype-loops-and-dispatch-amplification) explains why batching and bounded responsibilities were selected. Its evidence concerns workflow behavior and does not promote the unfinished level or prove a universal batching threshold.

Automate when the responsibility is repeated, the inputs and outputs are defined, the manual result is understood, and objective postconditions can detect partial or incorrect execution. Keep high-judgment aesthetic or architectural approval outside deterministic builder automation.

## Design considerations

- Define typed or structured inputs, outputs, units, ranges, and empty-result semantics.
- Prefer idempotent operations or explicit overwrite refusal.
- Separate generic orchestration from project-specific paths, assets, and policy.
- Serialize game-thread or stateful Editor mutations.
- Detect cancellation, timeout, partial completion, compilation, and persistence states.
- Log enough factual evidence to diagnose failure without storing private prompts, credentials, or unrelated user data.
- Use the narrowest execution surface that exposes the required engine capability.

## Round-trip economics and batch boundaries

For Editor automation, latency is often dominated by orchestration and state
coordination rather than by the individual property assignment. A design that
performs one remote call per Actor, repeatedly discovers the same tools, or
revalidates the whole world after every small change can turn a cheap prototype
edit into an unbounded wait. Prefer a task-scoped execution context with one
tool discovery phase, one scoped inventory read, local validation, one
serialized mutation batch, an in-memory postcondition read, one save under the
declared policy, and one persistence read. Keep the batch small enough to roll
back and compare, but large enough to avoid per-item dispatch overhead.

Expose the operation boundary in the contract. A normal prototype mutation
should be transform- or data-bounded and should not inherit spawn, wildcard or
broad delete, terrain rewrite, asset replacement, or full-rebuild behavior. An
explicit delete of a named existing prototype Actor may be part of
`BOUNDED_PROTO_EDIT` only when ownership, parent/child scope, protected systems,
and downstream route or generated-output responsibilities are known. Read-only
diagnostics should return one structured snapshot. Promotion should consume
evidence and approval state rather than silently invoking more mutation or
capture work. Broad rebuilds belong to a separately confirmed maintenance
operation.

### `BOUNDED_PROTO_EDIT` transaction boundary

For an existing accepted prototype baseline, the smallest useful batch is:

`classify → compact inspect → local preconditions → mutate → in-memory verify → save → persistence verify`

The operation contract should allow only explicit target IDs, allowed
operation kinds, a local zone or envelope, a bounded item count, one target
level, a wall-clock budget, a rollback target, and a declared save policy. The
pre-mutation snapshot should include stable references or digests for Landscape,
water/stream, bridges, zone markers/registry, authoritative route or
Navigation/collision sources, and any camera or streaming boundary that the
edit could affect. A target building may use a compact four-corner grounding
check, but a center trace or average grounded ratio never replaces the
four-corner postcondition and a missing verifier is an exit condition.

Verify the in-memory target and protected state before saving unless the
execution surface provides an atomic transaction with equivalent rollback
semantics. The default response should be structural and compact: changed and
deleted IDs, before/after Transform, protected-snapshot comparison, save state,
warnings, elapsed/call counts, rollback status, and checks not run. Viewport or
fixed-camera capture is a separate evidence responsibility and must not be
implicitly attached to a Transform-only edit.

Keep `operation_verdict` separate from `promotion_verdict`. A bounded edit can
pass its local postconditions while visual review, PIE, full Landscape
inventory, or broad plan/translation review remain `NOT_RUN_BY_CONTRACT` and
the promotion verdict remains unchanged. This is a scope-risk reduction, not
a removal of safety or a production approval shortcut.

When a typed execution surface exposes a capability or schema descriptor,
cache it for the task or session. Omitted optional fields should use documented
defaults; missing required fields should fail clearly; unknown fields should
produce an actionable error rather than being silently discarded. Schema
negotiation reduces dispatch overhead but never waives protected-scope or
postcondition checks.

Discover capabilities progressively. Begin with the smallest stable catalog
needed to identify the responsible domain, then load only the selected
operation schemas and reference material. Eagerly loading every tool and schema
increases context cost and stale assumptions without improving authority.
Invalidate cached descriptions when the engine, plugin, project capability, or
session boundary changes, and treat a discovery result as availability evidence
rather than proof that the operation is safe or appropriate. A particular tool
registry or search command is one implementation of this rule, not the rule
itself.

Measure `setup_seconds`, `classification_seconds`, `discovery_seconds`,
`inspect_seconds`, `wait_seconds`, `mutation_seconds`, `verification_seconds`,
`save_seconds`, `persistence_seconds`, `background_seconds`, `tool_calls`,
`redundant_calls`, `capture_calls`, affected-item count, protected-touch
verdict, exit reason, and rollback status. Set a wall-clock budget for the
complete operation. If the budget or call-count bound is exceeded, stop, audit
state read-only, and classify the result before retrying. A retry without a
state audit is a second mutation hypothesis, not a recovery strategy.

## Postconditions for spatial and Editor automation

Treat a successful tool call as transport evidence, not as proof that the intended Unreal state exists. Any mutation that creates or changes spatial content should have explicit postconditions for the object count or identity, transform or topology, semantic tags or ownership, visibility and collision state, save persistence, and downstream compatibility. For `BOUNDED_PROTO_EDIT`, the changed-ID set must equal the declared target set, the protected snapshot must remain stable, and omitted high-cost checks must be recorded as not run. For route or procedural work, also verify representative points, named connections, the derived exclusion or review output, and the absence or classification of blockers.

An empty result, a missing Actor, an unexpected point count, or a partial batch is a failed postcondition even when the command returned without an error. Stop and inspect the input schema, ownership, and partial state before retrying. Retrying a timed-out or ambiguous mutation without a state audit can create duplicates, overlapping candidates, or a false comparison baseline.

Record whether a postcondition is confirmed, contradicted, or not yet tested. That distinction prevents an unobserved state from being reported as a successful iteration and makes interruption and recovery part of the automation contract.

### Reuse a validation contract without replaying historical mutations

A retained experiment can save discovery and setup work, but its builder may
assume an empty map, exact object identities, or unused output paths. Reuse the
intent, preconditions, postconditions, and evidence mapping first. Adapt only
the required operation to the new owned scope; a readable historical script is
not evidence that replay is safe.

Keep archive inspection non-destructive. A recheck should print its result or
create a distinct report rather than replace accepted evidence or reset a
stored promotion verdict. Preserve the state observed immediately after reopen
before regenerating, so recovery cannot be confused with persistence. An
archive check proves only the retained inputs and outputs it actually reads;
it does not observe the current Editor. The
[PCG learning-fixture case](../../analyze-unreal-development-cases/references/16-case-studies.md#case-an-inspectable-pcg-learning-fixture-is-not-a-production-starter)
illustrates this boundary. Measure the complete next decision loop before
claiming that the reusable reference reduced total authoring time.

## Python as an option

Prefer Python when the required Unreal API is exposed, rapid iteration matters, and deployment can reliably load and reload the package. Prefer C++ or another supported surface when coverage, lifecycle, performance, distribution, or testing requirements are not met. Stop and report an API gap rather than emulating unsupported behavior unsafely.

In UE 5.9 Preview, an MCP connection can succeed while a new project exposes no level-editing tools (Epic issue UE-412135). Inspect the tools offered by the intended Editor instance and the requested scope of work before planning a batch. If the operation is available and authorized, try the [single-copy Blueprint check](../../design-unreal-blueprint-and-cpp/references/06-blueprint.md#scripted-graph-edits-in-ue-59-preview). A direct Python test exercises a different entry point from an agent calling an MCP tool. [Epic's Preview 1 issue report](https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840/3)

## Recommended workflow

1. Prove the responsibility manually or with a small benchmark.
2. Define preconditions, postconditions, failure states, and recovery.
3. Implement the smallest repeatable unit.
4. Test one item, a representative batch, empty input, invalid input, and interruption.
5. Re-read representative results after mutation.
6. Verify save persistence and downstream compatibility.
7. Measure authoring and setup time separately from repeat execution time.

For a spatial batch, keep the iteration's observable invariant separate from the implementation command. For example, “the approved corridor remains clear under the recorded clearance envelope” is a useful postcondition; “the script completed” is not.

## Common mistakes

- Automating an unstable design.
- Retrying after timeout without checking partial results and creating duplicates.
- Treating a script exit code as proof of asset or level correctness.
- Treating a non-empty tool response or a successful graph invocation as proof that the intended scene state was created.
- Re-running an ambiguous spatial mutation before classifying active, hidden, recoverable, retired, and unapproved state.
- Treating a bounded edit's explicit delete as permission for wildcard cleanup or a broad reset.
- Adding image capture, full-world inventory, or promotion review to a local Transform edit without a scope change.
- Treating a compact response or omitted optional schema field as permission to omit a required postcondition.
- Loading an entire capability inventory for every request, or reusing a cached schema after its version or capability scope changed.
- Executing arbitrary in-editor Python without treating it as privileged code.
- Hard-coding private paths or current Tool names into durable knowledge.

## Related topics

C++; Procedural Systems & PCG; Validation, Testing & Debugging; AI-Assisted Development.
