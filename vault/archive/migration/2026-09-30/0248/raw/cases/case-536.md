## Case 536 — case-guppi gives the meaning of the person's words and never quotes them

> **context:**
> The main agent sends the person's words and answers to `case-guppi` in Russian, verbatim and untranslated, as `rule-case-protocol` requires. The frame of `case-guppi` in `rule-case-build` says to write the whole Case in English, but it does not say what to do with a quotation of those words. So `case-guppi` has copied the person's Russian words into the `context` of a Case. The pre-spec language finding then found a letter outside the Latin script, and the Case was built and ratified again. This happened twice. Case 512 quoted the person in Russian in its context (`lesson-case-build-quotes-the-person-in-the-chat-language`). At the rebuild of Case 524, its context held the person's Russian reply (`lesson-case-build-rebuild-quotes-the-relayed-words`). Both lessons are clustered under `insight-case-form-chat-form-read-by-no-script`, which is open in the backlog. The person asked for one line in the frame of `case-guppi` so that it does not write their words verbatim.
> The Case adds one sentence to the Render of `rule-case-build`. The sentence uses the placeholders `{{chat_lang}}` and `{{documentation_lang}}`, which the render fills from `rule-guppi-config` (case 476.1). No page is created, so no vault query ran. In the frame, `estimate-case-build-writes-the-case` already promises the Case "whole in English". A Russian quotation breaks that line, so a reading against it catches one. The person chose to leave that Estimate as it stands (round answer (b)), and its reading can still run in this session. `estimate-case-build-writes-a-plain-round` is about the shape of a round and is not touched. `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` is about readers in code and is not touched either. The line of `rule-case-protocol` that has the main agent relay the words verbatim stands: the new sentence governs what `case-guppi` writes, not what it gets. The `－` line of `estimate-language-spec-prose-in-english` says that a quotation in `given`, `when` or `then` keeps its language. That line describes what the check reads, and it grants no permission, so it stands. This Case does not add the language finding to the `SubagentStop` check of `rule-case-check`: Case 537 of this session does that. This Case leaves the backlog item `rule-prespec-script-skips-code-spans` as it stands.

> **problem:**
> `case-guppi` gets the person's words in Russian and has no instruction about quoting them. So a Case sometimes holds a Russian quotation, the pre-spec language finding refuses it, and the Case is built and ratified again.

> **recommend:**
> Add one sentence to the frame of `case-guppi`: the person's words reach it in the chat language, and it gives their meaning in the documentation language and quotes none of them word for word in the Case. This is the one line the person asked for, and it closes the cause the second lesson names. Adding the language finding to the `SubagentStop` check in code is not part of this Case, because Case 537 of this session does that.

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the rendered frame
> **＋** `rule-case-protocol` — the main agent relays the person's words verbatim and untranslated
> **＋** `rule-prespec` — its language finding refuses a name, `context` or `problem` with a letter outside the script of the documentation language

> **when:**
> The main agent sends `case-guppi`, by the dispatch or by `SendMessage`, the person's words or answers in the chat language, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> `case-guppi` gives the meaning of the person's words in the documentation language in the Case it answers with.
> **＋** No part of the Case quotes the person's words word for word.
> **＋** The language finding of `rule-prespec` finds no quotation of the person in the name, `context` or `problem` of a Case built this way.
> **－** The main agent still relays the person's words to `case-guppi` verbatim and untranslated, as `rule-case-protocol` requires.

> **tasks:**
> - [ ] update `rule-case-build` — one sentence added to its Render: `case-guppi` gives the meaning of the person's words and never quotes them
>   - old: `You decide nothing the person has not decided.`
>   - new: `The person's words reach you in {{chat_lang}}: give their meaning in {{documentation_lang}}, and quote none of them word for word in the Case. You decide nothing the person has not decided.`
>   - change: `case-guppi gives the meaning of the person's words in the documentation language and quotes none of them word for word in the Case (case 536)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`

> **ratification:**
> ```
> - decision[case 536][update][rule-case-build]{ref:rule-case-build}
> ```
