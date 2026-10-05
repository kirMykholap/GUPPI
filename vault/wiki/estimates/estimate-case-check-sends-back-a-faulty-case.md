---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: A Case of case-guppi that the checks refuse goes back to it before the main agent sees it
method: uv run pytest tests/test_casecheck.py -k subagent, then by hand in a session after the render a file of case-guppi the hook sends back, fixed by Edit and passed, and a live round after a built Case, which leaves the stored entry of that Case as it stood
checked: 2026-10-04
origin: raw/2026-09-25/1228/ledger.md#case-419.3
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` stops; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

Then:
`uv run guppi casecheck --subagent` takes each file under the `cases/` folder of a session folder, judged by `is_case_file` of `guppi/casecheck.py`, that a `Write` or `Edit` call of the subagent in `agent_transcript_path` names, and reads its Cases as the file stands now.
**＋** A file whose Cases `<plan>.checked.json` already holds with the same text, line ends and trailing spaces aside, and with no findings is not checked or stored again, so the time of its store stands.
**＋** Any other such file is checked whole: each Case is read in the chat form by the functions of `guppi/ratified.py`, its section of the Spec is built in memory as the Spec hook writes it, and `judge` of `guppi/prespec.py` runs over them, the decision lines of the `ratification` fences standing for the ledger and, with the session's window, giving the categories whose schema rule the session changes.
**＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
**＋** Each Case of the file is stored, its text as the file holds it, with its findings and the time of the store, in `<plan>.checked.json`; the hook does not write that file.
**＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` fixes the file and stops again, whatever `stop_hook_active` says.
**＋** Until a reading of `estimate-case-build-writes-the-case` passes live, a transcript that names no such file and whose newest output holds a Case heading is read the old way: that output is checked and stored as the Cases of a file are, and with no finding the hook writes it into `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the whole file when it holds the top-level Case, the section of each sub-case otherwise. A Case of a later session removes this path.
**－** A finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged file is not sent back twice.
**－** An output of the subagent with no Case heading — a summary, a round or a `**Fact:**` answer — is not read as a Case; the form of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`.
**－** A subagent of another type, and a transcript the hook cannot read, get none of these checks, and nothing is stored. A session with no plan file is not sent back for a fault of a Case.

## Result

2026-10-04, the Work readings of session 0112: `uv run pytest -q tests/test_casecheck.py -k subagent` 72 passed, 45 deselected; live in session 0112 (transcript b76bfabb): the SubagentStop hook sent back the answer of Case 625 (agent a309e5b8dc383eed8) with "casecheck: case 625: /box is not named in its given; case 625: /pre-spec is not named in its given", and case-guppi answered again; the store glimmering-waddling-wigderson.checked.json holds 624, 625, 626, 626.1 and 626.2, each with its agent_id, the time of the store and no findings; cases/case-625.md was written at 02:24:10.05 after its store at 02:24:09.93, and cases/case-626.md, holding 626, 626.1 and 626.2, at 02:30:50.09 after its store at 02:30:49.96; a live round after a built Case: agent ad744674f53077ad2 built Case 626 at 02:09:40 and, sent the findings of /pre-spec, answered with the round Q6 at 02:23:52, which no hook feedback followed; the store and the file now hold the answer of 02:30:49, so their state between the round and that answer was not recorded and rests on the tests; not exercised: a `**Fact:**` answer

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
