---
type: decision
case: "104.2"
status: archived
update: ["[[rule-page-generation]]"]
origin: raw/2026-09-13/ledger.md#case-104.2
sprint: migration
created: 2026-09-13
tags: [harness, workflow, ledger]
---

## Context

The outcome of the talk on the archive: a page leaves when it stops describing the present. Today `generate.cascade` (after all entries) computes two things: `built`/`draft` of an Entity or Rule from its Estimates, and the `severity` of an Insight from its live children. `archived` is set by `delete` alone. A Decision a later Case superseded stays `superseded` for good (24 pages); a lesson stays `clustered` after its Insight is `actioned` — the schema promises the archive, nothing does it; an Insight whose children are all withdrawn (case 97: `insight-ledger-hook-reads-only-the-final-text` after case 70) hangs `open`.

## Problem

Three status transitions follow from facts already ratified and must be made by the script, not by hand: superseded → archived, the children of an actioned Insight → archived, an Insight with no live child → archived. Until then the archive is a promise.

## Given

`generate.py:596–605`: a supersedes sets `status: superseded`, `superseded_by`, History `superseded by [[X]]`, clears `deferred_by`. `generate.cascade` (`generate.py:610–655`): `built`/`draft`, the recount of `severity` over children whose status is not `archived`. Statuses: Decision `current | superseded | archived` (`decisions/schema.md`); Lesson `new | clustered | archived`, "Archived when its Insight is `actioned`" (`lessons/schema.md:16`); Insight `open | actioned | archived`, `severity` = live children, `actioned` is not an end — a new lesson returns it to `open`, the older children stay `archived` (`insights/schema.md:17–34`). `rule-synthesis:22–23`: "a lesson is archived only when its Insight was actioned, and that Insight stays live".
**＋** `cleanup` moves everything with `status: archived` (102.2: under the session of the run); lint counts archived slugs as known (`lint.py:451`), `deferred_by` and `[[decision-…]]` in History are refs like any other (`lint.py:21`). A superseded decision is never in a `deferred_by`: the supersedes takes it out.
**＋** Today: 24 decisions `superseded`, 0 Insights `actioned`, 20 lessons `clustered`, `insight-ledger-hook-reads-only-the-final-text` at severity 2 with one archived child (the recount of brief K).
**＋** `rule-page-generation` (two Estimates; 101.1 already puts a block on `estimate-generate-writes`); the text "After all entries: …" (`rule-page-generation.md:59–61`).
**－** A `current` Decision is not touched before the close of the sprint (Slice 5). An `actioned` Insight is not archived. The `## Insight` section of a lesson is case 96, not this one.
**－** `decisions/schema.md`: the `status` row gains "`archived` the moment a later Case supersedes it" — in the `decisions-schema` item of 103.6, no new line.

## Criterion

- [[estimate-generate-writes]] § case 104.2

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-104.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
