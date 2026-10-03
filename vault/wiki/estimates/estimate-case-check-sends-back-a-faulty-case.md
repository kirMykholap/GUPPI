---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: A Case of case-guppi that the checks refuse goes back to it before the main agent sees it
method: uv run pytest tests/test_casecheck.py -k subagent, then by hand the first answer of case-guppi the hook sends back, the first file of cases/ it writes, and the first live round after a built Case, which is not sent back for that Case and leaves its stored entry and its file as they stood
checked: 2026-09-30
origin: raw/2026-09-25/1228/ledger.md#case-419.3
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

Then:
`uv run guppi casecheck --subagent` takes as the answer the newest output of the subagent in `agent_transcript_path` that holds a Case heading, that `is_round` of `guppi/casecheck.py` finds a round, or that is a `**Fact:**` answer, a text with no Case heading in which a line that opens with `**Fact:**` stands before any line that opens with `❓` — the `message` input of a `SubagentHandback` tool call or the text of an assistant message, whichever stands later — or `last_assistant_message` when `agent_transcript_path` is not readable or holds no such output.
**＋** It reads each Case of the answer in the chat form, by the functions of `guppi/ratified.py`, builds each Case's section of the Spec in memory, as the Spec hook writes it, and runs `judge` of `guppi/prespec.py` over them, the decision lines of the `ratification` fence standing for the ledger.
**＋** The categories whose schema rule the session changes, whose `create` and `defer` items `judge` does not judge by their keys, it takes from the decision lines of the `ratification` fences and of the session's window.
**＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
**＋** Each Case of the answer is stored, its text as the answer holds it, with its findings and the time of the store, in `<plan>.checked.json` beside the plan file of the session.
**＋** When no Case of the answer has findings, it writes the Cases of the answer, as the store holds their text, into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case: the file is replaced whole when the answer holds the top-level Case, and only the section of a sub-case is replaced when the answer holds that sub-case alone.
**＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` answers again, whatever `stop_hook_active` says.
**－** An answer with a finding writes no file, and a finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged answer is not sent back twice.
**－** An output that is none of the three, such as a short text after a `SubagentHandback` call, is passed over for an older output.
**－** An answer that is a round or a `**Fact:**` answer gets none of these checks of a Case, and a Case in an earlier output of the subagent is not checked, stored or written again.
**－** An answer of another agent, and one whose outputs hold no Case heading, get none of these checks of a Case and are not stored or written. A session with no plan file is not sent back for a fault of a Case.
**－** The form of the questions of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`, not of this one.

## Result

2026-09-30, uv run pytest tests/test_casecheck.py -k subagent: 43 passed, 21 deselected; live in session 2042: the store validated-munching-muffin.checked.json holds 16 Case entries, none with findings, notes on 9 sub-cases, which case-guppi reported as sent back once; the files cases/case-554.md to case-558.md were written from the stored text and replaced at each answer that held the top-level Case; no finding was sent back live, so that branch rests on the tests

## History

- 2026-09-25 created · [[decision-case-419.3]]
- 2026-09-26 updated: the Criterion replaced whole — the answer is the newest output of the subagent that holds a Case, else last_assistant_message; an unchanged answer is not sent back twice · [[decision-case-434]]
- 2026-09-26 updated: the Criterion replaced whole — the categories whose schema rule the session changes come from the ratification fences and the session's window (case 436.4) · [[decision-case-436.4]]
- 2026-09-27 updated: the Criterion replaced whole — the time of the store, and the file of a Case with no findings written from the stored text (case 452.1) · [[decision-case-452.1]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/2042/ledger.md#L29
- 2026-10-03 updated: the Criterion replaced whole — an answer whose outputs hold no Case heading gets none of the checks of a Case, and the form of a round is the promise of estimate-case-check-sends-back-a-faulty-round (case 601.2) · [[decision-case-601.2]]
- 2026-10-03 updated: the Criterion replaced whole — the answer is the newest output that is a Case, a round or a Fact answer; a round or a Fact answer gets no check of a Case, and an earlier Case is not checked, stored or written again (case 607.1) · [[decision-case-607.1]]
