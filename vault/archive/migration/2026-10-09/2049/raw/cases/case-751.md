## Case 751 — Horizontal rules set off each reply of case-guppi and each Case of a batch

> **context:**
> The main agent shows the replies of `case-guppi` in the chat: a round of questions, a `**Fact:**` answer, and a built Case with its list and its `ratification`. Today `orchestration.md` allows one horizontal rule at most in a reply, after the Case or the last question of a round, and only when the agent's own text follows. In a batch, the rounds of several Cases stand in one list, and only the Context label and the question numbers mark where one Case ends and the next begins; case 699.5 forbids any other line of the agent's own there, and step 4 of the `/pre-spec` skill says the same for the loop after its findings (case 699.7). A Fact answer that the agent passes on gets no rule. The person asked for each reply of `case-guppi` to stand between two rules, and for a rule between the Cases of a batch, in the loop after `/pre-spec` too. The note that `uv run guppi casecheck --prompt` gives at the person's next message works against that layout: `round_opening` of `guppi/casecheck.py` takes the first line that is not blank, so a leading `---` gets the note, and `outside_the_list` notes any line before the first Case heading and stops reading at the first `---`, so in a batch only the first Case would be judged. Both only add a note and never refuse; the `Stop` comparison (`shown_text`, `mechanical_parts`, `fence_ledger_lines`) cuts each Case at its own `---` after `split_cases` splits by heading, so a leading rule or a rule between Cases changes nothing there. The code changes in Work Mode and accepts a showing and a round with or without the rules, so the agent may keep the old layout until the librarian renders the new `orchestration.md` and `SKILL.md`, and no old form needs to be kept apart. `tests/test_orchestration.py` is the one test that reads a live file and reaches the changed code: a Grep `orchestration\.md` over `tests/` printed only that file. It runs `outside_the_list` over the example of a showing in `vault/wiki/orchestration.md`; the new check accepts the example as it stands and as Case 751.6 changes it. A Grep `horizontal rule` over `guppi/`, `tests/`, `.claude/` and `vault/wiki/` printed `guppi/casecheck.py`, `.claude/skills/pre-spec/SKILL.md`, `vault/wiki/rules/rule-prespec.md`, `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `tests/test_casecheck.py`, `vault/wiki/estimates/estimate-case-check-refuses-text-outside-the-list.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md`, `vault/wiki/estimates/estimate-orchestration-showing-example-passes-the-check.md` and `vault/wiki/estimates/estimate-prespec-confirms-the-findings-once.md`. These stand: step 7 of the `/pre-spec` skill and `estimate-prespec-confirms-the-findings-once` put the agent's own text after the rule, which still holds; `case-guppi.md`, rendered from `rule-case-build`, has `case-guppi` end a round with no rule, and the main agent adds the rules; the line of `rule-case-protocol` and `log.md` are History; the two notes now allow a horizontal rule before a round or a Case, and the parts of their text that `tests/test_casecheck.py` asserts, `nothing before it` and `after the horizontal rule`, stay in them. A Grep `mark where|other line of|rule at most|one horizontal rule` over `vault/wiki/` printed `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-skill-grill-me.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-prespec.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md`, `vault/wiki/estimates/estimate-prespec-gathers-the-answers-after-findings.md`, `vault/wiki/estimates/estimate-orchestration-showing-example-passes-the-check.md` and `vault/wiki/estimates/estimate-orchestration-marks-each-round-of-a-batch.md`; the hit of `rule-skill-grill-me` is about the lines of a question, not a rule. `estimate-orchestration-shows-the-built-case` stands: its Criterion puts the agent's own text after one rule, which still holds, and its line that the main agent writes no context of its own before a round does not cover a rule. Other sentences of `rule-orchestration` also stand: the round sentence of `## Who builds a Case` adds nothing between the questions of one round, and a rule stands between rounds of two Cases. The sentence that a text of the agent's own before a round or a Case is not refused also stands, since the new rules are part of the form. A Grep `\*\*Fact:\*\*` over `.claude/` and `vault/wiki/` printed `vault/wiki/orchestration.md`, `.claude/agents/case-guppi.md`, `vault/wiki/estimates/estimate-case-check-sends-back-a-faulty-round.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/estimates/estimate-case-build-writes-the-case.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md`, `vault/wiki/estimates/estimate-case-check-sends-back-a-faulty-case.md`, `vault/wiki/estimates/estimate-case-check-sends-back-a-summary-without-the-case-name.md` and `vault/wiki/estimates/estimate-orchestration-forwards-a-discussion-question.md`. Only `rule-orchestration` sets how the agent shows a Fact; the four Estimates of `rule-case-check` and `rule-case-build` speak of what `case-guppi` gives back, not of the chat. `estimate-orchestration-forwards-a-discussion-question` stands: it has the agent show the Fact answer translated and then ask the open question again, which still holds; the rules around that answer are the promise of 751.1. `estimate-orchestration-signs-a-batch-together`, `estimate-orchestration-signs-items-taken-together` and `estimate-orchestration-batches-cases-out-at-once` stand too. They promise one list of every round, each question numbered `<Case id>.Q<n>`, and every Case of the batch in one reply, which still holds; none of them forbids a line between rounds, and the rules of that list are the promise of 751.2. Case 752 of this session changes `rule-case-build` and sets what `case-guppi` searches before a code task; it touches no page and no moment of this Case. A re-pitch by `wait-what` is the agent's own text and is not covered. The page `rule-case-check` names no first line of a round or a showing, so it does not change; its Estimates do. Each sub-case that replaces a Criterion carries its standing lines as they are and rewrites only the lines the rules change, so the check notes those rewritten lines as not carried. The sub-cases share words because 751.4 and 751.5 carry the standing lines of two Criteria of one check, and the other sub-cases speak of the same rules at different moments; no line of one sub-case states the promise of another.

> **problem:**
> In a batch the questions of one Case run into those of the next, and a reply of `case-guppi`, a Fact answer included, does not stand apart from the rest of the chat. The check of the layout would note the rules that would fix this.

> **recommend:**
> - **Where does the rule stand around a single reply of `case-guppi`?**
>   - Recommended: (a) a rule before and after each round, Fact answer and built Case.
>   - Answer: agreed, (a).
> - **What separates the Cases of a batch?**
>   - Recommended: (a) a rule between the rounds of two Cases and between the showings of two Cases.
>   - Answer: agreed, (a).
> - **Does the loop of fixes after `/pre-spec` take the same rules?**
>   - Recommended: (a) yes, `rule-prespec` changes too.
>   - Answer: agreed, (a).
> - **How does the layout check change?**
>   - Recommended: (a) the check accepts the rules and reads past a rule to the next Case heading.
>   - Answer: agreed, (a).
> - **Does the example of a showing gain the new rules?**
>   - Recommended: (a) yes, a rule above the heading too.
>   - Answer: agreed, (a).
> - **How is the Case split, and how is each part checked?**
>   - Recommended: (a) one part per promise.
>   - Answer: agreed, (a).

### Case 751.1 — A rule before and after each reply of case-guppi

> **given:**
> `rule-orchestration`: its Render sets how the main agent shows a reply of `case-guppi`.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-sets-off-each-reply-of-case-guppi`: the new check of the rules around a reply.

> **when:**
> The main agent shows in the chat a reply of `case-guppi` — a round of questions, a `**Fact:**` answer it passes on, or a built Case with its list and its `ratification` — with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> A horizontal rule stands on its own line before the reply of `case-guppi`.
> **＋** A second horizontal rule stands after the reply; the main agent's own text follows it, or, in a batch, the next reply of `case-guppi`, for which that rule is the rule before it.
> **＋** Each rule is the line `---` alone, with a blank line after it, and with a blank line before it unless it opens the reply, so that Markdown does not read the line above it as the underline of a heading.
> **－** A `**Waiting:**` line, the acknowledging reply and a Case in the short form are no reply of `case-guppi` and get no such rules.

> **tasks:**
> - [ ] create `estimate-orchestration-sets-off-each-reply-of-case-guppi`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether each reply of case-guppi that the main agent shows — a round, a Fact answer or a built Case — stands between two horizontal rules, with the agent's own text after the second`
>   - method: `by hand at the Retro of this session: the new Render of rule-orchestration in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow]`
> - [ ] update `rule-orchestration`
>   - old: `In the chat one horizontal rule at most, after the Case, its last sub-case or the last question of a round, and only when the agent's own text follows.`
>   - new: `` In the chat each reply of `case-guppi` that the agent shows — a round, a `**Fact:**` answer it passes on, or a built Case with its list and its `ratification` — stands between two horizontal rules, one before it and one after it, and the agent's own text follows the second, or, in a batch, the next reply of `case-guppi`, for which that rule is the rule before it; each rule is the line `---` alone, with a blank line after it, and with a blank line before it unless it opens the reply, so that Markdown does not read the line above it as the underline of a heading; a `**Waiting:**` line, the acknowledging reply and a Case in the short form get no such rules (case 751.1). ``
>   - change: `each reply of case-guppi that the agent shows stands between two horizontal rules (case 751.1)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-sets-off-each-reply-of-case-guppi`

> **ratification:**
> ```
> - decision[case 751.1][create][estimate-orchestration-sets-off-each-reply-of-case-guppi]{ref:rule-orchestration}{tags:session,workflow}
> - decision[case 751.1][update][rule-orchestration]{ref:rule-orchestration}
> ```

### Case 751.2 — A rule between the Cases of a batch

> **given:**
> `rule-orchestration`: its Render sets how the rounds and the Cases of a batch are shown.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-marks-each-round-of-a-batch`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose item the label of a first round names.
> **＋** `/pre-spec`: the skill before which a batch is shown this way.

> **when:**
> In Plan Mode before `/pre-spec`, the main agent shows in one list the rounds of `case-guppi` that came back for a batch of Cases, or shows every Case of a batch in one reply for one ratification, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The `**Context:**` paragraph of each first round on an item opens with a label that names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`.
> **＋** A later round, which has no Context paragraph, is marked by its question numbers `<Case id>.Q<n>`.
> **＋** One horizontal rule stands between the last question of one Case and the round of the next Case: the rule after one reply of `case-guppi` is the rule before the next.
> **＋** One horizontal rule stands between the showings of two Cases of the batch in the reply that shows them for one ratification: the rule after one showing is the rule before the next.
> **＋** No heading, and no line of the main agent's own other than a horizontal rule, stands before a round to mark where it begins: a rule stands before the first round of the list, and one rule between two rounds.
> **－** A round shown alone, outside a batch, keeps its `**Context:**` label as `case-guppi` gave it, translated.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `with no heading or other line of the agent's own to mark where a round begins (case 699.5)`
>   - new: `` with a horizontal rule before the first round of the list and one between the last question of one Case and the round of the next — the rule after one reply of `case-guppi` is the rule before the next — and no heading or other line of the agent's own but such a rule to mark where a round begins (cases 699.5, 751.2) ``
>   - old: `` each in the showing `## Who builds a Case` sets, for one ratification. ``
>   - new: `` each in the showing `## Who builds a Case` sets, with one horizontal rule between the showings of two Cases, which is the rule after the one and the rule before the next, for one ratification (case 751.2). ``
>   - change: `a horizontal rule stands between the rounds and between the showings of two Cases of a batch (case 751.2)`
> - [ ] update `estimate-orchestration-marks-each-round-of-a-batch`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the list of the rounds of a batch marks where each Case's round begins by a horizontal rule, by its Context label, which names the Case and its item, and by its question numbers, with no heading of the main agent's own, and whether the Cases of a batch shown for one ratification stand apart by a horizontal rule
>     ```
>   - change: `the Criterion replaced whole — a horizontal rule between the rounds and between the showings of two Cases of a batch`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-marks-each-round-of-a-batch`

> **ratification:**
> ```
> - decision[case 751.2][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 751.2][update][estimate-orchestration-marks-each-round-of-a-batch]{ref:rule-orchestration}
> ```

### Case 751.3 — A rule between the rounds of the loop after pre-spec

> **given:**
> `rule-prespec`: its Render sets the list of rounds in the loop after the findings.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the file rendered from `rule-prespec`.
> **＋** `estimate-prespec-gathers-the-answers-after-findings`: its Criterion is replaced whole.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of each question of the list.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose item the label of a first round names.
> **＋** `vault/wiki/orchestration.md`: the showing of the Cases built again.
> **＋** `guppi/casecheck.py`: the check behind `uv run guppi casecheck`, which lets a reply that opens with the labelled line through.

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
> **＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
> **＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
> **＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
> **＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** In that list the `**Context:**` label of each first round on an item names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`; a horizontal rule stands before the first round of the list and one between the last question of one Case and the round of the next, and no heading or other line of the main agent's own but such a rule marks where a round begins.
> **＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
> **－** A question that no answer settles stays in the next list under its number.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `and no heading or other line of your own marks where a round begins (case 699.7).`
>   - new: `` a horizontal rule stands before the first round of the list and one between the last question of one Case and the round of the next, as `vault/wiki/orchestration.md` sets it for a batch, and no heading or other line of your own but such a rule marks where a round begins (cases 699.7, 751.3). ``
>   - change: `a horizontal rule stands between the rounds of two Cases in the loop after the findings (case 751.3)`
> - [ ] update `estimate-prespec-gathers-the-answers-after-findings`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a horizontal rule between the rounds of two Cases in the list`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-gathers-the-answers-after-findings`

> **ratification:**
> ```
> - decision[case 751.3][update][rule-prespec]{ref:rule-prespec}
> - decision[case 751.3][update][estimate-prespec-gathers-the-answers-after-findings]{ref:rule-prespec}
> ```

### Case 751.4 — The check of a round accepts a leading rule

> **given:**
> `guppi/casecheck.py`: `round_opening` and the module docstring.
> **＋** `tests/test_casecheck.py`: the tests of the note on the opening of a round.
> **＋** `estimate-case-check-refuses-text-before-a-round`: its Criterion is replaced whole.
> **＋** `.claude/settings.json`: registers `uv run guppi casecheck --prompt` on `UserPromptSubmit`, rendered by `rule-hook-registry`.
> **＋** `guppi/ledger.py`: `refusals`, which reads the refusals of the check in the turn.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: how the refusals of the `Stop` run are counted.

> **when:**
> A reply of the main agent shows a round of `case-guppi`, `Stop` fires and `uv run guppi casecheck` of `guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

> **then:**
> At `Stop`, `uv run guppi casecheck` refuses no reply for the way it opens a round of `case-guppi`, or for a text of the main agent's own before the round. Its other reasons stand.
> **＋** On `UserPromptSubmit`, `uv run guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends. The turn holds a round when a text that `case-guppi` gave back in it is a round by `is_round` of `guppi/casecheck.py`.
> **＋** It finds a fault when the first line of the reply that is neither blank nor the horizontal rule `---` opens neither with `❓ ` nor with a bold label that ends in a colon. While the session's event log holds no `prespec` line of this session after its `hi`, it also finds a fault when the main agent wrote text in the turn after the first round came back and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run guppi casecheck` in the turn follows, judged by `refusals` of `guppi/ledger.py`.
> **＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the text before the round, says that the round stands as shown and is not shown again, and tells the agent to open the next round with its Context paragraph or its first question, with nothing before it but a horizontal rule.
> **＋** `.claude/settings.json` registers `uv run guppi casecheck --prompt` on `UserPromptSubmit`, as `rule-hook-registry` renders it.
> **－** A reply that opens with the horizontal rule `---` before its round gets no note for it, and neither does a reply with no rule before its round.
> **－** With no fault, in a turn with no round, and for text after the last question, it prints nothing.
> **－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
> **－** The person sees nothing of the note. It stores nothing and writes no file.
> **－** The refusals of the `Stop` run are counted as `estimate-case-check-judges-a-showing-after-a-refusal` sets it, and a layout fault of a round is not one of them.

> **tasks:**
> - [ ] `guppi/casecheck.py`: `round_opening` takes the first line of the reply that is neither blank nor `RULE`, and its note says nothing before the round but a horizontal rule; the module docstring on how a round opens says so.
> - [ ] `tests/test_casecheck.py`: a round that opens with `---` gets no note; a round with no rule gets no note; a text of the agent's own after a leading `---` still gets the note.
> - [ ] update `estimate-case-check-refuses-text-before-a-round`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a leading horizontal rule is no text before a round`
> - [ ] read `estimate-case-check-refuses-text-before-a-round`

> **ratification:**
> ```
> - decision[case 751.4][update][estimate-case-check-refuses-text-before-a-round]{ref:rule-case-check}
> ```

### Case 751.5 — The check of a showing accepts the rules and reads past them

> **given:**
> `guppi/casecheck.py`: `outside_the_list` and the module docstring.
> **＋** `tests/test_casecheck.py`: the tests of the note on the layout of a showing.
> **＋** `estimate-case-check-refuses-text-outside-the-list`: its Criterion is replaced whole.
> **＋** `estimate-case-check-shows-only-the-checked-case`: the refusals of the `Stop` run that stand.
> **＋** `.claude/settings.json`: registers `uv run guppi casecheck --prompt` on `UserPromptSubmit`.
> **＋** `guppi/ledger.py`: `refusals`, which reads the refusals of the check in the turn.

> **when:**
> A reply of the main agent shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form. `Stop` fires and `uv run guppi casecheck` of `guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

> **then:**
> At `Stop`, `uv run guppi casecheck` refuses no showing for a text of the main agent's own before its first Case heading, outside its list and its `ratification`, or written after the summary of `case-guppi` came back.
> **＋** It still refuses a shown Case that differs from the checked text, or whose file was not sent or differs from the store, as `estimate-case-check-shows-only-the-checked-case` sets it.
> **＋** On `UserPromptSubmit`, `uv run guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends, when that reply shows a Case.
> **＋** It finds a fault when a line that is neither blank nor the horizontal rule `---` stands before the first Case heading. It finds a fault when a line between a Case heading and the next Case heading or the horizontal rule `---` is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote.
> **＋** A horizontal rule `---` whose next line that is not blank is a Case heading ends one Case, and the judgment goes on under that heading, so each Case of a batch is judged.
> **＋** It finds a fault when the main agent wrote text in the turn after the first summary of `case-guppi` came back — a text given back whose first line that is not blank opens with `**Built:**` — and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run guppi casecheck` in the turn follows, judged by `refusals` of `guppi/ledger.py`.
> **＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the first such text, says that the Case stands as shown and is not shown again, and tells the agent to write nothing of its own before the Case but a horizontal rule and to keep its own text after the horizontal rule at the next showing.
> **－** A showing with no rule before its first Case heading, or with no rule between two Cases, gets no note for it.
> **－** A text written before the first summary came back, text after a horizontal rule that no Case heading follows, a reply with no Case heading that holds a section, a fence tagged `DIFF` and a deferred decision in the short form are not judged, and it prints nothing for them.
> **－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
> **－** The person sees nothing of the note. It stores nothing and writes no file.

> **tasks:**
> - [ ] `guppi/casecheck.py`: `outside_the_list` passes over a `RULE` line before the first Case heading, and at a `RULE` line under a heading goes on when the next line that is not blank is a Case heading and stops otherwise; the note of `showing_layout` says nothing of its own before the Case but a horizontal rule; the module docstring on the layout of a showing says so.
> - [ ] `tests/test_casecheck.py`: a showing with a leading rule and a rule between two Cases gets no note; a text outside the list of the second Case after a rule gets the note; text after a last rule that no Case heading follows gets no note; a showing with no rules gets no note.
> - [ ] update `estimate-case-check-refuses-text-outside-the-list`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a horizontal rule before the first Case and between two Cases is no text outside the list, and each Case of a batch is judged`
> - [ ] read `estimate-case-check-refuses-text-outside-the-list`

> **ratification:**
> ```
> - decision[case 751.5][update][estimate-case-check-refuses-text-outside-the-list]{ref:rule-case-check}
> ```

### Case 751.6 — The example of a showing stands between two rules

> **given:**
> `rule-orchestration`: its Render holds the example of a showing.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-showing-example-passes-the-check`: its Criterion is replaced whole.
> **＋** `tests/test_orchestration.py`: the test that runs the example through the check.
> **＋** `guppi/casecheck.py`: the functions the test runs over the example.
> **＋** `rule-case-check`: the check whose functions the test runs.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `showing` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it the functions of `guppi/casecheck.py` that the check of `rule-case-check` runs over a reply that shows a Case — the comparison of its `Stop` run and the judgment of the layout of its run on `UserPromptSubmit` — with a store whose sub-cases hold the ledger lines the example's `ratification` gives them.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## Showing and signing a Case`, one block tagged `showing`: a reply that shows a Case with two sub-cases between two horizontal rules — a rule, its heading, one list with an item per sub-case, one `ratification`, a rule and the agent's own text.
> **＋** The `ratification` of the example is a quote block: the line `> **ratification:**`, then the fence and the ledger lines of both sub-cases, each line opening with `> `.
> **＋** The example is in English; the paragraph before the block says that in the chat the heading, the names and the short texts stand in the language of the chat, that the file goes by `SendUserFile` in the same reply, and that the example passes the check of `rule-case-check` at the `Stop` of the reply and at the person's next message, which is the source of the limits, and that a refusal of the check, or its note at the person's next message, names the limit a showing broke; it lists no other limit.
> **＋** The check finds no text outside the list and the `ratification`, the leading rule included, reads the `ratification` as the showing of each sub-case it names, and finds no difference from the store, and the test passes.
> **＋** The example with the lines of its fence not quoted gives the finding of a text outside the list, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `showing`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `The block below is the text of a reply that shows a Case with two sub-cases, written after`
>   - new: `The block below is the text of a reply that shows a Case with two sub-cases between two horizontal rules, written after`
>   - old: `## Case 7 — Members get a reminder before a booking`
>   - new:
>     ```
>     ---
>
>     ## Case 7 — Members get a reminder before a booking
>     ```
>   - change: `the example of a showing stands between two horizontal rules (case 751.6)`
> - [ ] update `estimate-orchestration-showing-example-passes-the-check`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the example opens with a horizontal rule`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-showing-example-passes-the-check`

> **ratification:**
> ```
> - decision[case 751.6][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 751.6][update][estimate-orchestration-showing-example-passes-the-check]{ref:rule-orchestration}
> ```
