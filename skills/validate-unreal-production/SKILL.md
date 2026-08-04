---
name: validate-unreal-production
description: Define, execute conceptually, or review Unreal production validation across rendering, performance, testing, debugging, content flow, builds, cooking, packaging, release readiness, collaboration, source control, recovery, and rollback. Use when setting success criteria, quality gates, evidence, budgets, test layers, or a definition of done. Do not use as a substitute for the tools that run tests or mutate the Editor.
---

# Validate Unreal Production

Define success before implementation and judge the final outcome against evidence rather than effort or command success.

## Load only the relevant Handbook chapters

- Read [12-validation-testing-debugging.md](references/12-validation-testing-debugging.md) for every validation or production-readiness request.
- Also read [10-rendering.md](references/10-rendering.md) for visual goals, materials, lighting, atmosphere, or rendered evidence.
- Also read [11-performance-scalability.md](references/11-performance-scalability.md) for budgets, profiling, streaming, memory, frame time, load, or scalability.
- Also read [13-production-pipeline.md](references/13-production-pipeline.md) for builds, cooking, packaging, deployment, distribution, or operational recovery.
- Also read [14-team-collaboration-source-control.md](references/14-team-collaboration-source-control.md) for ownership, review, integration, handoff, asset conflicts, or source control.

## Build the validation system

1. Translate intent and requirements into observable success criteria.
2. Classify checks as experience, functional, visual, performance, compatibility, persistence, collaboration, delivery, or recovery evidence.
3. Define the required environment, configuration, platform, data, and comparison baseline.
4. Separate hard failures from scored qualities and acceptable warnings.
5. Assign authority for producing evidence, reviewing it, approving promotion, and initiating rollback.
6. Establish gate states that distinguish pass, fail, pending evidence, and invalid evidence.

For a declared `BOUNDED_PROTO_EDIT` on an already accepted prototype, define a compact `operation_verdict` over the explicit target set, protected-scope snapshot, target-specific transform/grounding postcondition, and saved persistence. Keep `promotion_verdict` separate and unchanged: full visual review, PIE, independent review, broad Area Composition Plan/translation re-check, and fixed-camera evidence may be `NOT_RUN_BY_CONTRACT`, not an accidental pass. Direct Landscape, water, bridge, zone-marker, route/navigation, streaming, camera, or playable-composition changes reopen the normal validation gates; the fast path is a scope-risk reduction, not removal of safety.

## Cover the production lifecycle

Include relevant layers:

- static and structural checks;
- compile, asset, and automation tests;
- PIE or runtime scenarios;
- rendering and fixed-condition visual evidence;
- CPU, GPU, memory, streaming, load, and scalability budgets;
- cook, package, deployment, and clean-environment checks;
- source-control recovery and integration checks;
- representative edge cases and failure recovery.

For level work, validate the fun thesis and at least one POI or encounter unit alongside spatial, runtime, visual, performance, and delivery evidence. Treat experience density, tension and release, player choice, and payoff as design-specific criteria; do not replace them with a universal score or a fixed spacing rule.

Before accepting level prototype evidence, require both a recorded Area Composition Plan and a `PASS`ed Stage 2a Reference-to-Prototype Translation Contract before the first content-bearing geometry mutation. The plan must define a stable-ID set of fixed overview cameras whose risk-based coverage includes arrival, reverse, lateral, waterway/axis, elevation, and project-specific relationships; a single hero overview or an arbitrary fixed count is insufficient. Use the world-design Skill's [schema](../design-unreal-worlds-and-levels/references/reference-to-prototype-translation.schema.json) and [template](../design-unreal-worlds-and-levels/references/reference-to-prototype-translation.template.json), or a documented equivalent. The translation contract must inventory source authority, define zone-level quantitative composition ranges and hard failures, trace every planned and realized proxy group, path, water or bridge feature, reserved void, and terrain change to a source requirement, and preserve same-condition deviation evidence. Treat every fixed overview as `DIAGNOSTIC_ONLY`: it may approve assigned macro metrics such as zone distribution, footprint, density, hierarchy, paths, terrain, water, shade or void preservation, and silhouette, but never player visibility, scale, readability, or typology. During Stages 2–4, allow recorded player-height/FOV proxies only to reject gross scale, width, slope, or occlusion failures. Require the actual runtime camera rig at Stage 5 Playable Blockout, and use it for distance, enclosure, occlusion, route continuity, readability, asset density, and player-facing visual composition from the Visual Feasibility Slice onward.

Before accepting concept-led asset work, require the Content & Asset Architecture Skill's [Concept-to-Asset Readiness schema](../design-unreal-content-architecture/references/concept-to-asset-readiness.schema.json) and [template](../design-unreal-content-architecture/references/concept-to-asset-readiness.template.json), or a documented equivalent. Require `ASSET_PLAN_READY` before the Experience Prototype, `VISUAL_SLICE_READY` before Stage 6, and `PRODUCTION_DRESSING_READY` before Stage 7. Verify that demands trace to approved source requirements and zones; project-native and ownership-confirmed inventory was considered before new acquisition; selected versions have explicit entitlement or provenance, acquisition authority, license, compatibility, dependencies, total integration cost, representative evidence, and rollback; and every production-blocking demand is production-ready or has an approved concept/scope waiver. Treat search, ownership, download, staging, representative approval, and production approval as different evidence states. No design gate authorizes an external transaction or Editor mutation by itself.

## Preserve evidence integrity

Do not let the builder silently lower the acceptance bar. Keep failed and superseded results, compare from equivalent conditions, and require independent read-only review when the risk or policy warrants it. Reject aggregate Actor-count parity as sufficient reference-to-prototype evidence: zone distribution, footprint and density, preserved shade and intentional voids, hierarchy, frontage and gaps, route continuity, water and bridge relationships, and prohibited silhouettes retain separate verdicts. A focused repair pass closes only its named target; it does not imply full production acceptance.

Report the evidence, blockers, weakest system, next corrective action, regression risk, and truthful gate state. Leave concrete test commands, profiler operation, captures, packaging, and Editor mutation to the appropriate execution skill.
