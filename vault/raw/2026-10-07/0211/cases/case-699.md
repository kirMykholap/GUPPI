## Case 699 — A layout fault of a shown round or Case is told at the next message, not shown again

> **context:**
> The `Stop` run `uv run guppi casecheck` of `rule-case-check` judges each reply of the main agent when the reply ends. By then the person has already read the reply. When the reply shows a round of `case-guppi` and its first line opens neither with `❓ ` nor with a bold label that ends in a colon, or when the agent wrote a text of its own after the round came back, the run exits 2 (`round_opening` of `guppi/casecheck.py`). `orchestration.md` then requires a reply that shows the whole round again (case 561.9). A Case shown with a text of the agent's own before its heading or outside its list is refused the same way (`showing_layout`, case 611), and it is shown again (case 452.4). In this session the agent showed the rounds of Cases 697 and 698 in one list under a heading of its own, `### Case 697 — C4`. The run refused the reply, and the person read seven questions twice, though the questions were right. The lesson `lesson-orchestration-batch-rounds-headed-by-their-case` finds the cause: `rule-orchestration` numbers the questions of a batch `<Case id>.Q<n>`, but sets no mark where the round of each Case begins. The person chose four things. A layout fault of a round is let through at `Stop`. The agent is told of it when the person sends the next message, so the round is not shown twice (Case 699.1). A layout fault of a shown Case is handled the same way. A Case whose file was not sent, or whose lines differ from the checked text, is still refused (Case 699.2). In a batch, the Context label of each first round names its Case, so no heading of the agent's own is needed (Case 699.5). The person sees no extra line. The route to the agent is the one `guppi context --prompt` already uses: its code says that stdout of `UserPromptSubmit` reaches the context. The new run `uv run guppi casecheck --prompt` uses the judgments that the `Stop` run uses today, so no second copy exists. It exits 0 always, since a block on `UserPromptSubmit` would block the person's message. `.claude/settings.json` registers `uv run guppi event prompt`, `uv run guppi context --prompt` and `uv run guppi gate` on that event. Their rules, `rule-event-log`, `rule-context-size` and `rule-retro-commit`, write the `hi` and gate marks, print the size note and refuse a typed command. None of them reads a reply, so the new run sits beside them. Case 699.3 replaces the Criterion of `estimate-case-check-judges-a-showing-after-a-refusal`, whose `When` lists the layout faults among the reasons of the `Stop` run; its `purpose` and `method` state no promise that changes. Case 699.4 replaces the Criterion of `estimate-orchestration-shows-the-built-case`, which has a refused round shown again. Case 699.6 replaces the Criterion of `estimate-orchestration-showing-example-passes-the-check`, which says that the example passes the functions of the `Stop` run; its `purpose` is set anew, and the test stays as it is. `estimate-case-check-shows-only-the-checked-case` stands: it sets the comparison with the store and the sending, which the `Stop` run still refuses. `estimate-case-check-exits-2-on-an-error` stands: it sets an error of the `Stop` run. `estimate-hook-registry-rendered` stands: it promises only that the file equals the Render. `estimate-orchestration-signs-a-batch-together` and `estimate-orchestration-signs-items-taken-together` stand: they set the one list numbered `<Case id>.Q<n>`, which stays true, and the new Estimate of Case 699.5 checks the mark. The two Estimates of `rule-case-check` that Cases 699.1 and 699.2 change keep their slugs; their Criterion and `purpose` say the new behaviour. The `purpose` of `rule-case-check` is set once, in Case 699.2, for both runs. A Glob `vault/**/*marks-each-round*` printed nothing, so the new slug is free. The code runs from the working tree once Work Mode changes it. The registration in `.claude/settings.json` and the text of `orchestration.md` land at the librarian's render. In between, the `Stop` run refuses no layout fault and no note comes. The old text of `orchestration.md` has a refused round shown again, but no refusal comes. Nothing is refused and nothing is lost, so no old form is kept. Case 696 of this session sets what `uv run guppi onward --plan` does at the same `Stop`. It judges the refusals of the other `Stop` hooks in the transcript, and a refusal of another hook neither silences it nor sends it on again. Fewer refusals of `uv run guppi casecheck` change nothing there, so this Case does not cover that hook. Case 697 changes other sentences of `rule-orchestration`. Its `old` anchors and the anchors of this Case do not overlap, and its new text says nothing of a showing again or of a batch. A Grep ``shows? the round again|round shown again|refuses is followed|text before a round|text-before-a-round|text-outside-the-list`` over the repository with the glob `!vault/{raw,archive}/**` printed `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/log.md`, `vault/wiki/estimates/estimate-case-check-refuses-text-before-a-round.md`, `vault/wiki/rules/rule-case-check.md`, `vault/wiki/lessons/lesson-case-check-round-refused-for-an-own-text-no-showing-clears.md`, `tests/test_casecheck.py`, `guppi/casecheck.py`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-shows-the-built-case.md`, `vault/wiki/rules/rule-case-protocol.md` and `vault/wiki/insights/insight-case-form-chat-form-read-by-no-script.md`. The hits of the code, the tests, the two Estimates and the two rules enter the Case. `orchestration.md` is the Render of `rule-orchestration`. The hits of `rule-case-protocol`, of the Insight and of `rule-case-check` outside its `estimates` list are History lines. The lesson records a past event. A Grep ``own text before|text of (its|the main agent's|the agent's) own (before|outside)|before a round|before the round`` over `vault/wiki/` with the glob `!{log,brief}.md` printed `estimates/estimate-case-check-refuses-text-outside-the-list.md`, `estimates/estimate-case-check-refuses-text-before-a-round.md`, `rules/rule-case-check.md`, `estimates/estimate-case-check-judges-a-showing-after-a-refusal.md`, `estimates/estimate-orchestration-shows-the-built-case.md`, `insights/insight-case-form-chat-form-read-by-no-script.md` and `lessons/lesson-sendmessage-answers-open-a-turn-of-their-own.md`. All of them but the last two enter the Case. In `estimate-orchestration-shows-the-built-case` the hit says that the agent writes no context of its own before the first question of a round, which stays true. The hit of the Insight is a History line, and the lesson records a past measurement. The same Grep over `.claude/` printed nothing. A Grep ``round_opening|showing_layout|outside_the_list|texts_after`` over `*.py` printed `tests/test_schemas.py`, `tests/test_orchestration.py`, `tests/test_lint.py` and `guppi/casecheck.py`. The hits of `tests/test_schemas.py` and `tests/test_lint.py` are names of tests of their own. `tests/test_orchestration.py` runs `outside_the_list` over the showing example, which Case 699.6 keeps. `/pre-spec` found four faults, and the person agreed to each fix. In a batch the main agent writes the label of its own, so Case 699.4 has the showing of a round in `rule-orchestration` and in the Criterion of `estimate-orchestration-shows-the-built-case` let that label stand. Case 699.6 also replaces the sentence that a refusal of the check names the limit a showing broke, since a layout fault now gets a note instead. The list of the rounds after the findings of `/pre-spec`, which `rule-prespec` sets and `estimate-prespec-gathers-the-answers-after-findings` checks, shows rounds of several Cases too. So Case 699.7 sets the same label there. It is a sub-case of its own, since it replaces the Criterion of another Estimate. The `method` of that Estimate waits for the `/pre-spec` of a later session, so it is set to the reading of the Spec at the Retro of this session. Its `purpose` states no promise that changes. The vault already held `lesson-orchestration-batch-rounds-headed-by-own-text`, of session 0104, with the same root cause, a child of `insight-orchestration-items-taken-together-unruled`. By the person's answer, Case 699.5 sets that Insight `actioned`, so it leaves the backlog and its lessons go to the archive. The lesson is of another session, so no line of this Case carries a mark for it. The check of this file noted the lines of the old Criteria that the new ones do not carry, and each change is on purpose. In 699.1 and 699.2 a layout fault no longer exits 2 at `Stop`, and the judgment moves to the run at the next message. In 699.3 the layout faults leave the list of reasons. In 699.4 the refusal that is followed by a showing again names its faults, and the lines on the showing of a round and on the agent's own context let the batch label stand. In 699.7 the list of the rounds gains the label. In 699.6 the example passes both runs. The check also noted lines that 699.1 and 699.2 share, and lines that other sub-cases share with a sibling. The run at the next message acts the same way for a round and for a Case, so its exit and its silence are said in each sub-case. Each other shared line states the frame of its own sub-case, which the Criterion of its Estimate needs in order to read without the Case.

> **problem:**
> A layout fault of a shown round or Case makes the `Stop` check send the reply back after the person has read it, and the agent shows the whole round or Case a second time. In a batch, the agent marks where each Case's round begins with a heading of its own, because the rules set no mark, and the check reads that heading as such a fault.

> **recommend:**
> - **What the check does when only the layout of a round is wrong**
>   - Recommended: (b) let it through, and tell the agent at the next message: the check lets the reply through, and a hook at the person's next message tells the agent what was wrong.
>   - Answer: agreed, (b).
> - **How a joint showing marks where each Case's round begins**
>   - Recommended: (a) the Context label names the Case, such as `**Context — Case 697 (C4):**`, translated; a later round is marked by its question numbers alone.
>   - Answer: agreed, (a).
> - **Whether a layout fault in a shown Case is handled the same way**
>   - Recommended: (a) layout faults of a Case get the note too; a file not sent or ledger lines that differ from the checked ones are still sent back.
>   - Answer: agreed, (a).
> - **Whether the person sees anything when a layout fault is let through**
>   - Recommended: (a) the agent alone is told, at the person's next message.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by a finding of `/pre-spec` the person agreed to, let the batch label stand in the showing of a round in `rule-orchestration` and in the Criterion of `estimate-orchestration-shows-the-built-case`.
>   - Taken: Case 699.4 adds a pair on the Render and two lines of its Criterion.
> - **Change**
>   - Asked: by a finding of `/pre-spec` the person agreed to, replace the sentence that a refusal of the check names the limit a showing broke.
>   - Taken: Case 699.6 adds a pair that names the note at the next message too, and a line of its Criterion.
> - **Change**
>   - Asked: by a finding of `/pre-spec` the person agreed to, the label holds in the list of the rounds after the findings too, through `rule-prespec` and `estimate-prespec-gathers-the-answers-after-findings`.
>   - Taken: the new Case 699.7 does it, since it replaces the Criterion of another Estimate.
> - **Change**
>   - Asked: by the person's answer (a) to the question of `/pre-spec`, name the old lesson `lesson-orchestration-batch-rounds-headed-by-own-text` and its Insight, and set `insight-orchestration-items-taken-together-unruled` `actioned`.
>   - Taken: `context` names both, and Case 699.5 sets the Insight `actioned`.

### Case 699.1 — A layout fault of a shown round is told at the next message

> **given:**
> `rule-case-check`: the rule of the check, whose Purpose says what it prevents.
> **＋** `estimate-case-check-refuses-text-before-a-round`: its Criterion is replaced whole.
> **＋** `estimate-case-check-judges-a-showing-after-a-refusal`: the count of the refusals of the `Stop` run.
> **＋** `guppi/casecheck.py`: the check, whose `round_opening` judges how a round opens.
> **＋** `guppi/ledger.py`: its `refusals` reads the refusals of the check in the transcript.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `rule-hook-registry`: renders the hooks of `.claude/settings.json`.
> **＋** `.claude/settings.json`: registers the hooks.

> **when:**
> A reply of the main agent shows a round of `case-guppi`, `Stop` fires and `uv run guppi casecheck` of `guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

> **then:**
> At `Stop`, `uv run guppi casecheck` refuses no reply for the way it opens a round of `case-guppi`, or for a text of the main agent's own before the round. Its other reasons stand.
> **＋** On `UserPromptSubmit`, `uv run guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends. The turn holds a round when a text that `case-guppi` gave back in it is a round by `is_round` of `guppi/casecheck.py`.
> **＋** It finds a fault when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon. While the session's event log holds no `prespec` line of this session after its `hi`, it also finds a fault when the main agent wrote text in the turn after the first round came back and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run guppi casecheck` in the turn follows, judged by `refusals` of `guppi/ledger.py`.
> **＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the text before the round, says that the round stands as shown and is not shown again, and tells the agent to open the next round with its Context paragraph or its first question, with nothing before it.
> **＋** `.claude/settings.json` registers `uv run guppi casecheck --prompt` on `UserPromptSubmit`, as `rule-hook-registry` renders it.
> **－** With no fault, in a turn with no round, and for text after the last question, it prints nothing.
> **－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
> **－** The person sees nothing of the note. It stores nothing and writes no file.
> **－** The refusals of the `Stop` run are counted as `estimate-case-check-judges-a-showing-after-a-refusal` sets it, and a layout fault of a round is not one of them.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `` a round of `case-guppi` from being shown after a text of the main agent's own written after the round came back (case 562) ``
>   - new: `` a round of `case-guppi` from being shown after a text of the main agent's own written after the round came back with no word to the agent: the `Stop` run lets the showing through, and the run on `UserPromptSubmit` tells the agent of it at the person's next message, so that the round is not shown twice (cases 562, 699.1) ``
>   - change: `a layout fault of a shown round passes the Stop run and is told to the agent at the person's next message by casecheck --prompt (case 699.1)`
> - [ ] update `estimate-case-check-refuses-text-before-a-round`
>   - set: `{status: pending, purpose: "Whether the Stop run of the Case check lets through a reply that shows a round of case-guppi after a text of the main agent's own, and the run on UserPromptSubmit tells the agent of it at the person's next message, judging only what follows the last refusal in the turn, only the first line after pre-spec, and no turn with no round"}`
>   - change: `the Criterion replaced whole — the Stop run lets a layout fault of a round through, and casecheck --prompt tells the agent at the next message; purpose set anew`
> - [ ] update `rule-hook-registry`
>   - old: `"uv run guppi context --prompt", "timeout": 30 },`
>   - new: `"uv run guppi context --prompt", "timeout": 30 }, { "type": "command", "command": "uv run guppi casecheck --prompt", "timeout": 30 },`
>   - change: `uv run guppi casecheck --prompt registered on UserPromptSubmit (case 699.1)`
> - [ ] `guppi/casecheck.py`: `stop` no longer adds the reason of `round_opening`; `run` takes `--prompt`, which reads the transcript of the `UserPromptSubmit` payload, leaves out the person's message when the transcript holds it, judges the last reply of the main agent and its turn by `round_opening`, prints the note on stdout and exits 0 always, its own error on stderr; the module docstring says so.
> - [ ] `tests/test_casecheck.py`: the tests of a round expect the `Stop` run to exit 0 on a layout fault; new tests whose names hold `round` run `--prompt` over a transcript whose last reply opens with a line of its own, or with text written after the round came back, and find the note on stdout and exit 0; a round with nothing before it, a turn with no round and an unreadable payload print nothing and exit 0.
> - [ ] `uv run pytest tests/test_casecheck.py`
> - [ ] `uv run guppi render`: `.claude/settings.json`
> - [ ] read `estimate-case-check-refuses-text-before-a-round`

> **ratification:**
> ```
> - decision[case 699.1][update][rule-case-check]{ref:rule-case-check}
> - decision[case 699.1][update][estimate-case-check-refuses-text-before-a-round]{ref:rule-case-check}
> - decision[case 699.1][update][rule-hook-registry]{ref:rule-hook-registry}
> ```

### Case 699.2 — A layout fault of a shown Case is told at the next message

> **given:**
> `rule-case-check`: the rule of the check, whose `purpose` and Purpose say what it prevents.
> **＋** `estimate-case-check-refuses-text-outside-the-list`: its Criterion is replaced whole.
> **＋** `estimate-case-check-shows-only-the-checked-case`: sets the comparison and the sending that the `Stop` run still refuses; its Criterion stands.
> **＋** `guppi/casecheck.py`: the check, whose `showing_layout` judges the layout of a showing.
> **＋** `guppi/ledger.py`: its `refusals` reads the refusals of the check in the transcript.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `.claude/settings.json`: registers the run on `UserPromptSubmit`.

> **when:**
> A reply of the main agent shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections, not a deferred decision in the short form. `Stop` fires and `uv run guppi casecheck` of `guppi/casecheck.py` runs on it. Then the person sends a message, and `uv run guppi casecheck --prompt` runs on `UserPromptSubmit`, as `.claude/settings.json` registers it.

> **then:**
> At `Stop`, `uv run guppi casecheck` refuses no showing for a text of the main agent's own before its first Case heading, outside its list and its `ratification`, or written after the summary of `case-guppi` came back.
> **＋** It still refuses a shown Case that differs from the checked text, or whose file was not sent or differs from the store, as `estimate-case-check-shows-only-the-checked-case` sets it.
> **＋** On `UserPromptSubmit`, `uv run guppi casecheck --prompt` judges the last reply of the main agent before the person's message, and the turn that reply ends, when that reply shows a Case.
> **＋** It finds a fault when a line that is not blank stands before the first Case heading. It finds a fault when a line between a Case heading and the next Case heading or the horizontal rule `---` is not blank, not a list item — a line that opens with `- `, `* ` or a number and `. ` — not a line indented under a list item, and not a line of the `ratification` blockquote. It finds a fault when the main agent wrote text in the turn after the first summary of `case-guppi` came back — a text given back whose first line that is not blank opens with `**Built:**` — and before its last tool call. It judges only the texts after the reply that the last refusal of `uv run guppi casecheck` in the turn follows, judged by `refusals` of `guppi/ledger.py`.
> **＋** On a fault it prints one line to stdout, which reaches the agent's context. The line quotes the first such text, says that the Case stands as shown and is not shown again, and tells the agent to write nothing of its own before the Case and to keep its own text after the horizontal rule at the next showing.
> **－** A text written before the first summary came back, text after the horizontal rule, a reply with no Case heading that holds a section, a fence tagged `DIFF` and a deferred decision in the short form are not judged, and it prints nothing for them.
> **－** It exits 0 always and never blocks the person's message. An error of its own goes to stderr.
> **－** The person sees nothing of the note. It stores nothing and writes no file.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old: `` and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` or written after the summary of `case-guppi` came back (case 611), each judged only by what follows the last refusal of the check in the turn, so that one showing again clears a refusal (case 692) ``
>   - new: `` and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` or written after the summary of `case-guppi` came back with no word to the agent, told in the same way at the person's next message, so that the Case is not shown twice, while a Case whose file was not sent or whose showing differs from the stored text is still refused (cases 611, 699.2), each judged only by what follows the last refusal of the check in the turn (case 692) ``
>   - set: `{purpose: "Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi or a Case from being shown after a text of the main agent's own with no word to the agent at the person's next message, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built"}`
>   - change: `a layout fault of a shown Case passes the Stop run and is told to the agent at the person's next message; a file not sent or a showing that differs from the store is still refused (case 699.2)`
> - [ ] update `estimate-case-check-refuses-text-outside-the-list`
>   - set: `{status: pending, purpose: "Whether the Stop run of the Case check lets through a reply that shows a Case with a text of the main agent's own before its first Case heading, outside its list and its ratification, or written after the summary of case-guppi came back, and the run on UserPromptSubmit tells the agent of it at the person's next message, judging only what follows the last refusal in the turn"}`
>   - change: `the Criterion replaced whole — the Stop run lets a layout fault of a Case through, and casecheck --prompt tells the agent at the next message; purpose set anew`
> - [ ] `guppi/casecheck.py`: `stop` no longer adds the reason of `showing_layout`; `--prompt` judges the last reply of the main agent and its turn by `showing_layout` when that reply shows a Case, and prints the note on stdout; the module docstring says so.
> - [ ] `tests/test_casecheck.py`: the layout tests expect the `Stop` run to exit 0 on a text before the heading, outside the list or after the summary came back; new tests run `--prompt` over a transcript whose last reply shows such a Case and find the note on stdout and exit 0; a showing with no file sent is still refused at `Stop`.
> - [ ] `uv run pytest tests/test_casecheck.py`
> - [ ] read `estimate-case-check-refuses-text-outside-the-list`

> **ratification:**
> ```
> - decision[case 699.2][update][rule-case-check]{ref:rule-case-check}
> - decision[case 699.2][update][estimate-case-check-refuses-text-outside-the-list]{ref:rule-case-check}
> ```

### Case 699.3 — The count of the refusals holds only the reasons left to the `Stop` run

> **given:**
> `estimate-case-check-judges-a-showing-after-a-refusal`: its Criterion is replaced whole.
> **＋** `rule-case-check`: the rule of the check.
> **＋** `guppi/casecheck.py`: the check, whose `give` counts its reasons.
> **＋** `guppi/ledger.py`: its `refusals` reads the refusals in the transcript.
> **＋** `tests/test_casecheck.py`: the tests of the check.

> **when:**
> The `Stop` hook `uv run guppi casecheck` of `guppi/casecheck.py` fires at the end of a reply of the main agent in a session with a `hi`, and finds a reason to refuse it: a shown Case that differs from `<plan>.checked.json`, a shown Case whose file was not sent or differs from the store, or an error of its own after it read the payload.

> **then:**
> The hook judges the reply the same whether `stop_hook_active` is set or not.
> **＋** It gives a reason that names a Case, opening with `case <id>:`, while fewer than three of its own refusals in the stretch hold a reason of that Case, and any other reason while fewer than three of them hold the same reason.
> **＋** It exits 2 while a reason is left to give, with those reasons on stderr.
> **＋** When no reason is left to give, it exits 0 and prints on stderr one line per Case it let through: "casecheck: case <id> shown unchecked after three refusals; the Spec hook compares it at ratification".
> **＋** The stretch is the records of the transcript at `transcript_path` after the last `user` record whose `origin.kind` is `human`; its own refusal is a `user` record marked `isMeta` whose text opens with `Stop hook feedback:` and holds a line that opens with `[uv run guppi casecheck]: `, judged by `refusals` of `guppi/ledger.py`, the function that `guppi onward` calls.
> **－** A text of the main agent's own before a round of `case-guppi` or outside the list of a showing is no reason of the `Stop` run. `uv run guppi casecheck --prompt` refuses nothing, so it counts nothing.
> **－** With `stop_hook_active` set and a transcript it cannot read, it exits 0 and prints nothing.
> **－** The run `uv run guppi casecheck --subagent` keeps its own guard, the store.

> **tasks:**
> - [ ] update `estimate-case-check-judges-a-showing-after-a-refusal`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a text of the agent's own before a round or outside the list is no reason of the Stop run`
> - [ ] `tests/test_casecheck.py`: a test of the count whose reason is a text before a round or outside the list gives a reason of a shown Case instead, such as a file not sent.
> - [ ] `uv run pytest tests/test_casecheck.py`
> - [ ] read `estimate-case-check-judges-a-showing-after-a-refusal`

> **ratification:**
> ```
> - decision[case 699.3][update][estimate-case-check-judges-a-showing-after-a-refusal]{ref:rule-case-check}
> ```

### Case 699.4 — A round or a Case with a layout fault is not shown again

> **given:**
> `rule-orchestration`: its Render sets the showing of a round and of a Case after a refusal.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-case-check`: the check of a showing.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `.claude/skills/wait-what/SKILL.md`: the skill of a plain explanation.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a question.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose items the label of a batch names.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
> **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` a reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it (case 452.4); a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question (case 561.9) ``
>   - new: `` a reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it (case 452.4); a round or a Case shown with a text of the agent's own before it or outside its list is not refused and is not shown again: the check tells the agent of it at the person's next message, and the agent keeps the form from the next showing on (case 699.4) ``
>   - old: `` the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, ``
>   - new: `` the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label in a batch naming its Case and its Frontier item as `## Showing and signing a Case` sets it (case 699.4), ``
>   - change: `a round or a Case shown with a layout fault is not shown again; the check tells the agent at the person's next message; the Context label of a round in a batch names its Case (case 699.4)`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a round or a Case with a layout fault is not shown again, and the Context label of a round in a batch names its Case`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 699.4][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 699.4][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> ```

### Case 699.5 — The Context label marks the round of each Case of a batch

> **given:**
> `rule-orchestration`: its Render sets the list of the rounds of a batch.
> **＋** `estimate-orchestration-marks-each-round-of-a-batch`: the new check of the mark.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.
> **＋** `/pre-spec`: the skill before which a batch is shown.
> **＋** `rule-case-check`: the check of how a round opens.
> **＋** `estimate-orchestration-signs-a-batch-together`: sets the batch and its list; its Criterion stands.
> **＋** `insight-orchestration-items-taken-together-unruled`: the Insight whose lesson of the batch headings this Case closes; set `actioned`.

> **when:**
> In Plan Mode before `/pre-spec`, the main agent shows in one list the rounds of `case-guppi` that came back for a batch of Cases, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The `**Context:**` paragraph of each first round on an item opens with a label that names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`.
> **＋** A later round, which has no Context paragraph, is marked by its question numbers `<Case id>.Q<n>` alone.
> **＋** No heading or other line of the main agent's own stands before a round to mark where it begins, so the reply opens with a Context label or a question line, which the check of `rule-case-check` accepts.
> **－** A round shown alone, outside a batch, keeps its `**Context:**` label as `case-guppi` gave it, translated.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` one list shows every round that came back, each question numbered `<Case id>.Q<n>`; ``
>   - new: `` one list shows every round that came back, each question numbered `<Case id>.Q<n>` and the `**Context:**` label of each first round naming its Case and its Frontier item, translated, such as `**Context — Case 7 (C2):**`, with no heading or other line of the agent's own to mark where a round begins (case 699.5); ``
>   - change: `the Context label of each first round of a batch names its Case and its item, and no heading of the agent's own marks a round (case 699.5)`
> - [ ] create `estimate-orchestration-marks-each-round-of-a-batch`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the list of the rounds of a batch marks where each Case's round begins by its Context label, which names the Case and its item, and by its question numbers, with no heading of the main agent's own`
>   - method: `by hand at the Retro of this session: the new Render of rule-orchestration in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow]`
> - [ ] update `insight-orchestration-items-taken-together-unruled`
>   - set: `{status: actioned}`
>   - change: `actioned: the Context label of each first round of a batch names its Case, so no heading of the agent's own marks a round (case 699.5)`
> - [ ] read `estimate-orchestration-marks-each-round-of-a-batch`

> **ratification:**
> ```
> - decision[case 699.5][update][rule-orchestration]{ref:rule-orchestration}{addresses:lesson-orchestration-batch-rounds-headed-by-their-case}
> - decision[case 699.5][create][estimate-orchestration-marks-each-round-of-a-batch]{ref:rule-orchestration}{tags:session,workflow}
> - decision[case 699.5][update][insight-orchestration-items-taken-together-unruled]{ref:insight-orchestration-items-taken-together-unruled}
> ```

### Case 699.6 — The showing example passes both runs of the check

> **given:**
> `rule-orchestration`: its Render holds the showing example and the sentence on its test.
> **＋** `estimate-orchestration-showing-example-passes-the-check`: its Criterion is replaced whole.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `tests/test_orchestration.py`: the test of the example.
> **＋** `guppi/casecheck.py`: the check whose functions the test runs.
> **＋** `rule-case-check`: the check of a showing.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `showing` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it the functions of `guppi/casecheck.py` that the check of `rule-case-check` runs over a reply that shows a Case — the comparison of its `Stop` run and the judgment of the layout of its run on `UserPromptSubmit` — with a store whose sub-cases hold the ledger lines the example's `ratification` gives them.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## Showing and signing a Case`, one block tagged `showing`: a reply that shows a Case with two sub-cases, its heading, one list with an item per sub-case, one `ratification` and the agent's own text after one horizontal rule.
> **＋** The `ratification` of the example is a quote block: the line `> **ratification:**`, then the fence and the ledger lines of both sub-cases, each line opening with `> `.
> **＋** The example is in English; the paragraph before the block says that in the chat the heading, the names and the short texts stand in the language of the chat, that the file goes by `SendUserFile` in the same reply, and that the example passes the check of `rule-case-check` at the `Stop` of the reply and at the person's next message, which is the source of the limits, and that a refusal of the check, or its note at the person's next message, names the limit a showing broke; it lists no other limit.
> **＋** The check finds no text outside the list and the `ratification`, reads the `ratification` as the showing of each sub-case it names, and finds no difference from the store, and the test passes.
> **＋** The example with the lines of its fence not quoted gives the finding of a text outside the list, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `showing`, both tests of `tests/test_orchestration.py` that read it fail with a message that names the file; no test of the file is skipped.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` A test runs over the example the functions that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, and fails on any refusal, so the example keeps to that check as the check stands (case 651.2). ``
>   - new: `` A test runs over the example the functions that the check of `rule-case-check` runs over a reply that shows a Case, at the `Stop` of the reply and at the person's next message, and fails on any refusal or note, so the example keeps to that check as the check stands (cases 651.2, 699.6). ``
>   - old: `Copy its form; a refusal of the check names the limit a showing broke.`
>   - new: `Copy its form; a refusal of the check, or its note at the person's next message, names the limit a showing broke (case 699.6).`
>   - change: `the showing example is tested by the functions of both runs of the check (case 699.6)`
> - [ ] update `estimate-orchestration-showing-example-passes-the-check`
>   - set: `{status: pending, purpose: "Whether the example of a showing in orchestration.md passes the check of rule-case-check of a reply that shows a Case, at its Stop and at the person's next message, so the form the main agent copies stays a form the check accepts"}`
>   - change: `the Criterion replaced whole — the example passes the comparison of the Stop run and the layout judgment of the run at the next message; purpose set anew`
> - [ ] `uv run pytest tests/test_orchestration.py`
> - [ ] read `estimate-orchestration-showing-example-passes-the-check`

> **ratification:**
> ```
> - decision[case 699.6][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 699.6][update][estimate-orchestration-showing-example-passes-the-check]{ref:rule-orchestration}
> ```

### Case 699.7 — The Context label marks the round of each Case after the findings of `/pre-spec`

> **given:**
> `rule-prespec`: its Render sets the list of the rounds in the loop after the findings.
> **＋** `estimate-prespec-gathers-the-answers-after-findings`: its Criterion is replaced whole.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the skill rendered from `rule-prespec`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of a question.
> **＋** `vault/wiki/orchestration.md`: sets the showing of a Case and of a batch.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session, whose items the label names.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec of the session, read at Retro.

> **when:**
> `/pre-spec` has reported findings in Cases of the plan, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

> **then:**
> The main agent sends each finding in a Case, with each answer of the report that bears on that Case, to the `case-guppi` of that Case by `SendMessage`, one message to each `case-guppi`, as soon as the report asks the person no question or the person has answered every question of the report.
> **＋** While a question of the report is unanswered, the main agent sends nothing to any `case-guppi`.
> **＋** A question of the report that the person leaves unanswered is asked again in the shape of `.claude/skills/grill-me/SKILL.md` under its number.
> **＋** The main agent ends each turn that sends to a `case-guppi`, and each turn that an answer opens while another answer it sent is still out, with one line that opens with a bold label ending in a colon and names the Cases that have answered and the Cases still out.
> **＋** That line holds nothing of what an answer says and no question, and the main agent writes nothing else in the chat while an answer is out and passes on no answer of one `case-guppi` alone.
> **＋** It then shows the person one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>` by the Case it belongs to, sends each answer to the `case-guppi` of its Case in one message, and repeats the wait and the list until every `case-guppi` it sent has answered with its Case.
> **＋** In that list the `**Context:**` label of each first round on an item names its Case id and its item of `raw/<date>/<hi HHMM>/frontier.md`, translated, such as `**Context — Case 7 (C2):**`, and no heading or other line of the main agent's own marks where a round begins.
> **＋** It then shows every Case built again in one reply, in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
> **－** When an answer brings back a round while another answer is still out, the round is not shown in that turn, and `uv run guppi casecheck` does not refuse the reply that opens with the labelled line.
> **－** Outside this loop, Cases go out together for one ratification only in a batch, as `vault/wiki/orchestration.md` sets it.
> **－** A question that no answer settles stays in the next list under its number.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `` numbered `<Case id>.Q<n>` — the id of its Case and its number in the round — so that each answer goes back to its `case-guppi`. ``
>   - new: `` numbered `<Case id>.Q<n>` — the id of its Case and its number in the round — so that each answer goes back to its `case-guppi`; the `**Context:**` label of each first round names its Case and its Frontier item, translated, such as `**Context — Case 7 (C2):**`, and no heading or other line of your own marks where a round begins (case 699.7). ``
>   - change: `in the list of the rounds after the findings, the Context label of each first round names its Case (case 699.7)`
> - [ ] update `estimate-prespec-gathers-the-answers-after-findings`
>   - set: `{status: pending, method: "by hand at the Retro of this session: the new Render of rule-prespec in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — the Context label of each first round in the list names its Case; method set to the reading of the Spec at Retro`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-gathers-the-answers-after-findings`

> **ratification:**
> ```
> - decision[case 699.7][update][rule-prespec]{ref:rule-prespec}
> - decision[case 699.7][update][estimate-prespec-gathers-the-answers-after-findings]{ref:rule-prespec}
> ```
