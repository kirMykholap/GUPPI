## Case 716 — The checks of `case-guppi` are read at the Retro of the session that changes them

> **context:**
> The person asked whether any change to a rule or an entity sets every Estimate of it `pending`, even an Estimate nobody touched. The scripts do not do that. `lift_criterion` of `guppi/materialize.py` sets `pending` only on an `update` of an Estimate that a Case names and whose Criterion it writes; an `update` of a rule touches no Estimate (case 378.5). Three rules make an Estimate hang. A Case names each Estimate whose Criterion speaks of its change, and `/pre-spec` reports one it missed. A Criterion changes only whole (case 378.4). Retro reads each Estimate its session updates, or sets it `failed` (`rule-retro`, case 670.2). While an Estimate is not `passed`, the cascade of `guppi/generate.py` keeps its target `draft`, and `make lint` gives an `unread` finding for it. `estimate-case-build-writes-the-case` shows the cost. Its Criterion holds almost every behaviour of `case-guppi`, so almost every Case on that agent names it. Case 698 changed one line of it, and its History says "the other lines stand". The `method` waits for live dispatches after the render, and for rare kinds of dispatch. So the Retro of each such session could not read it and wrote it `failed`, after cases 698, 701.3 and 705.1. `estimate-case-build-checks-the-finished-case` hangs the same way: its `method` waits for a `/pre-spec` after the render. The brief carries both, as C7 and C8 of this session.
>
> The person chose to change the `method` of these two Estimates only, and not to split them. Each sub-case updates one of the two pages, which are two promises. Their `then` lines share most of their words because both pages take the same form of reading, as the person chose for both. The check of the file notes this overlap, and it stands. A rule that lets unchanged lines keep their last reading was not chosen. The new `method` follows the form of `estimate-retro-loads`. The reading is the Render of `rule-case-build`, read against the Criterion: the new text in the Spec when a Case of the session changes it, and `.claude/agents/case-guppi.md` otherwise. The Render paragraph of `rule-retro` and the Criterion of `estimate-retro-loads` already set that reading of a changed Render. `estimate-case-build-writes-the-case` keeps the tokens and seconds of each dispatch of the session. So the sentence of the Purpose of `rule-case-build` that gives the cost question to the `method` of its Estimate stays true. `estimate-case-build-checks-the-finished-case` keeps its count of the findings of `ask-guppi` at the session's own `/pre-spec`, which runs before Retro, in the same way as the cost line. That `method` no longer waits for another session. Its `purpose` still says that the check is counted by what `ask-guppi` finds at pre-spec, which stays true, so it stands. The person chose that each Criterion is written back word for word and that each page goes back to `pending`. The Retro of this session then reads both on the new `method`, and that reading is the check of this Case. This Case does not change the behaviour of `case-guppi`, so no Criterion changes and no other Estimate of `rule-case-build` is touched. The new `method` names no later session, no session after another, no librarian and no `/hi`. So neither the check of a `method` the plan writes nor the check that Case 715 adds reports it. Case 717.2 of this session changes the Render of `rule-case-build`. It adds `cacheTtl: "1h"` under `experimental` to the frontmatter of the agent, and says what the agent reads whole and what in parts. So the Retro reading that this Case sets reads the new text of the Render in the Spec, as Case 717.2 leaves it. That text keeps each line of both Criteria true. The agent still reads `case-schema.md` and `ratification.md` whole and reads each page and file the `given` names, and its model, effort, tools and mode stand. It reads whole the case file of each Case of the session that the prompt of its call names, or that the check of its file names in a finding or a note. It reads in parts only the case file of a Case of an earlier session. The context of Case 717 judges the same and names Case 716.1. No other Case of this session changes `rule-case-build` or these two pages.
>
> A Grep for `estimate-case-build-(writes-the-case|checks-the-finished-case)` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `guppi/casecheck.py`, `vault/wiki/brief.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/estimates/estimate-case-check-sends-back-a-faulty-case.md`, `vault/wiki/estimates/estimate-materialize-assembles.md` and `vault/wiki/estimates/estimate-skill-grill-me-asks-in-rounds.md`. I did not read `brief.md` or `log.md`. The hit in `estimate-skill-grill-me-asks-in-rounds` is a History line. The hit in `estimate-materialize-assembles` is a Result, the record of a past reading. The hit in `rule-case-build` is its `estimates` list. All three stand. `guppi/casecheck.py` and the Criterion of `estimate-case-check-sends-back-a-faulty-case` keep an old path of the hook until a reading of `estimate-case-build-writes-the-case` passes live, and a Case of a later session removes that path. The new `method` gives no live reading, so that condition will no longer come by itself, and the old path stays until a Case removes it. The sentence stays true, and both Case 716.1 and `estimate-case-check-sends-back-a-faulty-case` leave it as it stands. Its Criterion speaks of a reading of the Estimate that 716.1 changes, so 716.1 names it in `given`, unchanged. Not done: the removal of that old path, a split of the large Criterion, and a rule that keeps the reading of an unchanged line for every Estimate.

> **problem:**
> The two Estimates of `case-guppi` stand `failed` after every Case that changes them. Their `method` waits for dispatches or a `/pre-spec` after the render, which come only in a later session, and partly for kinds of dispatch that seldom happen.

> **recommend:**
> - **How wide should the fix be?**
>   - Recommended: (a) fix this check's method only: Retro reads the new text of the agent's instructions against the promise, in the session that changes it.
>   - Answer: agreed, (a).
> - **Does the fix also cover the second hanging check of `case-guppi`?**
>   - Recommended: (a) yes, one Case fixes both checks.
>   - Answer: agreed, (a).
> - **How does the check leave `failed` now?**
>   - Recommended: (a) set it back to `pending` with its promise unchanged, and this session's Retro reads it.
>   - Answer: agreed, (a).
> - **Does the check still record the tokens and seconds of each call?**
>   - Recommended: (a) keep it: the reading line also gives the tokens and seconds of this session's calls, when there were any.
>   - Answer: agreed, (a).

### Case 716.1 — `estimate-case-build-writes-the-case` is read at the Retro of the session that changes it

> **given:**
> `estimate-case-build-writes-the-case`: its `method` is set anew, its Criterion written back unchanged.
> **＋** `rule-case-build`: the rule whose Render is the agent file of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `rule-retro`: Retro reads each Estimate its session updates, and the new Render in the Spec.
> **＋** `raw/2026-10-07/1804/cases/case-717.md`: Case 717.2 changes the Render of `rule-case-build` that the reading reads.
> **＋** `estimate-case-check-sends-back-a-faulty-case`: its Criterion keeps an old path until a live reading of `estimate-case-build-writes-the-case`; unchanged.
> **＋** `guppi/casecheck.py`: the hook that keeps that old path; unchanged.

> **when:**
> The Retro of a session whose Spec updates `estimate-case-build-writes-the-case` takes its reading by its `method`.

> **then:**
> The reading reads the Render of `rule-case-build` against the Criterion: its new text in the Spec when a Case of that session changes it, and `.claude/agents/case-guppi.md` otherwise.
> **＋** The estimate line gives the tokens and seconds of each dispatch of `case-guppi` in that session, when there was one.
> **－** The reading waits for no dispatch of `case-guppi` after the render of `rule-case-build`, and for no kind of dispatch that the session did not hold.

> **tasks:**
> - [ ] update `estimate-case-build-writes-the-case`
>   - set:
>     ```
>     status: pending
>     method: "by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the tokens and seconds of each dispatch of case-guppi in that session, when there was one, in the estimate line"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
>     **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
>     **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, or the drop of a change to that Case.
>
>     Then:
>     `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
>     **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
>     **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
>     **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
>     **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
>     **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
>     **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
>     **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
>     **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
>     **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
>     **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
>     **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way.
>     **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
>     **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
>     **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
>     **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
>     **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
>     **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case included, and no ledger line.
>     **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.
>     ```
>   - change: `the method reads the Render of rule-case-build against the Criterion at the Retro of the session that changes it, with the tokens and seconds of that session's dispatches; the Criterion written back unchanged; pending again (case 716)`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 716.1][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> ```

### Case 716.2 — `estimate-case-build-checks-the-finished-case` is read at the Retro of the session that changes it

> **given:**
> `estimate-case-build-checks-the-finished-case`: its `method` is set anew, its Criterion written back unchanged.
> **＋** `rule-case-build`: the rule whose Render is the agent file of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `.claude/agents/ask-guppi.md`: the agent whose findings at `/pre-spec` the estimate line counts.
> **＋** `rule-retro`: Retro reads each Estimate its session updates, and the new Render in the Spec.
> **＋** `raw/2026-10-07/1804/cases/case-717.md`: Case 717.2 changes the Render of `rule-case-build` that the reading reads.

> **when:**
> The Retro of a session whose Spec updates `estimate-case-build-checks-the-finished-case` takes its reading by its `method`.

> **then:**
> The reading reads the Render of `rule-case-build` against the Criterion: its new text in the Spec when a Case of that session changes it, and `.claude/agents/case-guppi.md` otherwise.
> **＋** The estimate line gives the count of each kind of finding of `ask-guppi` at the `/pre-spec` of that session on the Cases `case-guppi` built, when that `/pre-spec` ran.
> **－** The reading waits for no `/pre-spec` after the render of `rule-case-build`.

> **tasks:**
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set:
>     ```
>     status: pending
>     method: "by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the findings of ask-guppi at the /pre-spec of that session, when it ran, read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a Case of the session named in the prompt whose page or moment the Case clashes with, an Estimate whose purpose or method still states the promise its replaced Criterion dropped, a claim of context that its search did not print, a search in context that the Case does not rest on, two sub-cases whose texts on one page contradict — the count of each in the estimate line"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.
>
>     Then:
>     It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
>     **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
>     **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
>     **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and of each Case of the session that the check of `rule-case-check` names in a finding or a note on its file, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
>     **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
>     **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
>     **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
>     **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
>     **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
>     **－** A hit in a History line, in `log.md` or in `brief.md` is not read.
>     ```
>   - change: `the method reads the Render of rule-case-build against the Criterion at the Retro of the session that changes it, with the count of the findings of ask-guppi at that session's /pre-spec; the Criterion written back unchanged; pending again (case 716)`
> - [ ] read `estimate-case-build-checks-the-finished-case`

> **ratification:**
> ```
> - decision[case 716.2][update][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}
> ```
