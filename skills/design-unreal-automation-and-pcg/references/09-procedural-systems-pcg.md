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

## Validation checklist

- Deterministic regeneration under recorded inputs.
- Clear responsibility, hierarchy, exclusions, and ownership.
- Counts, coverage, contact, collision, navigation, warnings, and regeneration time.
- Instancing, LOD or Nanite, HLOD, streaming, memory, and frame-budget viability.
- Generation mode, partition grid, Data Layer and HLOD ownership, source radii, cleanup behavior, scheduler limits, and cache or pooling behavior are documented.
- Runtime generation is tested while moving, stopping, turning, and teleporting, including time-to-screen, cleanup, popping, and recovery after a failed or interrupted generation.
- Player-height, reverse, elevated, and contact evidence as appropriate.
- No visible tiling, equal spacing, repeated hero assemblies, or impossible ecological placement.
- Revalidation after reuse in a new context.

## Research basis and further reading

The following sources document current Unreal Engine applications of these durable procedural principles. Their API names and feature status are version-sensitive; the design contract above should remain useful if the implementation changes:

- [Epic Games: Using PCG Generation Modes](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-generation-modes-in-unreal-engine) — partitioned, hierarchical, and runtime generation, source radii, scheduling, cleanup, and frame-time controls.
- [Epic Games: Using PCG with World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-pcg-with-world-partition-in-unreal-engine?lang=en-US) — Data Layer and HLOD assignment for generated actors.
- [Epic Games: PCG Runtime Generation Debugging](https://dev.epicgames.com/documentation/en-us/unreal-engine/pcg-runtime-generation-debugging) — runtime inspection, partition actors, and cache-related diagnostics.
- [Epic Games: World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine?lang=en-US) — streaming sources, actor loading policy, HLOD, and builder-oriented large-world workflows.

## Related topics

World & Level Design; Automation & Python; Performance & Scalability; Production Pipeline; Validation, Testing & Debugging.
