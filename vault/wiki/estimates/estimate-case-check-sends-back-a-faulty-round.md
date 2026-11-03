---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the SubagentStop check sends back to case-guppi a round whose question has a title line out of the grill-me form or misses a fixed label, once per text, and leaves a round in form, a Case and a Fact answer alone
method: "uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form whose After lines have no dash, a round in form whose After lines have the dash, a title line without the colon, a question with no Now line, no lone Options label, no option with an After line and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand at the Retro of a session in which a case-guppi answered with a round, uv run --project .guppi guppi casecheck --subagent run from the repository with a payload on stdin of agent_type case-guppi and an agent_transcript_path to a copy, in the scratchpad, of a transcript of a case-guppi of that session cut after a round and before any Write of a case file: the copy as cut exits 0 and prints nothing; the copy with the colon removed from a title line of its last round exits 2, its stderr naming that question, the title line it misses, and telling case-guppi to answer with the round whole again; the same faulty round added again as a later output exits 0; the plan file of the session is unchanged by the runs"
checked: 2026-10-09
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` answers, and `uv run --project .guppi guppi casecheck --subagent` reads its newest output in `agent_transcript_path`: a text, or the `message` of a `SubagentHandback` call, whichever stands later.

Then:
`uv run --project .guppi guppi casecheck --subagent` takes that output as a round when `is_round` of `.guppi/guppi/casecheck.py`, the one test of a round that the `Stop` run also imports, finds it one. That holds when it holds no Case heading, no line that opens with `**Fact:**` stands before its first line that opens with `❓`, and one of its lines opens with the mark `❓`, with the indent of each line set aside.
**＋** Each line that opens with `❓` opens a question, and the question runs to the next such line or to the end of the output. The text before the first question, the `**Context:**` paragraph, is not judged.
**＋** A question is out of form when its first line does not match the title line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, judged by `QUESTION_LINE` of `.guppi/guppi/casecheck.py`.
**＋** A question is out of form when it holds no line that opens with `**Now:**`, or no line that holds `**Options:**` and nothing else.
**＋** A question is out of form when it holds no line that opens with `➡️`, or when none of its lines that open with `🔹` has a line after it, before the next line that opens with `🔹` or `➡️`, that opens with `**After:**` or with `- **After:**`.
**＋** A round with a question out of form exits 2. Its stderr names each such question by its first line and each part it misses, and tells `case-guppi` to answer with the round whole again.
**－** A round gets none of the checks of a Case in the same run, and no earlier Case of the transcript is checked for it, so the exit 2 of a round carries the findings of its form alone.
**－** A round out of form is not sent back again when an earlier output of `case-guppi` in `agent_transcript_path` holds the same text, trailing spaces aside.
**－** A round in form gives no finding and prints nothing of its own.
**－** These are not judged here: an output with a Case heading, a `**Fact:**` answer, an output with no line that opens with `❓`, an answer of another agent, and an `agent_transcript_path` that cannot be read.
**－** The check of the form stores nothing and writes no file, whether or not the session has a plan file.
**－** A round as the main agent shows it in the chat is not judged here.

## Result

2026-10-09, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
