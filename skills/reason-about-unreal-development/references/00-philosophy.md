# 00 — Philosophy

## Purpose

Establish the durable reasoning principles that should govern Unreal development even when the Editor, APIs, automation layer, AI client, or project scale changes.

## Decision contrast: Outcome before procedural confidence

**Evidence class:** constructed teaching scenario; no measured production outcome is claimed.

**Situation.** Two environment workflows finish their promised batches. Both save successfully; one still leaves the intended walking experience empty and unreadable.

**Choice and reason.** Choose the next action by the unsatisfied outcome. Revisit spatial hierarchy and the route hypothesis before polishing already grounded details. Successful local work narrows an implementation risk; it cannot establish that the place is worth exploring.

**When the choice changes.** An intentionally sparse contemplative vista can satisfy a different brief. Do not infer that every empty view needs more objects, or that more activity means better work.

**Smallest useful test.** Use the representative player view and one short approach to a destination. Ask what invites movement, what changes along the way, and what pays off arrival. Keep the direction provisional until observed.

## Intent

Optimize for a correct, maintainable, production-appropriate outcome rather than the fastest visible implementation. Treat tools as execution options and successful commands as evidence of activity, not proof that development succeeded.

## Core principles

### Learn judgment from cases first

Use cases to learn which problem matters, why a choice changes the outcome, and when the same choice becomes wrong. This is the handbook's first priority. A rule is useful when it supports that judgment; quoting the rule or completing its checklist does not demonstrate understanding.

For the consequential decision, connect **intent → observation → competing explanations → alternatives → contextual choice → smallest test**. Use a relevant retained case or a clearly labeled teaching contrast. State the mechanism being transferred, a context difference that could reverse the recommendation, and the observation that would change your mind. When no suitable precedent exists, name the uncertainty and use a reversible experiment.

Reuse the current brief, stage, and evidence record. This is not an additional approval stage, mandatory research cycle, or form. Detailed safety and promotion contracts still govern the operation they protect. Judge this teaching through [unfamiliar decision scenarios](../../validate-unreal-production/references/judgment-evaluation.md), separately from structural document tests. A [Korean review](case-based-judgment.ko.md) covers this principle and the domain contrasts.

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

When technically correct work still fails the intended experience, reopen the problem at the scale where it fails. Local measurements cannot settle whole-system responsibility, world composition, player experience, or production viability. Prefer the next experiment that separates likely causes over the next task that is easiest to automate. Keep a failed result visible while deciding what to change.

## Validation checklist

- Can the reader identify the consequential decision, explain a relevant case's mechanism, and change the recommendation when its assumptions no longer hold?
- Is the smallest proposed test capable of disproving the recommendation, with teaching examples kept separate from observed outcomes?
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
