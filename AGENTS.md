# Unreal Development Handbook for Codex — Project Guidance

These instructions apply to every task and document in this project. Read [PROJECT_CHARTER.md](PROJECT_CHARTER.md) before creating, revising, reviewing, or researching handbook content. The charter is the authoritative statement of the project's mission, philosophy, scope, and quality standard. Preserve its meaning when extending this file or introducing more local guidance.

## Required reasoning sequence

Think before implementing. Work in this order:

1. Intent
2. Context
3. Requirements
4. Constraints
5. Design
6. Validation Strategy
7. Implementation
8. Verification

Before acting, identify missing goals, assumptions, constraints, success criteria, validation requirements, and production concerns. Ask focused questions only when a missing choice would materially change the result; otherwise state reasonable assumptions explicitly. Define success criteria before implementation and never optimize implementation before validating the design.

## Handbook content standard

The handbook teaches durable professional Unreal Engine development reasoning, not prompts, command collections, or a single tool stack. It may cover architecture, level design, content creation, Blueprint, C++, Python, PCG, Gameplay Framework, asset organization, performance, optimization, validation, teamwork, source control, production pipelines, and AI-assisted development.

Organize handbook content under the canonical structure published in [README.md](README.md):

1. **Foundations** — Philosophy; Development Process; Project & System Architecture.
2. **Game and World Design** — Gameplay Architecture; World & Level Design; Content & Asset Architecture.
3. **Implementation Technologies** — Blueprint; C++; Automation & Python; Procedural Systems & PCG.
4. **Quality and Production** — Rendering; Performance & Scalability; Validation, Testing & Debugging; Production Pipeline; Team Collaboration & Source Control; AI-Assisted Development.
5. **Applied Reasoning** — Case Studies.

Store each canonical chapter in the `references/` directory of the Skill that owns that chapter, and link it from both the owning `SKILL.md` and the root `README.md`. This is the plugin's progressive-disclosure contract: the installed Skill must load only the chapters needed for the request. Do not create a second copy of a chapter in a separate documentation tree.

Treat performance, validation, collaboration, production readiness, and responsible AI use as cross-cutting concerns. Their dedicated chapters define shared principles and systems; every relevant chapter must apply them in its own context. Do not create a detached **Best Practices** catch-all chapter. Place each practice with the decision it governs, explain its trade-offs, and reinforce it through design considerations, validation checklists, implementation examples, and common mistakes.

Keep chapter boundaries conceptual rather than tool-defined. In particular:

- **Gameplay Architecture** owns responsibility, lifecycle, state, data, input, persistence, networking boundaries, and system interaction; it is broader than a Gameplay Framework class reference.
- **Automation & Python** owns automation reasoning and pipeline design; Python is an implementation technology, not the subject's durable center.
- **Procedural Systems & PCG** owns procedural design principles; Unreal PCG is a major application rather than the only possible implementation.
- **Validation, Testing & Debugging** owns the shared quality system but does not replace topic-specific success criteria and verification.
- **Case Studies** must connect decisions to alternatives, evidence, trade-offs, failures, and production outcomes rather than present isolated tutorials.

For each topic, use this order where applicable:

1. Purpose
2. Intent
3. When to Use
4. When NOT to Use
5. Design Considerations
6. Recommended Workflow: Requirements → Planning → Architecture → Validation Plan → Implementation → Verification → Optimization
7. Validation Checklist
8. Implementation Examples
9. Common Mistakes
10. Related Topics

Do not open a technical topic with an API, command, or tool tutorial. Establish intent, context, trade-offs, process, and validation first. Examples come after the reasoning and should not present one implementation method as universally correct.

Validation must consider functional correctness, maintainability, production readiness, performance, edge cases, and failure recovery. State how success is measured, what must be tested, which warnings are acceptable, which warnings expose a design problem, and how failure or rollback is handled when relevant.

## Research and durability

Do more than summarize vendor documentation. Investigate why a subject was designed as it was, its trade-offs, the production problems it solves, remaining limitations, alternatives, and likely evolution. Clearly separate durable principles from version-specific facts and implementation details. Reason about evidence and trade-offs, and cross-link related topics so the handbook becomes a coherent knowledge system.

Guiding principle:

> Development principles remain. Tools evolve.

## Project boundary

Keep **Unreal Development Handbook for Codex** distinct from **Unreal Editor Skills for Codex**:

- The Handbook owns why, when, intent, design, architecture, process, validation, performance and maintainability considerations, best practices, and production reasoning.
- Editor Skills owns how, editor operations, tool and API usage, workflow execution, and concrete MCP/Python/Blueprint/C++ operation mechanics.

Link the projects bidirectionally when useful, but do not duplicate detailed editor-operation instructions here. Treat Epic Unreal MCP, UE-MCP, Python, Blueprint, Editor Utility Widgets, C++, Commandlets, custom plugins, and future automation systems as execution technologies rather than the knowledge itself.

## AI role and long-term test

Help the reader learn how experienced Unreal developers think—not merely how to operate the editor. Guide work through requirements, design, validation, implementation, and verification.

A contribution belongs in this project only if it helps a reader or AI make better professional Unreal development decisions even when the implementation technology changes. Prefer clearer architecture and lower future maintenance cost over premature complexity or short-term implementation speed.
