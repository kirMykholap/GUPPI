---
type: decision
case: "103.4"
status: current
update: ["[[rule-pretask]]"]
origin: raw/2026-09-13/ledger.md#case-103.4
sprint: migration
created: 2026-09-13
tags: [session, workflow, harness]
---

## Context

The ledger, the yaml and `event_log.md` live at the date level (`raw/<date>/`); the session folder `raw/<date>/<HHMM>/` holds `spec.md`, `frontier.md`, `handoff.md` (case 73.1 left the ledger in place with a `－` line). A session across midnight writes into two ledgers; the three sessions of 2026-09-12 into one. The archive by session (102) on a date-level ledger comes out with an exception, "the ledger one level up".

## Problem

The unit of work is the session: Plan Mode, Spec, Frontier, handoff, the librarian, the archive. The ledger is the one file of the session that does not sit with it. Every reader of the ledger is tied to the date: the hook's write path, the walks of `materialize` and `generate`, the window of `pretask`, the form of `origin` and its resolution in lint.

## Given

`ledger.py`: `ledger_path` = `raw/<today>/ledger.md`; `session_dir` (`ledger.py:196`) already gives `raw/<hi date>/<hi HHMM>/` from the event logs and the session stamp — `guppi spec` writes there; `existing_bodies` (the dedupe) reads `raw/*/ledger.md`; the `hi` window is `session_event_logs` over `event_log.md` back across dates (55.1).
**＋** `materialize.py`: `dates_with(ledger.md)` walks by date; `read_specs` reads `raw/<date>/spec.md` (before 73) and every `raw/<date>/<HHMM>/spec.md`; `origin` is built at lines 351, 566, 577, 654 as `raw/{date}/ledger.md#…`; the yaml is `yaml_path(date)`. `generate.py:795`: `dates_with(materialize.yaml)`. `pretask.window_lines` (`pretask.py:119`): the date-level ledgers from the `hi` date to today, on the `hi` date from the `hi` time; findings `raw/<day>/ledger.md:<n>`. `lint.py:57–58`: `ORIGIN_CASE`, `ORIGIN_LINE` — the date form only; `archived_slugs` — `rglob` over the archive.
**＋** Pages: `rule-ledger-write` (Estimate `estimate-ledger-write-lifts`), `rule-materialize` (`estimate-materialize-assembles`, `estimate-materialize-walks-dates`), `rule-page-generation` (`estimate-generate-writes`, `estimate-generate-walks-dates`), `rule-pretask` (`estimate-pretask-reconciles`), `rule-lint` (`estimate-lint-catches`, the block of 100.3 from this session). `index.md` §1 (the tree of `raw/`), §4 ("`#case-N` in an `origin`"); glossary rows `Ledger`, `Working files`, `origin`, `archived`; `origin` in five `schema.md` (entities, rules, estimates, lessons, decisions) as prose — `schema.yaml` has no pattern; `decisions/schema.md:23`: "`raw/` stays in place; it is not archived with the session".
**＋** Case 100.3 (line written) — `origin` resolved in the archive; 100.5 — `index.md`, the glossary. Their content is the Spec, not yet approved; 103.5 and 103.6 take them over with `{supersedes}`, so `estimate-lint-catches` holds one block and the files have one place.
**＋** Case 102 as first shown loses 102.3 and 102.5 (folded into 103.5, 103.6).
**－** `event_log.md`, `rule-event-log`, `rule-spec-capture`, `rule-skill-hi` do not change: the session folder, the log of the day and the window stay as they are.
**－** The hook changes its write path the moment the code changes — in Work Mode of this session; the lines of this session written before that stay in the date-level ledger and are read in the old shape. Pre-task of this session runs on the old code.

## Criterion

- [[estimate-pretask-reconciles]] § case 103.4

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-103.4
