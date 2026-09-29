## Case 511 — The options and the lists of a round stand on their own lines

> **context:**
> A round of questions from `case-guppi`, and the person's own `/grill-me`, follows the question template of the skill `grill-me`. Today the options come right after the `**Now:**` text as ordinary bullet items `- **(a) name**`, and no word introduces them. A list inside the Now text uses the same bullet, so the options blend into the text above them. Enumerations are also written inside a sentence. For example, "the hook checks (1) the heading, (2) the ledger lines and (3) the fence" runs as one line where three lines would read better.
> The person asked for three changes. Every list, numbered or not, starts on a new line. A word stands before the options to say that a list of choices follows. The options carry their own mark, so they look different from any other list. In the round the person settled the details: the label `**Options:**`, the mark `🔹` in place of the bullet, what counts as a list, and a list allowed inside an `**After:**` item and under the `➡️` line. The person saw an example question in the new form and accepted it. The person also asked for the same list rule in the `**Context:**` paragraph that opens a first round of `case-guppi`. That was sub-case 511.2, which Case 512 of this session superseded and which now carries the change, so 511.2 has left the Spec and Case 511 keeps only 511.1.
> The Render of `rule-skill-grill-me` holds the template. No code reads the shape of a round: a search of the `.py` files for the round's labels and marks finds nothing, so no reader has to accept an old form beside the new one. The Case creates no page, so no vault query was needed.
> From the frame: the Criterion of `estimate-skill-grill-me-asks-in-rounds` describes the option shape, so it is replaced whole, and the old option line and its wording are dropped on purpose. The lines of `rule-case-protocol`, and `estimate-case-protocol-shows-the-built-case`, say that the main agent shows each question closing with its `➡️` line and translates the recommended answer in place. They stand: a list under `➡️` is part of the recommended answer, and the showing translates it line by line. The rule "an option has nothing else under it" stands, because a list inside an `**After:**` item is part of that item. The Render of `rule-skill-wait-what` and the Criterion of `estimate-skill-wait-what-re-pitches` both say that options take "the question shape of `.claude/skills/grill-me/SKILL.md`". They point to the template and do not repeat its shape, so they stay true and pick up the new shape as they stand. The shape itself is read by `estimate-skill-grill-me-asks-in-rounds`, as that Criterion says.

> **problem:**
> The template does not introduce the options, gives them the same bullet as any other list, and has no rule against enumerations written inside a sentence. A round is harder to scan than it needs to be.

> **recommend:**
> Change the template and its explanation in `rule-skill-grill-me`. A label `**Options:**` stands on its own line before the options. Each option line starts with `🔹` after a blank line, and its `**After:**` is a bullet under it. A new paragraph says what counts as a list and where it stands. Replace the Criterion of `estimate-skill-grill-me-asks-in-rounds` whole. The person rejected the other choice, a `🔹` inside a bullet item, because every option line would show two marks and would still look like a list.

### Case 511.1 — The grill-me template introduces the options with a label, marks them with 🔹 and puts every list on its own lines

> **given:**
> `rule-skill-grill-me` — the rule page whose Render holds the question template.
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill rendered from it.
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by `skills: [grill-me]`.
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise on the shape of a question.
> **＋** `rule-case-protocol` — the rule on how the main agent shows a round, translated line by line.

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** Each question opens with its numbered `❓ **Qn** - **<title>**:` line and closes with its `➡️` line, the recommended answer, together with the lines of a list under it. Its body starts on the next line with one `**Now:**` line that says once what holds today, or that nothing exists yet.
> **＋** The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark `🔹` and its name in bold. Under it stands one nested `**After:**` item that says what holds with that option.
> **＋** A list stands one item per line, never inside a sentence. This covers items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things. Under an `**After:**` item a list stands nested inside that item.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** An option carries nothing under it but its `**After:**` item: no list of costs, no second item and no other label. A cost is a plain sentence inside the `**After:**` text or in the `➡️` line.
> **－** A short series of words inside a sentence stays in the sentence.
> **－** No line of a question except an option starts with `🔹`.
> **－** In the chat the labels may stand translated, as the main agent shows a round of `case-guppi` by `rule-case-protocol`. A translated label counts as the same label: the shape is what is read, not the language of the labels.
> **－** The `**Context:**` paragraph of a round of `case-guppi`, its lists included, and the place of its case numbers are not read here. They are the promises of the Estimates of the rule of `.claude/agents/case-guppi.md`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

> **tasks:**
> - [ ] update `rule-skill-grill-me`
>   - old:
>     ```
>         - **(a) <option name>**
>           - **After:** <what holds with this option>
>         - **(b) <option name>**
>           - **After:** <what holds with this option>
>     ```
>   - new:
>     ```
>         **Options:**
>
>         🔹 **(a) <option name>**
>           - **After:** <what holds with this option>
>
>         🔹 **(b) <option name>**
>           - **After:** <what holds with this option>
>     ```
>   - old:
>     ```
>     Each option starts on its own line as a list item with its name in bold, and under it stands one nested `**After:**` item: what holds with this option.
>     ```
>   - new:
>     ```
>     The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark 🔹 and its name in bold, and under it stands one nested `**After:**` item: what holds with this option. No other line of a question starts with 🔹.
>     ```
>   - old:
>     ```
>     In the language of the chat the labels may stand translated; the shape stays.
>     ```
>   - new:
>     ```
>     In the language of the chat the labels may stand translated; the shape stays.
>
>     A list starts on a new line and never runs inside a sentence. Items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things, stand one per line; a short series of words inside a sentence stays in it. In the `**Now:**` text a list stands under the sentence that introduces it. Under an `**After:**` item it stands nested one level deeper, inside that item. In the recommended answer it stands on the lines under `➡️`, which close the question.
>     ```
>   - change: `the options of a question stand under an Options label, each marked with 🔹; every list stands one item per line (case 511.1)`
> - [ ] update `estimate-skill-grill-me-asks-in-rounds`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Options label, the 🔹 mark and a list one item per line (case 511.1)`
> - [ ] `uv run guppi render`: `.claude/skills/grill-me/SKILL.md`
> - [ ] read `estimate-skill-grill-me-asks-in-rounds` — in a later session after the render: one round of `case-guppi` or of the person's `/grill-me`, read in the chat

> **ratification:**
> ```
> - decision[case 511.1][update][rule-skill-grill-me]{ref:rule-skill-grill-me}
> - decision[case 511.1][update][estimate-skill-grill-me-asks-in-rounds]{ref:rule-skill-grill-me}
> ```
