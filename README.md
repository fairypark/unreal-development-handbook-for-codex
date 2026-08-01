# Unreal Development Handbook for Codex

A living handbook for teaching Codex—and its human readers—how experienced Unreal Engine developers reason about intent, design, architecture, validation, implementation, and verification.

This project preserves durable development principles rather than collecting prompts, commands, or tool-specific recipes. Its central rule is:

> Development principles remain. Tools evolve.

## Start here

- [Project Charter](PROJECT_CHARTER.md) — the authoritative mission, philosophy, writing principles, AI behavior, project boundary, research mindset, and long-term goal.
- [Project Guidance](AGENTS.md) — the operational rules every future Codex task and handbook contribution must follow.

## Handbook structure

The handbook progresses from durable reasoning, through game and world design, into implementation technologies, and finally into production-quality validation and applied examples.

### Part I — Foundations

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 00 | Philosophy | Intent-first, design-first, and validation-first principles; durable reasoning; responsible trade-offs. |
| 01 | Development Process | Requirements, planning, architecture, validation planning, implementation, verification, optimization, and recovery. |
| 02 | Project & System Architecture | System boundaries, dependencies, data flow, lifecycle, modularity, extensibility, and maintainability. |

### Part II — Game and World Design

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 03 | Gameplay Architecture | Gameplay Framework responsibilities, gameplay systems, state, data, input, persistence, networking boundaries, and system interaction. |
| 04 | World & Level Design | Player experience, spatial composition, world structure, streaming, gameplay space, environmental storytelling, and production constraints. |
| 05 | Content & Asset Architecture | Asset organization, naming, ownership, dependencies, data assets, reuse, migration, and content lifecycle. |

### Part III — Implementation Technologies

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 06 | Blueprint | Visual scripting design, responsibility boundaries, communication patterns, maintainability, and appropriate use. |
| 07 | C++ | Native system design, API boundaries, ownership, lifecycle, extensibility, Blueprint integration, and appropriate use. |
| 08 | Automation & Python | Automation strategy, repeatability, batch workflows, pipeline integration, failure handling, and Python as one implementation option. |
| 09 | Procedural Systems & PCG | Procedural design principles, determinism, authorial control, data flow, scalability, validation, and PCG-specific applications. |

### Part IV — Quality and Production

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 10 | Rendering | Visual goals, rendering architecture, content implications, platform constraints, quality trade-offs, and verification. |
| 11 | Performance & Scalability | Performance budgets, measurement, bottleneck reasoning, scalability policy, optimization priorities, and regression prevention. |
| 12 | Validation, Testing & Debugging | Success criteria, validation strategy, testing layers, diagnostics, acceptable warnings, regressions, recovery, and rollback. |
| 13 | Production Pipeline | Content flow, builds, cooking, packaging, deployment, automation boundaries, release readiness, and operational resilience. |
| 14 | Team Collaboration & Source Control | Ownership, communication, review, source-control strategy, asset conflicts, integration, documentation, and team-scale workflows. |
| 15 | AI-Assisted Development | Appropriate AI roles, context and constraint management, human oversight, evidence, validation, reproducibility, and failure containment. |

### Part V — Applied Reasoning

| No. | Chapter | Responsibility |
| --- | --- | --- |
| 16 | Case Studies | End-to-end decisions, alternatives, trade-offs, validation evidence, production outcomes, failures, and lessons learned. |

Performance, validation, collaboration, production readiness, and responsible AI use are cross-cutting concerns. Their dedicated chapters define shared principles and systems, while every relevant technical chapter applies those concerns locally. Best practices are likewise taught in context through design considerations, validation checklists, implementation examples, and common mistakes rather than collected in a detached catch-all chapter.

The handbook and **Unreal Editor Skills for Codex** are complementary but separate: this project owns the theory and professional reasoning behind development decisions; Editor Skills owns concrete editor and tool execution. Detailed handbook chapters will be added only as later work establishes their intent, scope, evidence, validation criteria, and place in the broader knowledge system.
