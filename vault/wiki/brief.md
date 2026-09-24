# Brief — 2026-09-23, after the librarian's run on session 1859

Written by the librarian from `vault/raw/2026-09-23/1859/handoff.md`, the four `materialize.yaml`
the walk named (`2026-09-23/0034`, `2026-09-23/1126` and `2026-09-23/1355`, each extended with
0 entries; `2026-09-23/1859`, written by `materialize`, 3 entries appended by the librarian's
synthesis) and `tags.md`. The session opened on 2026-09-23 at 18:59 and closed on 2026-09-24.

## Where things stand

- Plan Mode of session 1859 ratified Cases 383, 384, 385, 386, 387.1–387.4 and 388, and deferred
  389 at Retro. Cases 384–388 were shown again after pre-spec and ratified again; the
  re-ratification wrote no new ledger lines. Frontier: C2 closed by a reading, C3–C10 closed by
  Cases, C1 left `[-] · sprint`, C11 deferred by Case 389, W1 and W2 stay open. From the handoff.
- Work Mode, commit `733132c`: `guppi/ratified.py` (new: the Spec writer, the reconciliation, the
  comparison `differences`), `guppi/prespec.py` (`check_ratified`), `guppi/bashguard.py`,
  `guppi/sprint.py`, `guppi/cli.py`; `plan_path` moved to `ledger.py`, `tagged_blocks` to
  `materialize.py`; tests `tests/test_ratified.py` (new), `tests/test_prespec.py`,
  `tests/test_bashguard.py`, `tests/test_sprint.py`. From the handoff.
- The session's readings: 4, all `passed` — `estimate-sprint-migration-index-dissolved` (L1),
  `estimate-bash-guard` (L28), `estimate-prespec-checks-the-ratified-copy` (L27, folded into the
  `create` entry of L23).
- This run, 1859 yaml: 29 entries from the ledger and 3 from synthesis, 32 of 32 `applied`. None
  `failed`, none `incomplete`, none `unparsed`; 2 marked `near`; the defer of 389 marked `exists`.
  The ledger has 30 lines; the yaml accounts for all 30 (L27 by `folded` in the entry of L23).
  `materialize` printed "written with 30 entries" for this yaml.
- Pages created: 10 decisions (383–389), 2 rules (`rule-spec-write`, `rule-spec-reconcile`),
  3 estimates (`estimate-spec-write-copies-the-ratified-case`,
  `estimate-spec-reconcile-shows-a-changed-case`, `estimate-prespec-checks-the-ratified-copy`),
  1 lesson, 1 insight (synthesis).
- Pages updated: 9 rules (`rule-case-protocol` by 383, 387.1, 387.2, 387.3 in ledger order and the
  defer of 389; `rule-prespec` by 387.4 then 388; `rule-hook-registry` by 387.2 then 387.3;
  `rule-bash-guard` by 384, its defer of 382 superseded; `rule-synthesis` and
  `rule-insights-schema` by 385; `rule-language` by 387.1; `rule-plan-mode` by the backlinks of the
  two new rules; `rule-sprint` `built → draft` by the cascade), 6 estimates (5 by Cases 384, 385,
  386, 387.1, 388; `estimate-sprint-migration-index-dissolved` `failed → passed` by its reading;
  `estimate-bash-guard` set `pending` by 384, then `passed` by L28), 3 insights, 1 live lesson
  (`lesson-plan-mode-contract-change-skips-the-estimates-blocks`, clustered by synthesis),
  2 decisions (`decision-case-380`, `decision-case-382`, superseded by 388 and 384).
- Insights: `insight-workflow-case-schema-silent-on-what-the-scripts-accept` `actioned` by 383;
  `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` `actioned` by 388, its defer
  of 380 superseded; `insight-workflow-contract-change-leaves-its-derived-text-stale` has
  `addressed_by: decision-case-378.5` again by 385, which also states that `addressed_by` moves
  only to a later case.
- Synthesis: `lesson-case-designed-in-dialogue-not-checked-against-its-rules` and
  `lesson-plan-mode-contract-change-skips-the-estimates-blocks` → the new
  `insight-workflow-case-written-without-reading-the-pages-it-changes`, `open`, severity 2. No
  lesson of this run carried `addressed_by`.
- Cleanup moved 6 pages to the archive: `decision-case-380`, `decision-case-382`, and the
  4 lessons of the two Insights actioned by 383 and 388
  (`lesson-generate-replace-anchor-stays-in-one-section`,
  `lesson-sub-case-given-the-parents-plus-lines-has-no-form`,
  `lesson-case-context-bookkeeping-written-from-memory`,
  `lesson-case-context-claim-wider-than-its-search`).
- Renders: rewritten `.claude/settings.json` (the hooks `guppi ratified` on `Stop` and
  `guppi ratified --edit` on `PostToolUse` of `Edit|Write|MultiEdit`), `CLAUDE.md`,
  `.claude/agents/librarian-guppi.md`, `.claude/skills/pre-spec/SKILL.md`,
  `vault/wiki/case-schema.md`, `sprint.md`. `render --check` and `glossary --check` exit 0.
- `vault/wiki/sprint.md` after `guppi sprint`: a blank line follows each of the three milestone
  headings (Slice 3g, Slice 4, Slice 5), and the Done-when line of `index.md` is `[x] · passed`.

## Readings due

No Estimate stands `failed`. 23 stand `pending`; every target stands `draft`: each rule named
below and `entity-sprint-migration`.

From an unticked `- [ ] read …` line of `vault/raw/2026-09-23/1859/spec.md`:

- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` — L161. This run had no
  lesson with `addressed_by`, so it is not the reading place.
- `estimate-sprint-renders-the-backlog` — `rule-sprint` — L203, `sprint.md` after this run (the
  fact is under Where things stand).
- `estimate-language-followed` — `rule-language` — L261, by hand in the next session.
- `estimate-spec-write-copies-the-ratified-case` — `rule-spec-write` — L333, live at the first
  ratification of the next session.
- `estimate-spec-reconcile-shows-a-changed-case` — `rule-spec-reconcile` — L400, live at the first
  edit of a ratified Case.
- `estimate-prespec-reconciles` — `rule-prespec` — L497, by hand at the first `/pre-spec` after the
  render.

No read line in the session's Spec; the place is the page's `method`:

- `estimate-agent-writing-followed` — `rule-agent-writing` — by hand in the next session: the
  section in `CLAUDE.md` and one reply of the agent against it.
- `estimate-carry-over-writes` — `rule-carry-over` — pytest over the skill's render, plus one live
  reading of a carried-over session.
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` — by hand, the first
  acknowledging reply of a session.
- `estimate-case-protocol-case-form` — `rule-case-protocol` — by hand, the Cases of a session at its
  close.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — by hand, the ledger and the
  preview of the first session where a lesson and the Case that closes its cause stand together.
- `estimate-case-protocol-loaded` — `rule-case-protocol` — at the first `/hi` of a session by hand,
  plus the preview cases of `tests/test_ledger.py`.
- `estimate-documentation-completes` — `rule-documentation` — `make test-documentation`; the live
  reading by hand.
- `estimate-generate-fails-alone` — `rule-page-generation` — `pytest tests/test_generate.py`, the
  tests of the failed, skipped and marked entries.
- `estimate-one-judgment-one-implementation-followed` — `rule-one-judgment-one-implementation` —
  `render --check` exit 0, then by hand the section in `CLAUDE.md` and the diff of the next Work
  Mode session.
- `estimate-prespec-binds-a-sprint-line` — `rule-prespec` — `uv run pytest tests/test_prespec.py -k sprint`.
- `estimate-retro-report-holds-each-fact-once` — `rule-retro` — by hand at the first `/retro` after
  the render.
- `estimate-rules-schema-checked` — `rule-rules-schema` — `pytest tests/test_schemas.py -k rules`;
  the live reading `make lint`.
- `estimate-session-phases-in-order` — `rule-session` — by hand at the close of a session.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — the tree by hand at the
  close of the sprint.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — `make lint` exit 0, or only
  unread lines on the sprint page's own Estimates.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — `make test` on the last commit
  of `migration`, then `git log` of `main` after the merge.
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` — by hand:
  `ls vault/wiki/*/schema.md` empty, `index.md` absent, the grep over `guppi/` and `tests/` empty,
  `render --check` and `glossary --check` exit 0.

## Deferred

Two items. The previous brief's three left the list: `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`
went `actioned` by Case 388, which superseded its defer 380;
`insight-workflow-case-schema-silent-on-what-the-scripts-accept` went `actioned` by Case 383;
`rule-bash-guard` left with Case 382, which Case 384 superseded.
`insight-workflow-code-live-before-the-page-it-reads` is `open` and named by the sprint page's
Backlog, so it is not listed here (case 229.4).

1. `insight-workflow-case-written-without-reading-the-pages-it-changes` — `severity` 2, standing in
   1 brief. Pattern: a Case is composed from what the agent has in view, and the pages it changes
   or runs beside are not read against it before it is shown, so a contradiction is found only by
   pre-task or pre-spec. Proposal: before a Case that changes a contract or adds a hook is shown,
   list the pages its tasks touch or run beside and read each against it.
2. `rule-case-protocol` — deferred by Case 389, no related Insight, standing in 1 brief: the
   acknowledging reply of a re-ratification carries the `LEDGER` block with the Case's lines again,
   so the hook of `rule-spec-write` writes it.

## Flags

- `near`, from the index check (no page merged):
  - `rule-spec-write` near `rule-spec-capture`: both keep the Spec to what was approved; the first
    writes each ratified Case into the plan file, the second copies the approved plan into the
    repository.
  - `rule-spec-reconcile` near `rule-case-protocol`: both keep a Case from acting without its
    content ratified in view.
- No entry is marked `failed`, `incomplete` or `unparsed`. No Estimate stands `failed`.
- `generate` printed no move to the Backlog and dropped no milestone in this run.
- No contradiction found in this run. The previous brief's contradiction on `addressed_by` of an
  `actioned` Insight was answered by Case 385.
- Stale defers, from lint: `rule-work-mode` and `rule-subagent-guppi` 31 times since case 29,
  `rule-morph` 1 time since case 239. All three are on the sprint page.
- `rule-spec-box`: three findings — missing `kind`, missing `estimates`, orphan.
- No MOC candidate: no input this run names a threshold crossed.
- `make lint`: 92 findings, exit 1 — 62 on 31 legacy decision pages (`missing section ## Context`
  / `## Problem`), 23 `unread` (all `pending`), 3 on `rule-spec-box`, 3 `deferred` counters,
  1 `unmigrated: 22 pages in the shape before case 193`.

## Next session

Cases — what needs a decision:

- The handoff gives `estimate-case-protocol-case-form` and `estimate-case-protocol-loaded`, which
  speak of the re-showing Case 387 changes, to Slice 3g; the Slice 3g item of the sprint page does
  not name them. From the handoff and `sprint.md`.

Work — what is done without a decision:

- Take the pending readings of Readings due, by slug: `estimate-synthesis-keeps-actioned-by-the-mark`,
  `estimate-sprint-renders-the-backlog`, `estimate-language-followed`,
  `estimate-spec-write-copies-the-ratified-case`, `estimate-spec-reconcile-shows-a-changed-case`,
  `estimate-prespec-reconciles`, `estimate-agent-writing-followed`, `estimate-carry-over-writes`,
  `estimate-case-protocol-acknowledging-reply`, `estimate-case-protocol-case-form`,
  `estimate-case-protocol-ledger-line-form`, `estimate-case-protocol-loaded`,
  `estimate-documentation-completes`, `estimate-generate-fails-alone`,
  `estimate-one-judgment-one-implementation-followed`, `estimate-prespec-binds-a-sprint-line`,
  `estimate-retro-report-holds-each-fact-once`, `estimate-rules-schema-checked`,
  `estimate-session-phases-in-order`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`,
  `estimate-sprint-migration-rule-class-files-dissolved`.
- The unticked boxes of the Specs: 6 `read` lines in `vault/raw/2026-09-23/1859/spec.md`; 2 in
  the Spec of 1355; 13 in the Spec of 1126 (12 `read` lines and the task L467
  `uv run pytest tests/test_schemas.py -k rules`); 11 `read` lines in the Spec of 0034. The last
  three Specs moved with their units to `vault/archive/migration/2026-09-23/<unit>/raw/spec.md` by
  `guppi archive` in this run.
- W1 and W2 of the Frontier stay open. From the handoff.
- From the next session the agent creates the plan file with its title line before the first Case,
  so the hook of `rule-spec-write` finds it. From the handoff.
- No ledger line of 1859 was left unapplied. The tree at the close of this run holds only the
  librarian's own writes and the session's `handoff.md`; this brief's commit covers `vault`,
  `CLAUDE.md` and `.claude`.

## Readings at the close

- `make test`: 616 passed, 2 skipped.
- `make lint`: 92 findings, exit 1.
- Pages: 61 rules, 113 estimates, 50 lessons, 21 insights, 533 decisions, 4 entities.
