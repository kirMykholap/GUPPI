## Case 524 — A quotation in a round stands as a blockquote on its own line

> **context:**
> When a round of questions quotes the words of a page, a file or a reply, the quoted words stand inline in plain double quotes. When the main agent shows the round in Russian, they stand in Russian angle quotes. So the quoted words do not stand apart from the agent's own words. Here is an example from the first round on Case 521: *The parser kept only "Correct the description of".* The four quoted words are a fragment of a page, but they read like part of the agent's sentence. The person saw this in the rounds of this session and said, translated from the chat, that the quotations "are not formatted as quotations" and that this should be fixed. Rounds quote pages often since case 512, which lets a number stand in a round only beside a quotation of the words it points to.
> In one round the person decided the following:
> - Every quotation stands as a blockquote on its own line, a fragment of a few words too.
> - The rule is for rounds only. It covers the rounds of `case-guppi` and the person's own `/grill-me`, so it is set in the grill-me template.
> - When the main agent shows a round in Russian, it keeps the blockquote and the quoted words as the source holds them.
>
> The person asked to see an example before ratifying. The example is the new text of the template in 524.1: the `new` of its first and second pairs. The first pair puts a quotation under the `**Now:**` line. The second puts one inside an `**After:**` item. In a round the `**After:**` item is written `  - **After:** …`, so its text begins four spaces in. A blockquote line indented four spaces, `    > …`, renders inside that item. With no indentation it would end the list. In the template both lines carry the four extra spaces of the code block that holds the template.
>
> Pre-spec found a fault in the first ratified text, and the person accepted the fix. In the person's words, translated from the chat: "Okay, I agree with the recommendations". 524.1 had put the third decision into the grill-me skill. But the main agent shows a round of `case-guppi` by `vault/wiki/case-schema.md`, the Render of `rule-case-protocol`: "translated into {{chat_lang}} line by line, slugs, paths and quotations unchanged". So the decision stood in a file the main agent does not read at the showing, and `estimate-case-protocol-shows-the-built-case`, which promises that showing, was named by no Case. The new sub-case 524.3 adds "each quotation in its blockquote" to that sentence and replaces the Criterion of that Estimate whole. 524.1 no longer holds the sentence on the showing, in the skill or in its Criterion. The showing is signed once, in 524.3, and the person's own `/grill-me` is not translated. Cases 521.4 and 523 of this plan also update `rule-case-protocol`. 521.4 changes a pair in the short-form paragraph, and 523 has only a `change`. The `old` of 524.3 is in the paragraph on who builds a Case, so it overlaps neither.
>
> What `case-guppi` found in the frame. `rule-case-build` says that the first round opens with "one prose paragraph under the label `**Context:**`" and that "A list in the context stands as the grill-me template sets a list". The example of this item stands in a Context, so 524.2 lets a quotation there stand as the template sets it too. The prose goes on after the blockquote, as it does after a list. Its Estimate, `estimate-case-build-writes-a-plain-round`, reads the Context and the instructions that point to the template, so its Criterion is replaced whole. `estimate-skill-grill-me-asks-in-rounds` reads the shape of a question, so 524.1 replaces its Criterion whole and adds a line on the quotation.
> The check of the answer notes four lines that are not carried word for word. Each one changes on purpose:
> - In 524.1, "The `**Context:**` paragraph of a round of `case-guppi`, its lists included…" now says "its lists and quotations included". The quotations of the Context are read by the Estimate of 524.2.
> - In 524.2, "The instructions of `case-guppi` point each question, and each list of the Context…" now names each quotation of the Context too.
> - In 524.2, "The shape of a question, and what counts as a list, are read by `estimate-skill-grill-me-asks-in-rounds`…" now names the form of a quotation in a question too.
> - In 524.3, "An answer with no Case heading and no first line `**Fact:**` is a round of questions…" now adds "each quotation in its blockquote" after "quotations unchanged". The rest of the line is the same.
>
> Every other line is carried word for word. The check also notes `then` lines of sibling sub-cases that share words: two lines of 524.2 with a line of 524.1, and the showing line of 524.3 with a line of 524.1 and a line of 524.2. The shared words are the path `.claude/skills/grill-me/SKILL.md`, "quotation", "blockquote" and common words. The 524.1 line promises that the skill asks for no sub-agent. The 524.2 lines promise the form of a list and of a quotation in the Context that `case-guppi` writes. The 524.3 line promises what the main agent keeps when it shows a round. These are separate promises with separate readings. The line "only beside a short quotation of the words it points to" stays true: the number stands in the sentence that introduces the blockquote.
> Several sentences stay true and stand:
> - `rule-language` keeps "quotations from pages" as they are. This agrees.
> - The template's "An option has nothing else under it" stays true: the blockquote stands inside the `**After:**` item, not as a second item.
> - The `"nothing exists yet"` of the template is a phrase to write, not a quotation of a source.
>
> No code reads a round. A search of `guppi/` for "round" finds only unrelated lines in `lint.py` and `render.py`, so no reader keeps an old form. The Case creates no page, so no vault query was run.
> Not done: the `context`, `problem` and `recommend` of a Case, the main agent's own chat text, and a mechanical check of a round. The person chose rounds only.

> **problem:**
> The quoted words of a page or a reply stand inside the agent's sentence in quote marks. The person cannot tell at a glance what the page says and what the agent says about it. No text of the harness sets a form for a quotation in a round.

> **recommend:**
> Set the form in the grill-me template. Every quotation stands as a blockquote on its own line under the sentence that introduces it and names its source. Under an `**After:**` item it stands indented four spaces, inside the item. Let the Context of `case-guppi` point to the same form, as it already does for a list. Let the case schema say that the Russian showing keeps each quotation in its blockquote, since that is the text the main agent reads when it shows a round. Rejected: italics inline for a fragment. The person chose a blockquote for every quotation.

### Case 524.1 — The grill-me template sets a quotation as a blockquote on its own line

> **given:**
> `rule-skill-grill-me` — the rule; its Render is the grill-me skill and its question template
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill rendered from it
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by its `skills` field
> **＋** `guppi/render.py` — writes the file from the Render
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise on the shape of a round; its Criterion is replaced whole
> **＋** `rule-case-protocol` — the case schema, which sets how the main agent shows a round of `case-guppi`

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer, together with the lines of a list under it. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
> **＋** The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark `🔹` and its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
> **＋** A list stands one item per line, never inside a sentence. This covers items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things. Under an `**After:**` item a list stands nested inside that item.
> **＋** A quotation, words taken from a page, a file or a reply, stands as a blockquote on its own line under the sentence that introduces it and names its source, a fragment of a few words too; it never stands inside a sentence in quote marks. Under an `**After:**` item it stands indented to the text of the item, inside that item, and is no second item.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
> **－** A short series of words inside a sentence stays in the sentence.
> **－** No line of a question except an option starts with `🔹`.
> **－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `rule-case-protocol`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
> **－** The `**Context:**` paragraph of a round of `case-guppi`, its lists and quotations included, and the place of its case numbers are not read here. They are the promises of the Estimates of the rule of `.claude/agents/case-guppi.md`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

> **tasks:**
> - [ ] update `rule-skill-grill-me`
>   - old: `"nothing exists yet" when nothing does>`
>   - new:
>     ````
>     "nothing exists yet" when nothing does>
>         <a sentence that introduces a quotation and names its source, when the question quotes one>:
>         > <the quoted words, as the source holds them>
>     ````
>   - old:
>     ````
>     **After:** <what holds with this option>
>
>         🔹 **(b) <option name>**
>     ````
>   - new:
>     ````
>     **After:** <what holds with this option>
>             > <a quotation inside the item, indented four spaces as far as the text of the item>
>
>         🔹 **(b) <option name>**
>     ````
>   - old: `` In the recommended answer it stands on the lines under `➡️`, which close the question. ``
>   - new:
>     ````
>     In the recommended answer it stands on the lines under `➡️`, which close the question.
>
>     A quotation — words taken from a page, a file or a reply to show what they say — stands as a blockquote on its own line, a fragment of a few words too; it never stands inside a sentence in quote marks. The sentence that introduces it stands on the line before it and names its source, and the quoted words stand as the source holds them. In the `**Now:**` text the blockquote stands under the sentence that introduces it. Under an `**After:**` item it stands inside that item, indented four spaces as far as the text of the item, so that it renders there and is no second item. In the recommended answer it stands on the lines under `➡️`.
>     ````
>   - change: `a quotation in a round stands as a blockquote on its own line, inside an After item indented to its text (case 524.1)`
> - [ ] update `estimate-skill-grill-me-asks-in-rounds`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a quotation stands as a blockquote on its own line (case 524.1)`
> - [ ] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
> - [ ] read `estimate-skill-grill-me-asks-in-rounds` — in a later session after the render: `uv run guppi render --check`, then one round that quotes a page read in the chat against the Criterion

> **ratification:**
> ```
> - decision[case 524.1][update][rule-skill-grill-me]{ref:rule-skill-grill-me}
> - decision[case 524.1][update][estimate-skill-grill-me-asks-in-rounds]{ref:rule-skill-grill-me}
> ```

### Case 524.2 — A quotation in the Context of a first round stands as the template sets it

> **given:**
> `rule-case-build` — the rule page whose Render holds the round instructions of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from it
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill whose template sets a list and a quotation
> **＋** `estimate-case-build-writes-a-plain-round` — the promise on a readable round; its Criterion is replaced whole
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape of a question, a list and a quotation
> **＋** `rule-case-protocol` — the rule that lets the story sections of a Case keep their numbers

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
> **＋** A list in the `**Context:**` stands one item per line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a list.
> **＋** A quotation in the `**Context:**` stands as a blockquote on its own line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a quotation.
> **＋** The instructions of `case-guppi` point each question, and each list and each quotation of the Context, to `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
> **＋** The round says what it rests on in plain words and uses no number where plain words are enough.
> **＋** A case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in any line of the round, the `➡️` line included, only beside a short quotation of the words it points to, as the source of that quotation.
> **＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
> **－** A page name in a code span is no such reference: it stays where the question is about that page.
> **－** The shape of a question, what counts as a list, and the form of a quotation in a question are read by `estimate-skill-grill-me-asks-in-rounds`, not here.
> **－** The `context`, `problem` and `recommend` of a Case keep their numbers as `rule-case-protocol` allows: this promise is about a round only.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `A list in the context stands as the grill-me template sets a list.`
>   - new: `A list or a quotation in the context stands as the grill-me template sets it, and the prose goes on after it.`
>   - change: `a quotation in the Context of a first round stands as the grill-me template sets it (case 524.2)`
> - [ ] update `estimate-case-build-writes-a-plain-round`
>   - set: `{status: pending, purpose: "Whether a round of case-guppi gives the mechanism with a concrete example, a list one item per line, a quotation in the Context as a blockquote, a number only beside a quotation of what it points to, and an unknown term explained"}`
>   - change: `the Criterion replaced whole — a quotation in the Context stands as the grill-me template sets it (case 524.2)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-a-plain-round` — in a later session after the render: one first round that quotes a page and one later round of `case-guppi` read in the chat against the Criterion

> **ratification:**
> ```
> - decision[case 524.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 524.2][update][estimate-case-build-writes-a-plain-round]{ref:rule-case-build}
> ```

### Case 524.3 — The main agent shows a round with each quotation in its blockquote

> **given:**
> `rule-case-protocol` — the rule; its Render is the case schema, which sets how the main agent shows a round
> **＋** `vault/wiki/case-schema.md` — the file rendered from it, read by the main agent
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise on the showing; its Criterion is replaced whole
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill whose template sets the shape of a question and a quotation
> **＋** `.claude/skills/wait-what/SKILL.md` — the skill by which the main agent answers a request for a plain explanation
> **＋** `rule-case-check` — the rule whose hook writes the Case file the main agent sends
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the Case file the main agent sends at a showing

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, then its own text after one horizontal rule.
> **＋** A reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `line by line, slugs, paths and quotations unchanged — the`
>   - new: `line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the`
>   - change: `the main agent shows a round with each quotation in its blockquote (case 524.3)`
> - [ ] update `estimate-case-protocol-shows-the-built-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a round shown with each quotation in its blockquote (case 524.3)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-shows-the-built-case` — in a later session after the render: one round of `case-guppi` that quotes a page, read in the chat against the answer and the Criterion

> **ratification:**
> ```
> - decision[case 524.3][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 524.3][update][estimate-case-protocol-shows-the-built-case]{ref:rule-case-protocol}
> ```
