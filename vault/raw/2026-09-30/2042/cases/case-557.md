## Case 557 — `case-guppi` checks moments and searches, records each question as it was answered, and lists what a round decides

> **context:**
> `case-guppi` builds every Case from the instruction in `.claude/agents/case-guppi.md`, which is rendered from `rule-case-build`. Three readings of that instruction failed in session 1736, and the handoff carried each one on as a fix to decide. First, `estimate-case-build-checks-the-finished-case`: at `/pre-spec`, `ask-guppi` found three faults the builder's own check had missed. Case 547 widened the Frontier rule to cover the first reply of `/hi`, whose form `rule-skill-hi` sets. The builder's Grep for `Frontier` over `.claude/` printed `.claude/skills/hi/SKILL.md`, but only its passage on a later reply was judged, and the summary line of `rule-skill-hi` says nothing about the Frontier. Case 548 said a Grep found only the page and `brief.md`, while it printed `brief.md`, `log.md` and `rule-decisions-schema`. Case 552 listed the hits of `parse_line` without three of them. Second, `estimate-case-build-records-the-rounds-in-recommend`: the item of Case 549 on how the texts state the condition kept its first recommendation after the next question settled it the other way, which goes against the rule that asks for the latest one. Third, `estimate-case-build-writes-a-plain-round`: the sentence on what a first round decides ran parallel clauses inside one sentence on Cases 548 and 550, and the Context of Case 547 named five examples in one sentence. `.claude/skills/grill-me/SKILL.md` sets such a series one item per line. Case 551 put `rule-case-build` off over that third fault, so the page carries `deferred_by` and stands in `backlog.md`. The Frontier of this session names the three faults as its items C4, C6 and C9, and the person took all three into this Case. Its sub-case 557.3 decides the fault of Case 551 and carries `{supersedes:case 551}`, so the defer is retired and the page leaves the backlog. The Frontier lines come from the brief, not the backlog, so the check of `rule-case-check` on backlog lines does not apply. The rule stands `draft`.
> The Case was ratified, then built again after each of two reports of `ask-guppi` at `/pre-spec`. The first report raised four points. The new text of 557.1 had dropped the clause that a claim of `context` names the search it rests on, while its `then` kept it. The text now keeps it. The new text of 557.3 wrote a list shape of its own, against the line of `estimate-case-build-writes-a-plain-round` that asks the instruction to point each list to `.claude/skills/grill-me/SKILL.md` and word no shape of its own. The person chose to have the text name the two places and point to the template for the shape. `estimate-case-check-requires-each-question-of-the-rounds` asks that every question title of the rounds have an item in `recommend`, but 557.2 gave an item only to an answered question. The person chose that a question never answered still gets one item that says so, so that promise stands and is named in 557.2. The count of **＋** lines in the new Criterion of 557.1 was corrected. The second report found two more points. The `then` of 557.3 set every series of examples as a list, which is wider than `estimate-skill-grill-me-asks-in-rounds`, where a short series of words inside a sentence stays in it. That Estimate now stands in the `given` of 557.3, and the `then` says a series falls under the template's list rule like any other series. The text also said "when it has two or more parts", while the same paragraph already uses "part" for the parts of the Context. It now says "when it names two or more decisions". The second point was the list of hits of one Grep below, which had left out `entity-glossary`.
> This Case holds only `update` items, so no vault query ran. It adds no hook and changes no code. The hook of `rule-case-check` reads only the bold title of each `recommend` item, by `recommend_titles` in `guppi/casecheck.py`, which reads the top level of the list. So the sub-items that 557.2 sets need no old form in any reader. `tests/test_casecheck.py`, `tests/test_ratified.py` and `tests/test_generate.py` already write `Recommended:` and `Answer:` as sub-items. All five Estimates of `rule-case-build` were read. Two have their Criterion replaced whole. The new Criterion of 557.1 carries each old line word for word and adds two, so it holds seven **＋** lines. The new Criterion of 557.2 rewrites its first line and drops the line on the latest recommendation, as the person's choice sets, and carries its other lines word for word. `estimate-case-build-writes-a-plain-round` asks for a list one item per line in the Context, and for an instruction that points to the template, which the new text of 557.3 does. So it stands, stays `failed` until a reading after the render, and leaves what counts as a list to `estimate-skill-grill-me-asks-in-rounds`, which also stands. `estimate-case-build-writes-the-case` says the Context is one prose paragraph. That stays true, because a list inside it has been allowed since case 512. `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` speaks of readers in code and is not touched.
> Searches, outside `vault/raw/` and `vault/archive/`. A Grep for `Recommended:|both the latest|the latest recommendation|latest answer` printed 20 files: `case-schema.md`, `decisions/schema.yaml`, `.claude/agents/case-guppi.md`, `log.md`, nine Decision pages from `decision-case-547` to `decision-case-552.4`, `estimate-case-build-records-the-rounds-in-recommend`, `rule-case-build`, `rule-case-protocol`, `rule-decisions-schema` and the three tests above. The pages and renders among them enter 557.2, and `log.md` and the Decision pages were not read. A Grep for `[Rr]ecommend` over `vault/wiki/estimates/` printed 16 pages. Beyond the two Estimates of this Case and `estimate-case-check-requires-each-question-of-the-rounds`, each speaks of where `recommend` stands or how it is copied, not of what its items say. `estimate-case-protocol-case-form` points to the Sections table of `case-schema.md` and stays true. A Grep for `[Rr]ecommend|latest` over `glossary.md`, `vault/wiki/entities/`, `.claude/skills/`, `.claude/agents/` and `guppi/*.py` printed 12 files: `glossary.md`, `entity-glossary`, `.claude/skills/grill-me/SKILL.md`, `.claude/skills/wait-what/SKILL.md`, `.claude/agents/case-guppi.md`, `guppi/ratified.py`, `guppi/materialize.py`, `guppi/generate.py`, `guppi/casecheck.py`, `guppi/context.py`, `guppi/cleanup.py` and `guppi/archive.py`. The glossary rows name the section. The two skills speak of the recommended answer of a question. `ratified.py`, `materialize.py` and `generate.py` carry the section as text, and `casecheck.py` reads its titles. `context.py`, `cleanup.py`, `archive.py` and a docstring of `materialize.py` use "recommended" or "latest" in other senses. `case-guppi.md` is the render this Case changes. None of them is made false. A Grep for `judge them by meaning|names the search it rests on|search it rests on|by meaning` printed 27 files. Besides `rule-case-build`, its render and its Estimate, the live hits in `rule-ask`, `.claude/agents/ask-guppi.md`, `glossary.md`, `entity-glossary`, `rule-synthesis`, `.claude/agents/librarian-guppi.md`, `estimate-synthesis-clusters` and `estimate-ask-finds` speak of how `ask-guppi` and the synthesis compare pages. `brief.md`, `log.md` and 14 Decision pages were not read. A Grep for `rule-case-build` outside `vault/raw/`, `vault/archive/` and `vault/wiki/decisions/` printed 19 files. None of their lines states the check, the form of `recommend` or the Context of a round, except the pages this Case changes. `insight-case-form-chat-form-read-by-no-script`, near item C6, is about the main agent's own text before a round, which is item C5, and stays `open`.

> **problem:**
> The instruction of `case-guppi` does not tell it to look for other rules that act at the moment a change sets, and it does not tell it to report what a search printed, so faults reached `/pre-spec`. It asks a `recommend` item to give the latest recommendation even when a later question with its own title replaced it, which rewrites the record of the choice. It lets the Context of a first round run what the round decides and a series of examples inside one sentence, against the list rule of `grill-me`, and that fault holds the rule in the backlog.

> **recommend:**
> - **How does this Case stand next to the put-off rule and the two other items on it?**
>   - Recommended: (a) this Case alone, for the check only, with the put-off decision left for the Case on the plain-round item.
>   - Answer: (b) one Case for all three items on the rule, in sub-cases; the plain-round sub-case retires the put-off decision.
> - **Change**
>   - Asked: at the second pre-spec, the fix of the two points the report of `ask-guppi` found.
>   - Taken: `estimate-skill-grill-me-asks-in-rounds` stands in the `given` of 557.3, whose `then` puts a series of examples under the template's list rule like any other series; the text says "when it names two or more decisions"; the list of live hits of the Grep for `by meaning` in `context` names `entity-glossary`.

### Case 557.1 — `case-guppi` searches for rules at the same moment and reports what a search printed

> **recommend:**
> - **How should the check before a Case is shown be fixed?**
>   - Recommended: (a) sharpen the instruction on both points: search for rules that act at the moment the change sets, and report what a search printed; the Estimate's Criterion replaced to match.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render paragraph on the check of the finished Case changes
> **＋** `.claude/agents/case-guppi.md` — the render of `rule-case-build`, read by `case-guppi` at each dispatch
> **＋** `.claude/agents/ask-guppi.md` — the recipe whose index lines the check reads by meaning
> **＋** `vault/wiki/rules/` — the rule pages the check searches for the moment a change sets
> **＋** `.claude/` — the harness files the check searches for the same moment
> **＋** `estimate-case-build-checks-the-finished-case` — the promise of the check, its Criterion replaced whole

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one.
> **＋** Where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit.
> **＋** For a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands, and a claim of `context` about every text names the search it rests on.
> **＋** A claim of `context` about a search names its pattern and the paths it ran over, lists each file the search printed, a file it does not read included, or gives the count it printed, and claims nothing the search did not print.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. Each hit the change makes false enters the Case, or `context` says why it stands, and a claim of `context` about every text names the search it rests on. ``
>   - new: `` For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. When the change sets what happens at a moment — a reply, a hook event, a command — Grep `vault/wiki/rules/` and `.claude/` for the words that name that moment, read each passage of each hit that sets a form or a behaviour at that moment, and bound the Case so that it does not cover that moment, or name the other rule in `given` (case 557.1). Each hit the change makes false enters the Case, or `context` says why it stands, and a claim of `context` about every text names the search it rests on. A claim of `context` about a search names its pattern and the paths it ran over, and lists each file the search printed, a file it does not read included, or gives the count the search printed; it claims nothing the search did not print (case 557.1). ``
>   - change: `case-guppi searches the rules and .claude/ for the moment a change sets, and a claim of context about a search lists what the search printed (case 557.1)`
> - [ ] update `estimate-case-build-checks-the-finished-case`
>   - set: `{status: pending, purpose: "Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the rules that act at the moment the change sets, what each search printed, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec", method: "by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, a rule acting at the same moment that the Case misses, a claim of context that its search did not print, two sub-cases whose texts on one page contradict; the count of each in the reading line"}`
>   - change: `the Criterion replaced whole — the search for rules at the same moment, and a claim about a search that lists what it printed (case 557.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-checks-the-finished-case` — in a later session, at `/pre-spec` after the render

> **ratification:**
> ```
> - decision[case 557.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 557.1][update][estimate-case-build-checks-the-finished-case]{ref:estimate-case-build-checks-the-finished-case}
> ```

### Case 557.2 — `recommend` records each question as it was answered

> **recommend:**
> - **How should an item of `recommend` read when a later question replaced its recommendation?**
>   - Recommended: (b) each item keeps what was asked and answered at the time, with the title in bold and the sub-items `Recommended:` and `Answer:` as they stood when it was answered; a later question that replaced it is its own item; a question asked again is one item; a question the person left unanswered is asked again, and one never answered gets a short item that says so; `rule-case-protocol` and its render change too.
>   - Answer: the person proposed to record every answered question with its recommendation and answer as sub-items, asked how costly it is for `case-guppi` to place each item under its sub-case, and asked for an example first; after the example and the explanation, (b); a later question added the short item for a question never answered.
> - **What happens to a question that never got an answer, now that `recommend` holds only answered questions?**
>   - Recommended: (a) an unanswered question still gets a short item: its `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did; the check and its promise do not change.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render paragraph on how it writes `recommend` changes
> **＋** `.claude/agents/case-guppi.md` — the render of `rule-case-build`
> **＋** `rule-case-protocol` — its Render sets the form of `recommend` in the Sections table and the Language paragraph
> **＋** `vault/wiki/case-schema.md` — the render of `rule-case-protocol`, loaded by `/hi`
> **＋** `rule-decisions-schema` — its Render describes the `## Recommend` of a Decision page
> **＋** `vault/wiki/decisions/schema.yaml` — the render of `rule-decisions-schema`, read by `guppi lint`
> **＋** `estimate-case-build-records-the-rounds-in-recommend` — the promise of the record, its Criterion replaced whole
> **＋** `estimate-case-check-requires-each-question-of-the-rounds` — the promise of the hook of `rule-case-check` that each question title of the rounds has an item in `recommend`

> **when:**
> `case-guppi` answers with a Case, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, with a sub-item `Recommended:` with what the agent recommended and a sub-item `Answer:` with the person's answer in English, both as they stood when the person answered that question.
> **＋** A later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer.
> **＋** A question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it.
> **＋** A question the person left unanswered is asked again in the next round under the same title; a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did.
> **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
> **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
> **＋** An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, and the other items stand in the parent's `recommend`.
> **＋** A Case with sub-cases carries `problem` on the parent only.
> **－** No item quotes the person's words word for word.
> **－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` Write `recommend` as the schema sets it: one item per question of your rounds on the Case, its first line the title of the question in bold as the round wrote it, then a line `Recommended:` with what you recommended and a line `Answer:` with the person's answer in English, both the latest where a later question changed them; ``
>   - new: `` Write `recommend` as the schema sets it: one item per question of your rounds on the Case, its first line the title of the question in bold as the round wrote it, then a sub-item `Recommended:` with what you recommended and a sub-item `Answer:` with the person's answer in English, both as they stood when the person answered that question; a later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer; a question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it; a question the person left unanswered you ask again in your next round under the same title, and a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did (case 557.2); ``
>   - change: `recommend holds one item per question, its recommendation and answer as they stood when the person answered it, as sub-items; a question never answered says so (case 557.2)`
> - [ ] update `rule-case-protocol`
>   - old: `` one item per question of the rounds of `case-guppi` — the question, what it recommended, the person's answer in English, both the latest — one per change ``
>   - new: `` one item per question of the rounds of `case-guppi` — the question, what it recommended, the person's answer in English, both as they stood when the person answered it, or a note that it was not answered (case 557.2) — one per change ``
>   - old: `` `recommend` is a list, one item per question of the rounds: its first line the title of the question in bold as the round wrote it, then a line `Recommended:` and a line `Answer:`, the person's answer in English, both the latest where a later question changed them; ``
>   - new: `` `recommend` is a list, one item per question of the rounds: its first line the title of the question in bold as the round wrote it, then a sub-item `Recommended:` and a sub-item `Answer:`, the person's answer in English, both as they stood when the person answered that question; a later question that replaced an earlier one is an item of its own, a question asked in more than one round is one item, of the last round in which the person answered it, and a question never answered says so in its `Answer:` sub-item (case 557.2); ``
>   - change: `recommend holds one item per question, its recommendation and answer as they stood when the person answered it, as sub-items; a question never answered says so (case 557.2)`
> - [ ] update `rule-decisions-schema`
>   - old: `` one item per question of the rounds of `case-guppi` — the question, the latest recommendation, the person's latest answer — one per change ``
>   - new: `` one item per question of the rounds of `case-guppi` — the question, its recommendation and the person's answer as they stood when the person answered it, or a note that it was not answered (case 557.2) — one per change ``
>   - change: `## Recommend holds each question with its recommendation and answer as they stood when the person answered it (case 557.2)`
> - [ ] update `estimate-case-build-records-the-rounds-in-recommend`
>   - set: `{status: pending, purpose: "Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the recommendation and the answer in English as they stood when the person answered it, or a note that it was not answered — a sub-case with its own items and no problem"}`
>   - change: `the Criterion replaced whole — one item per question, its recommendation and answer as they stood when the person answered it, a question never answered noted (case 557.2)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] read `estimate-case-build-records-the-rounds-in-recommend` — in a later session after the render, the Case files against the rounds in the chat

> **ratification:**
> ```
> - decision[case 557.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 557.2][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 557.2][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 557.2][update][estimate-case-build-records-the-rounds-in-recommend]{ref:estimate-case-build-records-the-rounds-in-recommend}
> ```

### Case 557.3 — The Context of a first round treats what the round decides and a series of examples as lists

> **recommend:**
> - **How should the Context of a first round stop running a list inside one sentence?**
>   - Recommended: (a) name the two places, what the round decides when it has two or more parts and a series of examples, as lists; the shape is left to the `grill-me` template; the Criterion of `estimate-case-build-writes-a-plain-round` stands; this Case retires the put-off decision.
>   - Answer: agreed, (a); a later question set the wording to point to the template.
> - **How does the instruction name the two places in the Context without writing a list shape of its own?**
>   - Recommended: (a) name the two places and point to the template for the shape; the promise of a plain round stands and is read again after the render.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build` — the rule of `case-guppi`, whose Render paragraph on the Context of a first round changes
> **＋** `.claude/agents/case-guppi.md` — the render of `rule-case-build`
> **＋** `.claude/skills/grill-me/SKILL.md` — the template that sets what a list is and its shape
> **＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads what counts as a list, which stands
> **＋** `estimate-case-build-writes-a-plain-round` — the promise of a plain round, whose Criterion stands
> **＋** `decision-case-551` — the defer of `rule-case-build` that this sub-case retires

> **when:**
> `case-guppi` answers with a first round of questions on an item, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

> **then:**
> What the round decides, when it names two or more decisions, falls in the `**Context:**` under the list rule of `.claude/skills/grill-me/SKILL.md` like any other series.
> **＋** A series of examples in the `**Context:**` falls under the list rule of `.claude/skills/grill-me/SKILL.md` like any other series.
> **＋** `.claude/agents/case-guppi.md` names these two places and points to `.claude/skills/grill-me/SKILL.md` for the shape, with no shape of its own.
> **＋** The prose of the `**Context:**` goes on after a list.
> **－** What counts as a list stays as `estimate-skill-grill-me-asks-in-rounds` reads it.
> **－** The Criterion of `estimate-case-build-writes-a-plain-round` does not change.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `A list or a quotation in the context stands as the grill-me template sets it, and the prose goes on after it.`
>   - new: `A list or a quotation in the context stands as the grill-me template sets it, and the prose goes on after it; what the round decides, when it names two or more decisions, and a series of examples fall under the list rule of that template like any other series (case 557.3).`
>   - change: `what a first round decides and a series of examples in its Context fall under the list rule of grill-me; the defer of case 551 retired (case 557.3)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-writes-a-plain-round` — in a later session after the render, one first round and one later round of `case-guppi`

> **ratification:**
> ```
> - decision[case 557.3][update][rule-case-build]{ref:rule-case-build}{supersedes:case 551}
> ```
