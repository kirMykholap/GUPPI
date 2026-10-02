---
type: decision
case: "451.9"
status: current
update: ["[[rule-carry-over]]", "[[estimate-carry-over-writes]]"]
origin: raw/2026-09-27/1255/ledger.md#case-451.9
sprint: migration
created: 2026-09-27
tags: [session, workflow, harness, render]
---

## Context

A Frontier line closes with a box and a closer, which is the last segment after ` · `. Today an item is put off in three ways, and each leaves a different trace:
- A sprint item passed over closes `[-] … · sprint`. It gets no Case, and `generate` moves it to the sprint page's `## Backlog` after three such sessions in a row.
- A decision put off closes `[-] … · defer case N`, with a short-form Case and `deferred_by` on its page.
- An item of the brief's Deferred list left as it stands closes `[-] … · deferred · kept`, and the brief carries it on.

`prespec.check_frontier` ties the box to the closer only for `sprint` and `kept`. So in session 2300 a brief item could take the closer `sprint` and pass. The brief's Deferred list holds at most seven items, and an item cut off the seven drops out of sight. A Spec conserved by `carry` stands only in the brief that `carry` writes.
The person decided one standard:
- `[x]` is an item ended: `case N` when decided, `work` when done with no decision.
- `[-]` is an item put off: `· sprint · defer` for a sprint item, with no Case, as case 356.2 set; `· backlog · kept` for a backlog item left as it stands, with no Case; `· defer case N` for a new decision put off.
- The check ties the box, the closer and the source in both directions.
- `vault/wiki/backlog.md` holds every deferred item. `guppi backlog` writes it, under a new rule `rule-backlog`. It holds the conserved Specs with their targets, and a line for each page with `deferred_by`, each open Insight and each line of the sprint page's `## Backlog`, with its `purpose` and a count of the sessions that put it off.
- `sprint.md` stops showing `## Backlog`.
- The brief drops its Deferred list and its cap.
- `/hi` loads the backlog. The Frontier writes the backlog's count, names the backlog items near a Frontier item, and puts each conserved Spec first under `## Cases`.
- Open Insights compete for nothing: they stand in the backlog like any other item.
- The librarian and `carry` run `guppi backlog`, and `make lint` runs its `--check`.

The vault query found no page that holds every deferred item. The near pages are `rule-sprint` and `rule-brief`. `rule-vault-layout` requires a rule that names the new file, and `rule-one-judgment-one-implementation` requires the count to use the Frontier reader of the sprint move. The new slugs are free and the tags exist.
Beyond the agreed sub-cases, the frame and pre-spec added these: `rule-internal-context` (451.12), `rule-documentation` (451.13), `rule-harness` (451.14), and the Estimate of the rendered schema of Insights (451.15), each with the Estimate that speaks of it.
These stand, for the reasons given:
- `case-schema.md` and the Purpose of `rule-skill-hi` name what `/hi` loads without `backlog.md`, and so does the Criterion of `estimate-hi-no-read-calls`. None of them claims the list is complete. The `Given:` list of `estimate-vault-layout-holds` gives examples.
- `estimate-orchestration-defers-in-one-reply` speaks of `· defer case N`, which stays.
- `estimate-case-protocol-loaded` promises only that the file equals its Render.

This session's Frontier closes with the old closers, because the new check is built in Work Mode. Frontier files of earlier sessions are not rewritten.

## Problem

An item is put off in three ways with three different traces, and the check misses a closer given to the wrong source. The brief's cap of seven drops deferred items out of sight, and a conserved Spec stands only in a brief. The person wants one standard for putting an item off, and one place that holds every deferred item.

## Given

`rule-carry-over` — the Render of the skill `carry`
**＋** `.claude/skills/carry/SKILL.md` — the skill file rendered from it
**＋** `estimate-carry-over-writes` — the promise of the skill, whose Criterion this sub-case replaces whole
**＋** `vault/wiki/brief.md` — the brief it rewrites in the short shape
**＋** `vault/wiki/backlog.md` — the file `guppi backlog` writes, with the conserved Spec and its targets
**＋** `vault/raw/` — the session folder it marks with `carry.md`
**＋** `/retro`, `/handoff` — phases the skill does not run

## History

- 2026-09-27 created · raw/2026-09-27/1255/ledger.md#case-451.9
