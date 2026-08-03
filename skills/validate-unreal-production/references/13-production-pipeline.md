# 13 — Production Pipeline

## Purpose

Move Unreal content and code from authored source through validation, build, cook, package, deployment, and recovery with explicit ownership and reproducible state.

## Intent

Treat production flow as a system with contracts and failure states, not as a final sequence of buttons after development is complete.

## Pipeline boundaries

Define source inputs, generated outputs, configuration, target platforms, ownership, caches, artifacts, promotion states, retention, and rollback. Separate deterministic mechanics from contextual approval and keep environment-specific configuration outside reusable logic.

## Version and feature release contract

Make engine and feature identity part of the production artifact contract. For every release-relevant engine, plugin, renderer, replication system, procedural system, or capture feature, record:

- engine version, branch or build, plugin versions, project configuration, and target platforms;
- upstream maturity (`Experimental`, `Beta`, or `Production Ready`) and the date of the assessment;
- hardware or platform prerequisites, known limitations, and affected content or systems;
- baseline evidence, fallback behavior, migration cost, owner, and rollback target.

Keep one current version matrix with the release evidence rather than scattering unqualified feature claims through the handbook. A feature can be production-ready upstream and still fail a project's visual, performance, packaging, licensing, or recovery gates. When a version change or maturity change affects a contract, reopen the relevant validation gate and preserve the previous accepted baseline for comparison.

### UE 5.8 snapshot — 2026-08-01

Epic's UE 5.8 release notes describe Iris as Production Ready for licensees, while the public Iris documentation presents it as an opt-in system and labels the feature Experimental. Record the audience, license or distribution context, engine version, and project validation state instead of treating either label as universal. The same UE 5.8 material reports MegaLights and Movie Render Graph as Production Ready; Lumen Lite as Beta; and Mesh Terrain as Experimental. It also describes shader-compilation, shader-deduplication, and PSO pre-caching improvements. Treat this as a dated snapshot, not a timeless handbook rule:

- adopt a Production Ready feature only after target-platform and project-level evidence passes;
- prototype Beta or Experimental features behind a reversible boundary and name the fallback before production content depends on them;
- for Iris, reconcile the licensee release-note status with the public opt-in or Experimental documentation, then validate the selected replication driver and migration path in the project;
- after engine or feature changes, re-run cold and warm startup, shader or PSO behavior, representative runtime, capture, package, and recovery checks;
- for Movie Render Graph, compare output, automation, and recovery behavior with the existing Movie Render Queue path before changing the release pipeline.

## Content promotion and cost control

Level content should move through explicit promotion states so that disposable exploration is not confused with production commitment:

`CONCEPT` → `SPATIAL_PLAN` → `EXPERIENCE_PROTOTYPE` → `EXPERIENCE_VALIDATED` → `PLAYABLE_BLOCKOUT` → `PLAYABLE_VALIDATED` → `VISUAL_FEASIBILITY` → `PRODUCTION` → `AUDIO_AND_LIGHTING_INTEGRATED` → `POLISH` → `RELEASE_CANDIDATE`

Each transition should identify the versioned source, the evidence package, the approver, the known limitations, and the rollback target. A level may contain zones at different states, but map-wide duplication should wait until the representative pattern has passed `VISUAL_FEASIBILITY` under intended asset, lighting, collision, audio, streaming, and performance conditions.

Keep prototypes and production content distinguishable through naming, folders, metadata, or source-control policy. Do not silently replace an accepted blockout with final assets in a way that removes the comparable baseline. If a production asset, generated result, or integration change invalidates route, readability, collision, or budget assumptions, reopen the affected state instead of papering over the difference with local fixes.

## Workflow release versus content promotion

Release the repeatable workflow separately from the content it operates on.
The workflow release record should identify its version, scope, default
operation mode, allowed mutation boundary, test results, known limitations,
rollback path, and whether it changed level content. A status such as
the workflow-release state means that the guardrails and execution contract
are available; it does not mean that the map has passed its spatial, runtime,
visual, performance, or production gates.

This separation allows a project to improve its prototype loop without
pretending that invalid visual evidence or missing runtime review has been
resolved. Keep the level or system's promotion state independently recorded as
`PASS`, `FAIL`, `PENDING_EVIDENCE`, or `INVALID_EVIDENCE`. If the workflow
release itself cannot execute on the available Editor surface, mark live
execution as untested and do not claim that an offline compile or manifest
check proves an in-Editor mutation.

## POI-first production and density planning

For open-world or exploration-heavy levels, organize the content plan around experience units and their relationships, not around uniformly filling terrain. A POI record should include its scale, player question, approach and reveal or refusal, interaction or repeated verb, risk, reward or outcome, next hook, expected time or distance, dependencies, owner, and production cost.

Place large destinations and long-term orientation anchors first, then medium and small POIs that support the route's emotional beats. Use time to the next meaningful change as a diagnostic, calibrated to actual movement speed, camera, vehicle or mount use, fast travel, and genre. A 40-second interval can be an initial open-world exploration hypothesis, but it must not become a mechanical spacing rule or a reason to fill intentional quiet with low-value content.

Before a POI pattern is promoted to `EXPERIENCE_VALIDATED`, test a cheap unit from approach through question, reveal or refusal, player choice, interaction, payoff, and exit or next hook. For a small level, this prototype may be combined with the playable blockout; the evidence still needs to be named. Do not commit map-wide final assets until the POI unit and the surrounding rhythm have survived the relevant playtest.

## Recommended workflow

1. Establish a versioned source and dependency state.
2. Validate content, code, configuration, and required plugins before expensive work.
3. Generate derived content reproducibly and reject unsafe overwrites.
4. Build and cook the intended targets and configurations.
5. Package and test in an environment containing only declared dependencies.
6. Verify startup, loading, representative gameplay, assets, performance, logging, save behavior, and deployment assumptions.
7. Promote artifacts only with evidence and a recovery plan.

For a level, the expensive work begins only after the experience prototype, playable blockout, and representative visual feasibility slice have retired the dominant design and production risks. This does not prohibit early asset experiments; it limits broad, difficult-to-reverse placement until the experience and visual patterns are known to scale.

## Failure handling

Distinguish invalid input, missing dependency, compile failure, cook failure, package failure, deployment failure, runtime regression, and incomplete evidence. Preserve useful logs and artifacts without collecting credentials, private user data, or unrelated project information.

Do not silently retry a partial pipeline stage when duplication, stale output, or corrupted state is possible. Inspect the actual output and clean or roll back only the verified target.

## Distribution readiness

Audit direct and transitive dependencies, licensing, engine compatibility, private paths, user data, asset provenance, version metadata, and installation assumptions. If a clean-project test is not possible, reduce the distribution scope rather than shipping an opaque package with hidden dependencies.

## Validation checklist

- Reproducible inputs, configuration, and version identity.
- Correct build, cook, and package targets.
- Declared dependencies and license-clean distributable content.
- Promotion state, evidence, approver, retention, and rollback target are recorded for each major level milestone.
- Fun thesis, POI inventory, experience-unit evidence, density/tension rationale, and intentional quiet sections are recorded for level milestones.
- Engine, plugin, feature-maturity, target-platform, fallback, and migration state are recorded for release-relevant changes.
- Audience, license or distribution scope, and source date are recorded when different official materials assign different maturity labels.
- Clean-environment installation and startup.
- Representative runtime, performance, persistence, and recovery checks.
- Engine or feature changes include cold/warm, capture, packaging, and rollback evidence where relevant.
- Traceable artifact, approval, rollback, and retention policy.

## Common mistakes

- Treating `Production Ready` as a substitute for project-level acceptance.
- Updating the engine or a render/capture path without preserving a comparable baseline and a rollback target.
- Recording a feature name without its engine version, maturity, target platform, fallback, or evidence date.
- Copying an upstream maturity label without recording its audience, license or distribution scope, and compatibility constraints.

## Research basis and further reading

- [Epic Games: State of Unreal 2026](https://www.unrealengine.com/news/state-of-unreal-2026-top-news) — UE 5.8 feature maturity, shader compilation, shader deduplication, and PSO pre-caching context.
- [Epic Games: Unreal Engine 5.8 Release Notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes) — version-specific release and production-status details.
- [Epic Games: Transitioning to Movie Render Graph from Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/transitioning-to-the-movie-render-graph-from-movie-render-queue-in-unreal-engine) — migration considerations for the capture pipeline.

Additional current context:

- [Epic Games: Introduction to Iris](https://dev.epicgames.com/documentation/unreal-engine/introduction-to-iris-in-unreal-engine) — public opt-in and feature-status context for Iris; confirm the wording against the target engine and distribution.
- [Epic Games: Migrate to Iris](https://dev.epicgames.com/documentation/en-us/unreal-engine/migrate-to-iris-in-unreal-engine) — migration scope and compatibility considerations that belong in the project release contract.

## Related topics

Content & Asset Architecture; Gameplay Architecture; Automation & Python; Rendering; Performance & Scalability; Validation, Testing & Debugging; Team Collaboration & Source Control.
