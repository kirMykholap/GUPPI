# Handoff — 2026-10-30, the items of the brief of 2005 and the librarian's report in a file

## Notes from memory

- At /hi the person did not understand what A1 asked and why the agent could not read the report itself. After the explanation the person answered "Да, все было", and said that the Estimate is wrong, since the agent should check the report by itself; that became C7 and Case 944.
- The reading of `estimate-rules-schema-leaf-carries-no-how-it-works` at /hi was `failed` on its old Criterion, which asked that each fact of the dropped sections stand in a docstring, two of them false; Case 946.1 replaced that Criterion and Retro read it `passed`.
- Case 944, 945, 947 and 948 were built again after the findings of `ask-guppi` at /pre-spec and ratified again; only Case 944 gained a decision line (`update` of `rule-documentation`, the stop at step 1 of the librarian's frame); the others changed in `context` only.
- The person put off C1 of the sprint, the push of `plugin` with a tag `prod-x.y.z` and the read of the CI run, with no reason given.

## Direct instructions to the librarian

- `rule-documentation` takes two updates: Case 944 rewrites the step-1 sentence of the frame ("If it exits 1, write the report and stop"), and Case 946.2 drops the reason "since a subagent does not inherit the project's hooks" from its `## How it works`. They change different sentences.
- `rule-close` and `rule-documentation` both render into `.claude/agents/librarian-guppi.md`. Your own run still loads the old frame: write no `report.md` in this run.
- The decision lines of Case 944, 945, 947 and 948 stand twice in the ledger, the second time at the re-ratification after /pre-spec; the second carries no new mark, so apply each once. The one new line is the `update` of `rule-documentation` under Case 944.
- Case 949 is a defer of `estimate-plugin-install-sets-aside-the-files-of-the-project`, a page that stands; it enters `backlog.md` through `deferred_by`.

## What actually got done

- Cases ratified: 944, 945, 946 (946.1, 946.2), 947, 948 (948.1, 948.2), and the defer 949.
- Code: `.guppi/guppi/prespec.py` (`conserved_decisions`; `check_frontier` passes the decision lines of the conserved ledger to `check_backlog_defer_line`), and the module docstrings of `.guppi/guppi/guard.py`, `.guppi/guppi/ratified.py` and `.guppi/guppi/shellwrite.py`.
- Tests: `.guppi/tests/test_prespec.py`, three new tests of a backlog line put off again by a Case of a conserved Spec.
- `uv run --project .guppi guppi test`: 1822 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L1–L3 at /hi (L1 `failed`, L2 and L3 `passed`); at the end of Retro three `passed`, on `estimate-rules-schema-leaf-carries-no-how-it-works`, `estimate-shell-write-check-repairs-and-reports` and `estimate-prespec-checks-the-frontier`. No lesson.

## Debt

- No box of code, test or command is left unticked, and no test was reverted.
- 23 boxes of the Spec wait for the librarian.
- `estimate-close-reports-the-run` — the first librarian's run whose frame holds the new Render of `rule-close`, that of the next session: its `report.md` in the session folder.
- `estimate-where-to-stop-writes-each-step-whole` — the first stop of Work Mode whose reply asks the person to run commands by hand.
- `estimate-case-build-reads-each-list-of-a-new-member` — the /pre-spec of the first session whose `case-guppi` runs on the new Render of `rule-case-build`; its Retro part, the new Render in the Spec read against the Criterion, matched each line of it at this Retro.
- `estimate-case-build-reads-the-readers-of-a-changed-step` — the same /pre-spec.

## Observations

- `uv run --project .guppi guppi check` was red before the work: 13 lines, 12 pages with `core: true` that stand `draft` and `estimate-case-build-reads-the-readers-of-a-changed-step: unread: failed` (`## Baseline` of `work.md`). Case 948.2 sets that Estimate `pending`, so its line should leave after the librarian's run.
- `ask-guppi` at /pre-spec said it did not read the code of `remove_superseded` and its helpers, so the claim of Case 946 that the two wordings of the parent removal give the same result rests on `case-guppi` alone.

## For the next session

## Ask the person
