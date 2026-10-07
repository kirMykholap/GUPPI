# Handoff — 2026-10-07, dropped Cases and tag lines

## Notes from memory

- On Case 701 the person first chose (Q4 of its round) that the drop is checked by one more line in `estimate-case-build-writes-the-case`; on C4 the person kept that choice (Q2 (a)) knowing that the line holds the whole Estimate unpassed until a session after the render.
- On Case 702 the person chose to register the tag (Q1 (b)) against the recommendation to take `orchestration` off the pages; the declaration of `orchestration` itself was put to a later session (Q4 (a)).
- C4 needed no Case of its own: its `case-guppi` answered with a `**Fact:**` and wrote no file; the line closed under case 701.
- A1 (`estimate-permissions`): the person did not know whether `case-guppi` read a transcript. The agent counted the tool calls of the three `case-guppi` transcripts of this session: every `file_path` and `path` lay under `c:\PROJECTS\GUPPI`, none under `~/.claude/projects/` or elsewhere outside the project. The person agreed to keep A1 open. The person said that no permission prompt came while the Case files were written.
- C1 and C2 (`rule-sprint-close`, the close of migration) were put off `[-] · sprint · defer` for a session of their own; the person agreed.
- `/pre-spec`: `ask-guppi` gave 11 findings, the person answered one question (the turn of the short Case after a drop, (a)), Case 701 was built again with sub-cases 701.5–701.7 and Case 702 with `rule-case-check` in `given`; `ask-guppi` confirmed all 11 closed. It did not check that each new `old` anchor hits its page once, nor that the code tasks fit the code.

## Direct instructions to the librarian

- Case 701 was ratified twice: the first time with 701.1–701.4 (L1–L8), then again on the findings with 701.1–701.7 (L12–L18). The Spec holds the second form; read the Case from the Spec, not from the first lines. 701.2 gained an `update` of `rule-prespec-onward` only in the second form (L12).
- `rule-orchestration` is updated by 701.4, 701.5 and 701.6, `rule-prespec-onward` by 701.1 and 701.2: several `replace` pairs on one page; check each anchor before the render.
- The lesson of L27 shares its cause with the open Insight `insight-workflow-file-changed-through-a-shell-command`.
- Render: `.claude/agents/case-guppi.md`, `vault/wiki/orchestration.md` and `vault/wiki/case-schema.md`, by the render lines of the Spec.

## What actually got done

- Cases ratified: 701 (701.1–701.7) and 702.
- Code: `guppi/casecheck.py` (`dropped`, `other_blocks` takes the session folder and skips a dropped Case, `check_answer` and `judge_and_store` pass the folder); `guppi/onward.py` (`case_out` and `built_after` skip an empty Case file by `casecheck.dropped`); `guppi/ratified.py` (`read_tasks` reads a tag line into `new_tags` at the head of the `then` block, refuses one off the form). Tests: `tests/test_onward.py`, `tests/test_casecheck.py`, `tests/test_ratified.py`.
- `make test`: 1361 passed, 6 skipped. `make style`: clean.
- Readings: L19–L23 `passed`; L24 (`estimate-case-build-writes-the-case`), L25 (`estimate-orchestration-defers-in-one-reply`), L26 (`estimate-orchestration-shows-the-frontier-after-a-closed-line`) `failed`, Retro, not read. Lesson: L27.

## Debt

- No box of code, test or command is left unticked.
- 29 boxes wait for the librarian.
- `estimate-hi-writes-frontier`, `estimate-hi-takes-a-conserved-spec`, `estimate-brief-written`, `estimate-sprint-close-next-session-opens-the-sprint`: the session after the close of the sprint.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, `estimate-backlog-renders`, `estimate-sprint-close-runs-in-the-librarian-run`, `estimate-sprint-close-takes-the-readings-in-groups`, `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`: the session that closes the sprint.

## Observations

- `make lint` was red before the work, exit 2, 14 finding lines (1 `deferred`, 13 `unread`), as `## Baseline` of `work.md` holds; it was not run in Retro.
- The answer of `case-guppi` to a `SendMessage` came back each time in a turn of its own, as a task notification; the `**Waiting:**` step of 701.4 rests on this.
- No expected red: no task changed a check that reads a page this Spec updates.

## For the next session

- Declare the tag `orchestration` by a tag line in a Case, once the render puts the form into `case-schema.md`; that Case also needs a decision line of a page change (Case 702, Q4 (a)).
- No check stops a tag that `tags.md` does not hold from getting onto a lesson line or a `create` line; the warning of `guppi generate` stays the only signal (Case 702, Q2 (a)).
- `estimate-case-build-writes-the-case`, `estimate-orchestration-defers-in-one-reply` and `estimate-orchestration-shows-the-frontier-after-a-closed-line` stand `failed`: their readings wait for live moments after this session's render — a dropped Case, a decision put off, and the reply that closes a line with no ratification.
- A ratified Case that is sent back and then dropped still keeps the hook of `rule-prespec-onward` silent: its file is never emptied (Case 701, left not done).
- `rule-sprint-close` and the close of migration still wait for a session of their own.

## Ask the person

- `estimate-permissions` — needs the person — in a session where `case-guppi` reads a transcript under `~/.claude/projects/c--PROJECTS-GUPPI` or a path outside the project that no rule names: did that read and the write of its Case file, in `permissionMode: auto`, come with no permission prompt?
