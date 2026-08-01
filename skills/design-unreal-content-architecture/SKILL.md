---
name: design-unreal-content-architecture
description: Design or review Unreal content and asset architecture, including naming, folders, ownership, dependencies, data assets, reuse, migration, provenance, licensing, and lifecycle. Use before reorganizing Content, sharing systems across projects, packaging reusable assets, or diagnosing dependency and ownership problems. Do not use for an isolated import or Content Browser operation.
---

# Design Unreal Content Architecture

Treat content as versioned production data with ownership and lifecycle, not as a collection of convenient files.

## Load the Handbook chapter

Read [05-content-asset-architecture.md](references/05-content-asset-architecture.md) before reorganizing, reusing, migrating, or distributing content. Apply its ownership, dependency, provenance, promotion, licensing, and revalidation contracts.

## Establish ownership and boundaries

1. Identify the source of truth, owner, consumers, and mutation authority for each asset family.
2. Separate authored source, generated or derived content, runtime data, project configuration, and disposable intermediates.
3. Define dependency direction and prohibit cycles that make migration or cooking unpredictable.
4. Use naming and folders to communicate stable responsibility rather than temporary task history.
5. Record provenance, licensing, engine compatibility, and third-party constraints.

## Design for reuse and migration

Distinguish:

- project source libraries that may retain project-licensed dependencies;
- portable, dependency-free system contracts;
- distributable content plugins whose complete dependency graph is license-clean.

Default reused systems to revalidation in the new biome, scale, platform, lighting, gameplay, and dependency context. Previous technical or visual approval does not transfer automatically.

## Validate the lifecycle

Require dependency and redirector checks, clean-project or clean-plugin tests when distribution is intended, representative load and cook verification, rollback planning, and ownership review. Confirm that migration does not silently change references, configuration, or runtime behavior.

Leave imports, renames, Asset Registry calls, redirects, packaging commands, and other Editor operations to the execution layer after the architecture is approved.
