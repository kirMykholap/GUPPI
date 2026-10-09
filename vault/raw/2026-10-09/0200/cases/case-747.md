## Case 747 — The round check is read by a staged run of the hook

> **context:**
> When `case-guppi` stops, the `SubagentStop` hook `uv run guppi casecheck --subagent` reads its newest output. If that output is a round with a question out of the grill-me form, the hook exits 2 and tells the agent to give the round whole again. `estimate-case-check-sends-back-a-faulty-round` holds that promise. Case 744.2 replaced its Criterion so that the After line of an option passes with or without its list dash, and the Retro of session 2352 set it `failed` without a reading. The pytest part of its method passed, 13 tests. The by-hand part asked for a round the hook sends back live, with its stderr and the round the agent gave again, and none occurred after the change. A live send-back happens only when the agent happens to write a faulty round, so every later change of this promise can fail the same way. The last live send-back was read on 2026-10-04 (ledger line 37 of session 2041). The person chose a staged run in place of the live part: at the Retro of this session the hook command runs by hand from the repository on a copy of a real `case-guppi` transcript of this session that ends with a faulty round. The run cannot show the agent answering again. The person chose to drop that clause from the Criterion, which now ends at what the hook does. That the subagent answers again after an exit 2 is a fact of Claude Code, recorded in `lesson-hooks-subagentstop-exit-2-sends-the-subagent-back`, and not a judgment of this check. The Criterion is replaced whole. The one old line not carried word for word is the line on the exit 2 of a round, which keeps its words up to the clause that `case-guppi` answers again and drops that clause; the other lines are carried word for word. The `purpose` of the Estimate speaks of what the check sends back and leaves alone, and not of the agent answering again, so it stands.
>
> The staged copy is cut after a round and before any `Write` of a case file. With no written case file and no Case heading in the output, `subagent` of `guppi/casecheck.py` returns from `send_back` before it reads the plan file. So the staged runs store nothing in the plan of the session. No code changes. `rule-case-check` does not state that the agent answers again, so its text stands. The Grep `round whole again|answers again` over the repository root, with the glob `{vault/wiki/**/*.md,.claude/**/*.md,guppi/*.py}`, printed `vault/wiki/log.md`, `vault/wiki/insights/insight-hi-skill-substitution-checked-by-a-model-call.md`, `vault/wiki/lessons/lesson-hooks-subagentstop-exit-2-sends-the-subagent-back.md`, `vault/wiki/rules/rule-case-build.md`, `guppi/casecheck.py`, `vault/wiki/estimates/estimate-case-check-sends-back-a-faulty-round.md` and `vault/wiki/estimates/estimate-case-check-sends-back-a-clash-with-another-case.md`. The hits in `log.md` and in the History of `rule-case-build` were not read. The insight speaks of a server that answers again, not of the agent. The docstring of `guppi/casecheck.py` says that the hook tells the agent to answer again, which stays true. The Criterion of `estimate-case-check-sends-back-a-clash-with-another-case` promises that `case-guppi` answers again after a clash finding. That is another promise, read by its own method, which this Case does not touch, so it stands. Case 746 of this session sets other readings at the same Retro and touches no page of this Case.

> **problem:**
> `estimate-case-check-sends-back-a-faulty-round` stands `failed` because its method waits for a faulty round that only chance produces. One line of its Criterion promises an act of the agent that no run of this check can show.

> **recommend:**
> - **How should the failed reading of the round check be closed?**
>   - Recommended: (b) read it again at the end of this session, with a staged run of the hook command on a copy of a real agent transcript ending in a faulty round, in place of the live part.
>   - Answer: agreed, (b).
> - **Does the promise keep the line that the agent answers again?**
>   - Recommended: (a) drop that line from the promise; it ends at what the hook does, and the other lines stay word for word.
>   - Answer: (a).

> **given:**
> `estimate-case-check-sends-back-a-faulty-round`: the check of the form of a round; its Criterion is replaced whole and its `method` changes.
> **＋** `rule-case-check`: the rule of the check whose code judges the form of a round.
> **＋** `guppi/casecheck.py`: `is_round`, `QUESTION_LINE`, `round_form` and `faulty_round`, the code the check runs.
> **＋** `tests/test_casecheck.py`: the tests of the form of a round.
> **＋** `.claude/settings.json`: the `SubagentStop` registration of `uv run guppi casecheck --subagent`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the template the check judges a round against.
> **＋** `.claude/agents/case-guppi.md`: the agent whose rounds the check reads.

> **when:**
> `SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads its newest output in `agent_transcript_path`: a text, or the `message` of a `SubagentHandback` call, whichever stands later.

> **then:**
> `uv run guppi casecheck --subagent` takes that output as a round when `is_round` of `guppi/casecheck.py`, the one test of a round that the `Stop` run also imports, finds it one. That holds when it holds no Case heading, no line that opens with `**Fact:**` stands before its first line that opens with `❓`, and one of its lines opens with the mark `❓`, with the indent of each line set aside.
> **＋** Each line that opens with `❓` opens a question, and the question runs to the next such line or to the end of the output. The text before the first question, the `**Context:**` paragraph, is not judged.
> **＋** A question is out of form when its first line does not match the title line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, judged by `QUESTION_LINE` of `guppi/casecheck.py`.
> **＋** A question is out of form when it holds no line that opens with `**Now:**`, or no line that holds `**Options:**` and nothing else.
> **＋** A question is out of form when it holds no line that opens with `➡️`, or when none of its lines that open with `🔹` has a line after it, before the next line that opens with `🔹` or `➡️`, that opens with `**After:**` or with `- **After:**`.
> **＋** A round with a question out of form exits 2. Its stderr names each such question by its first line and each part it misses, and tells `case-guppi` to answer with the round whole again.
> **－** A round gets none of the checks of a Case in the same run, and no earlier Case of the transcript is checked for it, so the exit 2 of a round carries the findings of its form alone.
> **－** A round out of form is not sent back again when an earlier output of `case-guppi` in `agent_transcript_path` holds the same text, trailing spaces aside.
> **－** A round in form gives no finding and prints nothing of its own.
> **－** These are not judged here: an output with a Case heading, a `**Fact:**` answer, an output with no line that opens with `❓`, an answer of another agent, and an `agent_transcript_path` that cannot be read.
> **－** The check of the form stores nothing and writes no file, whether or not the session has a plan file.
> **－** A round as the main agent shows it in the chat is not judged here.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-faulty-round`
>   - set:
>     ```
>     status: pending
>     method: "uv run pytest tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form whose After lines have no dash, a round in form whose After lines have the dash, a title line without the colon, a question with no Now line, no lone Options label, no option with an After line and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand at the Retro of the session of case 747, uv run guppi casecheck --subagent run from the repository with a payload on stdin of agent_type case-guppi and an agent_transcript_path to a copy, in the scratchpad, of a transcript of a case-guppi of that session cut after a round and before any Write of a case file: the copy as cut exits 0 and prints nothing; the copy with the colon removed from a title line of its last round exits 2, its stderr naming that question, the title line it misses, and telling case-guppi to answer with the round whole again; the same faulty round added again as a later output exits 0; the plan file of the session is unchanged by the runs"
>     ```
>   - change: `the Criterion replaced whole — the clause that case-guppi answers again leaves it, and the live send-back of the method gives way to a staged run of the hook command at the Retro (case 747)`
> - [ ] read `estimate-case-check-sends-back-a-faulty-round`

> **ratification:**
> ```
> - decision[case 747][update][estimate-case-check-sends-back-a-faulty-round]{ref:rule-case-check}
> ```
