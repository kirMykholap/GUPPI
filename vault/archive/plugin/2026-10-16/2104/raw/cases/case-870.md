## Case 870 — case-guppi asks before it puts a change into a new Case

> **context:**
> When the main agent asks `case-guppi` to change a Case by name, the agent sometimes writes a new top-level Case under a new number, and the named Case stays as it was. `insight-case-build-opens-a-new-case-where-one-was-named` clusters two lessons of this cause. In session 0104, at `/pre-spec`, the agent of Case 847 was asked to take the task that pushes the release tag into Case 847. It built Case 850 beside it, and Cases 841, 843 and 846, built again in the same message, named Case 847 as the holder of the push and went back a second time (`lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own`). The case file of Case 850 says why: Case 847 already had a decision line. That follows the sentence of case 725.1 in the Render of `rule-case-build`, which has the agent build a fix that adds a second behaviour to a ratified Case with no sub-cases as a new Case beside it, under a number it picks itself. In session 0342 the agent of Case 851, ratified in Plan Mode, got the `/pre-spec` findings and wrote `case-856.md` with `{supersedes:case 851}` marks, the step that the sentence of case 806.2 sets for Work Mode only, and the main agent sent it back to rebuild under 851 (`lesson-case-build-rebuilds-a-ratified-case-under-a-new-number-in-plan-mode`). In both events the agent alone chose where a change goes. The rule that governs this is `rule-case-build` itself, whose Render says that the agent decides nothing the person has not decided.
>
> The person chose to action the Insight by a round before a new Case. Where a message names a Case, the agent builds the change under that number. Outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one, as it does for a Case built again in another shape. Where a fix would add a second behaviour to a ratified Case with no sub-cases, the agent writes no new file. It asks the person in a round whether the behaviour goes into that Case or into a new Case beside it. The Insight's own proposal, that only the main agent gives out new numbers, was not taken. It conflicts with `vault/wiki/case-schema.md`, where the check of the file names the new number of a Case built again in another shape, and with the guard of `rule-spec-reconcile`, which holds a number the agent takes. That guard and `next_id` of `.guppi/guppi/caseid.py` already keep two Cases from one number, since `next_id` counts the keys of the store and the case files. Other Cases being rebuilt in parallel may still name the old Case before the person answers. That part is the item of Case 872.
>
> The behaviour is checked by `estimate-case-build-writes-the-case`, whose Criterion holds the old line on a new Case beside a ratified one. This Case replaces that Criterion whole. The old line becomes three, and a fourth line is new: a `－` line that says it does not put a change asked on a named Case into a new top-level Case without the person's answer to a round. The line on the tools names WebFetch, since Case 871, ratified in this session, adds `WebFetch` to the tools of the Render, and the reading of this Criterion at Retro comes after that render. Every other line stands as it was. The check of the file notes two old lines as not carried: the line on a new Case beside a ratified one and the line on the model and the tools. Both are rewritten, not dropped. Its `purpose` and `method` do not state the old promise, so they stand. In `rule-case-build`, read whole, these sentences state the behaviour. The sentence of case 645.1, which says that a message is answered by `Edit` of the file, or by a round when it opens a fork, stays true. The sentence of case 725.1 changes by the `replace` pair below, and its end, from the number onward, stays. The sentences of case 806.2 on Work Mode stay true. The list of files the agent may write, which names the file of a new Case built beside a ratified Case, stays true, since that Case is still built when the person chooses it. In `vault/wiki/orchestration.md`, the sentence that the guard holds a number `case-guppi` takes for a Case built again stays true. A round sent back at `/pre-spec` is shown to the person by step 4 of `rule-prespec`, so this Case does not set that moment.
>
> A Grep for `case-guppi\.md|rule-case-build|estimate-case-build-writes-the-case` over `.guppi/tests/` printed no file, so no test reads the live agent file or these pages. A Grep for `estimate-case-build-writes-the-case|insight-case-build-opens-a-new-case-where-one-was-named` over `vault/wiki/` printed `backlog.md`, `log.md`, `lessons/lesson-case-build-rebuilds-a-ratified-case-under-a-new-number-in-plan-mode.md`, `lessons/lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own.md`, `rules/rule-case-build.md`, `estimates/estimate-case-check-sends-back-a-faulty-case.md` and `estimates/estimate-skill-grill-me-asks-in-rounds.md`. `backlog.md` is written again by `guppi backlog`, and `log.md` is not read. The `insight` field of the two lessons stays true. The hit in `estimate-skill-grill-me-asks-in-rounds` is a History line. The Criterion of `estimate-case-check-sends-back-a-faulty-case` waits for a reading of `estimate-case-build-writes-the-case` that passes live, for an old way of reading a transcript. This Case does not change that path, and the Result of that Estimate already records a passing reading on 2026-10-14, so the line stands.
>
> The Insight leaves the backlog by an `update` to `actioned` with `addressed_by: decision-case-870`, as `rule-insights-schema` sets it (case 712). It has no `deferred_by`, so no `{supersedes:...}` mark is needed. Its two lessons belong to other sessions, so they get no mark. Cases 868 and 869 of this batch change `rule-case-build` by pairs on the sentence on a reader that only goes red and on the sentence of case 785. This Case's pair stands on the sentence of case 725.1, so the anchors do not overlap. Cases 871 and 872 also change `rule-case-build`, and their files were not read. If one of them takes the sentence of case 725.1 as its anchor, the two pairs must be read side by side. No option rests on a check passing.

> **problem:**
> Asked to change a named Case, `case-guppi` may put the change into a new top-level Case under a number it picks. The named Case then stays as it was, and the Cases that name it are built again. The person never chose where the change goes.

> **recommend:**
> - **What should be done with this insight?**
>   - Recommended: (a) ask before opening a new Case: a change goes under the number of the Case a message names; where a fix would add a second behaviour to a ratified Case with no sub-cases, `case-guppi` writes no new file and asks in a round whether it goes into that Case or into a new Case beside it; during planning a named Case keeps its number unless the schema sets a new one.
>   - Answer: agreed, (a).
> - **Which check page proves the change?**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-writes-the-case` whole, its old line on a new Case beside a ratified one made three.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.
> **＋** `estimate-case-build-writes-the-case`: its Criterion is replaced whole.
> **＋** `insight-case-build-opens-a-new-case-where-one-was-named`: the Insight this Case actions.
> **＋** `vault/wiki/case-schema.md`: the form that sets a new number for a Case built again.
> **＋** `rule-prespec`: the rule that shows the person a round sent back at `/pre-spec`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the shape of a round.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the case files of the session.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case.
> **＋** `.guppi/guppi/ratified.py`: the guard that names a free number for a case file.
> **＋** `rule-case-check`: the check of a case file and of a summary.
> **＋** `vault/wiki/ratification.md`: the form of the ledger lines.
> **＋** `.claude/agents/ask-guppi.md`: the vault query run before a `create` without a `ref`.
> **＋** `.claude/settings.json`: the hooks registered on each event.

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
> **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
> **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
> **＋** Or, in Work Mode, the main agent dispatches it with the id of a new top-level Case, the path of the file of a ratified Case of the approved Spec, the sub-case of it that must change and the reason.

> **then:**
> `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
> **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
> **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
> **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
> **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
> **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
> **＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
> **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
> **＋** Asked, by a message or by a finding of `/pre-spec`, to change a Case, it builds the change under the number of that Case; outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one for it.
> **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it writes no new file and answers with a round that asks whether the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it.
> **＋** Where the person chooses a new Case beside it, it builds that behaviour as a new top-level Case in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `.guppi/guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
> **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
> **＋** Dispatched in Work Mode with a ratified Case and the sub-case of it that must change, it reads the file of that Case whole and builds under the id of the prompt a new top-level Case that holds each sub-case it replaces whole, as it is to stand: each page change, task and Estimate of that sub-case that still holds, with the change.
> **＋** Each decision line of that new Case carries `{supersedes:case N.M}` for each sub-case it replaces, or `{supersedes:case N}` for a ratified Case with no sub-cases, and the file of the ratified Case stays as it is.
> **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
> **＋** In Work Mode a round may also come when it builds a new Case that replaces a sub-case of a ratified Case.
> **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write, Edit and WebFetch, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
> **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
> **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
> **－** It does not put a change asked on a named Case into a new top-level Case without the person's answer to a round.
> **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
> **－** In Work Mode it never builds a Case of the approved Spec again under its own number; a Case ratified in that Work Mode that comes back to it before any of its tasks has run it changes under its own number, as in Plan Mode.
> **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
> **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
> **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
> **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
> **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
> **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` A fix, asked by a message or by a finding of `/pre-spec`, that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, you build as a new top-level Case beside it, in its own file and with no `{supersedes:case N}` mark, under a number ``
>   - new: `` A change that a message or a finding of `/pre-spec` asks on a Case you build under the number of that Case: outside Work Mode a Case keeps its number unless `vault/wiki/case-schema.md` sets a new one for it (as set in case 870). A fix, asked by a message or by a finding of `/pre-spec`, that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, you do not place yourself: you write no new file and answer with a round that asks whether the behaviour goes into that Case, built again under a new number as `vault/wiki/case-schema.md` sets it, or into a new top-level Case beside it (as set in case 870). Where the person chooses a new Case beside it, you build it in its own file and with no `{supersedes:case N}` mark, under a number ``
>   - change: `case-guppi builds a change under the number of the Case a message names, and asks in a round before it puts a second behaviour of a ratified Case into a new Case beside it (case 870)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a change goes under the number of the named Case, and a round comes before a new Case beside a ratified one`
> - [ ] read `estimate-case-build-writes-the-case`
> - [ ] update `insight-case-build-opens-a-new-case-where-one-was-named`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-870
>     ```
>   - change: `actioned: case-guppi builds a change under the number of the Case a message names, and asks in a round before a new Case beside a ratified one, in rule-case-build (case 870)`

> **ratification:**
> ```
> - decision[case 870][update][rule-case-build]{ref:rule-case-build}
> - decision[case 870][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> - decision[case 870][update][insight-case-build-opens-a-new-case-where-one-was-named]{ref:insight-case-build-opens-a-new-case-where-one-was-named}
> ```
