## Case 562 — The end-of-reply check refuses text before a round

> **context:**
> When `case-guppi` answers with a round of questions, the main agent shows the round in the chat. The schema says the round opens with its Context paragraph or its first question, and the main agent's own text stands only after the last question and one horizontal rule. In session 1736 the main agent broke this before every round. It wrote a line of its own first, for example that `case-guppi` builds Case N and starts with a round. So `estimate-case-protocol-shows-the-built-case` failed, and case 560 put it off. The root cause in `lesson-case-protocol-own-text-before-a-round` is that no check reads the reply that shows a round. Today the `Stop` run of `uv run guppi casecheck` reads only Cases shown under their headings. It returns before any other reading when the reply shows none. This Case adds a check of how a round opens to that run, with no new hook. The line may stand in a text written before the call that dispatches `case-guppi`, so before `/pre-spec` the check reads every text of the main agent in the turn, not only `last_assistant_message`. The turn is found by `turn_of_reply`, and the question line by `QUESTION_LINE`, which the check of the rounds on `SubagentStop` already uses. Nothing in the vault says where the answer of an `Agent` or `SendMessage` call stands in the transcript, or whether an answer that comes back after the turn ended opens a record that `turn_of_reply` takes for a prompt. So a task measures this before the reader is written. The Context label stands translated in the chat, so the check accepts any bold label that ends in a colon on the first line. That catches the fault that was seen. It does not judge whether the whole paragraph is a Context. At pre-spec `ask-guppi` found that this check would refuse the loop after the findings that 561.1 and 561.2 set. In that loop, one turn holds the report, the `SendMessage` calls and the gathered list of the questions that came back, and the hook of 561.5 sends the agent on with no prompt of the person in between. The person decided that once the session's event log holds a `prespec` line of this session after its `hi`, the check does not judge text written before the last tool call. It judges only the first line of the reply, and the gathered list opens with a question line. The window is judged by the same function that the hook of `rule-prespec-hook` uses on `ExitPlanMode`, imported. Case 561.9 replaces the Criterion of `estimate-case-protocol-shows-the-built-case` whole. The person decided that 561.9 goes back to its own `case-guppi`. There it carries `{supersedes:case 560}` on its line for that Estimate, so the defer is retired where the Criterion changes and this Case does not name the page. A second whole replacement of one Criterion would be the finding of 561.4. The Estimate page carries no `deferred_by` field, because `generate` writes that field only on rules, entities and Insights, and so `backlog.md` does not list it. For the same reason 561.9 also narrows the schema's sentence that a reply the `Stop` check refuses is followed by a reply that sends the file. That sentence stands in `vault/wiki/case-schema.md` and word for word in the Criterion 561.9 writes. A refused round has no file and is shown again, so 561.9 also adds that line. This Case is the check alone. Its promise is the new `estimate-case-check-refuses-text-before-a-round`, and that answers what done means. The slug is free: a Glob of `vault/**/estimate-case-check-refuses-text-before-a-round*.md` found no file. The `create` carries a `ref`, so no vault query ran. The lesson stands in the ledger of session 1736, and its fix is ratified in another session, so no `{addresses}` mark is written. `rule-case-check` is a Leaf that still carries `## How it works`. This Case adds a sentence there, as 561.10 and case 555.1 did, and keeps the section as they keep it. Its removal, which the schema of rules asks for at the next touch, is not taken up here. Searches over the frame: a Grep for `first question` over the repository outside `vault/raw/` printed 31 files. Of the live rules and harness files among them, `.claude/agents/case-guppi.md`, `vault/wiki/case-schema.md`, `rule-case-build` and `rule-case-protocol` set the form of a round. Each says what this check enforces, and none becomes false. A Grep for `shows? (it|a round|the round)|round of questions` over `vault/wiki/rules/` printed `rule-context-size`, `rule-case-build`, `rule-case-protocol`, `rule-spec-write`, `rule-sprint`, `rule-skill-wait-what`, `rule-handoff` and `rule-page-read`. Over `.claude/` it printed `skills/wait-what/SKILL.md`, `skills/handoff/SKILL.md` and `agents/case-guppi.md`. Of these, only `rule-skill-wait-what` sets a reply about a round: the plain re-pitch. The check leaves that reply out, because its turn holds no round. The other hits use "shows it" of other things. A Grep for `rule-case-check` over the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed 26 files. Besides the sentence that 561.9 narrows, `estimate-case-build-writes-the-case` says the `SubagentStop` hook neither checks nor stores a round. That stays true, because this check runs on `Stop` and stores nothing. `rule-case-build`, `rule-spec-write`, `rule-spec-reconcile` and `rule-plan-mode` name the hook for what it writes or where it stands, and stay true. The other `Stop` hooks in `.claude/settings.json` are `guppi ledger`, `guppi ratified`, `guppi context` and `guppi onward`, with `guppi onward --plan` from 561.5. Each reads a `LEDGER` block, the Spec, the event log or the size of the context, and none judges the text of a round, so none conflicts. Estimates of `rule-case-check` left alone, and why. `estimate-case-check-shows-only-the-checked-case`, replaced by 561.10, speaks of shown Cases, not rounds. `estimate-case-check-exits-2-on-an-error` already covers an exception while the `Stop` run reads the transcript or the event log. `estimate-case-check-requires-each-question-of-the-rounds` reads the rounds on `SubagentStop`, and its `QUESTION_LINE` is reused unchanged. 561.10 changes the same module and page. Its anchor on the page, the sentence on a parent compared part by part, does not overlap the two anchors of this Case. The hook refuses a reply and writes nothing, so no line is lost while the code runs before the page lands, and no old form is kept.

> **problem:**
> The rule that the main agent writes nothing of its own before a round of `case-guppi` is text alone, and it failed at every round of a session. No script reads the reply that shows a round. The question is how the rule is enforced, and how the defer of case 560 on the failed Estimate is retired.

> **recommend:**
> - **How is the rule "nothing before a round" enforced?**
>   Recommended: (a) a check at the end of the reply: `guppi casecheck` on `Stop`, when the turn holds a round of `case-guppi`, refuses a reply that does not open with the Context paragraph or the first question line, and the agent shows the round again; the main agent's own questions are not checked.
>   Answer: (a).
> - **How is the earlier put-off closed?**
>   Recommended: (a) Case 561.9, sent back to its own `case-guppi`, carries `{supersedes:case 560}` on its line for `estimate-case-protocol-shows-the-built-case` and is ratified again; this Case holds only the check.
>   Answer: (a).
> - **Who fixes the schema's sentence on a refused reply?**
>   Recommended: (a) Case 561.9, while it is sent back, narrows the sentence of the schema and its line in the check to a reply that shows a Case, and adds that a refused round is shown again with nothing before it; this Case stays the check alone.
>   Answer: (a).
> - **Change**
>   Asked: the pre-spec finding that the check would refuse the gathered list of the loop after the findings of `/pre-spec`, which runs in one turn. The person agreed with the recommendation: once the session's event log holds a `prespec` line of this session after its `hi`, the check does not judge text before the last tool call of the turn and judges only the first line of the reply. Before `/pre-spec` the check stays whole. The context also says that `## How it works` of `rule-case-check` is kept, as 561.10 keeps it.
>   Taken: a `then` line and a `－` line bound the text check to the time before `/pre-spec`. The window is judged by the function of the hook of `rule-prespec-hook`, and the page text and the tasks say so. The context records the finding and the kept section.

> **given:**
> `rule-case-check` — the rule of the `Stop` check, whose Purpose and How it works gain the round
> **＋** `guppi/casecheck.py` — the `Stop` run of `uv run guppi casecheck`, which gains the reading of a round
> **＋** `tests/test_casecheck.py` — the tests of the check
> **＋** `estimate-case-check-refuses-text-before-a-round` — the promise this Case creates
> **＋** `rule-case-protocol` — the schema, whose rule on the showing of a round the check enforces
> **＋** `.claude/skills/grill-me/SKILL.md` — the question line of a round
> **＋** `.claude/skills/wait-what/SKILL.md` — the plain re-pitch, which the check does not judge
> **＋** `/pre-spec` and `/hi` — the moments of the main agent's own questions; `/pre-spec` leaves the `prespec` line of the session in the event log, judged as the hook of `rule-prespec-hook` judges it

> **when:**
> `Stop` fires after a reply of the main agent, and `uv run guppi casecheck` runs on it.

> **then:**
> When the turn of the reply, the records after the person's last prompt, holds a round of `case-guppi`, `uv run guppi casecheck` judges how the reply opens. A round is a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that holds a question line `❓ **Q<n>** - **<title>**:` of `.claude/skills/grill-me/SKILL.md`, no Case heading and no first line `**Fact:**`.
> **＋** While the session's event log holds no `prespec` line of this session after its `hi`, it exits 2 when the main agent wrote text in the turn before its last tool call.
> **＋** It exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon, the label of the Context paragraph as it stands translated.
> **＋** Its reason on stderr quotes the text that stands before the round and tells the agent to show the round again, opening with its Context paragraph or its first question, with nothing before it.
> **＋** Text after the last question and one horizontal rule is not judged.
> **＋** The check runs in the same `Stop` run as the comparison of shown Cases, and a reply that both refuse gives both reasons.
> **－** Once the session's event log holds a `prespec` line of this session after its `hi`, text before the last tool call of the turn is not judged, so the loop after the findings of `/pre-spec`, which runs in one turn, is judged only by the first line of its reply.
> **－** A turn with no round of `case-guppi` is not judged: the main agent's own questions in the report of `/pre-spec`, at `/hi` or at a stop of Work Mode, a `**Fact:**` answer shown with the question that stood open, and a re-pitch by `.claude/skills/wait-what/SKILL.md`.
> **－** On the re-fire (`stop_hook_active`) it exits 0, so the round shown again after a refusal is not judged again.
> **－** It stores nothing and writes no file.

> **tasks:**
> - [ ] update `rule-case-check` — the `Stop` run judges how a round of `case-guppi` opens
>   - set: `{purpose: "Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, and a round of case-guppi from being shown after a text of the main agent's own"}`
>   - old:
>     ````
>     than the ones that passed them; the Case reaches the person in a file
>     ````
>   - new:
>     ````
>     than the ones that passed them, and a round of `case-guppi` from being shown after a text of the main agent's own (case 562); the Case reaches the person in a file
>     ````
>   - old:
>     ````
>     on the re-fire (`stop_hook_active`) it exits 0.
>     ````
>   - new:
>     ````
>     on the re-fire (`stop_hook_active`) it exits 0. The same run judges how a round opens (case 562). When the turn of the reply — the records after the person's last prompt, by `turn_of_reply` — holds a round of `case-guppi`, a text that `case-guppi` gives back to an `Agent` or `SendMessage` call and that holds a line `❓ **Q<n>** - **<title>**:` by `QUESTION_LINE`, no Case heading and no first line `**Fact:**`, it exits 2 when the first line of the reply that is not blank opens neither with `❓ ` nor with a bold label that ends in a colon — the label of the Context paragraph, translated — and, while the session's event log holds no `prespec` line of this session after its `hi`, judged by the function the hook of `rule-prespec-hook` uses, when the main agent wrote text in the turn before its last tool call; after `/pre-spec` that text is not judged, since the loop after its findings runs in one turn. The reason quotes the text before the round and tells the agent to show the round again with nothing before it. Text after the last question and one horizontal rule is not judged, a turn with no round — the main agent's own questions, a `**Fact:**` answer, a re-pitch by `wait-what` — is not judged, and the check stores nothing.
>     ````
>   - change: `the Stop run refuses a reply that shows a round of case-guppi after a text of the main agent's own; after pre-spec only the first line of the reply is judged (case 562)`
> - [ ] create `estimate-case-check-refuses-text-before-a-round`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the Stop run of the Case check refuses a reply that shows a round of case-guppi after a text of the main agent's own, judges only the first line of the reply after pre-spec, and leaves a turn with no round alone`
>   - method: `uv run pytest tests/test_casecheck.py -k round; by hand in a later session, the first rounds of case-guppi shown before and after pre-spec, the replies and the hook's refusals read in the transcript`
>   - tags: `[hooks, harness, workflow]`
> - [ ] by hand, before the reader is written: in a transcript of this session, where the text that `case-guppi` gives back stands after an `Agent` call and after a `SendMessage` call, and whether an answer that comes back after the turn ended opens a record that `turn_of_reply` takes for a prompt; the reader follows what is measured, and the module docstring names the measurement
> - [ ] `guppi/casecheck.py`: a function over the records of the turn and the reply finds a round among the texts `case-guppi` gave back, by `QUESTION_LINE`, `split_cases` and the first line `**Fact:**`, and gives the reason when the reply's first line that is not blank opens neither with `❓ ` nor with a bold label ending in a colon, or, while the window of `guppi/prespec.py` that the `ExitPlanMode` hook judges holds no `prespec` line of this session after its `hi`, when a text of the main agent stands before the last tool call of the turn; the window function is imported, not copied; `stop` runs the check before it returns on a reply that shows no Case, and joins its reason with the comparison's; the module docstring says so
> - [ ] `tests/test_casecheck.py`: a turn with a round and a reply that opens with a line of its own exits 2; before a `prespec` line, a turn with a round and a text before the `Agent` call exits 2; after a `prespec` line, a turn with a text before a `SendMessage` call and a reply that opens with a question line passes, and a reply that opens with a line of its own exits 2; a reply that opens with the Context label or with the first question passes; a turn with a `**Fact:**` answer, with no answer of `case-guppi`, or with the main agent's own question lines alone passes; the re-fire exits 0
> - [ ] read `estimate-case-check-refuses-text-before-a-round` — in a later session

> **ratification:**
> ```
> - decision[case 562][update][rule-case-check]{ref:rule-case-check}
> - decision[case 562][create][estimate-case-check-refuses-text-before-a-round]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```
