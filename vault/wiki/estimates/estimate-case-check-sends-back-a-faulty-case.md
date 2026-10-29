---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A Case of case-guppi that the checks refuse goes back to it before the main agent sees it
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k subagent
checked: 2026-10-29
origin: raw/2026-09-25/1228/ledger.md#case-419.3
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

Then:
`uv run --project .guppi guppi casecheck --subagent` takes each file `case-<N>.md` under the `cases/` folder of a session folder, judged by `is_case_file` and `case_number` of `.guppi/guppi/casecheck.py`, that a `Write` or `Edit` call of the subagent in `agent_transcript_path` names, and reads its Cases as the file stands now.
**＋** A file whose Cases `<plan>.checked.json` already holds with the same text, line ends and trailing spaces aside, and with no findings is not checked or stored again, so the time of its store stands.
**＋** Any other such file is checked whole: each Case is read in the chat form by the functions of `.guppi/guppi/ratified.py`, its section of the Spec is built in memory as the Spec hook writes it, and `judge` of `.guppi/guppi/prespec.py` runs over them, the decision lines of the `ratification` fences standing for the ledger and, with the session's window, giving the categories whose schema rule the session changes.
**＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
**＋** Each Case of the file is stored, its text as the file holds it, with its findings and the time of the store, in `<plan>.checked.json`; the hook writes no file of a Case.
**＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` fixes the file and stops again, whatever `stop_hook_active` says.
**－** A finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged file is not sent back twice.
**－** A transcript that names no file `case-<N>.md` gets no check of a Case, whatever its newest output holds: a Case given only in the text of an answer is not checked, stored or written into a file.
**－** An output of the subagent with no Case heading — a summary, a round or a `**Fact:**` answer — is not read as a Case; the form of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`.
**－** A subagent of another type, and a transcript the hook cannot read, get none of these checks, and nothing is stored. A session with no plan file is not sent back for a fault of a Case.
**－** A file of another name under `cases/`, such as the working note `note-<N>.md` of `case-guppi`, is no such file: it is not read as a Case, stored or sent back, and a transcript whose calls name no file `case-<N>.md`, though they name the note, is read as one that names no such file.

## Result

2026-10-29, Retro of session 1930, uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k subagent: 120 passed, 114 deselected; the old path is gone from subagent of casecheck.py (answer_of and write_case_files removed); test_subagent_a_case_given_only_by_handback_is_not_stored, test_subagent_a_case_in_the_answer_text_alone_is_not_stored and test_subagent_file_an_answer_text_with_no_case_file_is_not_stored assert that a Case given only in an answer text is not checked, stored or written; test_subagent_the_hook_leaves_the_file_as_case_guppi_wrote_it asserts the hook writes no file of a Case; the full run 1790 passed, 6 skipped, 1 deselected

## History

- 2026-09-25 created · [[decision-case-419.3]]
- 2026-09-26 updated: the Criterion replaced whole — the answer is the newest output of the subagent that holds a Case, else last_assistant_message; an unchanged answer is not sent back twice · [[decision-case-434]]
- 2026-09-26 updated: the Criterion replaced whole — the categories whose schema rule the session changes come from the ratification fences and the session's window (case 436.4) · [[decision-case-436.4]]
- 2026-09-27 updated: the Criterion replaced whole — the time of the store, and the file of a Case with no findings written from the stored text (case 452.1) · [[decision-case-452.1]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/2042/ledger.md#L29
- 2026-10-03 updated: the Criterion replaced whole — an answer whose outputs hold no Case heading gets none of the checks of a Case, and the form of a round is the promise of estimate-case-check-sends-back-a-faulty-round (case 601.2) · [[decision-case-601.2]]
- 2026-10-03 updated: the Criterion replaced whole — the answer is the newest output that is a Case, a round or a Fact answer; a round or a Fact answer gets no check of a Case, and an earlier Case is not checked, stored or written again (case 607.1) · [[decision-case-607.1]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0112/ledger.md#L13
- 2026-10-05 updated: the Criterion replaced whole — the check reads the file case-guppi wrote, whole, and keeps the old path until the writer is live; the method follows (case 645.2) · [[decision-case-645.2]]
- 2026-10-05 deferred · [[decision-case-659]]
- 2026-10-05 updated: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669) · [[decision-case-669.6]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-29 updated: the Criterion replaced whole — only a file case-<N>.md under cases/ is a file of a Case, so the working note of case-guppi is no Case; the method is the tests alone · [[decision-case-896.4]]
- 2026-10-29 status: pending → passed · raw/2026-10-28/2312/ledger.md#L26
- 2026-10-29 updated: the Criterion replaced whole — the check reads only the files case-<N>.md that case-guppi wrote; the old path of the answer text is gone · [[decision-case-904.1]]
- 2026-10-29 status: pending → passed · raw/2026-10-29/1930/ledger.md#L22
