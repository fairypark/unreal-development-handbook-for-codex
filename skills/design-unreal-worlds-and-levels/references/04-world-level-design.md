# 04 — World & Level Design

## Purpose

Design playable spaces whose spatial composition, traversal, terrain, content, atmosphere, and production constraints support one coherent player experience.

## Intent

Build a place that works from movement and multiple viewpoints, not a hero-camera diorama. Turn subjective direction into observable spatial and visual targets before layout.

## Fun model and experience density

Level design is the design of a player's journey through space, not only the construction of a map. A level may be readable, beautiful, and technically correct yet still feel empty if it does not create meaningful questions, choices, actions, consequences, and rewards. Define the experience hypothesis before committing to broad spatial or asset production.

### Fun thesis

Record a short, testable statement for the level or route:

- **Core pleasure:** what the player should enjoy doing repeatedly;
- **Repeated verbs:** the actions the space should invite, vary, and escalate;
- **Player questions:** what the player wonders, pursues, or may intentionally defer;
- **Agency, risk, and recovery:** what choices matter, what can be lost, and how the player can recover;
- **Reward and next hook:** what pays off attention or effort and what creates the next decision;
- **Emotional rhythm:** where curiosity, challenge, tension, release, rest, and escalation should occur;
- **Failure hypothesis:** where boredom, confusion, repetition, or arbitrary obstruction is most likely;
- **Proof:** the smallest playable unit that could disprove the thesis.

The thesis is genre- and project-specific. Open-world exploration may emphasize curiosity, voluntary discovery, and layered rewards; a combat arena, stealth space, puzzle room, or narrative scene may require a different source of pleasure. Do not use visual spectacle, traversal completion, or difficulty as a substitute for evidence that the intended fun exists.

### POI ecology

A **point of interest (POI)** is a meaningful destination, event, interaction, or discovery that gives the player a reason to look, approach, choose, act, or return. A landmark helps the player orient; a POI creates curiosity or purpose. One object can be both, but they are not interchangeable.

Use a hierarchy to manage commitment and pacing rather than to force every space into the same density:

| POI scale | Design role | Typical evidence |
| --- | --- | --- |
| Large | Long-term orientation, destination, story or progression goal, or a cluster of smaller experiences. | The player can recognize its promise, understand a broad purpose, and form a route or return decision. |
| Medium | Mid-term objective, encounter, sub-area, story beat, or meaningful exploration branch. | The approach creates anticipation and the arrival produces an interaction, choice, or consequence. |
| Small | Short discovery, environmental clue, resource, micro-encounter, optional interaction, or local reward. | The player receives a legible payoff without requiring a disproportionate detour. |

For each important POI, record its scale, player question, approach and reveal, interaction or verb, risk, reward or outcome, next hook, expected time or distance, dependencies, and production cost. This makes density a content-and-experience decision rather than a count of props placed on a map.

### Experience density and the 40-second heuristic

Measure density as the time to the next **meaningful change**, not as the number of objects or a fixed distance. A meaningful change may be a visual reveal, interaction, choice, encounter, reward, narrative clue, new traversal affordance, or player-led discovery. Calibrate the interval against movement speed, camera, vehicle or mount use, fast travel, route visibility, player mastery, and genre.

The often-cited 40-second rule is a useful starting hypothesis for some open-world exploration routes, not a universal law. Do not fill the world mechanically every 40 seconds or convert the number into a mandatory physical radius. Deliberate quiet can provide scale, recovery, contrast, anticipation, or a chance to choose a direction; it needs an intentional role and should not become unobserved empty travel.

### Refusal and reward

Curiosity often grows when a POI is promised, partially withheld, and then paid off:

`promise or reveal → refusal or occlusion → partial re-reveal → approach choice → arrival and payoff`

Use terrain, structures, S-curves, elevation, gates, distance, sound, lighting, and player-controlled detours to control what is known and when. Refusal should create anticipation or a meaningful choice, not arbitrary obstruction. Test whether the player understands enough to remain curious, whether the route permits a chosen deferral or return when intended, and whether the eventual interaction or reward justifies the approach.

### Emotional rhythm and POI-unit proof

Annotate the route as a sequence of beats rather than only as geometry: curiosity, orientation, approach, challenge, tension, release, reward, and the next hook. Large, medium, and small POIs can support different beats, but their role must follow the project's fun thesis rather than a rigid template.

The cheapest credible playtest unit is usually not a whole world or a hero screenshot. It is a POI experience unit containing the approach, reveal or refusal, player choice or repeated verb, interaction or encounter, outcome or reward, and exit or next hook. Test this unit with boxes and placeholder behavior before spending on final assets. Then test several units in sequence to verify rhythm, optionality, and the absence of repetitive or unintentional empty travel.

## When to use

Use this workflow when a level, mission space, environment, or terrain change is expected to become production content. When an AI agent performs the work, the workflow record and stage order are mandatory even for a small level. A disposable experiment may combine adjacent gates in one reversible pass only when that choice is declared before mutation and every gate's question and evidence remains visible; combined is not skipped. For a level whose failure would strand significant art, audio, or technical work, keep the pauses explicit and evidence-based.

## When NOT to use

Do not interpret the sequence as a rigid one-pass waterfall or a fixed number of passes, and do not replace it with a tool-first sequence or retrospective checklist. Audio-first, vehicle, multiplayer, VR, systemic, and highly procedural experiences may need their defining risks in the first playable prototype. The rule is to move the expensive or experience-defining uncertainty earlier; for AI work, this flexibility changes how stages are combined, not the obligation to record and evaluate each stage.

## Decision-ready brief

Record the fun thesis, core verbs, intended emotional rhythm, POI hierarchy, experience-density hypothesis, and curiosity/reward pattern alongside player fantasy, setting, scale, biome, era, weather, time, route length, target platform, performance budget, expansion directions, and construction provenance. Define the arrival, reverse, lateral, waterway/axis, elevation, route, and contact relationships that must be inspected, then assign the smallest set of fixed overview cameras that covers those relationships and the project's specific spatial risks; one hero overview is not a coverage plan. For each important view, identify focal anchors, depth layers, value hierarchy, horizon intent, spatial relationships, and prohibited failure imagery.

Record the actual height above local ground and FOV of the project's player tracking camera in the initial brief, and identify the intended runtime camera rig and configuration source when known. The height/FOV record supports a comparable static player-height proxy during early prototyping; it does not claim that boom length, socket or shoulder offset, pitch, SpringArm collision or retraction, or other runtime behavior has been matched. Exact rig authority begins at Stage 5 Playable Blockout. Do not substitute a convenient editor or overview camera for evidence reserved to the player camera.

## Exploration and production modes

Keep two related loops distinct:

- **Exploration:** use disposable primitives, temporary materials, and placeholder cues to discover whether the space is fun, readable, and in scope. For an **outdoor map level-design prototype**, make a minimal **Landscape terrain** the actual playable floor by default, even when buildings, cover, route furniture, and other masses remain primitive. Do not replace it with a flat cube or plane merely to move faster: the early prototype must expose elevation, slopes, drainage, terrain transitions, grounding, and terrain contacts. Use another floor only when a specific user or stakeholder request explicitly overrides this default. Diverge from the plan when playtest evidence disproves an assumption.
- **Production:** use explicit review gates, approved asset and material rules, owned dependencies, representative performance conditions, and retained evidence to scale a pattern that has already been proved.

The transition is not triggered by an attractive screenshot or personal confidence. Promote only when a representative slice demonstrates that the intended experience, visual language, asset families, production method, and technical budget can work together. A short segment can be production-ready while the rest of the level remains exploratory.

## Readiness for a production workflow

Treat consistent visual output as a measurable readiness threshold. Before adopting a heavier studio-style workflow, demonstrate that:

- the visual target reproduces across at least two representative contexts or viewpoints, including an ordinary area rather than only a hero shot;
- the approved asset, material, lighting, collision, and audio rules are documented and can be applied without ad hoc exceptions;
- the time, ownership, dependencies, and performance cost of a representative content unit are understood;
- the same playtest, visual capture, performance, and recovery checks can be repeated with comparable results;
- review, source-control, evidence retention, and rollback are practical for the current project scale.

Then analyze real production workflows for the control points they solve—briefing, ownership, review, asset readiness, integration, budgets, and recovery—and adapt those principles to the project. Copying a studio's vocabulary or pass order without matching its risks, team structure, or toolchain creates ceremony rather than production reliability.

## Concept-to-production workflow

The following sequence turns the proposed pauses into scoped decisions. A gate freezes only the assumptions it names; later evidence may reopen an earlier gate when those assumptions change.

### Mandatory AI execution contract

When an AI agent creates or materially changes a level, world, environment, terrain, route, POI, or map-wide dressing, it **MUST** execute the stages below as an ordered sequence of evidence gates. This is an execution contract, not a retrospective checklist. Tool success, a rendered screenshot, or agent confidence never authorizes the next stage by itself.

Before the first mutation, the agent must create or update an inspectable workflow record containing:

- the work class (`DISPOSABLE_EXPERIMENT` or `PRODUCTION_INTENDED`) and scope;
- the current stage, the approved predecessor artifact or baseline, and the stage objective;
- required artifacts, evidence conditions, hard failures, owner or approver, and rollback target;
- allowed mutations and the exact version or change set that the next gate will review;
- for level composition work, the Stage 2a translation-contract identifier and version, its broad-placement lock state, the conditional dependent-strata strategy decision when source and dependent layers are in scope, and the source, plan, prototype, camera, and deviation-record versions currently in force.

The agent must start at Stage 1, or resume at a later stage only when an existing artifact and approval record prove that every predecessor gate passed. Existing level content without stage evidence is not proof of completion and must be audited or reconstructed before further promotion.

At every stage, the agent must:

1. state the stage it is executing and the decision it is trying to prove;
2. perform only the mutations needed for that stage;
3. verify the stage's required evidence under the stated test conditions;
4. record `PASS`, `FAIL`, `PENDING_EVIDENCE`, or `INVALID_EVIDENCE`;
5. advance only on `PASS` and an explicit promotion decision; otherwise stop, revise the responsible earlier stage, or request the missing approval or evidence;
6. preserve the baseline, failed attempts, generated outputs, and factual change scope so the gate can be reopened or rolled back.

The numbered stages are always represented in the record. A small or disposable level may combine adjacent stages in one reversible pass, but it may not silently skip a stage or promote downstream work while one of its questions is unanswered. When a later change invalidates an accepted assumption, reopen the affected stage, preserve the previously accepted version, and re-run the dependent evidence. At the feedback pauses named below, absence of the required user or designated-approver response remains `PENDING_EVIDENCE`; it is not permission to continue.

| Order | Required handoff before promotion |
| --- | --- |
| 1. Concept and intent review | Decision-ready brief, non-goals, constraints, unresolved questions, and recorded intent feedback. |
| 2. Area Composition Plan review | A versioned, recorded area plan with zone boundaries and stable IDs, terrain elevations and steps, primary circulation, rivers and bridges, building footprints and typology hierarchy, and a risk-covering set of fixed `DIAGNOSTIC_ONLY` overview cameras with stable IDs. The set covers required arrival, reverse, lateral, waterway/axis, elevation, and project-specific relationships without imposing a universal count. It also records the player-camera height/FOV proxy and planned runtime-rig source. No prototype geometry or broad asset placement is authorized before this gate passes. |
| 2a. Reference-to-Prototype Translation Gate | A machine-readable source registry and authority order, zone-level quantitative composition contracts, a planned traceability map for every prototype array/proxy group/route/terrain or water change, camera-specific comparison rules, tolerance and hard-failure rules, and an explicit broad-placement decision. Stage 2 `PASS` alone never authorizes prototype placement. |
| 3. Experience prototype | Runtime evidence for one POI or encounter unit, including approach, player question, choice or verb, payoff, next hook, and the live zone marker that identifies its area. |
| 4. Terrain and macro blockout | The fixed overview set proves whole-area composition, terrain relief, axes, water/bridge relationships, and risk coverage; auxiliary static player-height/FOV views reject gross scale, width, slope, and occlusion failures without claiming exact runtime-rig or fine-composition authority. |
| 4a. Route authority and corridor contract | Inspectable route source of truth, ownership, surface provider, clearance, grade, and corridor validation. |
| 5. Playable blockout and feedback gate | Playtest evidence from the representative player controller and actual runtime camera rig for traversal, authoritative camera behavior, scale, readability, pacing, collision, boundaries, POI flow, and recovery. |
| 6. Visual feasibility slice | Representative visual and experience evidence captured through the actual runtime camera rig, with asset density, composition, material, lighting, collision, streaming, and budget evidence. |
| 7. Production meshing and dressing | Approved asset-family substitutions, preserved spatial contracts, chunk evidence, deviation records, and a complete zone-marker inventory proving every production area remained identifiable through final placement. |
| 8. Layered lighting and audio integration | Functional and final integration evidence for navigation, mood, interaction feedback, and propagation or occlusion risks. |
| 9. Collision, polish, and release validation | Final runtime, collision, performance, streaming, persistence, packaging, accessibility, and recovery evidence. |

### 1. Concept and intent review

Treat concept art as a direction hypothesis and an intent contract, not as a complete 3D blueprint. Translate it into a brief containing:

- player fantasy, emotional arc, setting, time, weather, and cultural or biome signals;
- the fun thesis, repeated player verbs, intended emotional rhythm, and the evidence that would disprove them;
- focal hierarchy, silhouette language, palette, material response, depth layers, and the views that must work;
- what the player must notice, what may remain ambiguous, and which visual readings are prohibited;
- rough scale cues, asset or technology constraints, construction provenance, and unresolved questions.

Pause for user or stakeholder feedback here. The review question is not merely “is the image beautiful?” but “does this written interpretation preserve the intended experience, priorities, and limits?” Record corrections before layout work begins.

### 2. Area Composition Plan review

Between the concept view and the first cube prototype, create a versioned **Area Composition Plan** as a floor plan, node map, annotated top-down diagram, and side or elevation profile as appropriate. Record its artifact path or identifier, version, status, reviewer, and source concept in the workflow record. The plan must make these contracts inspectable before decorating or building:

- zone boundaries, stable IDs, anchors or bounds, roles, and semantic colors;
- terrain height bands, absolute or relative elevations, terraces, slopes, steps, drainage, and other vertical transitions;
- arrival, primary circulation, optional loops, objectives, player verbs, encounter or rest roles;
- rivers, creeks, water boundaries, bridge locations, crossing roles, banks, and approach transitions;
- landmarks, reveals, sightlines, occlusion, readable openings, gates, and recovery paths;
- POI hierarchy, player questions, approach/reveal/payoff beats, optional deferral or return, and the experience-density hypothesis;
- building footprints, entrances, orientation, negative space, courtyard or street relationships, and a named typology hierarchy from primary landmark to supporting structures;
- a source-artifact inventory covering the concept images, top-down plans, side or elevation views, and composition references that govern the plan, with stable IDs, versions, approval states, authority scopes, priority, and any unresolved conflict;
- a fixed overview-camera set whose members have stable IDs, roles, `DIAGNOSTIC_ONLY` authority, and a coverage matrix for arrival, reverse, lateral, waterway/axis, elevation, and project-specific spatial risks; use the smallest set that closes the identified blind spots rather than one hero overview or an arbitrary fixed count;
- auxiliary fixed player-height cameras bound to the recorded height above local ground and FOV for gross scale, route-width, slope, and occlusion checks, plus the intended runtime camera rig and its Stage 5 configuration source when known;
- foundations, boundaries, streaming cells, and expansion directions;
- approximate scale, route timing, content cost hotspots, and the assumptions that the blockout must test.

Pause again for feedback. The plan should be understandable to someone who did not author it, and it should make the whole-space role allocation visible before construction cost rises. If the role or placement of a major area is unclear in two dimensions, more detail in three dimensions will usually hide rather than solve the problem. Treat a missing, unrecorded, or `PENDING_EVIDENCE` plan as a mutation lock: do not create the first cube or graybox volume and do not start broad final-asset placement. A plan `PASS` releases work only to Stage 2a; it does not release content-bearing prototype geometry. This gate may be lightweight for a disposable experiment, but it may not be reconstructed retrospectively from geometry that already exists.

For a typology-critical precinct, state the required reading as a sequence, hierarchy, negative-space pattern, and prohibited silhouette. Building envelopes that merely match approximate size do not pass. For a palace, require the legible gate -> outer court -> middle gate -> central courtyard -> main hall axis, with the courts and supporting halls reinforcing the ceremonial hierarchy. If the composition reads as a fortress or castle because of a dominant keep, tower-like blocks, a monolithic plinth, or continuous high defensive walls, record a hard failure and return to the Area Composition Plan before adding detail.

### Persistent zone identification contract

Define the zone registry in the Area Composition Plan, before prototyping begins. Give every major area a stable machine-readable ID, numeric review ID, reviewer-facing name, ASCII fallback, gameplay or production role, bounds or anchor, semantic color, and marker owner. The IDs must survive proxy replacement, asset renaming, streaming changes, and production chunking.

Create the live zone markers before the first prototype geometry mutation. Use obvious editor/debug-only labels, billboards, text, TargetPoints, volumes, or a dedicated debug Data Layer that cannot be mistaken for production geometry. Store them in a dedicated folder or layer, tag them consistently, and exclude them from shipping visuals and performance evidence unless the project explicitly needs runtime wayfinding. Format every visible marker with the numeric ID plus the ASCII fallback, for example `03 PALACE PRECINCT`; a localized name may be added but never replaces the fallback. Empty glyphs, clipped labels, or locale-dependent text without the numeric ASCII form fail the marker gate.

Keep every marker visible and inspectable throughout experience prototyping, terrain and macro blockout, playable blockout, the visual feasibility slice, and all production meshing and dressing. Proxy replacement or asset-placement batches must not delete, hide, rename, or move the markers. Overview or arrival evidence must identify all zones; zone-local evidence must show the active zone name, and scale-sensitive building evidence should also include an agreed player-scale reference.

Do not retire zone markers merely because production assets make the areas look recognizable. They may be removed or disabled only after Stage 7 asset placement is complete, the zone inventory matches the approved plan, every zone has placement and reverse-view evidence, and an explicit cleanup decision is recorded. Default to retaining inexpensive editor-only markers through final release validation when their presence does not interfere with evidence.

### Staged camera-evidence contract

Record every fixed validation camera in the Area Composition Plan and keep its stable ID, role, evidence class, transform source, height above local ground, FOV, and covered spatial relationships inspectable. Camera evidence has three distinct authority levels:

- **Overview diagnostic set, Stages 2–4:** use multiple fixed overview or bird's-eye cameras as the primary evidence for whole-area composition, terrain high/low structure, axes, circulation, water crossings and bridge approaches, footprint overlap, and marker coverage. The minimum set is risk-based: it must cover arrival, reverse, lateral, waterway/axis, elevation, and any project-specific relationship that another view leaves ambiguous. One camera may cover several roles when the coverage matrix proves it; a single hero overview fails whenever it leaves a required relationship untested. Label every overview `DIAGNOSTIC_ONLY`.
- **Static player-height proxy, Stages 2–4:** bind auxiliary fixed views to the brief's player tracking-camera height above local ground and FOV; where terrain height changes, preserve the same local-ground relationship rather than a convenient world Z. Use these views to reject grossly implausible building scale, route width, slope presentation, or occlusion. They are minimum plausibility checks, not an exact simulation of a runtime rig, and they do not authorize detailed player-view composition, final readability, final scale, or typology approval.
- **Actual runtime camera rig, Stage 5 onward:** at Playable Blockout, use the representative player controller and the real runtime camera rig—for example, `BP_ThirdPersonCharacter` and its `FollowCamera`/SpringArm chain—as the authority for player-camera evidence. Record the rig asset or class, configuration version, boom length, socket or shoulder offset, pitch behavior, SpringArm collision and retraction, and other project-relevant behavior. From the Visual Feasibility Slice onward, judge player readability, asset density, and visual composition through this rig under representative movement and camera states. A fixed player-height proxy may support comparison but cannot substitute for runtime capture.

Overview evidence can find a macro problem and is the principal way to review prototype-wide spatial relationships, but it can never prove what the player sees or understands. `DIAGNOSTIC_ONLY` does not make the overview set non-gating: it may pass or fail the Stage 2–4 macro relationships assigned to it, while remaining unauthorized for player-camera claims. At every stage, exclude overview cameras from player-visibility, landmark-readability, scale, or typology approval; promotion of those questions requires the stage-authorized player-camera evidence. During Stages 2–4, do not spend prototype effort precisely composing scenery or detail to a player proxy whose runtime offsets, pitch, collision, and retraction have not yet been validated.

### 2a. Reference-to-Prototype Translation Gate (blocking)

An approved Area Composition Plan describes intent, but it does not by itself define what a builder must place. Before the first content-bearing prototype mutation, translate the approved references and plan into an inspectable **Reference-to-Prototype Translation Contract**. Use the bundled [JSON Schema](reference-to-prototype-translation.schema.json) and [template](reference-to-prototype-translation.template.json), or a project-owned equivalent that preserves the same fields, identifiers, gate semantics, and validation rules. The contract has two lifecycle phases: `PRE_PLACEMENT`, which authorizes or blocks broad placement, and `POST_MUTATION_AUDIT`, which compares the realized prototype with the same approved contract after a composition-changing batch.

#### Source registry and authority

Inventory every concept image, annotated plan, floor plan, side or elevation view, composition reference, and written direction used to control the prototype. Each source record must include a stable ID, artifact path or external identifier, media type, version, approval state, approving authority, authority scopes and applicable zone IDs, priority within each scope and zone, and the exact crop, page, layer, or annotation used. Authority scopes should distinguish at least footprint and density, circulation, elevation, water and bridges, typology and hierarchy, silhouette, and atmosphere or shade when relevant.

Do not silently average contradictory sources. Record the conflict, the controlling source and scope, the overridden source, the decision owner, and the resolution. Only approved sources may control a placement decision. An unapproved source may remain as context, but its non-authoritative status must be explicit. If the controlling source, version, crop, approval, or priority changes, mark the translation evidence stale and reopen Stage 2 or Stage 2a before continuing.

#### Zone-level quantitative composition contract

For every stable zone ID, extract bounded targets from the controlling sources and state the measurement basis, estimate confidence, and allowed deviation. Use ranges where an image supports only an estimate; do not invent false precision. Every zone contract must cover:

- built-footprint occupancy relative to a declared denominator such as buildable zone area;
- building-mass and roof-mass count ranges, including the rule for what constitutes one mass;
- typology composition and primary/supporting hierarchy, expressed as count or share ranges;
- street or courtyard frontage continuity, building-gap ranges or distributions, and intentional breaks;
- primary-route, secondary-route, and alley widths, corridor continuity, junctions, and reserved clearances;
- relative or absolute height bands, terraces, steps, grade transitions, and skyline order;
- water bodies, banks, crossings, bridge count or role, approach geometry, and continuity, or an explicit `NOT_APPLICABLE` reason;
- important shaded or enclosed spaces that must remain spatially legible, intentional open or empty spaces that must remain unbuilt, and the relationship each serves;
- required focal hierarchy, reveal or occlusion relationships, negative-space patterns, and prohibited silhouettes.

Aggregate Actor count is only a supporting diagnostic. It cannot pass this gate when zone distribution, footprint, frontage, gaps, preserved shade or voids, hierarchy, route continuity, or a prohibited silhouette fails. Counts that fall within range also fail when they are concentrated in the wrong zone or arranged with the wrong spatial rhythm.

#### Prototype traceability map

Create a planned trace entry before mutation for every prototype array, repeated placement set, architecture proxy group, route or alley, water or bridge proxy, reserved void or shade volume, and Landscape height or surface change. Each entry needs a stable prototype element ID, element kind, owning zone IDs, implemented source-requirement IDs, planned bounds or anchor, implementation rule, owner, lifecycle state, and later the realized Actor, spline, Landscape layer, component, folder, Data Layer, or generated-member inventory. A grouped trace entry may cover a deterministic array only when its member count, ordering or keys, bounds, and generation version are inspectable; an opaque folder label is not traceability.

The traceability map connects the source artifact to a normalized requirement, the requirement to the Area Composition Plan feature, and the plan feature to the realized prototype element:

`source artifact -> source requirement -> zone/plan feature -> prototype element -> evidence and deviation record`

For outdoor prototypes, keep the minimal Landscape as the playable floor and trace terrain height, terrace, bank, and route-surface changes to their source requirements. A cube-only architecture-proxy policy applies to building and roof masses, not to the ground: it does not authorize replacing the Landscape with a cube plane. Persistent zone markers are evidence infrastructure, not architecture proxies; retain their stable IDs and lifecycle independently and never consume or delete them during array replacement.

#### Conditional dependent-strata strategy gate

When the approved scope includes two spatially dependent strata, such as rocks or hardscape plus grass or ground cover, complete a `Dependent-Strata Strategy Gate` as part of Stage 2a before the first relevant generator, Foliage, or batch-placement mutation. The gate must record `CONSIDERED`, the selected mode (`VIDEO_DISTANCE_EXCLUSION`, `MASK_OTHER`, `DIRECT_AUTHORED`, or `PENDING_EVIDENCE`), the decision reason, source authority, dependency order, units, clearance, transition band, validation method, and status. If the strata are not in scope, record `NOT_APPLICABLE` rather than silently omitting the consideration.

`VIDEO_DISTANCE_EXCLUSION` is appropriate when the source hardscape has a stable final or conservative footprint and the dependent layer should clear or approach it. `MASK_OTHER` is appropriate when a route, Landscape region, volume, or another declared spatial rule is the real authority. `DIRECT_AUTHORED` is appropriate for exploratory, hero-specific, or intentionally hand-composed placement. Use `PENDING_EVIDENCE` when bounds, scale, ownership, units, or platform constraints are unresolved. A missing, unrecorded, or non-passing applicable strategy gate keeps the relevant generator and dependent placement locked, even when the general Stage 2a gate has otherwise passed. Reopen the strategy gate when the source mesh, footprint, transforms, graph, generation mode, terrain, or exclusion rule changes.

#### Placement lock and promotion decision

Before Stage 2a `PASS`, allowed mutations are limited to evidence infrastructure that cannot be mistaken for layout content: fixed cameras, persistent zone markers, measurement aids, empty organizational containers, and reversible test probes that are explicitly excluded from the prototype inventory. Content-bearing prototype placement remains locked.

Set `broad_placement_authorized` to true only when all of the following are true:

- Stage 2 passed against the exact recorded Area Composition Plan version;
- the source registry is complete, controlling authority is approved, and every relevant conflict is resolved;
- every zone has a complete quantitative contract and project-specific tolerance or hard-failure rule;
- all planned arrays, proxy groups, paths, water or bridge features, voids, and terrain changes have trace entries with no orphan requirement or unmapped placement group;
- every applicable dependent-strata strategy has `CONSIDERED`, a selected mode and reason, a declared source authority and dependency order, and a `PASS` status;
- overview and player-camera evidence responsibilities are separated and their fixed comparison conditions are recorded;
- the Stage 2a status is `PASS`, the approver and decision time are recorded, and the rollback target is recoverable.

A missing trace table, a qualitative-only density direction, an unapproved reference, an unresolved source conflict, an empty tolerance record, or a contract/schema error leaves the stage `PENDING_EVIDENCE`, `INVALID_EVIDENCE`, or `FAIL` and keeps broad cube placement blocked. Do not reconstruct a passing contract from a dense prototype after the fact.

#### Same-condition deviation audit and reopening

After every composition-changing prototype batch, update the same contract to `POST_MUTATION_AUDIT` and record the source, plan, translation-contract, prototype, and camera versions. Preserve a reference/plan/prototype comparison rather than replacing the previous capture:

- **Fixed overview comparison:** from each assigned `DIAGNOSTIC_ONLY` camera, compare an identified reference crop or diagram, the aligned plan view, and the prototype capture under the same camera transform, crop, projection, resolution, and measurement basis. Use this evidence only for assigned macro questions such as footprint, zone density and distribution, frontage, gaps, hierarchy, terrain bands, axes, water and bridges, shade and void preservation, and silhouette. When a perspective concept cannot be geometrically aligned, state which qualitative relation it controls rather than claiming pixel equivalence.
- **Actual player-camera comparison:** beginning at Stage 5, capture the representative player controller and runtime rig at stable route samples and states. Compare perceived distance, enclosure, occlusion and reveal, route and alley continuity, landmark hierarchy, clearance, and recovery. Record rig class or asset, configuration version, transform or route sample, boom, offset, pitch, and collision or retraction state. Overview evidence cannot substitute for these claims.

For every measured or binary requirement, record planned value or relation, observed value or verdict, allowed deviation, evidence IDs, result, and reviewer. Reuse the same relevant camera and test conditions for pre-change and post-change evidence. A changed composition remains `PENDING_EVIDENCE` until this audit is complete. Any out-of-tolerance metric, lost shade or intentional void, hierarchy reversal, route discontinuity, or prohibited silhouette is a hard failure even when total Actor count matches.

When the audit fails, set `broad_placement_authorized` to false, preserve the last accepted baseline and failed candidate, and reopen the earliest responsible stage. Reopen Stage 1 or 2 when reference intent or the plan is wrong, Stage 2a when extraction, authority, tolerance, or mapping is wrong, and the relevant prototype stage when implementation drifted from a correct contract. Re-run every dependent camera and zone check before restoring `PASS`; a local repair capture cannot silently promote the whole level.

#### Compatibility and migration

This gate adds evidence; it does not replace the existing Landscape, route-authority, persistent-zone-marker, or staged-camera contracts. A project may serialize the same semantics in JSON, YAML, a Data Asset, a database, or another typed system, but it must retain stable IDs, versions, authority, quantitative ranges, traces, comparison conditions, gate states, and reopening behavior. Record the project format and schema version in the workflow record.

For a legacy prototype that already contains geometry, do not claim that a reconstructed contract predates placement. Freeze further broad placement, preserve the existing prototype as a `LEGACY_UNVERIFIED` candidate outside the accepted baseline, rebuild the source registry and zone contracts from approved artifacts, map the existing proxy groups and terrain or route changes, and run the same-condition deviation audit. Keep the gate `INVALID_EVIDENCE` or `PENDING_EVIDENCE` until the reconstruction and audit are explicitly approved. If controlling sources, plan versions, or comparable cameras cannot be recovered, return to Stage 1 or 2 rather than promoting the legacy geometry by appearance.

### 3. Experience prototype before full blockout

Only after both the recorded Area Composition Plan and Stage 2a translation gate pass, select one representative POI or encounter and build the cheapest playable version of its experience unit: approach, question or reveal, refusal or occlusion, player choice or repeated verb, interaction, outcome or reward, and exit or next hook. Use boxes, semantic materials, temporary effects, and placeholder behavior. Create or verify the persistent zone marker before adding the first prototype geometry, keep it visible in the review evidence, and bind every new proxy group, path, or terrain change to its planned trace entry.

Test the fun thesis, not only the geometry. Observe whether players understand what they are curious about, choose to approach or defer, experience anticipation or tension, receive a worthwhile payoff, and know what to do next. Record time to meaningful change and the role of any intentional quiet section. If the unit is weak, revise the thesis or spatial plan before building the whole route. For a small level, this gate may be combined with the next blockout step, but its evidence and approval question should remain explicit.

Pause for user or designated approver feedback after the unit has runtime evidence. A visual preference cannot promote an experience that has not yet demonstrated its player question, choice, and payoff.

### 4. Terrain and macro blockout

Build the terrain and large spatial masses first: height bands, ridges, valleys, terraces, drainage, route transitions, skyline, boundaries, and major volumes. Use simple materials or semantic colors only when they communicate function, threat, ownership, or navigation. Do not use final props to compensate for a weak macro structure.

After each composition-changing batch, complete the Stage 2a post-mutation audit before the next broad batch. Verify realized member inventories against the traceability map and compare zone distribution, density, footprint, frontage, gaps, height bands, routes, water and bridge relationships, preserved shade and voids, hierarchy, and prohibited silhouettes against the recorded tolerances. A whole-map Actor total or an attractive overview cannot close this audit.

For an outdoor map level-design prototype, the ground in this stage is a minimal Landscape terrain by default, not a flat cube or plane. Keep its extent, resolution, material, and detail deliberately cheap, but use it as the source of truth for the playable height field, route elevation, slopes, grounding, and terrain contacts. Place temporary architecture and other blockout volumes on top of it. Use another floor only when a specific user or stakeholder request explicitly overrides the default, and record the reason in the brief.

Use the fixed overview set as the primary Stage 4 evidence. Compare its stable arrival, reverse, lateral, waterway/axis, elevation, and project-specific views to verify the whole-area arrangement, terrain relief, route hierarchy, bridge and water relationships, major occlusion, and risk coverage. Add or reposition a camera when the coverage matrix exposes a blind spot; do not force a fixed camera count, and do not accept a single hero overview merely because it is attractive.

Then use auxiliary fixed views at the recorded player-camera height above local ground and FOV to reject building scale, route width, slope presentation, or occlusion that is obviously implausible. These checks are intentionally coarse. Do not fine-tune scene composition or detail to the player proxy, and do not claim exact gameplay-camera, final readability, final scale, or typology approval before Stage 5. A level that works only from an intended beauty camera has not passed macro validation, and every overview remains `DIAGNOSTIC_ONLY` even though the overview set is the primary macro-composition diagnostic.

### 4a. Route authority and corridor contract (blocking sub-gate)

Treat a route as a spatial contract, not as a collection of visual strips, cubes, or debug lines. Before architecture and dressing are approved, define:

- named origins, destinations, branches, and optional loops;
- an ordered centerline represented by a spline, a typed segment graph, or another inspectable source of truth;
- intended width, slope limits, head and capsule clearance, surface provider, grade transitions, stairs or landings, and ownership;
- the objects and systems that must consume the route, such as review visualization, playable ground, collision or navigation, and procedural exclusion masks.

A spline is useful for continuous centerlines, bends, and branching relationships, but it is not a universal replacement for authored stair, landing, or terrain-transition modules. Choose the representation that preserves topology and the relevant traversal semantics. Derive route previews, exclusion masks, and automated corridor checks from the same authoritative source whenever possible.

Keep three responsibilities distinct: route intent data, review visualization, and the actual playable or walkable surface. A `NoCollision` semantic strip or a spline debug line can communicate intent, but neither proves that a player can traverse the route or that the production scene visually carries it. A route gate must state which of these responsibilities has been approved.

Validate a route as a continuous corridor rather than only at its endpoints. Sample intermediate surfaces and grade, test an expanded corridor or representative capsule against architecture, boundaries, props, and headroom, and report blockers by ownership and lifecycle state. Use simple bounds as an early filter, not as the sole proof of traversal.

### 5. Playable blockout and feedback gate

Translate the approved Area Composition Plan and Stage 2a translation contract into a playable rough draft made from a minimal Landscape terrain as the ground, simple boxes, temporary ramps, doors, cover, obstacles, encounter placeholders, and other functional volumes. Use the representative player controller and actual runtime camera rig—for example, `BP_ThirdPersonCharacter` and its `FollowCamera`/SpringArm chain—plus representative gravity, speed, and collision. Record the rig asset or class and configuration version and verify project-relevant behavior such as boom length, socket or shoulder offset, pitch, and SpringArm collision or retraction. This is the first gate with authority to approve exact gameplay-camera behavior and the perceived distance, enclosure, occlusion, route continuity, scale, visibility, readability, and typology observations that depend on it. Add these runtime results to the translation contract's post-mutation deviation records; overview metrics remain macro diagnostics. The blockout may include rough lighting, shape or color language, and functional audio cues, but it should not be burdened with decorative detail.

Play in the runtime, not only by flying an editor camera. Test at least:

- scale, capsule and camera clearance, slopes, jumps, climbs, cover, and traversal transitions;
- runtime camera distance and offsets, pitch behavior, SpringArm collision or retraction, shoulder-side assumptions, and representative near-wall, doorway, slope, and occlusion cases;
- movement, grounding, collision, route grade, and terrain contacts on the Landscape surface that will carry the prototype's outdoor traversal;
- primary route, optional loops, wrong turns, objective readability, pacing, and recovery after failure;
- landmark recognition, sightlines, occlusion, reveal timing, boundaries, unreachable shortcuts, and reverse views;
- POI-unit flow from approach and question through reveal or refusal, player choice, interaction, outcome or reward, and the next hook;
- time to meaningful change, intentional quiet sections, repeated-beat variation, and the player's ability to defer or return where the design allows it;
- representative gameplay or interaction placeholders, loading or streaming assumptions, and obvious performance risks.

Use self-playtests for fast correction, informed critique for design diagnosis, and fresh-player tests for wayfinding and expectation. Pause for user or designated approver feedback only after the evidence package is complete. Approval should state which blockout version is accepted, which decisions are frozen, and which risks remain. A failed gate returns to the plan or blockout; it does not advance to final dressing.

### 6. Visual feasibility slice before map-wide assets

Before committing the broad asset budget, build a small **visual feasibility slice** (also called a golden or representative slice). It should contain the route transition, focal landmark, foreground/midground/background structure, boundary or reverse view, contact conditions, and the asset families that will dominate the final level. Use real or representative meshes, materials, lighting, collision, target platform settings, and the Stage 5-approved runtime camera rig. Include enough repetition to expose kit weakness, not only a hero asset.

The slice must also preserve one representative experience unit: an approach, a question or reveal, a player verb or choice, an outcome or reward, and a next hook. A slice that looks convincing but does not demonstrate the fun thesis has only retired visual risk, not level-design risk.

This slice answers a different question from the graybox: can the team reproduce the intended visual quality consistently, at an acceptable cost, with viable pivots, scale, materials, LOD or Nanite behavior, collision, streaming, and frame-time or memory budgets? Judge readability, asset density, foreground/midground/background balance, and player-facing visual composition through the actual runtime rig under representative camera states. Validate more than one required gameplay view and at least one ordinary, non-hero area. The overview set may still diagnose macro drift but cannot approve these player-facing qualities. If the slice fails, repair the visual language, asset kit, material rules, or pipeline before scaling. Do not spend map-wide art effort to defend an unproven direction.

### 7. Production meshing and dressing

Replace approved proxies with approved asset families while preserving the spatial contract: zone distribution, footprint, density ranges, frontage and gaps, shade and intentional voids, hierarchy, route width and continuity, floor height, sightlines, landmark position, camera clearance, collision intent, and boundary behavior. Keep the Stage 2a traceability IDs through substitution and record deliberate deviations instead of allowing them to accumulate invisibly. Use procedural systems for repeatable placement and hand authorship for hero composition, transitions, exceptions, and story detail.

Promote in zones or representative chunks. Place large POIs and their route relationships first, then medium and small POIs according to the approved beat sheet and density hypothesis. Each chunk should be checked for contacts, repetition, reverse views, route readability, meaningful-change timing, and POI payoffs before the next chunk multiplies the same pattern. When a real asset reveals a structural problem, return to the blockout or kit rule instead of hiding it with local props.

Keep the persistent zone markers and stable zone IDs throughout every replacement and placement batch. Stage 7 cannot pass while a planned zone lacks its marker, a marker no longer matches its approved anchor or bounds, or the zone cannot be identified in overview and local evidence. Marker retirement is a separate recorded cleanup action after asset placement completion; it is never an implicit side effect of deleting blockout Actors.

### 8. Layered lighting and audio integration

Do not postpone all sound until the end. Use a functional audio scaffold during blockout when footsteps, interaction feedback, spatial cues, ambience, or a landmark signal affect navigation or pacing. If audio is a core mechanic, it belongs in the first playable slice. Add final sound effects, ambience, music, and mixing after the layout and art are stable enough that placement and context will not be discarded.

Likewise, use rough lighting and contrast early enough to test readability and mood, then perform final lighting after the asset and material pass. Lighting and audio may guide the player, but neither should be used to conceal a blockout that cannot guide the player through its geometry and spatial language.

### 9. Collision, polish, and release validation

Collision is continuous whenever geometry or traversal changes; the final pass is an audit, not the first collision test. Verify walkable and blocked expectations, capsule and camera clearance, slopes, ledges, climb or jump affordances, physics interactions, navigation, water or terrain boundaries, audio occlusion, and the absence of invisible blockers that contradict player expectation.

Polish then combines visual detail, lighting, VFX, final audio, animation or interaction feedback, accessibility, performance and scalability, streaming, persistence, packaging, and cleanup. A polish pass may close a known issue, but it cannot convert an unvalidated layout into a validated level. Reopen the responsible gate when a polish change alters route, readability, collision, or performance assumptions.

## Spatial structure

- Establish primary circulation, optional loops, reveals, landmarks, boundaries, and sightlines.
- Use coherent low, circulation, and elevated terrain roles rather than decorating one plane.
- Shape macro terrain before architecture and dressing; add mid-scale banks, terraces, drainage, routes, and foundations before micro detail.
- Grade building sites deliberately or author retaining, pier, or stepped support that visibly carries the load.
- Reserve expansion terrain with plausible elevation, drainage, boundary silhouettes, and streaming behavior.

## World-scale streaming contract

Treat World Partition as a data-management and streaming architecture decision, not as a synonym for an open world or a default project setting. Use it when world size, collaboration, runtime loading, or large-scale content generation justify the added ownership and validation work. Keep smaller or tightly authored spaces on a simpler level structure when partitioning would add more coordination cost than it removes.

Define the contract before production scale:

- **Streaming sources:** player movement, teleportation, vehicles, fast travel, cinematics, and any non-player source that must pre-load a destination.
- **Grid and cell intent:** what each grid is allowed to contain, its expected memory and I/O cost, and why its size matches the visibility and gameplay scale rather than a template default.
- **Actor loading policy:** which actors are spatially loaded, always loaded, or grouped by references, and how those choices affect persistence and failure recovery.
- **Data Layer ownership:** which editor or runtime state belongs in a Data Layer, who owns transitions, and how layer changes affect gameplay, art, audio, and save state.
- **Far-field representation:** the HLOD and reserve-content plan for distant views, including the evidence needed to prove that a streamed-out region still reads correctly.
- **Collaboration boundary:** how One File Per Actor, generated outputs, source control, review, and rollback interact with the world structure.

Connect the contract to procedural generation. A PCG graph that emits actors into a partitioned world must preserve the intended Data Layer and HLOD ownership; otherwise generation may succeed while streaming, visibility, or production review is wrong. Test the world as a sequence of loaded, loading, and unloaded states rather than judging only a fully loaded editor view.

## Asset readiness and representative proof

Inspect final-scale terrain, architecture, vegetation, water-edge, contact, and focal asset families before map-wide production. Judge appearance, pivot, scale, material compatibility, LOD or Nanite behavior, collision intent, and reverse-side quality.

Prove one representative gameplay segment before scaling. A useful golden slice is often tens of metres rather than an entire district, but its size must represent the actual route, terrain transition, POI approach-to-payoff unit, focal content, contacts, materials, lighting, boundary, reverse view, and ordinary repetition. Do not preserve a fixed number when project scale demands another representative unit.

## Full layout and ecology

Scale validated systems while preserving local variation, route readability, focal hierarchy, intentional open space, and the intended emotional rhythm. Plan large POIs and long-term destinations before filling in medium and small experiences, but allow player choice and quiet space to break a uniform pattern. Use procedural systems for repeatable spatial logic and hand authorship for hero composition, transitions, exceptions, and story detail. Finish backs, secondary routes, arrival boundaries, water banks, foundations, and views away from the focal camera. Recheck each production chunk when asset substitution changes sightlines, contacts, sound propagation, performance, or the approach and payoff of a POI.

## Feedback pauses are scoped decisions

User feedback is most useful when the question is narrow enough to answer and the artifact is concrete enough to inspect:

- **Concept pause:** Is the player fantasy, emotional tone, visual priority, and non-goal correctly understood?
- **Plan pause:** Are the fun thesis, POI roles, player questions, routes, landmarks, beats, density, and boundaries arranged as intended?
- **Translation pause:** Have the approved references been converted into zone-level ranges, hierarchy and negative-space rules, traceable prototype groups, fixed comparison conditions, and an explicit placement decision without unresolved authority conflicts?
- **Experience pause:** Does a cheap POI unit produce the intended question, choice, tension, payoff, and next hook with placeholders?
- **Blockout pause:** Does movement through the space produce the intended direction, pacing, recognition, choice, and interaction?
- **Visual-slice pause:** Does the representative quality bar and POI experience match the intended target, and is the production method affordable and repeatable?
- **Production review:** Are deviations, dependencies, and remaining risks still within the approved contract?

Do not ask a late visual review to decide an unresolved spatial question. If a later request changes a frozen assumption, explicitly reopen the affected gate and preserve the previous accepted version for comparison.

## Validation checklist

- Fun thesis, repeated verbs, player questions, emotional rhythm, and a falsifiable experience hypothesis.
- POIs have a purpose, hierarchy, approach, reveal or refusal, interaction, outcome or reward, and next hook.
- Meaningful-change intervals are intentional and calibrated to the actual movement and camera context; no mechanical 40-second filler.
- Refusal and reward are legible, tension and release have an intended rhythm, and optional deferral or return works where promised.
- Traversable terrain, route width, slopes, stairs, capsule clearance, boundaries, and spawn intent.
- Route topology, named connections, authoritative surface ownership, intermediate grade samples, continuous corridor clearance, headroom, and the distinction between intent visualization and playable surface.
- Coherent foreground, midground, and background from representative directions.
- Architecture-ground, wall-terrain, water-bank, vegetation-hardscape, and assembly contact.
- No world voids, exposed reserve edges, placeholders, uniform scatter, or unfinished reverse sides.
- Material scale, lighting hierarchy, cultural and biome coherence.
- Concept, Area Composition Plan, Reference-to-Prototype Translation, blockout, and visual-slice gates have explicit evidence, approvers, and rollback targets; both the plan and the translation contract existed and passed before the first content-bearing cube or broad asset-placement mutation.
- The Area Composition Plan records zone boundaries and stable IDs, terrain elevations and steps, primary circulation, rivers and bridges, building footprints and typology hierarchy, the source-artifact inventory and authority order, a stable-ID `DIAGNOSTIC_ONLY` overview-camera set, its relationship/risk coverage matrix, auxiliary player-height/FOV proxies, and the planned runtime-rig source.
- The Stage 2a contract validates against the bundled schema or a documented equivalent and records source IDs, versions, approval and authority scopes; the dependent-strata strategy consideration and selection when applicable; zone-level density, mass-count, typology, occupancy, frontage, gap, route-width, elevation, water/bridge, shade/void, hierarchy, and prohibited-silhouette requirements; measurement bases; tolerances; and hard failures.
- Every prototype array, repeated set, architecture proxy group, route, water or bridge proxy, reserved shade or void, and Landscape change has a stable trace from source requirement through plan feature to realized inventory; no orphan requirement or unmapped broad placement exists.
- After each composition-changing batch, same-condition reference/plan/prototype deviation records exist. Fixed overviews test assigned footprint, density, distribution, hierarchy, path, terrain, water, shade/void, and silhouette questions only; Stage 5-or-later runtime-rig evidence separately tests distance, enclosure, occlusion, reveal, route continuity, scale, and player readability.
- Gate approval is not based on aggregate Actor count: zone distribution, preserved shade and intentional voids, focal hierarchy, frontage and gaps, route continuity, and prohibited silhouettes each meet their own contract.
- Typology-critical areas pass their required sequence, hierarchy, negative-space, and silhouette rules; palace approval includes the gate -> outer court -> middle gate -> central courtyard -> main hall axis, and any fortress- or castle-like reading is a hard failure.
- AI workflow records identify the current stage, predecessor evidence, allowed mutations, promotion authority, and rollback target.
- Stable zone IDs, numeric review IDs, names, ASCII fallbacks, roles, anchors or bounds, semantic colors, marker Actors or debug-layer entries, and marker ownership are recorded before prototype geometry begins.
- Zone markers remain present and readable in overview and local evidence through the completed production-asset placement gate; any retirement has an explicit Stage 7-or-later cleanup record.
- The overview-camera set covers arrival, reverse, lateral, waterway/axis, elevation, and project-specific blind spots with the smallest sufficient number of cameras; no single hero overview or arbitrary fixed count substitutes for coverage.
- During Stages 2–4, overview evidence is the primary macro-composition diagnostic, every overview is labeled `DIAGNOSTIC_ONLY`, and auxiliary player-height/FOV proxies are limited to rejecting gross scale, width, slope, and occlusion failures without fine player-view composition.
- Stage 5 evidence records and uses the representative player controller and actual runtime camera rig, including project-relevant boom, offset, pitch, collision, and retraction behavior; Stage 6 and later player readability, asset density, and visual composition are judged through that rig.
- Overview evidence never approves player visibility, landmark readability, scale, or typology, regardless of stage.
- Every numbered stage and the route sub-gate has a recorded status; no downstream work is promoted from `PENDING_EVIDENCE`, `INVALID_EVIDENCE`, or an unrecorded gate.
- Combined stages are declared before mutation, and reopened stages preserve the accepted baseline and re-run dependent evidence.
- Functional audio and collision are tested early when they affect play, while final authoring and full audits are verified after integration.
- Streaming, persistence, warnings, and performance viability.
- World Partition is justified by the project scale, with documented streaming sources, grid/cell budgets, Data Layer ownership, HLOD intent, and teleport or fast-travel behavior.
- Representative streaming transitions, far-field views, loading recovery, and PCG-generated ownership are tested in the intended runtime configuration.
- Fixed-condition evidence before and after each major repair.

## Common mistakes

- Treating a POI as a prop or marker without a player question, action, consequence, or reward.
- Applying a 40-second rule as a uniform physical spacing requirement or filling every quiet area with low-value content.
- Testing only a whole-map traversal or a hero camera instead of the POI experience unit and its approach-to-payoff sequence.
- Confusing visual spectacle, traversal completion, or difficulty with the project's intended fun.
- Using arbitrary obstruction to create refusal without anticipation, player choice, or a worthwhile payoff.
- Using buildings, rocks, fog, or foliage to hide a flat spatial structure.
- Approving a route because its endpoints match terrain height, its AABBs do not overlap, or its debug visualization is visible.
- Adding routes after architecture is already treated as fixed, then moving unrelated props to hide a structural conflict.
- Treating a spline, semantic strip, or PCG exclusion mask as interchangeable with a complete playable route.
- Beginning rock and ground-cover generation without a `CONSIDERED` dependent-strata strategy decision, or treating the first available PCG graph as that decision.
- Building the first cube or placing broad asset batches before a versioned Area Composition Plan and its gate status are recorded.
- Treating Area Composition Plan `PASS` as permission to place prototype geometry before the Stage 2a source registry, quantitative zone contract, traceability map, tolerances, and explicit placement decision pass.
- Translating visual references by memory, silently averaging conflicting sources, or recording only qualitative phrases such as “dense” without a bounded target and measurement basis.
- Mapping only a folder or total Actor count while leaving arrays, proxy groups, paths, reserved voids, or Landscape changes without source-requirement trace IDs.
- Capturing a new convenient camera after a change, overwriting the previous comparison, or accepting an in-range total count while zone distribution, shade, hierarchy, frontage, or path continuity has drifted.
- Using one hero overview instead of a stable-ID set that covers arrival, reverse, lateral, waterway/axis, elevation, and identified spatial risks.
- Approving a palace from building size alone while its ceremonial axis or courtyard hierarchy is missing, or accepting a fortress- or castle-like silhouette.
- Using localized zone text without an always-visible numeric ID and ASCII fallback, allowing missing glyphs or clipping to erase the area's identity.
- Using a high overview camera to approve player visibility, typology, landmark readability, or scale instead of the actual player tracking-camera height and FOV.
- Precisely tuning player-view composition or detail during Stages 2–4 to a static height/FOV proxy, or treating that proxy as proof of boom, shoulder offset, pitch, SpringArm collision, or retraction behavior.
- Reaching Stage 5 without the actual runtime camera rig, or judging Golden/Visual Feasibility Slice readability, asset density, or visual composition from a fixed proxy instead of that rig.
- Replacing the default Landscape floor in an outdoor map level-design prototype without a specific user or stakeholder request; a flat cube or plane defers the highest-risk spatial assumptions until production.
- Relying on visual memory, Outliner browsing, or production art alone to identify zones, or deleting zone markers as part of proxy replacement before the asset-placement gate passes.
- Treating concept art as a complete level specification or treating user approval as a substitute for runtime evidence.
- Choosing a concept that available assets cannot support.
- Scaling a weak representative slice.
- Waiting until the end to discover that audio, collision, lighting, or streaming changes the player experience.
- Letting an AI agent begin a downstream level stage because a Tool call succeeded, a screenshot looks convincing, or the agent feels confident.
- Treating a small-level combined pass as permission to omit a stage's decision question, evidence, approval, or rollback target.
- Enabling World Partition because a template exposes it, without defining cell budgets, ownership, streaming sources, or a recovery plan.
- Treating a fully loaded editor view as evidence that a partitioned world works at runtime.
- Deleting visually appropriate content instead of repairing collision.
- Equating Actor count or grounded ratio with visual quality.

## Research basis and further reading

These sources support the durable principles above without implying that one studio's exact sequence is universal:

- [Epic Games: Project Setup and Level Blockout](https://dev.epicgames.com/documentation/en-us/unreal-engine/designer-01-project-setup-and-level-blockout-in-unreal-engine) — sketching, node maps, scale, blockout, sightlines, and early runtime testing.
- [Epic Games: World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine?lang=en-US) — streaming sources, actor loading policy, HLOD, and large-world data management.
- [Epic Games: World Partition - Data Layers](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition---data-layers-in-unreal-engine?lang=en-US) — editor organization, runtime state, and Data Layer ownership.
- [Epic Games: Level Design Content Examples](https://dev.epicgames.com/documentation/en-us/unreal-engine/level-design-content-examples?application_version=4.27) — an illustrative Prototype → Meshing → Lighting → Polish progression.
- [GDC Vault: Invisible Intuition — Blockmesh and Lighting Tips](https://www.gdcvault.com/play/1025179/Level-Design-Workshop-Invisible-Intuition) — blockmesh, player guidance, lighting, and early playtest reasoning from Naughty Dog and NYU Game Center contributors.
- [The Level Design Book: Blockout](https://book.leveldesignbook.com/process/blockout) and [Playtesting](https://book.leveldesignbook.com/process/blockout/playtesting) — massing, metrics, wayfinding, playable blockouts, and testing as the design experiment.
- [GDC: The Vertical Slice](https://media.gdcvault.com/gdc2015/presentations/Donovan_Greg_TheVerticalSlice.pdf) — a representative cross-section used to prove the intended player experience before production scale.
- [Ubisoft Toronto NEXT: Level Design Brief](https://static-wordpressv2.ubisoft.com/toronto.ubisoft.com/wp-content/uploads/2024/09/Ubisoft-Toronto-NEXT-2024-2025-Level-Design-Brief-1.pdf) — a concrete public example of a mission design document progressing to a playable blockout with feedback between phases.
- [Ubisoft Reflections: Ode behind the scenes](https://news.ubisoft.com/en-us/article/4XfuzwMvLzoWREf81P74Tn/ode-behind-the-scenes-of-reflections-musical-exploration-game) — an example of flow and navigation being established before musical patterns are layered into the world, while audio and visuals remain interdependent.

## Research notes on experience density

The following sources inform the experience-design additions without implying that one studio's exact rule is universal:

- [NDC25: 오픈 월드 레벨 디자인 시작하기](https://www.youtube.com/watch?v=Am3UnsgZqgo) — the presentation that motivated the explicit treatment of experience density, POI hierarchy, and refusal/reward in this chapter.
- [매경 게임진: 좋은 오픈월드 설계와 40초 규칙](https://game.mk.co.kr/news/it/11353182) — a public report describing POI purpose, large/medium/small hierarchy, the 40-second heuristic, and reveal/occlusion patterns; use the heuristic as a calibrated hypothesis rather than a law.
- [공개 발표 정리: 오픈 월드 레벨 디자인](https://mongmyo.tistory.com/49?category=1248586) — a secondary summary useful for the POI-unit and tension-curve interpretation, not a replacement for the primary presentation.

## Related topics

Development Process; Content & Asset Architecture; Procedural Systems & PCG; Rendering; Performance & Scalability; Validation, Testing & Debugging; Production Pipeline; Team Collaboration & Source Control; AI-Assisted Development.
