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

Expose a small typed and composable surface rather than mirroring the entire engine API. Design every mutation beside the observation needed to plan it and verify it: callers should be able to get, list, or inspect the relevant identity, current state, dependencies, and capability limits without mutating the project. Maintain create, read, update, and delete symmetry where those lifecycle operations are meaningful; do not add destructive symmetry merely for completeness.

Define request and response schemas with units, coordinate spaces, defaults, bounds, identity rules, side effects, save behavior, concurrency assumptions, and version or capability scope. Return ordinary structured data on success. Distinguish a valid empty result from unsupported capability, invalid input, missing target, partial completion, timeout, cancellation, and internal failure. Errors should identify the failed responsibility, any known partial state, whether retry is safe, and the next observation or recovery action.

Prefer focused operations that can be composed into a bounded workflow. A broad convenience endpoint that hides discovery, mutation, saving, and validation prevents callers from proving where a failure occurred. Observation parity and explicit postconditions make the same interface usable by people, automation, tests, and AI agents without giving any of them implicit approval authority.

### Extensibility

Create extension points for known variation, not hypothetical flexibility. Prefer a clear current responsibility with a migration path over a large abstraction without users.

## Validation checklist

- Can every state and decision be assigned to one owner?
- Are dependency direction and forbidden cycles explicit?
- Are lifecycle and teardown paths testable?
- Are errors distinguishable from empty valid results?
- Can the system be observed without breaking encapsulation?
- Can every mutation be planned and re-read through a non-mutating observation path?
- Are identity, units, coordinate spaces, defaults, side effects, save behavior, and capability/version scope explicit?
- Do partial, timeout, and cancellation failures report known state and a safe recovery or inspection action?
- Can one implementation technology be replaced without rewriting the domain intent?
- Are rollback and compatibility boundaries defined?

## Common mistakes

- Selecting framework classes before assigning responsibilities.
- Duplicating generic behavior inside every domain.
- Creating broad APIs for agent convenience without stable semantics.
- Exposing a setter without the corresponding get, list, or inspect path needed to verify its effect.
- Returning one ambiguous success or error shape for empty results, partial mutation, timeout, and unsupported capability.
- Adding abstraction to hide a confused ownership model.
- Treating a generated schema as the architecture itself.

## Related topics

Gameplay Architecture; Content & Asset Architecture; Blueprint; C++; AI-Assisted Development.
