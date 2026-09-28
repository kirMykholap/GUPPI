# Handoff — 2026-09-28, Plan Mode on the brief and the backlog Insights

## Notes from memory

- The person asked for a plain explanation three times, all in the rounds of case-guppi. Twice the agent gave it in its own words, without case-guppi: the non-blocking hook of 472, and the whole of 473 with its fallback. This is a signal for `rule-case-build` (the clarity of a round) and `rule-agent-writing`.
- The person first deferred the fallback half of 473 together with `rule-work-mode`, then took it up in the same Case. The sentence on a red check stands in `rule-retro` for now. The person wants to decide where it belongs when `rule-work-mode` is taken up.
- In 471 the person first doubted the ban on reading the archive, then chose a read by slug with no hook. The notes of 472 threshold at 60 percent of shared words. Nobody measured that number, and the person accepted it as it is.
- The person touched `cases/case-471.md` by hand at its first showing and put it back. The code spans of the file lost their padding, which looks like an editor format on save. The Spec was written from the stored answer and was not affected.

## Direct instructions to the librarian

- Case 471, 471.1 and 471.2 are superseded by Case 474 through three `{supersedes}` blocks on the lines of 474.1 and 474.2. The Spec holds no Case 471. Its ledger lines (the first ratification of `case 471` and the re-ratification of `471.1` and `471.2`) need no page of their own beyond what `generate` does with a superseded Case. `cases/case-471.md` stays in the folder as the file that was shown.
- The `rule-atomicity` line of 472.3 stands in the ledger among the re-ratification lines of 03:31:13, not beside the other lines of 472.3.
- `rule-prespec` is updated by 472.1, 472.2 and 472.3, and `rule-case-check` by 472.1 and 472.2. Each pair's anchors are in different sentences, and 472.1's anchor on `rule-case-check` ("a later answer for the same id replacing it.") is its own.
- `make lint` stops at `backlog --check` until `guppi backlog` runs: this session closed a Frontier line `· backlog · kept`.

## What actually got done

Ratified: 470, 472.1, 472.2, 472.3, 473.1, 473.2, 474.1, 474.2, 475.

What got done: commit 0bdffcc — `guppi/prespec.py` and `guppi/casecheck.py` changed, with their tests in `tests/test_prespec.py` and `tests/test_casecheck.py`. `make test` gave 856 passed, 2 skipped, and `make style` was clean. Readings: `estimate-case-check-requires-a-backlog-item-decided-on-its-page` `passed`, and `estimate-language-followed` and `estimate-agent-writing-followed` `failed`. Lesson `lesson-spec-write-keeps-the-body-of-a-case-rebuilt-as-a-parent`.

What is not done:
- The Spec hook keeps the body of a Case rebuilt as a parent: a short defer, Case 475, on `rule-spec-write`.
- The Criterion of `estimate-sprint-migration-file-route-gone` has an unclear line, "`make lint` has no finding on a schema". Read as "no `schema:` finding", it fails today on 64 findings (the Decision pages of cases 1–28 and `rule-spec-box`). Read as "no finding on a schema page", it passes. A question for the next Plan Mode. The grep and pytest parts of its method pass today.
- `make lint` was red on `backlog --check` in Work Mode because this session's Frontier put an item off `kept`. This is the case of 473.1: the check is read at the librarian's run.
- The notes of 472 are loud on a real plan. `guppi prespec --check` on this session's Spec printed 19 notes: reworded lines of the Criteria of 470, 472.3, 474.1 and 474.2, the old-shape lines of `estimate-synthesis-clusters` (`### case 147.4` among them), and one sibling pair 472.1/472.3. The first reading of the note Estimates should judge whether that many is workable.
- The agent answered in English in the chat on Case 471: lesson `lesson-chat-language-follows-the-last-english-file-read`.
- Three requests for a plain explanation: a note, written above under Notes from memory.
- `estimate-case-protocol-shows-the-built-case`: read `passed` at Retro.
- Not read in this session, each for the reason given: `estimate-case-build-writes-the-case` (no `create` without a `ref` was dispatched); `estimate-prespec-requires-a-backlog-item-decided-on-its-page` (pre-spec ran with the closed `backlog` lines C5 and C6 and gave no finding, but no reading line was written); `estimate-generate-writes-the-decision-page` (the live part is the librarian's run); `estimate-retro-report-holds-each-fact-once` and `estimate-handoff-holds-each-fact-once` (this Retro and this handoff are the first after their render, readable from the transcript in the next session); `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-check-shows-only-the-checked-case` and `estimate-event-log-records` (their parts by hand did not occur); `estimate-carry-over-writes`, `estimate-case-protocol-defers-in-one-reply`, `estimate-case-protocol-ledger-line-form` and `estimate-context-size-warns-past-the-limit` (their occasion did not come); `estimate-session-phases-in-order` (at the close of the session); `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean` and `estimate-sprint-migration-merges` (at the close of the sprint); `estimate-spec-write-reaches-the-approved-spec` (no Case was ratified in Work Mode).

27 boxes wait for the librarian.

Read lines that wait for a later session: `estimate-skill-grill-me-asks-in-rounds`, `estimate-case-check-notes-a-criterion-line-not-carried`, `estimate-case-check-notes-a-then-line-shared-by-siblings`, `estimate-prespec-checks-the-form-of-an-item`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`, `estimate-documentation-completes`, `estimate-synthesis-clusters`.
