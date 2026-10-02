## Case 569 — The reply that ends Retro: one line and the ledger block, and when work.md counts as read

> **context:**
> Retro ends with one reply. That reply holds the readings and lessons of the run, and then the agent commits the session folder and calls `/handoff` in the same turn. The skill `.claude/skills/retro/SKILL.md` forbids a report, but it sets only the end of the reply, the `LEDGER` block. It does not say what may stand before that block. It also tells the agent to read `work.md`, the file in which `/work` notes the Baseline and the Expected red. It does not say whether a file the agent wrote itself in the same turn counts as read. Reading W36 of session 1237 failed `estimate-retro-runs-on-to-the-handoff` on both points. In session 4ba72976 the reply at 03:10:52 opened with five headed parts in English (What I built, Left open, Readings taken, Not taken yet, One lesson), and the `LEDGER` block came after them. The chat language is Russian. Lines 325-332 of `raw/2026-10-01/event_log.md` cover Retro, from its mark at 03:09:42 to the last Bash call before the `handoff` mark of line 333. They hold no call of the Read tool on `work.md`. The log cuts each Bash command at about 110 characters, so it cannot show on its own whether a Bash command read the file. The transcript of session 4ba72976 can show it. A Grep for `work\.md` over it printed records 8, 589, 625-627, 1030, 1047, 1084, 1089 and 1110. Of these, records 1030 and 1047 fall between the call of `/retro` and the reply. Record 1030 is the text of the skill. Record 1047 is the output of a Bash command that printed Estimate pages. So no tool call of Retro named `work.md`. The agent had written that file itself with the Write tool at 02:59:28 (event log line 259, transcript record 625). The result of that call said that the file state was current in the agent's context. The agent did not change the file after that, so the text it held was the text on disk. The glossary already names `handoff.md` as the report of Retro, and the person gets the librarian's report at the end of `/handoff`. A report in the reply therefore repeats both. The person decided three things. The reply holds one sentence in the chat language that names the commit, then the block, and nothing else. The skill's text alone holds that form, and the reading by hand checks it. While one agent does both the work and the report, the text of `work.md` that the agent wrote or changed itself in the turn counts as read. Sub-case 569.1 changes the last paragraph of the Render of `rule-retro` and replaces the Criterion of `estimate-retro-runs-on-to-the-handoff` whole. Sub-case 569.2 changes the sentence of the Render on `work.md` and replaces the Criterion of `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` whole. The first line of that Criterion says that the agent reads `work.md`, and the person's option named both Estimates that say this. The check of the answer noted the Criterion lines that the two sub-cases do not carry. Each was changed on purpose: the opening line of each Estimate gains the rule on the read, the line on the one reply gains its form, and the line on a stop gains the reply that opens with `STOP:`. The check also noted that a `then` line of 569.2 shares most of its words with one of 569.1. That is on purpose: the clause on the read stands word for word in both Criteria, so the two Estimates say the same thing about it. The two replace pairs on `rule-retro` stand in different paragraphs of the Render and do not overlap. The new sentences agree with the rest of the skill: the opening sentence against a report stays, and so does the sentence that a stop opens with `STOP:`. Not done here: the person said that once the work and the report are split between agents, reading the file becomes required. No Case takes that split up now. No hook is added. The skill is rendered at the librarian's run, and no code reads the text of this reply, so no old form is kept. The vault query was not run because no page is created. The `given` of 569.1 has more than seven lines because its `then` names each file of the session's folder, each skill of the run and the rule of the chat language. These are one behaviour, the one reply that ends Retro, and the Estimate's Criterion already named them before this Case. Searches over the frame follow. A Grep for `work\.md` over `vault/wiki/` printed 15 files: `brief.md`, `log.md`, `rule-permissions`, `estimate-permissions`, `rule-work-mode`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-retro-runs-on-to-the-handoff`, `decision-case-479.1` to `decision-case-479.5`, `rule-retro` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`. `rule-permissions`, `estimate-permissions` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` speak of writing the file. `estimate-retro-red-in-the-baseline-is-not-charged` speaks of what its Baseline holds, not of reading it, so it is left alone. The Purpose of `rule-work-mode` says that Retro reads the mark of an expected red. That stays true, because Retro takes the mark in, by a Read or by the text it wrote itself. A Grep for `no report` over the repository outside `vault/raw/`, `vault/archive/`, `vault/wiki/decisions/`, `log.md` and `brief.md` printed `.claude/skills/retro/SKILL.md`, `rule-retro` and `estimate-retro-runs-on-to-the-handoff`. Each of them stays true or is changed here. A Grep for `ends Retro|end of Retro|ending Retro` over `vault/wiki/` outside `decisions/` printed `rule-case-protocol`, `case-schema.md`, `log.md`, `rule-retro-onward`, `rule-work-mode`, `glossary.md`, `entity-glossary`, `estimate-handoff-dispatches`, `estimate-handoff-holds-each-fact-once`, `estimate-work-mode-takes-the-work-readings` and `estimate-retro-runs-on-to-the-handoff`. Each says that the lines stand in that one reply, or that the agent goes on after it, and none sets what else the reply holds. `case-schema.md` also says that a line closed at Retro shows no Frontier, which the new form keeps. A Grep for `ends Retro|end of Retro|reply that ends|Retro` over `.claude/` printed the skills `work`, `hi`, `retro` and `handoff`. The hit in `hi` speaks of closing a line at Retro, and `work` and `handoff` set no form for this reply. The hook of `rule-retro-onward` judges only the first word `STOP:`, which the new sentence does not open with. `estimate-retro-onward-sends-the-agent-to-the-handoff` therefore stands. `estimate-retro-loads` promises only that the rendered file equals the Render, so it stands too.

> **problem:**
> The skill forbids a report but sets only the end of the reply that ends Retro, so a report in English stood before the `LEDGER` block. The skill also tells the agent to read `work.md` without saying whether a file it wrote itself in the same turn counts as read. The question was what that reply may hold, what enforces it, and what reading `work.md` means.

> **recommend:**
> - **What does reading `work.md` mean when the agent wrote it in the same turn?**
>   - Recommended: (a) Retro opens `work.md` with the Read tool as its first step, always, even when the agent wrote it in this turn; the event log shows the Read.
>   - Answer: (b) what the agent already holds counts: the Read is needed only when the agent did not write or change the file in this turn. While one agent does the work and the report, this counts; once the work and the report are split between agents, reading the file becomes required.

### Case 569.1 — The reply that ends Retro holds one line and the ledger block

> **recommend:**
> - **What may stand before the ledger block in the reply that ends Retro?**
>   - Recommended: (a) one short line in Russian, then the block: one sentence in the chat language that names the commit, then the `LEDGER` block and nothing else; a headed part or a list before the block breaks the rule.
>   - Answer: (a).
> - **Does anything beyond the skill's text hold the form of that reply?**
>   - Recommended: (a) the text alone, checked by the reading: the skill states the form exactly, and the reading by hand of the Estimate catches a departure.
>   - Answer: (a).

> **given:**
> `rule-retro` — the rule of the skill `/retro`, whose Render sets the reply that ends Retro
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from that Render
> **＋** `estimate-retro-runs-on-to-the-handoff` — the promise whose Criterion this sub-case replaces
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the tasks of the run, whose boxes Retro sorts
> **＋** `raw/<date>/<hi HHMM>/work.md` — the Baseline and the Expected red that `/work` writes
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the report of Retro, which `/handoff` writes
> **＋** `.claude/skills/work/SKILL.md` — the run that calls `/retro`
> **＋** `.claude/skills/handoff/SKILL.md` — the step after the reply that ends Retro
> **＋** `vault/wiki/where-to-stop.md` — the conditions of a stop and the reply that stops
> **＋** `rule-language` — the language of the chat

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

> **then:**
> Retro asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read —, takes the readings whose moment has come, and decides which lessons to write.
> **＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
> **＋** The agent commits the work when `make style` is clean and `make test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
> **＋** One reply ends Retro: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block with every reading and lesson of `/work` and Retro; it asks the person nothing.
> **－** That reply shows the person no report: no heading, no list and no other paragraph stands before or after the block, since `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro.
> **＋** After that reply, in the same turn, the agent commits the session folder and calls `/handoff`.
> **－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`, with a reply that opens with `STOP:` and asks the person instead.
> **－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

> **tasks:**
> - [ ] update `rule-retro` — the reply that ends Retro holds one sentence that names the commit and the `LEDGER` block, nothing else
>   - old:
>     ````
>     Then end the reply with one `LEDGER` block that holds every reading and lesson of this turn, those of the Work readings of `/work` included; the reply asks the person nothing.
>     ````
>   - new:
>     ````
>     Then end the reply: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block that holds every reading and lesson of this turn, those of the Work readings of `/work` included. The reply holds nothing else — no heading, no list and no other paragraph — since `handoff.md` is the report of Retro, and it asks the person nothing (case 569.1).
>     ````
>   - change: `the reply that ends Retro holds one sentence in the language of the chat that names the commit, then the LEDGER block, and nothing else (case 569.1)`
> - [ ] update `estimate-retro-runs-on-to-the-handoff`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the reply that ends Retro holds one sentence in the language of the chat that names the commit and the LEDGER block, no heading, list or other paragraph; work.md the agent wrote or changed in the same turn counts as read (case 569.1)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-runs-on-to-the-handoff` — in a later session

> **ratification:**
> ```
> - decision[case 569.1][update][rule-retro]{ref:rule-retro}
> - decision[case 569.1][update][estimate-retro-runs-on-to-the-handoff]{ref:rule-retro}
> ```

### Case 569.2 — work.md the agent wrote in the same turn counts as read

> **given:**
> `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the promise whose Criterion this sub-case replaces
> **＋** `rule-retro` — the rule of the skill `/retro`, whose Render tells the agent to read `work.md`
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from that Render
> **＋** `.claude/skills/work/SKILL.md` — the run that writes `work.md` and its marks of an expected red
> **＋** `raw/<date>/<hi HHMM>/work.md` — the Baseline and the Expected red of the session
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the report of Retro, which holds the Observations

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

> **then:**
> The agent reads `raw/<date>/<hi HHMM>/work.md` if it stands — with the Read tool, unless the agent wrote or changed the file itself in the same turn, whose text then counts as read.
> **＋** A red or a refusal of a check on a page or file that a line of `## Expected red` of `work.md` names with that check is a line of `## Observations` of `raw/<date>/<hi HHMM>/handoff.md` that names the check and the page or file it waits for.
> **－** The red is not debt: the agent does not fix it or revert it into a patch.
> **＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
> **＋** A red or a refusal on a page or file that no line of `## Expected red` names is debt, even when another line names the same check, unless `## Baseline` of `work.md` holds its line.
> **－** In a session with no `work.md`, a red or a refusal of such a check is a line of `## Observations` by the agent's judgment.
> **－** A red test is never an expected red, even when `## Expected red` names it: it is fixed or reverted into a patch by the rule for red tests.

> **tasks:**
> - [ ] update `rule-retro` — `work.md` that the agent wrote or changed itself in the same turn counts as read
>   - old:
>     ````
>     Read `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3).
>     ````
>   - new:
>     ````
>     Read `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3): when you wrote or changed it yourself in this turn, the text you hold counts as read; otherwise open it with the Read tool (case 569.2).
>     ````
>   - change: `work.md that the agent wrote or changed itself in the same turn counts as read; otherwise Retro opens it with the Read tool (case 569.2)`
> - [ ] update `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the agent reads work.md with the Read tool unless it wrote or changed the file itself in the same turn, whose text then counts as read (case 569.2)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — in a later session

> **ratification:**
> ```
> - decision[case 569.2][update][rule-retro]{ref:rule-retro}
> - decision[case 569.2][update][estimate-retro-red-check-of-an-updated-page-is-a-handoff-note]{ref:rule-retro}
> ```
