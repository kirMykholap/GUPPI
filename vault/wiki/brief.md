# Brief — 2026-09-10, after Slice 3 session G

Written by the librarian.

## Where things stand

Session G did what its two handoff documents record under "What actually got done".

- Commit `68bb295`: the render of `.claude/agents/librarian-guppi.md` after Case 43; the
  ledger tail of session F and the Spec of session G in `raw/`; the owner's note in
  `brief.md`.
- Commit `3eaf5a3`: `guppi/generate.py` — an entry fails alone whatever the cause and is
  marked `failed`, `log.md` is appended after each entry, History and log lines carry the
  run's date while `created` carries the yaml's, a delete with `category: unknown` is
  applied with a stdout line. Five tests, `make test` 137. `log.md` regained six lines of
  entries 78–82. `case-schema.md` pins `replace` as a list of pairs; `index.md` §5 gains
  the delete-outside-the-vault row; `migration-plan.md` and `sprint.md` carry Slice 3c.
- Commit `ebf943b`: the two defers of Retro (Cases 50, 51).
- Commit `7dc4f7f`: `guppi/materialize.py` skips entries without `line` when matching the
  ledger and entries without `case` when grouping decisions; one test, `make test` 138.
- Reading taken in session: `estimate-librarian-reads-beyond-the-four-inputs` passed
  (13:10:37).
- Not done by that session: the pages of Cases 44–49 (written by this run); the render of
  the Case 44 frame into the agent file; the readings of Case 44 and of the four new
  generate estimates; the close of Slice 3; Cases 45, 50, 51 (deferred).

`guppi materialize` walked two dates: `raw/2026-09-09/materialize.yaml` extended with 0
entries, `raw/2026-09-10/materialize.yaml` extended with 37. The 2026-09-10 yaml now holds
128 entries (6 added by the librarian across two runs) and 31 decision entries; the
2026-09-09 yaml holds 74 entries and 34 decision entries. No line is `unparsed` in either.

`guppi generate` wrote 49 pages for 2026-09-10 and 0 for 2026-09-09, stderr empty, exit 0.

| category | created | updated |
|---|---|---|
| rules | 1 (`rule-ledger-tail`, a Case 45 defer placeholder) | 11 pages from 8 entries and the cascade: `rule-documentation`, `rule-index-check`, `rule-synthesis`, `rule-materialize`, `rule-page-generation` (Cases 47 and 48), `rule-retro`, `rule-ledger-write`, `rule-brief`, `rule-close`, `rule-end-of-work`, `rule-handoff` |
| estimates | 11 (4 of Cases 47–48, 7 paired with the lessons) | 10 (readings of Cases 42 and 44, criterion rewrites of Cases 44 and 49) |
| lessons | 7 | 2 of the 7, set `clustered` by synthesis |
| insights | 1 (`insight-harness-yaml-entry-shape-assumed`, severity 2, `open`) | 0 |
| decisions | 8 (`decision-case-44` … `decision-case-51`) | 0 |
| entities | 0 | 0 |

The cascade left `rule-documentation`, `rule-synthesis` and `rule-page-generation` in
`draft` (two failed readings and four pending estimates); `rule-brief`, `rule-close`,
`rule-end-of-work`, `rule-handoff`, `rule-retro`, `rule-index-check` and `rule-materialize`
are `built`. `guppi cleanup` moved 0 pages. `sprint.md` was not touched; Slice 3 is not
closed.

## What the next session does first

1. `uv run guppi render`, then commit. `.claude/agents/librarian-guppi.md` differs from
   `rule-documentation`, whose Render text Case 44 rewrote in this run. `make lint` is red
   at its first step until then.
2. Take the readings of Case 44 (`estimate-documentation-completes`,
   `estimate-index-check-merges`, `estimate-synthesis-clusters` against their new
   criteria) and of the four estimates of Cases 47–48
   (`estimate-generate-rejects-shape-alone`, `estimate-generate-logs-per-entry`,
   `estimate-generate-dates-history-by-run`,
   `estimate-generate-passes-delete-outside-vault`). The first three run against this
   librarian's run; the last four against `guppi generate` of this run, whose stderr was
   empty and whose walk over 2026-09-09 printed the delete on stdout.
3. Close Slice 3 in `sprint.md` once the two `failed` readings are re-taken and pass.
4. Plan Mode over Cases 50 (`rule-retro`), 51 (`rule-ledger-write`), Slice 3c (raw
   lifecycle, with Case 45 `rule-ledger-tail`) or Slice 3b.

## Deferred

1. **Slice 3b: Work Mode** — `rule-work-mode`, `rule-subagent-guppi` (placeholders,
   `draft`, orphans at lint), `to-executable-plan`, the four hooks. Case 29. Related
   Insight `insight-harness-agent-visibility`, severity 2. (postponed 2 times)
2. `/grill-me` is kept without a page. Slice 3b or 5. (postponed 5 times)
3. `origin` points at the product repository and `migration` has no upstream; `git pull`
   in `/hi` fails visibly. Owner's decision 11.1: leave until Slice 5. (postponed 5 times)
4. `gh` is not logged in and there is no GitHub remote. Owner's decision 11.2.
   (postponed 5 times)
5. The fate of `vault/parked/`, `vault/archive/` (the old one, 505 files, beside the new
   `vault/archived/`), `docs/superpowers/`, `docs/HANDOFF.md`, `docs/migration/rule-*.md`
   and the 2026-08 documents under `docs/`. Slice 5. (postponed 4 times)
6. **Archive in `ask-guppi`:** a named slug checked against `vault/archived/`. Case 31
   discussion; decide when the archive holds something. (postponed 2 times)
7. **The three defers of this session**, one slot for three items: Case 45
   `rule-ledger-tail` → Slice 3c; Case 50 `rule-retro`, the Retro reshaped as an analysis;
   Case 51 `rule-ledger-write`, the Stop hook that misses a reply ending in a tool call.
   (postponed 1 time each)

## Flags

- **Entries marked `incomplete`, 2026-09-10:** nine — line 3
  `lesson-agents-at-import-not-expanded` (`tags`, `source`), line 4 `estimates-schema`
  (`then`), line 5 `rule-lint` (`then`), line 7 `lesson-tests-cli-date-pinned` (`tags`),
  line 80 `lesson-agents-visible-in-session` (`source`), line 99
  `lesson-librarian-reads-beyond-the-four-inputs` (`source`), line 100
  `lesson-readings-after-librarian-invisible-to-next-hi` (`source`), line 120 `rule-retro`
  (`then`), line 121 `rule-ledger-write` (`then`); four decision groups (Cases 28, 30, 50,
  51). The two `source` marks of lines 99 and 100 and the two `then` marks of the Retro
  defers were foretold in the handoff.
- **Entries marked `incomplete`, 2026-09-09:** all 74 entries and all 34 decision groups,
  the debt of the backfill. Unchanged.
- **`[delete][old-harness]` of case 6 now applies.** Stdout: `generate: old-harness:
  outside the vault, nothing to archive`; stderr empty, exit 0. Case 48 holds. The entry
  keeps its `failed` mark from the earlier run beside the new `applied` mark; `generate`
  does not clear a stale `failed` when the entry later applies.
- **Failed Estimates, 2:** `estimate-documentation-completes` and
  `estimate-synthesis-clusters`, both `failed` at 11:57:07 on the read constraint of the
  first librarian run. Case 44 rewrote both criteria in this same yaml, after the failed
  lines; the pages carry the new Criterion and the old `failed` status. Their parents
  `rule-documentation` and `rule-synthesis` are `draft`.
- **Entries marked `near`, 7 in all, 4 added by this run:**
  `estimate-generate-rejects-shape-alone` near `estimate-generate-writes`;
  `estimate-generate-logs-per-entry` near `estimate-generate-writes`;
  `estimate-generate-dates-history-by-run` near `estimate-generate-walks-dates`;
  `estimate-generate-passes-delete-outside-vault` near `estimate-generate-writes`. None
  merged: each checks a behaviour its neighbour does not name. Carried from the previous
  run: `lesson-agents-visible-in-session`, `estimate-materialize-walks-dates`,
  `estimate-generate-walks-dates`.
- **Six Estimate pages have no `## Criterion` section, so six index lines are empty:**
  `estimate-generate-rejects-shape-alone`, `estimate-generate-logs-per-entry`,
  `estimate-generate-dates-history-by-run`,
  `estimate-generate-passes-delete-outside-vault`, `estimate-generate-walks-dates`,
  `estimate-materialize-walks-dates`. All six were created by a standalone `create` entry
  with a `ref`, not by an `estimate:` block nested in a page create. The criterion is in
  the frontmatter of each. An index line without a criterion cannot be compared at the
  next index check.
- **Four `clustered` lessons have no `## Insight` section:**
  `lesson-agents-loaded-at-session-start`, `lesson-agents-visible-in-session`,
  `lesson-generate-replace-mapping-crashes`,
  `lesson-materialize-assumes-every-entry-has-a-line`. The synthesis update sets the
  `insight` field; nothing writes the section the schema requires.
- **Three lessons about hook events were compared and not clustered.**
  `lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (the `Stop` hook does not fire
  when a reply ends in a tool call) against `lesson-hooks-messagedisplay-cannot-block` and
  `lesson-hooks-sessionstart-cannot-block`. The two older pages were opened to read their
  Trigger and Root cause: both record a documented limit of an event, measured before any
  design leaned on it; the new one records a live loss of ratified ledger lines. Same
  area, different cause; no Insight made. All three stay `new`.
- **Three lessons stay `new` without a pair:** `lesson-generate-log-written-last`,
  `lesson-librarian-reads-beyond-the-four-inputs`,
  `lesson-readings-after-librarian-invisible-to-next-hi`.
- **Contradiction, closed by Case 44 in this run:** `rule-index-check` allowed a page read
  that the Criterion of `estimate-synthesis-clusters` forbade. Both texts were rewritten
  in this yaml. `estimate-librarian-reads-beyond-the-four-inputs` records the reading that
  found it, passed.
- **`log.md` is still nine lines short** for entries 78–82 of the aborted run of session F.
  The pages and their History lines exist; six lines were restored in commit `3eaf5a3`.
  Not repaired by this run.
- **Stale defers:** `rule-work-mode` and `rule-subagent-guppi` have stood as placeholders
  since Case 29 with no `kind`, `estimates` or `tags`; they are two of the three lint
  orphans. The third, `rule-ledger-tail`, was born in this run and is expected to be an
  orphan.
- No MOC candidate was identified. `entities-index.md` is still empty.
- **Lint.** `make lint` stops at its first step: `render: .claude/agents/librarian-guppi.md
  differs from its Rule page`, exit 1 — the caveat accepted in the Spec, now also carrying
  the Case 44 rewrite. Run separately: `guppi index --check` exit 0; `guppi lint` 198
  findings — 190 `schema: missing section` or `missing field` (44 `## Context`, 38
  `## Problem`, 38 `## Now`, 21 `tags`, 20 `## Then`, 8 `source`, 6 `## Method`, 6
  `## Criterion`, 4 `## Insight`, 3 `## Estimates`, 3 `kind`, 3 `estimates`), 3 `orphan`,
  1 `method` (`estimate-documentation-completes` says by hand while
  `estimate-materialize-walks-dates` names a test file). 169 findings at the previous
  close.

## Readings at the close

- `make test` → 138 passed.
- `make lint` → exit 1 at `render --check`; `index --check` → exit 0; `guppi lint` → 198
  findings.
- Live pages: rules 33, entities 0, estimates 53, lessons 17, insights 2, decisions 65;
  170 in all (166 at the close of session F).
- `raw/2026-09-10/materialize.yaml`: 128 entries, 31 decision groups, none unapplied, none
  unparsed. `raw/2026-09-09/materialize.yaml`: 74 entries, 34 decision groups, all applied,
  none unparsed, one entry carrying both `applied` and a stale `failed` (`old-harness`).
- `vault/archived/` is empty; `guppi cleanup` moved 0 pages.
