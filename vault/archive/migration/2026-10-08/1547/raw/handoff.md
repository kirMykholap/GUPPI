# Handoff — 2026-10-08, Case 733 taken up again, the test of a changed check, two tags

## Notes from memory

- The person took up the two brief items on Case 733 and on the lesson of the missed example in one answer, as a batch, and agreed with every recommendation of every round.
- The brief planned to change the example of `rule-case-example` and apply `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff` in one session. The `case-guppi` of Case 735 found that order fails again: `vault/wiki/case-example.md` is rendered only at the librarian's run, so the patched check would meet the old example in Work Mode. The person chose the example now and the patch in a later session.
- The person put off both items of the sprint's Slice 5, `rule-sprint-close` and the close of `migration`, as `· sprint · defer`, since the close is a session of its own.
- `/pre-spec`: the check printed no finding, only three `note:` lines on Case 736 (the 9 `given` lines of 736.2, the replaced last line of the where-to-stop Criterion, a `then` line of 736.3 close to one of 736.2), answered as no finding. `ask-guppi` made four findings; three went to their `case-guppi` without a word of the person, one needed it: Case 737 tags a lesson that the cascade of 736.1 archives in the same run, and the person chose to keep the target and say so in the Case. `ask-guppi` confirmed all four closed; Cases 736 and 737 were ratified a second time.
- The reading of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` rests on the text of the Render in the Spec and on the `/work` of this session at the fork; a `/work` that `/box` calls and the `/work` of a session that closes a sprint, which its `method` names, were not observed.
- The `/work` of this session ran under the old skill, so the full `make test` run after the last task that Case 736.2 adds did not run as a step of Work Mode; Retro ran the full suite.

## Direct instructions to the librarian

- Order matters for Case 737 and Case 736.1: 737 sets the tags of `lesson-case-build-misses-the-example-a-changed-check-runs-over`, and 736.1 sets its Insight `insight-workflow-contract-change-leaves-its-derived-text-stale` `actioned`, so the cascade archives that lesson in the same run. Check that the lesson keeps `case-build` and `prespec` under `vault/archive/`, and that both tags land in `tags.md` from the `new_tags` of 737.
- Judge the cluster of the lesson `lesson-case-build-misses-the-cascade-of-a-related-case`. Joined to `insight-workflow-contract-change-leaves-its-derived-text-stale`, it would reopen the Insight that 736.1 sets `actioned` in this run; its cause is the cascade a related Case sets off, not a text derived from a change.
- `guppi backlog` should drop the Insight once it is `actioned`: it holds no `deferred_by`.
- Each `replace` old text of this Spec stands once in its page (checked at Retro by Grep on `rule-case-example`, `rule-case-build`, `rule-work-mode` and `rule-where-to-stop`).

## What actually got done

- Cases ratified: 735, 736 (736.1, 736.2, 736.3), 737. None is superseded.
- Code and tests: none changed. `make test` 1428 passed, 6 skipped; `make style` clean.
- Readings: L10 `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check` `passed`, L11 `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` `passed`, L12 `estimate-where-to-stop-stops-only-on-its-conditions` `passed`, each read on the new Render in the Spec.
- Lesson: L13 `lesson-case-build-misses-the-cascade-of-a-related-case`, tagged `case-build`, which the ledger hook took after the ratification of Case 737.

## Debt

- No box of the Spec is debt, and no test was reverted.
- 16 boxes wait for the librarian: the page, render and `read` lines of the five Cases.
- `estimate-prespec-catches-a-method-without-a-form` — `failed`; its reading waits for the patch of Case 733, applied in a session after the render of `vault/wiki/case-example.md`.
- `estimate-hi-takes-a-conserved-spec` — a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — `backlog.md` after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone` — the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-lint-clean` — `make lint` in the Work Mode of the session that closes the sprint.
- `estimate-sprint-migration-merges` — `make test` on the last commit of `migration`, in the Work Mode of the session that closes it.

## Observations

- Red before the work: `make lint` exit 2 with 14 finding lines in `## Baseline` of `work.md`, among them `backlog: vault/wiki/backlog.md differs from its sources`, `rules/rule-morph: deferred: 1 time since case 239`, 11 `unread: pending` and 1 `unread: failed` (`estimate-prespec-catches-a-method-without-a-form`).
- No `## Expected red`: no task of this Spec changes a check.
- The Spec has no task of code; every box is a page, render or `read` line.

## For the next session

- Apply `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff` once `vault/wiki/case-example.md` holds the `make test-cart` method of Case 735, format it with `make style`, and read `estimate-prespec-catches-a-method-without-a-form`; the patch holds the 4 unticked code boxes of Case 733 in the 0213 Spec.
- `lesson-case-build-misses-the-cascade-of-a-related-case` has no fix: no step makes `case-guppi` follow the status cascade that a related Case of the session sets off onto the pages its own Case changes.
- The close of `migration` and `rule-sprint-close`: a session of its own.

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
