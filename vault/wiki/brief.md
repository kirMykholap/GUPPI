# Brief — 2026-09-23, after the librarian's walk of the units 1724 and 2046 of 2026-09-22

Written by the librarian from `vault/raw/2026-09-22/2046/handoff.md`, the four `materialize.yaml`
of 2026-09-22 and `tags.md`. Both units of the day were applied in ascending order: the conserved
Spec of 1724 first, then 2046.

## Where things stand

- Plan Mode of session 2046 produced seven live Cases — 344, 347, 349, 350, 351, 352, 353 —
  repairing the eight findings the second `ask-guppi` pass had left in the conserved Spec of 1724
  and the two deferred items of the previous brief. Six more Cases were written and superseded
  inside the session as their own facts were checked.
- Work Mode built the code of nine Cases across both Specs: in `guppi/lint.py` `is_reading` by
  `by hand` alone with `READING` gone, the predicate `names_a_form` lifted out, the new class
  `markers`; in `guppi/prespec.py` `check_markers`, `check_pairs` (the `replace` and `reword` pairs
  of a Spec simulated in entry order over copies in memory), `check_tasks` by `generate.READ_LINE`,
  `check_frontier` by the source segment of a Frontier line, and the check of `method` over the
  Estimate items of a plan; in `guppi/generate.py` `replace_hits` and `replace_once` lifted,
  `tick_read` over every live Spec of `raw/`, and the cascade passing over an `archived` Estimate.
  572 tests green, `make style` clean, `prespec --check` exits 0 on the session's own plan. Two
  commits: `8e618d1` and `7033975`.
- Not done by the session: no page of `vault/wiki/` — this run wrote them; eleven readings and the
  two `by hand` checks waited for it; the two items of Slice 3b, `rule-work-mode` and
  `rule-subagent-guppi`, stay on the sprint page with no defer.
- The walk: 34 entries in the 1724 yaml, 43 in the 2046 yaml (37 from the ledger, 6 appended by the
  librarian's synthesis), `unparsed` empty in both; 0014 and 1121 extended with 0 entries. 26
  entries were skipped as `superseded_by` — of 1724: 330.2, 332.1, 332.2, 333, 334, 336, 337, 338.1,
  339, 340; of 2046: 341, 342, 343, 345, 346, 348. Exactly the set the handoff named.
- Pages created: 34 decisions (21 Cases of 1724, 13 of 2046), 8 lessons, 3 estimates
  (`estimate-prespec-catches-an-unwrapped-render`, `estimate-prespec-catches-a-method-without-a-form`,
  `estimate-prespec-simulates-the-pairs`), 2 insights by synthesis
  (`insight-harness-one-rule-implemented-twice-drifts`,
  `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`).
- Pages updated: 9 rules (`rule-atomicity`, `rule-carry-over`, `rule-case-protocol`,
  `rule-documentation`, `rule-estimates-schema`, `rule-lint`, `rule-page-generation`,
  `rule-prespec`, `rule-skill-hi`), 14 estimates, 4 lessons (the four clustered by synthesis),
  1 insight (`insight-workflow-edit-pair-signed-from-a-grep-fragment`, `actioned` by
  `decision-case-351`, one link).
- Archived: 16 decision pages of the superseded Cases and the two `clustered` children of
  `insight-workflow-edit-pair-signed-from-a-grep-fragment` —
  `lesson-replace-anchors-overlap-in-one-spec` and
  `lesson-reword-pairs-signed-before-the-places-were-read` — 18 pages under
  `vault/archive/migration/2026-09-23/2046/`.
- The two `by hand` boxes of the 1724 Spec were read after `generate` and both pass:
  `rule-materialize` stands `built` with no lint finding on it (line 283), and no finding of the
  class `method` stands on `estimate-sprint-migration-index-dissolved` (line 319). The boxes stay
  unticked: only a `read` line is ticked by a script.

## Readings due

Ten Estimates went `pending` by a Case of this walk and thirteen stood `pending` before it; no
Estimate stands `failed`. Every target rule stands `draft`.

From an unticked `- [ ] read …` line of `vault/raw/2026-09-22/2046/spec.md`:

- `estimate-case-protocol-loaded` — `rule-case-protocol` — L54, one reading at the first `/hi` of a
  session, by hand, plus the preview cases of `tests/test_ledger.py`.
- `estimate-estimates-schema-checked` — `rule-estimates-schema` — L119.
- `estimate-prespec-binds-a-sprint-line` — `rule-prespec` — L164.
- `estimate-prespec-reconciles` — `rule-prespec` — L263, by hand at the first `/pre-spec` after the
  render.
- `estimate-carry-over-writes` — `rule-carry-over` — L326.
- `estimate-documentation-completes` — `rule-documentation` — L374.

From an unticked `- [ ] read …` line of the 1724 Spec, which `guppi archive` moved to
`vault/archive/migration/2026-09-22/1724/raw/spec.md` at the close of this run — the line is no
longer in a live Spec of `raw/`, so nothing will tick it and the reading is taken by the page's
`method`:

- `estimate-lint-catches` — `rule-lint` — L142 and L368; `pytest tests/test_lint.py`, one test per
  defect class, plus one live reading by hand written into the estimate line.
- `estimate-generate-ticks-the-spec` — `rule-page-generation` — L193; `pytest
  tests/test_generate.py` with a Spec beside the yaml, plus one reading of the session's `spec.md`
  after the librarian's run.
- `estimate-prespec-checks-the-plan` — `rule-prespec` — L241, L623 and L692; `pytest
  tests/test_prespec.py`, the tests of `--check`.
- `estimate-generate-cascades` — `rule-page-generation` — L284; `pytest tests/test_generate.py`, the
  tests of the cascade.

No read line stands for these; the place is the page's `method`:

- `estimate-atomicity-rendered` — `rule-atomicity` — `make lint`, `render --check` exit 0, the text
  between the markers of `case-schema.md` read by hand after the render.
- `estimate-case-protocol-case-form` — `rule-case-protocol` — one reading by hand of the Cases of a
  session, at its close.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — one reading by hand of
  `case-schema.md` after the render, at a session start.
- `estimate-generate-fails-alone` — `rule-page-generation` — `pytest tests/test_generate.py`, the
  tests of the failed, skipped and marked entries.
- `estimate-harness-pipeline` — `rule-harness` — `make test-harness`, then `make lint` by hand.
- `estimate-hi-writes-frontier` — `rule-skill-hi` — one reading by hand at the first `/hi` of the
  next session, written into the estimate line.
- `estimate-session-phases-in-order` — `rule-session` — by hand at the close of a session, the
  seven artefacts read in order.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` — one reading by hand of the
  yaml and the brief after a librarian's run on the first marked lesson clustered under an
  `actioned` Insight.
- `estimate-sprint-migration-index-dissolved` — `entity-sprint-migration` — `test -e
  vault/wiki/index.md` false, then every `rg` hit read by hand.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — one reading of the tree
  by hand at the close of the sprint.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — `make lint` exit 0, or only
  unread lines on the sprint page's own Estimates.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — `make test` on the last commit of
  `migration`, then `git log` of `main` after the merge.
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` — one reading
  at the close of Slice 3f, the four commands of its `method`.

## Deferred

Three items. Two Insights born of this run's synthesis, and one defer. `rule-work-mode`,
`rule-subagent-guppi`, `rule-morph` and `insight-workflow-code-live-before-the-page-it-reads` are
named by the sprint page and are not listed here (case 229.4).

1. `insight-harness-one-rule-implemented-twice-drifts` — `severity` 2, standing in 1 brief.
   Pattern: a judgment the pipeline makes in two places is implemented twice — a check re-states
   what a writer, a ticker or another check does — and the copies drift with no test about the
   difference. Proposal: where a check judges the same text as a writer or a ticker, the pattern or
   the predicate lives in one module and both sides import it; where the code cannot be shared, one
   test runs both sides over the same input and asserts they answer alike.
2. `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — `severity` 2, standing in 1
   brief. Pattern: a fact is signed on a check narrower than the claim — the command that ran
   answered one question and the sentence it supports makes a wider one. Proposal: a claim names the
   command its output rests on and is no wider than that output; a claim about a whole set is
   checked by a count on both sides, and that count stands in the Case's `tasks` as a reading.
3. `rule-skill-hi` — defer `decision-case-352`, standing in 2 briefs, no related Insight. What a
   Frontier closer must tell apart, with the person's own words in its `purpose`: a session that
   looks at an item of the sprint and passes over it leaves no trace anywhere but the Frontier,
   which dies with the session; whether a Work line closes in a second moment of its own, whether
   `pre-spec` requires closed lines under `Cases` alone, and whether `· sprint` and
   `· defer case N` stay two closers or become one.

Two items of the previous brief's list left it: `insight-workflow-edit-pair-signed-from-a-grep-fragment`
went `actioned` by case 351, and the defer 333 of `rule-documentation` was retired by 348, itself
superseded by 349, which is an update — `estimate-documentation-completes` stands `pending`, not
`failed`.

## Flags

- Five entries of the 2046 yaml carry `incomplete: [criterion]` — lines 2 and 4 (case 341, 342 on
  `estimate-case-protocol-loaded`), 6 (343 on `estimate-estimates-schema-checked`), 9 (345 on
  `estimate-prespec-simulates-the-pairs`) and 20 (348 on `estimate-documentation-completes`). All
  five are also `superseded_by`, so no page was written from them and the live Cases 350, 351, 353
  and 349 carry the Criterion instead. No entry of either yaml is marked `failed`, `near` or
  `unparsed`.
- No Estimate stands `failed`.
- The handoff instructed one read of `vault/raw/.../ledger.md` — its line count and the lines the
  yaml does not account for — as case 349 widens the librarian's frame. The read was refused: the
  frame this run loaded is the one rendered before case 349 (`.claude/agents/librarian-guppi.md` is
  written by `guppi render` in step 4 of this same run), and that text forbids the read without
  exception. Consequence: this brief cannot say which ledger line of 2046 or 1724 has no entry;
  `unparsed` is empty in all four yamls, which is not the same statement. The next librarian's frame
  carries case 349.
- The handoff counts seven lessons of the session; eight `lesson` entries stand in the 2046 yaml
  (lines 7, 12, 13, 16, 21, 22, 37, 38) and eight lesson pages were written.
- The handoff says eleven Estimates go `pending`; ten distinct Estimates were set `pending` by
  applied entries of the two yamls.
- `addressed_by` on an Insight is one decision wikilink by the schema. Case 351 set one link on
  `insight-workflow-edit-pair-signed-from-a-grep-fragment`. The reopening path of case 284.4 moves
  the field to one decision, so a list of two would be dropped silently — named in the handoff, no
  Case yet.
- The `context` of Case 347 in the 2046 Spec was rewritten after its ratification to cite the event
  log instead of the person's premise. The person was told and did not object; no Case signs the
  edit.
- Case 352 defers `rule-skill-hi` alone. Case 346, which it supersedes, deferred `rule-prespec` too;
  `rule-prespec` now carries no `deferred_by`, and finding (8) of the previous brief — the questions
  of the defer bind `rule-prespec` as well — stands unrepaired.
- Stale defers, from lint: `rule-work-mode` and `rule-subagent-guppi` 31 times since case 29,
  `rule-morph` 1 time since case 239. All three are on the sprint page; this session added no defer
  to them.
- `rule-spec-box` earns three findings — missing `kind`, missing `estimates`, orphan. It is a
  placeholder of Slice 5 on the sprint page.
- `make lint` gives 92 findings, exit 1, against the 87 the handoff measured before the run: 62 on
  31 legacy decision pages (`missing section ## Context` / `## Problem`), 23 `unread: pending` on
  the Estimates above, 3 on `rule-spec-box`, 3 `deferred` counters, 1 `unmigrated: 23 pages in the
  shape before case 193`. The two findings of case 330.1 cleared, and no finding of the class
  `method` or `reading` stands anywhere; the growth is the eleven readings this walk made due.
- `guppi archive` moved the units 0014, 1121 and 1724 of 2026-09-22 to
  `vault/archive/migration/2026-09-22/<hi>/raw`, and kept 2046, the session of the run. The four
  readings whose `- [ ] read …` line stood in the 1724 Spec now have no line in a live Spec: a
  reading due at the close of a walk that archives its own Spec loses its place, and only the page's
  `method` says where it is taken.
- No MOC candidate: no category crossed a threshold named by any input this run.

## Next session

Cases — what needs a decision:

- The `addressed_by` shape on an Insight: one decision wikilink, or a list, and what the reopening
  of case 284.4 does with the second link. From the handoff's caveats and the flag above.
- The read of `ledger.md` case 349 grants and the frame of this run refused: whether the Criterion
  of `estimate-documentation-completes` and the Render now agree, read against this brief's flag.
- The edit of Case 347's `context` after its ratification: signed after the fact, or reverted.
- Whether `rule-prespec` takes the defer of case 352 beside `rule-skill-hi`.

Work — what is done without a decision:

- Take the pending readings named in Readings due, by slug: `estimate-case-protocol-loaded`,
  `estimate-estimates-schema-checked`, `estimate-prespec-binds-a-sprint-line`,
  `estimate-prespec-reconciles`, `estimate-carry-over-writes`, `estimate-documentation-completes`,
  `estimate-lint-catches`, `estimate-generate-ticks-the-spec`, `estimate-prespec-checks-the-plan`,
  `estimate-generate-cascades` — these ten have a read line in a Spec of 2026-09-22.
- The thirteen older pending readings, by slug: `estimate-atomicity-rendered`,
  `estimate-case-protocol-case-form`, `estimate-case-protocol-ledger-line-form`,
  `estimate-generate-fails-alone`, `estimate-harness-pipeline`, `estimate-hi-writes-frontier`,
  `estimate-session-phases-in-order`, `estimate-synthesis-keeps-actioned-by-the-mark`,
  `estimate-sprint-migration-index-dissolved`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`,
  `estimate-sprint-migration-rule-class-files-dissolved`.
- The unticked boxes of the 1724 Spec, now at
  `vault/archive/migration/2026-09-22/1724/raw/spec.md`, other than its read lines, are the boxes of
  the superseded Cases 332.2 (L533–539), 336 (L425–428), 337 (L576) and 340 (L729); no work is due
  on them. Its two `by hand` boxes (L283, L319) were read in this run and both pass.
  `vault/raw/2026-09-22/2046/spec.md` has no unticked box but its six read lines.
- The tree at the close of this run holds only the librarian's own writes; this brief's commit
  covers `vault`, `CLAUDE.md` and `.claude`.

## Readings at the close

- `make test`: 572 passed, 2 skipped.
- `make lint`: 92 findings, exit 1.
- Pages: 58 rules, 101 estimates, 52 lessons, 18 insights, 482 decisions, 4 entities.
