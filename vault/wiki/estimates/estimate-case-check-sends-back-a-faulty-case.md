---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: A Case of case-guppi that the checks refuse goes back to it before the main agent sees it
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k subagent
checked: 2026-10-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
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

2026-10-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
