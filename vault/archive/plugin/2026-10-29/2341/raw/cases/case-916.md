## Case 916 — A change left to an item with no Case yet waits for that item's Case

> **context:**
> When `case-guppi` builds a Case and finds that part of the work belongs to another Case, it writes a line `**Other Case:**` in its summary, and the main agent sends that other Case back with the change. `vault/wiki/orchestration.md` (`rule-orchestration`, `## Who builds a Case`) and `.claude/agents/case-guppi.md` (`rule-case-build`) set the line only for another Case of the session. In session 1930 the summary of Case 902 carried such a line that named Frontier item C7, which had no Case yet: the person had chosen in a round of 902 to leave the retirement of the defer of `decision-case-885` on `estimate-close-commits` to the Case of C7 (`vault/raw/2026-10-29/1930/cases/note-902.md`). No rule said what to do with it. The handoff of session 1930 says that the main agent showed 902 as it stood and passed the change into the prompt that later dispatched Case 903. The brief adds that the `method` of `estimate-orchestration-signs-items-taken-together` does not say whether such a line is the event it waits for.
>
> The person chose that the main agent keeps the change for the Case of the named item and puts it into the prompt that dispatches that item's `case-guppi`, so the person still chooses the order of the items, as the Frontier passage of `rule-orchestration` sets it: the reply ends with the question which open item is next. When the item ends with no Case of its own, the change goes back to the Case that wrote the line, with no question, and the person agrees or not at its showing, as for a line that names a Case (case 872.3). The two sides fail apart, so the Case splits: 916.1 sets what the main agent does on `rule-orchestration` with a new Estimate, and 916.2 sets the line and the dispatch prompt on `rule-case-build` with a new Estimate. 916.1 also sets the `method` of the two waiting Estimates of `rule-orchestration` to a line that names a Case of the session. That keeps the event each one waits for: the rule of case 781 on a part of a `method` that opens with `after` and names its event before a colon holds for both new texts. A Case taken back whole after it took the change puts its pages into `backlog.md` by the take-back of `rule-orchestration`; this Case adds nothing there.
>
> A Grep of `vault/wiki/` (Decision pages left out by the hook) and `.claude/` for `Other Case` printed `brief.md`, `orchestration.md`, `log.md`, `rules/rule-case-build.md`, `rules/rule-orchestration.md`, `estimates/estimate-orchestration-shows-the-built-case.md`, `estimates/estimate-orchestration-signs-items-taken-together.md`, `estimates/estimate-case-build-writes-the-case.md`, `estimates/estimate-case-build-reads-no-sibling-file-mid-send.md`, `insights/insight-subagents-read-a-sibling-mid-flight.md` and `.claude/agents/case-guppi.md`. The Criteria of `estimate-orchestration-shows-the-built-case` and `estimate-orchestration-signs-items-taken-together` speak of the other Case a line names and stay true for a line that names a Case of the session, so they stand, and only their `method` changes. The same holds for the Criterion of `estimate-case-build-writes-the-case`, whose line names another Case of the session, and for `estimate-case-build-reads-no-sibling-file-mid-send` and the insight, which speak of Cases built at the same time. The sentence of `rule-orchestration` on a batch (case 872.5) sends back the other Case a line names, and the description of the summary under `## Who builds a Case` sets the line only for another Case of the session; `/pre-spec` found both narrow (findings 1.3 and 1.4), and 916.1 widens each to the Case of a Frontier item that no Case of the session has built. When the person takes that item up in the same batch as the Case whose line names it, the `case-guppi` of the item is already out and its prompt has gone, so the change goes to that `case-guppi` by `SendMessage`, as the person agreed at `/pre-spec`. Line 23 of the Criterion of `estimate-orchestration-signs-items-taken-together` speaks of the other Case a line names; it stands, since its `method` now waits for a line that names a Case of the session, and the new Estimate checks a line that names an item, in a batch too. The Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch` sets which Cases are related by the pages they change or the moment they act at, and what the prompt holds for each (finding 2.3). The new clause names the Case that wrote the line in the prompt, with the change, even where it changes no page the item names. That Criterion only says that such a Case need not stand in the prompt, and its last `－` line holds only when no Case of the session is related. It lists what the prompt holds and forbids nothing more, so it stands, and `estimate-orchestration-passes-a-change-to-an-item-not-built` checks the change in the prompt.
>
> A Grep of `.guppi/tests/` for `orchestration\.md|case-guppi\.md|rule-orchestration|rule-case-build|signs-items-taken-together|shows-the-built-case` printed `test_onward.py`, `test_guppi_package.py` and `test_orchestration.py`. Only `test_orchestration.py` reads a live file, `vault/wiki/orchestration.md`, and it reads only the blocks tagged `showing` and `defer`, which this Case does not touch. A Grep of `.guppi/guppi/` for `Other Case` printed nothing, so no code judges the line. Case 915 of this session changes `rule-orchestration` under `## Writing the ledger lines` and `rule-case-build` after the sentence that ends with case 784; this Case changes other sentences, at the dispatch and the showing of a Case, so the two do not meet. The Glob `vault/wiki/estimates/estimate-*item-not-built*.md` printed nothing, so both new slugs are free. Both files change at the librarian's render after this session, so for the rest of the session the main agent works by the text that stands.

> **problem:**
> No rule says what the main agent does with an `**Other Case:**` line that names a Frontier item not yet built as a Case, so the change it names can be lost, and two Estimates do not say whether such a line is the event they wait for.

> **recommend:**
> - **What should the main agent do with an Other Case line that names a Frontier item not yet built as a Case?**
>   - Recommended: (a) keep the change for that item's Case: show the Case as it stands, and put the change into the prompt that dispatches the item's `case-guppi` when the person takes it up; `case-guppi` may name the item by its Frontier id.
>   - Answer: agreed, (a).
> - **What happens to the change when the named item ends with no Case?**
>   - Recommended: (a) send the change back, with no question, to the `case-guppi` of the Case that wrote the line; that Case is shown again, and the person agrees or not at that showing.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) two parts, each with a new check read at the Retro of this session against the new text in the Spec; the old checks stay as they are.
>   - Answer: agreed, (a).
> - **Should this Case also say what the two waiting checks wait for?**
>   - Recommended: (a) the `method` of `estimate-orchestration-shows-the-built-case` and of `estimate-orchestration-signs-items-taken-together` says that the line names a Case of the session.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: the person agreed to the fixes `/pre-spec` proposed: the change for a named item taken up in the same batch goes to that item's `case-guppi` by `SendMessage`; the description of the summary and the batch sentence of `rule-orchestration` cover a line that names such an item; `context` says why `estimate-orchestration-names-related-cases-in-the-dispatch` stands.
>   - Taken: 916.1 gains a `then` line and two `replace` pairs, its clause and the `purpose` of its new Estimate cover the batch, and `context` names the findings and why each Criterion stands.

### Case 916.1 — The main agent keeps the change for the named item, or sends it back

> **given:**
> `rule-orchestration`: renders `vault/wiki/orchestration.md`, which sets what the main agent does with an `**Other Case:**` line.
> **＋** `estimate-orchestration-passes-a-change-to-an-item-not-built`: the new check.
> **＋** `estimate-orchestration-shows-the-built-case`: its `method` names the line it waits for.
> **＋** `estimate-orchestration-signs-items-taken-together`: its `method` names the line it waits for.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose item the line names.

> **when:**
> In Plan Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, the summary of `case-guppi` carries, under the item of a Case, a line `**Other Case:**` that names an item of `raw/<date>/<hi HHMM>/frontier.md` by its id, an item that no Case of the session has built, and the change that item's Case needs.

> **then:**
> The main agent shows the Case as it stands, asks the person no question on the line, and sends no built Case back for it, in a batch too.
> **＋** When the person takes up the named item later, the prompt that dispatches its `case-guppi` names the Case that wrote the line, as a related Case, and the change the line names.
> **＋** When the person took up the named item in the same batch as the Case whose line names it, so that the `case-guppi` of the item is already out, the main agent sends the change to that `case-guppi` by `SendMessage`, and its Case stays in the batch.
> **＋** When the line of the named item in `raw/<date>/<hi HHMM>/frontier.md` closes with no Case of its own — put off, kept, closed as work, or its built Case dropped — the main agent, in the turn that closes it, sends the change by `SendMessage` to the `case-guppi` of the Case that wrote the line, with no question to the person.
> **＋** That Case is shown again when its `case-guppi` answers, in a batch while another Case of the session is out, and the person agrees or not at that showing.
> **－** When the Case that wrote the line is dropped or taken back before the item is taken up, the main agent passes the change to nobody.
> **－** A line `**Other Case:**` that names a Case of the session is handled as before.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` the change takes the way of Work Mode that `## Showing and signing a Case` sets (cases 629.1, 684.1, 872.3); ``
>   - new: `` the change takes the way of Work Mode that `## Showing and signing a Case` sets (cases 629.1, 684.1, 872.3); in Plan Mode a line `**Other Case:**` that names, by its id, an item of `frontier.md` that no Case of the session has built sends no built Case back, in a batch too: the Case that carries it is shown as it stands, with no question to the person, and the main agent keeps the change the line names and puts it into the prompt that dispatches the `case-guppi` of that item when the person takes it up later, beside the Case that wrote the line as a related Case, or, when the person took that item up in the same batch, so that its `case-guppi` is already out, sends the change to that `case-guppi` by `SendMessage`; when the line of that item closes with no Case of its own — put off, kept, closed as work, or its built Case dropped — the main agent, in the turn that closes it, sends the change by `SendMessage` to the `case-guppi` of the Case that wrote the line, with no question to the person, and shows that Case again when it answers, in a batch while another Case of the session is out, the person agreeing or not at that showing; and when the Case that wrote the line is dropped or taken back before the item is taken up, the change goes to nobody (as set in case 916.1); ``
>   - old: `` and, when its `context` says another Case of the session should change instead, a line `**Other Case:**`, ``
>   - new: `` and, when its `context` says another Case of the session, or the Case of a Frontier item that no Case of the session has built, should change instead, a line `**Other Case:**`, ``
>   - old: `` the other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, ``
>   - new: `` the other Case it names goes back to its `case-guppi` with the change the line names and joins the batch, and the change for a Frontier item of the batch whose Case is not yet built goes to the `case-guppi` of that item by `SendMessage`, ``
>   - change: `an Other Case line that names a Frontier item with no Case yet keeps its change for that item's Case, sends it to that item's case-guppi when the item is in the same batch, or sends it back to the Case that wrote it when the item ends with no Case`
> - [ ] create `estimate-orchestration-passes-a-change-to-an-item-not-built`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the main agent keeps the change that an Other Case line asks of a Frontier item with no Case yet for the prompt that dispatches that item's case-guppi, sends it to that case-guppi by SendMessage when the item is in the same batch, and sends it back to the Case that wrote the line when the item ends with no Case`
>   - method: `by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow]`
> - [ ] update `estimate-orchestration-shows-the-built-case`
>   - set:
>     ```
>     method: "by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec, read against the Criterion; after the first summary of case-guppi in Plan Mode that carries a line Other Case naming a Case of the session under that Render: the replies of the main agent from that summary to the showing of the other Case read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the method waits for a line Other Case that names a Case of the session`
> - [ ] update `estimate-orchestration-signs-items-taken-together`
>   - set:
>     ```
>     method: "by hand, after the first batch of items taken up together in Plan Mode under the new Render of rule-orchestration in which a summary carries a line Other Case naming a Case of the session: the replies of the main agent from the dispatch of the batch to the reply that acknowledged it read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the method waits for a line Other Case that names a Case of the session`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-passes-a-change-to-an-item-not-built`

> **ratification:**
> ```
> - decision[case 916.1][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 916.1][create][estimate-orchestration-passes-a-change-to-an-item-not-built]{ref:rule-orchestration}{tags:session,workflow}
> - decision[case 916.1][update][estimate-orchestration-shows-the-built-case]{ref:rule-orchestration}
> - decision[case 916.1][update][estimate-orchestration-signs-items-taken-together]{ref:rule-orchestration}
> ```

### Case 916.2 — case-guppi names the item not yet built, and its Case takes the change

> **given:**
> `rule-case-build`: renders `.claude/agents/case-guppi.md`, the agent that builds a Case and writes its summary.
> **＋** `estimate-case-build-names-an-item-not-built-on-the-other-case-line`: the new check.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier, whose item the line names.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of the Case, whose `context` names the item.

> **when:**
> In Plan Mode `case-guppi`, by `.claude/agents/case-guppi.md`, builds a Case that leaves a change to an item of `raw/<date>/<hi HHMM>/frontier.md` that no Case of the session has built, as a bound the person chose in a round.
> **＋** Or the main agent dispatches `case-guppi` for an item with a prompt that holds a change an `**Other Case:**` line of another Case of the session asks of that item.

> **then:**
> `case-guppi` writes into `context` the Frontier id of that item and what its Case must do, and its summary repeats both on a line `**Other Case:**` under the item of its own Case.
> **＋** Dispatched with such a change, `case-guppi` takes it into the Case of the item, or answers with a round where it opens a fork, and the `context` names the Case that asked it.
> **－** For a clash with another Case of the session, `case-guppi` keeps the form `.claude/agents/case-guppi.md` sets today.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `in Work Mode it asks the person first (cases 637.2, 645.1, 872.3).`
>   - new: `` in Work Mode it asks the person first (cases 637.2, 645.1, 872.3). Where, in Plan Mode, your Case leaves a change to an item of the Frontier that no Case of the session has built, as a bound the person chose in a round, name in `context` the item by its Frontier id and the change it needs, and again on a line `**Other Case:**` under the item of your Case in the summary that names the item by that id; the main agent keeps the change for the Case of that item, or sends it back to you when the item ends with no Case. Where your prompt holds a change that an `**Other Case:**` line of another Case of the session asks of your item, take it into your Case, or answer with a round where it opens a fork, and name in `context` the Case that asked it (as set in case 916.2). ``
>   - change: `case-guppi names a Frontier item with no Case yet on the Other Case line, and the Case of that item takes the change its prompt carries`
> - [ ] create `estimate-case-build-names-an-item-not-built-on-the-other-case-line`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi names a Frontier item with no Case yet, by its id and the change it needs, on the Other Case line of its summary, and takes into the Case of an item the change its prompt carries from such a line`
>   - method: `by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-names-an-item-not-built-on-the-other-case-line`

> **ratification:**
> ```
> - decision[case 916.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 916.2][create][estimate-case-build-names-an-item-not-built-on-the-other-case-line]{ref:rule-case-build}{tags:session,workflow,harness}
> ```
