# Handoff — 2026-09-28, the broken fence of case 483 and Slice 3g, the Given pass

## Notes from memory

- The person asked why the fence break of case 483 reached the librarian. The first idea was a full trial run of `materialize`, `generate` and `render` in Work Mode, on a branch or a worktree. After the discussion the person saw that such a run would not have caught the break: no check read a code fence. They dropped the trial run, and nothing records it.
- On Case 489 the person chose to restore the two Criteria that case 211.3 overwrote, from the archived Spec of session 2238 (211.1) and the librarian's commit `ebaef1e` (201.5). They kept `estimate-generate-writes` as one page with 12 `＋` lines, with no split and no backlog item, against the recommendation to put the split in the backlog.
- At pre-spec, `ask-guppi` found that 488.6–493.6 promised the Slice 3g note "still shows", while 494.6 of the same Spec removes it. All of 487–494 were built again and ratified a second time. The History `change` lines of 488.6–493.6 still end with "the note on every other Estimate stands"; the person chose to keep them as they are.
- The person chose not to fix `decision-case-13` (a fence open to the end of its `## When`) in this session. It stays with the old Decision pages 1–28.

## Direct instructions to the librarian

- Apply Case 487 whole: 487.4 was added at pre-spec, and its ledger line (L51) stands after the defers 495 and 496.
- After the run, `make lint` holds the class `fence`. It should report only `decisions/decision-case-13` once 486 and 487.3 are written. A `fence` finding on `rules/rule-retro` or `rules/rule-synthesis` after the run means a pair did not apply.
- 494.6 removes one line of `## Milestones` of `entity-sprint-migration` with a two-line anchor. Check that `vault/wiki/sprint.md` shows Slice 3g with the one note on the old shape after `guppi sprint`.
- 489.1 and 489.2 set `purpose` on two Estimates that lacked it, and 493.2, 493.3 and 493.5 set it on three more.
- Cases 488–494 repeat one form over 38 Estimates. A failed entry is most likely an anchor or a Criterion kept by `sections`; no Case writes `sections: Criterion`.

## What actually got done

Ratified: 486, 487.1–487.4, 488.1–488.6, 489.1–489.8, 490.1–490.8, 491.1–491.5, 492.1–492.4, 493.1–493.6, 494.1–494.6, 495, 496.

What got done: commits b67fc6c (code) and d7ad72f (the session folder); `guppi/materialize.py` (`fence_breaks`), `guppi/prespec.py` (`check_pairs`), `guppi/lint.py` (the class `fence`), tests in `tests/test_materialize.py`, `tests/test_prespec.py` and `tests/test_lint.py` (+15); the stale `materialize.cpython-314.pyc` and `pretask.cpython-312.pyc` deleted; make test 891 passed, 2 skipped; make style clean.

What is not done:
- `make lint` red in the class `fence` on `rule-retro` and `rule-synthesis` — handoff note: expected red, waits for this run to write 486 and 487.3. The person saw the break live: the Retro of this session showed its report skeleton and the commit paragraph as one code block.
- `make lint` red in the class `fence` on `decision-case-13` — handoff note: expected red, stays red after this run, with the old Decision pages 1–28.
- The 109 findings of the Baseline — handoff note: red before the work.
- The pair check of pre-spec judged only the anchor count — lesson `lesson-prespec-judged-a-pair-by-its-anchor-alone` (L52), addressed by case 487.
- Case 211.3 overwrote two ratified Criteria — lesson `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` (L53).
- The eight pre-spec findings of `ask-guppi` in the contexts of 487–494 — handoff note: fixed and ratified again in this session.
- The task line of 487.2 said "each give one `fence` finding"; a run with text after it and no later close gives two findings — handoff note: the lint test closes the fence, the pre-spec test covers the case with two.
- `guppi/__pycache__/__init__.cpython-314.pyc` left in place — handoff note: stale like the two deleted, not named in the brief.
- The readings of Readings due and the unticked `read` lines of the Specs of sessions 2000, 1318 and 0000 — handoff note: not done, left for a later session.
- The harness filter "settings-json" fired twice on answers of `case-guppi` — handoff note: a false alarm on a `given` line naming `.claude/settings.json`.

53 boxes wait for the librarian.
Read in a later session: `estimate-prespec-catches-a-broken-fence`, `estimate-lint-catches-a-broken-fence`, `estimate-materialize-judges-a-fence`, `estimate-glossary-renders-the-terms`, `estimate-glossary-checks-the-file`, `estimate-glossary-ticks-the-spec`, `estimate-glossary-terms-defined`, `estimate-guppi-tests-green`, `estimate-generate-writes`, `estimate-generate-walks-dates`, `estimate-generate-renames`, `estimate-generate-rewords`, `estimate-generate-writes-rules-from-applies-to`, `estimate-materialize-lifts-unfiltered-on-a-schema-change`, `estimate-materialize-refolds-a-reading-on-a-supersede`, `estimate-page-schemas-one-file-per-rule`, `estimate-rules-schema-checked`, `estimate-entities-schema-checked`, `estimate-estimates-schema-checked`, `estimate-decisions-schema-checked`, `estimate-lessons-schema-checked`, `estimate-vault-layout-holds`, `estimate-sprint-ticks-the-spec`, `estimate-sprint-checks-the-file`, `estimate-sprint-drops-an-emptied-milestone`, `estimate-render-harness-ticks-the-spec`, `estimate-atomicity-rendered`, `estimate-claude-md-rendered`, `estimate-one-judgment-one-implementation-followed`, `estimate-compact-recall-reloads`, `estimate-plan-mode-verified`, `estimate-retro-commit-gates`, `estimate-session-phases-in-order`, `estimate-prespec-hook-gates`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-merges`, `estimate-sprint-migration-rule-class-files-dissolved`, `estimate-sprint-migration-index-dissolved`.
