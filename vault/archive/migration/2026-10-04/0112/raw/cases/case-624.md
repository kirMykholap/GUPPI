## Case 624 — The handoff says each thing once and lists the readings that wait in Debt alone

> **context:**
> `/handoff` writes `handoff.md`, the report of Retro, in seven sections. Its skill says that a fact stands in one section only: a Case, a box, a reading, a lesson or an observation named in one section is not named in another. `estimate-handoff-holds-each-fact-once` holds the same rule as a `－` line of its Criterion. The check failed at the `/hi` of session 1341 on the handoff of session 0317, which names Case 613.3 in four sections. Cases 618 and 621 put the check off. The handoff of session 0004 breaks the rule too. Its Direct instructions to the librarian list every reading that waits, with its moment. Its Debt names `estimate-hi-takes-a-conserved-spec` and `estimate-prespec-checks-the-frontier` again in its line of `read` slugs. Its notes name readings and lessons that What actually got done lists by line. So the failure comes from how the skill is written, not from one old session. Part of the cause is in the rules. A note on a decision must name the decision, and What actually got done lists every decision. `rule-retro` says that `handoff.md` names every Estimate whose reading cannot be taken yet, and every Estimate the session creates or updates, but it names no section for them. The skill has a Debt line only for the second group.
>
> The person chose three things. The rule now reads: one statement once. A Case, box, reading, lesson or observation may stand in a second section only with what that section's kind adds about it. The readings that wait stand in Debt alone, each with its moment, and the Direct instructions list none of them. The new Criterion is measured on a handoff that the skill wrote after its new text was rendered. This session's handoff is written before the librarian renders the skill, so it does not count. The `When` names the skill as rendered from `rule-handoff`, and the `method` names that report. Three sentences of the Render of `rule-handoff` change. The Purpose still says one section for each kind of content, and that stays true. The Criterion of `estimate-handoff-holds-each-fact-once` is replaced whole. Its `purpose` stated the old promise, and its `method` named no report, so both are set anew. The section names and their order stay. So `estimate-handoff-dispatches`, which reads "the sections that `rule-handoff` names", keeps its Criterion. The handoff of session 0004 would still fail the new Criterion where it says the same thing twice: its notes say that a reading waits for a moment, and its instructions list that reading under the same moment.
>
> `rule-retro` says that a `read` line whose slug the session creates or updates waits for a later session and is neither debt nor the librarian's. The old skill already put the slugs of those lines under `## Debt`, and this Case widens that line. To keep the two texts in line, the skill text and the Criterion now say that the lines of waiting readings stand in the section `## Debt` but are not debt. So the sentence of `rule-retro` stays true and its text does not change. `estimate-retro-loads`, on `rule-retro`, says that an Estimate this session creates or updates gets no reading in this session, and that the handoff names it as a reading of a later session. This Case keeps that: the handoff still names each such Estimate, now in `## Debt` with its moment. Its Criterion does not say in which section, so it stands, and this Case does not name it for an update.
>
> The check of this answer noted that four lines of the old Criterion are not carried. That is on purpose, and new lines replace each of them:
> - The old `When` gains the skill as rendered from `rule-handoff`.
> - The old line on the notes and the instructions gains the words that the instructions list no reading that waits.
> - The old Debt line now lists, in place of the `read` slugs, every Estimate whose reading cannot be taken yet, with its moment, and says that these lines are not debt.
> - The old `－` line on two sections becomes the rule of one statement once.
>
> Every other line is carried word for word.
>
> This Case closes the failed reading put off by Cases 618 and 621. It carries no `{supersedes:case N}`. The front matter of `estimate-handoff-holds-each-fact-once` holds no `deferred_by` field, and its History holds the two lines `deferred · [[decision-case-618]]` and `deferred · [[decision-case-621]]`. The schema asks for one block per Case in a page's `deferred_by`, and here there is none. The Case creates no page, so the vault query was not run.
>
> Frame checks:
> - A Grep of `rule-handoff|estimate-handoff-holds-each-fact-once` over the repository outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed 13 files: `glossary.md`, `entity-glossary.md`, `log.md`, `brief.md`, `insight-session-frontier-no-closer-for-an-item-ended-outside-the-plan.md`, `estimate-end-of-work-order.md`, `estimate-handoff-holds-each-fact-once.md`, `estimate-handoff-dispatches.md`, `estimate-hi-takes-a-conserved-spec.md`, `estimate-retro-runs-on-to-the-handoff.md`, `entity-sprint-migration.md`, `rule-end-of-work.md` and `rule-handoff.md`. The hits in `log.md`, `brief.md`, `entity-sprint-migration.md` and `estimate-retro-runs-on-to-the-handoff.md` stand in History or log lines and were not read. The rest name the rule as the gate of the handoff, a child of the end of work, the sections it sets, or a past result, and each stays true.
> - The moment this Case sets is the writing of `handoff.md`. A Grep of the seven section names over the repository outside `vault/raw/` and `vault/archive/` printed the skills `handoff`, `retro`, `carry` and `hi`, `librarian-guppi.md`, `guppi/spec.py`, `orchestration.md`, `brief.md`, `log.md`, the rules `rule-handoff`, `rule-retro`, `rule-brief`, `rule-carry-over`, `rule-skill-hi` and `rule-orchestration`, the Estimates `estimate-handoff-holds-each-fact-once`, `estimate-brief-written`, `estimate-carry-over-writes`, `estimate-hi-writes-frontier`, `estimate-orchestration-defers-in-one-reply`, `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` and `estimate-spec-capture-offers-the-fork`, and the Decision pages of cases 168, 468.1 and 468.2, which were not read. Only `rule-handoff` and its Estimate set what Debt and the Direct instructions hold. `rule-retro` puts a patch in Debt and sends lines to Observations, For the next session and Ask the person, and its Estimates say the same. `rule-brief` and the `librarian-guppi` frame read What actually got done, For the next session and Ask the person by name, and they read no list of waiting readings from the handoff: Readings due come from the pages and the Specs. `estimate-spec-capture-offers-the-fork` and `guppi/spec.py` match only the words "Ask the person" in another sense. No hit is made false.
> - A Grep of `later session` over `estimate-retro-loads.md` printed lines 21, 22 and 28. Lines 21 and 22 are the lines treated above, and line 28 was not read. A Grep of `debt` over the same file printed only line 48, a History line.

> **problem:**
> The `/handoff` skill forbids naming any Case, reading or lesson in two sections. A note on a decision must name it, and nothing says where the readings that wait belong. So every handoff the check has read repeats things, and `estimate-handoff-holds-each-fact-once` stays failed.

> **recommend:**
> - **What "each fact once" means**
>   - Recommended: (b) one statement once: a section may name a Case, check or lesson that another section names, when it says something new about it; saying the same thing about it twice is the failure; the skill text and the check's pass condition are both rewritten to say this.
>   - Answer: agreed with the recommendation, (b).
> - **Where the checks that wait for a later session are listed**
>   - Recommended: (a) Debt only: the Debt line is widened to every check that cannot be measured yet, each with the moment it waits for; the instructions to the librarian list no checks.
>   - Answer: agreed with the recommendation, (a).
> - **Which report the new check is measured on**
>   - Recommended: (b) the first report written from the new text: a report of a later session, written after the new skill text takes effect.
>   - Answer: agreed with the recommendation, (b).

> **given:**
> `rule-handoff` — its Render is the text of the `/handoff` skill; three sentences of it change
> **＋** `.claude/skills/handoff/SKILL.md` — the skill rendered from `rule-handoff`
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the report of Retro that the skill writes
> **＋** `estimate-handoff-holds-each-fact-once` — the check whose Criterion is replaced whole and whose `purpose` and `method` are set anew
> **＋** `rule-retro` — says that the report names every Estimate whose reading cannot be taken yet, and which boxes are debt; unchanged
> **＋** `rule-brief` — reads `## What actually got done` of the report by name; unchanged

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
> **＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
> **＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, each one this session creates or updates among them, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
> **＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
> **＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
> **－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
> **－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

> **tasks:**
> - [ ] update `rule-handoff`
>   - old: `` - `## Direct instructions to the librarian`: what to check first, what may duplicate what. ``
>   - new: `` - `## Direct instructions to the librarian`: what to check first, what may duplicate what; no reading that waits, which `## Debt` lists (case 624). ``
>   - old: `` under them two lines: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates. ``
>   - new: `` under them a line with the count of the boxes that wait for the librarian, then one line per Estimate whose reading cannot be taken yet, each one this session creates or updates among them, except one that `## Ask the person` holds: its slug and the moment its reading waits for; these lines stand in the section and are not debt (case 624). ``
>   - old: `A fact stands in one section only: a Case, a box, a reading, a lesson or an observation named in one section is not named in another (cases 468.2, 531.5).`
>   - new: `` A thing is said once: a Case, a box, a reading, a lesson or an observation that one section names stands in another section only with what that section's kind adds about it — a caveat in `## Notes from memory`, what to check first in `## Direct instructions to the librarian` — and no section says again what another section says of it (cases 468.2, 531.5, 624). ``
>   - change: `a thing is said once: a second section names it only with what its kind adds; the readings that wait stand in Debt alone, each with its moment, and are not debt (case 624)`
> - [ ] update `estimate-handoff-holds-each-fact-once`
>   - set: `{status: pending, purpose: "Whether handoff.md, the report of Retro, says each thing once in the section of its kind — a Case, box, reading, lesson or observation named again only with what the second section adds, the readings that wait listed in Debt alone and not counted as debt — with no commit, no number and no end, and keeps the three old section names", method: "one reading by hand, at the /hi of a later session, of a handoff.md written by .claude/skills/handoff/SKILL.md as rendered from rule-handoff after case 624, against the close of its Retro, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — one statement once, a second section naming a thing only with what its kind adds; the readings that wait in Debt alone, each with its moment, not debt; read on a handoff the rendered skill wrote (case 624)`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] read `estimate-handoff-holds-each-fact-once`

> **ratification:**
> ```
> - decision[case 624][update][rule-handoff]{ref:rule-handoff}
> - decision[case 624][update][estimate-handoff-holds-each-fact-once]{ref:rule-handoff}
> ```
