# 02 — Project & System Architecture

## Purpose

Define stable responsibilities, boundaries, dependencies, and lifecycles so Unreal systems can evolve without hidden coupling or escalating maintenance cost.

## Intent

Make it possible to answer who owns a decision, where state lives, how data moves, when objects exist, what may depend on what, and how the system fails and recovers.

## Design considerations

### Responsibility and ownership

Assign one authoritative owner for each durable state and decision. Separate policy, orchestration, data, presentation, and external integration when they change for different reasons.

### Dependency direction

Prefer dependencies that point toward stable contracts. Avoid cycles, broad global reach, and domain-specific duplicates of generic behavior. Reuse an existing capability when its responsibility already matches.

### Lifecycle

Specify creation, initialization, activation, transition, teardown, travel, reload, and recovery. Treat initialization order and invalid transitional states as architectural concerns.

### Data flow

Use explicit inputs, outputs, events, and interfaces. Avoid hiding structured state in strings or relying on incidental object discovery when a durable contract is required.

### API surface

Expose a small typed and composable surface rather than mirroring the entire engine API. Return normal structured results on success and explicit failures on error. Maintain create, read, update, and delete symmetry where mutation genuinely supports it.

### Extensibility

Create extension points for known variation, not hypothetical flexibility. Prefer a clear current responsibility with a migration path over a large abstraction without users.

## Validation checklist

- Can every state and decision be assigned to one owner?
- Are dependency direction and forbidden cycles explicit?
- Are lifecycle and teardown paths testable?
- Are errors distinguishable from empty valid results?
- Can the system be observed without breaking encapsulation?
- Can one implementation technology be replaced without rewriting the domain intent?
- Are rollback and compatibility boundaries defined?

## Common mistakes

- Selecting framework classes before assigning responsibilities.
- Duplicating generic behavior inside every domain.
- Creating broad APIs for agent convenience without stable semantics.
- Adding abstraction to hide a confused ownership model.
- Treating a generated schema as the architecture itself.

## Related topics

Gameplay Architecture; Content & Asset Architecture; Blueprint; C++; AI-Assisted Development.
