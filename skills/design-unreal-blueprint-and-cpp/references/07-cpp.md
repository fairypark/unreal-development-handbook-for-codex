# 07 — C++

## Purpose

Provide stable native contracts, engine integration, performance-critical implementation, and reusable systems while preserving clear ownership and safe Blueprint extension.

## Decision contrast: Move a measured responsibility, not an entire feature by habit

**Evidence class:** constructed teaching scenario; no measured production outcome is claimed.

**Situation.** A feature combines a few designer-authored decisions with a repeated numerical operation suspected of dominating its cost.

**Choice and reason.** Profile the representative workload. If the repeated operation is the limiting cost, move that responsibility behind a narrow C++ interface while preserving useful authored behavior and an observable lifecycle.

**When the choice changes.** If rendering, streaming, or a low-frequency event is the actual issue, rewriting the feature in C++ may add build and integration cost without improving the outcome. A prototype may value iteration speed more.

**Smallest useful test.** Compare behavior parity and the identified cost before and after the smallest change, under the same workload and target. Retain a recovery path and inspect boundary-crossing overhead.

## When to use

Prefer C++ when the system needs native-only APIs, a stable shared abstraction, precise lifecycle or memory control, strong automated testing, broad reuse, or measured performance that Blueprint cannot meet within the target budget.

## When not to use

Do not select C++ solely for prestige, theoretical performance, or to hide a confused graph. Avoid adding a native abstraction when the responsibility is still changing rapidly and the build, migration, and ownership cost outweighs its current value.

## API and ownership design

- Design a small typed surface around domain responsibility rather than mirroring Unreal internals.
- Make object ownership, garbage-collection visibility, thread or game-thread constraints, and lifetime explicit.
- Separate public contract, protected extension points, and private implementation.
- Expose Blueprint functionality deliberately with stable metadata and failure semantics.
- Return structured values normally and surface failures explicitly.
- Use asynchronous result patterns only for genuinely long-running work.

## Lifecycle and integration

Define construction, registration, initialization, world availability, activation, teardown, hot reload, Live Coding expectations, module startup, and shutdown as applicable. Do not assume Editor-time and runtime lifecycles are interchangeable.

## Validation checklist

- Build the relevant targets and configurations.
- Test success, invalid input, missing dependency, teardown, and compatibility paths.
- Verify reflected types, serialization, Blueprint exposure, and module dependencies.
- Measure performance before and after optimization.
- Confirm changes survive restart, reload, cook, and packaging where relevant.
- Review API duplication, naming, types, documentation, and error coverage.

## Common mistakes

- Exposing a large native API for agent or Blueprint convenience without stable semantics.
- Hiding structured data in JSON-formatted strings.
- Returning status booleans or error strings instead of normal values and explicit failures.
- Depending on incidental module load order.
- Treating Live Coding success as proof of clean-build or packaged correctness.

## Related topics

Project & System Architecture; Blueprint; Automation & Python; Production Pipeline.
