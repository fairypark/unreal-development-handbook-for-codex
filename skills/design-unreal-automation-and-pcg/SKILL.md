---
name: design-unreal-automation-and-pcg
description: Design or review Unreal automation, Python, batch workflows, procedural systems, and PCG through repeatability, determinism, authorial control, data flow, scalability, failure handling, and validation. Use before automating repetitive Editor work, building procedural content, comparing generated candidates, or diagnosing nondeterministic and unsafe pipelines. Do not use for a one-off command invocation.
---

# Design Unreal Automation and PCG

Automate an approved responsibility and validation contract, not an unclear design.

## Load the relevant Handbook chapter

- Read [08-automation-python.md](references/08-automation-python.md) for repeatability, Python, batch work, failure handling, or pipeline automation.
- Read [09-procedural-systems-pcg.md](references/09-procedural-systems-pcg.md) for procedural content, PCG, deterministic generation, spatial rules, or authorial control.
- Read both when automation builds, validates, or promotes procedural systems.

## Decide what to automate

1. State the repeated responsibility, inputs, outputs, owner, and acceptable variation.
2. Confirm that the underlying manual or authored result is understood and testable.
3. Separate generic orchestration from project-specific content and parameters.
4. Choose the smallest implementation surface that supports required engine access and reliability.
5. Define deterministic controls, idempotence, overwrite policy, cancellation, partial failure, recovery, and audit output.

For a small edit on an already accepted prototype, use the Handbook's `BOUNDED_PROTO_EDIT` transaction boundary rather than treating the request as a new batch build. Batch the compact inspect, serialize the declared mutation, verify the in-memory postcondition, save, and perform a persistence re-read. Return separate `operation_verdict` and `promotion_verdict` values; visual capture, PIE, and broad composition review are `NOT_RUN_BY_CONTRACT` unless the scope requires reopening them. Cache task-scoped schema knowledge and make optional/default fields explicit, but never let a compact response or omitted API field weaken target, protected-scope, or save verification.

## Design procedural systems

- Author one coherent source assembly or spatial rule before proceduralizing it.
- Give each generator a distinct responsibility and use one authority for exclusions and final composition.
- When a request contains spatially dependent strata such as rocks or hardscape plus grass or ground cover, run the **Dependent-Strata Strategy Gate** before the first content-bearing generator mutation. Always record `CONSIDERED`, the selected mode (`VIDEO_DISTANCE_EXCLUSION`, `MASK_OTHER`, `DIRECT_AUTHORED`, or `PENDING_EVIDENCE`), the reason, source authority, dependency order, units, clearance, transition band, and validation status. Do not silently skip the video-style distance/exclusion option; select it when the source footprint is stable and the dependent layer should clear or approach that footprint, and select another mode when the source is exploratory, hero-specific, or not spatially trustworthy.
- For dependent strata such as ground cover around hardscape, make the source footprint, clearance band, and dependency order part of the data contract.
- Preserve hierarchy and dependent-child relationships.
- Expose seeds, masks, density, scale, and platform constraints for reviewable change.
- Compare one procedural candidate at a time; overlapping active generations invalidate the comparison.
- Preserve authorial control for focal composition, transitions, exceptions, and story detail.

## Validate beyond successful generation

Measure authoring and setup time separately from regeneration time. Verify determinism, counts, coverage, grounding, hierarchy, minimum separation after final transforms, collision intent, performance, warnings, save persistence, and representative visual or gameplay evidence. Treat these technical checks as diagnostic; they do not grant aesthetic or production approval by themselves.

Use Python, PCG Graph, Blueprint, C++, Commandlet, or Editor-tool execution only after this contract is explicit.
