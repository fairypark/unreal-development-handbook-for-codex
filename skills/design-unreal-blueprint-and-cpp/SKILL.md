---
name: design-unreal-blueprint-and-cpp
description: Choose, design, or review maintainable Unreal Blueprint and C++ systems, including responsibility boundaries, ownership, lifecycle, APIs, communication, extensibility, and integration. Use before implementing gameplay or tools, splitting Blueprint and native responsibilities, or recovering coupled and fragile systems. Do not use for syntax lookup, compilation commands, or a single graph edit.
---

# Design Unreal Blueprint and C++

Choose implementation technology after defining responsibility, lifecycle, and interface contracts.

## Load the relevant Handbook chapter

- Read [06-blueprint.md](references/06-blueprint.md) when Blueprint owns or may own any responsibility.
- Read [07-cpp.md](references/07-cpp.md) when native code owns or may own any responsibility.
- Read both for hybrid boundaries or migrations between Blueprint and C++.

## Design the system first

1. State the behavior, invariants, owners, callers, and observable outcomes.
2. Define lifetime, initialization order, teardown, failure, and hot-reload or iteration constraints.
3. Minimize public surface area and make dependency direction explicit.
4. Prefer events, interfaces, components, and data contracts that communicate intent over hidden casts or global reach.
5. Separate policy, orchestration, data, and presentation when they change for different reasons.

## Choose Blueprint and C++ responsibilities

Prefer Blueprint where rapid authoring, designer ownership, composition, or data-driven variation is the primary value. Prefer C++ where stable shared contracts, unsupported engine access, performance-critical work, native testing, or broad reuse justifies the added build and ownership cost. Use hybrid designs when the native layer exposes a small stable contract and Blueprint owns controlled variation.

Do not move code to C++ merely because a Blueprint is large. Repair responsibility and dependency problems first. Do not keep behavior in Blueprint merely because implementation is faster when lifecycle, authority, testing, or performance requirements are not met.

## Validate the boundary

Check lifecycle, null and failure paths, compile status, API compatibility, serialization, replication where relevant, automated tests, and representative runtime behavior. Require a migration and rollback plan when moving responsibility between Blueprint and C++.

Use coding or Editor skills only after the selected boundary and validation contract are explicit.
