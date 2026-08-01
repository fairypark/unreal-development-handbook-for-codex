# 11 — Performance & Scalability

## Purpose

Keep Unreal experiences viable across target hardware, content growth, runtime variability, and production change without sacrificing the wrong quality dimension.

## Intent

Set budgets and measurement conditions before optimization. Find the limiting system and repair its cause rather than applying broad quality loss.

## Budget model

Define target platform, frame-time goal, CPU and GPU envelopes, memory, streaming, load time, storage, network, and scalability expectations as applicable. Allocate budgets to systems with known owners and representative scenarios.

## Version-aware performance budgets

Performance budgets are valid only with an engine and feature identity. For each material rendering, streaming, networking, or content-generation feature, record the engine version and build, target hardware, maturity status, required prerequisites, expected cost envelope, scalability controls, fallback, and the evidence date. Re-run the baseline when any of those identities change.

Upstream feature maturity is a prioritization signal, not a project guarantee. A feature marked Production Ready may still be unsuitable for a target device, a particular content density, or a project's recovery policy. A Beta or Experimental feature can be valuable in a bounded experiment, but its adoption requires a comparable fallback and an explicit decision about whether a later migration can be absorbed.

The UE 5.8 release is a useful example of why this distinction matters: Epic reports improvements to shader compilation, shader deduplication, and PSO pre-caching, while also changing the maturity of features such as MegaLights and Lumen Lite. Those engine improvements should lead to new cold-start, warm-start, shader hitch, fallback-rendering, and target-platform measurements—not to the assumption that every project inherits the same result.

## Measurement workflow

1. Reproduce the target workload and configuration.
2. Capture a stable baseline with representative content.
3. Identify whether CPU, GPU, memory, streaming, I/O, networking, or content authoring is limiting.
4. Attribute cost to a responsible system or content family.
5. Change one major variable.
6. Re-run the same workload and inspect visual, gameplay, and production regressions.
7. Keep the change only when it improves the target without violating another required outcome.

## Content and world considerations

Choose Landscape resolution, component layout, texture treatment, collision, procedural density, instancing, LOD or Nanite, HLOD, World Partition, and reserve content together. A larger world is not automatically a more detailed surface, and dense empty data can be as wasteful as visibly insufficient content.

## Scalability policy

Define which qualities may change by tier and which preserve design intent. Protect gameplay readability, collision, authority, and essential feedback. Prefer controlled density, distance, shadow, effect, or material changes over ad hoc per-level degradation.

## Validation checklist

- Representative worst, typical, and transition scenarios.
- Stable capture conditions and correct target configuration.
- CPU, GPU, memory, streaming, load, and frame-pacing evidence as relevant.
- LOD, Nanite, instancing, HLOD, World Partition, and cook behavior.
- Engine and feature version identity, maturity, platform prerequisites, fallback behavior, and regression thresholds are attached to the baseline.
- No visual, traversal, authority, or persistence regression.
- Regression thresholds and owners for future changes.

## Common mistakes

- Optimizing from Actor count or intuition without profiling.
- Claiming authoring-speed gains from regeneration time alone.
- Measuring an empty or unrepresentative scene.
- Lowering all quality instead of repairing the bottleneck.
- Treating editor performance as packaged runtime evidence.
- Reusing a performance result after changing the engine, renderer, streaming mode, or feature maturity without re-establishing the baseline.

## Research basis and further reading

- [Epic Games: State of Unreal 2026](https://www.unrealengine.com/news/state-of-unreal-2026-top-news) — UE 5.8 shader compilation, PSO pre-caching, and feature-maturity context.
- [Epic Games: Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration) — frame-time, CPU/GPU, memory, and target-device profiling principles.
- [Epic Games: Guidelines for Optimizing Rendering for Real-Time](https://dev.epicgames.com/documentation/en-us/unreal-engine/guidelines-for-optimizing-rendering-for-real-time-in-unreal-engine?lang=en-US) — performance budgets, packaging considerations, and repeatable measurement.

## Related topics

Rendering; Procedural Systems & PCG; Production Pipeline; Validation, Testing & Debugging.
