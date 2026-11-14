# 11 — Performance & Scalability

## Purpose

Keep Unreal experiences viable across target hardware, content growth, runtime variability, and production change without sacrificing the wrong quality dimension.

## Decision contrast: Optimize the limiting cost under the actual target

**Evidence class:** constructed teaching scenario; no measured production outcome is claimed.

**Situation.** A scene misses its frame target. One proposed fix rewrites gameplay graphs; another reduces the rendering work suspected of saturating the target device.

**Choice and reason.** Measure the limiting frame stage, memory pressure, and representative workload before selecting either fix. Improving a non-limiting stage may leave the perceived frame time unchanged while consuming development effort.

**When the choice changes.** A different device, resolution, camera, or gameplay load can move the bottleneck. A fix that helped one run is not a universal quality setting, and a single average can hide unacceptable spikes.

**Smallest useful test.** Compare the relevant CPU/GPU and frame-time distribution under the same target identity and route. Recheck behavior and the visual budget after the smallest measured intervention.

## Intent

Set budgets and measurement conditions before optimization. Find the limiting system and repair its cause rather than applying broad quality loss.

## Budget model

Define target platform, frame-time goal, CPU and GPU envelopes, memory, streaming, load time, storage, network, and scalability expectations as applicable. Allocate budgets to systems with known owners and representative scenarios.

## Version-aware performance budgets

Performance budgets are valid only with an engine and feature identity. For each material rendering, streaming, networking, or content-generation feature, record the engine version and build, target hardware, maturity status, required prerequisites, expected cost envelope, scalability controls, fallback, and the evidence date. Re-run the baseline when any of those identities change.

Upstream feature maturity is a prioritization signal, not a project guarantee. A feature marked Production Ready may still be unsuitable for a target device, a particular content density, or a project's recovery policy. A Beta or Experimental feature can be valuable in a bounded experiment, but its adoption requires a comparable fallback and an explicit decision about whether a later migration can be absorbed.

The UE 5.8 release is a useful example of why this distinction matters: Epic reports improvements to shader compilation, shader deduplication, and PSO pre-caching, while also changing the maturity of features such as MegaLights and Lumen Lite. Those engine improvements should lead to new cold-start, warm-start, shader hitch, fallback-rendering, and target-platform measurements—not to the assumption that every project inherits the same result.

## Target identity beyond platform name

Treat a target as a structured identity, not only as a device or operating
system label. Record the engine/build and renderer configuration together with
the packaged runtime architecture (for example x64, ARM64, or ARM64EC),
authoring and build-host architecture, compiler and toolchain, SDK/GDK,
plugin or middleware ABI, hardware/device revision, scalability settings, and
content or streaming configuration. Keep runtime-target evidence separate from
Editor and build-host evidence: a project may package for one architecture
while authoring, cooking, or validating on another, and those environments do
not share the same performance, compatibility, or failure assumptions.

Re-establish CPU, GPU, memory, shader, I/O, streaming, startup, and hitch
baselines when any part of that identity changes. Record architecture-specific
fallbacks and plugin compatibility before treating a result as portable. A
performance improvement on one architecture or host is a hypothesis for the
next target, not transferable proof.

### Effective configuration and provenance

A named project configuration, scalability tier, or preview platform is not
the same as the configuration that a packaged runtime actually consumed. Treat
effective configuration as resolved state with provenance. For each performance
or release claim, record the relevant configuration-category and profile
revisions, selected device profile, scalability or user-settings state, launch
arguments and explicit overrides, and code, plugin, or hotfix overrides. For
claim-relevant variables, retain a secret-safe snapshot of the effective value,
its winning source or priority, and whether it was applied before the capture.
Do not flatten conflicting sources into one nominal setting; preserve the
overridden source and the reason it did not win.

The snapshot should be scoped to the claim rather than attempting to archive
every variable. Omit or redact sensitive values, and record the omission. An
Editor viewport setting or preview profile may guide diagnosis, but it is not
packaged-runtime evidence until the target build's effective configuration is
verified under the same workload.

### Match the measurement mode to the claim

Before comparing runs, state whether the test is measuring controlled
implementation cost or the player-facing behavior of an adaptive target. For
controlled cost, hold the resolution or screen-percentage policy, scalability
state, camera or route, warm-up, and timing window constant, then compare the
frame-time distribution and the relevant resource cost. For player-facing
behavior, preserve the target's normal adaptation policy and report frame time,
hitches, dynamic-resolution behavior, and image-quality consequences together.
Do not treat a fixed-resolution cost result and an adaptive-experience result
as the same claim.

Record the measurement mode and metric set with the effective configuration and
run identity. A dated UE 5.8 Automated Performance Testing example illustrates
the distinction: a performance mode observes metrics such as missed-vsync
percentage and dynamic-resolution behavior, while a GPU-cost mode holds the
dynamic-resolution percentage fixed so total frame time is more directly
comparable. The example is highly experimental and does not prescribe a
project-wide tool choice; the durable rule is to control or observe the
variable according to the question being answered.

### Run-bound capture and instrumentation health

A performance result is comparable only when the automation report, trace,
log, screenshot, and derived metric refer to the same process or session
attempt. Give each attempt a stable project-level run identity and bind every
artifact to it, rather than inferring identity from a filename, timestamp, or
the presence of a report. Record the capture window relative to process and
workload start, the required trace channels and targets, start and close
status, instrumentation mode and expected overhead, and trace or transport
health. A late-connected trace may be useful for diagnosis while missing
startup, warm-up, or allocation history; it is not automatically a complete
baseline.

Use the shared gate states from Chapter 12 and the artifact lineage from
Chapter 13. A run with mismatched artifact identities, missing required
channels, dropped or panicked tracing, incomplete close/flush, or unmeasured
instrumentation skew is `PENDING_EVIDENCE` or `INVALID_EVIDENCE`, not a
performance pass. Keep diagnostic captures separate from budget runs when
their channels, metadata, or collection overhead can change the workload. An
accepted performance record therefore contains the run identity, effective
configuration snapshot, target and workload identity, capture completeness,
health/overhead verdict, derived metrics, and the comparable baseline or
fallback decision.

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
- Target identity includes runtime and authoring/build-host architecture, compiler/toolchain, SDK/GDK, plugin or middleware ABI, and renderer/scalability configuration—not only the platform name.
- Claim-relevant packaged-runtime configuration has a secret-safe effective snapshot with profile/config revisions, override sources or priority, winning values, and recorded omissions; Editor preview settings are not treated as runtime proof.
- Measurement mode is explicit: controlled cost or target experience; resolution, dynamic-resolution, scalability, and metric choices match the claim, and fixed/adaptive runs are not mixed as one baseline.
- Automation, trace, log, and derived metrics share a stable run identity; capture start/close, required channels, transport health, and instrumentation overhead are recorded, and incomplete or skewed captures are not used as comparable performance evidence.
- No visual, traversal, authority, or persistence regression.
- Regression thresholds and owners for future changes.

## Common mistakes

- Optimizing from Actor count or intuition without profiling.
- Claiming authoring-speed gains from regeneration time alone.
- Measuring an empty or unrepresentative scene.
- Lowering all quality instead of repairing the bottleneck.
- Treating editor performance as packaged runtime evidence.
- Reusing a performance result after changing the engine, renderer, streaming mode, or feature maturity without re-establishing the baseline.
- Reusing a result across x64, ARM64, or ARM64EC, or between a packaged runtime and an Editor/build host, without architecture, toolchain, SDK/GDK, plugin-ABI, and fallback evidence.
- Recording only a project `.ini` or a named scalability tier while ignoring Device Profile, GameUserSettings, command-line, code, plugin, or hotfix overrides; the effective runtime may be different.
- Treating an Editor scalability change or preview platform as proof of the final packaged build without verifying the target runtime's resolved configuration.
- Comparing frame-time results gathered under different resolution or dynamic-resolution policies, or using an adaptive result to claim controlled render cost.
- Treating a self-describing trace, an exported test report, or a late-connected session as proof that the required workload window was captured completely and comparably.
- Mixing diagnostic trace channels or metadata with budget runs without recording their overhead or separating the resulting evidence class.

## Research basis and further reading

- [Epic Games: State of Unreal 2026](https://www.unrealengine.com/news/state-of-unreal-2026-top-news) — UE 5.8 shader compilation, PSO pre-caching, and feature-maturity context.
- [Epic Games: Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration) — frame-time, CPU/GPU, memory, and target-device profiling principles.
- [Epic Games: Configuration Files in Unreal Engine 5.8](https://dev.epicgames.com/documentation/unreal-engine/configuration-files-in-unreal-engine?lang=en-US) — configuration categories, hierarchy, platform layers, and override behavior.
- [Epic Games: Console Variables and Commands in Unreal Engine 5.8](https://dev.epicgames.com/documentation/unreal-engine/console-variables-cplusplus-in-unreal-engine?lang=en-US) — CVar sources, priority, command-line and code overrides; use the precedence as version-specific evidence, not as a Handbook API recipe.
- [Epic Games: Setting Up Device Profiles in Unreal Engine 5.8](https://dev.epicgames.com/documentation/unreal-engine/setting-up-device-profiles-in-unreal-engine) — device-specific configuration and scalability overrides.
- [Epic Games: Creating a Low-Overhead Mobile Project in Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/creating-a-lowoverhead-mobile-project) — editor scalability changes versus startup configuration and target-preview limitations.
- [Epic Games: Review Test Results in Unreal Engine 5.8](https://dev.epicgames.com/documentation/unreal-engine/review-test-results-in-unreal-engine) — Automation JSON's run events, durations, device details, and artifact fields; use them as inputs to a project run contract, not as a complete performance verdict.
- [Epic Games: Horde Automation Hub for Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-automation-hub-for-unreal-engine) — searchable test metadata and historical comparison across streams, platforms, configurations, targets, RHIs, and variations.
- [Epic Games: Developer Guide to Tracing in Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/developer-guide-to-tracing-in-unreal-engine) — self-describing `.utrace` sessions and `.ucache` companions; format self-description does not prove capture completeness.
- [Epic Games: Trace in Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/trace-in-unreal-engine-5) — tail tracing, late connection, important-event caching, and trace transport context.
- [Epic Games: Memory Insights in Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/memory-insights-in-unreal-engine) — a concrete case where the required memory channel must be active from process start.
- [Epic Games: A Tech Artist's Guide to Automated Performance Testing](https://dev.epicgames.com/community/learning/talks-and-demos/0zx9/unreal-engine-a-tech-artist-s-guide-to-automated-performance-testing) — dated UE 5.8 experimental example of adaptive-experience versus fixed-resolution cost measurements; use the distinction, not the tool setup, as the durable lesson.
- [Epic Games: Unreal Engine 5.8 Release Notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) — dated Trace health signals including trace-performance statistics, panic-mode invalidation, close events, and hitch snapshots.
- [Epic Games: Guidelines for Optimizing Rendering for Real-Time](https://dev.epicgames.com/documentation/en-us/unreal-engine/guidelines-for-optimizing-rendering-for-real-time-in-unreal-engine?lang=en-US) — performance budgets, packaging considerations, and repeatable measurement.
- [Epic Games: Windows ARM64 Support in Unreal Engine 5.8](https://dev.epicgames.com/documentation/unreal-engine/windows-arm64-support-in-unreal-engine-5-8) — a dated example of architecture-specific feature maturity, Editor/build constraints, GDK, and compiler limitations; verify the target release and project dependencies.

## Related topics

Rendering; Procedural Systems & PCG; Production Pipeline; Validation, Testing & Debugging.
