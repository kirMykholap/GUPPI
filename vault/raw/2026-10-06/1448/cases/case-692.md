## Case 692 — A refusal for own text before a round or a Case is cleared by one showing again

> **context:**
> The `Stop` run `uv run guppi casecheck` refuses a reply that shows a round of `case-guppi` when the main agent wrote text in the turn before its last tool call, by `texts_before_last_call` of `guppi/casecheck.py` (case 562). The turn starts at the person's message or a returned answer, by `opens_turn` of `guppi/ledger.py`, and a refusal of a `Stop` hook does not open a turn, so a text written before a tool call stays in the turn after every refusal. Showing the round again cannot remove it, yet the refusal tells the agent to do just that. In this session the main agent wrote a status note before it dispatched `case-guppi` for Case 691; the transcript holds the same refusal three times, quoting that note, and `LIMIT`, three, let the fourth showing through, so the person saw one round four times. The check of the layout of a showing (case 611) calls the same `texts_before_last_call`, and its refusal tells the agent to move that text after the horizontal rule, which a text written before a tool call cannot be. The person chose that the check judges only texts written after the round came back, and after a refusal only what follows it; that the check of a shown Case takes the same fix, applied to the summary of `case-guppi`; and that the limit of three stays. Case 692.1 replaces the Criterion of `estimate-case-check-refuses-text-before-a-round` and Case 692.2 that of `estimate-case-check-refuses-text-outside-the-list`, and sets the `purpose` of each anew, since each names text before the last tool call; their `method` lines name the tests and stand. Case 692.1 also changes the Purpose of `rule-case-check` and its `purpose` field for both sub-cases. The Criterion of `estimate-case-check-judges-a-showing-after-a-refusal` speaks of the count of refusals and of the reasons it counts; the count stays at three and a text before a round or outside a showing is still such a reason, so it stands. The check finds its last refusal by `refusals` of `guppi/ledger.py`, the one judgment of the refusals, which it already calls to count them, so no second test of a refusal record is written; `estimate-ledger-write-lifts`, `estimate-prespec-onward-sends-the-agent-on` and `estimate-retro-onward-sends-the-agent-to-the-handoff`, whose Criteria rest on that one judgment, stand. The bound of the turn does not change, only what is judged inside it, so `estimate-ledger-write-names-the-kind-of-a-user-record`, whose Criterion sets the turn the check reads for a round, stands. Case 692.2 knows a summary by one function, a first line that opens with `**Built:**`, which `summary_findings` of `guppi/casecheck.py` calls too in place of its own test, as `is_round` is shared for a round; the behaviour of that check does not change, so `estimate-case-check-sends-back-a-summary-without-the-case-name` stands. `LEDGER_LINE` of `guppi/casecheck.py` is a copy of `PREFIXES` of `guppi/ledger.py`; Case 692.1 drops it and imports `PREFIXES` (`rule-one-judgment-one-implementation`), and the tests of the check that read the `ratification` of a Case cover it with no promise changed. A Grep `estimate-case-check-refuses-text-before-a-round|estimate-case-check-refuses-text-outside-the-list|texts_before_last_call` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `vault/wiki/log.md`, not read, `guppi/casecheck.py`, which enters through its tasks, `vault/wiki/rules/rule-case-check.md`, whose hits are its `estimates` list and History, and `vault/wiki/estimates/estimate-case-check-refuses-text-outside-the-list.md`, which Case 692.2 changes. A Grep `(nothing before|text of (the main agent's|your) own|before the round|before a round)` over `vault/wiki/` and `.claude/` printed `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-case-check-judges-a-showing-after-a-refusal.md`, `vault/wiki/estimates/estimate-case-check-refuses-text-outside-the-list.md`, `vault/wiki/estimates/estimate-case-check-refuses-text-before-a-round.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/insights/insight-case-form-chat-form-read-by-no-script.md`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-case-check.md`, `vault/wiki/lessons/lesson-orchestration-own-text-before-a-round.md`, `vault/wiki/lessons/lesson-sendmessage-answers-open-a-turn-of-their-own.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md` and `vault/wiki/estimates/estimate-spec-capture-offers-the-fork.md`. The sentence of `rule-orchestration`, its render `orchestration.md` and `estimate-orchestration-shows-the-built-case` that a refused round is shown again with nothing before it stands, and with this Case that showing passes; the hits in `rule-case-protocol`, the insight and `log.md` are History; the two lessons tell what happened in past sessions; the hit in `estimate-spec-capture-offers-the-fork` is about another moment. Case 691 of this session sets what the ledger hook does at the same `Stop`; this Case sets only what `uv run guppi casecheck` judges and leaves the ledger hook as it stands, and it takes on the `LEDGER_LINE` of `guppi/casecheck.py` that Case 691 left to it.

> **problem:**
> The check refuses a round or a Case for a text written before a tool call, which no showing again can remove, so the person sees one round or Case up to four times.

> **recommend:**
> - **Which texts before the round does the check refuse?**
>   - Recommended: (b) only texts written after the round came back, and after a refusal only what follows it.
>   - Answer: agreed, (b).
> - **Does the check of a shown Case get the same fix?**
>   - Recommended: (a) the same fix, in this Case, as a sub-case of its own.
>   - Answer: agreed, (a).
> - **How many refusals before a showing is let through?**
>   - Recommended: (a) keep three.
>   - Answer: agreed, (a).

### Case 692.1 — A round is judged by the texts after it came back and after the last refusal

> **given:**
> `guppi/casecheck.py`: the `Stop` run that judges how a round is shown.
> **＋** `guppi/ledger.py`: `refusals`, the one judgment of the refusals, and `PREFIXES`, the openings of a ledger line.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `rule-case-check`: the rule of the check, whose Purpose names the change.
> **＋** `estimate-case-check-refuses-text-before-a-round`: its Criterion is replaced whole.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the count of refusals, which stands.
> **＋** `rule-prespec`: the rule of `/pre-spec`, whose `prespec` line ends the judgment of text before a tool call.
> **＋** `/hi` and `.claude/skills/wait-what/SKILL.md`: where the main agent puts its own questions and re-pitches, with no round.

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the last `user` record that the function of `guppi/ledger.py` names the person's message or a returned answer, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that `is_round` of `guppi/casecheck.py`, the one test of a round, finds one; it comes back in the `tool_result` of an `Agent` call, or in the returned answer that opens the turn.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn after the first round of the turn came back and before its last tool call.
> **＋** When the turn holds a refusal of `uv run guppi casecheck`, judged by `refusals` of `guppi/ledger.py`, it judges only the texts after the last such refusal, so a round shown again with nothing before it passes.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** A text the main agent wrote in the turn before the first round came back is not judged.
> **－** Text after the last question and one horizontal rule is not judged.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, and a reply of the loop after the findings of `/pre-spec` is judged only by its first line; in that loop each answer of a `case-guppi` comes back in a turn of its own, and the text the main agent writes there is set by `rule-prespec`.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** With `stop_hook_active` set a round shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] update `estimate-case-check-refuses-text-before-a-round`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the Stop run of the Case check refuses a reply that shows a round of case-guppi after a text of the main agent's own written after the round came back, judges only what follows its last refusal in the turn, judges only the first line of the reply after pre-spec, and leaves a turn with no round alone
>     ```
>   - change: `the Criterion replaced whole — only texts written after the round came back and after the last refusal of the check are judged, so one showing again clears a refusal`
> - [ ] update `rule-case-check`
>   - old: `` a round of `case-guppi` from being shown after a text of the main agent's own (case 562), and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` (case 611) ``
>   - new: `` a round of `case-guppi` from being shown after a text of the main agent's own written after the round came back (case 562), and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` or written after the summary of `case-guppi` came back (case 611), each judged only by what follows the last refusal of the check in the turn, so that one showing again clears a refusal (case 692) ``
>   - set:
>     ```
>     purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi from being shown after a text of the main agent's own written after the round came back, a Case from being shown with a text of the main agent's own outside the list under its heading and its ratification or written after the summary of case-guppi came back, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built
>     ```
>   - change: `the check judges a text before a round or a Case only after the round or the summary came back and after its last refusal in the turn`
> - [ ] `guppi/casecheck.py`: one function gives the texts the main agent wrote in the turn before its last tool call, after the first text given back that a predicate finds and after the reply that the last refusal of `uv run guppi casecheck` follows, by `refusals` of `guppi/ledger.py`; `round_opening` calls it with `is_round`, in place of `texts_before_last_call`; the module docstring and the docstring of `round_opening` say so.
> - [ ] `guppi/casecheck.py`: `LEDGER_LINE` goes, and its two readers import `PREFIXES` of `guppi/ledger.py`.
> - [ ] `tests/test_casecheck.py`: a text before the `Agent` call that brought the round back passes; a text after the round came back and before a later tool call is refused; a round shown again with nothing before it after a refusal of the check passes; a reply that opens with a line of its own after a refusal is refused; a round given back in the returned answer that opens the turn leaves every text of the turn judged.
> - [ ] read `estimate-case-check-refuses-text-before-a-round`

> **ratification:**
> ```
> - decision[case 692.1][update][estimate-case-check-refuses-text-before-a-round]{ref:rule-case-check}{addresses:lesson-case-check-round-refused-for-an-own-text-no-showing-clears}
> - decision[case 692.1][update][rule-case-check]{ref:rule-case-check}
> ```

### Case 692.2 — A shown Case is judged by the texts after its summary came back and after the last refusal

> **given:**
> `guppi/casecheck.py`: the `Stop` run that judges the layout of a showing.
> **＋** `guppi/ledger.py`: `refusals`, the one judgment of the refusals.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `estimate-case-check-refuses-text-outside-the-list`: its Criterion is replaced whole.
> **＋** `estimate-case-check-sends-back-a-summary-without-the-case-name`: the check of a summary, whose test of a summary is shared and which stands.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the count of refusals, which stands.
> **＋** `.claude/settings.json`: registers the `Stop` run of the check.

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form, and `uv run guppi casecheck` runs on it, as `.claude/settings.json` registers it.

> **then:**
> `uv run guppi casecheck` exits 2 when a line that is not blank stands in the reply before its first Case heading.
> **＋** It exits 2 when a line stands between a Case heading and the next Case heading or the horizontal rule `---` that is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote, its `> **ratification:**` line and the `>` lines after it.
> **＋** It exits 2 when the main agent wrote text in the turn of the reply after the first summary of `case-guppi` came back and before its last tool call; a summary is a text given back to an `Agent` or `SendMessage` call whose first line that is not blank opens with `**Built:**`, in the `tool_result` of an `Agent` call or in the returned answer that opens the turn.
> **＋** When the turn holds a refusal of `uv run guppi casecheck`, judged by `refusals` of `guppi/ledger.py`, it judges only the texts after the last such refusal, so a Case shown again with no text of its own before its last tool call passes.
> **＋** Its reason on stderr quotes the first such text and tells the agent to show the Case again with nothing of its own before it and its own text after the horizontal rule.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases with the stored answer and the check of how a round opens, and a reply that more than one of them refuse gives each reason.
> **－** A text the main agent wrote in the turn before the first summary came back is not judged, and a turn with no summary judges no text before its last tool call.
> **－** Text after the horizontal rule is not judged.
> **－** A reply with no Case heading that holds a section, the acknowledging reply among them, a fence tagged `DIFF`, and a deferred decision in the short form are not judged.
> **－** With `stop_hook_active` set a Case shown again after a refusal is judged again, and the reason is given as `estimate-case-check-judges-a-showing-after-a-refusal` sets it.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] update `estimate-case-check-refuses-text-outside-the-list`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the Stop run of the Case check refuses a reply that shows a Case with a text of the main agent's own before its first Case heading, under a heading outside the list and the ratification, or written after the summary of case-guppi came back and before the last tool call of the turn, judging only what follows its last refusal in the turn
>     ```
>   - change: `the Criterion replaced whole — only texts written after the summary came back and after the last refusal of the check are judged, so one showing again clears a refusal`
> - [ ] `guppi/casecheck.py`: one function tells a summary of `case-guppi`, a text whose first line that is not blank opens with `**Built:**`, and `summary_findings` calls it in place of its own test; `showing_layout` calls the function of Case 692.1 with it, in place of `texts_before_last_call`, which goes; its reason tells the agent to show the Case again with nothing of its own before it and its own text after the horizontal rule; the module docstring and the docstring of `showing_layout` say so.
> - [ ] `tests/test_casecheck.py`: a text before the call that brought the summary back passes; a text after the summary came back and before the sending is refused; a Case shown again with nothing of its own before the last tool call after a refusal of the check passes; a turn with no summary judges no text before its last tool call.
> - [ ] read `estimate-case-check-refuses-text-outside-the-list`

> **ratification:**
> ```
> - decision[case 692.2][update][estimate-case-check-refuses-text-outside-the-list]{ref:rule-case-check}
> ```
