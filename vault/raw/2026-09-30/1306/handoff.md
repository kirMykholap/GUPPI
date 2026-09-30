# Handoff — 2026-09-30, the check of case-guppi, recommend on the Decision page, the leading indent of a replace pair

## Notes from memory

- The person asked to check whether `estimate-glossary-terms-defined` passes now; the reading came back failed on one more row, and the fix became Case 541 on that row alone — the looser wording of `deferred_by` in the glossary, `rule-rules-schema` and `rule-entities-schema` was left, by the person's choice.
- On C5 the person drove the scope: they wanted the answers of the rounds kept and carried onto the Decision page, asked whether a hook could write them mechanically (no: a hook cannot translate), leaned to the name `recommend` over a new `## Choices`, and wanted `problem` on the parent only, with a graph edge parent ↔ sub-case. They kept it one Case against the agent's advice to split it; Case 544 ended with eleven sub-cases.
- The person objected when the first build of 544 showed, under `recommend`, a recommendation (`## Note`) a later round had replaced; the rule "the latest recommendation and the latest answer" came from that.
- The person asked why a sub-agent's file list is harmful; they accepted that paths already stand beside the quotations and in `given`.
- The person asked why the Frontier said "Retro" and not `/retro`; the answer (a phase, not the command) satisfied them, nothing to change.
- The person chose C2 with C3, not C3 with C5.
- Pre-spec found sixteen points; the person agreed to every proposed fix and to move the defer of C4 from `rule-skill-grill-me` to `rule-orchestration`.

## Direct instructions to the librarian

- Case 545 was superseded in its own session by Case 546 and left the Spec; its ledger line stands.
- `rule-case-build` is changed by 543.1, 544.1 and 544.2; `rule-case-protocol` by 543.3, 544.2 and 544.3; `rule-spec-write` by 542 and 544.5; `rule-page-generation` by 543.3 (a `change` line alone) and 544.7; `entity-glossary` by 541 and 544.8 on different rows; `rule-case-check` by 544.3 and 544.4. Pre-spec replayed every pair in order with no miss; check the pages after the run all the same.
- 544.1 deletes `rule-case-build-checks-its-sub-cases` and supersedes case 480; it sets both Insights `actioned`, so the cascade archives their lessons.
- The renders this run owes: `.claude/agents/case-guppi.md`, `.claude/skills/grill-me/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/case-schema.md`, `vault/wiki/decisions/schema.yaml`, and `guppi glossary`.
- The code of 544.6 and 544.7 is built before this run: `materialize` now gives a parent Case a record of its own with `children`, and `generate` writes its page. Look at what it does to the units still under `raw/` from earlier sessions (0138, 0248): their parent Cases (such as 534, 538, 539) may get new Decision pages. The ratified Cases say a parent gets a page; nobody decided it for Cases of earlier sessions. Report what was written.
- This session's Spec was written by the old Spec hook and holds no `recommend`, so no page of this session gets `## Recommend`.

## What actually got done

- Cases ratified: 541, 542, 543.1, 543.2, 543.3, 543.4, 544.1 to 544.11, 546 (a defer of `rule-orchestration`). 542, 543 and 544 were built again after pre-spec and ratified again.
- Code: `guppi/spec.py`, `guppi/ratified.py`, `guppi/materialize.py` (Retro out of the defer texts, 542); `guppi/generate.py` (the leading indent of a `replace` old, `indent_added_twice`, the Decision page with `## Recommend`, the parent page and `parent`); `guppi/prespec.py` (the indent finding); `guppi/casecheck.py` (the titles of the rounds in `recommend`, no `problem` in a sub-case); `guppi/ratified.py` (`recommend` in the Spec); `guppi/materialize.py` (the parent record, the sub-case inheriting `context` and `given` alone); `guppi/lint.py` (a parent page, the origin of a parent).
- Tests: `tests/test_generate.py`, `tests/test_prespec.py`, `tests/test_casecheck.py`, `tests/test_ratified.py`, `tests/test_materialize.py`, `tests/test_lint.py`, `tests/test_schemas.py`.
- `make test`: 964 passed, 3 skipped. `make style`: clean.
- Readings and lessons: ledger lines 1 to 3 (at `/hi` and in Plan Mode) and 43 to 48 (Work readings and Retro).

## Debt

- `read estimate-case-build-writes-a-plain-round` (543.1) and `read estimate-skill-grill-me-asks-in-rounds` (543.2): their method names a round of case-guppi in a later session after the render.
- 48 boxes wait for the librarian: the page, render and glossary lines.
- The `read` lines of Estimates this session creates or updates wait for a later session: `estimate-spec-write-writes-a-defer`, `estimate-generate-replace-takes-the-leading-indent`, `estimate-prespec-catches-an-indent-added-twice`, `estimate-case-build-checks-the-finished-case`, `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-check-refuses-a-problem-in-a-sub-case`, `estimate-spec-write-copies-the-ratified-case`, `estimate-materialize-assembles`, `estimate-generate-writes-the-decision-page`, `estimate-decisions-schema-checked`, `estimate-lint-finds-a-broken-link`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-case-protocol-case-form`.

## Observations

- Red before the work: `make lint` exit 2 with 85 lines in the Baseline, the same 85 after the work. Once `decisions/schema.yaml` renders with `## Problem` optional (544.8), the findings "missing section ## Problem" on the old Decision pages should go.
- Expected red: the new test of `tests/test_schemas.py` for 544.8 is skipped until the render of `vault/wiki/decisions/schema.yaml`; that is the third skipped test.
- Between the build of 544.3 and the render of the case-guppi frame, a dispatch of case-guppi that runs a round would be sent back: the hook already requires the titles in `recommend`, the frame does not ask for them yet. No dispatch ran in that window.
- The indent of `**Options:**` in the rounds of case-guppi came in most rounds of this session but not in all.
- The Case file of 541 carries a typo in its `context` ("does not names"); the person chose to leave it.
- Readings not taken, their moment not come: `estimate-ask-finds` (three dispatches of ask-guppi needed, one ran), `estimate-case-build-writes-the-case` (no `create` without a `ref` this session), `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-shows-only-the-checked-case` (no answer sent back, no reply refused), `estimate-case-protocol-ledger-line-form`, `estimate-case-protocol-shows-the-built-case` (at the close of a session), `estimate-compact-recall-reloads` (no compaction), `estimate-documentation-completes`, `estimate-end-of-work-order`, `estimate-event-log-records` (no `/hi` outside plan mode), `estimate-generate-rewords` (no reword), `estimate-generate-writes` (the live reading waits for this run with the new code), `estimate-governed-files-hook-refuses` (no refused edit of a governed file), `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-plan-mode-verified` (no vault query this session), `estimate-python-utf8-output-intact` (the Stop line of `guppi context` shows its dash only past 400 000 tokens), `estimate-retro-commit-gates`, `estimate-retro-loads`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` (no check went red on a page), `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-runs-on-to-the-handoff`, `estimate-session-phases-in-order`, `estimate-session-start-context`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (no `/work` typed by the person), `estimate-work-mode-takes-the-work-readings` (its own run; read it from this transcript), `estimate-brief-written`, `estimate-carry-over-writes`.
- `work.md` was written through Bash again, and its `## Expected red` by Edit.

## For the next session

- `estimate-hi-takes-its-readings` failed: at `/hi` the agent opened the pages of Estimates it did not read. Does `/hi` decide the moment of a reading from the method line of the brief alone, or may it open the page to decide?
- `estimate-glossary-terms-defined` stays failed until its table is read again after this run writes the row of Case 541.
- The parent Decision pages that this run may write for Cases of earlier sessions (see the instructions above): keep them, or limit the parent record to the Cases of the unit's own session?
- The rows `deferred_by` of the glossary and the field texts of `rule-rules-schema` and `rule-entities-schema` still say a `supersedes` clears `deferred_by`, without the condition that the superseding Case names the page.

## Ask the person

- `estimate-permissions` — needs the person — When the agent changed `vault/raw/2026-09-30/1306/work.md` in Work Mode with the Edit tool, did Claude Code ask you for permission?
