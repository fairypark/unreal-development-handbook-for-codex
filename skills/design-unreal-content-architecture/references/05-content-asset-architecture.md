# 05 — Content & Asset Architecture

## Purpose

Give Unreal content explicit ownership, dependency direction, provenance, lifecycle, and reuse boundaries so projects can migrate, cook, collaborate, and distribute safely.

## Intent

Treat assets as versioned production data rather than convenient files. Make their source, owner, consumers, dependencies, allowed mutations, and promotion state discoverable.

## Content layers

Separate authored source, generated or derived content, runtime data, configuration, caches, and disposable intermediates. Use naming and folders to communicate stable responsibility rather than a temporary task or contributor.

## Reuse and distribution model

Distinguish three layers:

1. **Project source library:** exact approved assets with project-licensed dependencies and evidence.
2. **Portable system contract:** dependency-free roles, inputs, outputs, exclusions, parameters, and validation requirements.
3. **Distributable content plugin:** actual assets whose complete dependency graph is declared, license-clean, and tested outside the source project.

Previous approval does not transfer automatically. Default reused systems to revalidation for the new scale, biome, platform, lighting, gameplay, content substitutions, and dependency context.

## Promotion contract

Record stable identity and version, owner, source, approval scope, direct and transitive dependencies, replaceable inputs, project-specific data, collision and navigation intent, rejected predecessors, and current revalidation state. Successful generation, saving, or high instance count is not sufficient promotion evidence.

## Migration workflow

1. Inventory references and dependency direction.
2. Classify ownership, license, and compatibility.
3. Isolate a representative migration set.
4. Define redirect, rename, version, and rollback strategy.
5. Migrate without silently changing configuration or authority.
6. Verify loading, references, cook, runtime behavior, and representative visuals.
7. Revalidate the destination context before broad migration.

## Validation checklist

- No unexpected hard or circular dependencies.
- Source and generated assets are distinguishable.
- Redirectors and stale references are resolved intentionally.
- Licenses allow the intended distribution.
- A clean project or declared-dependency environment loads and cooks the package.
- Private paths, credentials, user data, and project-only coordinates are absent from portable artifacts.
- Ownership and recovery remain clear after migration.

## Related topics

Project & System Architecture; Production Pipeline; Team Collaboration & Source Control; Case Studies.
