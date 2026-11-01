## Case 991 — A Frontier line closes by what the decision lines of its Case do

> **context:**
> The main agent closes a line of the session's Frontier, `raw/<date>/<hi HHMM>/frontier.md`, in the reply that ends its item. `vault/wiki/orchestration.md` and `.claude/skills/hi/SKILL.md` say that a line closes `[x] … · case N` when Case N is ratified. The check of `/pre-spec` asks for more. `check_frontier`, `updates_the_sprint`, `check_backlog_line`, `deferred_pages` and `decided_on_its_page` of `.guppi/guppi/prespec.py`, read whole, refuse a sprint line closed `· case N` when no `update` of the sprint page stands under Case N or a sub-case. For a backlog line closed `· case N`, they judge only each page of its title that carries `deferred_by`. `deferred_pages` leaves out a page without that field, such as an open Insight. Such a line is refused when no decision line of Case N other than a `defer` names the page, or when no Case among Case N and its sub-cases that names the page carries `{supersedes:case M}` for each Case M of the page's `deferred_by`. The agent followed the shorter text in three sessions, and each time the check refused the line: session 2026-10-10/1913 closed a milestone line by Case 769, which updated no sprint page; session 2026-10-30/1713 closed a backlog line by Case 934, which only deferred its page again; and session 2026-11-01/1721 closed the backlog line of `rule-ratification` by Case 988, in which the person kept the defer. The librarian clustered these three lessons in `insight-frontier-line-closed-by-the-case-built-on-its-item`.
>
> The person chose to fix the text the agent reads, with no new hook. Both texts now state that a Case ends its item only by its decision lines, and that a line whose Case ends nothing closes as the item put off. A sprint line whose Case updates no sprint page closes `[-] … · sprint · defer`, and the decision lines of that Case stand. The text names what the check judges: the sprint page, and a backlog page that carries `deferred_by`. An open Insight of the backlog ends by an `update` of its page, as `rule-insights-schema` sets it, and as Case 991.1 itself does. Any other item ends by its ratification, which no check judges. The texts no longer say that a closer of an item put off comes with no Case at all; they say the item gets no short Case and no ledger line of its own. This holds in `## Plan Mode and the Frontier` and `## The short form — deferred decisions` of `rule-orchestration`, and in `rule-skill-hi`. The take-back sentence of `## Showing and signing a Case` now changes the line from the closer it stands with, since after this Case a line can already stand as put off when its Case is taken back. Case 991.1 also creates `estimate-orchestration-closes-a-line-by-what-its-case-does` and marks the Insight `actioned`. The Insight has no `deferred_by`, so no `{supersedes}` mark applies.
>
> Three Estimates had one line each that the change makes false, so three sub-cases replace their Criteria whole, with each other line kept word for word. Case 991.2 does this for `estimate-hi-writes-frontier`. Its `method` waits for the person's answer after the close of a sprint, but it opened `by hand:`, a form that `case-schema.md` does not take as a wait for an event, since only a part that opens with `after`, or `by hand, after`, and names its event before a colon is such a wait (case 781). So 991.2 also sets that `method` anew in the form `by hand, after <event>: …`, with the same meaning, and its `read` line stays: the Retro of this session leaves the Estimate `pending` until that event. Case 991.3 does it for `estimate-orchestration-takes-back-a-ratified-case`, and Case 991.4 for `estimate-orchestration-defers-in-one-reply`. The `purpose` and `method` of those two do not state the old line, so they stand, and `estimate-hi-writes-frontier` has no `purpose`. These were findings of `/pre-spec` on the Case as first ratified.
>
> These stand. `estimate-orchestration-closes-a-backlog-item-deferred-again` says an item left as it stands with no Case closes `kept`, but not that only such an item does, so it stays true. `estimate-orchestration-acknowledging-reply` only lists the closers. `estimate-orchestration-shows-the-frontier-after-a-closed-line` and the matching sentence of `orchestration.md` speak of a reply that closes a line with no ratification. A line closed as put off in the reply that ratifies its Case is closed in the acknowledging reply, which already shows the Frontier. `estimate-prespec-checks-the-frontier` and `estimate-prespec-requires-a-backlog-item-decided-on-its-page` check what the new text names for a sprint item and for a backlog page that carries `deferred_by`, and the check does not change. `estimate-prespec-binds-a-sprint-line` says that an item closed `· sprint · defer` stays in its milestone until `generate` moves it after three such sessions in a row. A Grep of `in a row|three sessions` over `.guppi/guppi/` printed `.guppi/guppi/check.py` and `.guppi/guppi/powershellguard.py`, neither of them about such a move, so no code makes it. The closer `· sprint · defer` for a sprint line whose Case updates no sprint page is also what the check accepted and what the lesson of session 2026-10-10/1913 found before this Case. So that line is no more false than it was, and it stands for a Case of its own.
>
> The blocks in `.guppi/links.md` of `rule-orchestration`, `rule-skill-hi`, `vault/wiki/orchestration.md`, `.claude/skills/hi/SKILL.md`, the Insight and the three Estimates name `rule-prespec`, `rule-backlog`, `rule-sprint`, `rule-spec-write`, `rule-prespec-onward` and `estimate-orchestration-shows-the-frontier-after-a-closed-line` among their neighbours. None of them sets the closer by a Case in other words. Case 992 of this session replaces Case 990 whole, and its finished file was read. Case 992.2 changes `rule-orchestration` only in `## The acknowledging reply` and replaces the Criterion of `estimate-orchestration-acknowledging-reply`. This Case keeps its pairs to the closer passages of three other sections, so no `old` of either Case falls in the text of the other. The new texts agree. In Case 992.2, the acknowledging reply shows lines put off as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`, and these are the closers that Case 991.1 gives a line whose Case ends nothing, in the reply that carries the decision lines of that Case. The `STOP:` line that Case 992.2 sets before the `LEDGER` block of a reply that waits for the person after `/pre-spec` changes no closer. The defer reply and the reply that closes a line with no ratification, which Cases 991.3 and 991.4 keep, wait for nobody, as Case 992 also finds. A Grep of `when ratified|no Case but|no Case, no ledger line|needs none closes|937\.2` over `.guppi/tests/` printed nothing, so no test reads the changed sentences. No code changes, so no judgment gets a second copy. The ledger of this session holds no `error` lesson. The three lessons belong to earlier sessions, so this Case gives them no mark.

> **problem:**
> The texts the main agent reads say that a Frontier line closes `· case N` when its Case is ratified, while the check of `/pre-spec` asks that a decision line of that Case end the item. So the agent closes a line that the check then refuses, and the line is closed again.

> **recommend:**
> - **How the agent learns that a line does not close by its Case**
>   - Recommended: (a) say it in the text the agent reads; no code changes.
>   - Answer: (a).
> - **Which texts carry the rule of the closer**
>   - Recommended: (a) change both `orchestration.md` and the skill `/hi` the same way.
>   - Answer: (a).
> - **How a sprint line closes when its Case updates no sprint page**
>   - Recommended: (a) it closes `[-] … · sprint · defer`, and the decision lines of the Case stand.
>   - Answer: (a).
> - **Which Estimate checks the new text**
>   - Recommended: (a) a new Estimate, `estimate-orchestration-closes-a-line-by-what-its-case-does`, read by hand at the Retro of this session.
>   - Answer: (a).
> - **What happens to the closing line of `estimate-hi-writes-frontier`**
>   - Recommended: (a) a sub-case replaces its Criterion whole, with the one false line changed and pointing to `orchestration.md`.
>   - Answer: (a).
> - **Change**
>   - Asked: the findings of `/pre-spec` on the Case as first ratified: the short form and the take-back sentence of `rule-orchestration`, the Criteria of `estimate-orchestration-takes-back-a-ratified-case` and `estimate-orchestration-defers-in-one-reply`, the backlog items the check does not judge, the reading of `estimate-hi-writes-frontier`, and `estimate-prespec-binds-a-sprint-line`.
>   - Taken: 991.1 gains the pairs on the short form and the take-back, and its text and `then` name what the check judges and how an open Insight ends. Cases 991.3 and 991.4 replace the two Criteria. 991.2 keeps its `read` line, which the check of the case file asks for, and the Retro of this session leaves the Estimate `pending`, since its `method` waits for the close of a sprint. The `context` says why `estimate-prespec-binds-a-sprint-line` stands.
> - **Change**
>   - Asked: the person agreed, at the confirmation of the findings of `/pre-spec`, that 991.2 also rewrites the `method` of `estimate-hi-writes-frontier` into the form `by hand, after the reply that acknowledges the opening Case of /sprint-open in the session after the close of a sprint: …`, with the same meaning and the event named before the colon, the Criterion and the task line unchanged.
>   - Taken: the `update` of 991.2 sets that `method` beside `status: pending`, and its `read` line stays.

### Case 991.1 — The agent closes a line by what its Case decides

> **given:**
> `rule-orchestration`: renders `vault/wiki/orchestration.md`, which sets the closers of a Frontier line.
> **＋** `rule-skill-hi`: renders `.claude/skills/hi/SKILL.md`, which repeats the closers.
> **＋** `estimate-orchestration-closes-a-line-by-what-its-case-does`: the new check of the closer of a line by a Case.
> **＋** `insight-frontier-line-closed-by-the-case-built-on-its-item`: the Insight this Case fixes.
> **＋** `rule-prespec`: its check judges the closers and does not change.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose lines close.
> **＋** `entity-sprint-<id>`: the sprint page that a Case on a sprint item updates.
> **＋** `vault/wiki/backlog.md`: the list of the backlog items.
> **＋** `raw/2026-11-01/2038/cases/case-992.md`: Case 992.2 changes `## The acknowledging reply` of `rule-orchestration`, the reply in which a line closes.

> **when:**
> In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/skills/hi/SKILL.md` from `rule-skill-hi`, the person ratifies a Case built on the item of a line of `raw/<date>/<hi HHMM>/frontier.md` with the source `sprint` or `backlog`.

> **then:**
> The agent closes the line `[x] … · case N` only when a decision line of Case N ends the item.
> **＋** A sprint item ends by Case N only when Case N or a sub-case updates the sprint page `entity-sprint-<id>`.
> **＋** An item of `vault/wiki/backlog.md` whose page carries `deferred_by` ends by Case N only when a decision line of Case N other than a `defer` names the page, and a Case among Case N and its sub-cases that names the page carries `{supersedes:case M}` for each Case M of the page's `deferred_by`.
> **＋** An open Insight of `vault/wiki/backlog.md` ends by Case N only when Case N or a sub-case updates the page of the Insight.
> **＋** A sprint line whose Case updates no sprint page closes `[-] … · sprint · defer`, and the decision lines of that Case stand.
> **＋** A backlog line whose Case defers its page again closes `[-] … · backlog · defer case N`. A backlog line whose Case neither ends the item nor defers it again closes `[-] … · backlog · kept`, and the decision lines of that Case stand.
> **＋** The agent closes the line in the reply that carries the decision lines of Case N, so the frontier check of `uv run --project .guppi guppi prespec --check` of `rule-prespec` finds nothing on it.
> **－** Any other backlog item ends by the ratification of Case N, and the check of `rule-prespec` judges the closers as before.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` `[x]` for an item ended: `· case N` when ratified, ``
>   - new: `` `[x]` for an item ended: `· case N` when a decision line of Case N ends the item, ``
>   - old: `for an item of the sprint left for later — no Case but`
>   - new: `for an item of the sprint left for later — no short Case of its own but`
>   - old: `` and `/pre-spec` reports the line otherwise (as set in case 937.2). ``
>   - new: `` and `/pre-spec` reports the line otherwise (as set in case 937.2). A Case built on an item ends it only by what its decision lines do: an item of the sprint by an `update` of the sprint page `entity-sprint-<id>` under the Case or a sub-case; an item of `backlog.md` whose page carries `deferred_by` by a line other than a `defer` that names the page, a Case among the Case and its sub-cases that names the page carrying `{supersedes:case M}` for each Case M of that `deferred_by`; an open Insight of `backlog.md` by an `update` of its page; and any other item by its ratification. Where no decision line ends the item, its line closes as the item put off — `[-] … · sprint · defer`, `[-] … · backlog · defer case N` or `[-] … · backlog · kept` — and the decision lines of the Case stand, since `/pre-spec` reports a sprint line, or a backlog line whose page carries `deferred_by`, closed `· case N` otherwise (as set in case 991.1). ``
>   - old: `` the line of its item in `frontier.md` changes in the same reply from `[x] … · case N` to the closer of its source put off ``
>   - new: `` the line of its item in `frontier.md` changes in the same reply, unless it already stands so, from the closer it stands with to the closer of its source put off ``
>   - old: `` An item of `backlog.md` left as it stands is no decision: no short Case, no ledger line, but for the short Case of a take-back, ``
>   - new: `` An item of `backlog.md` left as it stands is no decision of its own: no short Case and no ledger line of its own, but for the short Case of a take-back, ``
>   - change: `a line closes · case N only when a decision line of Case N ends its item; otherwise it closes as the item put off, the Case's lines standing; a take-back changes the line from the closer it stands with`
> - [ ] update `rule-skill-hi`
>   - old: `` `[x]` is an item ended: `[x] … · case N` when ratified, ``
>   - new: `` `[x]` is an item ended: `[x] … · case N` when a decision line of Case N ends the item, as `orchestration.md` sets it, ``
>   - old: `` left for a later session — no Case, no ledger line, no `deferred_by`, but ``
>   - new: `` left for a later session — no short Case and no ledger line of its own, no `deferred_by`, but ``
>   - old: `is left as it stands — no Case, no ledger line, but for`
>   - new: `is left as it stands — no short Case and no ledger line of its own, but for`
>   - old: `` a `C` that needs none closes `· work`. ``
>   - new: `` a `C` that needs none closes `· work`. A Case built on an item ends it only by its decision lines, as `orchestration.md` sets it: where none of them ends the item, its line closes as the item put off, and the decision lines of the Case stand (as set in case 991.1). ``
>   - change: `a line closes · case N only when a decision line of Case N ends its item; otherwise it closes as the item put off`
> - [ ] create `estimate-orchestration-closes-a-line-by-what-its-case-does`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the agent closes a Frontier line of a sprint or backlog item · case N only when a decision line of Case N ends the item, and otherwise closes it as the item put off with the decision lines of the Case standing`
>   - method: `by hand at Retro of the session that changes it: the new Render of rule-orchestration and of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow]`
> - [ ] update `insight-frontier-line-closed-by-the-case-built-on-its-item`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-991.1
>     ```
>   - change: `actioned: orchestration.md and the skill /hi state that a Case ends its item only by its decision lines`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] `uv run --project .guppi guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-orchestration-closes-a-line-by-what-its-case-does`

> **ratification:**
> ```
> - decision[case 991.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 991.1][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 991.1][create][estimate-orchestration-closes-a-line-by-what-its-case-does]{ref:rule-orchestration}{tags:session,workflow}
> - decision[case 991.1][update][insight-frontier-line-closed-by-the-case-built-on-its-item]{ref:insight-frontier-line-closed-by-the-case-built-on-its-item}
> ```

### Case 991.2 — The Frontier of /hi keeps the lines of a Case on an item put off

> **given:**
> `rule-skill-hi`: renders `.claude/skills/hi/SKILL.md`, which assembles and closes the Frontier.
> **＋** `estimate-hi-writes-frontier`: its Criterion is replaced whole.
> **＋** `vault/wiki/sprint.md`: the current milestone, a source of the Frontier.
> **＋** `vault/wiki/brief.md`: the Next session of the brief, a source of the Frontier.
> **＋** `vault/wiki/backlog.md`: the backlog, a source of the Frontier.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier the skill writes.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the case file of the opening Case of `/sprint-open`.
> **＋** `entity-sprint-<id>`: the sprint page whose `create` the opening Case writes.
> **＋** `/pre-spec`: finds an open line under `## Cases`.
> **＋** `vault/wiki/orchestration.md`: sets when a line closes `· case N` and the short Case of a take-back.

> **when:**
> The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md`, the output of the skill's commands and, in the session that opens a sprint, the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of the opening Case, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, closed `[x] … · case N` by the opening Case of `/sprint-open`; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone of `vault/wiki/sprint.md`, or, while that opening line stands, the items of the first milestone that the `create` of `entity-sprint-<id>` writes under `## Milestones` in the case file of the opening Case, with the source `sprint`; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** A line of the `Cases` of the brief's Next session that names the same item as a line of the current milestone makes no line of its own. The milestone line stands as the sprint page, or the opening Case, gives it, with the source `sprint` alone. The agent judges the sameness by meaning, with no page opened.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when a decision line of Case N ends it, as `vault/wiki/orchestration.md` sets it, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`. An item closed `defer` or `kept` gets no short Case and no ledger line of its own, but for the short Case of a take-back of a ratified Case, as `vault/wiki/orchestration.md` sets it. A Case built on that item and ratified keeps its decision lines, and a sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** When the first reply of `/hi` shows the Frontier, the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`, and a `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of `vault/wiki/sprint.md` is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** `/pre-spec` finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `estimate-hi-writes-frontier`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the reply that acknowledges the opening Case of /sprint-open in the session after the close of a sprint: the person's answer on whether the Frontier came out as the Criterion says, written into the estimate line; unit: the frontier findings of guppi prespec --check in .guppi/tests/test_prespec.py"
>     ```
>   - change: `the Criterion replaced whole — an item closed defer or kept gets no short Case and no ledger line of its own; a Case built on it keeps its decision lines; · case N only when Case N ends the item; the method names its event before the colon`
> - [ ] read `estimate-hi-writes-frontier`

> **ratification:**
> ```
> - decision[case 991.2][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```

### Case 991.3 — A take-back changes the line from the closer it stands with

> **given:**
> `rule-orchestration`: renders `vault/wiki/orchestration.md`, which sets the take-back of a ratified Case.
> **＋** `estimate-orchestration-takes-back-a-ratified-case`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger that holds the decision lines of the Case taken back.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose line changes.
> **＋** `raw/<date>/<hi HHMM>/cases/`: the folder of the case files.
> **＋** `.guppi/guppi/generate.py`: adds the short Case to the `deferred_by` of each page.
> **＋** `vault/wiki/backlog.md`: lists each page put off.
> **＋** `rule-spec-write`: its `Stop` hook writes the short Case and removes the Case taken back.
> **＋** `case-guppi`: the agent that is not dispatched for the short Case.
> **＋** `/pre-spec`: the step before and after which the reply ends differently.

> **when:**
> In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to take back a Case of the session that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, whole or one of its sub-cases.

> **then:**
> In the same reply the main agent shows a short Case of its own in the form of a deferred decision, with no dispatch of `case-guppi`, and carries its `LEDGER` block, with no tool call after it.
> **＋** The block holds one `defer` line for each rule, entity and insight page the Case taken back names, one for each Estimate it updates, and one for the page that each Estimate it updates checks or each Estimate it creates would check, once per page; each line carries `{supersedes:case N}` for the Case or sub-case taken back.
> **＋** At the librarian's run, `.guppi/guppi/generate.py` adds the short Case to the `deferred_by` of each rule, entity and insight page a `defer` line names, and each such page stands in `vault/wiki/backlog.md`, also when the Case taken back changed only existing Estimates.
> **＋** The `context` of the short Case names the Case taken back and each Estimate that Case creates; the person's words asking for the take-back are its ratification, and no question asks for it.
> **＋** The `Stop` hook of `rule-spec-write` writes the short Case under `## Deferred` and removes the Case taken back from the plan file.
> **＋** When no part of the Case stays in the plan, the line of its item in `raw/<date>/<hi HHMM>/frontier.md` changes in the same reply from the closer it stands with to `[-] … · sprint · defer` for an item of the sprint, `[-] … · backlog · kept` for an item of the backlog, or `[-] … · defer case M` of the short Case for any other source, and a line that already stands with that closer stays as it is.
> **＋** The reply ends as the reply that carries a defer: the Frontier with the line closed by that closer, then the question which open item is next, or before `/pre-spec` the question whether to go on to `/pre-spec`, or after `/pre-spec` no question.
> **－** The file of the Case taken back under `raw/<date>/<hi HHMM>/cases/` is not emptied, and no `case-guppi` undoes it.
> **－** In Work Mode no Case is taken back: the main agent tells the person that the ratified Case stands, and that a Case of a later session may replace it.

> **tasks:**
> - [ ] update `estimate-orchestration-takes-back-a-ratified-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a take-back changes the line from the closer it stands with, and a line already put off by that closer stays`
> - [ ] read `estimate-orchestration-takes-back-a-ratified-case`

> **ratification:**
> ```
> - decision[case 991.3][update][estimate-orchestration-takes-back-a-ratified-case]{ref:rule-orchestration}
> ```

### Case 991.4 — A short defer leaves the lines of a Case on an item put off standing

> **given:**
> `rule-orchestration`: renders `vault/wiki/orchestration.md`, which sets the short form of a deferred decision.
> **＋** `estimate-orchestration-defers-in-one-reply`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose line closes.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the ledger of the session.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: where Retro puts what it would put off.
> **＋** `rule-spec-write`: its `Stop` hook writes the short Case.
> **＋** `rule-prespec-onward`: its hook sends the agent on after `/pre-spec`.
> **＋** `case-guppi`: the agent whose Case is dropped before the defer.
> **＋** `estimate-orchestration-takes-back-a-ratified-case`: the moment of a take-back.
> **＋** `estimate-orchestration-shows-the-frontier-after-a-closed-line`: the moment of a line closed with no ratification and no defer.

> **when:**
> In Plan Mode, the person asks in the chat to put off a decision: an item of `raw/<date>/<hi HHMM>/frontier.md` whose source is neither the sprint nor the backlog, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** While a line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, a question follows the Frontier and ends the reply: which open item is next.
> **＋** When no line under `## Cases` is open before `/pre-spec`, the question whether to go on to `/pre-spec` follows the Frontier and ends the reply. The agent calls `/pre-spec` only after the person says to go on.
> **＋** When no line under `## Cases` is open after `/pre-spec`, no question follows: the reply ends with the Frontier, and the hook of `rule-prespec-onward` sends the agent on with the loop after the findings.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **＋** When the item has a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, the drop goes to that `case-guppi` first and the turn of the person's words ends with one `**Waiting:**` line; the short Case, its `LEDGER` block and the Frontier come in the turn that the answer `**Dropped:**` opens.
> **－** No text follows the question, or the Frontier when no question stands.
> **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line of their own but for the short Case of a take-back of a ratified Case, which is the moment of `estimate-orchestration-takes-back-a-ratified-case`, and the decision lines of a Case built on such an item and ratified stand. A reply that closes only such lines with no take-back and no ratification is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.

> **tasks:**
> - [ ] update `estimate-orchestration-defers-in-one-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an item put off or kept takes no short Case and no ledger line of its own, and the decision lines of a Case built on it stand`
> - [ ] read `estimate-orchestration-defers-in-one-reply`

> **ratification:**
> ```
> - decision[case 991.4][update][estimate-orchestration-defers-in-one-reply]{ref:rule-orchestration}
> ```
