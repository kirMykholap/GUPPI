# Handoff — 2026-10-05, backlog clean-up, the batch of items taken together, two pipeline fixes

## Notes from memory

- The person removed `rule-prespec-judges-the-spec-whole` outright: no measurement of the cost of an `ask-guppi` run enters the vault; the person looks at it alone.
- The person accepted every recommendation of the rounds and of the pre-spec report without changes.
- The person asked that the reading of the batch Estimate be taken on a real batch taken up after the new rule, not on Cases 676–680, which were shown one by one before the person stopped it; Case 681 was built again for that, then replaced by Case 684 after `/pre-spec`, which added 684.2.
- Case 682 leaves the `{addresses:...}` side unchecked by the person's choice; it is named as not done in the Case.

## Direct instructions to the librarian

- Case 683 changes `generate.decision`: an archived Decision that a later Case supersedes stays `archived`. Case 676 carries nineteen `{supersedes:case N}` marks (cases 183 … 322), and all nineteen Decision pages stand archived under `vault/archive/migration/2026-09-28/1318/decisions/`. Check after `generate` and `cleanup` that none of them came back under `vault/wiki/decisions/`, and that each took `decision-case-676` into `superseded_by`.
- Case 680 removes six lines from `## Backlog` of `entity-sprint-migration`, the line `[[rule-subagent-guppi]]` among them, and retires the defer of case 642; Case 676 deletes `rule-subagent-guppi`. Check that no live page links to `rule-subagent-guppi`, `rule-complaint-becomes-a-lesson` or `rule-prespec-judges-the-spec-whole` after the run.
- Case 684 supersedes Case 681; Cases 675–683 were ratified a second time after `/pre-spec` with the same ledger lines, so the ledger holds each line once.
- Case 679 rewrites the `pattern`, `## Pattern` and `## Proposal` of `insight-hi-skill-substitution-checked-by-a-model-call` and sets it `actioned`; Case 678 sets `insight-harness-one-rule-implemented-twice-drifts` `actioned` again.
- `backlog.md` should drop from 23 items to 15 after `guppi backlog`.

## What actually got done

- Cases ratified: 675, 676, 677, 678, 679, 680, 682 (682.1, 682.2), 683, 684 (684.1, 684.2).
- Code: `guppi/ledger.py` (`unmarked_lessons`, `held_message`, the hold in `run`, the module docstring), `guppi/generate.py` (`generate.decision` leaves an archived earlier page archived; the module docstring).
- Tests: `tests/test_ledger.py`, 13 new tests of the hold and 6 existing tests that now answer the hold; `tests/test_generate.py`, the archived-supersede test asserts the page stays archived.
- `make test`: 1279 passed, 6 skipped. `make style`: clean.
- Readings: L20–L24, all passed. Lessons: L25 (`{addressed_by:case 684.1}`), L26.
- The new hold of Case 682.1 ran live at Retro: it held L26 once and named the twelve Cases of the session; the line written again unchanged landed.

## Debt

- No box of code, test or command is unticked.
- 25 boxes wait for the librarian: pages, renders, the glossary and the five read lines of L20–L24.
- `estimate-hi-writes-frontier`: the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec`: a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: the `/work` of a session that closes a sprint, and a `/work` that `/box` calls.
- `estimate-brief-written`: the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders`: the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run`: after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint`: the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups`: after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`: the Work Mode of the session that closes the sprint.

## Observations

- `make lint` was red before the work, exit 2: 4 `deferred` lines and 11 `unread` lines, as `## Baseline` of `work.md` holds them; three of the `deferred` lines name pages that Cases 675, 676 and 677 delete.
- The `ask-guppi` run of `/pre-spec` reported that it ran a Grep over `vault/wiki/` that the frame of case 633.2 forbids it to run again; no finding rested on it.
- The `case-guppi` of Case 676 did not take the line `[[rule-subagent-guppi]]` off the sprint page as the dispatch asked, since only the Case that retires the defer of case 642 may change that page; Case 680 took it.
- The hold of Case 682.1 asks about every unmarked lesson after any decision line, so the reply that ends Retro of a session that ratified Cases is held once for each such lesson.

## For the next session

- The rest of the backlog groups the person saw: Plan Mode and pre-spec (`rule-prespec-onward`, `insight-prespec-after-findings-loop-unruled`, `insight-case-show-built-case-retyped-by-hand`); the knowledge of the agent (`insight-session-vault-knowledge-not-loaded`, `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`); Work Mode (`rule-work-mode`, `rule-spec-box`); strategy (`entity-guppi`, `rule-morph`).
- `rule-sprint-close` and the close of migration stay for the session that closes the sprint.
- The `{addresses:...}` mark on a decision line written after an unmarked lesson stays unchecked (Case 682).

## Ask the person
