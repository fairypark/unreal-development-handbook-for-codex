---
name: guide-unreal-ai-development
description: Design or review AI-assisted Unreal development workflows through role boundaries, context and constraint management, human oversight, evidence, reproducibility, independent evaluation, failure containment, and durable project knowledge. Use when agents plan, implement, mutate, review, approve, or learn from Unreal work. Do not use to control the Editor or configure a specific model or MCP server.
---

# Guide Unreal AI Development

Use AI as a bounded development participant whose decisions and outputs remain inspectable, reproducible, and subject to evidence.

## Load the Handbook chapter

Read [15-ai-assisted-development.md](references/15-ai-assisted-development.md) before defining agent roles, context, mutation authority, evidence, evaluation, approval, or failure containment.

## Enforce domain workflows

When the relevant Handbook chapter defines an explicit workflow, treat its stages and gates as part of the mutation contract. For level or world creation, load Chapter 04 and require its ordered workflow record, stage evidence, promotion decision, stop conditions, and rollback behavior; never let a Tool result or agent confidence replace a required gate. Area Composition Plan `PASS` advances only to Stage 2a Reference-to-Prototype Translation. Do not authorize content-bearing prototype placement until the machine-readable source registry, quantitative zone contracts, traceability map, comparison tolerances, and explicit placement decision pass. Then require Stage 2b Concept-to-Asset Readiness: `ASSET_PLAN_READY` before the Experience Prototype, `VISUAL_SLICE_READY` before the representative slice, and `PRODUCTION_DRESSING_READY` before production meshing or dressing.

## Define AI responsibilities

1. State the agent's role, allowed mutations, decision authority, and stop conditions.
2. Provide goals, constraints, project context, success criteria, and production concerns without leaking a desired verdict.
3. For complex graph or data work, establish a reference-grounded context set before mutation: approved examples, source authority and version, bounded context slices, unresolved unknowns, and reviewer questions.
4. Separate builder, reviewer, and approval authority when independence matters.
5. Keep evaluators read-only and give them raw artifacts, neutral facts, and the applicable rubric.
6. Require human approval for materially destructive, external, high-risk, or policy-sensitive actions.

## Protect reliability

- Treat Tool and transport success as evidence of execution only.
- Require postconditions for project state, assets, behavior, performance, persistence, and recovery.
- After every composition-changing level batch, lock the next broad batch until the Stage 2a contract records same-condition reference/plan/prototype deviations and resolves every out-of-tolerance result or reopens the responsible stage.
- Treat a marketplace search hit as discovery, an authenticated library match as ownership evidence, a staged package as acquisition evidence, and representative or production approval as separate validation states. Never infer purchase, download, install, migration, plugin enablement, outsourcing, upload, or payment authority from a design request or readiness gate.
- Preserve failed attempts and factual change scope.
- Treat reference retrieval, semantic matching, or context truncation as context preparation—not as evidence; plan before mutation and execute complex work in incremental reviewable batches.
- Prevent the builder from manufacturing or rewriting approval evidence.
- Use deterministic scripts for fragile repeated mechanics while keeping contextual judgment explicit.
- Label self-review honestly when independent review is unavailable.

## Preserve durable knowledge

Store project knowledge that tools cannot infer, such as ownership, naming, folder rules, setup constraints, and canonical workflows. Keep it concise, versioned, and resilient to Tool or model changes. Separate general Handbook principles from project-specific coordinates, asset paths, private infrastructure, and temporary workarounds.

When live work is requested, pass the approved role and validation contract to the available Editor or coding layer. Do not encode current model names, host orchestration, or MCP schemas as durable development knowledge.
