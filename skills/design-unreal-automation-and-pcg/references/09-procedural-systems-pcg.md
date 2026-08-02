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

## Ecology and placement

Build canopy, understory, shrubs, ground cover, deadfall, and contact debris as distinct strata. Use gradients, clusters, transitions, and intentional gaps rather than uniform scatter or perimeter rings. Validate broad assets across their visual footprint; a center hit or grounded point count does not prove believable support.

## Comparative iteration

Expose one candidate at a time. Disable superseded generations and verify which components contribute to the frame before comparison. Overlapping candidates invalidate the result even when every graph reports success.

## Procedural exceptions and override provenance

Keep the procedural base and manual exceptions as separate layers with one declared authority. Use an exception for a focal composition, sightline, traversal requirement, story beat, ecological transition, or other approved design intent—not to hide a broken rule or an unvalidated source asset.

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
- A single declared spatial authority for route-coupled masks, with route version, width or clearance inputs, branch ownership, and regeneration dependencies recorded.
- Counts, coverage, contact, collision, navigation, warnings, and regeneration time.
- Instancing, LOD or Nanite, HLOD, streaming, memory, and frame-budget viability.
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

## Research basis and further reading

The following sources document current Unreal Engine applications of these durable procedural principles. Their API names and feature status are version-sensitive; the design contract above should remain useful if the implementation changes:

- [Epic Games: Using PCG Generation Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine) — partitioned, hierarchical, and runtime generation, source radii, scheduling, cleanup, and frame-time controls.
- [Epic Games: Using PCG with World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-world-partition-in-unreal-engine?lang=en-US) — Data Layer and HLOD assignment for generated actors.
- [Epic Games: PCG Runtime Generation Debugging](https://dev.epicgames.com/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging) — runtime inspection, partition actors, and cache-related diagnostics.
- [Epic Games: World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine?lang=en-US) — streaming sources, actor loading policy, HLOD, and builder-oriented large-world workflows.

Additional current context:

- [Epic Games: PCG Development Guides](https://dev.epicgames.com/documentation/en-us/unreal-engine/pcg-development-guides) — current PCG authoring and workflow context; verify feature names and maturity against the target engine version.
- [Epic Games: Unreal Engine 5.8 Release Notes](https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-8-release-notes) — dated evidence for the Manual Edit tool, Data Overrides Panel, and experimental Data Override System; use these as implementations of the override contract, not as the durable principle itself.

## Related topics

World & Level Design; Automation & Python; Performance & Scalability; Production Pipeline; Validation, Testing & Debugging.
