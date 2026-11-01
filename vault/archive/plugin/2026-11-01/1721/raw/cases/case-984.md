## Case 984 — A change that keeps a check's answer makes no related Case

> **context:**
> When the main agent starts `case-guppi` for a Frontier item, its prompt names each related Case of the session by its id, one sentence on what it sets and which pages it changes, and the path of its case file, as `## Who builds a Case` of the Render of `rule-orchestration` sets it. Since case 938 a Case is related when it sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind. `estimate-orchestration-names-related-cases-in-the-dispatch` failed at the Retro of session 0141 (line 14 of `vault/raw/2026-11-01/0141/ledger.md`): the reading counted Case 977 as related to every later item, since it changed how `check_bare_links` of `/pre-spec` reads the prose of the plan, and the prompts of Cases 980 and 981 named it without its path, the second without its sentence. The main agent had judged Case 977 not related (the `context` of `vault/raw/2026-11-01/0141/cases/case-980.md`), and the `context` of `vault/raw/2026-11-01/0141/cases/case-977.md` says its change keeps the answer of that check on every input but a `[[schema]]` with a `schema.md` in a category folder, which no page holds. The handoff of session 0141 says that under a narrower reading of related the prompts of 980 and 981 would pass. The person chose to narrow the term: a Case whose change to a check leaves the answer of that check the same on each text the Case of the item may write is not related by that change, since what a builder needs to know is a check that may answer otherwise on its own text. The Render gains that limit by one `replace` pair, `vault/wiki/orchestration.md` changes at the librarian's render, and the Estimate gets a Criterion replaced whole with one more `－` line, its `purpose` set anew since it states the old promise, and a `method` that waits for the librarian's render of the new Render into `vault/wiki/orchestration.md` and then reads the prompts of the first session that runs on it, at its Retro. A finding of `/pre-spec` showed that a reading at the Retro of this session would read prompts written under the old text, since the new text lands only at the librarian's render after this session; the person chose to read it in the first session after the render. The method opens with `by hand, after` and names that event before a colon, so Retro leaves the Estimate `pending` until the event, as `case-schema.md` sets it (case 781). The schema of the rules, in `vault/wiki/rules/schema.yaml`, lets a rule of the agent's own conduct have its text in the context as its guard; the person chose no hook on the prompt, which the documentation of Claude Code hooks (https://code.claude.com/docs/en/hooks) says could block an `Agent` call and read its `prompt`. `rule-estimates-schema` keeps a `failed` Estimate as debt until a person decides; this Case is that decision. A Grep `may write text of that kind` over `vault/wiki/` printed `rules/rule-orchestration.md` (the Render and a History line), `orchestration.md`, `log.md` and `estimates/estimate-orchestration-names-related-cases-in-the-dispatch.md`; the Render line enters the Case by its pair, the rendered file follows the render, and the Estimate is replaced whole. A Grep `judges related` over `.claude/` printed `.claude/agents/case-guppi.md`, whose frame says the main agent judges which Cases are related; it stands, since the judgment stays with the main agent. In `.guppi/links.md` the block of `rule-orchestration` names `rule-case-build` and `entity-glossary` among its neighbours; a Grep `related` over `vault/wiki/glossary.md` printed nothing, so no row defines the term. `.guppi/tests/test_orchestration.py` reads the live `orchestration.md`, but only its blocks tagged `showing` and `defer`, which this Case does not change. The session's ledger holds no `lesson[error]` line, so no `addresses` mark is written.

> **problem:**
> The check of the prompt failed again on a Case whose change to a check altered nothing a later Case could write, because the term related counts every change to how a check reads a text.

> **recommend:**
> - **What settles the failed check?**
>   - Recommended: (a) narrow what related means: a change to a check that keeps its answer on each text the Case of the item may write makes no related Case; the Criterion replaced and read again at the Retro of this session.
>   - Answer: agreed, (a).
> - **When is the narrowed check read?**
>   - Recommended: (a) at the Retro of the first session that runs on the new text, after the librarian's render.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: its Render sets what the prompt of `case-guppi` names, rendered into `vault/wiki/orchestration.md`.
> **＋** `estimate-orchestration-names-related-cases-in-the-dispatch`: its Criterion is replaced whole.
> **＋** `case-guppi`: the agent the prompt starts.
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
> **－** A Case whose change to a check leaves the answer of that check the same on each text the Case of the item may write is not related by that change.
> **－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `` where the Case of the item may write text of that kind, such as the `method` of an Estimate that `uv run --project .guppi guppi check` reads, by its id ``
>   - new: `` where the Case of the item may write text of that kind and the change may alter what the check answers on such text, such as the `method` of an Estimate that `uv run --project .guppi guppi check` reads, by its id ``
>   - change: `a Case whose change to a check keeps the answer of that check on each text the Case of the item may write is not related by that change`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] update `estimate-orchestration-names-related-cases-in-the-dispatch`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names, acts at the same moment, or sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind and the change may alter what the check answers on it, by its id, one sentence on what it sets and which pages it changes, and the path of its case file, and each other Case of a batch of items the person took up in one answer"
>     method: "by hand, after the librarian's render of this Criterion's rule text into vault/wiki/orchestration.md: at the Retro of the first session that runs on that render, each Agent call of that session that dispatched case-guppi for the Case of an item, read in the transcript of the session under ~/.claude/projects/ against the Criterion, only the Cases the Criterion counts as related judged and a Case named beyond them not counted, a related Case left unnamed or named without its sentence, the pages it changes or the path of its case file counted in the reading line and the transcript named (the first session after 2026-11-01/1721)"
>     ```
>   - change: `the Criterion replaced whole — a change to a check that keeps its answer on each text the Case of the item may write makes no related Case; purpose and method set anew, the reading after the render`
> - [ ] read `estimate-orchestration-names-related-cases-in-the-dispatch`

> **ratification:**
> ```
> - decision[case 984][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 984][update][estimate-orchestration-names-related-cases-in-the-dispatch]{ref:rule-orchestration}
> ```
