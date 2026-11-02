# Handoff — 2026-11-02, sprint plugin: the note of names and the English headings

## Notes from memory

- The person took the recommended option in each round: C4 closed with no Case (the `!` git lines of `/work`, `/box`, `/carry` and `/handoff` stay, since `/hi` stops first outside a git repository); Case 1005 moves the names search of `case-guppi` into the hook of `rule-case-check`; Case 1006 actions the Insight on English headings.
- The person held C1 until the W lines pass. The agent answered that W1–W3 do not block the clean build: by `is_draft_core` of `.guppi/guppi/pages.py`, `rule-case-build` and `rule-orchestration` block only through Estimates that stand `failed`, and this session sets both pages free once the librarian applies it. That is read from the code; no build has run.
- The readings of `estimate-orchestration-acknowledging-reply` were taken by the agent on its own replies in this session's transcript.
- Caveat on Case 1005.1: built as ratified, but a probe shows the note can list hundreds of files for one Case (Retro lesson on the note's breadth).

## Direct instructions to the librarian

- Check first, and say in the brief: after this run, does `guppi check` still name `rule-case-build` or `rule-orchestration` as `a page with core: true that is draft`? C1, the push to prod, waits on that answer.
- `estimate-orchestration-acknowledging-reply` has two `passed` readings, L7 and L9; L9 reads both replies the `method` names and is the one to keep as the result.
- Case 1006 sets the Insight `actioned` with `addressed_by: decision-case-1002`; the cascade should archive its two lessons and keep the Insight.
- The decision lines of Cases 1005 and 1006 stand once each in the ledger, though both were ratified again after `/pre-spec`.
- The plan file holds Case 1005 and Case 1006 only; Case 1004 was dropped with no decision line.

## What actually got done

- Cases ratified: 1005 with 1005.1, 1005.2, 1005.3; 1006.
- Code: `.guppi/guppi/casecheck.py` gains the note of names (`looked_files`, `carried_names`, `changed_targets`, `named_files`, `name_pattern`, `names_notes`, joined to `check_answer` by `looked`); `.guppi/tests/test_casecheck.py` gains eight tests and its fixture plan moves under a home folder.
- `uv run --project .guppi guppi test`: 1904 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L7 and L9 `estimate-orchestration-acknowledging-reply` passed; L10 `estimate-case-check-notes-the-files-that-name-what-a-case-changes` passed. Lessons: L11 (knowledge, the breadth of the note of names), L12 (error, a Frontier closer appended without its box).

## Debt

- No box is debt.
- 10 boxes wait for the librarian.
- `estimate-case-build-searches-the-names-of-what-it-changes` — waits for the `/pre-spec` of the first session in which the hook of `rule-case-check` sends `case-guppi` a note of names.
- `estimate-case-build-reads-each-list-of-a-new-member` — waits for the first later build whose Case adds a member to a list.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — waits for the first `/work` that loads in the Claude Code CLI while `guppi check` exits 1; this session's `/work` loaded in the VS Code extension.
- `estimate-retro-loads-on-a-red-command` — waits for the first load of `/retro` in the Claude Code CLI; this session's loaded in the VS Code extension.
- `estimate-synthesis-keeps-actioned-by-the-mark` — waits for a librarian's run that puts a lesson with `addressed_by` under an Insight that stood `actioned` before the run.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — waits for the owner's push of `plugin` and a tag `prod-x.y.z` after this run, before the close of `plugin`.

## Observations

- Red before the work: `guppi check` exit 1 with five lines — `rule-case-build` and `rule-orchestration` as core pages in draft, and three `failed` Estimates (`estimate-case-build-reads-each-list-of-a-new-member`, `estimate-case-build-searches-the-names-of-what-it-changes`, `estimate-orchestration-acknowledging-reply`).
- The fixture of `test_casecheck.py` kept its plan file under the made-up project's `.claude/plans/`, so the new note searched it and eleven tests broke; Claude Code writes plans under the home folder, so the fixture now does too, and the hook leaves out its own store `*.checked.json`.
- In the VS Code extension `/work` and `/retro` came to the agent as instructions to run their `!` commands, as `lesson-vs-code-extension-hands-the-skill-preamble-to-the-agent` records.
- No expected red.

## For the next session

- C1: if `guppi check` names no core page in draft after this run, the owner pushes `plugin` and a tag `prod-x.y.z`, and the session reads the CI run.
- The breadth of the note of names (L11): whether the hook narrows what it notes, such as the paths of a task line that only imports a module, or names that hundreds of texts hold — a decision once the first real note is seen.
- `estimate-synthesis-keeps-actioned-by-the-mark`: proposed to defer into the backlog, since its event may not come for long.
- W1 and W2 need a Work Mode run from the Claude Code CLI.

## Ask the person
