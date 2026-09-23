# Brief — 2026-09-23, after the librarian's run on session 1126

Written by the librarian from `vault/raw/2026-09-23/1126/handoff.md`, the two `materialize.yaml`
the walk named (`2026-09-23/0034`, extended with 0 entries; `2026-09-23/1126`, 45 entries from the
ledger and 6 appended by the librarian's synthesis) and `tags.md`.

## Where things stand

- Plan Mode of session 1126 ratified Cases 363, 364.1–364.3 and 365–374 and deferred 375. Frontier
  C1–C15 closed: C1 `· sprint`, C7 `· work`, C15 `· defer case 375`, the rest `· case N`. W1 and W2
  stay open. From the handoff.
- Work Mode, commit `23e9d11`: the Routing Table in the docstring of `guppi/materialize.py` and a
  `then` item found by `slug` alone; no "Rule-class" in two docstrings of `guppi/generate.py`; three
  test names renamed; a test for an `update` with no content. From the handoff.
- The session's readings L27–L40: 14, all `passed`.
- Not done by the session: the pages and renders, written by this run; the readings listed below.
- This run: all 51 entries of the 1126 yaml applied; none `failed` or `incomplete`; 3 marked
  `near`; the defer of 375 marked `exists` (its target `rule-retro` is on disk). `unparsed` is
  empty. The ledger has 45 lines and the yaml accounts for all 45.
- Pages created: 15 decisions (363–375), 5 lessons.
- Pages updated: 17 rules (5 by Cases: `rule-skill-hi`, `rule-materialize`, `rule-page-generation`,
  `rule-case-protocol`, `rule-rules-schema`; `rule-retro` by the defer of 375; 11 `draft → built`
  by the cascade), 23 estimates (10 by Cases, 14 by readings, `estimate-atomicity-rendered` by
  both), 4 insights (1 by Case 373, 3 by synthesis), 3 lessons (clustered by synthesis).
- Case 373 set `insight-workflow-ratified-content-changed-on-the-agents-own-finding` `actioned`,
  `addressed_by: decision-case-373`. Cleanup moved its two clustered lessons to the archive.
- Synthesis, three lessons clustered under Insights that stood `actioned`; each Insight is `open`
  again:
  - `lesson-case-context-claim-wider-than-its-search` → `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`.
  - `lesson-case-render-update-skipped-the-live-reading-estimate` → `insight-workflow-contract-change-leaves-its-derived-text-stale`.
  - `lesson-plan-mode-frontier-refused-at-hi-again` → `insight-session-vault-knowledge-not-loaded`.
  - `lesson-case-protocol-chat-case-without-heading` and `lesson-case-check-command-signed-without-a-run`
    found no pair and stay `new`.
- Renders: `render --check` exit 0 after the render; `vault/wiki/rules/schema.yaml`,
  `vault/wiki/case-schema.md` and `.claude/skills/hi/SKILL.md` were rewritten. `sprint.md` and
  `glossary.md` are unchanged.

## Readings due

One Estimate stands `failed` and 18 stand `pending`. Every target stands `draft`: `entity-sprint-migration`
and each rule named below.

Failed:

- `estimate-sprint-migration-index-dissolved` — `entity-sprint-migration` — read line L138 of
  `vault/raw/2026-09-23/1126/spec.md`. Its Result: two live pointers at `index.md`,
  `guppi/materialize.py:11` and the Given of `estimate-case-protocol-case-form`, line 18.

From an unticked `- [ ] read …` line of `vault/raw/2026-09-23/1126/spec.md`:

- `estimate-hi-writes-frontier` — `rule-skill-hi` — L45.
- `estimate-prespec-reconciles` — `rule-prespec` — L137.
- `estimate-generate-fails-alone` — `rule-page-generation` — L214.
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` — L253, after
  the tasks of Case 365.
- `estimate-case-protocol-case-form` — `rule-case-protocol` — L307, L390, L520.
- `estimate-case-protocol-loaded` — `rule-case-protocol` — L308, L391, L521.
- `estimate-case-protocol-acknowledging-reply` — `rule-case-protocol` — L309.
- `estimate-prespec-binds-a-sprint-line` — `rule-prespec` — L425.
- `estimate-rules-schema-checked` — `rule-rules-schema` — L468, after the task L467
  `uv run pytest tests/test_schemas.py -k rules`.

No read line in the session's Spec; the place is the page's `method`:

- `estimate-agent-writing-followed` — `rule-agent-writing` — by hand in the next session: the section
  in `CLAUDE.md` and one reply of the agent against it.
- `estimate-carry-over-writes` — `rule-carry-over` — pytest over the skill's render, plus one live
  reading of a carried-over session.
- `estimate-documentation-completes` — `rule-documentation` — `make test-documentation`; the live
  reading by hand.
- `estimate-one-judgment-one-implementation-followed` — `rule-one-judgment-one-implementation` —
  `render --check` exit 0, then by hand the section in `CLAUDE.md` and the diff of the next Work
  Mode session.
- `estimate-session-phases-in-order` — `rule-session` — by hand at the close of a session.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` — the yaml and the brief after
  a librarian's run on the first marked lesson clustered under an `actioned` Insight.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — the tree by hand at the
  close of the sprint.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — `make lint` exit 0, or only
  unread lines on the sprint page's own Estimates.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — `make test` on the last commit
  of `migration`, then `git log` of `main` after the merge.

## Deferred

Four items. The one item of the previous brief,
`insight-workflow-ratified-content-changed-on-the-agents-own-finding`, went `actioned` by Case 373.
`insight-workflow-code-live-before-the-page-it-reads` is `open` and named by the sprint page, so it
is not listed here (case 229.4). `severity` counts the live children of an Insight; the other
children of these three are in the archive.

1. `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — `severity` 1, standing in
   1 brief. Pattern: a fact is signed on a check narrower than the claim; the command that ran
   answered one question and the sentence it supports makes a wider one. Proposal: a claim names
   the command its output rests on and is no wider than that output; a claim about a whole set is
   checked by a count on both sides.
2. `insight-workflow-contract-change-leaves-its-derived-text-stale` — `severity` 1, standing in
   1 brief. Pattern: a ratified change lands on one text and leaves the text derived from it
   behind, because no step names the dependents of a change. Proposal: resolve the dependents of a
   change in one pass at pre-task — for each changed slug, the Estimates whose Criterion quotes it.
3. `insight-session-vault-knowledge-not-loaded` — `severity` 1, standing in 1 brief. Pattern: a
   fact the vault holds does not reach the session that needs it; only `brief.md`, `CLAUDE.md`, the
   skills and the agent frames are loaded. Proposal: a second channel beside the brief — the ledger
   tail at `/hi`, and a way for a Rule page to name the lessons that bear on it; the second half
   was rejected by Case 134.
4. `rule-retro` — deferred by Case 375, no related Insight, standing in 1 brief: the report of
   `/retro` holds each fact once — the ratifications in one list; the unticked boxes of the Spec
   inside the list of what is not done.

## Flags

- `near`, from the index check (no page merged):
  - `lesson-case-protocol-chat-case-without-heading` near `lesson-case-form-the-spec-free-sections-written-last`.
  - `lesson-case-render-update-skipped-the-live-reading-estimate` near
    `lesson-plan-mode-contract-change-skips-the-estimates-blocks`, which stays `new`.
  - `lesson-plan-mode-frontier-refused-at-hi-again` near
    `lesson-plan-mode-frontier-refused-on-the-client-text`, which stays `new`. The handoff calls the
    two a pair; the older lesson's root cause is the client's text put above the project's rule,
    so the synthesis did not cluster it.
- `lesson-case-protocol-chat-case-without-heading` carries `addressed_by: decision-case-368` in the
  yaml; it has no pair, stays `new`, and its page holds no `addressed_by`.
- No entry is marked `incomplete`, `failed` or `unparsed`. The defer entry of 375 is marked `exists`.
- One Estimate stands `failed`: `estimate-sprint-migration-index-dissolved` (Readings due).
- `generate` printed no move to the Backlog and dropped no milestone in this run.
- Stale defers, from lint: `rule-work-mode` and `rule-subagent-guppi` 31 times since case 29,
  `rule-morph` 1 time since case 239. All three are on the sprint page.
- `rule-spec-box`: three findings — missing `kind`, missing `estimates`, orphan.
- No MOC candidate: no input this run names a threshold crossed.
- No contradiction found by this run.
- `guppi archive` moved no unit: 0034 and 1126 are dated the day of the run, and `archive` looks
  only at units dated before it; 1126 is the session of the run.
- `make lint`: 88 findings, exit 1 — 62 on 31 legacy decision pages (`missing section ## Context`
  / `## Problem`), 19 `unread` (18 `pending`, 1 `failed`), 3 on `rule-spec-box`, 3 `deferred`
  counters, 1 `unmigrated: 23 pages in the shape before case 193`. The handoff read 100 in Work
  Mode.

## Next session

Cases — what needs a decision:

- `estimate-sprint-migration-index-dissolved` stands `failed`: its reading found two live pointers
  at `index.md`; Cases 364.1 and 364.2 changed both texts. From its page and the handoff.

Work — what is done without a decision:

- Take the pending readings of Readings due, by slug: `estimate-hi-writes-frontier`,
  `estimate-prespec-reconciles`, `estimate-generate-fails-alone`,
  `estimate-sprint-migration-rule-class-files-dissolved`, `estimate-case-protocol-case-form`,
  `estimate-case-protocol-loaded`, `estimate-case-protocol-acknowledging-reply`,
  `estimate-prespec-binds-a-sprint-line`, `estimate-rules-schema-checked`,
  `estimate-agent-writing-followed`, `estimate-carry-over-writes`,
  `estimate-documentation-completes`, `estimate-one-judgment-one-implementation-followed`,
  `estimate-session-phases-in-order`, `estimate-synthesis-keeps-actioned-by-the-mark`,
  `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`,
  `estimate-sprint-migration-merges`.
- The unticked boxes of the Specs: 15 in `vault/raw/2026-09-23/1126/spec.md` (14 `read` lines and
  the task L467 `uv run pytest tests/test_schemas.py -k rules`); 14 `read` lines in
  `vault/raw/2026-09-23/0034/spec.md`.
- W1 and W2 of the Frontier stay open. From the handoff.
- No ledger line of 1126 was left unapplied. The tree at the close of this run holds only the
  librarian's own writes and the session's `handoff.md`; this brief's commit covers `vault`,
  `CLAUDE.md` and `.claude`.

## Readings at the close

- `make test`: 582 passed, 2 skipped.
- `make lint`: 88 findings, exit 1.
- Pages: 59 rules, 104 estimates, 53 lessons, 19 insights, 511 decisions, 4 entities.
