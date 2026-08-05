# 09 — Procedural Systems & PCG

## Purpose

Encode repeatable spatial or content logic while preserving determinism, authorial control, performance budgets, and evidence-based validation.

## Intent

Use procedural systems to scale a proven rule, not to compensate for unsuitable source content, unclear composition, or missing ownership.

## When to use

Use procedural generation for repeatable distribution, density gradients, ecological or construction rules, exclusions, large-area regeneration, and controlled variation. Prefer direct authorship for hero composition, unique transitions, narrative specificity, and exceptions whose value comes from intentional placement.

## Design workflow

1. Define the visible or gameplay responsibility and approved scope.
2. Inspect source assets at final material, scale range, and viewing distance.
3. Author one coherent source assembly before proceduralizing multi-part relationships.
4. Assign semantic roots and required, optional, collision, and helper roles.
5. Preserve hierarchy and remove dependent children when required parents fail.
6. Separate generators by responsibility and use one orchestration authority for exclusions and final composition.
7. Expose deterministic seeds, masks, density, scale, slope, height, distance, and platform constraints.
8. Validate the isolated pattern, contact, unchanged scene context, and final role before broad promotion.

### Spatial authority and route-coupled generation

When a generator depends on circulation, boundaries, or buildable space, identify the authoritative spatial source before generating content. A route graph or spline may drive review geometry, playable-surface planning, and exclusion masks, but those outputs remain separate responsibilities with separate validation. Do not let a debug line, semantic strip, or exclusion mask stand in for a complete traversable route.

Derive route-related masks from the same versioned source used by corridor validation. Record the width, clearance envelope, surface provider, branch identity, and lifecycle state that the generator consumed. Regenerate after a route or terrain change, then recheck both the route and every generator that depends on its mask. If a route is still exploratory, keep generated ecology and construction candidates clearly unapproved rather than allowing them to become hidden blockers.

## Generation modes and the World Partition contract

Choose a PCG generation mode from the content scale, ownership, streaming behavior, and time-to-screen requirement. The modes are different production contracts, not interchangeable switches:

| Mode | Appropriate use | Main risk to validate |
| --- | --- | --- |
| Non-partitioned | Small, local, or intentionally atomic results where simple ownership is more valuable than streaming granularity. | A large domain creates an unstreamable or expensive result. |
| Partitioned | Large static or baked results that should be divided across a predictable grid and streamed with the world. | Grid size, cell ownership, regeneration scope, and cross-cell continuity are wrong. |
| Hierarchical | Content with meaningful scales, such as large rocks or trees at coarse grids and ground cover at finer grids. | A single grid causes poor streaming, excessive work, or visible scale transitions. |
| Runtime | Content that must generate and clean up near an active source during play, PIE, or standalone execution. | Generation scheduling, cleanup, pooling, cache use, or time-to-screen causes hitches or visible popping. |

For partitioned or hierarchical generation, choose grid sizes from the generated asset footprint and streaming budget. Larger, less numerous meshes generally belong to larger grids; smaller, more numerous detail can use smaller grids. Do not infer that deterministic inputs guarantee deterministic arrival order when runtime work is scheduled in parallel. If order affects composition, gameplay, or evidence capture, make the dependency explicit or remove the order dependency.

Treat Data Layer and HLOD assignment as part of the output contract. Each spawn or target branch should define whether generated actors inherit the source layer, use a referenced layer, or intentionally remain outside runtime layer changes. The same decision applies to HLOD ownership. A graph is not production-ready if it produces the right count of actors but loses the world's streaming, visibility, or review boundaries.

Runtime generation also needs a source and cleanup policy: identify which players, editor views, World Partition sources, or explicit components can trigger generation; define increasing generation radii by grid scale; set a cleanup radius that prevents thrashing; and measure scheduler work, pooling, cache use, and frame-time contribution under movement and teleportation. Validate the transitions, not only the final generated image.

### Dependent-strata strategy gate

When a placement request contains a source stratum and a dependent stratum—for example, rocks or stone hardscape followed by grass or other ground cover—run this conditional sub-gate of Stage 2a before the first content-bearing generator, Foliage, or batch-placement mutation. The gate is required even when the final choice is manual placement. Its purpose is to prove that the AI considered the video-style distance/exclusion method and selected a method for stated spatial reasons rather than inheriting an implementation from a tutorial or from the first tool that happens to be available.

Always record the following in the workflow or translation contract:

- `applicability`: `APPLICABLE` or `NOT_APPLICABLE`;
- `consideration_status`: `CONSIDERED`;
- `selected_mode`: `VIDEO_DISTANCE_EXCLUSION`, `MASK_OTHER`, `DIRECT_AUTHORED`, or `PENDING_EVIDENCE`;
- the decision reason, source authority, dependency order, units, clearance, transition band, validation method, and gate status;
- the source mesh or footprint version, generation/graph version, target platform, and evidence IDs when the mode is applicable.

Use the following decision order:

1. Select `VIDEO_DISTANCE_EXCLUSION` when the hardscape output has a stable final footprint or a declared conservative footprint, the dependent layer should clear or approach that footprint, and the project can validate final transformed mesh separation. Generate the source first, publish its footprint, then derive the dependent candidates and inner exclusion or outer transition band from that authority.
2. Select `MASK_OTHER` when a route, Landscape region, volume, Data Layer, or another spatial rule is the real authority and a hardscape-distance relationship would be misleading or redundant. Record why that authority owns the exclusion.
3. Select `DIRECT_AUTHORED` when the source is exploratory, hero-specific, irregular in a way that the declared bounds cannot represent, or intentionally composed by hand. Keep any procedural broad layer separate from the authored exception and record its provenance.
4. Select `PENDING_EVIDENCE` when source bounds, scale, units, ownership, engine support, target-platform budget, or the intended contact relationship is unresolved. Keep dependent placement read-only until the missing evidence is resolved.

`CONSIDERED` is not the same as `VIDEO_DISTANCE_EXCLUSION`: the record must preserve the rejected alternatives and the reason for the final selection. A `PASS` strategy gate authorizes only the selected responsibility; it does not approve visual quality or map-wide duplication. Reopen it when the source mesh, footprint, transforms, graph version, generation mode, terrain, exclusion rule, or target platform changes.

### Hardscape-to-ground-cover exclusion

A common multi-stratum pattern is to generate a hardscape assembly such as stone tiles, rocks, a curb, or a constructed edge, then generate ground cover in the remaining surface and in a controlled contact or transition band. This is a spatial dependency contract, not a universal graph recipe.

Use this pattern when the source assembly has a stable spatial footprint and the dependent layer must remain clear of, or intentionally approach, that footprint. Prefer direct authorship or a different mask when the source is still exploratory, its bounds are not trustworthy, or the visual result depends on hero-specific placement.

Design the contract as follows:

1. Author and validate the hardscape assembly first. Give it a semantic root and one published output that downstream generators can consume.
2. Treat the final hardscape footprint as the exclusion authority. Use conservative transformed bounds or another declared spatial representation; center-to-center distance alone can under-exclude large, rotated, or irregular meshes.
3. Generate ground-cover candidates from the authoritative terrain or surface provider, then calculate the nearest source distance. A distance operation such as a PCG Distance node may provide the attribute, but the durable contract is the declared footprint and its validation, not a particular node. Convert that distance into an inner exclusion radius and, when useful, an outer transition band whose density or scale changes gradually.
4. Keep the exclusion and final composition in one orchestrator. A missing, stale, or failed hardscape source should fail closed or remain visibly unapproved rather than silently allowing a second generator to fill the gap.
5. Expose the clearance, transition width, sample spacing, density, variation, seed, source/target representation, and platform constraints. Record units and do not promote a tutorial's numeric default across different asset scales.
6. Recompute and validate the minimum source-to-target separation after final translation, rotation, scale, projection, and mesh selection. A point attribute or center sample is diagnostic; it is not proof that the rendered mesh clears the hardscape.
7. Reopen validation when the source mesh, source bounds, transforms, graph version, terrain, exclusion rule, or generation mode changes.

The trade-off is between cost and fidelity. Conservative bounds are cheap and safe but can create gaps that are wider than the art direction intends. More precise mesh or distance-field representations can improve contact bands but add authoring, memory, or generation cost. Choose the representation from the visual and collision responsibility, then measure the result at representative scale and viewing distance.

### Version-sensitive rendering and culling decisions

Nanite detail streaming, PCG generation, traditional distance culling, and HLOD solve different problems. Do not treat enabling Nanite as evidence that a distance-cull policy is active, or treat a low visible instance count as proof that generation and memory cost are acceptable.

For any version-sensitive rendering or visibility feature, record the engine build, target hardware, feature maturity, prerequisites, fallback, and evidence date. At the time of this chapter, Epic's Unreal Engine 5.8 Nanite documentation lists view-specific distance culling as unsupported; verify the current target version rather than carrying that limitation forward or assuming it has changed. If distance-based visibility is required, choose a supported representation or generation/streaming policy and validate the actual behavior, popping, frame time, memory, and packaging result.

For broad PCG coverage, choose non-partitioned, partitioned, hierarchical, or runtime generation from ownership and time-to-screen requirements. Validate grid ownership, source and cleanup radii, Data Layer and HLOD behavior, scheduler work, and transitions while moving or teleporting. The choice is a production contract, not a post-hoc optimization toggle.

## Ecology and placement

Build canopy, understory, shrubs, ground cover, deadfall, and contact debris as distinct strata. Use gradients, clusters, transitions, and intentional gaps rather than uniform scatter or perimeter rings. Validate broad assets across their visual footprint; a center hit or grounded point count does not prove believable support.

## Comparative iteration

Expose one candidate at a time. Disable superseded generations and verify which components contribute to the frame before comparison. Overlapping candidates invalidate the result even when every graph reports success.

## Procedural exceptions and override provenance

Keep the procedural base and manual exceptions as separate layers with one declared authority. Use an exception for a focal composition, sightline, traversal requirement, story beat, ecological transition, or other approved design intent—not to hide a broken rule or an unvalidated source asset.

UE 5.8's PCG Manual Edit and Data Override System are a version-specific implementation of this contract: they allow selected generated data to be excluded or modified non-destructively and restored while exposing applied overrides for inspection. Treat these changes as a delta layer over a versioned procedural base, not as a replacement source of truth. Before promotion, record the generating graph and input snapshot, stable target identity or mapping policy, scope, intent, owner, approval, and rollback or revalidation condition. During regeneration, reapply an override only when the base remains compatible; classify missing or ambiguous mappings as orphaned or conflicting rather than silently baking, erasing, or duplicating them. Because the UE 5.8 Data Override System and PCG Editor Mode are version-sensitive and Experimental, validate persistence, regeneration, source-control behavior, performance, and fallback under the project's target build before making them a production dependency.

For every accepted exception, record the source generation identity, seed or input snapshot, graph version, target scope, intent, owner, approval, priority, expiration or revalidation condition, and rollback action. A manual change that cannot be traced back to the generated baseline is a future regeneration failure waiting to happen.

Regeneration must preserve valid overrides, report orphaned or conflicting overrides, and never silently erase or duplicate them. A graph change, asset replacement, World Partition change, or changed exclusion rule reopens validation for affected exceptions. Keep temporary exploration visibly distinct from a promoted exception, and review exceptions as a growing maintenance budget rather than allowing them to become a second hidden generator.

| Layer | Responsibility | Failure if missing |
| --- | --- | --- |
| Procedural base | Repeatable rule, broad coverage, deterministic inputs, and regeneration. | Manual edits become the only undocumented source of truth. |
| Exception record | Intentional deviation, owner, scope, provenance, precedence, and revalidation condition. | Regeneration silently breaks composition or gameplay. |
| Promotion and rollback | Decide when an exception is accepted, how it is compared, and how it is removed. | Temporary experiments accumulate as permanent technical debt. |

## Validation checklist

- Deterministic regeneration under recorded inputs.
- Clear responsibility, hierarchy, exclusions, and ownership.
- For dependent strata, the source footprint authority, clearance or transition band, units, dependency order, and stale-source behavior are recorded.
- A single declared spatial authority for route-coupled masks, with route version, width or clearance inputs, branch ownership, and regeneration dependencies recorded.
- Counts, coverage, contact, minimum separation after final transforms, collision, navigation, warnings, and regeneration time.
- Instancing, LOD or Nanite, HLOD, streaming, memory, and frame-budget viability.
- Version-sensitive culling or rendering claims include engine identity, target platform, fallback, and direct visibility/performance evidence.
- Generation mode, partition grid, Data Layer and HLOD ownership, source radii, cleanup behavior, scheduler limits, and cache or pooling behavior are documented.
- Procedural output and manual overrides are separate, with precedence and ownership documented.
- Each promoted override has scope, intent, source generation identity, graph version, approval, and rollback or revalidation conditions.
- Regeneration detects orphaned or conflicting overrides and preserves accepted exceptions without silently duplicating them.
- Runtime generation is tested while moving, stopping, turning, and teleporting, including time-to-screen, cleanup, popping, and recovery after a failed or interrupted generation.
- Player-height, reverse, elevated, and contact evidence as appropriate.
- No visible tiling, equal spacing, repeated hero assemblies, or impossible ecological placement.
- No generated result is evaluated as a route, playable surface, or approval evidence unless that responsibility was explicitly implemented and validated.
- Active, unapproved, hidden-recoverable, and retired outputs are reported separately during comparison and blocker audits.
- Revalidation after reuse in a new context.

## Common mistakes

- Baking manual changes into generated output and losing their provenance.
- Treating every exception as proof that the graph is wrong, or every graph failure as something to conceal with overrides.
- Allowing overrides to accumulate until they form a second, undocumented generator.
- Regenerating after a graph or asset change without checking orphaned, conflicting, or stale exceptions.
- Copying a distance threshold from a tutorial without recording units, source scale, bounds policy, and target viewing distance.
- Measuring distance between source centers while the rendered source meshes have materially different bounds or rotations.
- Assuming Nanite automatically replaces distance culling, streaming policy, instance budgeting, or target-platform profiling.

## Research basis and further reading

The following sources document current Unreal Engine applications of these durable procedural principles. Their API names and feature status are version-sensitive; the design contract above should remain useful if the implementation changes:

- [Epic Games: Using PCG Generation Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine) — partitioned, hierarchical, and runtime generation, source radii, scheduling, cleanup, and frame-time controls.
- [Epic Games: Using PCG with World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-world-partition-in-unreal-engine?lang=en-US) — Data Layer and HLOD assignment for generated actors.
- [Epic Games: PCG Runtime Generation Debugging](https://dev.epicgames.com/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging) — runtime inspection, partition actors, and cache-related diagnostics.
- [Epic Games: World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine?lang=en-US) — streaming sources, actor loading policy, HLOD, and builder-oriented large-world workflows.

Additional current context:

- [Epic Games: PCG Node Reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/procedural-content-generation-framework-node-reference-in-unreal-engine) - Distance, Surface Sampler, Get Landscape Data, and Static Mesh Spawner semantics; verify node options against the target engine version.
- [Epic Games: Nanite Virtualized Geometry](https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry) - Nanite streaming, supported features, and version-sensitive rendering limitations.
- [Epic Games: Cull Distance Volumes](https://dev.epicgames.com/documentation/en-us/unreal-engine/cull-distance-volumes-in-unreal-engine) - distance-cull configuration and popping checks for supported actor representations.
- [Epic Games: PCG Development Guides](https://dev.epicgames.com/documentation/en-us/unreal-engine/pcg-development-guides) — current PCG authoring and workflow context; verify feature names and maturity against the target engine version.
- [Epic Games: Unreal Engine 5.8 Release Notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) — dated evidence for the Manual Edit tool, Data Overrides Panel, and experimental Data Override System; use these as implementations of the override contract, not as the durable principle itself.

## Related topics

World & Level Design; Automation & Python; Performance & Scalability; Production Pipeline; Validation, Testing & Debugging.
