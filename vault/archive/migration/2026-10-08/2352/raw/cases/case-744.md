## Case 744 — The After line of an option stands without a list dash

> **context:**
> The skill `grill-me` sets the shape of each question of a round. Under each option name stands a line `- **After:**`, which shows as a bullet item. The person asked to remove the dash, as a cosmetic change. The dash is read in two places: the template of `.claude/skills/grill-me/SKILL.md`, which `rule-skill-grill-me` renders, and the check of a round in `guppi/casecheck.py`, whose `AFTER_ITEM` is `- **After:**`. If only the template changed, the check would send back every round that follows it. Three sentences of the skill also call the line a nested item and set the indent of a quotation or a list under it by the text of that item. The person chose that the check accepts the line with or without the dash, that the line stays directly under the option name, indented two spaces, with only the dash removed, and that the skill sentences are reworded for a line with no dash (744.1). Since the check accepts both forms for good, no round is refused between the change of the code and the render of the skill, and no later Case removes an old form. The two promises can fail apart, so the skill text and the check are two sub-cases.
>
> The frame: a Grep of `\*\*After:\*\*` over `vault/wiki/`, `.claude/`, `guppi/` and `tests/` printed `vault/wiki/orchestration.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-asks-in-the-grill-me-shape.md`, `vault/wiki/estimates/estimate-case-check-sends-back-a-faulty-round.md`, `vault/wiki/rules/rule-skill-grill-me.md`, `vault/wiki/estimates/estimate-skill-grill-me-asks-in-rounds.md`, `.claude/skills/grill-me/SKILL.md`, `guppi/casecheck.py` and `tests/test_casecheck.py`. The sentence of `rule-orchestration`, rendered into `orchestration.md`, and the Criterion of `estimate-orchestration-asks-in-the-grill-me-shape` speak of each option with its `**After:**` item. They stand: they name the label, which every option keeps, and no dash. The Criterion of `estimate-skill-grill-me-asks-in-rounds` speaks of a nested item and of the indent under it, so 744.1 replaces it. Its `method` reads a round in a session after the render, so 744.1 sets it to a reading this session can take; `uv run guppi render --check` is left to `make lint` in the librarian's run. The old Criterion lines that the two sub-cases do not carry word for word are the lines on the After item, which the change rewords, and the first line of the check, which now lists its conditions without counting them. Some `then` lines of the two sub-cases share words because they describe the same template from two sides: the skill that writes a round, and the check that reads it. The Criterion of `estimate-case-check-sends-back-a-faulty-round` names `- **After:**`, so 744.2 replaces it and adds both forms to its `method`. The Purpose of `rule-skill-grill-me` and the text of `rule-case-check` do not name the dash, so they stand. `tests/test_case_schema.py` and `tests/test_orchestration.py` read live files of `vault/` and import `guppi/casecheck.py`, but the texts they read hold no round, so `round_form` returns nothing for them and they stand. Case 743 of this session does not touch the skill or the check.

> **problem:**
> The template of `grill-me` puts a list dash before the `**After:**` label of each option, and the person wants it gone. The check of a round requires the dash, and the skill text describes the line as a nested item, so removing the dash from the template alone would get every round sent back and leave the skill in contradiction with itself.

> **recommend:**
> - **What the round check accepts as the After line**
>   - Recommended: (a) accept the line with or without the dash; the tests of the check and its promise change to match.
>   - Answer: agreed, (a).
> - **Where the After line stands without the dash**
>   - Recommended: (a) directly under the option name, indented two spaces, only the dash removed.
>   - Answer: agreed, (a).
> - **The skill sentences that call the After line a nested item**
>   - Recommended: (a) reword them for an `**After:**` line; a quotation or a list under it is indented as far as the label, and the sample quotation line moves to match.
>   - Answer: agreed, (a).

### Case 744.1 — The skill template writes the After line with no dash

> **given:**
> `rule-skill-grill-me`: the rule whose Render is the text of the skill.
> **＋** `.claude/skills/grill-me/SKILL.md`: the skill file the render writes.
> **＋** `.claude/agents/case-guppi.md`: the agent that loads the skill by its `skills` field.
> **＋** `rule-orchestration`: the rule by which the main agent shows a round in the chat.
> **＋** `estimate-skill-grill-me-asks-in-rounds`: its Criterion is replaced whole.

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer, together with the lines of a list under it. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
> **＋** The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark `🔹` and its name in bold. Directly under its name stands one `**After:**` line, indented two spaces with no list dash before the label, that says what holds with that option.
> **＋** A list stands one item per line, never inside a sentence. This covers items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things. Under an `**After:**` line a list stands on the lines after it, indented as far as the label.
> **＋** A quotation, words taken from a page, a file or a reply, stands as a blockquote on its own line under the sentence that introduces it and names its source, a fragment of a few words too; it never stands inside a sentence in quote marks. Under an `**After:**` line it stands on the line after it, indented as far as the label.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** An option carries nothing under it but its `**After:**` line: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
> **－** A short series of words inside a sentence stays in the sentence.
> **－** No line of a question except an option starts with `🔹`.
> **－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `rule-orchestration`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
> **－** The `**Context:**` paragraph of a round of `case-guppi`, its lists and quotations included, and the place of its case numbers are not read here. They are the promises of the Estimates of the rule of `.claude/agents/case-guppi.md`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

> **tasks:**
> - [ ] update `rule-skill-grill-me`
>   - old:
>     ```
>     (a) <option name>**
>           - **After:** <what holds with this option>
>             > <a quotation inside the item, indented four spaces as far as the text of the item>
>     ```
>   - new:
>     ```
>     (a) <option name>**
>           **After:** <what holds with this option>
>           > <a quotation under the line, indented as far as the label>
>     ```
>   - old:
>     ```
>     (b) <option name>**
>           - **After:**
>     ```
>   - new:
>     ```
>     (b) <option name>**
>           **After:**
>     ```
>   - old: `` and under it stands one nested `**After:**` item: what holds with this option. ``
>   - new: `` and directly under its name stands one `**After:**` line, indented two spaces with no list dash before the label: what holds with this option. ``
>   - old: `` Under an `**After:**` item it stands nested one level deeper, inside that item. ``
>   - new: `` Under an `**After:**` line it stands on the lines after it, indented as far as the label. ``
>   - old: `` Under an `**After:**` item it stands inside that item, indented four spaces as far as the text of the item, so that it renders there and is no second item. ``
>   - new: `` Under an `**After:**` line it stands on the line after it, indented as far as the label, so that it renders under that line. ``
>   - change: `the After line of an option stands with no list dash, and a quotation or a list under it is indented as far as the label (case 744.1)`
> - [ ] update `estimate-skill-grill-me-asks-in-rounds`
>   - set:
>     ```
>     status: pending
>     method: by hand, the Render of rule-skill-grill-me as the Spec of the session holds it, read at Retro against the Criterion
>     ```
>   - change: `the Criterion replaced whole — the After line of an option stands with no list dash (case 744.1)`
> - [ ] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
> - [ ] read `estimate-skill-grill-me-asks-in-rounds`

> **ratification:**
> ```
> - decision[case 744.1][update][rule-skill-grill-me]{ref:rule-skill-grill-me}
> - decision[case 744.1][update][estimate-skill-grill-me-asks-in-rounds]{ref:rule-skill-grill-me}
> ```

### Case 744.2 — The round check accepts the After line with or without the dash

> **given:**
> `rule-case-check`: the rule of the check whose code judges the form of a round.
> **＋** `guppi/casecheck.py`: `round_form` and `option_with_after`, the check of the After line of an option.
> **＋** `tests/test_casecheck.py`: the tests of the form of a round.
> **＋** `.claude/skills/grill-me/SKILL.md`: the template the check judges a round against.
> **＋** `.claude/agents/case-guppi.md`: the agent whose rounds the check reads.
> **＋** `estimate-case-check-sends-back-a-faulty-round`: its Criterion is replaced whole.

> **when:**
> `SubagentStop` fires when `case-guppi` answers, and `uv run guppi casecheck --subagent` reads its newest output in `agent_transcript_path`: a text, or the `message` of a `SubagentHandback` call, whichever stands later.

> **then:**
> `uv run guppi casecheck --subagent` takes that output as a round when `is_round` of `guppi/casecheck.py`, the one test of a round that the `Stop` run also imports, finds it one. That holds when it holds no Case heading, no line that opens with `**Fact:**` stands before its first line that opens with `❓`, and one of its lines opens with the mark `❓`, with the indent of each line set aside.
> **＋** Each line that opens with `❓` opens a question, and the question runs to the next such line or to the end of the output. The text before the first question, the `**Context:**` paragraph, is not judged.
> **＋** A question is out of form when its first line does not match the title line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, judged by `QUESTION_LINE` of `guppi/casecheck.py`.
> **＋** A question is out of form when it holds no line that opens with `**Now:**`, or no line that holds `**Options:**` and nothing else.
> **＋** A question is out of form when it holds no line that opens with `➡️`, or when none of its lines that open with `🔹` has a line after it, before the next line that opens with `🔹` or `➡️`, that opens with `**After:**` or with `- **After:**`.
> **＋** A round with a question out of form exits 2. Its stderr names each such question by its first line and each part it misses, and tells `case-guppi` to answer with the round whole again, and `case-guppi` answers again.
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
>     method: "uv run pytest tests/test_casecheck.py -k round_form over a temp agent transcript: a round in form whose After lines have no dash, a round in form whose After lines have the dash, a title line without the colon, a question with no Now line, no lone Options label, no option with an After line and no arrow line, the same faulty round given twice, a Fact answer, an answer with a Case, an unreadable transcript; then by hand a round the hook sends back live, its stderr and the round case-guppi gave again"
>     ```
>   - change: `the Criterion replaced whole — the After line of an option is accepted with or without the list dash (case 744.2)`
> - [ ] `guppi/casecheck.py`: `option_with_after` takes a line that opens with `**After:**` or with `- **After:**`; the finding names an option `🔹` with an `**After:**` line; the module docstring and the docstrings of `round_form` and `option_with_after` say so.
> - [ ] `tests/test_casecheck.py`: `QUESTION_BODY` writes the After lines with no dash; a test named `round_form` that a round whose After lines have the dash passes; the case of the test of a question out of form with no After line removes the lines with no dash and looks for the new finding.
> - [ ] read `estimate-case-check-sends-back-a-faulty-round`

> **ratification:**
> ```
> - decision[case 744.2][update][estimate-case-check-sends-back-a-faulty-round]{ref:rule-case-check}
> ```
