# Brief — 2026-09-11, after Slice 3 session H

Written by the librarian.

## Where things stand

Session H began on 2026-09-10 and crossed midnight. What its handoff records under "What
actually got done":

- Commit `241523d`: the render of the librarian agent after Case 44; the ledger tail of
  session G (ten lines of 16:15:34); the Spec of session H; `.gitignore` for `pages.base`.
- Commit `5b6b0df`: Case 55 — `guppi/ledger.py` joins the event logs of every date back to
  the session's start (55.1) and re-reads every main-agent message of `transcript_path` at
  each `Stop`, deduplicated against every `raw/*/ledger.md` (55.2); eleven tests. The run
  helper of `tests/test_generate.py` pins `now`.
- Commit `01f41cf`: Cases 52, 53, 56, 57 in code — `generate.py`, `materialize.py`,
  `index.py`, `cleanup.py`, `lint.py`; the six schema pairs; `make test` 158.
- Commit `df4cdcf`: `index.md`, `glossary.md`, `case-schema.md`, `CLAUDE.md` by hand; the
  one-off migrations (65 decision pages, 17 lessons, the two `*-walks-dates` estimates,
  the `old-harness` mark); Case 52 appended to the Spec of the 10th.
- Commit `833d3f0`: `estimates-index.md` removed; `deferred_by` on the four targets of
  current defers.
- Commit `66f0c9b`: the Retro — four readings passed, two lessons, the Spec items of 53.3
  and 55.1 added under their own Cases.
- Not done by that session: the render of the seven rule pages; the readings named below;
  the close of Slice 3; the rest of the deferred list.

`guppi materialize` walked three dates: `raw/2026-09-09/materialize.yaml` extended with 0
entries (74 entries, 34 decision groups, all applied), `raw/2026-09-10/materialize.yaml`
extended with 29 (157 entries, 35 decision groups), `raw/2026-09-11/materialize.yaml`
written with 73 entries and 9 decision groups. The librarian appended six entries to the
2026-09-11 yaml at synthesis, which now holds 79. No line is `unparsed` in any of the
three. No entry carries `failed`; every entry is applied.

`guppi generate` wrote 0 pages for 2026-09-09, 19 for 2026-09-10 and 64 for 2026-09-11;
exit 0, one line on stderr. `guppi cleanup` moved 21 pages, stderr empty.

| category | created | updated |
|---|---|---|
| decisions | 13 (`decision-case-52.1` … `52.4`, `53.1` … `53.4`, `54`, `55.1`, `55.2`, `56`, `57`) | 2 (`decision-case-50`, `decision-case-51`, marked superseded by 56 and 55.1) |
| lessons | 6 (`lesson-generate-keeps-a-stale-failed-mark`, `lesson-materialize-standalone-estimate-keeps-criterion-as-a-field`, `lesson-frame-read-clauses-omit-candidate-check-and-brief`, `lesson-ledger-hook-hi-lost-at-midnight`, `lesson-tests-generate-history-date-unpinned`, `lesson-spec-then-items-unchecked-against-ledger-lines`) | 2 by synthesis (`lesson-librarian-reads-beyond-the-four-inputs`, `lesson-tests-cli-date-pinned`, both set `clustered`); two of the six new ones were set `clustered` in the same run |
| insights | 2 by synthesis (`insight-librarian-frame-omits-required-reads`, `insight-tests-clock-not-pinned`, both severity 2, `open`) | 0 |
| rules | 0 | 14: `rule-ask`, `rule-brief`, `rule-cleanup`, `rule-documentation`, `rule-index`, `rule-index-check`, `rule-ledger-write`, `rule-lint`, `rule-materialize`, `rule-page-generation`, `rule-pretask`, `rule-retro`, `rule-spec-capture`, `rule-synthesis` |
| estimates | 0 | 11: `estimate-cleanup-moves`, `estimate-documentation-completes`, `estimate-generate-writes`, `estimate-index-check-merges`, `estimate-index-lists`, `estimate-ledger-write-lifts`, `estimate-lint-catches`, `estimate-materialize-assembles`, `estimate-retro-loads`, `estimate-spec-capture-appends`, `estimate-synthesis-clusters` |
| entities | 0 | 0 |

Readings that landed in this walk, all `passed`: `estimate-index-lists`,
`estimate-lint-catches`, `estimate-cleanup-moves`, `estimate-ledger-write-lifts`.
`estimate-documentation-completes` and `estimate-synthesis-clusters` were set back to
`pending` by Case 54. `guppi cleanup` moved 21 Estimate pages of Cases 53.1 and 53.2 to
`vault/archived/migration/2026-09-11/estimates/`. `deferred_by` was cleared on `rule-retro`
and `rule-ledger-write` by Cases 56 and 55.1. `sprint.md` was not touched; Slice 3 is not
closed.

## What the next session does first

1. `uv run guppi render` for the seven rule pages this session changed, then commit.
   `make lint` is red at its first step until then: `.claude/agents/ask-guppi.md`,
   `.claude/agents/librarian-guppi.md`, `.claude/skills/pre-task/SKILL.md`,
   `.claude/skills/retro/SKILL.md` and `CLAUDE.md` differ from their Rule pages.
2. Take the readings of `estimate-generate-writes` and `estimate-materialize-assembles`
   (the live parts against this run), `estimate-retro-loads` (at its `/retro`),
   `estimate-spec-capture-appends`, and `estimate-documentation-completes` and
   `estimate-synthesis-clusters` (against this librarian's report).
3. Close Slice 3 in `sprint.md` if the last two pass.
4. Plan Mode over the two observations of Retro below, Slice 3c (raw lifecycle, Case 45),
   Slice 3b.

Two observations of the Retro of session H carry no decision and belong on the Frontier:
(a) pre-task does not check that every decision line of the session has an item under its
own Case heading in the Spec — three lines lacked one and were fixed at Retro; a candidate
`update` of `rule-pretask` or `rule-spec-capture`. (b) `materialize` does not inherit a
parent Case's `given` into its sub-cases' decision entries; a candidate `update` of
`rule-materialize`.

## Deferred

1. **Slice 3b: Work Mode** — `rule-work-mode`, `rule-subagent-guppi` (placeholders,
   `draft`, orphans at lint), `to-executable-plan`, the four hooks. Case 29. Related
   Insight `insight-harness-agent-visibility`, severity 2. (postponed 3 times)
2. `/grill-me` is kept without a page. Slice 3b or 5. (postponed 6 times)
3. `origin` points at the product repository and `migration` has no upstream; `git pull`
   in `/hi` fails visibly. Owner's decision 11.1: leave until Slice 5. (postponed 6 times)
4. `gh` is not logged in and there is no GitHub remote. Owner's decision 11.2.
   (postponed 6 times)
5. The fate of `vault/parked/`, `vault/archive/` (the old one, beside the new
   `vault/archived/`), `docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`
   and the 2026-08 documents under `docs/`. Slice 5. (postponed 5 times)
6. **Archive in `ask-guppi`:** a named slug checked against `vault/archived/`. Case 31
   discussion; the archive now holds 21 pages. (postponed 3 times)
7. **Case 45, `rule-ledger-tail` → Slice 3c**, the raw lifecycle. (postponed 2 times)

Cases 50 and 51 left the list: Case 56 supersedes 50, Case 55.1 supersedes 51.

## Flags

- **Entries marked `incomplete`, 2026-09-11:** none at entry level. Six decision groups
  carry `incomplete: given` — 53.1, 53.2, 53.3, 53.4, 55.1, 55.2. Four more in the
  2026-09-10 walk: 52.1, 52.2, 52.3, 52.4. The `given` section sits on the parent Case
  heading in the Spec and `materialize` does not inherit it into a sub-case. Foretold in
  the handoff; `context` and `problem` were inherited, against its expectation.
- **Entries marked `incomplete`, 2026-09-10:** ten, one of them new in this walk —
  `lesson-frame-read-clauses-omit-candidate-check-and-brief` (`source`). The other nine
  stand unchanged from the previous brief. Decision groups 28, 30, 50, 51 keep their
  marks.
- **Entries marked `incomplete`, 2026-09-09:** all 74 entries and all 34 decision groups,
  the debt of the backfill. Unchanged.
- **No entry is marked `failed`** in any of the three yamls, and no Estimate page carries
  `failed`. Seven Estimates are `pending`: `estimate-documentation-completes`,
  `estimate-generate-writes`, `estimate-materialize-assembles`, `estimate-plan-mode-verified`,
  `estimate-retro-loads`, `estimate-spec-capture-appends`, `estimate-synthesis-clusters`.
- **Entries marked `near`, 5 added by this run.**
  `lesson-generate-keeps-a-stale-failed-mark` near `lesson-generate-log-written-last`;
  `lesson-materialize-standalone-estimate-keeps-criterion-as-a-field` near
  `lesson-materialize-assumes-every-entry-has-a-line`;
  `lesson-frame-read-clauses-omit-candidate-check-and-brief` near
  `lesson-librarian-reads-beyond-the-four-inputs`;
  `lesson-ledger-hook-hi-lost-at-midnight` near
  `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call`;
  `lesson-tests-generate-history-date-unpinned` near `lesson-tests-cli-date-pinned`. None
  was merged: each records a defect its neighbour does not name. Seven older `near` marks
  are carried in the 2026-09-10 yaml.
- **Two Insights were made at synthesis.** `insight-librarian-frame-omits-required-reads`
  over `lesson-librarian-reads-beyond-the-four-inputs` and
  `lesson-frame-read-clauses-omit-candidate-check-and-brief`;
  `insight-tests-clock-not-pinned` over `lesson-tests-cli-date-pinned` and
  `lesson-tests-generate-history-date-unpinned`. Four lessons moved to `clustered`.
- **The two ledger-hook lessons were compared and not clustered.**
  `lesson-ledger-hook-hi-lost-at-midnight` (the hook reads only today's event log) against
  `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (the `Stop` event does not fire
  when a reply ends in a tool call). Same area and one fix (Case 55), different mechanism.
  Both stay `new`, marked `near`.
- **`lesson-spec-then-items-unchecked-against-ledger-lines` stays `new` without a pair.**
- **Eight `clustered` lessons have no `## Insight` section**, four of them new:
  `lesson-frame-read-clauses-omit-candidate-check-and-brief`,
  `lesson-librarian-reads-beyond-the-four-inputs`, `lesson-tests-cli-date-pinned`,
  `lesson-tests-generate-history-date-unpinned`, beside the four of the previous run. The
  synthesis update sets the `insight` field; nothing writes the section the schema wants.
- **The tag `tests` is used but not registered in `tags.md`.** The only line on the stderr
  of `guppi generate`. It comes from `lesson-tests-generate-history-date-unpinned` and
  `insight-tests-clock-not-pinned`. The librarian does not write `tags.md`.
- **25 lint findings of class `decision` are the consequence of the archive.** The
  decision pages of Cases 47, 48, 53.1 and 53.2 name the 21 Estimate slugs they deleted;
  lint reads an archived target as naming no live page.
- **Two Estimate pages still have no `## Criterion` or `## Context` section:**
  `estimate-generate-walks-dates` and `estimate-materialize-walks-dates`. The other four
  of that group were archived by Case 53.2. Their criteria sit in the frontmatter.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 without `kind`, `estimates` or `tags`; `rule-ledger-tail` since Case 45.
  They are the three lint orphans.
- **No MOC candidate.** `entities-index.md` is empty; the vault holds no Entity page.
- **No contradiction between two rule texts was found in this run.**
- **Lint.** `make lint` stops at its first step with five `render: … differs from its Rule
  page` lines, exit 1. Run separately: `guppi index --check` exit 0; `guppi lint` 146
  findings, exit 1 — 116 `schema` (38 `## Context`, 38 `## Problem` on the 2026-09-09
  decision backfill, 9 `tags`, 9 `source`, 8 `## Insight`, 3 `## Estimates`, 3 `kind`,
  3 `estimates`, 2 `## Context` on estimates, 3 others), 25 `decision`, 3 `orphan`, 1
  `ref` (`rule-page-generation` names `decision-case-N` in its body, a literal), 1
  `method` (`estimate-documentation-completes` says by hand while
  `estimate-materialize-walks-dates` names a test file). 259 findings before this run.

## Readings at the close

- `make test` → 158 passed.
- `make lint` → exit 1 at `render --check` (five files); `index --check` → exit 0;
  `guppi lint` → 146 findings.
- Live pages: rules 33 (23 `built`, 10 `draft`), entities 0, estimates 32 (25 `passed`,
  7 `pending`, 0 `failed`), lessons 23 (15 `new`, 8 `clustered`), insights 4 (all `open`),
  decisions 78 (69 `current`, 9 `superseded`); 170 in all.
- `vault/archived/migration/2026-09-11/estimates/` holds 21 pages; `guppi cleanup` moved
  them in this run.
- `raw/2026-09-11/materialize.yaml`: 79 entries, 9 decision groups, none unapplied, none
  unparsed. `raw/2026-09-10/materialize.yaml`: 157 entries, 35 decision groups, all
  applied. `raw/2026-09-09/materialize.yaml`: 74 entries, 34 decision groups, all applied.
