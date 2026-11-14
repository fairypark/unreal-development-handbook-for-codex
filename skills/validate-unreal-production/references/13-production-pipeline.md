# 13 — Production Pipeline

## Purpose

Move Unreal content and code from authored source through validation, build, cook, package, deployment, and recovery with explicit ownership and reproducible state.

## Decision contrast: Release evidence must reach the destination

**Evidence class:** constructed teaching scenario; no measured production outcome is claimed.

**Situation.** An Editor session succeeds and the build pipeline is green, but the intended recipient has not yet exercised the delivered artifact and its required content.

**Choice and reason.** Treat build success as one pipeline result. Verify the actual artifact, destination dependencies, launch path, representative behavior, and recovery relevant to the release claim.

**When the choice changes.** An explicitly Editor-only prototype can finish without package qualification when reported in that scope. It must not inherit a release claim; equally, a local experiment need not run an unrelated distribution pipeline.

**Smallest useful test.** Exercise the candidate artifact under the declared recipient conditions and retain its identity. Separate product failure, incomplete evidence transport, and untested recovery rather than infer one from another.

## Intent

The retained [prototype-workflow investigation](../../analyze-unreal-development-cases/references/16-case-studies.md#investigation-note-unbounded-prototype-loops-and-dispatch-amplification) reports workflow qualification while the level stayed pending. Transfer the distinction between pipeline success and the destination product's evidence; do not infer that every Editor prototype requires a shipped build.

Treat production flow as a system with contracts and failure states, not as a final sequence of buttons after development is complete.

## Pipeline boundaries

Define source inputs, generated outputs, configuration, target platforms, ownership, caches, artifacts, promotion states, retention, and rollback. Separate deterministic mechanics from contextual approval and keep environment-specific configuration outside reusable logic.

### Derived-output provenance and consumer admission

A generated or transformed result is a separate production artifact, not automatically a release artifact. For every persistent generated output, disposable cache, cooked snapshot, staged container, runtime stream, or platform-specific derived artifact that can affect a consumer, preserve the chain:

`parent inputs → producer or transform → derived output → consumer admission or fallback`

Record, at the scope that can change the result:

- **Parent identity:** source, build, cook, configuration, target, and content revision; input fingerprint; and separate build-time versus runtime dependencies.
- **Producer scope:** engine, plugin, tool, and changelist identity; graph, partition, Data Layer, target, ABI, or driver scope where applicable; expected and actual inventory or coverage; and errors or omissions.
- **Lifetime and lineage:** whether the result is persistent generated content, disposable derived data or cache, cooked/deployment output, or runtime-generated state; its storage or snapshot/descriptor identity; base lineage; retention and garbage-collection owner; and reconstruction path.
- **Consumer admission:** compatibility keys, freshness and invalidation state, and explicit `COMPLETE`, `PARTIAL`, `FAILED`, `STALE`, `INAPPLICABLE`, or `UNKNOWN` classification. File presence, a successful builder, descriptor transport, or cache retrieval is not admission proof.
- **Verification and recovery:** generated-versus-consumed-versus-fallback verdicts, clean rebuild or package/runtime evidence, performance or coverage evidence where relevant, rebuild triggers, and rollback or safe fallback.

UE 5.8 examples (reviewed 2026-10-26) make the boundary concrete without defining universal tool requirements: HLOD output is rebuilt after changes to source Actors, meshes, materials, or textures; the World Partition PCG builder waits for asynchronous work and fails its job on generation errors by default; and Advanced Shader Delivery creates an SODB from a cooked Windows D3D12 SM6 build, then a GPU/driver-specific PSDB, while unsupported consumers fall back to runtime compilation. Keep this contract separate from **Release Artifact Lineage, Integrity Scope, and Rollback**: derived-output provenance explains how an artifact was produced and admitted, while the release contract proves distribution integrity, installation, replacement, and rollback.

### Build-to-test admission and source snapshot

A passing test report belongs to the executable and content it actually
consumed, not merely to a test name, timestamp, or green pipeline job. For a
result that can influence promotion, preserve the chain:

`source snapshot → build recipe and inputs → produced artifact → test session → promotion decision`

Record the identity at the boundary that can change the claim:

- **Source snapshot:** branch and revision or changelist, submitted versus
  shelved/presubmit state, relevant file scope, and whether the workspace was a
  clean sync or carried local state.
- **Build identity:** engine/build version, `BuildId` or compatible-build
  identity where relevant, target/configuration/RHI, toolchain and SDK, and the
  build recipe and parameters that produced the artifact.
- **Workspace and cache state:** pristine versus incremental execution,
  reused intermediates or derived data, dependency/invalidation coverage, and
  any reason a clean rebuild or equivalent recook was not performed.
- **Consumed artifact:** exact executable/content/package/container or other
  tested output, its manifest or digest, and the parent lineage that connects it
  to the source and build record.
- **Test linkage:** run/session/attempt identity, suite and configuration,
  target device or agent, report and raw-artifact references, and the exact
  artifact consumed by the test.
- **Admission scope:** whether the result applies only to a presubmit,
  incremental, branch, or exact artifact scope. A passing shelved change does
  not prove the submitted revision or release artifact; a cache hit or test
  report does not prove source/artifact equivalence.

If the source-to-artifact or artifact-to-test link is unknown, classify the
result as `PENDING_EVIDENCE` or `INVALID_EVIDENCE` for the affected promotion
claim. Keep test correctness, artifact integrity, runtime readiness, and
release approval as separate verdicts. This contract complements Chapter 12's
test isolation and run identity: a clean fixture and stable run can still test
the wrong build.

Epic's UE 5.8 material gives dated examples for this boundary: Horde's
Automation Hub exposes platforms and changelists linked to CI job steps;
Horde Build Automation syncs source-control workspaces and transfers
intermediate and final artifacts; and the build tutorial distinguishes
incremental workspaces, pristine packaged builds, and shelved-changelist
presubmit tests. UE's versioning guidance also records changelist, branch,
`BuildId`, compatible changelist, and promoted clean-sync state. These are
evidence for the contract, not requirements to adopt Horde, Perforce, or a
particular BuildGraph/UAT workflow.

### Release-artifact lineage, integrity, installation, and rollback

A release or update artifact has a different proof boundary from a generated
or tested artifact. For a distribution claim, preserve the applicable chain:

`authorized release → exact artifact and manifest → integrity verified → installed or updated → mounted and content-resolvable → runtime-ready → rollback-ready`

This is a project evidence contract, not a universal Unreal state machine.
Record only the verdicts and transitions that the selected distribution path
actually exposes, while keeping these concerns separate:

- **Release identity and scope:** base release, current release, target update
  or patch identity; platform, runtime architecture, configuration, package or
  container format, manifest version, chunk or bundle inventory, and transitive
  dependency closure.
- **Authorization and trust boundary:** release owner, entitlement or locale
  scope when applicable, manifest freshness and base compatibility, the
  non-secret trust-root or key identifier, and the owner and recovery policy for
  key rotation or revocation. Do not place key material or credentials in the
  evidence record.
- **Integrity:** expected file or container identity, size, digest or version
  check, package/container signature verification, and encryption policy. A
  transport success, size/version match, or encryption result is not by itself
  signature, manifest authorization, freshness, or runtime-readiness proof.
  Record verification coverage and method separately (for example, all files
  versus patch-touched files, and cryptographic hash/signature versus
  existence/size). A narrow check supports only that narrower claim; it is not
  whole-install integrity evidence.
- **Destination transition:** clean install, replacement, update, removal, or
  resume; staging and final destination; prerequisite and free-space result;
  partial or mixed-base state; and whether the previously accepted release was
  retained until the new one passed its checks.
- **Consumer proof and recovery:** installed-file and manifest inventory,
  mount/content resolution, startup and representative runtime evidence, and
  the exact rollback target. Exercise or classify interruption/offline retry,
  stale or wrong-base/replayed manifest, missing or invalid signature,
  partial/corrupt/tampered data, missing parent or dependency,
  entitlement/locale/prerequisite failure, mount or startup failure,
  replacement/uninstall, and rollback. Do not claim a successful update when
  the destination contains an unknown mixture of base and update content.

For a release claim, missing identity, trust, integrity, destination, consumer,
or rollback evidence is `PENDING_EVIDENCE`; a mismatched base, invalid signature,
tampered output, or unrecoverable partial state is `INVALID_EVIDENCE`. Keep the
release verdict separate from test correctness, artifact provenance, and
runtime behavior. The last accepted release must remain an identifiable and
recoverable target, not merely a file that happens to remain on disk.

UE 5.8 documentation supplies dated examples for this boundary: platform-
agnostic patching compares post-cook content with the released cooked base,
requires retained base content and locked serialization paths, and mounts the
patch above the base; Project Settings documents separate pak encryption and
signing; pak signature loading rejects missing or invalid signature data; and
ChunkDownloader separates manifest build/file identity, cached-file version
validation, download, and mount. These examples justify the distinctions but
do not define a universal manifest-authentication, replay-protection,
entitlement, or key-rotation policy. Keep patch, chunk, bundle, signing,
encryption, CDN, store, and platform SDK procedures in execution or project
pipeline documentation rather than this Handbook.

UE 5.8's BuildPatchServices provides a dated example of the same evidence
boundary: verification can cover all files or only files touched by the
install/patch, and can use SHA or file-size checks, while missing, open, hash,
and size failures remain distinct. Record the selected coverage and failure
class without making BuildPatchServices or its API choices a Handbook
requirement.

### Persistent-state compatibility and migration

A release can install, mount, and start while invalidating an existing
player's, session's, or service's durable state. For any release or update
that reads or rewrites SaveGame, profile, settings, progression, world state,
replay, or other persistent data, preserve the applicable chain:

`accepted prior state → compatibility decision → migration or fixup → post-migration invariant → new-state write → rollback or fallback`

Keep this state contract separate from package compatibility and release
artifact integrity. Record, at the boundary that can change the claim:

- **State identity and scope:** schema or data version, state owner and scope
  (user, world, match, or service), source release/build/configuration/content,
  and platform or user identity where applicable.
- **Compatibility decision:** supported old and current versions; behavior for
  missing, unknown/newer, corrupt, partial, or mixed state; one-way or
  bidirectional support; and whether an engine, content, configuration, or
  service change alters interpretation.
- **Migration behavior:** the explicit converter or fixup, ordering and
  dependencies, default/drop/reset decisions, idempotence, atomicity or
  write-after-read policy, retained original or backup, and the observed
  outcome. A successful load does not prove that the intended progression or
  invariants survived.
- **Validation and recovery:** representative fixtures for current, previous
  supported, missing, corrupt, partial, and interrupted states; load before and
  after the update; save after migration; progression and invariant checks;
  multi-user or platform cases when relevant; and retry or rollback evidence.
  Retain the prior state until the migrated state passes its checks and name a
  safe read-only, default, or operator-assisted fallback where applicable.

For a release claim, missing compatibility, migration, post-migration, or
recovery evidence is `PENDING_EVIDENCE`. Data loss, silent reset, mixed-schema
interpretation, non-idempotent corruption, or an unrecoverable migration is
`INVALID_EVIDENCE`. Startup success, package compatibility, or installation
integrity alone does not prove persistent-state continuity. Chapter 03 owns
the gameplay state model and versioned data contract; Chapter 13 owns the
release admission and recovery evidence for changing that state in production.

UE 5.8 documentation gives dated implementation examples without requiring a
particular API: `USaveGame` defines project-specific durable state, while
`ULocalPlayerSaveGame` exposes game-specific latest/saved data versions and
post-load, pre-save, reset, and save-result hooks. UE's asset/package
versioning guidance separately distinguishes Engine Version, Serialization
Version, and Build ID, and warns that newer serialized data is not safely
opened and resaved by older versions. Treat these as evidence for explicit
compatibility and migration decisions, not as a universal save format or
automatic migration guarantee.

#### Can players keep progress made after an update?

In this constructed example, a player updates at the harbor checkpoint, then
reaches the lighthouse and collects its reward. The team needs the option to
restore the previous game build while preserving play since the update.

- If the previous build supports the updated save, try the rollback with a
  copy of the **lighthouse** slot. Resume, confirm the checkpoint, and revisit
  the reward to check that it stays collected. This exercises both the reader
  and the gameplay meaning of the saved fields.
- If the update writes a format the previous build cannot read, keep the
  lighthouse copy intact. Restoring the pre-update backup would return the
  player to the harbor. A fix in the current build can preserve later progress.
  If the team proposes a reverse conversion, test it on a copy against the
  same checkpoint and reward before relying on it.

The two recovery paths have different costs. Reverting the executable may
restore service quickly. Reverting the slot also gives up everything earned
after that backup. Report the last progress the tested path can recover.

**Proposed UE 5.9 Preview web test.** Epic lists a Preview 1 issue affecting Launcher-built C++ web games where a browser reload can lose saves or settings (UE-412003). For a web delivery, host the candidate, reach the lighthouse on a test slot, collect the reward and save. Reload at the same origin in the same browser profile. Check the resumed checkpoint and whether the reward can be collected again. Record the build, browser and observed result. A reset blocks a continuity claim for that combination. [Epic's Preview 1 issues](https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840/3)

## Version and feature release contract

Make engine and feature identity part of the production artifact contract. For every release-relevant engine, plugin, renderer, replication system, procedural system, or capture feature, record:

- engine version, branch or build, plugin versions, project configuration, target platforms, runtime architecture, authoring/build-host architecture, compiler and toolchain, SDK/GDK, and plugin or middleware ABI;
- upstream maturity (`Experimental`, `Beta`, or `Production Ready`) and the date of the assessment;
- hardware or platform prerequisites, known limitations, and affected content or systems;
- baseline evidence, fallback behavior, migration cost, owner, and rollback target.

Keep one current version matrix with the release evidence rather than scattering unqualified feature claims through the handbook. A feature can be production-ready upstream and still fail a project's visual, performance, packaging, licensing, or recovery gates. When a version change or maturity change affects a contract, reopen the relevant validation gate and preserve the previous accepted baseline for comparison.

### UE 5.9 MegaJam Preview

**Retained UE 5.8 observations.** In the [meadow case](../../analyze-unreal-development-cases/references/16-case-studies.md#case-recovering-a-meadow-through-source-capability-and-coupled-ground-cover), the saved level reopened and a short local PIE walk completed. In the [5.8.3 PCG fixture](../../analyze-unreal-development-cases/references/16-case-studies.md#case-an-inspectable-pcg-learning-fixture-is-not-a-production-starter), generated transforms matched across two generations and a saved level reopen. The first case tested a player route. The second tested an authoring relationship. Neither tested a shipped build.

**Epic's Preview evidence, reviewed 2026-11-14.** Epic released the MegaJam Preview on November 9 with a shorter QA period and recommends testing project copies. Keep the accepted 5.8 project and its records available. Select Preview checks for the decisions the project faces. [Epic announcement](https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840) · [Korean review](ue-5-9-preview.ko.md)

**Open project checks.** If a visual decision depends on a processed viewport, inspect the [original game frame](10-rendering.md#evidence-strategy). A lighting-path change calls for a [same-build cache comparison](11-performance-scalability.md#comparing-lumen-world-cache-in-ue-59-preview). A web target adds the [browser reload check](#can-players-keep-progress-made-after-an-update). For terrain and vegetation, revisit the [representation decision](../../design-unreal-worlds-and-levels/references/04-world-level-design.md#terrain-representation-review-before-broad-terrain-mutation) and [PCG visibility and paint behavior](../../design-unreal-automation-and-pcg/references/09-procedural-systems-pcg.md#version-sensitive-rendering-and-culling-decisions) where the changed behavior matters.

**Observed on one Preview build.** The [Blueprint graph check](../../design-unreal-blueprint-and-cpp/references/06-blueprint.md#scripted-graph-edits-in-ue-59-preview) passed on Windows, UE 5.9.0 CL 60351404, using direct Python in a disposable project. A new Editor process reopened and compiled the edited copy. Testing through MCP remains a separate open check.

### Architecture-specific target note — UE 5.8, 2026-08-05

Epic's Windows ARM64 documentation for Unreal Engine 5.8 labels the support
Experimental. It describes ARM64, ARM64EC, and combined game-target options,
while the Editor is not supported for that target; it also calls out an April
2026 GDK requirement and lack of Clang support. Treat those statements as a
dated release contract, not a general Windows rule. Record the packaged
runtime architecture separately from the authoring/build host, then validate
compiler/toolchain, SDK/GDK, plugin and middleware ABI, cook/package, startup,
runtime performance, and recovery for the exact project target. A host that
can author or build the project is not evidence that the packaged target can
run it, and a combined target is not evidence that every dependency supports
both architectures.

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

For a level, the expensive work begins only after the experience prototype, playable blockout, and representative visual feasibility slice have retired the dominant design and production risks. The Concept-to-Asset Readiness Contract must separately pass `ASSET_PLAN_READY` before the Experience Prototype, `VISUAL_SLICE_READY` for the exact staged candidates used by the representative slice, and `PRODUCTION_DRESSING_READY` for the exact zones and production-approved asset versions before broad meshing or dressing. This does not prohibit early asset experiments; it limits broad, difficult-to-reverse placement until the experience, visual patterns, family coverage, license, dependencies, integration cost, and recovery plan are known to scale.

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
- Runtime architecture, authoring/build-host architecture, compiler/toolchain, SDK/GDK, plugin or middleware ABI, and architecture-specific fallback are recorded separately.
- Audience, license or distribution scope, and source date are recorded when different official materials assign different maturity labels.
- Clean-environment installation and startup.
- Representative runtime, performance, persistence, and recovery checks.
- Engine or feature changes include cold/warm, capture, packaging, and rollback evidence where relevant.
- Derived outputs have parent-input fingerprints, producer scope, expected/actual coverage, lifetime and lineage, consumer-admission state, fallback, and rebuild or rollback evidence; cache, descriptor, transport, or builder success alone is not sufficient.
- Promotion-relevant test results are bound to the exact source snapshot, build recipe and artifact consumed; clean versus incremental or presubmit scope is explicit, and an unknown link is `PENDING_EVIDENCE` or `INVALID_EVIDENCE`.
- Release or update evidence separates authorization, manifest/base identity, package integrity, destination transition, content resolution, runtime readiness, and rollback; verification coverage and method are explicit, and encryption, transport, size/version checks, or mount success alone do not prove the full chain.
- Patch/update validation retains the accepted base and verifies interruption, stale or wrong-base input, partial/corrupt content, dependency or prerequisite failure, replacement, and rollback without leaving mixed or unknown destination state.
- Persistent-state claims record prior-state identity, supported versions, migration or fixup, post-migration invariants, retained original/backup, and rollback/fallback evidence; startup or package compatibility alone is insufficient.
- Traceable artifact, approval, rollback, and retention policy.

## Common mistakes

- Treating `Production Ready` as a substitute for project-level acceptance.
- Updating the engine or a render/capture path without preserving a comparable baseline and a rollback target.
- Recording a feature name without its engine version, maturity, target platform, fallback, or evidence date.
- Treating Windows ARM64/ARM64EC support in the UE 5.8 dated note as proof of Editor support or dependency compatibility, or collapsing runtime architecture and build-host architecture into one target label.
- Copying an upstream maturity label without recording its audience, license or distribution scope, and compatibility constraints.
- Treating an install, mount, startup, or package-compatibility pass as proof that existing user or session state remains valid after an update.
- Rewriting or resetting old persistent data before the migrated state has passed its invariants and recovery checks.

## Research basis and further reading

- [Epic Games: State of Unreal 2026](https://www.unrealengine.com/news/state-of-unreal-2026-top-news-from-the-show) — UE 5.8 feature maturity, shader compilation, shader deduplication, and PSO pre-caching context.
- [Epic Games: Unreal Engine 5.8 Release Notes](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?application_version=5.8) — version-specific release and production-status details.
- [Epic Games: Transitioning to Movie Render Graph from Movie Render Queue](https://dev.epicgames.com/documentation/en-us/unreal-engine/transitioning-to-the-movie-render-graph-from-movie-render-queue-in-unreal-engine) — migration considerations for the capture pipeline.
- [Epic Games: Windows ARM64 Support in Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/windows-arm64-support-in-unreal-engine-5-8?application_version=5.8) — dated ARM64/ARM64EC game-target maturity, Editor, GDK, compiler, and architecture-boundary constraints.
- [Epic Games: World Partition Builder Commandlet Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-builder-commandlet-reference?application_version=5.8) — UE 5.8 HLOD, PCG, navigation, and RVT generated-output boundaries; use as version-specific evidence, not a procedure to copy into this chapter.
- [Epic Games: World Partition HLOD](https://dev.epicgames.com/documentation/unreal-engine/world-partition---hierarchical-level-of-detail-in-unreal-engine) — source-change conditions for rebuilding HLOD output.
- [Epic Games: Cooked Data Snapshots with Zen Storage Server](https://dev.epicgames.com/documentation/en-us/unreal-engine/cooked-data-snapshots-with-zen-storage-server-for-unreal-engine) — snapshot descriptors, base lineage, storage identity, and destination-equivalence expectations.
- [Epic Games: Generating a State Object Database for Advanced Shader Delivery](https://dev.epicgames.com/documentation/en-us/unreal-engine/generating-a-state-object-database-for-advanced-shader-delivery?application_version=5.8) — UE 5.8 cooked-build inputs, SODB/PSDB consumer identity, coverage, and runtime fallback.
- [Epic Games: 5.8.4 Hotfix Released](https://forums.unrealengine.com/t/5-8-4-hotfix-released/2842775) — dated UE 5.8.4 ASD additions for SODB generation and local testing workflow.
- [Epic Games: Horde Automation Hub for Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-automation-hub-for-unreal-engine?application_version=5.8) — dated test metadata, changelist linkage, CI job-step investigation, and historical comparison.
- [Epic Games: Horde Build Automation for Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-build-automation-for-unreal-engine?application_version=5.8) — source-control workspace sync plus intermediate and final artifact tracking/transfer.
- [Epic Games: Horde Build Automation Tutorial for Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/horde-build-automation-tutorial-for-unreal-engine?application_version=5.8) — dated distinction between incremental, pristine packaged, and shelved-changelist presubmit jobs.
- [Epic Games: Review Test Results in Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/review-test-results-in-unreal-engine?application_version=5.8) — report fields and device/test evidence; a report remains separate from source/artifact admission.
- [Epic Games: Versioning of Assets and Packages in Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/versioning-of-assets-and-packages-in-unreal-engine?application_version=5.8) — engine changelist, branch, `BuildId`, compatible-changelist, and promoted-build identity.
- [Epic Games: FBuildVersion API in Unreal Engine 5.8](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Core/FBuildVersion?application_version=5.8) — build metadata fields including optional build URL, changelist, compatibility, and promoted-build state.

- [Epic Games: How To Create a Patch (Platform-Agnostic)](https://dev.epicgames.com/documentation/en-us/unreal-engine/how-to-create-a-patch-in-unreal-engine?lang=en-US) — retained released cooked base, serialization-path stability, patch comparison, and mount priority.
- [Epic Games: Updating Unreal Engine Projects With Patches After Release](https://dev.epicgames.com/documentation/en-us/unreal-engine/updating-unreal-engine-projects-with-patches-after-release) — patch identity and platform-specific distribution boundary.
- [Epic Games: Project Section of the Unreal Engine Project Settings](https://dev.epicgames.com/documentation/en-us/unreal-engine/project-section-of-the-unreal-engine-project-settings) — separate pak encryption and signing settings; use as version-scoped evidence, not a key-management procedure.
- [Epic Games: FPakPlatformFile::GetPakSignatureFile](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/PakFile/FPakPlatformFile/GetPakSignatureFile) — missing or invalid pak signature handling.
- [Epic Games: FChunkDownloader](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Plugins/ChunkDownloader/FChunkDownloader) — dated manifest, cache-version validation, download, and mount lifecycle evidence.
- [Epic Games: BuildPatchServices::EVerifyMode](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/BuildPatchServices/BuildPatchServices__EVerifyMode?application_version=5.8) — UE 5.8 full-versus-touched and SHA-versus-file-size verification scope.
- [Epic Games: BuildPatchServices::EVerifyError](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/BuildPatchServices/BuildPatchServices__EVerifyError?application_version=5.8) — missing, open, hash, and file-size verification failure classes.
- [Epic Games: Saving and Loading Your Game](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine) — project-defined SaveGame state, slots, loading, and platform-dependent persistence.
- [Epic Games: ULocalPlayerSaveGame](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/ULocalPlayerSaveGame?application_version=5.8) — UE 5.8 game-specific data versions and lifecycle hooks for local-player save state.
- [Epic Games: Updating Projects to Newer Versions of Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/updating-projects-to-newer-versions-of-unreal-engine?lang=en-US) — copy-first project conversion and the risk of irreversible data loss; this is separate from user-save migration.

Additional current context:

- [Epic Games: Introduction to Iris](https://dev.epicgames.com/documentation/unreal-engine/introduction-to-iris-in-unreal-engine) — public opt-in and feature-status context for Iris; confirm the wording against the target engine and distribution.
- [Epic Games: Migrate to Iris](https://dev.epicgames.com/documentation/en-us/unreal-engine/migrate-to-iris-in-unreal-engine) — migration scope and compatibility considerations that belong in the project release contract.

## Related topics

Content & Asset Architecture; Gameplay Architecture; Automation & Python; Rendering; Performance & Scalability; Validation, Testing & Debugging; Team Collaboration & Source Control.
