## Case 501 — Each question in a round takes one fixed shape, set in the grill-me template

> **context:**
> When a choice is still open, `case-guppi` answers with a round of numbered questions. It builds the round on the template of the skill `grill-me`, which it loads through its `skills` field. The person's own `/grill-me` interviews use the same template. The template gives a question a title, a free body "including multiple choices", and a recommended answer. The instructions of `case-guppi` add one loose sentence: each question body tells what each option changes, "as a before and after". No script reads a round. In the rounds of session 2000, Case 482 Q2 and Q4 gave no before, and Case 483 Q3 and Q4 gave only "After:". `estimate-case-build-writes-a-plain-round` was read `failed` (L25 of `archive/migration/2026-09-28/2000/raw/ledger.md`). The rounds of this session came in mixed shapes. One of them put a list of costs under an option, a second label in all but name. Case 495 put the item off.
> The person chose these things. The shape goes into the template of `grill-me`, so that `/grill-me` and `case-guppi` share one template. A question states today once, on a `**Now:**` line. Every question takes the shape, and a question on something new says "nothing exists yet". Each option starts on its own line as a bold list item, with one nested `**After:**` item under it and nothing else. There is no list of costs, no second item and no other label. A cost is a plain sentence inside the `After:` text or in the reasoning after the arrow. At pre-spec the person added two things. The shape is worded once, in the template, and the instructions of `case-guppi` only point to it. The language of the labels does not matter: in the chat the labels stand translated and count as the same labels, because the shape is what is read.
> The vault's answer: every item is an `update` with a `ref`, so no vault query ran. `rule-case-build` carries `deferred_by: [[decision-case-495]]`, so its decision line in 501.2 carries `{supersedes:case 495}`, and the page leaves the backlog. What `case-guppi` found in the frame:
> - The question line keeps its colon, `❓ **Qn** - **<title>**:`, because `rule-case-protocol` describes how the main agent shows a round by that line. The body starts on the next line.
> - The shape is worded once as text, in the template of 501.1, and signed once as a promise, in `estimate-skill-grill-me-asks-in-rounds`, whose `when` already covers both `/grill-me` and a round of `case-guppi`. The new text of `rule-case-build` and `estimate-case-build-writes-a-plain-round` only point to it.
> - `estimate-case-protocol-shows-the-built-case` promises that the main agent translates a round line by line, each question "its title, body and recommended answer translated in place, nothing merged, dropped or added". It stays true and is not touched. A label translated in place keeps its line and its list item, so the shape reaches the chat whole. The `－` line of 501.1 says that a translated label counts as the same label.
> - The criterion of `estimate-case-build-writes-the-case` still holds true: a round is still "in the form of" the template.
> - `rule-skill-wait-what` keeps its own sentence, "as a before and after", for a re-explained round. Pointing it to the template is item C3 and is not done here.
> - Not done: the hook of `rule-case-check` still reads no round, so a question off the shape is found only at a reading.
> - The two Estimates set `pending` are read in a later session (case 428.1).
>
> The answer check noted that three lines of the old Criteria are not carried. Each is dropped on purpose:
> - "On the person's `/grill-me`, each question is numbered, with a title, a body and a recommended answer" in `estimate-skill-grill-me-asks-in-rounds` becomes the two shape lines. The shape covers `/grill-me` and `case-guppi` alike.
> - "The form of a round of `case-guppi` is not read here" in the same Estimate is no longer true: the shape of that form now lives in the template. It becomes a `－` line that leaves only the Context paragraph and the case numbers to the Estimates of `rule-case-build`.
> - "Each question body says what each option changes, as a before and after." in `estimate-case-build-writes-a-plain-round` moves to `estimate-skill-grill-me-asks-in-rounds`. There it is worded as the shape, so the same promise is not signed twice in two wordings.

> **problem:**
> A round of questions often does not say, for each option, what holds today and what holds after it, and its options run together in solid text. The template gives no shape, and the one sentence in the instructions of `case-guppi` is loose, so the before part gets dropped or merged and extra labels creep in.

> **recommend:**
> Put one question shape into the `grill-me` template, 501.1: a `**Now:**` line once, then each option on its own line, and one `**After:**` item under it and nothing else. `/grill-me` and `case-guppi` then share one text. The instructions of `case-guppi` point to that shape without restating it, and its plain-round promise keeps only what is its own, 501.2. The rejected option was to keep the shape in the instructions of `case-guppi` alone. The template it builds on would then say something looser, and the person's interviews would look different.

### Case 501.1 — The grill-me template gives every question one shape

> **given:**
> `rule-skill-grill-me` — the rule of the skill; its Render gains the shape of a question
> **＋** `.claude/skills/grill-me/SKILL.md` — the file rendered from it
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise of the skill; its Criterion replaced whole
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by `skills: [grill-me]`
> **＋** `rule-case-protocol` — the showing of a round by its question line, translated in place, which the shape keeps
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of how the main agent translates and shows a round
> **＋** `estimate-case-build-writes-the-case` — the promise of the Context paragraph of a round of `case-guppi`
> **＋** `estimate-case-build-writes-a-plain-round` — the promise of the plain words of a round of `case-guppi`

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
> **＋** Each option starts on its own line as a list item with its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
> **－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `estimate-case-protocol-shows-the-built-case`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
> **－** The Context paragraph of a round of `case-guppi` and the place of its case numbers are not read here. They are the promises of `estimate-case-build-writes-the-case` and `estimate-case-build-writes-a-plain-round`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

> **tasks:**
> - [ ] update `rule-skill-grill-me`
>   - old:
>     ````
>     Each question should be formatted like so:
>
>         ❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>
>
>         ➡️ <your recommended answer>
>     ````
>   - new:
>     ````
>     Each question should be formatted like so:
>
>         ❓ **Q1** - **<question title>**:
>
>         **Now:** <what holds today, said once for the question; "nothing exists yet" when nothing does>
>
>         - **(a) <option name>**
>           - **After:** <what holds with this option>
>         - **(b) <option name>**
>           - **After:** <what holds with this option>
>
>         ➡️ <your recommended answer, and why>
>
>     The body of a question starts on the line after its title. The `**Now:**` line says once what holds today. Each option starts on its own line as a list item with its name in bold, and under it stands one nested `**After:**` item: what holds with this option. An option has nothing else under it: no list of costs, no second item, no other label. A cost, when it matters, is a plain sentence inside the `**After:**` text or in the reasoning after `➡️`. Every question takes this shape, one on a new idea with nothing behind it too. In the language of the chat the labels may stand translated; the shape stays.
>     ````
>   - change: `every question of a round takes one shape: a Now line once, each option on its own line with one After item under it and nothing else (case 501.1)`
> - [ ] update `estimate-skill-grill-me-asks-in-rounds`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — every question of /grill-me and of case-guppi takes the Now and After shape, an option with nothing else under it, a translated label the same label (case 501.1)`
> - [ ] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
> - [ ] read `estimate-skill-grill-me-asks-in-rounds` — `uv run guppi render --check`; by hand, one round read in the chat in a later session

> **ratification:**
> ```
> - decision[case 501.1][update][rule-skill-grill-me]{ref:rule-skill-grill-me}
> - decision[case 501.1][update][estimate-skill-grill-me-asks-in-rounds]{ref:estimate-skill-grill-me-asks-in-rounds}
> ```

### Case 501.2 — case-guppi points to the question shape of the template

> **given:**
> `rule-case-build` — the rule of `case-guppi`; its Render points to the question shape of the template
> **＋** `.claude/agents/case-guppi.md` — the file rendered from it
> **＋** `estimate-case-build-writes-a-plain-round` — the promise of a plain round; its Criterion replaced whole
> **＋** `.claude/skills/grill-me/SKILL.md` — the template that holds the shape
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape

> **when:**
> `case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
> **＋** The instructions of `case-guppi` point each question to the question shape of `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
> **＋** Case numbers, the history of a slug and facts of the frame stand in the round only in the `➡️` line of a question, as the source of its recommendation.
> **＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
> **－** The shape of a question is read by `estimate-skill-grill-me-asks-in-rounds`, not here.
> **－** The `context` of a Case keeps its case numbers and frame facts: the sentence is about a round only.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `each question body says what each option changes, as a before and after;`
>   - new: `each question takes the question shape of the grill-me template;`
>   - change: `each question of a round of case-guppi takes the question shape of the grill-me template, not restated (case 501.2)`
> - [ ] update `estimate-case-build-writes-a-plain-round`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the instructions point to the question shape of the grill-me template, read by estimate-skill-grill-me-asks-in-rounds; this promise keeps the Context, the case numbers and the terms (case 501.2)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-a-plain-round` — by hand, one round of case-guppi read in the chat against the Criterion, in a later session

> **ratification:**
> ```
> - decision[case 501.2][update][rule-case-build]{ref:rule-case-build}{supersedes:case 495}
> - decision[case 501.2][update][estimate-case-build-writes-a-plain-round]{ref:estimate-case-build-writes-a-plain-round}
> ```
