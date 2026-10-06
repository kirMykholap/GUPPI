## Case 681 — Items taken up together are shown as one batch

> **context:**
> In this session the person took up five backlog items in one answer. The main agent dispatched a `case-guppi` for each item at once. It then showed each answer alone as it came back: a round, then a built Case for ratification, then another round, while the other builders were still out. The person stopped it, because a batch form had been agreed: wait for every builder, show one list of the questions, and show every Case at once for one ratification. The main agent then took the steps of the batch of case 598.1 for Cases 676 to 680. It wrote a `**Waiting:**` line while builders were out, showed one list of every open question numbered `<Case id>.Q<n>`, with its own question on another Case among them as 676.Q1, and then showed all five Cases in one reply. That worked. The Render of `rule-orchestration` lets Cases be shown together only in the loop after the findings of `/pre-spec` (case 561.2) and in a batch that a change of a ratified Case opens (case 598.1). It says nothing of several items taken up in one answer, so its rule of one Case per reply applied. Session 1831 made the same error with two Cases, as `lesson-orchestration-two-cases-built-side-by-side` records. That lesson belongs to another session, so this Case carries no `{addresses:}` mark (case 284.2).
> The person chose five things. The batch opens when one answer of the person takes up two or more Frontier items. The question whether another Case is built again goes into the list of the batch, before any Case is shown. Only the text changes, and no hook is added. A new Estimate checks the change, beside the existing one. After the ratification the person changed the reading. The batch of Cases 676 to 680 would fail it, because 679, 677, 680 and 676 were shown one by one before the person stopped it. So the reading at Retro of this session reads the next batch in the transcript instead. That batch is Cases 682 and 683, taken up together after this Case was ratified, with this Case built again in the same batch. Cases 682 and 683 change `rule-ledger-write` and `rule-page-generation`, not `rule-orchestration`. Their files did not exist yet when this Case was built again. Three pairs of `replace` change the Render. In `## Plan Mode and the Frontier` the second trigger joins the sentence that names the batch. In `## Who builds a Case` the sentence on the question about another Case says where that question stands in such a batch. In `## Showing and signing a Case` a sentence on the new trigger stands before the steps of the batch, so those steps apply to both triggers. The first sentence of `## Plan Mode and the Frontier` names "a batch, as below", which now covers both triggers, so it stands.
> The frame. The `Stop` check of `rule-case-check` (`round_opening` in `guppi/casecheck.py`) accepts a reply that opens with a bold label that ends in a colon, such as `**Waiting:**`. In the one-by-one showing it refused a round that opened with the main agent's own sentence. That refusal is correct, and the batch replies of this session passed, so the code does not change. `estimate-orchestration-signs-a-batch-together` speaks of the batch, but its When is the change of a ratified Case. That trigger stays, and its last exception, that outside a batch and the loop the next item waits, stays true with the wider batch, so its Criterion stands. `estimate-orchestration-shows-the-built-case` says that a Case with a line `**Other Case:**` is shown as it stands and that the main agent asks whether the other Case is built again. It does not say when the question comes, so it stays true and stands. `estimate-orchestration-asks-in-the-grill-me-shape` sets the shape of that question, which does not change, and `estimate-orchestration-acknowledging-reply` already covers Cases shown together for one ratification, so both stand. `estimate-orchestration-loaded` promises only that the file equals the Render and is loaded, so it stands (case 378.5). The Render of `rule-prespec` says that inside its loop the rule of one Case at a time does not hold. That stays true. Its loop is not changed.
> The searches. A case-insensitive Grep of `shows one Case|one Case at a time|next Case until|one agent response` over `vault/wiki/`, without `log.md` and `brief.md`, printed `vault/wiki/orchestration.md`, `vault/wiki/rules/rule-orchestration.md` and `vault/wiki/rules/rule-case-protocol.md`. The hit in `rule-case-protocol` is a History line. The line "One agent response ≈ one Case." stays: the exceptions follow it. A case-insensitive Grep of `Waiting|one reply shows one Case|side by side` over `.claude/` printed `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/case-guppi.md`. The first is the loop of `rule-prespec`, which stands. The second is about the sub-cases that `case-guppi` reads side by side, which is not this moment. A Glob of `vault/**/*taken-together*` printed nothing, so the new slug is free. Cases 675 to 680 of this session close backlog items and change no page that this Case changes.

> **problem:**
> When the person takes up several Frontier items in one answer, nothing tells the main agent to wait for every builder and show the questions and the Cases together. So it shows each answer alone as it arrives.

> **recommend:**
> - **When does the batch form apply?**
>   - Recommended: (a) when the person's one answer takes up two or more Frontier items; an item taken up alone is still shown alone.
>   - Answer: agreed, (a).
> - **Where does the main agent's question about changing another Case go in a batch?**
>   - Recommended: (a) it joins the shared list of questions, numbered under the Case that raised it, before any Case is shown; on a yes the other Case joins the batch.
>   - Answer: agreed, (a).
> - **Does only the page enforce the batch form, or does a hook also enforce it?**
>   - Recommended: (a) only the page; no code changes.
>   - Answer: agreed, (a).
> - **Which check says the change is done?**
>   - Recommended: (a) a new Estimate, `estimate-orchestration-signs-items-taken-together`, beside the existing check, which stands.
>   - Answer: agreed, (a).
> - **How is the check read?**
>   - Recommended: (a) at Retro of this session, this session's own batch read in the transcript against the check.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: after the ratification, the person asked that the reading try the next two items taken up side by side, and agreed to the items for Cases 682 and 683.
>   - Taken: the `method` of `estimate-orchestration-signs-items-taken-together` now reads, at Retro of this session, the batch of Cases 682 and 683 with this Case built again, not the batch of Cases 676 to 680; `context` says why.

> **given:**
> `rule-orchestration`: the rule whose Render sets when Cases are shown together.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`, which `/hi` loads.
> **＋** `estimate-orchestration-signs-items-taken-together`: the new check of the batch of items taken up together.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose items the person takes up.
> **＋** `case-guppi`: the builder dispatched for each item.
> **＋** `rule-prespec`: the loop after the findings of `/pre-spec`, whose steps the batch takes.
> **＋** `rule-case-check`: the `Stop` check that lets the `**Waiting:**` line pass, unchanged.
> **＋** `estimate-orchestration-signs-a-batch-together`: the check of the batch that a change of a ratified Case opens, which stands.

> **when:**
> In Plan Mode before `/pre-spec`, one answer of the person takes up two or more items of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches a `case-guppi` for each item, and shows no round and no Case of them alone: they are one batch.
> **＋** While an answer of a `case-guppi` of the batch is out, the main agent ends each turn with one line that opens with the bold label `**Waiting:**`, translated, and names the Cases that have answered and those still out. It writes nothing else in the chat, and `rule-case-check` refuses no such reply.
> **＋** It shows one list of every round that came back, each question numbered `<Case id>.Q<n>`. It sends each answer to the `case-guppi` of its Case, all in one message, until every `case-guppi` of the batch has answered with its Case.
> **＋** A question whether another Case is built again, which a line `**Other Case:**` in a summary of the batch raises, stands in that list, numbered under the Case that raised it, before any Case of the batch is shown. On the person's yes, that other Case goes back to its `case-guppi` and joins the batch.
> **＋** It shows every Case of the batch in one reply, each in the showing that `vault/wiki/orchestration.md` sets, for one ratification. The person ratifies the batch at once or names the ids.
> **－** An item the person takes up alone is shown alone, and the next item waits until its Case is ratified or deferred.
> **－** The loop after the findings of `/pre-spec` stays as `rule-prespec` sets it.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` and in a batch, when the person's word asks that a Case already ratified change while another Case is built, as `## Showing and signing a Case` sets it (case 598.1). ``
>   - new: `` and in a batch, when the person's one answer takes up two or more items of the Frontier, or when the person's word asks that a Case already ratified change while another Case is built, as `## Showing and signing a Case` sets it (cases 598.1, 681). ``
>   - old: `` in a batch when it is ratified, as `## Showing and signing a Case` sets it (case 629.1); ``
>   - new: `` in a batch when it is ratified, as `## Showing and signing a Case` sets it (case 629.1); in a batch of items the person took up together, the question stands in the list of the batch before any Case of it is shown (case 681); ``
>   - old: `the two are a batch, and a Case that a Case of the batch asks to change in the same way joins it.`
>   - new: `` the two are a batch, and a Case that a Case of the batch asks to change in the same way joins it. When, before `/pre-spec`, the person's one answer takes up two or more items of the Frontier, the agent dispatches a `case-guppi` for each of them and shows no round and no Case of them alone: they are a batch too. A question whether another Case is built again, which the line `**Other Case:**` of a summary of that batch raises, stands in the list of its rounds, numbered `<Case id>.Q<n>` under the Case that raised it, before any Case of the batch is shown, and on the person's yes that other Case goes back to its `case-guppi` and joins the batch (case 681). ``
>   - change: `Frontier items taken up together in one answer are a batch: the questions in one list, every Case shown for one ratification (case 681)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`
> - [ ] create `estimate-orchestration-signs-items-taken-together`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether, when the person's one answer takes up two or more Frontier items, the main agent shows their rounds in one list and their Cases in one reply for one ratification, with the waits marked`
>   - method: `by hand at the Retro of session 2249: the replies in its transcript from the dispatch of Cases 682 and 683, taken up together with Case 681 built again, to the reply that acknowledged that batch, read against the Criterion`
>   - tags: `[session, workflow]`
> - [ ] read `estimate-orchestration-signs-items-taken-together`

> **ratification:**
> ```
> - decision[case 681][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 681][create][estimate-orchestration-signs-items-taken-together]{ref:rule-orchestration}{tags:session,workflow}
> ```
