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

Use this workflow when a level, mission space, environment, or terrain change is expected to become production content. For a disposable experiment, several gates may be collapsed; for a level whose failure would strand significant art, audio, or technical work, keep the pauses explicit and evidence-based.

## When NOT to use

Do not treat the sequence as a universal linear recipe. Audio-first, vehicle, multiplayer, VR, systemic, and highly procedural experiences may need their defining risks in the first playable prototype. The rule is to move the expensive or experience-defining uncertainty earlier, not to force every project into the same number of passes.

## Decision-ready brief

Record the fun thesis, core verbs, intended emotional rhythm, POI hierarchy, experience-density hypothesis, and curiosity/reward pattern alongside player fantasy, setting, scale, biome, era, weather, time, route length, target platform, performance budget, expansion directions, and construction provenance. Define arrival, hero, route, reverse, elevated, and contact views as needed. For each important view, identify focal anchors, depth layers, value hierarchy, horizon intent, spatial relationships, and prohibited failure imagery.

## Exploration and production modes

Keep two related loops distinct:

- **Exploration:** use disposable primitives, rough terrain, temporary materials, and placeholder cues to discover whether the space is fun, readable, and in scope. Diverge from the plan when playtest evidence disproves an assumption.
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

### 1. Concept and intent review

Treat concept art as a direction hypothesis and an intent contract, not as a complete 3D blueprint. Translate it into a brief containing:

- player fantasy, emotional arc, setting, time, weather, and cultural or biome signals;
- the fun thesis, repeated player verbs, intended emotional rhythm, and the evidence that would disprove them;
- focal hierarchy, silhouette language, palette, material response, depth layers, and the views that must work;
- what the player must notice, what may remain ambiguous, and which visual readings are prohibited;
- rough scale cues, asset or technology constraints, construction provenance, and unresolved questions.

Pause for user or stakeholder feedback here. The review question is not merely “is the image beautiful?” but “does this written interpretation preserve the intended experience, priorities, and limits?” Record corrections before layout work begins.

### 2. Spatial plan review

Create a floor plan, node map, top-down diagram, and side or elevation profile as appropriate. Assign responsibilities to spaces before decorating them:

- arrival, primary route, optional loops, objectives, player verbs, encounter or rest roles;
- landmarks, reveals, sightlines, occlusion, readable openings, gates, and recovery paths;
- POI hierarchy, player questions, approach/reveal/payoff beats, optional deferral or return, and the experience-density hypothesis;
- terrain height bands, drainage or water logic, foundations, boundaries, streaming cells, and expansion directions;
- approximate scale, route timing, content cost hotspots, and the assumptions that the blockout must test.

Pause again for feedback. The plan should be understandable to someone who did not author it, and it should make the whole-space role allocation visible before construction cost rises. If the role or placement of a major area is unclear in two dimensions, more detail in three dimensions will usually hide rather than solve the problem.

### 3. Experience prototype before full blockout

Select one representative POI or encounter and build only the cheapest playable version of its experience unit: approach, question or reveal, refusal or occlusion, player choice or repeated verb, interaction, outcome or reward, and exit or next hook. Use boxes, semantic materials, temporary effects, and placeholder behavior.

Test the fun thesis, not only the geometry. Observe whether players understand what they are curious about, choose to approach or defer, experience anticipation or tension, receive a worthwhile payoff, and know what to do next. Record time to meaningful change and the role of any intentional quiet section. If the unit is weak, revise the thesis or spatial plan before building the whole route. For a small level, this gate may be combined with the next blockout step, but its evidence and approval question should remain explicit.

Pause for user or designated approver feedback after the unit has runtime evidence. A visual preference cannot promote an experience that has not yet demonstrated its player question, choice, and payoff.

### 4. Terrain and macro blockout

Build the terrain and large spatial masses first: height bands, ridges, valleys, terraces, drainage, route transitions, skyline, boundaries, and major volumes. Use simple materials or semantic colors only when they communicate function, threat, ownership, or navigation. Do not use final props to compensate for a weak macro structure.

Check the result from runtime arrival, route, reverse, elevated, and contact views. A level that works only from the intended beauty camera has not passed macro validation.

### Route authority and corridor contract

Treat a route as a spatial contract, not as a collection of visual strips, cubes, or debug lines. Before architecture and dressing are approved, define:

- named origins, destinations, branches, and optional loops;
- an ordered centerline represented by a spline, a typed segment graph, or another inspectable source of truth;
- intended width, slope limits, head and capsule clearance, surface provider, grade transitions, stairs or landings, and ownership;
- the objects and systems that must consume the route, such as review visualization, playable ground, collision or navigation, and procedural exclusion masks.

A spline is useful for continuous centerlines, bends, and branching relationships, but it is not a universal replacement for authored stair, landing, or terrain-transition modules. Choose the representation that preserves topology and the relevant traversal semantics. Derive route previews, exclusion masks, and automated corridor checks from the same authoritative source whenever possible.

Keep three responsibilities distinct: route intent data, review visualization, and the actual playable or walkable surface. A `NoCollision` semantic strip or a spline debug line can communicate intent, but neither proves that a player can traverse the route or that the production scene visually carries it. A route gate must state which of these responsibilities has been approved.

Validate a route as a continuous corridor rather than only at its endpoints. Sample intermediate surfaces and grade, test an expanded corridor or representative capsule against architecture, boundaries, props, and headroom, and report blockers by ownership and lifecycle state. Use simple bounds as an early filter, not as the sole proof of traversal.

### 5. Playable blockout and feedback gate

Replace the plan with a playable rough draft made from simple boxes, terrain, temporary ramps, doors, cover, obstacles, encounter placeholders, and other functional volumes. Use the representative player controller, camera, gravity, speed, and collision. The blockout may include rough lighting, shape or color language, and functional audio cues, but it should not be burdened with decorative detail.

Play in the runtime, not only by flying an editor camera. Test at least:

- scale, capsule and camera clearance, slopes, jumps, climbs, cover, and traversal transitions;
- primary route, optional loops, wrong turns, objective readability, pacing, and recovery after failure;
- landmark recognition, sightlines, occlusion, reveal timing, boundaries, unreachable shortcuts, and reverse views;
- POI-unit flow from approach and question through reveal or refusal, player choice, interaction, outcome or reward, and the next hook;
- time to meaningful change, intentional quiet sections, repeated-beat variation, and the player's ability to defer or return where the design allows it;
- representative gameplay or interaction placeholders, loading or streaming assumptions, and obvious performance risks.

Use self-playtests for fast correction, informed critique for design diagnosis, and fresh-player tests for wayfinding and expectation. Pause for user or designated approver feedback only after the evidence package is complete. Approval should state which blockout version is accepted, which decisions are frozen, and which risks remain. A failed gate returns to the plan or blockout; it does not advance to final dressing.

### 6. Visual feasibility slice before map-wide assets

Before committing the broad asset budget, build a small **visual feasibility slice** (also called a golden or representative slice). It should contain the route transition, focal landmark, foreground/midground/background structure, boundary or reverse view, contact conditions, and the asset families that will dominate the final level. Use real or representative meshes, materials, lighting, collision, and target platform settings. Include enough repetition to expose kit weakness, not only a hero asset.

The slice must also preserve one representative experience unit: an approach, a question or reveal, a player verb or choice, an outcome or reward, and a next hook. A slice that looks convincing but does not demonstrate the fun thesis has only retired visual risk, not level-design risk.

This slice answers a different question from the graybox: can the team reproduce the intended visual quality consistently, at an acceptable cost, with viable pivots, scale, materials, LOD or Nanite behavior, collision, streaming, and frame-time or memory budgets? Validate more than one required view and at least one ordinary, non-hero area. If the slice fails, repair the visual language, asset kit, material rules, or pipeline before scaling. Do not spend map-wide art effort to defend an unproven direction.

### 7. Production meshing and dressing

Replace approved proxies with approved asset families while preserving the spatial contract: route width, floor height, sightlines, landmark position, camera clearance, collision intent, and boundary behavior. Record deliberate deviations instead of allowing them to accumulate invisibly. Use procedural systems for repeatable placement and hand authorship for hero composition, transitions, exceptions, and story detail.

Promote in zones or representative chunks. Place large POIs and their route relationships first, then medium and small POIs according to the approved beat sheet and density hypothesis. Each chunk should be checked for contacts, repetition, reverse views, route readability, meaningful-change timing, and POI payoffs before the next chunk multiplies the same pattern. When a real asset reveals a structural problem, return to the blockout or kit rule instead of hiding it with local props.

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
- Concept, plan, blockout, and visual-slice gates have explicit evidence, approvers, and rollback targets.
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
- Treating concept art as a complete level specification or treating user approval as a substitute for runtime evidence.
- Choosing a concept that available assets cannot support.
- Scaling a weak representative slice.
- Waiting until the end to discover that audio, collision, lighting, or streaming changes the player experience.
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

Development Process; Content & Asset Architecture; Procedural Systems & PCG; Rendering; Performance & Scalability; Validation, Testing & Debugging; Production Pipeline; Team Collaboration & Source Control.
