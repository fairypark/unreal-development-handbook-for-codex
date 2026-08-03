# Unreal Development Handbook for Codex

A living handbook for teaching Codex—and its human readers—how experienced Unreal Engine developers reason about intent, design, architecture, validation, implementation, and verification.

This project preserves durable development principles rather than collecting prompts, commands, or tool-specific recipes. Its central rule is:

> Development principles remain. Tools evolve.

## Start here

- [Project Charter](PROJECT_CHARTER.md) — the authoritative mission, philosophy, writing principles, AI behavior, project boundary, research mindset, and long-term goal.
- [Project Guidance](AGENTS.md) — the operational rules every future Codex task and handbook contribution must follow.
- [License](LICENSE) and [third-party notices](THIRD_PARTY_NOTICES.md) — distribution terms and migrated-source attribution.

## Codex plugin and skills

This repository is also a Codex plugin. The canonical chapter files live in each owning Skill's `references/` directory so installed Codex tasks can load only the relevant Handbook content. Runtime Skills adapt the chapter structure to common user requests without turning the handbook into an Editor-control package:

| Skill | Handbook responsibility |
| --- | --- |
| `reason-about-unreal-development` | Chapters 00–02: intent, process, architecture, and cross-domain routing. |
| `design-unreal-gameplay-architecture` | Chapter 03: gameplay responsibilities, state, lifecycle, data flow, persistence, and networking boundaries. |
| `design-unreal-worlds-and-levels` | Chapter 04: player experience, spatial composition, world structure, gameplay space, and environment production. |
| `design-unreal-content-architecture` | Chapter 05: asset ownership, dependencies, reuse, migration, and lifecycle. |
| `design-unreal-blueprint-and-cpp` | Chapters 06–07: Blueprint and C++ responsibilities, APIs, ownership, lifecycle, and integration. |
| `design-unreal-automation-and-pcg` | Chapters 08–09: repeatable automation, Python as an option, determinism, authorial control, and procedural systems. |
| `validate-unreal-production` | Chapters 10–14: rendering, performance, validation, production pipeline, collaboration, and source control. |
| `guide-unreal-ai-development` | Chapter 15: AI roles, oversight, evidence, reproducibility, and failure containment. |
| `analyze-unreal-development-cases` | Chapter 16: evidence-backed cases, failures, outcomes, and transferable lessons. |

World and level workflows also include a machine-readable [Reference-to-Prototype Translation Contract schema](skills/design-unreal-worlds-and-levels/references/reference-to-prototype-translation.schema.json) and [starter template](skills/design-unreal-worlds-and-levels/references/reference-to-prototype-translation.template.json). They implement the blocking Stage 2a handoff between an approved Area Composition Plan and the first content-bearing prototype placement; project-specific formats may replace them only when they preserve the same identifiers, authority, traceability, evidence, and reopening semantics.

Validate the bundled contract assets and semantic gate rules with:

```powershell
uv run --with jsonschema python -m unittest discover -s tests -v
uv run --with jsonschema python scripts/validate_reference_to_prototype_contract.py skills/design-unreal-worlds-and-levels/references/reference-to-prototype-translation.template.json
```

The Skills provide reasoning and validation contracts. They do not bundle MCP servers, Editor hooks, Unreal operations, or implementation-specific tool instructions. When concrete Editor work is requested, use the independently installable **Unreal Editor Skills for Codex** execution layer after the relevant Handbook Skill has established intent, design, constraints, and success criteria.

Installing this plugin is not required to author the handbook inside this repository, where `AGENTS.md` supplies project guidance. Installation makes the Skills discoverable in other Codex projects and tasks.

## Install

The Fairypark marketplace catalogs both this reasoning plugin and the independent Editor execution plugin:

```powershell
codex plugin marketplace add fairypark/unreal-editor-skills-for-codex
codex plugin add unreal-development-handbook-for-codex@fairypark
```

Fully quit and restart the Codex or ChatGPT desktop app, then start a new task so the installed Skills are discovered. To pair design reasoning with live Editor execution, also install:

```powershell
codex plugin add unreal-editor-skills-for-codex@fairypark
```

The plugins have no runtime dependency on each other. When both are present, Handbook Skills establish intent, architecture, constraints, and validation evidence before Editor Skills execute operations. When only the Handbook is present, it produces decision-ready plans without attempting Editor control. When only Editor Skills is present, its environment workflow uses a compact fallback contract rather than failing.

To update an existing installation:

```powershell
codex plugin marketplace upgrade fairypark
codex plugin add unreal-development-handbook-for-codex@fairypark
```

## Handbook structure

The handbook progresses from durable reasoning, through game and world design, into implementation technologies, and finally into production-quality validation and applied examples.

### Part I — Foundations

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 00 | [Philosophy](skills/reason-about-unreal-development/references/00-philosophy.md) | Intent-first, design-first, and validation-first principles; durable reasoning; responsible trade-offs. |
| 01 | [Development Process](skills/reason-about-unreal-development/references/01-development-process.md) | Requirements, planning, architecture, validation planning, implementation, verification, optimization, and recovery. |
| 02 | [Project & System Architecture](skills/reason-about-unreal-development/references/02-project-system-architecture.md) | System boundaries, dependencies, data flow, lifecycle, modularity, extensibility, and maintainability. |

### Part II — Game and World Design

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 03 | [Gameplay Architecture](skills/design-unreal-gameplay-architecture/references/03-gameplay-architecture.md) | Gameplay Framework responsibilities, gameplay systems, state, data, input, persistence, networking boundaries, and system interaction. |
| 04 | [World & Level Design](skills/design-unreal-worlds-and-levels/references/04-world-level-design.md) | Player experience, spatial composition, world structure, streaming, gameplay space, environmental storytelling, and production constraints. |
| 05 | [Content & Asset Architecture](skills/design-unreal-content-architecture/references/05-content-asset-architecture.md) | Asset organization, naming, ownership, dependencies, data assets, reuse, migration, and content lifecycle. |

### Part III — Implementation Technologies

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 06 | [Blueprint](skills/design-unreal-blueprint-and-cpp/references/06-blueprint.md) | Visual scripting design, responsibility boundaries, communication patterns, maintainability, and appropriate use. |
| 07 | [C++](skills/design-unreal-blueprint-and-cpp/references/07-cpp.md) | Native system design, API boundaries, ownership, lifecycle, extensibility, Blueprint integration, and appropriate use. |
| 08 | [Automation & Python](skills/design-unreal-automation-and-pcg/references/08-automation-python.md) | Automation strategy, repeatability, batch workflows, pipeline integration, failure handling, and Python as one implementation option. |
| 09 | [Procedural Systems & PCG](skills/design-unreal-automation-and-pcg/references/09-procedural-systems-pcg.md) | Procedural design principles, determinism, authorial control, data flow, scalability, validation, and PCG-specific applications. |

### Part IV — Quality and Production

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 10 | [Rendering](skills/validate-unreal-production/references/10-rendering.md) | Visual goals, rendering architecture, content implications, platform constraints, quality trade-offs, and verification. |
| 11 | [Performance & Scalability](skills/validate-unreal-production/references/11-performance-scalability.md) | Performance budgets, measurement, bottleneck reasoning, scalability policy, optimization priorities, and regression prevention. |
| 12 | [Validation, Testing & Debugging](skills/validate-unreal-production/references/12-validation-testing-debugging.md) | Success criteria, validation strategy, testing layers, diagnostics, acceptable warnings, regressions, recovery, and rollback. |
| 13 | [Production Pipeline](skills/validate-unreal-production/references/13-production-pipeline.md) | Content flow, builds, cooking, packaging, deployment, automation boundaries, release readiness, and operational resilience. |
| 14 | [Team Collaboration & Source Control](skills/validate-unreal-production/references/14-team-collaboration-source-control.md) | Ownership, communication, review, source-control strategy, asset conflicts, integration, documentation, and team-scale workflows. |
| 15 | [AI-Assisted Development](skills/guide-unreal-ai-development/references/15-ai-assisted-development.md) | Appropriate AI roles, context and constraint management, human oversight, evidence, validation, reproducibility, and failure containment. |

### Part V — Applied Reasoning

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 16 | [Case Studies](skills/analyze-unreal-development-cases/references/16-case-studies.md) | End-to-end decisions, alternatives, trade-offs, validation evidence, production outcomes, failures, and lessons learned. |

Performance, validation, collaboration, production readiness, and responsible AI use are cross-cutting concerns. Their dedicated chapters define shared principles and systems, while every relevant technical chapter applies those concerns locally. Best practices are likewise taught in context through design considerations, validation checklists, implementation examples, and common mistakes rather than collected in a detached catch-all chapter.

The handbook and **Unreal Editor Skills for Codex** are complementary but separate: this project owns the theory and professional reasoning behind development decisions; Editor Skills owns concrete editor and tool execution. The bundled chapters are a durable foundational edition distilled from the current project charter and reusable Editor Skills knowledge. Future research should deepen version-sensitive topics and replace candidate case studies only when source evidence is available.
