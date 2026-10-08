# Handoff — 2026-10-08, Frontier items from the brief of session 2114

## Notes from memory

- The person agreed with every recommendation of every round and ratified each Case as shown; Cases 727 and 730 were ratified a second time after `/pre-spec`.
- Case 729: the person accepted that the line it adds to the Criterion of `estimate-hi-writes-frontier` is read only by the person's word at the `/hi` after the close of a sprint, where no milestone item becomes a line and so no merge can show.
- Case 728 set `estimate-orchestration-defers-in-one-reply` `passed` by the person's decision, its Criterion written back unchanged and its `method` changed in the same update.
- The person asked why C6 stood beside C2 (one item, two sources); C6 closed as a duplicate and the cause became Case 729.
- The person asked about the Ask line of `estimate-hi-writes-frontier`; the agent answered that its moment has not come and the line stays open. The agent offered an item to keep such a line out of Ask until its moment; the person did not take it up.
- The sprint items `rule-sprint-close` and the close of `migration` were put off again; the agent recommended a session of its own for the close, since this session ratified Cases outside it.

## Direct instructions to the librarian

- `estimate-hi-writes-frontier` takes two updates in one Spec: Case 729 replaces its Criterion, Case 731 rewrites its `method` to open with "by hand:". Check that both land, and that `make lint` prints no `method` line for the page.
- Case 728 updates `estimate-orchestration-defers-in-one-reply` with `status: passed`, the Criterion unchanged and a new `method`; check the status, and whether the cascade moves `rule-orchestration` — it should stay `draft` unless every live Estimate of it is `passed`, the new `estimate-orchestration-batches-cases-out-at-once` and `estimate-orchestration-signs-a-batch-together` included.
- Case 727 carries `{supersedes:case 722.3}`: check that `decision-case-722.3` is set `superseded` and what happens to the `deferred_by` of `rule-case-protocol`.
- Case 730.1 and 730.3 set `insight-orchestration-items-taken-together-unruled` and `insight-workflow-case-written-without-reading-the-pages-it-changes` `actioned`. The lesson `lesson-case-build-finds-the-sentences-it-changes-by-their-words` has no mark and may cluster with the second Insight, which would reopen it.
- The lesson `lesson-hi-repeats-a-sprint-item-the-brief-carries` carries `{addressed_by:case 729}`.
- The brief's Next session should not repeat a sprint milestone item as a Cases line: `/hi` merges it after the render of Case 729, but the repeat this session came from that list.

## What actually got done

- Cases ratified: 727, 728, 729, 730 (730.1, 730.2, 730.3), 731. No Case is superseded by another of the session.
- Code and tests: none changed. `make test`: 1428 passed, 6 skipped. `make style`: clean.
- Readings: L13–L15, all `passed` — `estimate-orchestration-batches-cases-out-at-once`, `estimate-orchestration-signs-a-batch-together`, `estimate-case-build-writes-the-case`, each read on the new Render in the Spec.
- Lessons: L16 `lesson-hi-repeats-a-sprint-item-the-brief-carries`, L17 `lesson-case-build-finds-the-sentences-it-changes-by-their-words`.

## Debt

- No box of the Spec is debt; no test was reverted.
- 19 boxes wait for the librarian (pages, renders, reads); the box `read estimate-hi-writes-frontier` waits for the person.
- `estimate-hi-takes-a-conserved-spec` — a session that takes a conserved Spec, and the `/hi` of the session after the close of a sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — a `/work` that `/box` calls and the `/work` of the session that closes a sprint.
- `estimate-brief-written` — the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders` — `backlog.md` after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run` — after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint` — the librarian's run of the session after the close of a sprint.
- `estimate-sprint-close-takes-the-readings-in-groups` — after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges` — the Work Mode of the session that closes `migration`.

## Observations

- Red before the work: `make lint` exit 2 with 15 finding lines, among them `backlog: vault/wiki/backlog.md differs from its sources`, `estimates/estimate-hi-writes-frontier: method: a MOC's Estimate names no \`make <target>\`` and 13 `unread`/`deferred` lines on the Estimates listed under Debt, `estimate-orchestration-defers-in-one-reply` and `rule-morph`.
- No expected red: no task changed a check.
- `/pre-spec`: the `ask-guppi` run found seven points; five went back to Cases 727 and 730 and were confirmed closed. Two were left as known: the `context` of 728 on the cascade, which holds as a condition, and the method of `estimate-hi-writes-frontier`, which cannot show a merge.
- The `context` of Case 727 named a sentence 722.3 added to Splitting that the page does not hold; corrected at `/pre-spec`.
- The pre-spec check printed one `note:` on 730.2 — a Criterion line not carried word for word — which is the replacement the finding asked for.
- Each turn in Plan Mode carried the Claude Code reminder to end with a picker or `ExitPlanMode`; the agent kept to `orchestration.md` and called `ExitPlanMode` only after `/pre-spec`.

## For the next session

- The close of the sprint `migration` and `rule-sprint-close`, put off again: a session of its own.
- The brief puts a reading whose `method` waits for a later moment under `Ask the person` at every `/hi` (`estimate-hi-writes-frontier`), though it cannot be answered before the `/hi` after the close of a sprint.
- `lesson-case-build-finds-the-sentences-it-changes-by-their-words` has no fix: `case-guppi` finds the sentences a change touches by the words of one sentence.
- `/pre-spec` and the Case-file check leave the `method` of an Estimate on a MOC to lint, so a method naming only a test file passes until the librarian's run (left by Case 731).

## Ask the person

- `estimate-hi-writes-frontier` — needs the person — at the `/hi` of the session after the close of a sprint: did the Frontier come out as the Criterion says, an item closed `defer` or `kept` with no short Case but the short Case of a take-back, and no second line for a brief line that repeats a milestone item?
