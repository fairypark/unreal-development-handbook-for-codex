# 05 — Content & Asset Architecture

## Contents

- [Purpose](#purpose)
- [Intent](#intent)
- [When to use](#when-to-use)
- [When NOT to use](#when-not-to-use)
- [Content layers and ownership](#content-layers-and-ownership)
- [Concept-led asset supply](#concept-led-asset-supply)
- [Concept-to-Asset Readiness Contract](#concept-to-asset-readiness-contract)
- [Readiness and promotion](#readiness-and-promotion)
- [Reuse and distribution model](#reuse-and-distribution-model)
- [Recommended workflow](#recommended-workflow)
- [Validation checklist](#validation-checklist)
- [Implementation examples](#implementation-examples)
- [Common mistakes](#common-mistakes)
- [Research basis and further reading](#research-basis-and-further-reading)
- [Related topics](#related-topics)

## Purpose

Give Unreal content explicit ownership, dependency direction, provenance, lifecycle, and reuse boundaries so projects can source, integrate, migrate, cook, collaborate, and distribute safely.

## Intent

Treat assets as versioned production data rather than convenient files. Make their source, owner, consumers, dependencies, allowed mutations, acquisition authority, licensing evidence, intended use, and promotion state discoverable.

For concept-led environment work, turn visual direction into a controlled content supply plan before level dressing begins. The goal is not to find objects that resemble one screenshot. It is to prove that a coherent family of assets can reproduce the concept's spatial function, visual language, variation, contacts, reverse views, and technical budget across a representative playable space.

## When to use

Use this chapter when content will be acquired, authored, reused, migrated, generated, packaged, or promoted into production; when a concept or art direction must be converted into asset requirements; or when ownership, licensing, dependencies, compatibility, integration cost, or replacement risk can affect scope.

## When NOT to use

Do not require a production supply contract for an isolated disposable placeholder with no reuse, acquisition, or downstream dependency. Do not use asset sourcing to postpone unresolved level structure: a large catalog cannot repair a weak route, hierarchy, or Area Composition Plan. Do not treat this chapter as authorization to purchase, download, install, migrate, or enable external content; those are separate external or Editor actions with their own approval and recovery requirements.

## Content layers and ownership

Separate authored source, generated or derived content, runtime data, configuration, caches, and disposable intermediates. Use naming and folders to communicate stable responsibility rather than a temporary task or contributor.

For every asset family, identify:

- source of truth, owner, consumers, and mutation authority;
- authored source, imported package, generated outputs, and project adaptations;
- direct and transitive dependencies, required plugins, configuration, and runtime systems;
- provenance, entitlement or license evidence, acquisition date or terms version, and permitted project or distribution scope;
- engine, renderer, platform, skeleton or rig, material, collision, navigation, streaming, memory, and packaging constraints;
- replaceable inputs, project-specific data, rejected predecessors, and rollback target.

Never store credentials, cookies, payment data, private tokens, or secret-bearing URLs in an asset record. Keep only non-sensitive evidence identifiers and redacted acquisition metadata.

## Concept-led asset supply

### Translate visual intent into asset demand

Begin with the approved concept interpretation, Area Composition Plan, and Stage 2a source requirements. Preliminary discovery may begin earlier to expose feasibility risk, but the supply plan cannot pass until each demand is traceable to approved source and zone requirements.

Decompose the concept by **production function**, not only by object noun. Record the asset families needed to carry:

- hero focal identity and silhouette;
- structural architecture kits, roofs, entrances, corners, endings, stairs, foundations, and level transitions;
- terrain, route, water-edge, retaining, bridge, and grounding transitions;
- boundaries, occluders, traversal affordances, cover, and gameplay-readable obstacles;
- biome layers, vegetation strata, hardscape, ground cover, decals, and contact dressing;
- materials, trims, surface variation, weathering, damage states, and color or value control;
- set dressing, cultural or narrative signals, repeated ordinary content, and intentional absence;
- lighting fixtures, VFX, audio, animation, interaction, or systemic content when they define the intended experience.

For each demand, state its stable ID, source-requirement and zone IDs, role, priority, required scale range, expected instance range, minimum useful variation, modular and transition pieces, reverse-side and contact requirements, visual constraints, technical constraints, acceptance evidence, fallback strategy, and the stage by which it must be ready. A concept crop may imply a family without proving its unseen sides, kit completeness, playable scale, or repetition quality; record those as unknowns instead of inventing them.

### Search in cost order

Search in an order that minimizes irreversible commitment and integration cost:

1. suitable project-native content already under project ownership;
2. organization or team libraries with known provenance and dependencies;
3. ownership-confirmed marketplace or vendor-library entitlements;
4. new external acquisition requiring explicit authorization;
5. custom authoring, scanning, kitbashing, procedural construction, or outsourcing;
6. an approved concept, scope, or spatial substitution when supply cannot support the original direction.

An external listing, search result, remembered purchase, or public product page does not prove ownership. Verify the entitlement in the authorized library or account context without extracting credentials. When an owned-catalog capability is available, use it before proposing a new purchase, but still inspect the exact candidate's current contents, compatibility, license, and integration cost.

### Evaluate families, not screenshots

Judge a candidate against the demand it must cover:

- visual fit under the target camera, lighting, weather, scale, and ordinary repetition—not only the listing's hero image;
- family completeness: straight modules, corners, caps, transitions, openings, foundations, reverse sides, damage or weather variants, and necessary negative space;
- material compatibility, texel density, parameter control, surface aging, tint range, and interaction with the project's rendering path;
- pivot, orientation, units, scale, collision, navigation, sockets, skeleton or rig, animation, LOD or Nanite behavior, impostors, and platform support;
- dependency graph, required plugins, source-control and storage cost, shader or derived-data cost, streaming behavior, memory, draw-call or instance behavior, and cook or packaging impact;
- integration, cleanup, adaptation, validation, maintenance, and replacement effort in addition to purchase price.

A large pack with many advertised assets may provide less production coverage than a smaller coherent kit. Count usable roles and variants after inspection, not listing item totals.

### Keep discovery, acquisition, and approval distinct

Use explicit states so the presence of a candidate cannot be mistaken for readiness:

`DISCOVERED → OWNERSHIP_VERIFIED → ACQUIRED_TO_STAGING → REPRESENTATIVE_APPROVED → PRODUCTION_APPROVED`

`REJECTED` and `BLOCKED` are terminal or reopening states, not hidden notes. For project-authored or procedural content, `OWNERSHIP_VERIFIED` may be `NOT_APPLICABLE`, but provenance and mutation authority remain required.

- **Discovered:** a possible source or authoring route is known.
- **Ownership verified:** entitlement or creation authority is confirmed; this does not prove compatibility.
- **Acquired to staging:** the exact version and dependencies are available in an isolated, recoverable evaluation context; this does not authorize map-wide placement.
- **Representative approved:** the candidate passes demand-specific visual and technical checks in a representative slice and may support the Visual Feasibility Slice.
- **Production approved:** the selected family passes licensing, ownership, dependency, integration, performance, packaging, repeatability, and replacement checks for its declared scope and may be used in production dressing.

New purchase, download, install, migration, plugin enablement, outsourcing commitment, or upload remains locked until the responsible person explicitly authorizes that action. Approval of the supply plan authorizes investigation and scheduled work only; it does not authorize an external transaction.

## Concept-to-Asset Readiness Contract

For concept-led level work, create a machine-readable **Concept-to-Asset Readiness Contract** using the bundled [JSON Schema](concept-to-asset-readiness.schema.json) and [starter template](concept-to-asset-readiness.template.json), or a project-owned equivalent that preserves the same semantics.

The contract contains:

1. the controlling concept, Area Composition Plan, Stage 2a translation-contract version, source requirements, zones, target engine and platforms, and performance context;
2. asset-demand records based on production functions, required family coverage, variation, constraints, acceptance evidence, fallback, owner, and due stage;
3. candidate records with source type, non-sensitive locator, entitlement, acquisition authorization, license, compatibility, dependency, total-cost, evaluation, and readiness state;
4. one coverage decision for every demand, including selected candidates, known gaps, fallback, waiver or concept-revision evidence, and owner;
5. acquisition or authoring actions with authority, budget reference, due gate, status, rollback, and evidence;
6. separate Plan, Visual Slice, and Production Dressing decisions so cheap blockout can continue without pretending final assets are ready;
7. computed integrity fields for orphan candidates, uncovered demands, unresolved licenses or compatibility, unauthorized external acquisitions, and demands not ready for production.

The contract is a decision record, not a shopping list. A candidate may cover several demands, and one demand may require several complementary candidates. Preserve those many-to-many mappings rather than forcing every concept object to one purchased asset.

## Readiness and promotion

Use three independent gates:

| Gate | Question | Minimum passing evidence | What it authorizes |
| --- | --- | --- | --- |
| `ASSET_PLAN_READY` | Do all approved concept demands have an owned, acquired, authored, procedural, outsourced, or concept-revision route with an owner, budget boundary, fallback, and due stage? | Complete demand registry, one coverage record per demand, explicit sourcing routes, high-risk gaps, authorization boundaries, and rollback. | Experience prototype and blockout may continue; no representative or production asset placement is implied. |
| `VISUAL_SLICE_READY` | Are the families required to prove visual feasibility actually available and credible? | Required candidates are acquired to staging or project-native, license and compatibility are resolved, and representative visual/technical checks pass. | Only the declared Visual Feasibility Slice scope. |
| `PRODUCTION_DRESSING_READY` | Can every production-blocking demand be supplied, integrated, repeated, cooked, and maintained within the approved scope? | Every required demand is `PRODUCTION_READY` or has an approved concept/scope waiver; selected candidates are production-approved; external actions are authorized and complete; dependencies, license, budget, performance, storage, and rollback evidence pass. | Production meshing and dressing for the approved zones and asset families. |

A gate authorizes only its named scope. A representative asset may pass the Visual Slice while the full kit, variant count, or license coverage remains insufficient for map-wide dressing. A Production Dressing decision must name the exact contract version, zones, demands, candidates, approver, time, and rollback baseline.

Reopen the earliest responsible decision when the concept, source authority, zone plan, target platform, engine version, rendering path, candidate version, license, dependencies, required plugin, acquisition authority, budget, or representative evidence changes. Preserve rejected candidates and the reason for rejection so the same mismatch is not rediscovered.

## Reuse and distribution model

Distinguish three layers:

1. **Project source library:** exact approved assets with project-licensed dependencies and evidence.
2. **Portable system contract:** dependency-free roles, inputs, outputs, exclusions, parameters, and validation requirements.
3. **Distributable content plugin:** actual assets whose complete dependency graph is declared, license-clean, and tested outside the source project.

Previous approval does not transfer automatically. Default reused systems and purchased content to revalidation for the new scale, biome, platform, lighting, gameplay, content substitutions, license scope, and dependency context.

## Recommended workflow

1. **Requirements:** approve the concept interpretation, non-goals, target zones, platforms, budget boundaries, and prohibited readings.
2. **Planning:** extract asset demands, required family coverage, variation, contacts, due stages, and acceptance evidence from the controlling source requirements.
3. **Architecture:** assign ownership, dependencies, staging boundaries, content roots, naming, metadata, sourcing routes, acquisition authority, and replacement strategy.
4. **Validation plan:** define Plan, Visual Slice, and Production Dressing gates; separate visual, technical, licensing, compatibility, performance, integration, cook, and recovery evidence.
5. **Implementation:** discover project and owned-library candidates first; request external authorization where required; acquire or author into staging; preserve exact versions and dependency reports.
6. **Verification:** inspect candidates in representative conditions, audit selected family coverage, test load and cook where appropriate, and record rejection, waiver, or promotion decisions.
7. **Optimization:** simplify dependencies, consolidate material and kit rules, reduce avoidable variants, and scale only production-approved families without lowering the approved visual or gameplay contract.

## Validation checklist

- Every asset demand traces to approved concept or Stage 2a source requirements and stable zone IDs.
- Demands describe production functions, family completeness, variation, scale, contacts, reverse sides, technical constraints, acceptance evidence, fallback, owner, and due stage.
- Project-native and ownership-confirmed library content was considered before a new purchase.
- Public listings and search results are never reported as owned without entitlement evidence.
- Discovery, ownership, acquisition, representative approval, and production approval remain separate states.
- External acquisition and outsourcing actions have explicit authority; no plan approval is treated as transaction approval.
- License name or identifier, terms version or acquisition date, intended scope, restrictions, and non-sensitive evidence are recorded.
- Engine, platform, renderer, material, skeleton or rig, collision, navigation, LOD or Nanite, plugin, dependency, streaming, memory, cook, and packaging implications are checked where relevant.
- Total cost includes integration, adaptation, storage, shader or derived-data, validation, maintenance, and replacement effort—not only purchase price.
- Every demand has exactly one current coverage decision, and every selected candidate traces back to one or more demands.
- Visual Slice readiness covers all families needed by the representative slice; placeholders are clearly excluded from readiness evidence.
- Production Dressing readiness covers every production-blocking demand or records an approved concept/scope revision with an owner and affected source requirements.
- No unexpected hard or circular dependencies.
- Source and generated assets are distinguishable.
- Redirectors and stale references are resolved intentionally.
- Licenses allow the intended use and distribution.
- A clean project or declared-dependency environment loads and cooks the package when distribution or migration is intended.
- Private paths, credentials, user data, and project-only coordinates are absent from portable artifacts.
- Ownership, rejected alternatives, replacement strategy, and recovery remain clear after integration or migration.

## Implementation examples

### Modular settlement from a concept image

Do not create one demand for every visible building. Create demands for the primary hall family, supporting residential kit, gate and wall transitions, roof language, foundations and terrain contacts, bridge or route transitions, ordinary props, and required material variation. A marketplace architecture pack may cover walls and roofs but fail the gate if it lacks corners, foundations, reverse sides, or the ceremonial hierarchy required by the source contract. The gap can be filled by a second compatible family, custom transition pieces, or an approved concept revision; it cannot be hidden by reporting the pack's total mesh count.

### Owned vegetation pack

An ownership-confirmed pack is a strong candidate, not a production approval. Stage it, verify the exact version and license scope, then test species mix, scale, season or biome match, wind and shading behavior, collision, Nanite or LOD policy, ground contact, procedural compatibility, density cost, and ordinary repetition in the representative slice. Promote only the asset families that pass; retaining the rest of the pack in a library does not make them project dependencies.

### Unavailable hero landmark

If no candidate can preserve the landmark's silhouette, scale, and playable approach within schedule and budget, record the supply failure early. Compare custom authoring, kitbash, outsourcing, procedural construction, and a concept or plan revision. The correct decision may be to change the concept before production, not to accept a visually similar but structurally wrong asset because it is immediately downloadable.

## Common mistakes

- Treating the concept image as a literal object shopping list instead of extracting functional asset families and unknown views.
- Searching public listings before checking project-native and ownership-confirmed content.
- Calling an asset “available” because a listing exists, it was remembered as purchased, or a tool returned a title.
- Downloading or installing a large pack before defining which demands it must cover and how it can be rolled back.
- Treating purchase price, advertised mesh count, or screenshot similarity as total value.
- Approving a kit without corners, caps, transitions, foundations, reverse sides, contacts, material control, or enough ordinary variation.
- Letting a hero asset pass while repeated supporting content, boundaries, or terrain transitions remain unresolved.
- Treating acquired content as production-ready before dependency, license, compatibility, representative, performance, and cook checks.
- Allowing a Visual Slice approval to authorize map-wide dressing.
- Hiding a supply failure with increasingly local substitutions instead of reopening the concept, plan, budget, or schedule decision.
- Copying credentials, cookies, payment information, secret-bearing URLs, or private account data into provenance records.

## Research basis and further reading

- [Epic Games: Purchasing and Downloading Assets in Fab](https://dev.epicgames.com/documentation/fab/purchasing-and-downloading-assets-in-fab?lang=en-US) — distinguishes listings, products, packs, acquisition, libraries, and migrated products; use current account and product evidence rather than memory.
- [Epic Games: Licenses and Pricing in Fab](https://dev.epicgames.com/documentation/fab/licenses-and-pricing-in-fab) — current Fab license types and tiers; record the terms that apply to the exact acquisition instead of assuming one universal marketplace license.
- [Epic Games: Migrating Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/migrating-assets-in-unreal-engine) — dependency reporting and the risk of incomplete migration.
- [Epic Games: Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine) — explicit asset discovery, loading, auditing, cooking, and chunking responsibilities.
- [Epic Games: Asset Metadata](https://dev.epicgames.com/documentation/unreal-engine/asset-metadata-in-unreal-engine) — editor-facing provenance and workflow metadata as inspectable production data.

## Related topics

Development Process; Project & System Architecture; World & Level Design; Automation & Python; Procedural Systems & PCG; Rendering; Performance & Scalability; Validation, Testing & Debugging; Production Pipeline; Team Collaboration & Source Control; AI-Assisted Development; Case Studies.
