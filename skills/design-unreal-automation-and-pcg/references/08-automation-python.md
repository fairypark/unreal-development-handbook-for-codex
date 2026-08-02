# 08 — Automation & Python

## Purpose

Make repeated Unreal work reproducible, observable, reversible, and safe across projects and production stages. Treat Python as one implementation option rather than the durable center of automation design.

## When to automate

Automate when the responsibility is repeated, the inputs and outputs are defined, the manual result is understood, and objective postconditions can detect partial or incorrect execution. Keep high-judgment aesthetic or architectural approval outside deterministic builder automation.

## Design considerations

- Define typed or structured inputs, outputs, units, ranges, and empty-result semantics.
- Prefer idempotent operations or explicit overwrite refusal.
- Separate generic orchestration from project-specific paths, assets, and policy.
- Serialize game-thread or stateful Editor mutations.
- Detect cancellation, timeout, partial completion, compilation, and persistence states.
- Log enough factual evidence to diagnose failure without storing private prompts, credentials, or unrelated user data.
- Use the narrowest execution surface that exposes the required engine capability.

## Postconditions for spatial and Editor automation

Treat a successful tool call as transport evidence, not as proof that the intended Unreal state exists. Any mutation that creates or changes spatial content should have explicit postconditions for the object count or identity, transform or topology, semantic tags or ownership, visibility and collision state, save persistence, and downstream compatibility. For route or procedural work, also verify representative points, named connections, the derived exclusion or review output, and the absence or classification of blockers.

An empty result, a missing Actor, an unexpected point count, or a partial batch is a failed postcondition even when the command returned without an error. Stop and inspect the input schema, ownership, and partial state before retrying. Retrying a timed-out or ambiguous mutation without a state audit can create duplicates, overlapping candidates, or a false comparison baseline.

Record whether a postcondition is confirmed, contradicted, or not yet tested. That distinction prevents an unobserved state from being reported as a successful iteration and makes interruption and recovery part of the automation contract.

## Python as an option

Prefer Python when the required Unreal API is exposed, rapid iteration matters, and deployment can reliably load and reload the package. Prefer C++ or another supported surface when coverage, lifecycle, performance, distribution, or testing requirements are not met. Stop and report an API gap rather than emulating unsupported behavior unsafely.

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
- Executing arbitrary in-editor Python without treating it as privileged code.
- Hard-coding private paths or current Tool names into durable knowledge.

## Related topics

C++; Procedural Systems & PCG; Validation, Testing & Debugging; AI-Assisted Development.
