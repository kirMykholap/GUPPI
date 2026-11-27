# Handoff — 2026-11-27, the first sketch, stop lines, the map of the plan, a trial of Code Mode

## Notes from memory

- The person first wanted the whole Cases to move out of the plan file into `spec.md` (1078.Q1, Q5 a). The person took the smaller step (Q9 c), the map at the head of the plan file, once the frame showed that 66 Estimate pages say that the plan file holds the Cases. The move is deferred as Case 1081, on `rule-spec-write`. Its context carries the change named by 1078.1: the map stays in the plan file after the move.
- The person picked ❓, the red question mark, as the sign of an `A` line, knowing that ❓ also opens each question of a round (1078.Q8). No blue question mark exists.
- The person put the exported board at `plugin/assets/GUPPI.png`, not at the path first ratified. After `/pre-spec`, Case 1076 was built again on that name and adds an `update` of `rule-clean-branch`, whose Purpose now names a third picture. The picture is about 6 MB at 4638×3710. It was committed as it stands, and nobody decided whether a smaller copy should replace it.
- The Excalidraw board itself could not be read by WebFetch: the page holds only the word "Excalidraw+". The main agent judged the exported picture by eye: many names on it are outdated, such as `/hi-guppi`, `/subagent-guppi`, `/pre-task` and `index.md`, which the note of the section covers.
- The person did not read the long plan before the exit of Plan Mode. That was the reason for Case 1078.

## Direct instructions to the librarian

- Case 1076 was ratified twice. Its second ratification adds `decision[case 1076][update][rule-clean-branch]` (ledger line 26). Its `update` of `entity-guppi-repository` sets `code_ref` with `plugin/assets/GUPPI.png`, not `guppi-first-sketch.png`, which the first build named.
- Cases 1077 and 1078 both change `rule-orchestration`: three pairs of 1077.2 and two pairs of 1078.3, with anchors that do not overlap. Apply 1077.2 first, then 1078.3, and check that each `old` hits once.
- 1078.4 changes `rule-skill-hi` by two pairs and replaces the Criterion of `estimate-hi-writes-frontier` whole. 1077.3 replaces the Criterion of `estimate-carry-over-writes`, and 1077.5 replaces the Criterion of `estimate-brief-written`. Each also sets `status: pending`.
- Cases 1080 and 1081 are short-form defers, on `rule-work-mode` and `rule-spec-write`. 1081 defers a page that 1078.1 changes in the same session, as the person chose. `guppi prespec --check` printed this as a note.
- The two Estimates of 1079 are one-off Research Estimates on `entity-sprint-plugin` with `once: true`. Both were read `passed` at Retro.

## What actually got done

- Cases ratified: 1076, 1077 (1077.1–1077.5), 1078 (1078.1–1078.4), 1079 (1079.1–1079.2); short-form defers 1080 and 1081. After the findings of `/pre-spec`, Cases 1076 to 1079 were built again and ratified again. All 15 findings of `ask-guppi` were confirmed closed.
- Code: `.guppi/guppi/ratified.py`.
  - The `Stop` hook rebuilds a map under the title line of the plan file after each run that writes, places or removes a Case. The map holds a table, a Mermaid diagram, entries with ✅ ⛔ 🔍 and the deferred Cases.
  - `guppi ratified --map <file> --session <stamp>` prints the map.
  - The map uses `prespec.STOP_LINE`, `generate.READ_LINE` and the module's `TASK_LINE` and `ITEM_LINE`, imported, not copied.
- Tests: nine tests `-k map` in `.guppi/tests/test_ratified.py`, `test_approved_spec_places_a_case_after_the_map` among them.
- Text: `README.md` gains the section "The first sketch" after "Main parts", with `plugin/assets/GUPPI.png`, the link to the board and the note.
- Outside the repository: the clone `C:/PROJECTS/guppi-codemode-trial` of the branch `plugin` and its `uv sync`. It stays there; deleting it is a deletion outside the repository.
- `uv run --project .guppi guppi test`: 2043 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean.
- Ledger: readings at `/hi` on lines 1 and 2. Retro readings of eight Estimates of this session, all `passed`: `estimate-case-build-names-a-stop-for-the-person`, `estimate-orchestration-keeps-a-stop-line-on-the-frontier`, `estimate-prespec-names-an-open-stop-line`, `estimate-brief-written`, `estimate-spec-write-writes-the-map`, `estimate-orchestration-marks-the-frontier-by-signs`, `estimate-sprint-plugin-code-mode-cost-measured` and `estimate-sprint-plugin-code-mode-hooks-answer-its-calls`. One lesson: `lesson-frontier-line-closed-in-two-edits`.

## Debt

- No box of code, a test or a command is left unticked; no patch.
- 41 boxes wait for the librarian: the page, render and `read` lines.
- `estimate-carry-over-writes` waits for its event: a `/carry` of a session whose `frontier.md` holds an open line of the source `stop`.
- `estimate-spec-write-shows-the-map-in-the-plan-view` waits for its event: the exit of Plan Mode in the VS Code extension of the next session whose plan file holds a ratified Case. Its reading is the person's answer then.
- `estimate-hi-writes-frontier` waits for its event: the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint. Its reading is the person's answer then.
- `estimate-orchestration-leaves-the-number-to-case-guppi` (W2) waits for its event: a ratified Case that comes back in another shape, under a new number. None did in this session: Cases 1076 to 1079 came back under their own numbers.

## Observations

- In the preview of the map (1078.2), the person found the map fine, with one gap. Each task line shows a sign, not a checkbox, and the ticks of Work Mode in `spec.md` do not reach the map. The plan file is never ticked, so the map shows every task open. The person wants real checkboxes that follow the ticks. The ratified form forbids a map line that opens with a box, since the tickers and `place` would take it for a task.
- The Code Mode trial ran on Claude Code 2.1.332 in a terminal. The two measured sessions ran at the same time, about 35 seconds apart, not one after the other.
- `guppi agents` counts each call made inside Code Mode code as a call: 2589 calls for 15 `REPL` calls. Its call count does not compare Code Mode with a session without it.
- In the hook session, every tool hook of the clone answered the calls made from code: `guard`, `bashguard`, `grepguard`, `pageread`, and the `PostToolUse` event lines.
- At `/hi`, the brief named the event of `estimate-orchestration-leaves-the-number-to-case-guppi` as standing in session 2333. The transcript shows Cases 1072 to 1074 sent back after `/pre-spec` and back under their own numbers in the same shape, so the event did not occur.
- The brief named the event of `estimate-case-build-names-a-stale-line-of-another-case` in session 2333, and it did stand there. The branches of its Criterion where another Case or the Case itself needs a fix did not arise in that event.

## For the next session

- The map of the plan file with real checkboxes that follow the ticks of `spec.md`, as the person asked after the preview. It changes the contract of 1078.1: no line of the map opens with a box. A Case on `rule-spec-write` has to settle how the map holds a box that the tickers of `generate.py`, `keep_boxes` and `place` of `ratified.py` and `split_cases` do not take for a task, and how the ticks of Work Mode reach the plan file or the map.
- Code Mode, by the two readings of 1079:
  - On the read-only task, Code Mode used about half the tokens and about 60% more seconds, and it gave the same answer.
  - The hooks answered the calls made from code.
  - Code Mode does not run in the VS Code panel, and `case-guppi`, `ask-guppi` and the librarian need `REPL` on their `tools` lists to use it.
  - Whether to change the harness for Code Mode is a decision of a later Case.
- The picture `plugin/assets/GUPPI.png` is about 6 MB. Whether `README.md` should show a smaller copy is not decided.

## Ask the person

- `estimate-guppi-repository-readme-shows-the-first-sketch` — needs the person — does the section "The first sketch" of `README.md`, after "Main parts", show the sketch as intended: the picture `plugin/assets/GUPPI.png`, the link to the Excalidraw board under it and the note that it is a rough first picture of GUPPI?
