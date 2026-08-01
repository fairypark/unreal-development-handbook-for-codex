# 00 — Philosophy

## Purpose

Establish the durable reasoning principles that should govern Unreal development even when the Editor, APIs, automation layer, AI client, or project scale changes.

## Intent

Optimize for a correct, maintainable, production-appropriate outcome rather than the fastest visible implementation. Treat tools as execution options and successful commands as evidence of activity, not proof that development succeeded.

## Core principles

### Intent before implementation

Understand the player, creator, team, or operational outcome before selecting a class, graph, Tool, or workflow. A clear implementation of the wrong intent remains a failure.

### Design before optimization

Validate responsibility, ownership, lifecycle, data flow, spatial structure, and recovery before investing in optimization or automation. Improve architecture before adding compensating complexity.

### Validation before confidence

Define success criteria and evidence before implementation. A save, compile, generated point count, or successful Tool response proves only its narrow postcondition.

### Principles outlive tools

Blueprint, C++, Python, PCG, Editor utilities, MCP, Commandlets, and future systems are implementation technologies. Prefer knowledge that remains useful when those technologies change.

### Quality is multi-dimensional

Functional correctness, visual quality, performance, maintainability, collaboration, production readiness, edge cases, and failure recovery may all matter. Do not hide one failed dimension inside an average.

### Reversibility is a design property

Choose checkpoints, ownership boundaries, migration plans, and recovery paths before difficult-to-undo work. A fast workflow without a truthful rollback strategy creates production risk.

## Responsible trade-offs

State what a design improves and what it sacrifices. Compare alternatives on the same constraints. Avoid presenting project preferences, current Tool limitations, or a single successful anecdote as universal best practice.

## Validation checklist

- Is the desired outcome explicit?
- Are assumptions separated from requirements?
- Are ownership and lifecycle clear?
- Are success and failure observable?
- Are performance and production constraints represented?
- Can the design recover or roll back?
- Would the reasoning remain useful with a different Tool stack?

## Common mistakes

- Starting from a familiar API instead of the problem.
- Treating technical neatness as proof of player or production value.
- Automating a design that has not passed a representative test.
- Lowering acceptance criteria after seeing weak results.
- Confusing a current engine limitation with a permanent principle.

## Related topics

Development Process; Project & System Architecture; Validation, Testing & Debugging; AI-Assisted Development.
