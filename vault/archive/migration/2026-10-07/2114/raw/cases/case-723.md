## Case 723 — The take-back of a ratified Case without the faults pre-spec found

> **context:**
> In Plan Mode the person can take back a Case already ratified in the session. The main agent then writes a short put-off Case of its own, whose `defer` lines carry `{supersedes:case N}` and so retire the Case. It closes the Frontier line of the item by the closer of its source: `[-] … · sprint · defer` for a sprint item, `[-] … · backlog · kept` for a backlog item, and `[-] … · defer case M` for any other source. Case 713 of session 1804 set this in the Render of `rule-orchestration`. The pre-spec of that session found faults F2–F6 in it, and Case 721 put `rule-orchestration` and `rule-case-protocol` off for them. F2: the short-form paragraph, which the take-back reply follows, names only the closer `[-] … · defer case N`, which `guppi/prespec.py` reports after the source `sprint` or `backlog`. F3: one sentence says both that the `defer` lines of a take-back add to the source of a backlog item and that its source stays as it is. F4: a take-back of a Case whose only targets are existing Estimates leaves nothing in `backlog.md`, since `guppi/generate.py` marks `deferred_by` only on rule, entity and insight pages. F5: `rule-case-protocol` says that a Frontier line is closed again by the superseding Case, which a sprint or backlog closer does not name. F6: the Criterion of `estimate-orchestration-defers-in-one-reply` says that a sprint or backlog item takes no short Case.
>
> Case 723.1 fixes F2, F3 and F4 in the Render of `rule-orchestration` and replaces the Criterion of `estimate-orchestration-takes-back-a-ratified-case` whole, so that the take-back stands whole in this Case. It carries `{supersedes:case 713}`, which sets `decision-case-713` `superseded`, and `{supersedes:case 721}`, since `rule-orchestration` holds `decision-case-721` in `deferred_by` and `generate` clears a defer only from the pages the superseding Case names (case 467.3). The new Criterion rewords four lines of the old one on purpose. The `defer` line also names the page each updated Estimate checks. The line on the `context` of the short Case and the line on the person's words stand as one line. The line on the end of the reply names the closer of the source. Case 723.2 fixes F6: the last `－` line of the Criterion of `estimate-orchestration-defers-in-one-reply` is reworded on purpose to add the take-back as an exception, and Case 723.3 rewords the line of `estimate-hi-writes-frontier` on an item closed `defer` or `kept` in the same way. F5 stays: Case 722.3 of this session puts `rule-case-protocol` off again for that sentence, and a mark that retired 722.3 would remove its fix of the same page from the plan. The frame showed the same fault as F6 in `rule-skill-hi` and its check `estimate-hi-writes-frontier`, which the pre-spec of session 1804 did not find, and Case 723.3 fixes it. The `method` of that check waited for the `/hi` after the close of a sprint, which the check of the Case file refuses for a Criterion replaced whole (case 715). The person chose to keep that moment, with the reading by hand made the person's answer there, and the unit tests kept.
>
> A Grep of `no short Case|take no short Case|has no short Case` over `vault/wiki/**/*.md` and `.claude/**/*.md` printed `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/estimates/estimate-hi-writes-frontier.md`, `vault/wiki/rules/rule-orchestration.md` and `vault/wiki/estimates/estimate-orchestration-defers-in-one-reply.md`. The brief names F6, `orchestration.md` is the Render, and the other hits enter this Case. A Grep of `sprint · defer` over `vault/wiki/rules/*.md` and `.claude/**/*.md` printed `.claude/skills/hi/SKILL.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-skill-hi.md` and `vault/wiki/rules/rule-case-protocol.md`. The hit in `rule-case-protocol.md` is a History line. `SKILL.md` is the Render of `rule-skill-hi`. A Grep of `sprint · defer|backlog · kept` over `vault/wiki/estimates/` printed `estimate-hi-writes-frontier.md`, `estimate-hi-takes-a-conserved-spec.md`, `estimate-orchestration-takes-back-a-ratified-case.md`, `estimate-orchestration-shows-the-frontier-after-a-closed-line.md`, `estimate-orchestration-shows-the-built-case.md`, `estimate-orchestration-defers-in-one-reply.md`, `estimate-orchestration-acknowledging-reply.md` and `estimate-prespec-binds-a-sprint-line.md`. The ones this Case does not name stand. They list the closers, judge where a closer may stand, or speak of a reply that carries no defer or of a Case with no decision line, and none says that such a line has no short Case. A Grep of `take-back|taken back|takes back|take back` over `vault/wiki/` printed `orchestration.md`, `log.md`, `rules/rule-orchestration.md` and `estimates/estimate-orchestration-takes-back-a-ratified-case.md`, and over `.claude/` it printed nothing. No code reads the changed texts. `orchestration.md` and `.claude/skills/hi/SKILL.md` change at the librarian's render.

> **problem:**
> The take-back of a ratified Case, as Case 713 set it, gives two closers for one reply and holds a sentence that contradicts itself. It leaves nothing in the backlog when the Case taken back changed only existing Estimates. The check of the put-off reply and the rule of `/hi` with its check still say that a sprint or backlog item never takes a short Case.

> **recommend:**
> - **Does this Case retire last session's take-back decision?**
>   - Recommended: (a) retire it: this Case carries the retiring mark and restates the whole take-back rule.
>   - Answer: agreed, (a).
> - **What reaches the backlog when the Case taken back changed only existing checks?**
>   - Recommended: (a) also put off the page each changed check checks, once per page.
>   - Answer: agreed, (a).
> - **The fault in the Case schema that the C3 Case put off again**
>   - Recommended: (b) fix it here; the C3 Case drops its put-off.
>   - Answer: first agreed, (b); then (a), leave it out: Case 722 stays as first ratified, its put-off of `rule-case-protocol` for this sentence included, and this Case changes only `rule-orchestration`, its Estimates, and the rule of `/hi` with its Estimate.
> - **The same wrong sentence in the rule of `/hi` and its check**
>   - Recommended: (a) fix it here.
>   - Answer: agreed, (a).
> - **When the `/hi` check is read after its wording changes**
>   - Recommended: (b) keep the reading after the sprint close.
>   - Answer: (b); the check of the Case file then refused the kept `method`, and the question "How the `/hi` check is read, now that keeping its old reading is refused" replaced this one.
> - **How the `/hi` check is read, now that keeping its old reading is refused**
>   - Recommended: (b) the person's answer at the `/hi` after the sprint close, with the unit tests.
>   - Answer: agreed, (b).

### Case 723.1 — The take-back puts off the pages its checks check and closes by its source

> **given:**
> `rule-orchestration`: its Render sets the take-back of a ratified Case and the put-off reply.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-takes-back-a-ratified-case`: its Criterion is replaced whole.
> **＋** `rule-spec-write`: the hook that writes the short Case and removes the Case its mark names.
> **＋** `guppi/generate.py` and `vault/wiki/backlog.md`: a `defer` marks `deferred_by` only on rule, entity and insight pages, and `rule-backlog` lists them from it.
> **＋** `/pre-spec`: the check whose moment the question after the Frontier names.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the Frontier, the ledger and the file of a Case.

> **when:**
> In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the person asks in the chat to take back a Case of the session that has a decision line in `raw/<date>/<hi HHMM>/ledger.md`, whole or one of its sub-cases.

> **then:**
> In the same reply the main agent shows a short Case of its own in the form of a deferred decision, with no dispatch of `case-guppi`, and carries its `LEDGER` block, with no tool call after it.
> **＋** The block holds one `defer` line for each rule, entity and insight page the Case taken back names, one for each Estimate it updates, and one for the page that each Estimate it updates checks or each Estimate it creates would check, once per page; each line carries `{supersedes:case N}` for the Case or sub-case taken back.
> **＋** At the librarian's run, `guppi/generate.py` adds the short Case to the `deferred_by` of each rule, entity and insight page a `defer` line names, and each such page stands in `vault/wiki/backlog.md`, also when the Case taken back changed only existing Estimates.
> **＋** The `context` of the short Case names the Case taken back and each Estimate that Case creates; the person's words asking for the take-back are its ratification, and no question asks for it.
> **＋** The `Stop` hook of `rule-spec-write` writes the short Case under `## Deferred` and removes the Case taken back from the plan file.
> **＋** When no part of the Case stays in the plan, the line of its item in `raw/<date>/<hi HHMM>/frontier.md` changes in the same reply from `[x] … · case N` to `[-] … · sprint · defer` for an item of the sprint, `[-] … · backlog · kept` for an item of the backlog, or `[-] … · defer case M` of the short Case for any other source.
> **＋** The reply ends as the reply that carries a defer: the Frontier with the line closed by that closer, then the question which open item is next, or before `/pre-spec` the question whether to go on to `/pre-spec`, or after `/pre-spec` no question.
> **－** The file of the Case taken back under `raw/<date>/<hi HHMM>/cases/` is not emptied, and no `case-guppi` undoes it.
> **－** In Work Mode no Case is taken back: the main agent tells the person that the ratified Case stands, and that a Case of a later session may replace it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `one for each Estimate it updates, and one for the page that each Estimate it creates would check, once per page,`
>   - new: `` one for each Estimate it updates, and one for the page that each Estimate it updates checks or each Estimate it creates would check, once per page, so that each such page enters `backlog.md` through its `deferred_by` (case 723.1), ``
>   - old: `` then the Frontier with the line closed `[-] … · defer case N` and, last, ``
>   - new: `` then the Frontier with the line closed `[-] … · defer case N`, or, in the reply of a take-back, by the closer of its source that `## Showing and signing a Case` sets (case 723.1), and, last, ``
>   - old: `` whose item closes the same way and whose `defer` lines add to its source (case 713); its Frontier line closes `[-] … · backlog · kept`, its source stays as it is ``
>   - new: `` whose `defer` lines add the short Case to the `deferred_by` of each page they name (cases 713, 723.1); its Frontier line closes `[-] … · backlog · kept`, and, with no take-back, its source stays as it is ``
>   - change: `the take-back also puts off the page each updated Estimate checks, its reply closes the line by the closer of its source, and the source of a backlog item stays as it is only with no take-back (case 723.1)`
> - [ ] update `estimate-orchestration-takes-back-a-ratified-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the page each updated Estimate checks is put off too, and the reply closes the line by the closer of its source (case 723.1)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-takes-back-a-ratified-case`

> **ratification:**
> ```
> - decision[case 723.1][update][rule-orchestration]{ref:rule-orchestration}{supersedes:case 713}{supersedes:case 721}
> - decision[case 723.1][update][estimate-orchestration-takes-back-a-ratified-case]{ref:rule-orchestration}
> ```

### Case 723.2 — The check of the put-off reply names the short Case of a take-back

> **given:**
> `estimate-orchestration-defers-in-one-reply`: its Criterion is replaced whole.
> **＋** `rule-orchestration`: its Render sets the put-off reply.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`.
> **＋** `rule-spec-write`: the hook that writes the short Case into the plan file.
> **＋** `estimate-orchestration-takes-back-a-ratified-case` and `estimate-orchestration-shows-the-frontier-after-a-closed-line`: the checks of the moments this check leaves out.
> **＋** `/pre-spec` and `rule-prespec-onward`: the check whose moment the question after the Frontier names, and the hook that sends the agent on after it.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/handoff.md`: the Frontier, the ledger and the handoff of the session.

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
> **－** An item of the sprint put off, its line of `raw/<date>/<hi HHMM>/frontier.md` closed `[-] … · sprint · defer`, and an item of the backlog left as it stands, closed `[-] … · backlog · kept`, are not this moment: they take no short Case and no ledger line but for the short Case of a take-back of a ratified Case, which is the moment of `estimate-orchestration-takes-back-a-ratified-case`, and a reply that closes only such lines with no take-back is the moment of `estimate-orchestration-shows-the-frontier-after-a-closed-line`.

> **tasks:**
> - [ ] update `estimate-orchestration-defers-in-one-reply`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a sprint or backlog item takes no short Case but for the short Case of a take-back (case 723.2)`
> - [ ] read `estimate-orchestration-defers-in-one-reply`

> **ratification:**
> ```
> - decision[case 723.2][update][estimate-orchestration-defers-in-one-reply]{ref:rule-orchestration}
> ```

### Case 723.3 — The rule of `/hi` names the short Case of a take-back

> **given:**
> `rule-skill-hi`: its Render sets the closers of a Frontier line.
> **＋** `.claude/skills/hi/SKILL.md`: the file rendered from `rule-skill-hi`.
> **＋** `estimate-hi-writes-frontier`: its Criterion is replaced whole and its `method` set anew.
> **＋** `vault/wiki/orchestration.md`: the Render of `rule-orchestration`, which sets the take-back.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`: the sources of the Frontier.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier of the session.

> **when:**
> The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an open `W` line whose reading cannot run now, written by the reading step of `/hi`; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line, but for the short Case of a take-back of a ratified Case, as `vault/wiki/orchestration.md` sets it. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of the current milestone is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** Pre-spec finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` no Case, no ledger line, no `deferred_by`, never `· defer case N` (cases 310.5, 356.2) ``
>   - new: `` no Case, no ledger line, no `deferred_by`, but for the short Case of a take-back that `orchestration.md` sets, never `· defer case N` (cases 310.5, 356.2, 723.3) ``
>   - old: `left as it stands — no Case, no ledger line, it stays in the backlog`
>   - new: `` left as it stands — no Case, no ledger line, but for the short Case of a take-back that `orchestration.md` sets, it stays in the backlog (case 723.3) ``
>   - change: `a sprint item put off and a backlog item kept take no Case but for the short Case of a take-back (case 723.3)`
> - [ ] update `estimate-hi-writes-frontier`
>   - set:
>     ```
>     status: pending
>     method: "the person's answer at the /hi of the session after the close of a sprint, on whether the Frontier came out as the Criterion says, written into the estimate line; unit: the frontier findings of guppi prespec --check in tests/test_prespec.py"
>     ```
>   - change: `the Criterion replaced whole — an item closed defer or kept has no short Case but for the short Case of a take-back; the reading by hand is the person's answer at that /hi (case 723.3)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-writes-frontier`

> **ratification:**
> ```
> - decision[case 723.3][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 723.3][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```
