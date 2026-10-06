## Case 689 — /hi loads the stop rules of the run after Plan Mode

> **context:**
> A session holds only the texts it loads: `CLAUDE.md`, the skills, the agent frames and the files `/hi` imports. A fact elsewhere in the vault reaches the agent only through a read the agent must first think to make. `insight-session-vault-knowledge-not-loaded` gathers the lessons where this went wrong; each earlier child was closed on its own, by moving the fact into a loaded text or a hook, and a general list of lessons on Rule pages was rejected (case 134). The Insight is `open` again with two live children. `lesson-carry-short-brief-drops-the-work-list` is already fixed: since case 538.1 the short brief keeps the Work and Ask lists of Next session. `lesson-work-mode-a-staged-moment-promised-inside-a-run-with-no-stop` is not: at the close of Plan Mode the agent told the person to ask for a change in Work Mode, while `vault/wiki/where-to-stop.md` runs everything from the approved Spec to the librarian in one turn with no stop for the person; only `/work` and `/box` import that file, so Plan Mode did not hold it.
> The person chose that `/hi` imports `where-to-stop.md` right after `orchestration.md`, so Plan Mode holds the same list of stops as Work Mode, and the Insight is set `actioned` by this Case. The check is `estimate-internal-context-loaded`, whose Criterion lists the files `/hi` loads in order; the change makes that list incomplete, so Case 689.1 replaces it whole and sets its `purpose` anew. Its `method`, a reading by hand at a `/hi`, waits for a later session, which case 670.4 forbids; the person chose the two-part method of the other rendered skills, the new Render in the Spec read at Retro of this session, or the rendered skill file read by hand; the check of the Case file refuses a method that names a later `/hi`, so the second part reads the skill file, as the other skills' checks do. That `/hi` turns an `@` line into loaded text was read at the `/hi` of session 2049. Case 689.2 sets the Insight `actioned`; `estimate-backlog-renders` checks the effect on `backlog.md`, since its Criterion lists an Insight under `## Deferred` only while its `status` is `open`, and it stands.
> The frame. `rule-where-to-stop` says in its Purpose that `/work` and `/box` load its text; Case 689.1 adds `/hi` there. Its Estimate `estimate-where-to-stop-stops-only-on-its-conditions` speaks of the context of `/work` and `/box` and of the run after them, which stay true; it stands. `estimate-orchestration-loaded` and `estimate-ratification-loaded` promise that their file is repeated in no other file the session holds, and their `－` line names `CLAUDE.md`, `vault/wiki/case-schema.md` and the other of the two; the set of files a session holds grows by `where-to-stop.md` in Plan Mode, but those lines never named every file a session holds — the glossary, the brief and the sprint page are held and not named, and `where-to-stop.md` has stood in the context of every Work Mode since case 531.7 without being named — and the text of `where-to-stop.md` repeats no paragraph of either file: a Grep of `` Nothing else is a stop|From the approved Spec to the librarian|end the reply with the question|open that reply with `STOP:` `` over `CLAUDE.md`, `vault/wiki/orchestration.md`, `vault/wiki/ratification.md` and `vault/wiki/case-schema.md` printed nothing. Both Criteria stay true, and both stand. `guppi/recall.py` takes the paths it reads back after a compaction from the `@` lines of the skill file, never from a copy, so it needs no change. Cases 685, 686 and 688 change other sentences of the Render of `rule-orchestration`; the sentence Case 689.1 changes, the opening line that names the files loaded with `orchestration.md`, is in none of them, and the new texts do not touch. No reader refuses on the old list, so no old form is kept.
> The searches. A Grep of `rule-internal-context|estimate-internal-context-loaded` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed 11 files: `log.md`, not read; `.claude/skills/hi/SKILL.md`, which follows at the render; `rule-internal-context.md` and `estimate-internal-context-loaded.md`, which enter Case 689.1; `guppi/recall.py` and `tests/test_recall.py`, which read the skill file or a fixture of their own and stand; `rule-skill-hi.md`, whose hit is the marker of the block; `rule-claude-md.md`, which names three files that arrive with `/hi` and no full list, and stands; `estimate-hi-no-read-calls.md`, which names the files of the block without a list, and stands; `schema.yaml` and `rule-rules-schema.md`, whose hits are examples of the schema, and stand. A Grep of `` loaded by `/hi` with `` over `vault/wiki/` printed `orchestration.md` and `rule-orchestration.md`: the list of the files loaded with `orchestration.md` enters Case 689.1, and the file follows at the render. A Grep of `where-to-stop` over `vault/wiki/rules/` printed `rule-retro.md`, `rule-case-protocol.md`, `rule-work-mode.md`, `rule-where-to-stop.md`, `rule-spec-box.md`, `rule-retro-onward.md` and `rule-retro-commit.md`: the Purpose of `rule-where-to-stop` enters Case 689.1, and the others speak of the run after Plan Mode or of a task that opens with `stop:`, stay true, and stand.

> **problem:**
> The main agent in Plan Mode does not hold the stops of the run from the approved Spec to the librarian, so it can promise the person a turn inside that run that never comes.

> **recommend:**
> - **How far the Case goes**
>   - Recommended: (a) fix the open instance by importing the stop rules into `/hi`; the Insight marked as dealt with by this Case.
>   - Answer: agreed, (a).
> - **What checks that the fix works**
>   - Recommended: (a) only the loading is checked: the Criterion of `estimate-internal-context-loaded` replaced to name `where-to-stop.md`.
>   - Answer: agreed, (a).
> - **Where the stop rules stand in the `/hi` list**
>   - Recommended: (a) right after `orchestration.md`.
>   - Answer: agreed, (a).
> - **When the check of the loading is read**
>   - Recommended: (a) the two-part method of the other rendered skills: the new Render in the Spec at Retro of this session, or the context of a later `/hi`.
>   - Answer: agreed, (a).

### Case 689.1 — /hi loads where-to-stop.md after orchestration.md

> **given:**
> `rule-internal-context`: the list of the files `/hi` imports.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-internal-context-loaded`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `rule-where-to-stop`: the stops of the run after Plan Mode, rendered into `vault/wiki/where-to-stop.md`.
> **＋** `rule-orchestration`: the main agent's rules, whose opening line names the files loaded with them.
> **＋** `guppi/recall.py`: the paths read back after a compaction, taken from the skill file.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/ratification.md`, `vault/wiki/glossary.md` and `vault/wiki/case-schema.md`: the files `/hi` loads beside `where-to-stop.md`, and the schema it does not load.

> **when:**
> The person invokes `/hi`, with `.claude/skills/hi/SKILL.md` rendered from `rule-internal-context`.

> **then:**
> The text of `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/where-to-stop.md`, `vault/wiki/ratification.md` and `vault/wiki/glossary.md` is in the context of the first turn, in that order, without a read call.
> **＋** `vault/wiki/case-schema.md` is not in it.
> **＋** The glossary and the backlog reach a session through this block alone. After a compaction, the paths of these files are in the list of `guppi recall`.
> **－** A subagent, such as `librarian-guppi`, `ask-guppi` or one of Work Mode, carries none of these texts. Its prompt names what it needs.

> **tasks:**
> - [ ] update `rule-internal-context`
>   - old:
>     ```
>     @vault/wiki/orchestration.md
>     ```
>   - new:
>     ```
>     @vault/wiki/orchestration.md
>     @vault/wiki/where-to-stop.md
>     ```
>   - old: `prints the paths of these lines back (case 287).`
>   - new: `` prints the paths of these lines back (case 287). `where-to-stop.md` is listed after `orchestration.md` since case 689.1: the run from the approved Spec to the librarian stops for the person only on its conditions, and Plan Mode, which plans that run with the person, holds the same list, so the main agent promises no turn of the person inside it. ``
>   - change: `/hi loads where-to-stop.md after orchestration.md (case 689.1)`
> - [ ] update `estimate-internal-context-loaded`
>   - set:
>     ```
>     status: pending
>     purpose: The text of sprint.md, backlog.md, brief.md, orchestration.md, where-to-stop.md, ratification.md and glossary.md is present in the first turn's context after /hi, without a read call, and case-schema.md is not
>     method: by hand, the text of .claude/skills/hi/SKILL.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-internal-context in the Spec, read against the Criterion, recorded in the estimate line
>     ```
>   - change: `the Criterion replaced whole — where-to-stop.md loaded after orchestration.md; purpose and method set anew (case 689.1)`
> - [ ] update `rule-where-to-stop`
>   - old: `` `/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md` (case 591), ``
>   - new: `` `/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md` (case 591), `/hi` loads it for Plan Mode too, so the main agent promises the person no turn the run does not give (case 689.1), ``
>   - change: `/hi loads the file for Plan Mode (case 689.1)`
> - [ ] update `rule-orchestration`
>   - old: `` loaded by `/hi` with `sprint.md`, `backlog.md`, `brief.md`, `ratification.md` and `glossary.md`, ``
>   - new: `` loaded by `/hi` with `sprint.md`, `backlog.md`, `brief.md`, `where-to-stop.md`, `ratification.md` and `glossary.md`, ``
>   - change: `the opening line names where-to-stop.md among the files /hi loads (case 689.1)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-internal-context-loaded`

> **ratification:**
> ```
> - decision[case 689.1][update][rule-internal-context]{ref:rule-internal-context}
> - decision[case 689.1][update][estimate-internal-context-loaded]{ref:rule-internal-context}
> - decision[case 689.1][update][rule-where-to-stop]{ref:rule-where-to-stop}
> - decision[case 689.1][update][rule-orchestration]{ref:rule-orchestration}
> ```

### Case 689.2 — The Insight on vault knowledge not loaded closes

> **given:**
> `insight-session-vault-knowledge-not-loaded`: the Insight this Case closes.
> **＋** `rule-insights-schema`: the form of an Insight and of its `actioned` status.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which applies the update and archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/backlog.md`: the backlog, which lists each `open` Insight.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decision of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `insight-session-vault-knowledge-not-loaded` stands `actioned`, and its `addressed_by` names the Decision of this Case.
> **＋** Its `clustered` lessons become `archived` by the cascade.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.

> **tasks:**
> - [ ] update `insight-session-vault-knowledge-not-loaded`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-689.2
>     ```
>   - change: `actioned: /hi loads where-to-stop.md, so Plan Mode holds the stops of the run after it (case 689.1); the short brief keeps the Work list since case 538.1 (case 689.2)`

> **ratification:**
> ```
> - decision[case 689.2][update][insight-session-vault-knowledge-not-loaded]{ref:insight-session-vault-knowledge-not-loaded}
> ```
