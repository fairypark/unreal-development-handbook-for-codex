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

Before accepting level prototype evidence, require a recorded Area Composition Plan that predates the first geometry mutation. It must define a stable-ID set of fixed overview cameras whose risk-based coverage includes arrival, reverse, lateral, waterway/axis, elevation, and project-specific relationships; a single hero overview or an arbitrary fixed count is insufficient. Treat every overview as `DIAGNOSTIC_ONLY`: the set may be the primary macro-composition diagnostic but never approves player visibility, scale, readability, or typology. During Stages 2–4, allow recorded player-height/FOV proxies only to reject gross scale, width, slope, or occlusion failures. Require the actual runtime camera rig at Stage 5 Playable Blockout, and use it for readability, asset-density, and visual-composition evidence from the Visual Feasibility Slice onward.

## Preserve evidence integrity

Do not let the builder silently lower the acceptance bar. Keep failed and superseded results, compare from equivalent conditions, and require independent read-only review when the risk or policy warrants it. A focused repair pass closes only its named target; it does not imply full production acceptance.

Report the evidence, blockers, weakest system, next corrective action, regression risk, and truthful gate state. Leave concrete test commands, profiler operation, captures, packaging, and Editor mutation to the appropriate execution skill.
