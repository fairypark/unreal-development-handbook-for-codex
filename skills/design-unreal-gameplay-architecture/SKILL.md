---
name: design-unreal-gameplay-architecture
description: Design or review Unreal gameplay architecture, including Gameplay Framework responsibilities, gameplay systems, state, data, input, persistence, replication boundaries, lifecycle, and system interaction. Use before implementing gameplay features or when diagnosing ownership, coupling, extensibility, or maintainability problems. Do not use for a class-reference lookup or a single Editor operation.
---

# Design Unreal Gameplay Architecture

Design responsibilities and data flow before choosing classes, Blueprints, or C++ implementations.

## Load the Handbook chapter

Read [03-gameplay-architecture.md](references/03-gameplay-architecture.md) before designing or reviewing the system. Apply its ownership, lifecycle, authority, persistence, networking, and validation boundaries rather than reducing the request to framework-class selection.

## Define the gameplay contract

1. State the player experience, rules, and authoritative outcomes.
2. Identify actors, systems, data, and external services that participate.
3. Assign ownership for state, decisions, presentation, input, persistence, and replication.
4. Describe lifecycle: creation, initialization, activation, transition, teardown, travel, and recovery.
5. Map data flow and communication direction. Prefer explicit interfaces and events over hidden coupling.
6. Separate durable game state from transient presentation and cached data.
7. Decide authority and prediction boundaries before networking implementation.
8. Define extension points without creating abstractions that have no current responsibility.

## Evaluate alternatives

Compare designs using:

- correctness and authority;
- coupling and dependency direction;
- lifecycle safety;
- testability and observability;
- save, load, travel, and reconnect behavior;
- multiplayer implications;
- Blueprint and C++ integration;
- team ownership and future change cost.

Do not reduce Gameplay Architecture to a list of framework classes. Select framework roles only after responsibilities are clear.

## Validate before implementation

Require scenarios for normal flow, invalid transitions, teardown, persistence, authority conflicts, late join or reconnect when relevant, and failure recovery. Define what evidence proves each scenario and which warnings reveal an architectural problem.

When implementation is requested, pass the responsibility map, lifecycle, interfaces, state model, and validation cases to the appropriate Editor or coding skill.
