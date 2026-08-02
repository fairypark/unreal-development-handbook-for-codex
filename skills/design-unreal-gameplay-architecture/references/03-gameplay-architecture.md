# 03 — Gameplay Architecture

## Purpose

Organize gameplay rules, state, input, persistence, networking, and presentation into responsibilities that remain correct across runtime transitions and project growth.

## Intent

Design from the player experience and authority model rather than from a catalog of Gameplay Framework classes.

## Design workflow

1. State player actions, rules, outcomes, and invalid states.
2. Identify participating systems, actors, data, UI, and services.
3. Assign authority for decisions and ownership for durable state.
4. Separate input interpretation, gameplay policy, execution, feedback, and presentation.
5. Define creation, initialization, possession, travel, respawn, teardown, save, load, reconnect, and failure paths as applicable.
6. Map communication direction and data contracts.
7. Decide persistence and replication boundaries before implementation.
8. Choose Gameplay Framework roles, components, subsystems, data assets, Blueprint, or C++ only after the responsibility map is stable.

## Key boundaries

- Keep transient visual state separate from authoritative gameplay state.
- Avoid placing unrelated persistent policy on short-lived actors.
- Distinguish per-player, per-match, per-world, and application-lifetime state.
- Prefer explicit events or interfaces over repeated casts and hidden searches.
- Make server authority, client prediction, reconciliation, and late-join behavior deliberate when networking applies.
- Give save data a versioned contract rather than serializing incidental runtime structure.

## Replication strategy is an architecture decision

Choose a replication strategy from the authority model, actor population, relevancy rules, update rates, late-join and reconnect requirements, prediction and reconciliation behavior, server cost, and migration constraints. Player count alone is not a sufficient decision rule, and a newer or more scalable system does not remove the need to define gameplay ownership.

| Strategy | Fit to investigate | Trade-offs to validate |
| --- | --- | --- |
| Generic Replication | A small or medium population, a straightforward relevancy model, or a compatibility-first baseline. | Per-object update and relevancy cost, bandwidth, late join, and whether growing actor counts make the baseline unsustainable. |
| Replication Graph | A large actor population with spatial, group, or connection-specific relevancy that benefits from an explicit routing model. | Graph ownership, dynamic membership, lifecycle and debugging complexity, driver compatibility, and CPU cost under movement or reconnect. |
| Iris | A project that needs shared serialization, filtering, prioritization, or a deliberate migration to the Iris replication model. | Opt-in and migration boundaries, filtering and prioritization semantics, dirty-state behavior, subobject contracts, compatibility, and rollback or fallback strategy. |

Treat Iris as an implementation option that must pass the project's architecture and production gates, not as a default chosen from a maturity label. Public documentation and release material can describe different audiences or support states; record the target engine version, license or distribution context, feature maturity source, selected driver, and project acceptance evidence in the production contract. Do not treat Replication Graph and Iris as interchangeable assumptions: their ownership, filtering, prioritization, and migration boundaries must be designed and tested explicitly.

## Validation checklist

- Normal player flow and invalid transitions.
- Ownership during spawn, possession, travel, respawn, and teardown.
- Save/load compatibility and missing or old data.
- Authority conflicts, latency, reconnect, and late join when relevant.
- The selected replication strategy and rejected alternatives, including engine version and migration constraints.
- Relevancy, filtering, prioritization, bandwidth, server CPU, prediction, reconciliation, late join, and reconnect under representative load.
- Replicated subobjects, travel, save/load, teardown, and failure recovery with the selected replication driver.
- A documented fallback, migration, or rollback path when the replication strategy or engine version changes.
- UI and presentation consistency without becoming authoritative.
- Automated domain tests plus representative PIE or runtime scenarios.
- Recovery from partial initialization and external-service failure.

## Common mistakes

- Treating `GameMode`, `GameState`, `PlayerState`, or a subsystem name as sufficient design reasoning.
- Keeping important state on an object whose lifecycle is shorter than the state.
- Mixing presentation callbacks with game-rule authority.
- Adding replication after designing a single-player ownership model.
- Using a global singleton to avoid defining a real boundary.
- Selecting a replication system because an upstream release label says it is ready, without recording audience, version, license, or project evidence.
- Measuring packet throughput while missing gameplay correctness, late join, reconnect, or migration behavior.
- Combining Replication Graph and Iris assumptions without a clear driver, ownership, and fallback contract.

## Research basis and further reading

- [Epic Games: Networking Overview](https://dev.epicgames.com/documentation/unreal-engine/networking-overview-for-unreal-engine?lang=en-US) — identifies Generic Replication, Replication Graph, and Iris as separate replication systems and recommends choosing deliberately from their trade-offs.
- [Epic Games: Replication Graph](https://dev.epicgames.com/documentation/unreal-engine/replication-graph-in-unreal-engine?lang=en-US) — describes persistent, shared actor-list routing for large numbers of actors and connections; use the production fit and CPU claims as hypotheses to measure in the project.
- [Epic Games: Introduction to Iris](https://dev.epicgames.com/documentation/unreal-engine/introduction-to-iris-in-unreal-engine) — documents Iris as opt-in and explains its authority, state, filtering, prioritization, and migration context.

## Related topics

Project & System Architecture; Blueprint; C++; Validation, Testing & Debugging; Performance & Scalability; Production Pipeline.
