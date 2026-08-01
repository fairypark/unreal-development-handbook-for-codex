# 06 — Blueprint

## Purpose

Use visual scripting for fast, observable, designer-accessible composition without allowing graphs to become unowned collections of state and side effects.

## When to use

Prefer Blueprint when the primary value is rapid iteration, designer ownership, asset composition, data-driven variation, event wiring, or project-specific behavior built on stable engine or native contracts.

## When not to use

Do not choose Blueprint by default when the work requires unsupported engine access, a large stable shared API, native-only integration, performance characteristics that profiling shows cannot meet budget, or test and lifecycle guarantees that the proposed graph structure cannot provide.

## Design considerations

- Assign each Blueprint a clear responsibility and owner.
- Separate durable state, orchestration, presentation, and reusable components.
- Prefer explicit interfaces, dispatchers, and typed data over repeated casts, global searches, and string conventions.
- Treat construction, initialization, BeginPlay, activation, teardown, and editor-time execution as distinct lifecycle phases.
- Keep public variables and events intentional; avoid exposing implementation detail merely for convenience.
- Move shared or stable contracts to a lower dependency layer before duplicating them across many Blueprints.

## Recommended workflow

1. Define behavior, state, callers, and invariants.
2. Choose the narrowest Blueprint class or component responsibility.
3. Design communication and lifecycle before drawing the graph.
4. Implement one representative path and its failure cases.
5. Compile and inspect warnings after each coherent change.
6. Validate runtime behavior, serialization, replication, and teardown as applicable.
7. Profile before moving work to C++ for performance.

## Validation checklist

- No unresolved compile errors or unexplained warnings.
- No hidden dependency on editor selection, load order, or incidental object discovery.
- Invalid references and missing data fail visibly and safely.
- State persists or resets according to its intended lifecycle.
- Interfaces remain stable for known consumers.
- Representative PIE or runtime scenarios match the original intent.

## Common mistakes

- Moving a large graph to C++ without first repairing its responsibility model.
- Using Tick because event or state ownership is unclear.
- Keeping authoritative state in presentation widgets or short-lived actors.
- Creating circular Blueprint dependencies through casts and asset references.
- Treating a successful compile as complete gameplay validation.

## Related topics

Gameplay Architecture; C++; Performance & Scalability; Validation, Testing & Debugging.
