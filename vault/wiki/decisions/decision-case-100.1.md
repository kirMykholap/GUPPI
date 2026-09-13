---
type: decision
case: "100.1"
status: current
create: [rule-raw-archive]
supersedes: [decision-case-95]
origin: raw/2026-09-13/ledger.md#case-100.1
sprint: migration
created: 2026-09-13
tags: [harness, librarian, ledger]
---

## Context

Case 95 (Slice 3c, deferred four times: 45, 63, 79, 95) is the lifecycle of `raw/`. Today `raw/` holds four dates: 4 ledgers (529 lines), 4 yamls (21 911 lines), the session folders. Every librarian run walks every date again: `materialize` reads 4 ledgers and every Spec, `generate` 4 yamls, and prints "extended with 0 entries", "0 pages". Case 95 bundles six things; this Case takes one, the archive of an applied unit of `raw/`, and leaves the tail `/hi` prints and `decided_by` to their own Cases. Shown again twice in the session: for the root `vault/archive/` (case 102) and for the ledger of a session (case 103).

## Problem

Nothing says when a unit of `raw/` is done with, and nothing takes it away. The `origin` of every page (`raw/<date>/ledger.md#case-N`) points in, lint checks it, `rule-cleanup` and `index.md` §1 say "`raw/` stays". The migration plan meant a move "by run stamp with every path rewritten": 82 pages point at 2026-09-09 alone, plus History lines and `log.md`.

## Given

Ask-guppi: no live or archived page is about the archive of `raw/`; `rule-raw-archive` and `estimate-raw-archive` are free; the tags `harness`, `librarian`, `ledger` are registered.
**＋** `rule-ledger-tail` (`draft`, placeholder, `deferred_by: decision-case-95`) is about the tail, not the archive; this Case takes 95 up (`{supersedes:case 95}` on 100.1); the tail is Case 101.
**＋** Pointers into `raw/`: `origin: raw/<date>/ledger.md#case-N` on the pages of Cases, `#L<n>` on 48 lessons and readings, 318 History lines with `#L<n>`, `line`/`folded`/`unparsed` in the yaml — all by line number; §4 of `index.md`: a ledger line is never edited or deleted. So no file is cut and no pointer is rewritten: a ledger keeps its name, lint resolves it in `raw/` or in the archive (103.5).
**＋** Readers: `materialize` and `generate` walk `vault/raw/` only — an archived unit leaves the walk by itself; `lint.check_origin` (`guppi/lint.py:289–314`) is the one place the path is resolved; `ledger.session_event_logs` walks `event_log.md` back to a `session-start`; `ledger.existing_bodies` (the dedupe) reads the ledgers under `raw/`; `pretask` reads the session folder of the day.
**＋** A supersedes across dates goes through pages (`generate.py:601` sets `superseded_by` on `decision-case-N`), not through the earlier yaml; `materialize.mark_superseded` marks entries of its own yaml only.
**＋** After case 103 the unit of `raw/` is the session folder `raw/<date>/<HHMM>/` with its own `ledger.md` and `materialize.yaml`; a date-level `raw/<date>/ledger.md` with its yaml (the shape before 103) is a unit of its own, with the `<HHMM>/` folders of that date that have no ledger of their own.
**＋** In `raw/` today: 09-09, 09-10, 09-11, 09-12, all date-level — every yaml entry `applied`, no ledger line outside its yaml (checked 2026-09-13 with `parse_line`: 74/90, 157/151, 84/78, 244/210 entries/lines, 0 kept); 09-13 will hold both shapes. `raw/notes/`: four files of August (two owner's notes, two `.coverage.tsv`), referenced only by the handoffs of the old `vault/archive/2026-08-*` (removed by 102.1).
**＋** The archive root is `vault/archive/` (case 102): `<sprint>/<date>/<HHMM>/<category>/<slug>.md` for pages, `<sprint>/<date>/<HHMM>/raw/` for a session's raw, `<sprint>/<date>/raw/` for a date-level ledger; `<sprint>` the first `## <id>` of `sprint.md` (`materialize.sprint_id`).
**＋** `rule-cleanup` Purpose: "`raw/<date>/` stays where it is: every `origin` points into it and lint checks that path"; `rule-documentation` (`render_mode: full`): steps 1–4, the frame forbids the librarian to read the archive (90.3) — running a script is not a read.
**－** `.gitignore` does not change: `event_log.md` does not move (the `hi` window of the hook across midnight); a `raw/<date>/` with one gitignored file is empty for git.
**－** `rule-brief`, `rule-close`, `rule-materialize`, `rule-page-generation` do not change for the archive; `git add vault` picks the move up.
**－** The session of the run never moves, nor any unit dated the day of the run: after the librarian's commit Retro and the readings still write into the session's ledger.
**－** A failed entry is fixed by hand in `raw/` (the Spec or the yaml, in Plan Mode) or by a superseding Case; the librarian never repairs (90.3).

## Criterion

- [[estimate-raw-archive]] § case 100.1

## History

- 2026-09-13 created · raw/2026-09-13/ledger.md#case-100.1
