## Case 477 — A plain round, the skill wait-what, and a request for a plain explanation that is no failure

> **context:**
> `estimate-agent-writing-followed` is `failed`. In session 0000 the person asked three times for a plain explanation of a round of `case-guppi`: once on Case 472 and twice on Case 473. The same happened twice on Case 467 and once on Case 476. Case 466.1 had already added a `**Context:**` paragraph to the first round, and the requests went on. The round of 473 was dense because it packed frame facts into the Context and the question bodies: case numbers, slug histories and words like "stamped writer". The main agent's own explanation, which the person understood, was different. It gave the problem in two points and one concrete example ("the hook refused 13 ledger lines, and they were lost"), and it said what each option changes. On 476 a before/after example answered the request. Today no text says who answers such a request. `rule-case-protocol` sends "a question or a change of the person on a shown Case" to `case-guppi`, but the main agent answered the requests itself. The Result of `estimate-case-protocol-shows-the-built-case` records this.
> The person decided in two rounds. A round gets a sentence in `rule-case-build`: the mechanism with an example, a before and after for each option, case numbers only in the `➡️` line, and an unknown term explained. A new Estimate reads that sentence against the text of a round. A request for a plain explanation becomes a legal skill, `wait-what`, taken from github.com/mattpocock/skills with its name kept. The person or the main agent starts it. Such a request is then its normal use, not a complaint, because requests like it can come without end. The main agent explains, and it asks the `case-guppi` of the Case only for a fact of the Case.
> The vault's answer: no page or skill named `wait-what` or `explain` exists in `vault/wiki/`, `vault/archive/` or `.claude/skills/`. Every `create` carries a `ref`. `rule-skill-grill-me` is the pattern for the page of a skill.
> The frame. The sentence of `rule-case-protocol` on a question on a shown Case, and the line of the Criterion of `estimate-case-protocol-shows-the-built-case` that repeats it, would become false for a request for a plain explanation, so 477.3 changes both. `rule-case-build` tells `case-guppi` to answer every message with the Case or a round. A message of the main agent that asks for a fact would break that sentence, so 477.3 adds the answer to such a message. That answer opens with the line `**Fact:**`. Without the mark the main agent would show it as a round, because `rule-case-protocol` reads every answer with no Case heading as a round. So the sentence on a round and the line of the Criterion that repeats it except an answer with this mark. In that Criterion the `when` and three lines are changed on purpose, so the old wording of each is not carried: the line on the answers now excepts a request for a plain explanation, the line on a round now excepts an answer under `**Fact:**`, and the line on the request is new. Every other line is carried unchanged, "Russian" included, since Estimates keep this project's values (Case 476).
> The hook of `rule-case-check` needs no new line. Its How it works already takes as the answer the newest output of `case-guppi` that holds a Case heading. After a built Case, a fact answer makes the hook check and store that Case again and write its file with the same text. Before any Case, it is neither checked nor stored.
> Two Estimates stay untouched. The Criterion of `estimate-case-build-writes-the-case` states the form of a round and the messages that carry the person's words. The round sentence adds to that form, and the fact request is a message of the main agent outside its `when`, so no line of it becomes false. The person chose a separate promise for plainness. `estimate-skill-grill-me-asks-in-rounds` says the form of a round of `case-guppi` "is the promise of `estimate-case-build-writes-the-case`". Once 477.1 puts plainness into `estimate-case-build-writes-a-plain-round`, that line no longer names every promise on a round, but it is still true. It is not updated, because that Estimate is to be read in Work Mode of this session, and an update would push its reading to a later session (case 428.1).
> The Render of `rule-agent-writing` does not change. Case 476.2 of this session changes three phrases of the Render of `rule-case-build` and one phrase in `## Who builds a Case` of `rule-case-protocol` ("which the agent shows translated into Russian line by line"). The anchors of this Case are other text. The Render of `rule-skill-wait-what` holds `{{chat_lang}}`: the render puts in the name of the language that the `## Render` of `rule-guppi-config` (476.1) sets, and both land at the same librarian's run. No reader in code changes.
> Not done: no check counts the requests or reads a round by script. The Case file and the pages get no new sentence on plainness, because no request fell on them. The Render of `rule-agent-writing` stays as it is.

> **problem:**
> The rounds of `case-guppi` carry frame facts where the person needs the mechanism and the effect of each option, so the person asks for a plain explanation again and again. Each request fails `estimate-agent-writing-followed`, and no text says who answers the request or in what form.

> **recommend:**
> Four sub-cases, one promise each. 477.1 adds the round sentence to `rule-case-build` and creates `estimate-case-build-writes-a-plain-round`, which reads the text of a round. 477.2 creates the skill `wait-what`, with its page `rule-skill-wait-what` and an Estimate. 477.3 lets the main agent answer a request for a plain explanation by the skill, and ask `case-guppi` only for a fact, which comes back under a `**Fact:**` line. It changes `rule-case-protocol`, `rule-case-build` and the Criterion of `estimate-case-protocol-shows-the-built-case`. 477.4 replaces the Criterion of `estimate-agent-writing-followed` so that such a request is no complaint. The rejected option was to count each request as a failure of a new Estimate: that test would fail again at every hard topic and never close.

### Case 477.1 — A round of case-guppi written in plain words

> **given:**
> `rule-case-build` — its Render, the paragraph on a round and its Context
> **＋** `.claude/agents/case-guppi.md` — the agent rendered from `rule-case-build`
> **＋** `estimate-case-build-writes-a-plain-round` — the new promise
> **＋** `estimate-case-build-writes-the-case` — the form of a round, which stands

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
> **＋** Each question body says what each option changes, as a before and after.
> **＋** Case numbers, the history of a slug and facts of the frame stand in the round only in the `➡️` line of a question, as the source of its recommendation.
> **＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
> **－** The `context` of a Case keeps its case numbers and frame facts: the sentence is about a round only.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `a part with nothing to say left out. A later round on the item`
>   - new: `` a part with nothing to say left out. Write the round for a person who has not opened the pages: the context gives the mechanism in plain words with one concrete example of where it goes wrong; each question body says what each option changes, as a before and after; case numbers, the history of a slug and facts of the frame stay out of the context and the question bodies, and stand in the `➡️` line as the source of the recommendation, and in the `context` of the Case; a term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it (case 477.1). A later round on the item ``
>   - change: `a round of case-guppi gives the mechanism with a concrete example, a before and after for each option, case numbers only in the recommended answer, and an unknown term explained (case 477.1)`
> - [ ] create `estimate-case-build-writes-a-plain-round`
>   - type: `estimate`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether a round of case-guppi gives the mechanism with a concrete example, a before and after for each option, case numbers only in the recommended answer, and an unknown term explained`
>   - method: `by hand, in a session after the render: one round of case-guppi read in the chat against the four parts of the Criterion`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-a-plain-round`

> **ratification:**
> ```
> - decision[case 477.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 477.1][create][estimate-case-build-writes-a-plain-round]{ref:rule-case-build}{tags:session,workflow,harness}
> ```

### Case 477.2 — The skill wait-what writes the last text again in plain words

> **given:**
> `rule-skill-wait-what` — the new Rule; its Render is the skill
> **＋** `.claude/skills/wait-what/SKILL.md` — the skill, rendered in full from `rule-skill-wait-what`
> **＋** `estimate-skill-wait-what-re-pitches` — the new promise
> **＋** `rule-plan-mode` — the parent of the skills of Plan Mode
> **＋** `vault/wiki/glossary.md` — the terms of the vault
> **＋** `rule-guppi-config` — the code of `chat_lang` that the render puts in (case 476.1)
> **＋** `.claude/agents/case-guppi.md` — the agent that holds the facts of its Case

> **when:**
> The person types `/wait-what` on `UserPromptSubmit`, or the main agent calls the skill on `PreToolUse Skill` when the person asks in words for a plain explanation of its last text, after `uv run guppi render` wrote `.claude/skills/wait-what/SKILL.md` from `rule-skill-wait-what`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/wait-what/SKILL.md` equals the Render of `rule-skill-wait-what`, with the name of the language that the `## Render` of `rule-guppi-config` sets for `chat_lang` in place of its placeholder.
> **＋** The main agent writes its last text again — a round, the short text on a Case or a reply — in the language of `chat_lang`, in short active sentences with one idea each.
> **＋** It opens with a little background, shows how the thing works on one real case, and names the effect of every choice the text offers.
> **＋** It holds no case number and no history of a slug, uses the terms of `vault/wiki/glossary.md`, and explains a term in a few words where it first stands.
> **＋** It takes a fact of a Case that the main agent does not hold from the `case-guppi` of that Case, never from a guess.
> **＋** It ends with the open question asked again.
> **－** No option and no recommendation of the last text changes.
> **－** The skill starts no Case and writes no ledger line.

> **tasks:**
> - [ ] create `rule-skill-wait-what`
>   - type: `rule`
>   - ref: `rule-plan-mode`
>   - kind: `Leaf`
>   - purpose: `Prevents a text the person did not understand from being explained again in the same dense words, or changed while it is explained`
>   - enforcement: `render`
>   - governs: `.claude/skills/wait-what/SKILL.md`
>   - render_mode: `full`
>   - tags: `[harness, workflow]`
>   - sections.Purpose:
>     ```
>     Prevents a text the person did not understand from being explained again in the same dense words, or changed while it is explained. `/wait-what` writes the agent's last text again — a round of `case-guppi`, the short text on a Case, a reply — in the chat language, in plain words, with a concrete example and the terms of `vault/wiki/glossary.md`. It comes from the skill `wait-what` of github.com/mattpocock/skills and keeps its name. The upstream text asks for ASD-STE100 and `CONTEXT.md`: here they are short active sentences in the chat language and the glossary, since ASD-STE100 is a standard for English only. The main agent may start it too, when the person asks in words, so one text decides what a plain explanation holds. A request for it is its normal use, not a complaint about the agent's text (case 477.2).
>     ```
>   - sections.Render:
>     ```
>     <!-- rule-skill-wait-what -->
>     ---
>     name: wait-what
>     description: "Stop. That last message did not land: re-pitch it. Run it when the person types /wait-what, or asks in words for a plain explanation of the agent's last text."
>     ---
>
>     Wait, I don't understand where you've got to here. Re-pitch your last text — a round of questions, the short text on a Case, or a reply — in {{chat_lang}}.
>
>     Give a little context first. Then say the mechanism in plain words, with one concrete example of where it goes wrong. For each option, say what changes, as a before and after. Write short sentences, one idea per sentence, in the active voice.
>
>     Leave out case numbers and the history of a slug. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.
>
>     When you need a fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.
>
>     Change no option and no recommendation. End with the open question, asked again.
>     <!-- /rule-skill-wait-what -->
>     ```
> - [ ] create `estimate-skill-wait-what-re-pitches`
>   - type: `estimate`
>   - ref: `rule-skill-wait-what`
>   - kind: `QA`
>   - purpose: `Whether the skill wait-what writes the agent's last text again in plain words in the chat language, with the open question asked again and no option changed`
>   - method: `uv run guppi render --check; by hand, in a session after the render, one run of the skill read in the chat, on the person's /wait-what or on a request in words`
>   - tags: `[harness, workflow]`
> - [ ] `uv run guppi render`: `.claude/skills/wait-what/SKILL.md`
> - [ ] read `estimate-skill-wait-what-re-pitches`

> **ratification:**
> ```
> - decision[case 477.2][create][rule-skill-wait-what]{ref:rule-plan-mode}{tags:harness,workflow}
> - decision[case 477.2][create][estimate-skill-wait-what-re-pitches]{ref:rule-skill-wait-what}{tags:harness,workflow}
> ```

### Case 477.3 — The main agent answers a request for a plain explanation, case-guppi gives the facts

> **given:**
> `rule-case-protocol` and `vault/wiki/case-schema.md` — the section Who builds a Case, on what goes to `case-guppi` and what is a round
> **＋** `rule-case-build` and `.claude/agents/case-guppi.md` — the answer of `case-guppi` to a message
> **＋** `.claude/skills/grill-me/SKILL.md` and `.claude/skills/wait-what/SKILL.md` — the form of a round, and the plain explanation
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a shown Case, written by the hook of `rule-case-check`
> **＋** `.claude/agents/ask-guppi.md` — dispatched once, at pre-spec
> **＋** `estimate-case-protocol-shows-the-built-case` — its Criterion replaced whole

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no Case heading and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, then its own text after one horizontal rule.
> **＋** A reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no context of its own before the first question of a round.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `` A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`, and so do the person's answers to a round of questions, verbatim and untranslated. ``
>   - new: `` A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`, and so do the person's answers to a round of questions, verbatim and untranslated. A request for a plain explanation — of a round, of the short text on a Case or of a reply, by `/wait-what` or in the person's words — is not such a question: the main agent answers it itself by the skill `wait-what` (`rule-skill-wait-what`), and asks the `case-guppi` of the Case by `SendMessage` only for a fact of the Case it does not hold; `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading (case 477.3). ``
>   - old: `` an answer with no Case heading is a round of questions by the skill `grill-me` (`rule-case-build`), ``
>   - new: `` an answer with no Case heading and no first line `**Fact:**` is a round of questions by the skill `grill-me` (`rule-case-build`), ``
>   - change: `a request for a plain explanation is answered by the main agent with the skill wait-what; case-guppi is asked only for a fact of its Case and answers under a Fact line, which is not a round (case 477.3)`
> - [ ] update `rule-case-build`
>   - old: `Asked again by a message, answer with the Case whole again, changed as asked, or with a round when the message opens a fork.`
>   - new: `` Asked again by a message, answer with the Case whole again, changed as asked, or with a round when the message opens a fork. A message that asks you for a fact of the Case, so that the main agent can explain the Case to the person in plain words, you answer with the fact alone, in plain words, under a first line `**Fact:**`, with no Case heading and no round (case 477.3). ``
>   - change: `case-guppi answers a request of the main agent for a fact of its Case with the fact alone, under a Fact line (case 477.3)`
> - [ ] update `estimate-case-protocol-shows-the-built-case`
>   - set: `{status: pending, method: "by hand, the Cases of a session at its close, their context against the Agent calls and their showings against the SendUserFile calls of the transcript, and each request for a plain explanation against the Skill and SendMessage calls"}`
>   - change: `the Criterion replaced whole — a request for a plain explanation is answered by the main agent with the skill wait-what, and case-guppi gives only a fact, under a Fact line that is not a round (case 477.3)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-protocol-shows-the-built-case`

> **ratification:**
> ```
> - decision[case 477.3][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 477.3][update][rule-case-build]{ref:rule-case-build}
> - decision[case 477.3][update][estimate-case-protocol-shows-the-built-case]{ref:estimate-case-protocol-shows-the-built-case}
> ```

### Case 477.4 — A request for a plain explanation is no complaint about the agent's text

> **given:**
> `estimate-agent-writing-followed` — its Criterion replaced whole
> **＋** `CLAUDE.md` — the section `## How the agent writes`
> **＋** `rule-agent-writing` — its Render, which does not change
> **＋** `.claude/skills/wait-what/SKILL.md` — the skill that re-pitches a text the person did not follow

> **when:**
> A session starts with `CLAUDE.md` loaded, and the agent writes a text — a reply, a page, a commit message, a document.

> **then:**
> The person raised no complaint in the session that the agent's text broke the section `## How the agent writes` of `CLAUDE.md` — a claim with no real source or wider than the output it rests on, a sales pitch, a long or passive sentence, an answer not given first, a not-done left implied.
> **－** A slip in the agent's text that the agent found and corrected itself, with no complaint of the person, is no fault.
> **－** When the person says they did not follow and wants it said more simply, by `/wait-what` or in words, that is the normal use of `.claude/skills/wait-what/SKILL.md`, not a fault of this rule.
> **－** The code the agent writes is not a text of this rule; `make style` judges the code.

> **tasks:**
> - [ ] update `estimate-agent-writing-followed`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a request for a plain explanation, answered by the skill wait-what, is no complaint (case 477.4)`
> - [ ] read `estimate-agent-writing-followed` — by hand, in the session after the render

> **ratification:**
> ```
> - decision[case 477.4][update][estimate-agent-writing-followed]{ref:estimate-agent-writing-followed}
> ```
