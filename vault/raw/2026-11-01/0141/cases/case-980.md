## Case 980 — The dispatch that names related Cases is read again in this session

> **context:**
> When the main agent starts `case-guppi` to build the Case of a Frontier item, its prompt names each related Case of the session by its id, one sentence on what it sets and which pages it changes, and the path of its case file, as the dispatch paragraph of the Render of `rule-orchestration` sets it in `## Who builds a Case`. No code checks that prompt; only a reading of the transcript by hand does. `estimate-orchestration-names-related-cases-in-the-dispatch` failed at the Retro of session 0431 (line 46 of `vault/archive/plugin/2026-10-31/0431/raw/ledger.md`): the dispatch of Case 961 named the related Case 960 by its id and path, but its sentence named only the new Estimate of Case 960 and not the pages it changes. Cases 971 and 976 put the Estimate off, and it stands in `backlog.md`, put off in 2 sessions. `rule-estimates-schema` says a `failed` Estimate is debt until a human decides. The person chose to read it again in this session with the Render and the Criterion unchanged, since the text already asks for the pages and the failure was one prompt that left them out. So the `update` sets the Estimate `pending`, writes the Criterion back word for word as the `when` and `then` of this Case, and sets a new `method` that reads, at the Retro of this session, each dispatch of `case-guppi` in the transcript of session 0141, judging only the Cases the Criterion counts as related. The prompt of this very build names Case 979 with the page it changes and the path of its file, and names Cases 977 and 978 with their pages but no path; the main agent judged those two not related, so the method does not count a Case named beyond the related ones. The person also chose to set the `purpose` anew, since it named the id, the sentence and the path but not the pages, which are the part that failed. The decision line carries one `{supersedes:...}` mark for each of Cases 971 and 976, so both defers are retired. The Render of `rule-case-build`, the frame of `case-guppi`, names the related Case by its id, one sentence on what it sets and the path of its case file; it stands, since it sets what the builder reads, and the pages in the sentence serve the main agent's judgment and a builder that may not read the file of a Case built at the same time. In `.guppi/links.md` the block of the Estimate names `rule-orchestration`, `rule-case-protocol`, `rule-estimates-schema` and `estimate-where-to-stop-writes-each-step-whole`; the last three stand there only through the old Result, and none of their purpose lines speaks of the dispatch. A Grep for `names-related-cases` over `.guppi/tests/` printed nothing, so no test reads the page live, and a Grep for `one sentence on what it sets` over `.guppi/guppi/` printed nothing, so no code judges the prompt. The session's ledger holds no `lesson[error]` line, so no `addresses` mark is written.

> **problem:**
> The check that the dispatch names each related Case with the pages it changes failed once and has been put off twice, and its purpose line leaves out the pages that failed.

> **recommend:**
> - **What settles the failed check?**
>   - Recommended: (a) read it again in this session, with no text changed, both defers cleared.
>   - Answer: agreed, (a).
> - **Does the check's purpose line name the pages too?**
>   - Recommended: (a) rewrite the purpose in the same update.
>   - Answer: agreed, (a).

> **given:**
> `estimate-orchestration-names-related-cases-in-the-dispatch`: its `purpose` and `method` change, and its Criterion is written back word for word.
> **＋** `rule-orchestration`: the rule it checks, rendered into `vault/wiki/orchestration.md`.
> **＋** `case-guppi`: the agent the dispatch starts.
> **＋** `raw/<date>/<hi HHMM>/frontier.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the item and the case files the prompt names.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of an item of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** The prompt also names each Case of the session, ratified or already shown, that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind, such as the `method` of an Estimate.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** When the item is one of two or more items that one answer of the person took up, the prompt also names each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names, acts at another moment, sets no form of a text of a kind the Case of the item may write and is no Case of the same batch need not stand in the prompt.
> **－** A Case that only writes a text a check reads, and sets no form of it, is not related by that text alone.
> **－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

> **tasks:**
> - [ ] update `estimate-orchestration-names-related-cases-in-the-dispatch`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names, acts at the same moment, or sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind, by its id, one sentence on what it sets and which pages it changes, and the path of its case file, and each other Case of a batch of items the person took up in one answer"
>     method: "by hand, at Retro: each Agent call of the session that dispatched case-guppi for the Case of an item, read in the transcript of the session under ~/.claude/projects/ against the Criterion, only the Cases the Criterion counts as related judged and a Case named beyond them not counted, a related Case left unnamed or named without the pages it changes or the path of its case file counted in the reading line and the transcript named (the dispatches of session 2026-11-01/0141, the dispatch of Case 980 among them)"
>     ```
>   - change: `the method reads the dispatches of session 0141 at its Retro and the purpose names the pages of a related Case, the Criterion written back unchanged; the defers of cases 971 and 976 retired`
> - [ ] read `estimate-orchestration-names-related-cases-in-the-dispatch`

> **ratification:**
> ```
> - decision[case 980][update][estimate-orchestration-names-related-cases-in-the-dispatch]{ref:rule-orchestration}{supersedes:case 971}{supersedes:case 976}
> ```
