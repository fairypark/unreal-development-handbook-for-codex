# 14 — Team Collaboration & Source Control

## Purpose

Coordinate people, agents, assets, code, reviews, and integration so ownership and recovery remain clear as an Unreal project scales.

## Intent

Reduce hidden work, conflicting authority, asset contention, irreversible edits, and review ambiguity without replacing communication with process overhead.

## Ownership model

Assign owners for systems, content families, generated outputs, configuration, validation evidence, and release approval. Separate builder, reviewer, and final approval authority when independence or risk requires it.

## Source-control strategy

- Create recovery points before bulk, multi-asset, or difficult-to-undo changes.
- Keep changes scoped to one coherent decision where practical.
- Inspect exact files before staging, review generated and binary content deliberately, and preserve unrelated user work.
- Define locking or ownership policy for assets that cannot merge safely.
- Keep project-specific configuration, generated files, and caches under an intentional source-control policy.
- Integrate frequently enough to expose dependency and ownership conflicts before final delivery.

## Review contract

Provide intent, constraints, factual change scope, evidence, affected owners, migration notes, and known risks. Review responsibility, lifecycle, dependencies, failure paths, production impact, and validation—not just visible diff size or effort.

Resolve disagreement with corrected evidence, a verified false premise, or an explicit product decision. Do not silently override a failed gate, rewrite review history, or pressure an evaluator with the intended verdict.

## Documentation and knowledge

Record durable naming, folder, ownership, setup, and workflow rules where future contributors and agents can discover them. Keep private paths, credentials, temporary machine details, and incidental project anecdotes out of reusable guidance.

## Validation checklist

- Every changed system and asset family has an owner.
- Recovery and integration boundaries are known.
- Binary and generated assets follow the agreed policy.
- Reviewers receive comparable evidence and neutral context.
- Source-control status contains no unintended or secret-bearing files.
- Handoff records remaining work and unresolved risk truthfully.

## Related topics

Project & System Architecture; Content & Asset Architecture; Production Pipeline; AI-Assisted Development.
