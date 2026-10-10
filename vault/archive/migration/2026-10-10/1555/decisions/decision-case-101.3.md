---
type: decision
case: "101.3"
status: archived
update: ["[[rule-skill-hi]]"]
origin: raw/2026-09-13/ledger.md#case-101.3
sprint: migration
created: 2026-09-13
tags: [session, harness]
---

## Context

What Case 95 held besides the archive of Case 100: the ledger tail and `decided_by`. Lines written after the librarian's commit — the readings of its run, the lessons of the close — reach the Frontier two sessions later: the next librarian materializes them, and only its brief names them (`lesson-readings-after-librarian-invisible-to-next-hi`, `insight-session-vault-knowledge-not-loaded`, severity 2). `/hi` reads the brief alone. Case 45 described `guppi tail`; deferred as 63, 79, 95.

## Problem

`/hi` sees nothing of what was written after the librarian's commit; a failed reading and a lesson wait one session more. `rule-ledger-tail` cannot be taken up as a `create`: the placeholder page exists and `generate` (`guppi/generate.py:289`) answers with a collision; none of the three placeholders has a way to be filled.

## Given

Ask-guppi (the first question of the session): `rule-ledger-tail` is a placeholder — `draft`, no `kind`, `estimates` or `tags`, `deferred_by: [decision-case-95]`, one of the three lint orphans; `estimate-ledger-tail` is free; the tags `session`, `harness`, `ledger` are registered.
**＋** A placeholder is born in `generate.defer` without a `ref`: `type`, `purpose`, `status: draft`, `deferred_by`, `origin`, `sprint`, `created`, History `deferred, placeholder`; it has no `kind`, and every real Entity or Rule has one. That is the mark.
**＋** `generate.create` (`generate.py:289`): `path.exists()` → "a page with this slug exists; a collision is an error, not a rename". `rule-page-generation` (`built`, two Estimates: `estimate-generate-writes`, `estimate-generate-walks-dates`) says the same in its Purpose.
**＋** 100.1 (`{supersedes:case 95}`) takes `decision-case-95` out of the placeholder's `deferred_by` in the same run, before this create applies: the yaml keeps the ledger's order.
**＋** `rule-skill-hi` (`built`, MOC, `render_mode: full`, children `rule-internal-context`, `rule-git-context`, `rule-github-issues`; `deferred_by: [decision-case-98]`, the render after the pull, F4): its Render holds one marker per child in `children` order; Estimates `estimate-hi-no-read-calls` (the context holds everything without a read call) and `estimate-hi-writes-frontier` (`### case 73.3`).
**＋** `materialize.parse_line`, the yaml fields `line`, `folded`, `unparsed`, `load_yaml` — the same as 100.1; the coverage of a line is one function for both scripts. After case 103 the ledgers under `raw/` are the session ledgers and, until archived, the date-level ones.
**＋** `sprint.md`, Slice 3c, lists `decided_by`, `origin` as a pointer, the archive by run stamp with paths rewritten, the tail, lint on both fields, the pages migrated by script; Done-when 1 says "`decided_by` or `origin`". `docs/migration/migration-plan.md` is a draft, not the vault.
**＋** Glossary row `/hi, Frontier`: "the open items it assembles (brief, sprint, issues, an unfinished plan)".
**－** `hi` goes to the event log, not the ledger: it is never in the tail.
**－** A line outside the ledger grammar is not printed: it is either `unparsed` in the yaml or not a record.
**－** `decided_by` is not made; `origin` stays the one pointer from a page to its Case: `#case-N` names `decision-case-N`, History carries the wikilink, lint checks `origin`. `estimate-tail-lists-unmaterialized` (the slug of Case 45) is not used; the Estimate is derived from the slug: `estimate-ledger-tail`.

## Criterion

- [[estimate-hi-no-read-calls]] § case 101.3

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-101.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
