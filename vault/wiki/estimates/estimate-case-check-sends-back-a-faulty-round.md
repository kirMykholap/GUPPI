---
type: estimate
kind: QA
status: pending
target: "[[rule-case-check]]"
purpose: Whether the SubagentStop check sends back to case-guppi a round whose question has a title line out of the grill-me form or misses a fixed label, once per text, and leaves a round in form, a Case and a Fact answer alone
method: "uv run pytest tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form, a title line without the colon, a question with no Now line, no lone Options label, no option with an After item and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand the first round the hook sends back live, its stderr and the round case-guppi gave again"
origin: raw/2026-10-02/2300/ledger.md#case-601.1
sprint: migration
created: 2026-10-02
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads its newest output in `agent_transcript_path`: a text, or the `message` of a `SubagentHandback` call, whichever stands later.

Then:
`uv run guppi casecheck --subagent` takes that output as a round when `is_round` of `guppi/casecheck.py`, the one test of a round that the `Stop` run also imports, finds it one. That means three things hold: it holds no Case heading; no line that opens with `**Fact:**` stands before its first line that opens with `❓`; and one of its lines opens with the mark `❓`, with the indent of each line set aside.
**＋** Each line that opens with `❓` opens a question, and the question runs to the next such line or to the end of the output. The text before the first question, the `**Context:**` paragraph, is not judged.
**＋** A question is out of form when its first line does not match the title line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, judged by `QUESTION_LINE` of `guppi/casecheck.py`.
**＋** A question is out of form when it holds no line that opens with `**Now:**`, or no line that holds `**Options:**` and nothing else.
**＋** A question is out of form when it holds no line that opens with `➡️`, or when none of its lines that open with `🔹` has a line that opens with `- **After:**` after it, before the next line that opens with `🔹` or `➡️`.
**＋** A round with a question out of form exits 2. Its stderr names each such question by its first line and each part it misses, and tells `case-guppi` to answer with the round whole again, and `case-guppi` answers again.
**－** A round gets none of the checks of a Case in the same run, and no earlier Case of the transcript is checked for it, so the exit 2 of a round carries the findings of its form alone.
**－** A round out of form is not sent back again when an earlier output of `case-guppi` in `agent_transcript_path` holds the same text, trailing spaces aside.
**－** A round in form gives no finding and prints nothing of its own.
**－** These are not judged here: an output with a Case heading, a `**Fact:**` answer, an output with no line that opens with `❓`, an answer of another agent, and an `agent_transcript_path` that cannot be read.
**－** The check of the form stores nothing and writes no file, whether or not the session has a plan file.
**－** A round as the main agent shows it in the chat is not judged here.

## History

- 2026-10-03 created · [[decision-case-601.1]]
- 2026-10-03 updated: the Criterion replaced whole — a round is known by is_round as the code holds it, and gets no check of a Case in the same run, so its exit 2 carries the findings of its form alone (case 607.2) · [[decision-case-607.2]]
