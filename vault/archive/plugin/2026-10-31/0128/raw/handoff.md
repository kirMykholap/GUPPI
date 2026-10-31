# Handoff — 2026-10-31, backlog items and two-part readings

## Notes from memory

- The person took the recommended answer on most rounds with a short "Ок". Two answers went the other way: in Case 950 the person chose to fix both Estimates with a Retro part before a waiting part, not only the one the item named; in Case 955 the person chose a new Estimate over the existing `estimate-backlog-renders`, which the main agent offered as a third way since Case 953 uses it for the same kind of change.
- The person put off the sprint item of the clean branch (the push of `plugin` with a tag `prod-x.y.z` and the read of the CI run) again, with no reason given.
- The person kept `rule-ratification` in the backlog as it stands: its defer, the removal of `PLAIN_SPRINTS` from `.guppi/guppi/caseid.py`, waits for the close of sprint `plugin`. Its Case 951 was dropped with no decision line; its case file is empty.
- At `/pre-spec`, `ask-guppi` gave eleven findings; ten were closed in its confirmation. The person left finding 6 on Case 953 open (see `## Observations`).
- Case 954 grew from one sub-case to three over the rounds and `/pre-spec`: the trial needs an exception in `rule-orchestration` (954.2) and a reason in the frame of `ask-guppi` (954.3), and the trial waits for a session after this librarian's render, since the exception is not in the loaded rules of this session.

## Direct instructions to the librarian

- Four defers are retired by `{supersedes:...}`: case 910 on `rule-skill-sprint-open`, case 934 on `rule-spec-capture`, case 936 on `estimate-search-leaves-out-decisions-refuses-ask-guppi`, case 616 on `entity-guppi`. `backlog.md` should go from 8 items to 4; check each of the four pages has an empty `deferred_by` after generate.
- Case 950.2 replaces the Criterion of `estimate-orchestration-shows-the-built-case` whole: one line, on `ask-guppi` at pre-spec, is changed on purpose to except the start that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads, and one `－` line is added. `/pre-spec` printed a note that the line is not carried word for word; that is expected.
- Case 954.3 updates `rule-ask` with two `replace` pairs. `ask-guppi` compared their `old` texts only with the frame text it holds, not with the page `rule-ask`; check that each `old` stands on the page before applying, and flag one that does not.
- Renders due: `.claude/skills/sprint-open/SKILL.md` (Case 952), `vault/wiki/orchestration.md` (Case 954.2), `.claude/agents/ask-guppi.md` and `.claude/rules/search-leaves-out-decisions.md` (Case 954.3).
- The new lesson `lesson-plugin-cli-withholds-approval-in-every-window` sits beside `lesson-plugin-cli-withholds-approval-of-a-long-plan`. Both blame the Claude Code CLI; the new one rules out the terminal window. Judge at the index check whether it repeats the old page or stands as a new fact.

## What actually got done

- Cases ratified: 950 (950.1, 950.2), 952, 953, 954 (954.1, 954.2, 954.3), 955. Cases 950, 952, 953 and 954 were built again on the findings of `/pre-spec` and ratified again, 950 and 954 a third time on two findings of `guppi prespec --check` (a pointer to a session and to a case outside a bracket).
- Code and tests: none changed.
- `uv run --project .guppi guppi test`: 1822 passed, 6 skipped, 1 deselected, at the baseline, after the tasks and at Retro. `uv run --project .guppi guppi style`: clean.
- By hand in Work Mode: the test of Case 953 — the person ran the Claude Code CLI in the empty folder `C:\tmp\plan-approval-test` with the plan text of `resilient-munching-peacock.md`; the approval was withheld in a standalone PowerShell window (120×30) and in the terminal of VS Code (330×16). `pytest .guppi/tests/test_backlog.py` 18 passed; `pytest .guppi/tests/test_grepguard.py` 30 passed.
- Readings: L14 `estimate-skill-sprint-open-asks-the-goal-as-an-open-question` passed, L15 `estimate-backlog-renders` passed. Lesson: L16 `lesson-plugin-cli-withholds-approval-in-every-window`.

## Debt

- No box of the Spec is debt, and no test was reverted.
- 18 boxes wait for the librarian: the page lines, the four render lines and the `read` line of L14.
- `estimate-case-build-reads-each-list-of-a-new-member` — the `/pre-spec` of the first session on the Render of `rule-case-build` whose plan holds a Case that adds a member to a list; this session's plan held none.
- `estimate-orchestration-shows-the-built-case` — the first summary of `case-guppi` with a line `Other Case` in a session on the Render of `rule-orchestration` that this run renders.
- `estimate-search-leaves-out-decisions-refuses-ask-guppi` — the trial in the Work Mode of the session whose brief puts this reading under Work, after this run renders `orchestration.md`, `ask-guppi.md` and `search-leaves-out-decisions.md`; its test part passed in this session.
- `estimate-orchestration-starts-ask-guppi-for-a-hook-test` — the same trial.
- `estimate-ask-tries-a-decision-call-only-for-a-hook-trial` — the same trial.
- `estimate-guppi-keeps-no-defer-of-its-shape` — this librarian's run that applies Case 955; the next session reads `entity-guppi.md` and `backlog.md`.

## Observations

- Red before the work: `uv run --project .guppi guppi check` exit 1 with 13 lines at the baseline — the 12 pages with `core: true` that stand `draft`, as the brief lists them, and one line new since the brief: `backlog: vault/wiki/backlog.md differs from its sources`.
- Finding 6 of `/pre-spec` on Case 953 stands open by the person's choice: had the test blamed the terminal, nothing would have corrected the old lesson. The test blamed the CLI, so the two lessons agree.
- The event of the old method of `estimate-orchestration-shows-the-built-case` came in this session (the summary of Case 954 carried a line `Other Case` naming Case 950) under the old Render; Case 950.2 moved the reading to a session on the new Render, so it was not read.
- The plan of this session, much larger than 15347 bytes, was approved by `ExitPlanMode` in the VS Code extension.

## For the next session

- The bug of the approval of a long plan: the test shows the Claude Code CLI withholds it in any window, while the VS Code extension approves it. A Case decides the fix, such as a shorter plan file, an approval in the chat, or the extension as the way to approve a Spec.
- The sprint item of the clean branch stays open: the push of `plugin` with a tag `prod-x.y.z` and the read of the CI run.

## Ask the person
