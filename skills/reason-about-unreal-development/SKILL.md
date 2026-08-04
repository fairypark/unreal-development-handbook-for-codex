---
name: reason-about-unreal-development
description: Frame, plan, or review Unreal Engine development work before implementation. Use for vague or cross-cutting Unreal feature requests, architecture choices, requirement gaps, design reviews, implementation plans, validation plans, recovery plans, or questions about why and when an approach fits. Do not use as a substitute for live Unreal Editor operations.
---

# Reason About Unreal Development

Turn an Unreal request into a decision-ready development contract before selecting tools or writing implementation.

## Load the Handbook chapters

- Read [00-philosophy.md](references/00-philosophy.md) for every request handled by this Skill.
- Also read [01-development-process.md](references/01-development-process.md) for planning, execution sequencing, iteration, recovery, or definitions of done.
- Also read [02-project-system-architecture.md](references/02-project-system-architecture.md) for ownership, dependencies, lifecycle, data flow, modularity, APIs, or extensibility.
- Load only the chapters relevant to the request; do not restate the entire Handbook.

## Establish the decision

Work in this order:

1. State the user intent and desired player, creator, or production outcome.
2. Record relevant project context and existing-system boundaries.
3. Separate requirements from preferences and assumptions.
4. Identify constraints: platform, performance, schedule, team, content, compatibility, and recovery.
5. Compare viable designs and their trade-offs.
6. Define success criteria and validation evidence before implementation.
7. Choose implementation technologies only after the design is defensible.
8. Verify the result against the original intent, not merely successful execution.

Ask a focused question only when a missing choice would materially change the design. Otherwise state a reversible assumption and continue.

For a local change to an already accepted prototype, classify the request as `BOUNDED_PROTO_EDIT` before reopening a new design review. Apply the bounded contract in [01-development-process.md](references/01-development-process.md) and the world-specific entry/exit contract in [04-world-level-design.md](../design-unreal-worlds-and-levels/references/04-world-level-design.md): reuse stable predecessor evidence, keep operation and promotion verdicts separate, and return to the full workflow when protected scope or plan assumptions change. This classification reduces scope-matched gates; it does not authorize Editor mutation or production promotion.

## Route to the relevant reasoning domain

- Use gameplay architecture guidance for responsibility, state, input, persistence, networking, and system interaction.
- Use world and level guidance for spatial experience, routes, terrain, streaming, environmental storytelling, and playable structure.
- Use content architecture guidance for concept-led asset demand, owned-library and sourcing plans, acquisition readiness, ownership, dependencies, reuse, migration, and asset lifecycle.
- Use Blueprint and C++ guidance for implementation boundaries and maintainability.
- Use automation and procedural guidance for repeatability, determinism, batch behavior, and PCG.
- Use production validation guidance for rendering, performance, tests, release readiness, recovery, and collaboration.
- Use AI-development guidance when agents create, mutate, review, or approve work.

## Produce a decision-ready result

Report:

- intent and context;
- confirmed requirements and explicit assumptions;
- constraints and risks;
- selected design and rejected alternatives;
- validation plan and failure conditions;
- implementation options without treating one tool as universally correct;
- verification and recovery plan;
- unresolved decisions.

Keep execution separate. When live Editor work is requested, hand the approved contract to an available Editor-operation skill or tool layer and require postcondition evidence.
