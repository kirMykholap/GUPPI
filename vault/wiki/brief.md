# Brief — 2026-09-23, after the librarian's run on session 1355

Written by the librarian from `vault/raw/2026-09-23/1355/handoff.md`, the three `materialize.yaml`
the walk named (`2026-09-23/0034` and `2026-09-23/1126`, each extended with 0 entries;
`2026-09-23/1355`, 40 entries from the ledger and 7 appended by the librarian's synthesis) and
`tags.md`.

## Where things stand

- Plan Mode of session 1355 ratified Cases 376, 377.1, 377.3, 378.1–378.8, 379 and 381, and
  deferred 380 (Plan Mode) and 382 (Retro). Case 379 superseded 377.2 in its own session. Frontier:
  C4–C8 closed by Cases, C3 deferred, C1 and C2 left on the sprint; W1–W3 stay open. From the
  handoff.
- Work Mode, commit `0e48e5d`: `guppi/materialize.py` (the lesson line's mark through one function
  `address`, `CRITERION_SECTIONS = ("when", "then")`, a pair inside a Criterion
  `incomplete: [criterion]`), `guppi/generate.py` (`## Given` on the Decision page),
  `guppi/prespec.py` (the pair inside a Criterion, the frame check, the `note:` lines), with tests.
  From the handoff.
- The session's readings: 7, all `passed` — L38, L44 and the five folded into their `create`
  entries (L39–L43).
- Not done by the session: the pages and renders, written by this run; the readings listed below;
  the one pass over the Estimates (Slice 3g). From the handoff.
- This run, 1355 yaml: 44 of 47 entries applied. The 3 entries of Case 377.2 (L4–L6) carry
  `superseded_by: 379` and were not applied; `estimate-case-protocol-loaded` is not touched. None
  `failed`; 2 `incomplete`, both of 377.2; 2 marked `near`; the defers of 380 and 382 marked
  `exists`. `unparsed` is empty. The ledger has 45 lines; the yaml accounts for all 45.
- Pages created: 16 decisions (376–382; `decision-case-377.2` moved to the archive by cleanup),
  6 estimates, 3 lessons, 1 insight (synthesis).
- Pages updated: 10 rules (7 by Cases: `rule-retro`, `rule-case-protocol`, `rule-materialize`,
  `rule-estimates-schema`, `rule-decisions-schema`, `rule-prespec`, `rule-plan-mode`;
  `rule-bash-guard` by the defer of 382; `rule-page-generation` by the backlink of an Estimate;
  `rule-skill-hi` `draft → built` by the cascade; `rule-retro` also `built → draft`), 3 estimates
  (1 by Case 379, 1 by Case 377.3 and a reading, 1 by a reading), 3 insights (Cases 377.1, 378.5,
  defer 380; 2 of them also by synthesis), 2 entities (`entity-glossary` by 378.2 and 378.3,
  `entity-sprint-migration` by 381), 1 lesson (`lesson-sub-case-given-the-parents-plus-lines-has-no-form`,
  clustered by synthesis).
- Cleanup moved 5 pages to the archive: `decision-case-375` (superseded by 376),
  `decision-case-377.2`, and 3 lessons archived by the cascade under `actioned` Insights.
- Case 377.1 set `insight-session-vault-knowledge-not-loaded` `actioned`; Case 378.5 set
  `insight-workflow-contract-change-leaves-its-derived-text-stale` `actioned`.
- Synthesis:
  - `lesson-case-context-bookkeeping-written-from-memory` → `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`,
    which stays `open`.
  - `lesson-generate-replace-anchor-stays-in-one-section` and `lesson-sub-case-given-the-parents-plus-lines-has-no-form`
    → the new `insight-workflow-case-schema-silent-on-what-the-scripts-accept`, `open`.
  - `lesson-case-appended-a-line-inside-another-criterion`, whose entry carries
    `addressed_by: decision-case-378.4`, → `insight-workflow-contract-change-leaves-its-derived-text-stale`.
    The Insight stays `actioned`; its `addressed_by` moved to `decision-case-378.4` (case 284.4);
    the lesson went to the archive by the cascade. This pair is the first marked lesson clustered
    under an `actioned` Insight.
- Renders: `render --check` exit 0 after the render. Rewritten: `vault/wiki/case-schema.md`,
  `vault/wiki/decisions/schema.yaml`, `vault/wiki/estimates/schema.yaml`,
  `.claude/skills/pre-spec/SKILL.md`, `.claude/skills/retro/SKILL.md`, `sprint.md` (Slice 3g),
  `glossary.md`.

## Readings due

One Estimate stands `failed` and 19 stand `pending`. Every target stands `draft`:
`entity-sprint-migration` and each rule named below.

Failed:

- `estimate-sprint-migration-index-dissolved` — `entity-sprint-migration` — read line L138 of
  `vault/raw/2026-09-23/1126/spec.md`. Its Result: two live pointers at `index.md`,
  `guppi/materialize.py:11` and the Given of `estimate-case-protocol-case-form`, line 18.

From an unticked `- [ ] read …` line of `vault/raw/2026-09-23/1355/spec.md`:

- `estimate-retro-report-holds-each-fact-once` — `rule-retro` — L70, by hand at the first `/retro`
  after the render.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` — L616.

No read line in the session's Spec; the place is the page's `method`:

- `estimate-agent-writing-followed` — `rule-agent-writing` — by hand in the next session: the section
  in `CLAUDE.md` and one reply of the agent against it.
- `estimate-carry-over-writes` — `rule-carry-over` — pytest over the skill's render, plus one live
  reading of a carried-over session.
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` — by hand, the first
  acknowledging reply of a session.
- `estimate-case-protocol-case-form` — `rule-case-protocol` — by hand, the Cases of a session at its
  close.
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
- `estimate-prespec-reconciles` — `rule-prespec` — by hand at the first `/pre-spec` after the render.
- `estimate-rules-schema-checked` — `rule-rules-schema` — `pytest tests/test_schemas.py -k rules`;
  the live reading `make lint`.
- `estimate-session-phases-in-order` — `rule-session` — by hand at the close of a session.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` — the yaml and the brief after
  a librarian's run on the first marked lesson clustered under an `actioned` Insight; this run is
  one (`vault/raw/2026-09-23/1355/materialize.yaml`, the pair above).
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

Three items. Of the previous brief's four, `insight-workflow-contract-change-leaves-its-derived-text-stale`
went `actioned` by Case 378.5, `insight-session-vault-knowledge-not-loaded` went `actioned` by Case
377.1, and `rule-retro` left with Case 375, which Case 376 superseded.
`insight-workflow-code-live-before-the-page-it-reads` is `open` and named by the sprint page's
Backlog, so it is not listed here (case 229.4).

1. `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — `severity` 2, standing in
   2 briefs, deferred by Case 380. Pattern: a fact is signed on a check narrower than the claim; the
   command that ran answered one question and the sentence it supports makes a wider one. Proposal:
   a claim names the command its output rests on and is no wider than that output; a claim about a
   whole set is checked by a count on both sides.
2. `insight-workflow-case-schema-silent-on-what-the-scripts-accept` — `severity` 2, standing in
   1 brief. Pattern: the Case schema does not say how the scripts read the text a Case writes, so
   the agent writes a form the scripts do not handle and only the pre-spec check finds it. Proposal:
   the Case schema states, beside each form, the limit the scripts put on it — a replace pair acts
   inside one section of a page, a sub-case's given is its own or none.
3. `rule-bash-guard` — deferred by Case 382, no related Insight, standing in 1 brief: the refusal
   message says the refusal is by design — use Write, and do not report it at Retro.

## Flags

- `incomplete`: L5 `estimate-case-protocol-ledger-line-form` and L6 `estimate-case-protocol-loaded`,
  `[criterion]`, both of Case 377.2, marked `superseded_by: 379` and not applied.
- `near`, from the index check (no page merged):
  - `lesson-case-context-bookkeeping-written-from-memory` near
    `lesson-case-context-claim-wider-than-its-search`; both are children of
    `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`.
  - `lesson-case-appended-a-line-inside-another-criterion` near
    `lesson-plan-mode-contract-change-skips-the-estimates-blocks`, which stays `new`.
- No entry is marked `failed` or `unparsed`.
- One Estimate stands `failed`: `estimate-sprint-migration-index-dissolved` (Readings due).
- Contradiction: `rule-insights-schema` says `addressed_by` is one link, the latest (case 361), and
  that it moves to the decision of a marked lesson (case 284.4). In this run the second moved the
  `addressed_by` of `insight-workflow-contract-change-leaves-its-derived-text-stale` from
  `decision-case-378.5`, the Case that set it `actioned`, to the earlier `decision-case-378.4`.
- `vault/wiki/sprint.md`, written by `guppi sprint`: the collapsed headings of Slice 4 and Slice 5
  stand on two lines with no blank line between them.
- `generate` printed no move to the Backlog and dropped no milestone in this run.
- Stale defers, from lint: `rule-work-mode` and `rule-subagent-guppi` 31 times since case 29,
  `rule-morph` 1 time since case 239. All three are on the sprint page.
- `rule-spec-box`: three findings — missing `kind`, missing `estimates`, orphan.
- No MOC candidate: no input this run names a threshold crossed.
- `make lint`: 89 findings, exit 1 — 62 on 31 legacy decision pages (`missing section ## Context`
  / `## Problem`), 20 `unread` (19 `pending`, 1 `failed`), 3 on `rule-spec-box`, 3 `deferred`
  counters, 1 `unmigrated: 23 pages in the shape before case 193`.

## Next session

Cases — what needs a decision:

- `estimate-sprint-migration-index-dissolved` stands `failed`: its reading found two live pointers
  at `index.md`. From its page.
- The contradiction on `addressed_by` of an `actioned` Insight: the latest decision (case 361) or
  the decision of the marked lesson (case 284.4). From `rule-insights-schema` and this run.
- The person found the re-showing of Cases after a change of the model correct but not convenient,
  "worth a thought on how to lighten it". From the handoff.
- The fact about the tool into the schema — a `replace` pair acts inside one section of a page
  (`lesson-generate-replace-anchor-stays-in-one-section`), named by the handoff as a candidate Case
  for the next Plan Mode.
- `vault/wiki/sprint.md` has no blank line between two collapsed milestone headings; a defect of
  `guppi sprint`'s output found by this run.

Work — what is done without a decision:

- Take the pending readings of Readings due, by slug: `estimate-retro-report-holds-each-fact-once`,
  `estimate-case-protocol-ledger-line-form`, `estimate-agent-writing-followed`,
  `estimate-carry-over-writes`, `estimate-case-protocol-acknowledging-reply`,
  `estimate-case-protocol-case-form`, `estimate-case-protocol-loaded`,
  `estimate-documentation-completes`, `estimate-generate-fails-alone`,
  `estimate-one-judgment-one-implementation-followed`, `estimate-prespec-binds-a-sprint-line`,
  `estimate-prespec-reconciles`, `estimate-rules-schema-checked`,
  `estimate-session-phases-in-order`, `estimate-synthesis-keeps-actioned-by-the-mark`,
  `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`,
  `estimate-sprint-migration-merges`, `estimate-sprint-migration-rule-class-files-dissolved`.
- The unticked boxes of the Specs: 2 `read` lines in `vault/raw/2026-09-23/1355/spec.md`; 14 in
  `vault/raw/2026-09-23/1126/spec.md` (13 `read` lines and the task L467
  `uv run pytest tests/test_schemas.py -k rules`); 11 `read` lines in
  `vault/raw/2026-09-23/0034/spec.md`.
- W1–W3 of the Frontier stay open. From the handoff.
- No ledger line of 1355 was left unapplied but the three of Case 377.2, superseded by 379. The
  tree at the close of this run holds only the librarian's own writes and the session's
  `handoff.md`; this brief's commit covers `vault`, `CLAUDE.md` and `.claude`.

## Readings at the close

- `make test`: 596 passed, 2 skipped.
- `make lint`: 89 findings, exit 1.
- Pages: 59 rules, 110 estimates, 53 lessons, 20 insights, 525 decisions, 4 entities.
