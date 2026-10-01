## Case 568 — A recommend item may stay on the parent

> **context:**
> Each Case that `case-guppi` builds records the questions of its rounds in `recommend`. Each item gives a question, what was recommended and the person's answer. Since case 544.2, an item whose answer changed only one sub-case must stand under that sub-case's heading, and the others stand on the parent. `case-guppi` keeps the item on the parent anyway. The reading on ledger line 45 of session 2356 marked `estimate-case-build-records-the-rounds-in-recommend` failed for this. In Case 561, the question on what done means changed only 561.11, and its item stands on the parent. The file `raw/2026-10-01/1237/cases/case-567.md` repeats the fault: the question on whether the report still names every page changed only 567.1, and its item stands on the parent. A second read of Case 561 found more items on the parent that shaped one sub-case, such as the question on what blocks leaving Plan Mode and the question on how `/pre-spec` starts with no question. The person sees no problem in an item on the parent, and chose that the parent is allowed. An item whose answer changed only one sub-case may stand on the parent or under that sub-case. Every other item stands on the parent. No script checks the place, since either place is now correct. Cases 561 and 567 stay as ratified, because under the new rule nothing in them is misplaced.
>
> The rule stands in three sentences. One is in the Render of `rule-case-build`, and two are in the Render of `rule-case-protocol`: the `recommend` row of the sections table and the paragraph on splitting. This Case rewrites all three. The Criterion of `estimate-case-build-records-the-rounds-in-recommend` is replaced whole. The check of the answer noted that the old line on the place of an item is not carried. That line changes on purpose, to the new rule, and every other line is carried word for word. The `purpose` of the Estimate changes to match. The Estimate is set `pending` and is read again on the Cases of a later session.
>
> No reader in code changes. In `guppi/casecheck.py`, `recommend_titles` collects the item titles from every Case of the answer, so the check that each question has an item passes with the item in either place. In `guppi/materialize.py`, a sub-case never reads `recommend` from its parent, and a parent with sub-cases gets a record of its own that carries the parent's `recommend`. So an item on the parent lands on the parent's Decision page.
>
> No create is made, so the vault was not queried. Searches:
> - A Grep of ``changed only one sub-case|changed it alone|changed that sub-case alone|answer changed|own items|its own `recommend`|own recommend`` over the repository, leaving out `vault/raw/` and `vault/archive/`, printed eleven files: `vault/wiki/case-schema.md`, `brief.md`, `log.md`, `rule-decisions-schema.md`, `rule-case-protocol.md`, `rule-case-build.md`, `.claude/agents/case-guppi.md`, `estimate-case-build-records-the-rounds-in-recommend.md`, `estimate-case-protocol-case-form.md`, `decisions/schema.yaml` and `decision-case-459.md`. Of the hits outside `given`, `rule-decisions-schema` says that a sub-case's Decision page carries its own items and a parent's page the rest. That stays true, since the items a sub-case carries are its own. `decisions/schema.yaml` is rendered from that page. `estimate-case-protocol-case-form` says a sub-case has its own `recommend` when it has one, which stays true. The printed line of `decision-case-459` is about lint findings, and the page was not opened. `brief.md` and `log.md` were not read, and History lines were not read.
> - A Grep of `sub-case.{0,80}recommend|recommend.{0,80}sub-case` over `vault/wiki/estimates/` printed seven files: `estimate-case-build-records-the-rounds-in-recommend`, `estimate-case-check-requires-each-question-of-the-rounds`, `estimate-case-protocol-case-form`, `estimate-generate-writes-the-decision-page`, `estimate-materialize-assembles`, `estimate-spec-write-reaches-the-approved-spec` and `estimate-spec-write-copies-the-ratified-case`. All but the first copy, check or write a sub-case's `recommend` wherever it stands, so their Criteria stand.
> - A Grep of ``recommend` `` printed seven files over `vault/wiki/rules/`: `rule-case-check`, `rule-case-protocol`, `rule-case-build`, `rule-decisions-schema`, `rule-spec-write`, `rule-page-generation` and `rule-language`. Over `.claude/` it printed one file, `.claude/agents/case-guppi.md`. In `rule-case-check`, `rule-spec-write` and `rule-page-generation`, the sub-case passages copy or check a sub-case's `recommend` and set no place for an item, so they stand. `rule-language` holds no such passage.
>
> The other Estimates of `rule-case-build` and `rule-case-protocol` speak of other things: the frame, the round, the showing, the form of the Case and the loaded file. Their Criteria stand.

> **problem:**
> The rule that an item whose answer changed only one sub-case must stand under that sub-case asks `case-guppi` for a judgment it keeps missing, and the person sees no harm in the item standing on the parent. The question is where an item of `recommend` may stand in a Case with sub-cases.

> **recommend:**
> - **How do we stop answers being filed in the wrong place?**
>   - Recommended: (b) every question item goes on the parent, a sub-case carries only the Change items asked on it, and a script can refuse a question title under a sub-case.
>   - Answer: outside the options: simply allow `recommend` to be written on the parent, since the person sees no problem in it.
> - **What happens to the two Cases already ratified with misplaced entries?**
>   - Recommended: (a) leave them as they are; under the new rule nothing in them is misplaced.
>   - Answer: (a). Not answered in the first round, asked again.
> - **Must question entries stand on the parent, or may they stand there?**
>   - Recommended: (a) must, with no script check: every question item on the parent, a sub-case only with the Change items asked on it.
>   - Answer: (c) may: an item stands on the parent or under the one sub-case its answer changed, as `case-guppi` judges, and no script checks the place.

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render sets where an item of `recommend` stands
> **＋** `rule-case-protocol` — the Case schema, whose `recommend` row and splitting paragraph set the same
> **＋** `estimate-case-build-records-the-rounds-in-recommend` — the Estimate whose Criterion is replaced
> **＋** `.claude/agents/case-guppi.md` — the agent file rendered from `rule-case-build`
> **＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
> **＋** `guppi/casecheck.py` — constrains: compares the question titles with the items of every `recommend` of the answer

> **when:**
> `case-guppi` answers with a Case that has sub-cases, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> An item whose answer changed only one sub-case stands in the parent's `recommend` or in a `recommend` under that sub-case's heading.
> **＋** Every other item stands in the parent's `recommend`.
> **－** The check of `guppi/casecheck.py` refuses no item for the place it stands in, the parent or a sub-case.

> **tasks:**
> - [ ] update `rule-case-build` — an item may stand on the parent; a sub-case holds only items that changed it alone
>   - old: `` An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, the others in the parent's, and a sub-case carries no `problem` (case 544.2). ``
>   - new: `` An item may stand in the parent's `recommend` whatever its answer changed; an item whose answer changed only one sub-case may stand instead in a `recommend` under that sub-case's heading, and no other item stands there; a sub-case carries no `problem` (cases 544.2, 568). ``
>   - change: `an item of recommend may stand on the parent; a sub-case holds only items whose answer changed it alone (case 568)`
> - [ ] update `rule-case-protocol` — the same in the `recommend` row and in the splitting paragraph
>   - old: `a sub-case carries the items that changed it alone (case 544.2)`
>   - new: `an item may stand on the parent whatever it changed, and a sub-case carries only items whose answer changed it alone (cases 544.2, 568)`
>   - old: `` a sub-case carries its own `recommend` with the items whose answer changed that sub-case alone, the parent's `recommend` the rest (case 544.2) ``
>   - new: `` the parent's `recommend` may carry every item, and a sub-case may carry its own `recommend` with items whose answer changed that sub-case alone (cases 544.2, 568) ``
>   - change: `an item of recommend may stand on the parent; a sub-case holds only items whose answer changed it alone (case 568)`
> - [ ] update `estimate-case-build-records-the-rounds-in-recommend` — the Criterion replaced whole
>   - set: `{status: pending, purpose: "Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the recommendation and the answer in English as they stood when the person answered it, or a note that it was not answered — each item on the parent or under the one sub-case its answer changed, and a sub-case with no problem"}`
>   - change: `the Criterion replaced whole — an item whose answer changed only one sub-case may stand on the parent or under that sub-case (case 568)`
>   - sections.Criterion:
>     ```
>     When:
>     `case-guppi` answers with a Case, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.
>
>     Then:
>     The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, with a sub-item `Recommended:` with what the agent recommended and a sub-item `Answer:` with the person's answer in English, both as they stood when the person answered that question.
>     **＋** A later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer.
>     **＋** A question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it.
>     **＋** A question the person left unanswered is asked again in the next round under the same title; a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did.
>     **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
>     **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
>     **＋** An item whose answer changed only one sub-case stands in the parent's `recommend` or in a `recommend` under that sub-case's heading; every other item stands in the parent's `recommend`.
>     **＋** A Case with sub-cases carries `problem` on the parent only.
>     **－** No item quotes the person's words word for word.
>     **－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.
>     ```
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-build-records-the-rounds-in-recommend` — by hand, the Case files of a later session after the render, each `recommend` read against the rounds of its Case in the chat

> **ratification:**
> ```
> - decision[case 568][update][rule-case-build]{ref:rule-case-build}
> - decision[case 568][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 568][update][estimate-case-build-records-the-rounds-in-recommend]{ref:estimate-case-build-records-the-rounds-in-recommend}
> ```
