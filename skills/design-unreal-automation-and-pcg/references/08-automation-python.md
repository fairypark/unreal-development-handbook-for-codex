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

## Common mistakes

- Automating an unstable design.
- Retrying after timeout without checking partial results and creating duplicates.
- Treating a script exit code as proof of asset or level correctness.
- Executing arbitrary in-editor Python without treating it as privileged code.
- Hard-coding private paths or current Tool names into durable knowledge.

## Related topics

C++; Procedural Systems & PCG; Validation, Testing & Debugging; AI-Assisted Development.
