# Handoff — 2026-10-07, Plan Mode flow and the Case check

## Notes from memory

- The person picked C3 (lesson L24 of session 1448). The agent closed C1 and C2 (`rule-sprint-close`, the close of migration) `[-] · sprint · defer`, because a session that closes a sprint holds no other Cases. The person was told and did not object.
- The person interrupted `/pre-spec` once, before `ask-guppi` ran, to add C4 and C5. That interruption is where Case 697 comes from. The `prespec` line of that first call stayed in the event log, so the hook of `rule-prespec-onward` later counted `/pre-spec` as run. The agent opened that reply with `STOP:` and asked the person instead.
- A1 (`estimate-permissions`) closed `· work` with no reading line. The person said the prompt for reading the transcript came after `case-guppi` started, so the old Criterion failed in fact. Case 698.2 replaces that Criterion, so a `failed` line on it would have landed on the new Criterion.
- At `/pre-spec` the person chose to keep both read rules beside `auto` (Q2) and to set `insight-orchestration-items-taken-together-unruled` `actioned` (Q1). The person left the duplicate lesson as it stands.
- Case 698 was first built again as a new Case 700 that superseded 698. The `Stop` check refused to show it: its clash findings clear only once the supersedes marks stand in the ledger, and they get there only at ratification. So 698 was built again under its own id. Its `rule-morph` update holds only a History line. Case 700 was never ratified and holds no ledger line.

## Direct instructions to the librarian

- Case 696 was ratified twice with the same decision lines, and the later text in the Spec is the one that holds. Cases 697, 698 and 699 were each ratified once and then again after `/pre-spec`. Write each page from the last text of its Case in the Spec.
- `lesson-orchestration-batch-rounds-headed-by-their-case` (L16) has the same root cause as `lesson-orchestration-batch-rounds-headed-by-own-text`, a child of `insight-orchestration-items-taken-together-unruled`. Case 699.5 sets that Insight `actioned`. The person chose to leave the duplicate for your judgment on a duplicate.
- `rule-morph` gets an update from Case 698.2 that holds only a History line: the read rules it names stay.
- `vault/raw/2026-10-07/0211/cases/case-700.md` is an empty file of a dropped Case. No ledger line names it.
- The render changes `.claude/settings.json` (the hook `uv run guppi casecheck --prompt` on `UserPromptSubmit`, by 699.1), `.claude/agents/case-guppi.md` (`permissionMode: auto`, by 698.1), `vault/wiki/orchestration.md` and `.claude/skills/pre-spec/SKILL.md`.

## What actually got done

- Ratified: Cases 696 (696.1, 696.2), 697 (697.1–697.4), 698 (698.1, 698.2) and 699 (699.1–699.7).
- Code: `guppi/onward.py`. `--plan` is silent before `/pre-spec`, and `TO_PRESPEC` is gone. A Case that a supersedes mark retires is not out (`session_decisions`, `case_out`). The answer with no `LEDGER` block to a reply the ledger hook sent back is sent on. Its own error exits 0 before `/pre-spec` (`after_prespec`).
- Code: `guppi/prespec.py` gains `retired_whole`.
- Code: `guppi/ledger.py` gains `stretch_of`, `refusals_in`, `refusal_records` and `sent_back_last`.
- Code: `guppi/casecheck.py`. The `Stop` run no longer refuses a layout fault. The new `--prompt` run (`before_message`, `last_reply`, `prompt_note`) prints the note. `last_refused` now takes records.
- Tests: `tests/test_onward.py`, `tests/test_casecheck.py`.
- `make test`: 1344 passed, 6 skipped. `make style`: clean.
- Readings: L34–L47. One of them is `failed`: `estimate-case-build-writes-the-case`, Retro, not read. Lessons: L16, L48, L49.

## Debt

- No box of code, test or command is left unticked.
- 53 boxes wait for the librarian: page lines, render lines and `read` lines.
- `estimate-hi-writes-frontier`: the `/hi` of the session after the close of a sprint.
- `estimate-hi-takes-a-conserved-spec`: a session that takes a conserved Spec, and the `/hi` after a sprint close.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: the `/work` of a session that closes a sprint.
- `estimate-brief-written`: the `/hi` after the librarian's run of the session that closes a sprint.
- `estimate-backlog-renders`: after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-runs-in-the-librarian-run`: after the librarian's run of the session that closes a sprint.
- `estimate-sprint-close-next-session-opens-the-sprint`: the librarian's run of the session after a sprint close.
- `estimate-sprint-close-takes-the-readings-in-groups`: after the Work Mode of the session that closes a sprint.
- `estimate-sprint-migration-leftovers-gone`, `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges`: the Work Mode of the session that closes migration.

## Observations

- `make lint` was red before the work, exit 2, with 13 finding lines (1 `deferred`, 12 `unread`), as `## Baseline` of `work.md` holds them. It was not run in Retro.
- The new code of `onward --plan` and `casecheck` runs from the working tree now. `casecheck --prompt` runs only once the render registers it, so until then a layout fault of a showing is neither refused nor told.
- The `Stop` check of `rule-case-check` refused one showing during this session: two rounds headed by the agent's own heading. That is lesson L16, closed by Case 699.5.
- The harness flagged two answers of subagents as instruction-shaped, because they mentioned `settings.json` and `bypassPermissions`. Both were rounds and reports on permission modes. Nothing in them was acted on as an instruction.

## For the next session

- Lesson L48: a dropped Case file with no decision line keeps the hook of `rule-prespec-onward` silent. Decide whether `case-guppi` removes the file of a Case it drops, or whether the hook leaves out a file that no ledger line and no reply names.
- `rule-sprint-close` and the close of migration still wait for a session of their own.
- `estimate-case-build-writes-the-case` stands `failed` (Retro, not read). Its live dispatches can be read in the first session after the render.

## Ask the person

- `estimate-permissions` — needs the person — in the first session after the librarian's render: did `case-guppi`, in `permissionMode: auto`, read a transcript under `~/.claude/projects/c--PROJECTS-GUPPI`, read a path outside the project that no rule names, and write its Case file, all with no permission prompt?
