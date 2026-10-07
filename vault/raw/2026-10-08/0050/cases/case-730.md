## Case 730 — Cases out at once are a batch, and a change asked of another Case points to the promise

> **context:**
> Two lessons of session 2114 have no fix. First, `lesson-orchestration-showed-a-case-while-a-round-stood-open`: `rule-orchestration` makes Cases a batch only when one answer of the person takes up two or more items, or when the person's word asks that a ratified Case change while another Case is built (cases 598.1, 684.1); a Case the person questions or changes is shown again "alone or in a new batch". In session 2114, after the person dropped a change to Case 722, its `case-guppi` undid the change and 722 came back while a question of Case 723 stood unanswered; the main agent showed 722 for ratification in the same reply as that question. The person chose that any Cases out at the same time are a batch, by whatever route, with no hook: the fault came from a gap in the rule. Case 730.1 writes that into the Render of `rule-orchestration` under a new Estimate, and Case 730.2 turns the line of `estimate-orchestration-signs-a-batch-together` that allowed the Case alone into a pointer to it and sets its method to read the new Render at Retro, so that the reading does not wait for a live moment. Second, `lesson-orchestration-recommended-a-rebuild-that-signed-a-promise-twice`: the `case-guppi` of Case 725 named, in its `context`, the change Case 722.1 needed as an exception written into the Criterion of 722.1, though 725.2 created `estimate-case-check-leaves-out-a-case-the-file-supersedes` for that exception; the main agent recommended the rebuild, and `/pre-spec` found the promise signed twice. The person chose to fix it where the wording is born: Case 730.3 makes `case-guppi` word that change as a pointer to its own Estimate. The main agent, which does not load `case-schema.md`, passes the wording on as it stands. The lessons belong to session 2114, so no decision line carries an `{addresses:...}` mark (case 284.2). Each lesson reopened its Insight, so 730.1 sets `insight-orchestration-items-taken-together-unruled` `actioned` and 730.3 sets `insight-workflow-case-written-without-reading-the-pages-it-changes` `actioned`, as case 699.5 did.
>
> A Grep for `alone or in a new batch|shown again alone|shown alone` over `vault/wiki/`, `.claude/`, `guppi/` and `tests/` printed `vault/wiki/orchestration.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/estimates/estimate-orchestration-signs-items-taken-together.md`, `vault/wiki/estimates/estimate-orchestration-signs-a-batch-together.md` and `vault/wiki/estimates/estimate-orchestration-marks-each-round-of-a-batch.md`. `orchestration.md` is the file rendered from `rule-orchestration`. The line of `estimate-orchestration-signs-items-taken-together` that an item the person takes up alone is shown alone stands, since the main agent takes up no next item while another Case is out, and its other hit is its Result. The line of `estimate-orchestration-marks-each-round-of-a-batch` on a round shown alone speaks of the Context label, which this Case does not touch. A Grep for `Other Case` over `.claude/` printed `.claude/agents/case-guppi.md`, the file rendered from `rule-case-build`, and over `vault/wiki/rules/` printed `vault/wiki/rules/rule-case-build.md` and `vault/wiki/rules/rule-orchestration.md`; `rule-orchestration` sets how the main agent asks the person about another Case, and that stands, since only the wording of the change in `case-guppi`'s `context` changes. A Grep for `Other Case|other Case` over `vault/wiki/estimates/` with the glob `estimate-case-build-*` printed `estimate-case-build-writes-the-case.md` and `estimate-case-build-checks-the-finished-case.md`: the first states the `**Other Case:**` line, so 730.3 replaces its Criterion whole with one line added, its `purpose` and `method` standing, since the method already reads the new Render at Retro; the hit of the second speaks of reading the Cases of the session, not of the wording of a change, and stands. A Glob `vault/wiki/**/estimate-orchestration-batches-*.md` printed nothing, so the new slug is free. The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.
>
> `/pre-spec` found three more sentences of the Render of `rule-orchestration` that state the batch without the new route, and 730.1 gives each the condition: the routes of a batch in `## Plan Mode and the Frontier`, the showing of a Case whose dropped change is undone (case 705.2), and a sub-case shown again alone (case 355.2). `estimate-orchestration-shows-the-built-case` says that the main agent shows the Case again "as after a change" when a dropped change is undone. Its Criterion stands, since it promises the showing of the Case and not when it is shown; the showing after a change now takes the condition of 730.1, and `estimate-orchestration-batches-cases-out-at-once` checks that condition. Writing the condition into that Criterion too would sign it twice.

> **problem:**
> Outside the two kinds of batch, nothing stops the main agent from showing a Case that comes back while a round of another Case stands unanswered, so one reply asks two things. And a `case-guppi` that names the change another Case needs may word as a new promise what an Estimate of its own Case already promises, so the rebuild it leads to signs one promise twice.

> **recommend:**
> - **One Case or two parts**
>   - Recommended: (a) one Case with sub-cases, one for each lesson.
>   - Answer: agreed, (a).
> - **What the main agent does with a Case that comes back while another Case's question is open**
>   - Recommended: (a) any Cases out at the same time, by any route, are a batch until each is ratified or deferred.
>   - Answer: agreed, (a).
> - **Is the rule enforced by a hook**
>   - Recommended: (a) the rule text only, read at the Retro of this session.
>   - Answer: agreed, (a).
> - **Where the double-signed promise is stopped**
>   - Recommended: (a) the Case that asks for the change words it as a pointer to its own Estimate (`rule-case-build`).
>   - Answer: agreed, (a).
> - **Which check covers Cases that are out at the same time**
>   - Recommended: (a) a new Estimate of `rule-orchestration`, read on the new Render at Retro; the line of `estimate-orchestration-signs-a-batch-together` that allows a Case alone becomes a pointer to it, and its method reads the new Render at Retro.
>   - Answer: agreed, (a).
> - **Which check covers the pointer wording of an "Other Case" request**
>   - Recommended: (a) replace the Criterion of `estimate-case-build-writes-the-case` whole, with one line added.
>   - Answer: agreed, (a).
> - **What happens to the two Insights**
>   - Recommended: (a) each sub-case sets its Insight `actioned`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the findings of `/pre-spec` asked that 730.1 give the new condition to three more sentences of `rule-orchestration` and say why `estimate-orchestration-shows-the-built-case` stands, and that 730.2 replace the old line of its Criterion instead of keeping it beside a pointer.
>   - Taken: 730.1 gains three replace pairs and a paragraph of `context` on that Estimate; in 730.2 the old line is replaced by the conditioned line.

### Case 730.1 — Cases out at the same time are a batch

> **given:**
> `rule-orchestration`: the rule whose Render sets when Cases are a batch.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-batches-cases-out-at-once`: the new check of Cases out at the same time.
> **＋** `estimate-orchestration-signs-items-taken-together`: the check of the batch of items taken up in one answer.
> **＋** `estimate-orchestration-signs-a-batch-together`: the check of the batch of a ratified Case asked to change.
> **＋** `rule-prespec`: the rule of the loop after the findings of `/pre-spec`.
> **＋** `insight-orchestration-items-taken-together-unruled`: the Insight that the lesson of this sub-case reopened; set `actioned`.

> **when:**
> In Plan Mode before `/pre-spec`, a Case of the session goes back to its `case-guppi` — the person questions or changes it, or the person drops a change to it and its `case-guppi` undoes the change — while the `case-guppi` of another Case has not answered or a round of another Case stands unanswered, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The Cases out at the same time are one batch, and take the steps of a batch that `vault/wiki/orchestration.md` sets until each is ratified or deferred.
> **＋** The main agent shows no Case while a round of another Case of the batch stands unanswered: a Case that comes back built waits, and is not shown.
> **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line under the bold label `**Waiting:**`, translated, that names the Cases that have answered and those still out, and nothing else.
> **＋** It shows every round that came back in one list, each question numbered `<Case id>.Q<n>`, and sends each answer to the `case-guppi` of its Case, all in one message.
> **＋** It shows every Case of the batch in one reply, for one ratification.
> **－** A Case that goes back while no other Case of the session is out is shown again alone.
> **－** A batch of items that one answer of the person takes up, and a batch of a ratified Case asked to change while another Case is built, are the moments of `estimate-orchestration-signs-items-taken-together` and `estimate-orchestration-signs-a-batch-together`.
> **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` a Case the person questions or changes goes back to its `case-guppi` and is shown again, alone or in a new batch with each Case it asks to change (case 598.1). ``
>   - new: `` a Case the person questions or changes goes back to its `case-guppi` and is shown again, alone when no other Case of the session is out, or in a new batch with each Case it asks to change (case 598.1). Before `/pre-spec`, Cases out at the same time by any other route — a Case the person questions or changes, or a Case whose dropped change its `case-guppi` undoes, while the `case-guppi` of another Case has not answered or a round of another Case stands unanswered — are a batch too, and take its steps until each is ratified or deferred: a Case that comes back built while a round of another Case stands unanswered waits, and is not shown, and every Case of the batch is shown in one reply (case 730.1). ``
>   - old: `` or when the person's word asks that a Case already ratified change while another Case is built, as `## Showing and signing a Case` sets it (cases 598.1, 684.1) ``
>   - new: `` or when the person's word asks that a Case already ratified change while another Case is built, or when Cases are out at the same time by any other route, as `## Showing and signing a Case` sets it (cases 598.1, 684.1, 730.1) ``
>   - old: `the agent shows the Case again as after a change, and the person ratifies it again`
>   - new: `the agent shows the Case again as after a change — in a batch while another Case of the session is out (case 730.1) — and the person ratifies it again`
>   - old: `a sub-case the person questions or changes is shown again alone (case 355.2)`
>   - new: `a sub-case the person questions or changes is shown again alone when no other Case of the session is out, and otherwise in a batch (cases 355.2, 730.1)`
>   - change: `Cases out at the same time by any route are a batch, so no Case is shown while a round of another Case stands unanswered (case 730.1)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] create `estimate-orchestration-batches-cases-out-at-once`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether Cases out at the same time by a route other than the two batches already set are a batch, so that no Case is shown while a round of another Case stands unanswered`
>   - method: `by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow]`
> - [ ] update `insight-orchestration-items-taken-together-unruled`
>   - set: `{status: actioned}`
>   - change: `actioned: Cases out at the same time by any route are a batch, so no Case is shown while a round of another Case stands unanswered (case 730.1)`
> - [ ] read `estimate-orchestration-batches-cases-out-at-once`

> **ratification:**
> ```
> - decision[case 730.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 730.1][create][estimate-orchestration-batches-cases-out-at-once]{ref:rule-orchestration}{tags:session,workflow}
> - decision[case 730.1][update][insight-orchestration-items-taken-together-unruled]{ref:insight-orchestration-items-taken-together-unruled}
> ```

### Case 730.2 — A Case shown again alone only when no other Case is out

> **given:**
> `estimate-orchestration-signs-a-batch-together`: the check of the batch of a ratified Case asked to change; its Criterion is replaced whole and its method set.
> **＋** `estimate-orchestration-batches-cases-out-at-once`: the check that a Case shown again while another Case is out points to.
> **＋** `rule-orchestration`: the rule whose Render the method reads.

> **when:**
> In a batch of a ratified Case asked to change, the person questions or changes a Case of the batch after it is shown, and it goes back to its `case-guppi`.

> **then:**
> While another Case of the session is out, the Case is shown as `estimate-orchestration-batches-cases-out-at-once` sets it.
> **－** The main agent does not show it alone while that other Case is out.

> **tasks:**
> - [ ] update `estimate-orchestration-signs-a-batch-together`
>   - set:
>     ```
>     status: pending
>     method: "by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     In Plan Mode before `/pre-spec`, the person's answer to a round of a `case-guppi`, or the person's word on a shown Case, asks that a Case already ratified in the session change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
>
>     Then:
>     The main agent sends the ratified Case back to its `case-guppi` by `SendMessage`, and shows neither that Case nor the Case being built alone: the two are one batch.
>     **＋** A Case that a Case of the batch asks to change in the same way joins the batch.
>     **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
>     **＋** It shows one list of every round that came back, each question in the shape of `.claude/skills/grill-me/SKILL.md` and numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
>     **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification.
>     **＋** The person ratifies the batch at once or names the ids. A Case the person questions or changes goes back to its `case-guppi` and is shown again, alone only when no other Case of the session is out, or in a new batch with each Case it asks to change; while another Case is out, it is shown as `estimate-orchestration-batches-cases-out-at-once` sets it.
>     **－** Outside a batch and the loop after the findings of `/pre-spec`, the main agent does not take up the next item of `raw/<date>/<hi HHMM>/frontier.md` before the shown Case is ratified or deferred.
>     **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.
>     ```
>   - change: `the Criterion replaced whole — a Case is shown again alone only when no other Case is out, and otherwise as estimate-orchestration-batches-cases-out-at-once sets it; the method reads the new Render at Retro (case 730.2)`
> - [ ] read `estimate-orchestration-signs-a-batch-together`

> **ratification:**
> ```
> - decision[case 730.2][update][estimate-orchestration-signs-a-batch-together]{ref:rule-orchestration}
> ```

### Case 730.3 — A change asked of another Case points to the promise

> **given:**
> `rule-case-build`: the rule whose Render sets how `case-guppi` names the change another Case needs.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-case-build-writes-the-case`: the check of the `**Other Case:**` line; its Criterion is replaced whole.
> **＋** `vault/wiki/case-schema.md`: the schema that says nothing is signed twice.
> **＋** `insight-workflow-case-written-without-reading-the-pages-it-changes`: the Insight that the lesson of this sub-case reopened; set `actioned`.

> **when:**
> `case-guppi` of `.claude/agents/case-guppi.md` names in the `context` of its Case another Case of the session and the change that Case needs, and again on a line `**Other Case:**` of its summary.

> **then:**
> Where an Estimate that its own Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate.
> **－** It does not word that promise again as a change the other Case needs, since `vault/wiki/case-schema.md` says that nothing is signed twice.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` name in `context` the other Case and the change it needs, and again on a line ``
>   - new: `` name in `context` the other Case and the change it needs — where an Estimate your own Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it needs is a pointer to that Estimate, never that promise written again, since nothing is signed twice (case 730.3) — and again on a line ``
>   - change: `the change another Case needs is a pointer to an Estimate of the Case that names it, when that Estimate already makes its promise (case 730.3)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-writes-the-case`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
>     **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.
>     **＋** Or the main agent sends it by `SendMessage` the drop of the Case it built, the drop of a change to that Case, or a finding of `/pre-spec` on that Case.
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
>     **＋** Where an Estimate that the Case creates, or whose Criterion it replaces, already makes the promise behind that change, the change it names is a pointer to that Estimate, never that promise written again.
>     **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
>     **＋** Asked, by a message or by a finding of `/pre-spec`, for a fix that adds a second behaviour with a promise of its own to a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and no sub-cases, it builds that behaviour as a new top-level Case beside it, in its own file and with no `{supersedes:case N}` mark. The number of the new Case is one above the highest number of the files under `raw/<date>/<hi HHMM>/cases/` and of the decision lines of that ledger, or the free number that the guard of `guppi/ratified.py` names when it refuses that number. The ratified Case and its file stay as they are, and its summary names the new Case.
>     **＋** A pair of that new Case whose sentence the ratified Case changed takes that sentence as the ratified Case leaves it.
>     **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
>     **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: auto`, so it writes its file with no prompt while the session is in Plan Mode.
>     **＋** Sent the drop of its Case, which has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, it writes empty text into the file of that Case by `Write` and answers with a first line `**Dropped:**` and the path of the file, and nothing else. A file of its own that it leaves behind, when it builds the Case again under another number, it empties the same way only when that Case has no decision line in that ledger.
>     **＋** Sent the drop of a change to its Case, which has a decision line in `raw/<date>/<hi HHMM>/ledger.md` and which it changed after the Case was last ratified, it undoes by `Edit` each edit it made since then in every section but `recommend`. `recommend` keeps its items and gains one item `**Change**`: its `Asked:` line says that the person dropped the change, and its `Taken:` line says that the Case went back to its ratified form. It answers with the summary again, so that the check of `rule-case-check` finds an item for each question of its rounds.
>     **－** A fix that changes what the ratified Case already set is not built beside it: `case-guppi` builds the Case again under a new number, as `vault/wiki/case-schema.md` sets it.
>     **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
>     **－** It does not write the whole Case again to fix a finding, make a change or undo a change.
>     **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
>     **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
>     **－** It writes no file but the file of its Case, the file it leaves behind under an earlier number of the same Case, and the file of a new Case it builds beside a ratified Case, and no ledger line.
>     **－** It empties no file of a Case that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, the file it leaves behind when it builds that Case again under a new number included: sent the drop of such a Case that it did not change after the Case was last ratified, it answers under a first line `**Fact:**` that the Case is ratified, and the file stands.
>     ```
>   - change: `the Criterion replaced whole — the change another Case needs is a pointer to an Estimate of the Case that names it, when that Estimate already makes its promise (case 730.3)`
> - [ ] update `insight-workflow-case-written-without-reading-the-pages-it-changes`
>   - set: `{status: actioned}`
>   - change: `actioned: case-guppi words the change another Case needs as a pointer to its own Estimate when that Estimate already makes the promise (case 730.3)`
> - [ ] read `estimate-case-build-writes-the-case`

> **ratification:**
> ```
> - decision[case 730.3][update][rule-case-build]{ref:rule-case-build}
> - decision[case 730.3][update][estimate-case-build-writes-the-case]{ref:rule-case-build}
> - decision[case 730.3][update][insight-workflow-case-written-without-reading-the-pages-it-changes]{ref:insight-workflow-case-written-without-reading-the-pages-it-changes}
> ```
