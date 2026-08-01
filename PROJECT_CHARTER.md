# Unreal Development Handbook for Codex — Project Charter

## Project Mission

This project is a living handbook that teaches Codex how experienced Unreal Engine developers think, design, validate, and implement professional Unreal projects.

It is not a collection of prompts or Unreal Engine commands, and it is not tied to any single implementation technology. Its purpose is to preserve development principles that remain valuable even when tools, AI models, Unreal Engine versions, or automation systems change.

The handbook should cover professional Unreal Engine development, including architecture, level design, content creation, Blueprint design, C++, Python, PCG, Gameplay Framework, asset organization, performance, optimization, validation, teamwork, source control, production pipelines, and AI-assisted development.

## Core Philosophy

Think before implementing.

Every solution must begin by understanding the problem. Use this order:

1. Intent
2. Context
3. Requirements
4. Constraints
5. Design
6. Validation Strategy
7. Implementation
8. Verification

Implementation is the last major step.

Tools are implementations, not knowledge. Epic Unreal MCP, UE-MCP, Python, Blueprint, Editor Utility Widgets, C++, Commandlets, and custom plugins are execution technologies. The handbook must explain why and when a technique is appropriate before explaining how to implement it.

Development principles must outlive tools. The handbook should remain useful if MCP implementations disappear or change, Codex changes, another AI becomes the primary client, or Unreal Engine introduces new automation systems.

Guiding principle:

> Development principles remain. Tools evolve.

## Design-first Principle

Never optimize implementation before validating the design.

Prefer:

- improving architecture over adding complexity;
- reducing future maintenance cost over saving implementation time now;
- clarifying intent, requirements, constraints, assumptions, and success criteria before execution.

Do not jump directly into tools or code when essential design information is missing. Ask focused clarification questions when a missing choice would materially change the result; otherwise state reasonable assumptions explicitly.

## Validation-first Principle

Define success criteria before implementation begins.

Successful execution is not the same as successful development. Validation must cover:

- functional correctness;
- maintainability;
- production readiness;
- performance;
- edge cases;
- failure recovery.

Every topic and implementation should say how success will be measured, what must be tested, which warnings are acceptable, which warnings signal a design problem, and how failure or rollback will be handled where relevant.

## Writing Principles

Every handbook topic should answer, in an appropriate order:

1. **Purpose** — Why does this technology or practice exist? What problem does it solve?
2. **Intent** — What is the developer actually trying to achieve?
3. **When to Use** — In which contexts is it appropriate?
4. **When NOT to Use** — When are alternatives better?
5. **Design Considerations** — Scalability, maintainability, performance, collaboration, production risk, and extensibility.
6. **Recommended Workflow** — Requirements → Planning → Architecture → Validation Plan → Implementation → Verification → Optimization.
7. **Validation Checklist** — Objective evidence that the result works and is production-appropriate.
8. **Implementation Examples** — Only after the preceding sections; multiple approaches are encouraged.
9. **Common Mistakes** — Why they happen, how to detect them, and how to prevent them.
10. **Related Topics** — Connect the handbook as a knowledge graph rather than isolated articles.

Do not begin a new technical topic with an API, command, or tool tutorial. Explain intent, context, trade-offs, process, and validation first. No single implementation method should be treated as universally correct.

## AI Behavior

For every request, first identify whether important information is missing:

- goals;
- assumptions;
- constraints;
- success criteria;
- validation requirements;
- production concerns.

Prefer clarification or explicit assumptions over immediate implementation when those missing details matter. Reason about trade-offs rather than simply restating vendor documentation. Analyze why a technology was designed as it was, what production problem it solves, its limitations, alternatives, and likely evolution.

The AI should help the user learn Unreal development thinking—not merely operate the editor. It should guide the user through requirements, design, validation, implementation, and verification.

## Relationship with “Unreal Editor Skills for Codex”

Keep the two projects distinct and independently valuable.

**Unreal Development Handbook for Codex** owns:

- Why;
- When;
- Intent;
- Design;
- Architecture;
- Process;
- Validation;
- Performance and maintainability considerations;
- Best practices and production reasoning.

**Unreal Editor Skills for Codex** owns:

- How;
- Editor operations;
- Tool usage;
- API usage;
- Workflow execution;
- concrete MCP/Python/Blueprint/C++ operation mechanics.

The Handbook is the theory/reasoning layer; Editor Skills is the execution/practice layer. Link them bidirectionally when useful: Handbook topics may point to relevant Editor Skills implementation guidance, while Editor Skills may point back to the Handbook for design context. Do not duplicate detailed editor-operation instructions in the Handbook.

## Research Mindset

Do not merely summarize documentation. For each subject, investigate and explain:

- Why was it designed this way?
- What trade-offs does it make?
- What production problems does it solve?
- What limitations remain?
- How does it compare with alternatives?
- How might it evolve in future Unreal Engine versions?

Separate durable principles from version-specific facts and implementation details.

## Long-term Goal

The final objective is not an Unreal Engine manual. It is a durable handbook that teaches AI to think like an experienced Unreal Engine developer.

A reader or AI that studies the handbook should make better design decisions even if the implementation technology changes completely. Over time, the project should become a coherent, cross-linked knowledge system for professional Unreal development rather than a loose collection of prompts, recipes, or command references.

## Charter Governance

This file is the authoritative foundation for the project. All project guidance, research, topic outlines, reviews, and future handbook content must remain consistent with it. More specific guidance may add detail but must not silently weaken or contradict this charter.

When the charter itself changes, update project-level guidance and entry-point documentation in the same change, review the boundary with Unreal Editor Skills for Codex, and record any intentional shift in mission or quality standards explicitly.
