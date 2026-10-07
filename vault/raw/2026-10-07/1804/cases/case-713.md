## Case 713 — The person takes back a ratified Case by a short Case that supersedes it

> **context:**
> A ratified Case has decision lines in the ledger of the session, and the ledger only grows. Only a `{supersedes:case N}` mark on a line of a newer Case retires it: the `Stop` hook of `rule-spec-write` then removes Case N from the plan, `/pre-spec` asks no item for its lines, and the hook of `rule-prespec-onward` never counts it as out. Case 705 set how a dropped change to a ratified Case is undone, and left the take-back of a whole ratified Case not done; the handoff of session 0636 and the brief carry it. Today no rule sets it: `case-guppi` answers a drop of a ratified Case under `**Fact:**` that it is ratified, and the Case stays in the plan, where Work Mode would build it. The person chose that the main agent writes, with no dispatch, a short Case in the form of a deferred decision whose `defer` lines carry the mark; that this holds in Plan Mode only; that it may name one sub-case; that the line of the item in `frontier.md` closes as its source is put off; and that a new Estimate checks it.
>
> The frame changed one choice. `guppi/generate.py` marks `deferred_by`, and so the backlog, only on rule, entity and insight pages (`DEFERRABLE`); a `defer` of an existing Estimate writes one History line, and a `defer` of a missing Estimate writes a placeholder with no `target`, `method` or Criterion, which `vault/wiki/estimates/schema.yaml` requires. So the person chose that the short Case puts off each rule, entity and insight page, each Estimate the Case updates, and, for each Estimate it creates, the page that Estimate checks; its `context` names the Estimates left out. For a page that exists, `defer` sets no field: the `type` and `purpose` of its item reach only the `## Deferred` list of the Decision page. A `defer` line passes the hold of the ledger hook, which judges only lines of another kind.
>
> `guppi/prespec.py` reports a line closed `case N` whose heading left the plan, and a line closed `defer case N` whose source is `sprint` or `backlog`. So the line of the item changes from `[x] … · case N` to the closer of its source. Two sentences of the Render of `rule-orchestration` say that such closers come with no Case: the sprint closer has no Case, and an item of `backlog.md` kept has no short Case and no ledger line. The Case rewords both, and the sentence that gives the short form one moment. The sentence of `case-schema.md` that a Frontier line closed by a superseded Case is closed again by the superseding Case stays true: the line closes again in the reply of the short Case.
>
> A Grep for `(?i)\bdrop(s|ped)? (that|the|its|your|a) (ratified )?Case|take(s|n)? back` over `vault/wiki/rules/` printed `rule-case-build.md` and `rule-orchestration.md`, and over `.claude/` printed `.claude/agents/case-guppi.md`. The hit in `rule-orchestration.md` is the paragraph of the drop, which this Case extends. The hit in `rule-case-build.md`, rendered into `.claude/agents/case-guppi.md`, sets the answer of `case-guppi` to the drop of a ratified Case. It stands, since at a take-back the main agent sends `case-guppi` no message. A Glob `vault/**/*take*back*` printed nothing, so the new slug is free.
>
> Of the Estimates of `rule-orchestration`, `estimate-orchestration-defers-in-one-reply` checks the reply that puts off an item not yet decided. Its line that a sprint item put off or a backlog item kept takes no short Case stands: its `when` is that moment, and the take-back is the moment of the new Estimate. `estimate-orchestration-shows-the-frontier-after-a-closed-line` covers only a reply with no defer, and `estimate-orchestration-shows-the-built-case` says that the file of a Case with a decision line is never emptied, which still holds. `estimate-spec-write-removes-a-superseded-case` already checks the removal by the hook. No code changes. The rendered `orchestration.md` changes at the librarian's render. Until then the main agent has no rule for a take-back, and no hook refuses anything in between.

> **problem:**
> The person cannot take back a ratified Case in its session. The Case stays in the plan, and Work Mode would build it.

> **recommend:**
> - **What does taking back an approved Case leave behind?**
>   - Recommended: (a) a short "put off" Case replaces it; its line carries the mark that replaces the old Case, and its pages go to the backlog.
>   - Answer: agreed, (a).
> - **When can an approved Case be taken back?**
>   - Recommended: (a) in Plan Mode only; in Work Mode the agent tells the person that the Case is already being built.
>   - Answer: agreed, (a).
> - **Can a take-back name a single sub-case?**
>   - Recommended: (a) the whole Case or one sub-case.
>   - Answer: agreed, (a).
> - **How does the item's Frontier line close after a whole take-back?**
>   - Recommended: (a) close it the way its source is put off: put off by the short Case, a sprint item put off, or a backlog item kept.
>   - Answer: agreed, (a).
> - **Which pages does the short Case put off?**
>   - Recommended: (a) every page of the approved Case, Estimates included.
>   - Answer: agreed, (a); the Estimates were then settled by the question on the Estimates of the approved Case.
> - **Which check proves that the take-back works?**
>   - Recommended: (a) a new Estimate for the take-back; the put-off check stays as it is.
>   - Answer: agreed, (a).
> - **What happens to the Estimates of the approved Case when it is taken back?**
>   - Recommended: (a) put off each rule, entity and insight page and each Estimate the Case updates, and for each Estimate it creates the page that Estimate would check; the short Case names the Estimates left out.
>   - Answer: agreed, (a).
> - **What goes into the backlog when the Case taken back changes only Estimates that already exist?**
>   - Recommended: (a) also put off the page each changed Estimate checks, once per page.
>   - Answer: agreed, (a); Case 719 carries it, and supersedes this Case.

> **given:**
> `rule-orchestration`: its Render sets the take-back of a ratified Case and the closers of the Frontier.
> **＋** `estimate-orchestration-takes-back-a-ratified-case`: the new check of the take-back.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-spec-write`: the hook that writes a short Case and removes the Case its `{supersedes:case N}` names.
> **＋** `rule-prespec-onward`: the hook that never counts a Case retired by such a mark as out.
> **＋** `guppi/generate.py`: a `defer` marks only rule, entity and insight pages.
> **＋** `/pre-spec` and `rule-prespec`: the check that reads the closers of the Frontier and the end of Plan Mode.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the Frontier, the ledger and the file of a Case.

> **when:**
> In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to take back a Case of the session that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, whole or one of its sub-cases.

> **then:**
> In the same reply the main agent shows a short Case of its own in the form of a deferred decision, with no dispatch of `case-guppi`, and carries its `LEDGER` block, with no tool call after it.
> **＋** The block holds one `defer` line for each rule, entity and insight page the Case taken back names, one for each Estimate it updates, and one for the page that each Estimate it creates would check, once per page; each line carries `{supersedes:case N}` for the Case or sub-case taken back.
> **＋** The `context` of the short Case names the Case taken back and each Estimate that Case creates.
> **＋** The person's words asking for the take-back are its ratification: no question asks for it.
> **＋** The `Stop` hook of `rule-spec-write` writes the short Case under `## Deferred` and removes the Case taken back from the plan file.
> **＋** When no part of the Case stays in the plan, the line of its item in `raw/<date>/<hi HHMM>/frontier.md` changes in the same reply from `[x] … · case N` to `[-] … · sprint · defer` for an item of the sprint, `[-] … · backlog · kept` for an item of the backlog, or `[-] … · defer case M` of the short Case for any other source.
> **＋** The reply ends as the reply that carries a defer: the Frontier, then the question which open item is next, or before `/pre-spec` the question whether to go on to `/pre-spec`, or after `/pre-spec` no question.
> **－** The file of the Case taken back under `raw/<date>/<hi HHMM>/cases/` is not emptied, and no `case-guppi` undoes it.
> **－** In Work Mode no Case is taken back: the main agent tells the person that the ratified Case stands, and that a Case of a later session may replace it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` `[-] … · sprint · defer` for an item of the sprint left for later — no Case, never `· defer case N` (case 356.2) ``
>   - new: `` `[-] … · sprint · defer` for an item of the sprint left for later — no Case but the short Case of a take-back (case 713), never `· defer case N` (case 356.2) ``
>   - old: `` so that the hook of `rule-prespec-onward` counts the Case as ratified (case 705.2). ``
>   - new: `` so that the hook of `rule-prespec-onward` counts the Case as ratified (case 705.2). When, in Plan Mode, the person takes back a ratified Case whole, or one of its sub-cases, the agent dispatches no `case-guppi` and shows in its reply a short Case of its own, in the form of `## The short form — deferred decisions`, whose `LEDGER` block holds one `defer` line for each rule, entity and insight page the Case taken back names, one for each Estimate it updates, and one for the page that each Estimate it creates would check, once per page, each line carrying `{supersedes:case N}` for the Case or sub-case taken back, and whose `context` names the Case taken back and each Estimate that Case creates; the person's words are its ratification, the `Stop` hook of `rule-spec-write` removes the Case taken back from the plan, and its file under `cases/` stands; when no part of the Case stays in the plan, the line of its item in `frontier.md` changes in the same reply from `[x] … · case N` to the closer of its source put off — `[-] … · sprint · defer` for an item of the sprint, `[-] … · backlog · kept` for an item of `backlog.md`, and `[-] … · defer case M` of the short Case for any other source — and the reply ends as the reply that carries a defer; in Work Mode no Case is taken back, and the agent tells the person that the ratified Case stands and that a Case of a later session may replace it (case 713). ``
>   - old: `It has one moment: the close of Plan Mode, when the person defers the items left open;`
>   - new: `` It has two moments: the close of Plan Mode, when the person defers the items left open, and the take-back of a ratified Case in Plan Mode, as `## Showing and signing a Case` sets it (case 713); ``
>   - old: `` An item of `backlog.md` left as it stands is no decision: no short Case, no ledger line; ``
>   - new: `` An item of `backlog.md` left as it stands is no decision: no short Case, no ledger line, but for the short Case of a take-back, whose item closes the same way and whose `defer` lines add to its source (case 713); ``
>   - change: `the person takes back a ratified Case, or one of its sub-cases, in Plan Mode by a short Case whose defer lines supersede it, and the line of its item closes as its source is put off (case 713)`
> - [ ] create `estimate-orchestration-takes-back-a-ratified-case`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `A ratified Case the person takes back in Plan Mode is retired by a short Case of the main agent whose defer lines supersede it, and the line of its item closes as its source is put off`
>   - method: `by hand at Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, ledger]`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-takes-back-a-ratified-case`

> **ratification:**
> ```
> - decision[case 713][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 713][create][estimate-orchestration-takes-back-a-ratified-case]{ref:rule-orchestration}{tags:session,workflow,ledger}
> ```
