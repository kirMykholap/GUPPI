# Handoff — 2026-11-27, the plan file holds the map; a Frontier line closes in one edit

## Notes from memory

- On Case 1087 the person first asked why the Cases should not go straight into `spec.md`. They took the Cases file beside the plan file only after the round showed that several readers take a standing `spec.md` for an approved Spec.
- The person closed C2 (the two options of the Code Mode answer not built) with no Case. Code Mode will not be used, and neither option is wanted.
- C1, the clean branch, was put off again (`· sprint · defer`). It still waits for the owner to push `plugin` and a tag `prod-x.y.z`.
- Plan Mode of this session ran the old code. So this session's own plan file holds its Cases itself, in the old form. Since Work Mode, its map opens with the new line that names `iridescent-coalescing-dragon-of-e973ab46-87d7-4725-89b2-668fc204031c.cases.md`, a file that does not stand for this session.

## Direct instructions to the librarian

- Case 1087 was ratified twice: at first, and again after the findings of `/pre-spec`. The ledger holds the lines of 1087.1–1087.13 once, from the first ratification, and the line of 1087.14 from the second. Take the Case text from `vault/raw/2026-11-27/2214/spec.md` and `cases/case-1087.md`, which hold the rebuilt Case.
- `rule-orchestration` gets pairs from Case 1087.3 and from Case 1088. Apply them in ledger order. Their anchors lie in different paragraphs, as the context of 1088 says.
- The line of 1087.1 on `rule-spec-write` carries `{supersedes:case 1081}`. It clears the `deferred_by` of `rule-spec-write`, and the page leaves `backlog.md`.
- Case 1088 sets `insight-orchestration-frontier-closer-leaves-the-box-open` to `actioned`, with `addressed_by: decision-case-1088`.
- The render lines are `vault/wiki/case-schema.md`, `vault/wiki/orchestration.md` and `.claude/skills/pre-spec/SKILL.md`. There is a glossary line for the term Spec of `entity-glossary`.

## What actually got done

- Cases ratified: 1087 with 1087.1–1087.14, and 1088.
- Code:
  - `.guppi/guppi/ledger.py` gains `plan_cases_file`, `with_cases` and `plan_cases_text`.
  - `ratified.py`:
    - Cases, defers and parents are written into the Cases file, and a superseded Case is removed from `spec.md`, the plan file and the Cases file.
    - The map of the plan file is cut from `plan_cases_text` and opens with `plan_map_head`, the line that names the Cases file. `case_map` and `with_map` take that line as a parameter.
    - `without_maps` is new.
    - The check after the write reads `plan_cases_text`, and the guard's reason now names the map.
  - `spec.py` appends `with_cases` / `plan_cases_text` through `capture`, then rebuilds the maps of `spec.md`. It judges a Spec already in the file with its maps out.
  - `prespec.py` (`gate_refusal`, `--check`), `casecheck.py` (the other Cases of the session) and `gate.py` (`spec_check`) read `plan_cases_text`.
  - `recall.py` names the Cases file after the plan file.
  - The docstrings follow.
- Tests:
  - `test_ratified.py`: the Stop-hook tests read the Cases file, and `plan_holds_no_case` is asserted.
  - New tests in `test_ratified.py`: an older plan file that holds the superseded Case, a plan file with Cases of its own in the map, and the line of the map of `spec.md` after an approval.
  - `test_spec.py`: an approval with and without a Cases file, a typed `/approve-spec`, and that `spec.py` joins no text itself.
  - `test_ledger.py -k cases_file`: `plan_cases_text`, and each reader on a Case that stands only in the Cases file.
  - `test_recall.py`: the Cases file is named after the plan file.
- The code and test boxes of `spec.md` (25 lines) were ticked by a script in the scratchpad, which then rebuilt the maps of `spec.md` and of the plan file, as `--boxes` does.
- `uv run --project .guppi guppi test`: 2074 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean.
- Readings written:
  - At `/hi`: ledger lines 1–5.
  - At Retro: eleven readings in the reply that ends Retro, all `passed`, of `estimate-spec-write-writes-the-map`, `-rebuilds-the-maps-of-the-spec`, `-copies-the-ratified-case`, `-reaches-the-approved-spec`, `-checks-the-written-case`, `-answers-a-refusal`, `-reads-a-new-tag`, `-writes-a-defer`, `-copies-a-built-defer-only-case`, `-removes-a-superseded-case` and `estimate-orchestration-takes-back-a-ratified-case`.
- Lessons written: none.

## Debt

- No box of code, a test or a command is left unticked.
- The other unticked boxes of `spec.md` wait for the librarian: the page lines, the render lines, the glossary line and the `read` lines of the Retro readings.
- `estimate-spec-capture-appends` — waits for the approval of a plan in a later session. Its pytest part passed (`test_spec.py`, 29 passed).
- `estimate-spec-write-readers-take-the-cases-file` — waits for the librarian's run that renders `.claude/skills/pre-spec/SKILL.md`. Its pytest part passed (`test_ledger.py -k cases_file`, 8 passed).
- `estimate-compact-recall-reloads` — waits for the first compaction in Plan Mode of a later session with a Cases file beside its plan file. Its pytest part passed (`test_recall.py`, 8 passed).

## Observations

- `is_plan_file` judges the Cases file a plan file, since it is a `.md` under `.claude/plans/`. So the guard refuses an `Edit` of it, as the context of 1087 says. But a `tool Write:` line of the Cases file in the event log would make `plan_path` name it as the plan. No step of the harness writes it by a tool call, so this did not occur.
- The Cases file is created only by the `Stop` hook. Nothing removes an empty one: after a supersede that empties it, it stands with a blank line, and `with_cases` leaves it out.
- `frontierguard` refused the first edit of the C2 line at `/hi` (end of the line only). That is the defect Case 1088 addresses.

## For the next session

- The first Plan Mode on the new code is the live check of Case 1087. The plan view should show the map alone, the Cases should stand in `<plan stem>.cases.md`, and the approval should write both into `spec.md`. Watch that the VS Code plan view still renders the map and its boxes. `estimate-spec-write-shows-the-boxes-in-the-plan-file` stays open for that.

## Ask the person
