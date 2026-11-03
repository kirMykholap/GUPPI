# Handoff — 2026-11-02, the acknowledging reply and skills that load on a red check

## Notes from memory

- Case 1003: the person turned down a skill text in which the agent runs the tests and the check by hand, and asked that they run by themselves when the skill loads. The person also said that a core page in `draft` must block CI and the push of the plugin to prod, not the work. The flag `--exit-zero` serves both: without it the commands stay red.
- Case 1003.3: its reading waits for a live load of `/work`. In the VS Code extension the load does not fail on a red check (L21), so the reading means something only in the CLI.
- The trial of `estimate-spec-box-runs-a-conserved-spec` (L6) ran a Spec of two short-form defers with no task. The chain of `/box` held, but no task ran on the spec branch.
- In the trial of `estimate-skill-approve-spec-takes-the-spec` (L4) the CLI did offer the approval of the plan. The person pressed Esc on purpose, to try `/approve-spec`.
- The person put off C1, the clean branch, with no word on when.

## Direct instructions to the librarian

- Check first whether L7 (`lesson-work-skill-fails-to-load-on-a-red-check`) and `lesson-hi-fails-outside-a-git-repository` share a root cause: Claude Code refuses a skill whose `!` command exits non-zero. L21 (`lesson-vs-code-extension-hands-the-skill-preamble-to-the-agent`) bears on the same mechanism in another client. L12 carries `{addresses:lesson-work-skill-fails-to-load-on-a-red-check}`.
- `estimate-skill-approve-spec-takes-the-spec` passed (L4). Check whether the cascade sets `rule-skill-approve-spec` `built`, and report which pages `guppi check` still names as `core: true` and `draft` after the run.
- The `replace` of Case 1003.1 on `rule-guppi-config` replaces a sentence of its Purpose.
- Case 1002 sets only the `method` of `estimate-orchestration-acknowledging-reply`; it stays `failed`.

## What actually got done

- Cases ratified: 1002; 1003 with 1003.1–1003.4.
- Code: `.guppi/guppi/commands.py` gains `add_exit_zero` and `exit_zero`, used by `guppi test` and `guppi style`; `.guppi/guppi/check.py` imports both for `guppi check`. Tests: `.guppi/tests/test_commands.py` (3 tests), `.guppi/tests/test_check.py` (2 tests).
- The `read estimate-close-reports-the-run` box of `vault/archive/plugin/2026-11-01/2227/raw/spec.md` ticked by hand in Work Mode, since its reading passed in session 0254.
- `uv run --project .guppi guppi test`: 1896 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L1 `estimate-clean-branch-refuses-a-draft-core-page` passed; L4 `estimate-skill-approve-spec-takes-the-spec` passed; L5 `estimate-orchestration-names-the-typed-approval` passed; L6 `estimate-spec-box-runs-a-conserved-spec` passed; L16 `estimate-case-build-reads-the-readers-of-a-changed-step` passed; L17 `estimate-case-build-searches-the-names-of-what-it-changes` failed; L18 `estimate-case-build-reads-each-list-of-a-new-member` failed; L19 `estimate-guppi-config-runs-the-test-and-style-commands` passed; L20 `estimate-lint-runs-every-step` passed.
- Lessons: L7 (error), L21 (knowledge).

## Debt

- No box of the Spec is debt; no test reverted.
- 15 boxes wait for the librarian.
- `estimate-orchestration-acknowledging-reply` — after the librarian's render of the new text of `rule-orchestration`, an acknowledging reply written after it.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — after the librarian's render of `.claude/skills/work/SKILL.md`, the first `/work` that loads while `guppi check` exits 1, in the CLI.
- `estimate-retro-loads-on-a-red-command` — after the librarian's render of `.claude/skills/retro/SKILL.md`, the first load of `/retro`.
- The other pending Estimates stand as the last brief lists them.

## Observations

- Red before the work: `guppi check` exit 1 with three lines — `rule-orchestration` and `rule-skill-approve-spec`, `status: a page with core: true that is draft`; `estimate-orchestration-acknowledging-reply`, `unread: failed`.
- In this session, in the VS Code extension, `/work` and `/retro` loaded while `guppi check` exited 1: the skill text came with an instruction to run its `!` commands. The refusal of L7 was seen in the CLI only.
- The `case-guppi` of Case 1001 in session 0254 ran on the Render that sets the search of all the names of each page a Case changes, and ran it one slug at a time, with no Grep of the purpose lines and no search of a member already in a list (L17, L18).
- The trial clone `C:\PROJECTS\GUPPI-trial` stands on disk; nothing of it was pushed.
- `guppi ship --check` refuses a reference to a case of the form `Case N` in a docstring of a test; the form `(case N)` passes.

## For the next session

- `estimate-case-build-searches-the-names-of-what-it-changes` and `estimate-case-build-reads-each-list-of-a-new-member` are `failed` (L17, L18): whether `rule-case-build` needs a change, such as a check of the transcript or a guard on the summary, or only a new reading on a later build.
- C1, the clean branch, was put off: with `rule-skill-approve-spec` read (L4), the pages that block the build depend on this run's cascade and on the reading of `estimate-orchestration-acknowledging-reply` after the render.

## Ask the person
