---
type: decision
case: "133"
status: current
update: [insights-schema-yaml]
origin: raw/2026-09-14/1229/ledger.md#case-133
sprint: migration
created: 2026-09-14
tags: []
---

## Context

Case 124.3 added a `deferred_by` row to `insights/schema.md` (no; a list of decision slugs; the `defer` decisions that postponed the Insight, set by `generate`, cleared by a `supersedes`). Lint requires `schema.md` and `schema.yaml` to agree, so Work Mode of session N added `deferred_by` to `optional` of `schema.yaml` with a two-line comment — commit `a5dc64e`, outside every `then` block. The brief raised it as a Flag: ratify or revert.

## Problem

The line lives in a Rule-class file and nobody signed it. A revert breaks lint and `generate` (124.2 writes `deferred_by` on an Insight at a `defer`; Case 129 already did). A signature after the fact is the one path on which the chain 124.2 → 124.3 → yaml agrees.

## Given

`vault/wiki/insights/schema.yaml` at HEAD: `optional: [addressed_by, deferred_by]` and the comment "`deferred_by`: the `defer` decisions that postponed the Insight; set by `generate`, cleared by a `supersedes` (case 124.2)".
**＋** `rules/schema.yaml` and `entities/schema.yaml` carry the same line with the same comment, signed by Case 52.3.
**＋** `guppi lint` today: 74 findings, none on `insights/schema` — md and yaml agree.
**＋** Slug precedent: `decisions-schema-yaml`, `rules-schema-yaml`, `estimates-schema-yaml` (Cases 31.1, 52.3, 72.2) — here `insights-schema-yaml`.
**－** `generate` already leans on the line: `decision-case-129` stands in `deferred_by` of two Rule pages, and any future `defer` with an Insight as target writes the field on the Insight.

## History

- 2026-09-14 created · raw/2026-09-14/1229/ledger.md#case-133
