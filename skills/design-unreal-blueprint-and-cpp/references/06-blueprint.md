# 06 — Blueprint

## Purpose

Use visual scripting for fast, observable, designer-accessible composition without allowing graphs to become unowned collections of state and side effects.

## Decision contrast: Choose update behavior from the behavior being modeled

**Evidence class:** constructed teaching scenario; no measured production outcome is claimed.

**Situation.** An interaction changes only when state changes, while a nearby camera effect must respond continuously to motion.

**Choice and reason.** Use explicit state changes for the interaction and a suitable continuous update for the moving effect. Updating every object every frame obscures causality and can add unnecessary work; removing all continuous updates can break the intended motion.

**When the choice changes.** Event-driven is not a universal ban on Tick, and a working graph is not proof of maintainable ownership. The right design follows frequency, lifetime, observability, and measured cost.

**Smallest useful test.** Exercise the state transition and continuous motion independently, inspect who owns each update, and measure representative cost before restructuring the graph.

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

### Scripted graph edits in UE 5.9 Preview

Before applying a scripted Blueprint change to many assets, try the intended edit on one duplicate. Compile it, save, close the Editor and reopen the copy. Check the changed graph and confirm the source still has its original structure. Epic expanded Blueprint graph scripting in this Preview and reported a crash when Python replaces a Blueprint root component (UE-411502). A successful function-graph edit covers that operation only. Assess a root change separately if the design actually needs it. [Preview notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-9-release-notes?application_version=5.9) · [Preview 1 issues](https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840/3)

**Observed on Windows, 2026-11-14.** On UE 5.9.0 CL 60351404, a headless Editor running Python duplicated an Actor Blueprint, added one empty function graph to the copy, compiled and saved it. A fresh Editor process found the graph only in the copy and compiled it again. This verifies graph persistence through this Python entry point. In the later UE5_9 project run, the native MCP AddFunctionGraph, CompileBlueprint and SaveAsset tools edited a duplicate GameMode. A fresh process reopened both assets and found the function only in the duplicate. The project had editing toolsets enabled. Component-root replacement and function execution remain untested.

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
