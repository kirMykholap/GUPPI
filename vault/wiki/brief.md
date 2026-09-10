# Brief — 2026-09-10, after Slice 3 session F

Written by the librarian on its first run.

## Where things stand

Session F did what its handoff records under "What actually got done": commit
`165a261 chore(ledger): the tail of session E` (three ledger lines of 11:18:24) and
commit `893b3d9 feat(harness): Case 43 — materialize and generate walk every date`
(`guppi/materialize.py` with `dates_with` and `materialize_date`, `guppi/generate.py`
with `generate_date`, six tests, `make test` 132 green, the Spec of session F appended
to `raw/2026-09-10/spec.md`, the five decision lines of Case 43).

Not done by that session: the pages of Case 43 (written by this run), `guppi render` of
`.claude/agents/librarian-guppi.md`, the ten estimate readings of Case 42, the close of
Slice 3 in `sprint.md`.

`guppi materialize` walked two dates: `raw/2026-09-09/materialize.yaml` extended with 0
entries, `raw/2026-09-10/materialize.yaml` extended with 8. The 2026-09-10 yaml now holds
88 entries (3 added by the librarian) and 23 decision entries; the 2026-09-09 yaml holds
74 entries and 34 decision entries.

Pages written by `guppi generate` in this run:

| category | created | updated |
|---|---|---|
| rules | 0 | 4 (`rule-materialize`, `rule-page-generation`, `rule-documentation`, `rule-retro-commit`) |
| estimates | 3 (`estimate-agents-visible-in-session`, `estimate-materialize-walks-dates`, `estimate-generate-walks-dates`) | 1 (`estimate-retro-commit-gates`, pending → passed) |
| lessons | 1 (`lesson-agents-visible-in-session`) | 2 (both clustered) |
| insights | 1 (`insight-harness-agent-visibility`, severity 2) | 0 |
| decisions | 1 (`decision-case-43`) | 0 |
| entities | 0 | 0 |

`estimate-materialize-assembles` was skipped: it is already `passed` with a Result.
The cascade moved `rule-retro-commit` to `built` and `rule-materialize` and
`rule-page-generation` to `draft`, as the handoff foretold. `guppi cleanup` moved 0 pages.

## What the next session does first

1. `uv run guppi render`, then commit: `.claude/agents/librarian-guppi.md` differs from
   `rule-documentation` since this run rewrote its Render text (Case 43). `make lint` is
   red at its first step until then.
2. Write the ten estimate readings of Case 42 (eight of Slice 3, two of Case 43) as
   `estimate[...]` ledger lines. `estimate-materialize-walks-dates` and
   `estimate-generate-walks-dates` now exist as `pending`, and the walk over two dates
   ran live in this session.
3. Close Slice 3 in `sprint.md` once those readings are in. This run did not touch
   `sprint.md`; the handoff said not to.
4. Decide the route of `[delete][old-harness]` of case 6 or accept it as permanent noise.
5. **Hand-written by the owner's word after the librarian's run, 2026-09-10 12:05.** The ten
   readings of item 2 are already in the ledger (11:57:07), plus five lessons; two readings
   failed (`estimate-documentation-completes`, `estimate-synthesis-clusters`: the librarian
   read a lesson page and `guppi/generate.py` before any script error), so Slice 3 is not
   closed. Those fifteen lines are not in `materialize.yaml`; the next librarian picks them
   up. Question to discuss as a Case: readings written after the librarian's commit reach
   the Frontier two sessions later, because `/hi` loads this brief only and the brief is
   written before them. Proposal on the table: `/hi` prints the ledger lines of every date
   not yet in its `materialize.yaml`; the page lag of one session is accepted.

## Deferred

1. **Slice 3b: Work Mode** — `rule-work-mode`, `rule-subagent-guppi` (placeholders,
   `draft`, orphans at lint), `to-executable-plan`, the four hooks. Case 29. Related
   Insight `insight-harness-agent-visibility`, severity 2. (postponed 1 time)
2. `/grill-me` is kept without a page. Slice 3b or 5. (postponed 4 times)
3. `origin` points at the product repository and `migration` has no upstream; `git pull`
   in `/hi` fails visibly. Owner's decision 11.1: leave until Slice 5. (postponed 4 times)
4. `gh` is not logged in and there is no GitHub remote. Owner's decision 11.2.
   (postponed 4 times)
5. The fate of `vault/parked/`, `vault/archive/` (the old one, 505 files, beside the new
   `vault/archived/`), `docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`
   and the 2026-08 documents under `docs/`. Slice 5. (postponed 3 times)
6. **Archive in `ask-guppi`:** a named slug checked against `vault/archived/`. Case 31
   discussion; decide when the archive holds something. (postponed 1 time)

## Flags

- **`generate` stopped with `'str' object has no attribute 'get'`** on its first run of
  this session. Cause: entries 83 and 85 carry `replace` as a mapping (`old:`/`new:`
  under the key), while `guppi/generate.py` iterates `replace` as a list of items. The
  librarian rewrote those two blocks into the list form, without changing the `old` or
  `new` text, and reran. Both `raw/2026-09-10/materialize.yaml` (lines 2306, 2356) and
  the shape produced by `materialize` from the Spec are involved; `case-schema.md` does
  not pin the shape.
- **The aborted run left `log.md` short.** Entries 78–82 wrote their pages and their page
  `History` lines before the crash, but their lines never reached `vault/wiki/log.md`:
  nine lines are missing (`estimate-retro-commit-gates` passed, `lesson-agents-visible-in-session`
  and its estimate created, `estimate-materialize-walks-dates` created and its backlink,
  `rule-materialize` updated). The pages are correct; the feed is not. Not repaired by
  hand.
- **Log lines of a multi-date walk carry the date of the yaml, not of the run.** Two
  `2026-09-09` cascade lines sit after the `2026-09-10` lines in `log.md`, and
  `rule-materialize` ends its History with a `2026-09-09` line written today.
- **`[delete][old-harness]` of case 6** (2026-09-09 yaml) fails on every run: no page and
  no category. `generate: old-harness: no page to delete` on stderr, exit 1. Not routed,
  per the handoff.
- **Entries marked `incomplete`:** 2026-09-10 — line 3 `lesson-agents-at-import-not-expanded`
  (`tags`, `source`), line 4 `estimates-schema` (`then`), line 5 `rule-lint` (`then`),
  line 7 `lesson-tests-cli-date-pinned` (`tags`), line 80 `lesson-agents-visible-in-session`
  (`source`); decision entries of Cases 28 and 30. 2026-09-09 — all 74 entries and all 34
  decision entries, the debt of the backfill.
- **Entries marked `near` by the librarian:** `lesson-agents-visible-in-session` near
  `lesson-agents-loaded-at-session-start`; `estimate-materialize-walks-dates` near
  `estimate-materialize-assembles`; `estimate-generate-walks-dates` near
  `estimate-generate-writes`. None was merged: each checks a behaviour its neighbour does
  not check, and the two lessons make opposite claims.
- **Contradiction, clustered:** `lesson-agents-loaded-at-session-start` (session D) and
  `lesson-agents-visible-in-session` (session E) claim the opposite about the same
  mechanism. Both are now `clustered` under `insight-harness-agent-visibility`, severity
  2, status `open`. Its Proposal is a suggestion, not a decision.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` are the two lint orphans;
  they have stood as placeholders since Case 29 with no `kind`, `estimates` or `tags`.
- No entry is marked `failed` in the 2026-09-10 yaml, no line is `unparsed` in either
  yaml, no Estimate in the vault has `status: failed`, and 17 are `pending`.
- No MOC candidate was identified.
- **Lint.** `make lint` stops at its first step: `render: .claude/agents/librarian-guppi.md
  differs from its Rule page`, exit 1 — expected, and the caveat accepted in the Spec of
  Case 43. Run separately: `guppi index --check` exit 0; `guppi lint` 169 findings — 166
  `schema: missing section` on Decision pages of Cases 1–30, 2 `orphan`
  (`rule-work-mode`, `rule-subagent-guppi`), 1 `method`
  (`estimate-documentation-completes` says by hand while `estimate-materialize-walks-dates`
  names a test file).

## Readings at the close

- `make test` → 132 passed. `make style` → clean.
- `make lint` → exit 1 at `render --check`; `index --check` → exit 0; `guppi lint` → 169
  findings.
- `find vault/wiki -type f | wc -l` → 166 (160 at the close of session E).
- Live pages: rules 32, entities 0, estimates 42, lessons 10, insights 1, decisions 57.
- `raw/2026-09-10/materialize.yaml`: 88 entries, 23 decisions, none failed, none unparsed,
  none unapplied. `raw/2026-09-09/materialize.yaml`: 74 entries, 34 decisions, one failed
  and unapplied (`old-harness`), none unparsed.
