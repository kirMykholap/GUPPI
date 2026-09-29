## Case 502 — /wait-what explains with a real example and points its options to the grill-me shape

> **context:**
> `/wait-what` writes the agent's last text again in plain words when the person did not follow it: a round of questions, the short text on a Case, or a reply. Today it asks for "one concrete example of where it goes wrong". It also asks the `case-guppi` of a Case for a fact the main agent does not hold. It does not say that the example must be real, or that the main agent may find the line itself. In session 2000 the re-explanation of round 2 Q1 on Case 485 showed a made-up line, "guppi cleanup prints one line per moved file", marked as made up. `estimate-skill-wait-what-re-pitches` was read `failed` (L26 of `archive/migration/2026-09-28/2000/raw/ledger.md`), and `lesson-wait-what-invents-an-example` records the cause. In this session the main agent explained Case 497 with a real ledger line, L52 of `raw/2026-09-28/2229/ledger.md`, which it found itself, and that met the aim. The skill also keeps its own "as a before and after" for options, while the question template of `grill-me` now has a fixed shape (case 501.1).
> The person chose these things. The example is a real line, quoted with its path. The main agent finds the line itself. When no real example is found, the re-explanation says so in one sentence and gives the mechanism without one. A quoted line keeps its case numbers as written. Options take the shape of the `grill-me` template. One Criterion covers all of this.
> This is the Case built again after pre-spec, with three fixes the person agreed to:
> - The shape of a question is worded once, in the `grill-me` template (501.1). The Render and the Criterion here only point to the question shape of `.claude/skills/grill-me/SKILL.md` and say where it applies. They do not repeat the `**Now:**` and `**After:**` lines. `estimate-skill-grill-me-asks-in-rounds` reads the shape.
> - The main agent translates the labels of the shape into the chat language, and a translated label counts as the label of the template.
> - `rule-case-build` has `case-guppi` answer a fact in plain words under a `**Fact:**` line, not as a quoted line. So, for a line the main agent cannot find, `case-guppi` names the file and the line, and the main agent reads the file and quotes the line itself. `rule-case-build` stays as it is. "Do not guess it" stays for every other fact of a Case.
>
> The vault's answer: both items are an `update` with a `ref`, so no vault query ran. `rule-skill-wait-what` carries `deferred_by: [[decision-case-496]]`, so its decision line carries `{supersedes:case 496}`, and the page leaves the backlog (case 429).
> What `case-guppi` found in the frame:
> - `rule-case-protocol` says the main agent asks `case-guppi` "only for a fact of the Case it does not hold". That stays true: a line the main agent read is a fact it holds. `estimate-case-protocol-shows-the-built-case` promises a `SendMessage` "only to ask for a fact of the Case", answered under a `**Fact:**` line. That also stays true, since the file and the line are such a fact. Neither page is changed.
> - `estimate-agent-writing-followed` speaks only of a request for a plain explanation being no complaint. It is not touched.
> - The skill names `.claude/skills/grill-me/SKILL.md` because it does not load that template. The shape reaches that file at the render of 501.1, so Work Mode renders `grill-me` before this skill. No code reads the skill, so no old form is kept.
> - The lesson comes from session 2000, so its fix carries no `{addresses:...}` mark (case 284.2).
> - The Estimate set `pending` is read in a later session (case 428.1).
> - Not done: no script reads a re-explanation, so an invented example is found only at a reading.
>
> Four lines of the old Criterion are not carried word for word. Each one is reworded on purpose:
> - The line on the language and the short sentences is carried into the first `＋` line, which also takes the background.
> - "shows how the thing works on one real case" becomes the real-example line. "names the effect of every choice" becomes the line that points to the question shape.
> - The line on case numbers now says "its own sentences". A `－` line lets a quoted line keep its case numbers.
> - The line on facts from `case-guppi` becomes a `－` line for every other fact. The example line says how a line is found and quoted.

> **problem:**
> The re-explanation of `/wait-what` may show an invented example when no real one is at hand. Its options have no fixed layout, while the rounds it explains now have one.

> **recommend:**
> Change the Render of `rule-skill-wait-what` in three ways:
> - The example is a real line that the main agent finds, or locates through the file and the line that `case-guppi` names, and quotes itself. When there is none, the text says so.
> - Every other fact of a Case is still asked, never guessed.
> - Options follow the question shape of the `grill-me` template, by a pointer only, with translated labels allowed.
>
> Replace the Criterion of `estimate-skill-wait-what-re-pitches` whole. The rejected option was to have `case-guppi` quote the line itself: that would change its `**Fact:**` answer, which `rule-case-build` sets.

> **given:**
> `rule-skill-wait-what` — the rule of the skill; its Render changes
> **＋** `.claude/skills/wait-what/SKILL.md` — the file rendered from it
> **＋** `estimate-skill-wait-what-re-pitches` — the promise of the skill; its Criterion replaced whole
> **＋** `.claude/skills/grill-me/SKILL.md` — the template that holds the question shape
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape
> **＋** `rule-case-build` — `case-guppi` answers a fact under a `**Fact:**` line
> **＋** `rule-guppi-config` — sets `chat_lang`, the language of the skill
> **＋** `vault/wiki/glossary.md` — the terms the skill uses

> **when:**
> The person types `/wait-what` on `UserPromptSubmit`, or the main agent calls the skill on `PreToolUse Skill` when the person asks in words for a plain explanation of its last text, after `uv run guppi render` wrote `.claude/skills/wait-what/SKILL.md` from `rule-skill-wait-what`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/wait-what/SKILL.md` equals the Render of `rule-skill-wait-what`, with the name of the language that the `## Render` of `rule-guppi-config` sets for `chat_lang` in place of its placeholder.
> **＋** The main agent writes its last text again — a round, the short text on a Case or a reply — in the language of `chat_lang`. It uses short active sentences with one idea each and opens with a little background.
> **＋** It shows the mechanism on one real example: a line of a page, a file, a ledger or the Case, which the main agent reads itself and quotes as it stands, with its path. For a line it cannot find, it asks the `case-guppi` of the Case by `SendMessage` for the file and the line, then reads the file and quotes the line.
> **＋** When it finds no real example, it says so in one sentence and gives the mechanism without one.
> **＋** Each question of a round it explains, and the options of a short text on a Case or of a reply, take the question shape of `.claude/skills/grill-me/SKILL.md`.
> **＋** Its own sentences hold no case number and no history of a slug. They use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.
> **＋** It ends with the open question asked again.
> **－** No example is made up, whether it is marked as made up or not.
> **－** A quoted line keeps its case numbers as written.
> **－** A label of the shape translated into the language of `chat_lang` counts as the label of the template.
> **－** The question shape itself is read by `estimate-skill-grill-me-asks-in-rounds`, not here.
> **－** No other fact of a Case that the main agent does not hold is guessed: it comes from the `case-guppi` of that Case.
> **－** No option and no recommendation of the last text changes.
> **－** The skill starts no Case and writes no ledger line.

> **tasks:**
> - [ ] update `rule-skill-wait-what`
>   - old:
>     ````
>     Give a little context first. Then say the mechanism in plain words, with one concrete example of where it goes wrong. For each option, say what changes, as a before and after. Write short sentences, one idea per sentence, in the active voice.
>
>     Leave out case numbers and the history of a slug. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.
>
>     When you need a fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.
>     ````
>   - new:
>     ````
>     Give a little context first. Then say the mechanism in plain words, with one real example of where it goes wrong: a line of a page, a file, a ledger or the Case, quoted as it stands, with its path. Find the line yourself where you can read or search for it. When you cannot find it, ask the `case-guppi` of the Case by `SendMessage` which file and which line hold it, then read the file and quote the line yourself. Never make up an example, not even one marked as made up. When you find no real example, say so in one sentence, and give the mechanism without one.
>
>     Lay out each question of a round, and the options in the short text on a Case or in a reply, in the question shape of `.claude/skills/grill-me/SKILL.md`. Its labels may stand in {{chat_lang}}. Write short sentences, one idea per sentence, in the active voice.
>
>     Leave the case numbers and the history of a slug out of your own sentences. A quoted line keeps its case numbers as written. Use the terms of `vault/wiki/glossary.md`, and explain a term in a few words where it first stands.
>
>     When you need any other fact of a Case that you do not hold, ask the `case-guppi` of that Case by `SendMessage`. Do not guess it.
>     ````
>   - change: `the re-pitch quotes a real line with its path, found by the main agent or located through case-guppi, never a made-up one; options follow the question shape of the grill-me template (case 502)`
> - [ ] update `estimate-skill-wait-what-re-pitches`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a real quoted example or a plain word that none was found, and options in the question shape of the grill-me template (case 502)`
> - [ ] `uv run guppi render`: `.claude/skills/wait-what/SKILL.md`
> - [ ] read `estimate-skill-wait-what-re-pitches` — `uv run guppi render --check`; by hand, one run of the skill read in the chat in a later session

> **ratification:**
> ```
> - decision[case 502][update][rule-skill-wait-what]{ref:rule-skill-wait-what}{supersedes:case 496}
> - decision[case 502][update][estimate-skill-wait-what-re-pitches]{ref:estimate-skill-wait-what-re-pitches}
> ```
