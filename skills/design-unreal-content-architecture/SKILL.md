---
name: design-unreal-content-architecture
description: Design or review Unreal content and asset architecture, including concept-led asset requirements, owned-library discovery, sourcing and acquisition planning, readiness gates, naming, folders, ownership, dependencies, data assets, reuse, migration, provenance, licensing, and lifecycle. Use before level dressing, external asset acquisition, Content reorganization, cross-project reuse, distributable packaging, or when diagnosing dependency and ownership problems. Do not use for an isolated import or Content Browser operation.
---

# Design Unreal Content Architecture

Treat content as versioned production data with ownership and lifecycle, not as a collection of convenient files or marketplace search results.

## Load the Handbook chapter

Read [05-content-asset-architecture.md](references/05-content-asset-architecture.md) before deriving assets from a concept, planning acquisition, reorganizing, reusing, migrating, or distributing content. Apply its ownership, demand, candidate, acquisition-authority, dependency, provenance, promotion, licensing, and revalidation contracts.

For concept-led level work, also use `design-unreal-worlds-and-levels` and its approved concept interpretation, Area Composition Plan, and Stage 2a source requirements. Do not invent asset demand from an unapproved image interpretation.

## Build concept-led asset readiness

1. Extract functional asset-family demands from approved source requirements and stable zone IDs: hero, structural, transition, contact, traversal, boundary, ecology, material, ordinary dressing, and experience-defining systemic content.
2. Record role, priority, scale, expected use, minimum variation, modular and transition pieces, reverse sides, contacts, visual and technical constraints, acceptance evidence, fallback, owner, budget boundary, and due stage.
3. Inspect project-native content first, then ownership-confirmed team or marketplace libraries. When `fab-library-advisor` is available, use it before proposing a new Fab purchase; treat its results as candidate and ownership evidence only, not compatibility, license, or production approval.
4. Give every gap an explicit reuse, owned-library, new-acquisition, custom-authoring, procedural, outsourcing, substitution, or concept-revision route.
5. Keep `DISCOVERED`, `OWNERSHIP_VERIFIED`, `ACQUIRED_TO_STAGING`, `REPRESENTATIVE_APPROVED`, and `PRODUCTION_APPROVED` distinct. Preserve `REJECTED` and `BLOCKED` candidates with reasons.
6. Evaluate exact candidate versions for family completeness, ordinary repetition, transitions, scale, materials, collision, navigation, rig or skeleton, LOD or Nanite, platform, required plugins, dependencies, storage, streaming, memory, cook, license, integration cost, maintenance, and rollback.

Use the bundled [Concept-to-Asset Readiness Contract schema](references/concept-to-asset-readiness.schema.json) and [starter template](references/concept-to-asset-readiness.template.json), or a project-equivalent typed record that preserves the same semantics.

## Enforce three locks

- Require `ASSET_PLAN_READY` before the level's Experience Prototype. Every demand needs a coverage record, route, owner, budget boundary, due stage, acceptance evidence, and fallback; exact assets may remain planned gaps.
- Require `VISUAL_SLICE_READY` before the Visual Feasibility Slice. Every family needed by that slice must be project-native or staged, entitlement or provenance-resolved, license- and compatibility-checked, and representative-ready.
- Require `PRODUCTION_DRESSING_READY` before production meshing or dressing. Every production-blocking demand must be production-ready or carry an approved concept/scope waiver, and selected candidates, external actions, dependencies, performance, cook, collaboration, replacement, and rollback evidence must pass.

Approval of any design gate does not authorize a purchase, download, install, migration, plugin enablement, outsourcing commitment, upload, or other external mutation. Perform those only when the user explicitly requests the separate action and a safe recovery boundary is defined. Never collect or store credentials, cookies, payment data, private tokens, or secret-bearing URLs.

## Establish ownership and boundaries

1. Identify the source of truth, owner, consumers, and mutation authority for each asset family.
2. Separate authored source, imported packages, generated or derived content, runtime data, project configuration, and disposable intermediates.
3. Define dependency direction and prohibit cycles that make migration or cooking unpredictable.
4. Use naming, folders, and metadata to communicate stable responsibility and readiness rather than temporary task history.
5. Record provenance, entitlement or license evidence, engine and platform compatibility, third-party constraints, and project adaptations.

## Design for reuse and migration

Distinguish:

- project source libraries that may retain project-licensed dependencies;
- portable, dependency-free system contracts;
- distributable content plugins whose complete dependency graph is license-clean.

Default reused or externally acquired systems to revalidation in the new biome, scale, platform, lighting, gameplay, rendering, license, and dependency context. Previous technical, visual, ownership, or marketplace approval does not transfer automatically.

## Validate the lifecycle

Require one current coverage decision per demand; no orphan candidates; explicit external authorization; dependency and redirector checks; representative visual and technical evidence; clean-project or clean-plugin tests when distribution is intended; representative load and cook verification; rollback planning; and ownership review. Confirm that acquisition or migration does not silently change references, configuration, license scope, or runtime behavior.

Leave purchases, downloads, imports, renames, Asset Registry calls, redirects, migrations, plugin enablement, packaging commands, and other Editor or external operations to the appropriate execution layer after the architecture and action authority are approved.
