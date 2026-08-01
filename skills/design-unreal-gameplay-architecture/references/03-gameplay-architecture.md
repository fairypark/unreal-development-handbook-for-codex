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

## Validation checklist

- Normal player flow and invalid transitions.
- Ownership during spawn, possession, travel, respawn, and teardown.
- Save/load compatibility and missing or old data.
- Authority conflicts, latency, reconnect, and late join when relevant.
- UI and presentation consistency without becoming authoritative.
- Automated domain tests plus representative PIE or runtime scenarios.
- Recovery from partial initialization and external-service failure.

## Common mistakes

- Treating `GameMode`, `GameState`, `PlayerState`, or a subsystem name as sufficient design reasoning.
- Keeping important state on an object whose lifecycle is shorter than the state.
- Mixing presentation callbacks with game-rule authority.
- Adding replication after designing a single-player ownership model.
- Using a global singleton to avoid defining a real boundary.

## Related topics

Project & System Architecture; Blueprint; C++; Validation, Testing & Debugging.
