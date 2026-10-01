## Case 544 — case-guppi checks its finished Case, and its recommend records the rounds onto the Decision page

> **context:**
> `case-guppi` asks the person rounds of questions and then writes the Case from the answers and from its reading of the frame. The frame is the pages and files that the Case's `given` names. Two faults of this step were found only at pre-spec, each after ratification, and each cost a second ratification. In session 0248 the person chose an option saying that the brief of `/carry` lists no Cases, and the built Case took its Cases from the open lines of the Frontier (`lesson-case-build-built-case-departs-from-the-chosen-option`). The context of Case 534 said the Case changed all three texts that count the children of `rule-settings`, but the Purpose of `rule-hook-registry` held the same count (`lesson-case-build-frame-count-claimed-over-a-partial-search`). The frame reads only the pages that `given` names. Nothing compares the built Case with the options the person chose, and nothing holds those choices once the session ends: no vault file records the rounds, `recommend` stays in the Case file, and the Decision page carries only `## Problem`.
> The two lessons are the newest children of `insight-case-build-promise-lines-compared-by-no-check` and `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`. Both Insights are open in the backlog, each one reopened by its lesson after an earlier Case had actioned it (cases 472.3, 388). The first Insight also names a Criterion replaced whole that drops a line. The note of pre-spec from case 472 already covers that half, and 544.1 closes the half about the chosen option. The draft rule `rule-case-build-checks-its-sub-cases`, put off by case 480, asks for a side-by-side reading of the sub-cases that change one page before the Case is shown. The person took it up here. A Grep of `vault/wiki/` finds its slug only in `brief.md`, `backlog.md`, `log.md` and `decision-case-480`. The two lessons come from another session and get no mark. Setting each Insight `actioned` lets the cascade of `generate` archive its clustered lessons.
> The person asked that the rounds reach the Decision page, and that this stay one Case with the form of `recommend` rather than become a Case of its own. On the shown Case the person objected that some items of `recommend` showed an earlier recommendation that a later question had replaced, such as `## Note`. Each item now gives the latest recommendation and the latest answer, and 544.2 makes that the rule. Each question keeps its own item, so the check of 544.3 still finds every title.
> The frame gave these findings. `SPEC_SECTIONS` of `guppi/ratified.py` leaves `recommend` out of the Spec, so `materialize` never sees it. A parent Case has no ledger line and so no Decision page: there is no `decision-case-534`. The `decision` class of `guppi/lint.py` refuses a Decision page with no kind list. Its `origin` check looks for `[case N]` in the ledger, which a parent does not have. `guppi/materialize.py` fills a sub-case's `problem` and `recommend` from its parent and needs `problem` on every record. `generate` writes `## Context` for a record whose `case_text` has no `given`. A parent record carries the parent's `given` when the parent has one, and a record with `children` never gets `## Context`. `estimate-materialize-lifts-when-and-then` still holds, because a Case with its own `given` still carries it in its `case_text`, and a sub-case without one carries its parent's. The row `Decision page` of the glossary, the rule that bold is for section labels and operands only, and the sentences of `rule-case-protocol`, `rule-case-check` and `rule-decisions-schema` on `recommend`, the kind lists and the body of a Decision page would become false, so each gets a pair here.
> These Estimates speak of the change, and each one's Criterion is replaced whole: `estimate-spec-write-copies-the-ratified-case`, `estimate-spec-write-reaches-the-approved-spec`, `estimate-case-protocol-case-form`, `estimate-materialize-assembles`, `estimate-generate-writes-the-decision-page`, `estimate-decisions-schema-checked` and `estimate-lint-finds-a-broken-link`. The reading of `estimate-spec-write-reaches-the-approved-spec` on this session's Frontier then waits for a later session. The lines of these Criteria that are not carried word for word are the lines this Case changes on purpose. The then lines that the check found to share words across sub-cases name different pages and different promises. Some Estimates stand. `estimate-case-build-writes-the-case` stands, because case-guppi still reads each page `given` names, and the new checks are a new promise. `estimate-case-check-sends-back-a-faulty-case` stands, because the two new findings are sent back like any other. This session's cases 543.1 and 543.3 change `rule-case-build` and `rule-case-protocol`, and case 542 changes `rule-spec-write`. The pairs here touch other text.
> No reader needs an old form. The two new findings send a Case back to `case-guppi`, and nothing is lost. `materialize` never rewrites a `materialize.yaml`. Decision pages written before are not rewritten. This session's Spec was written by the old Spec hook and holds no `recommend`, so no page of this session gets `## Recommend`. If the code of 544.6 to 544.9 is built before the librarian's run, this session's pages do get the parent pages, `parent`, and sub-case pages with no `## Problem`. The full new shape starts with the Cases of the first session after the code is built. Every `create` carries a `ref`, so no vault query ran, and a Glob finds each new slug free.
> Not done: a similarity search by vectors, any judgment of what an answer says, and a hook that writes the rounds itself. The report of `ask-guppi` at pre-spec stays as a second net.

> **problem:**
> `case-guppi` can build a Case that departs from the option the person chose, and it can sign a claim about every text in the vault after reading only the pages it named. Two sub-cases of one Case can also contradict each other on one page. All three faults are found only at pre-spec, after ratification. The choices the person makes in the rounds are held by no page. The Decision page shows only the problem, and a Case with sub-cases has no page of its own.

> **recommend:**
> - **Where does the record of your choices go?**
>   - Recommended: the choices go into `recommend`, and a script carries it through the Spec onto the Decision page as `## Recommend`.
>   - Answer: agreed; one item per question, with the question, the agent's recommendation and the person's answer.
> - **How does the list reach the Decision page, and under what heading?**
>   - Recommended: through the Spec, lifted by `materialize` and written by `generate` under `## Recommend`.
>   - Answer: agreed.
> - **What heading does the list have on the Decision page?**
>   - Recommended: `## Recommend`.
>   - Answer: `## Recommend`.
> - **What does the Decision page of a sub-case show?**
>   - Recommended: the page of each sub-case carries only its own items, from a `recommend` of its own, and `parent` links it to the parent's page.
>   - Answer: agreed.
> - **Where does the parent's part go, and how are the pages linked?**
>   - Recommended: a Decision page for the parent with `## Problem`, its `## Recommend` and `children`, and `parent` on the page of each sub-case.
>   - Answer: agreed; `## Problem` stands on the parent's page only.
> - **How does a sub-case get its own items?**
>   - Recommended: a `recommend` of its own under each sub-case.
>   - Answer: a `recommend` of its own under each sub-case.
> - **Can a sub-case still write a `problem` of its own?**
>   - Recommended: no `problem` in a sub-case.
>   - Answer: no `problem` in a sub-case.

### Case 544.1 — case-guppi checks its finished Case before it answers

> **recommend:**
> - **How does the built Case keep to the option the person chose?**
>   - Recommended: the agent checks the finished Case against the chosen options before it answers.
>   - Answer: agreed.
> - **How is a claim about every text in the vault backed?**
>   - Recommended: a search of the vault by the slugs the change touches, plus the index lines.
>   - Answer: agreed.
> - **What does the search look for, and what does it cost?**
>   - Recommended: a search by the slugs the change touches, plus the index lines.
>   - Answer: that search; a similarity search by vectors is not built now.
> - **Is the put-off rule on sub-cases taken up in this Case?**
>   - Recommended: take it up.
>   - Answer: taken up; the check covers the whole Case with its sub-cases.
> - **Who checks the finished Case before you see it?**
>   - Recommended: a self-check by `case-guppi`, measured at pre-spec.
>   - Answer: agreed.
> - **What happens to the two open Insights?**
>   - Recommended: mark both as handled by this Case.
>   - Answer: agreed.

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the frame rendered from it
> **＋** `.claude/agents/ask-guppi.md` — the recipe of the index lines, judged by meaning
> **＋** `rule-case-build-checks-its-sub-cases` — the rule put off by case 480, taken up here
> **＋** `insight-case-build-promise-lines-compared-by-no-check` — the Insight of the departed option
> **＋** `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it` — the Insight of the claim wider than its search
> **＋** `estimate-case-build-checks-the-finished-case` — the promise this sub-case creates

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

> **then:**
> It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one.
> **＋** Where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
> **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit.
> **＋** For a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
> **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands, and a claim of `context` about every text names the search it rests on.
> **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `When no fork is open, answer with the Case in the chat form of the schema,`
>   - new:
>     ````
>     Before you answer with the Case, check it whole, its sub-cases with it. Put each option the person chose in your rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and fix the Case where it departs; where the frame shows after a round that a chosen option cannot hold as written, answer with a round on that point, never with a Case of another behaviour. For each page whose text the change makes false, Grep the live pages of `vault/wiki/` outside `decisions/`, and the code, for its slug, and read each hit that `given` does not name around the line of the hit; a hit in a History line, in `log.md` or in `brief.md` is not read. For a fact that no slug marks, read the index lines of the recipe of `.claude/agents/ask-guppi.md` and judge them by meaning. Each hit the change makes false enters the Case, or `context` says why it stands, and a claim of `context` about every text names the search it rests on. Read side by side the finished new texts of all your sub-cases that change one page, and fix a contradiction between them (case 544.1).
>
>     When no fork is open, answer with the Case in the chat form of the schema,
>     ````
>   - change: `case-guppi checks its finished Case before it answers: the chosen options, the pages that name a changed slug, the sub-cases on one page side by side (case 544.1)`
> - [ ] create `estimate-case-build-checks-the-finished-case`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi checks its finished Case before it answers — the chosen options, the pages that name a slug the change makes false, the sub-cases that change one page — counted by what ask-guppi still finds at pre-spec`
>   - method: `by hand: at /pre-spec of a later session after the render, the report of ask-guppi read for each Case case-guppi built — a Case that departs from a chosen option, a page naming a changed slug that the Case misses, two sub-cases whose texts on one page contradict; the count of each in the reading line`
>   - tags: `[session, workflow, harness]`
> - [ ] delete `rule-case-build-checks-its-sub-cases`
>   - impact: `its one sentence stands in the frame of rule-case-build; in vault/wiki/ only brief.md, backlog.md, log.md and decision-case-480 name it, and the supersede of case 480 retires that defer`
> - [ ] update `insight-case-build-promise-lines-compared-by-no-check`
>   - set: `{status: actioned, addressed_by: decision-case-544.1}`
>   - change: `actioned: the half on a replaced Criterion is closed by the note of pre-spec (case 472); case-guppi checks its finished Case against the options the person chose before it answers (case 544.1)`
> - [ ] update `insight-workflow-fact-signed-from-a-check-that-does-not-cover-it`
>   - set: `{status: actioned, addressed_by: decision-case-544.1}`
>   - change: `actioned: case-guppi searches the live pages for each slug the change makes false, and a claim about every text names its search (case 544.1)`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-checks-the-finished-case`

> **ratification:**
> ```
> - decision[case 544.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 544.1][create][estimate-case-build-checks-the-finished-case]{ref:rule-case-build}{tags:session,workflow,harness}
> - decision[case 544.1][delete][rule-case-build-checks-its-sub-cases]{ref:rule-case-build-checks-its-sub-cases}{supersedes:case 480}
> - decision[case 544.1][update][insight-case-build-promise-lines-compared-by-no-check]{ref:insight-case-build-promise-lines-compared-by-no-check}
> - decision[case 544.1][update][insight-workflow-fact-signed-from-a-check-that-does-not-cover-it]{ref:insight-workflow-fact-signed-from-a-check-that-does-not-cover-it}
> ```

### Case 544.2 — The recommend of a Case records the rounds

> **recommend:**
> - **What does one item of the new `recommend` hold?**
>   - Recommended: the question, what the agent recommended and the person's answer.
>   - Answer: agreed.
> - **Which questions stand in the list?**
>   - Recommended: one item per question with the latest recommendation and answer; a change to a shown Case is an item; a Case with no round has one item.
>   - Answer: agreed; an item must not show a recommendation that a later question replaced.

> **given:**
> `rule-case-build` — the rule whose Render is the frame of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the frame rendered from it
> **＋** `rule-case-protocol` — the schema of a Case, whose Render is `vault/wiki/case-schema.md`
> **＋** `vault/wiki/case-schema.md` — the schema rendered from it
> **＋** `estimate-case-build-records-the-rounds-in-recommend` — the promise this sub-case creates

> **when:**
> `case-guppi` answers with a Case, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

> **then:**
> The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, followed by a line `Recommended:` with what the agent recommended and a line `Answer:` with the person's answer in English.
> **＋** Where a later question changed the recommendation or the answer of an earlier one, the earlier item gives the latest recommendation and the latest answer.
> **＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
> **＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
> **＋** An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, and the other items stand in the parent's `recommend`.
> **＋** A Case with sub-cases carries `problem` on the parent only.
> **－** No item quotes the person's words word for word.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `Write no file and no ledger line.`
>   - new:
>     ````
>     Write `recommend` as the schema sets it: one item per question of your rounds on the Case, its first line the title of the question in bold as the round wrote it, then a line `Recommended:` with what you recommended and a line `Answer:` with the person's answer in English, both the latest where a later question changed them; one item `**Change**`, with a line `Asked:` and a line `Taken:`, for each change the person asked for on a Case you built; with no round, one item of a line `Recommended:` and the line `Answer: ratified as built`. An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, the others in the parent's, and a sub-case carries no `problem` (case 544.2). Write no file and no ledger line.
>     ````
>   - change: `case-guppi writes recommend as the record of its rounds, the latest recommendation and answer of each question, a sub-case with its own items and no problem (case 544.2)`
> - [ ] update `rule-case-protocol`
>   - old:
>     ````
>     | `recommend` | yes | The agent's suggestion. Not carried onto the Decision page. |
>     ````
>   - new:
>     ````
>     | `recommend` | yes | The record of the choices: one item per question of the rounds of `case-guppi` — the question, what it recommended, the person's answer in English, both the latest — one per change the person asked for on the shown Case, and, with no round, one item of the recommendation ratified as built; a sub-case carries the items that changed it alone (case 544.2). Carried onto the Decision page as `## Recommend` (case 544.7). |
>     ````
>   - old:
>     ````
>     `recommend` says the choice and why, the rejected option in one sentence (case 267).
>     ````
>   - new:
>     ````
>     `recommend` is a list, one item per question of the rounds: its first line the title of the question in bold as the round wrote it, then a line `Recommended:` and a line `Answer:`, the person's answer in English, both the latest where a later question changed them; a change the person asked for on the shown Case is an item `**Change**` with the lines `Asked:` and `Taken:`; a Case with no round has one item, a line `Recommended:` and the line `Answer: ratified as built` (case 544.2).
>     ````
>   - old: `bold is for section labels and operands only.`
>   - new:
>     ````
>     bold is for section labels and operands only, and for the title of a question of a round and the title of an item of `recommend`, as the grill-me template sets it (case 544.2).
>     ````
>   - old:
>     ````
>     `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing one there (case 60).
>     ````
>   - new:
>     ````
>     `context`, `problem`, `recommend` and a shared `given` live on the parent, and `materialize` reads a missing `context` or `given` there (case 60); `problem` stands on the parent only, and a sub-case carries its own `recommend` with the items whose answer changed that sub-case alone, the parent's `recommend` the rest (case 544.2).
>     ````
>   - old:
>     ````
>     The Case holds `context`, `problem`, `given`, `when`, `then`, the `then` block
>     ````
>   - new:
>     ````
>     The Case holds `context`, `problem`, `recommend`, `given`, `when`, `then`, the `then` block
>     ````
>   - old:
>     ````
>     `recommend` and `ratification` stay in the chat;
>     ````
>   - new:
>     ````
>     `ratification` stays in the chat (case 544.5);
>     ````
>   - change: `recommend is the record of the rounds and stands in the Spec, its item titles in bold; a sub-case carries its own items and no problem (cases 544.2, 544.5)`
> - [ ] create `estimate-case-build-records-the-rounds-in-recommend`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the latest recommendation, the latest answer in English — a sub-case with its own items and no problem`
>   - method: `by hand: the Case files of a later session after the render, each recommend read against the rounds of its Case in the chat`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-build-records-the-rounds-in-recommend`

> **ratification:**
> ```
> - decision[case 544.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 544.2][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 544.2][create][estimate-case-build-records-the-rounds-in-recommend]{ref:rule-case-build}{tags:session,workflow,harness}
> ```

### Case 544.3 — The Case check requires each question of the rounds in recommend

> **recommend:**
> - **Does a script check the form of the list?**
>   - Recommended: no check of the form, only a check that each question of the rounds is present.
>   - Answer: agreed.
> - **Can a hook write the questions and your answers into the Case?**
>   - Recommended: `case-guppi` writes the list, and the hook checks that no question is missing.
>   - Answer: that option.

> **given:**
> `rule-case-check` — the rule of the check of each answer of `case-guppi`
> **＋** `guppi/casecheck.py` — `uv run guppi casecheck --subagent`, the hook on `SubagentStop`
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `.claude/skills/grill-me/SKILL.md` — the question template whose title line the hook reads
> **＋** `rule-case-protocol` — the schema of a Case, whose Render is `vault/wiki/case-schema.md`
> **＋** `vault/wiki/case-schema.md` — the schema rendered from it
> **＋** `estimate-case-check-requires-each-question-of-the-rounds` — the promise this sub-case creates

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case, and `agent_transcript_path` holds the agent's earlier outputs with no Case heading, which are its rounds of questions on that Case.

> **then:**
> `uv run guppi casecheck --subagent` takes the title of each question of those rounds from its line `❓ **Q<n>** - **<title>**:`, the title line of the template of `.claude/skills/grill-me/SKILL.md`.
> **＋** A title that no item of a `recommend` of the top-level Case or of its sub-cases in the answer opens with, in bold, is a finding of the top-level Case that names the title, sent back and stored as any other finding.
> **－** An answer with no earlier round gives no such finding.
> **－** A title asked in more than one round is looked for once.
> **－** The words of an item after its title are not judged.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old:
>     ````
>     only their presence, their order and the script of the name, `context` and `problem` of a Case, by the language finding of pre-spec
>     ````
>   - new:
>     ````
>     only their presence, their order, the script of the name, `context` and `problem` of a Case, by the language finding of pre-spec, and the title of each item of `recommend` against the questions of the rounds (case 544.3)
>     ````
>   - old:
>     ````
>     An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored;
>     ````
>   - new:
>     ````
>     For an answer that holds a Case, it reads besides the earlier outputs of the subagent in `agent_transcript_path` that hold no Case heading — its rounds — and takes the title of each question from its line `❓ **Q<n>** - **<title>**:`; a title that no item of a `recommend` of the top-level Case or of its sub-cases in the answer opens with, in bold, is a finding of the top-level Case, sent back and stored as any other finding; a title asked in more than one round is looked for once, and the words of an item after its title are not judged (case 544.3). An answer with no Case heading, where no earlier output holds one either, is neither checked nor stored;
>     ````
>   - change: `the check of each answer of case-guppi requires the title of each question of its rounds in a recommend of the Case (case 544.3)`
> - [ ] update `rule-case-protocol`
>   - old: `no script judges them: the person does`
>   - new:
>     ````
>     no script judges their text but for the titles of the items of `recommend`, which the hook of `rule-case-check` compares with the questions of the rounds (case 544.3): the person does
>     ````
>   - change: `a script reads the titles of the items of recommend (case 544.3)`
> - [ ] create `estimate-case-check-requires-each-question-of-the-rounds`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of each answer of case-guppi sends back a Case whose recommend misses the title of a question of its rounds`
>   - method: `pytest tests/test_casecheck.py -k rounds over a temp agent transcript: a round and a Case whose recommend holds every title, one that misses a title, a title asked in two rounds, an answer with no round; then by hand the first Case the hook sends back for a missing title`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: the pattern of a question line, the rounds read from the earlier outputs in `agent_transcript_path`, the finding for a title missing from every `recommend` of the answer; the docstring says so
> - [ ] `tests/test_casecheck.py`: the cases of the method
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-check-requires-each-question-of-the-rounds`

> **ratification:**
> ```
> - decision[case 544.3][update][rule-case-check]{ref:rule-case-check}
> - decision[case 544.3][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 544.3][create][estimate-case-check-requires-each-question-of-the-rounds]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 544.4 — The Case check refuses a problem in a sub-case

> **given:**
> `rule-case-check` — the rule of the check of each answer of `case-guppi`
> **＋** `guppi/casecheck.py` — `form_findings`, the check of the chat form
> **＋** `tests/test_casecheck.py` — the tests of the hook
> **＋** `estimate-case-check-refuses-a-problem-in-a-sub-case` — the promise this sub-case creates

> **when:**
> `SubagentStop` fires when `case-guppi` answers with a Case that has sub-cases, and `uv run guppi casecheck --subagent` checks the chat form of each Case of the answer.

> **then:**
> A sub-case of the answer that carries a `problem` section is a finding of that sub-case from `form_findings` of `guppi/casecheck.py`, sent back to `case-guppi` and stored as any other finding.
> **＋** A parent that lacks `problem` still gets its finding of a missing section.
> **－** A Case with no sub-cases keeps its `problem` with no such finding.

> **tasks:**
> - [ ] update `rule-case-check`
>   - old:
>     ````
>     and that `ratification` holds one untagged fence of ledger lines and nothing else.
>     ````
>   - new:
>     ````
>     and that `ratification` holds one untagged fence of ledger lines and nothing else; a sub-case that carries `problem` is a finding of that sub-case, since `problem` stands on its parent only (case 544.4).
>     ````
>   - change: `a sub-case that carries problem is a finding of the check of the answer (case 544.4)`
> - [ ] create `estimate-case-check-refuses-a-problem-in-a-sub-case`
>   - ref: `rule-case-check`
>   - kind: `QA`
>   - purpose: `Whether the check of each answer of case-guppi sends back a sub-case that carries its own problem`
>   - method: `pytest tests/test_casecheck.py -k problem: a sub-case with problem, a parent without problem, a Case with no sub-cases`
>   - tags: `[hooks, harness, workflow]`
> - [ ] `guppi/casecheck.py`: `form_findings` gives the finding for a sub-case that carries `problem`; the docstring says so
> - [ ] `tests/test_casecheck.py`: the cases of the method
> - [ ] read `estimate-case-check-refuses-a-problem-in-a-sub-case`

> **ratification:**
> ```
> - decision[case 544.4][update][rule-case-check]{ref:rule-case-check}
> - decision[case 544.4][create][estimate-case-check-refuses-a-problem-in-a-sub-case]{ref:rule-case-check}{tags:hooks,harness,workflow}
> ```

### Case 544.5 — The Spec holds recommend

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case into the Spec
> **＋** `guppi/ratified.py` — `SPEC_SECTIONS` and the writer of a Case's section of the Spec
> **＋** `tests/test_ratified.py` — the tests of the hook
> **＋** `guppi/materialize.py` — `tagged_blocks` and `item_keys`, which read the written blocks back
> **＋** `guppi/casecheck.py` — the comparison of a showing with the stored answer, which the hook imports
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of the Case whose sending the hook reads
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of the session once it stands
> **＋** `estimate-spec-write-copies-the-ratified-case` — the promise whose Criterion this sub-case replaces

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads `<plan>.checked.json` beside the plan file for the answer of `case-guppi` stored under Case N, and the session's transcript for the `SendUserFile` calls on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and for the last earlier reply that shows Case N with at least one of its sections.

> **then:**
> The hook writes the stored answer of Case N into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then` as the answer holds them; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points; `ratification` is not written.
> **＋** A sub-case's own `recommend` is written under its heading, and the `context`, `problem` and `recommend` of its parent come from the parent's stored answer.
> **＋** Each of the two blocks opens and closes with a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least, which `tagged_blocks` of `guppi/materialize.py` reads back whole; the same fence rule holds for the blocks it writes into `raw/<date>/<hi HHMM>/spec.md` once it stands, and for the `then` block of a short-form defer under `## Deferred`.
> **＋** No `SendUserFile` call on the file of Case N made after the time the store holds for Case N: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A last showing of Case N that differs from the stored answer in a section it shows — by the one comparison `uv run guppi casecheck` makes on `Stop`, imported from `guppi/casecheck.py` — a store with no Case N, or a Case N stored with findings: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
> **＋** A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives the kind and the category of its item, or a value that holds a backtick in an outer span not padded on both sides, is refused: exit 2 with `` `<key>`: not a key of <kind> <slug> `` or `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
> **＋** No plan file in the event log, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys.
> **－** A reply with no showing of Case N is no refusal when the file of Case N was sent after the store.

> **tasks:**
> - [ ] update `rule-spec-write`
>   - old:
>     ````
>     the heading, `context`, `problem`, `given`, `when` and `then` as they stand,
>     ````
>   - new:
>     ````
>     the heading, `context`, `problem`, `recommend`, `given`, `when` and `then` as they stand — a sub-case's own `recommend` under its heading (case 544.5) —
>     ````
>   - old:
>     ````
>     the `context` and `problem` of a sub-case's parent come from the parent's stored answer
>     ````
>   - new:
>     ````
>     the `context`, `problem` and `recommend` of a sub-case's parent come from the parent's stored answer
>     ````
>   - change: `the Spec holds recommend (case 544.5)`
> - [ ] update `estimate-spec-write-copies-the-ratified-case`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Spec holds recommend, a sub-case's own under its heading (case 544.5)`
> - [ ] `guppi/ratified.py`: `SPEC_SECTIONS` holds `recommend`, and the writer writes a sub-case's own `recommend` and the parent's from the parent's stored answer; the docstring says so
> - [ ] `tests/test_ratified.py`: a Case whose `recommend` reaches the plan file, a sub-case with its own `recommend`, a parent's `recommend` from its stored answer
> - [ ] read `estimate-spec-write-copies-the-ratified-case`

> **ratification:**
> ```
> - decision[case 544.5][update][rule-spec-write]{ref:rule-spec-write}
> - decision[case 544.5][update][estimate-spec-write-copies-the-ratified-case]{ref:estimate-spec-write-copies-the-ratified-case}
> ```

### Case 544.6 — materialize gives a parent Case its own record

> **given:**
> `rule-materialize` — the rule of the lift of the ledger and the Spec into one yaml
> **＋** `guppi/materialize.py` — `INHERITED`, the decision record and its needed sections
> **＋** `tests/test_materialize.py` — the tests of the lift
> **＋** `estimate-materialize-assembles` — the promise whose Criterion this sub-case replaces

> **when:**
> `uv run guppi materialize` lifts the record lines of a unit's `ledger.md` against the `then` blocks of its `spec.md`.

> **then:**
> `materialize.yaml` holds one entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `addresses`, `origin`, `line`, `text`, `decision`; from the `then` item found by its slug — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented.
> **＋** `reword` is carried as a list of `{old, new}` pairs; a mapping or a scalar under it is `incomplete: [reword]`.
> **＋** An Estimate has its own line and its own entry, the `ref` of the line the Estimate itself; the entry of its `create` keeps `kind`, `purpose`, `method` and `tags` as fields.
> **＋** One decision record per Case: `decision`, `case_text`, `targets`; a sub-case reads a missing `context` and `given` from its parent, never `problem`, `recommend` or `when`, and carries `parent`, the `decision` of its parent.
> **＋** A Case whose sub-cases have decision lines in the unit gets one decision record of its own: its `decision` and its `origin` named by the id of the Case, `case_text` with its `context`, `problem` and `recommend`, and its `given` when it has one, `children` the `decision` of each of its sub-cases in ledger order, and no `targets`.
> **＋** An `estimate` line whose slug has a `create` in the same unit is folded into it; one for a page of an earlier unit is an `estimate` entry of its own.
> **＋** The `new_tags` of any Case reach the yaml once each; an existing `materialize.yaml` is extended with the lines it does not hold, never rewritten.
> **＋** A line the grammar does not parse goes under `unparsed`, and the run goes on.
> **－** No entry of an Estimate is derived from a key of the item of a rule or an entity: an Estimate comes only from its own line.
> **－** A sub-case record without `problem` carries no `incomplete: [problem]`.

> **tasks:**
> - [ ] update `rule-materialize`
>   - change: `a sub-case reads no problem or recommend from its parent; a parent Case gets a decision record of its own with children and its given when it has one (case 544.6)`
> - [ ] update `estimate-materialize-assembles`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a sub-case reads no problem or recommend from its parent, and a parent Case gets its own record (case 544.6)`
> - [ ] `guppi/materialize.py`: `INHERITED` holds `context` and `given`; a sub-case record carries `parent` and needs no `problem`; a parent Case with sub-case lines in the unit gets its own record with `children` and its `given` when it has one; the docstring says so
> - [ ] `tests/test_materialize.py`: a sub-case with no `problem` or `recommend` of its own, a parent record with `children` and no `targets`, with and without a `given` of its own, a Case with no sub-cases as before
> - [ ] read `estimate-materialize-assembles`

> **ratification:**
> ```
> - decision[case 544.6][update][rule-materialize]{ref:rule-materialize}
> - decision[case 544.6][update][estimate-materialize-assembles]{ref:estimate-materialize-assembles}
> ```

### Case 544.7 — generate writes the Recommend and the parent page

> **given:**
> `rule-page-generation` — the rule of the writer of pages
> **＋** `guppi/generate.py` — the writer of the Decision page
> **＋** `tests/test_generate.py` — the tests of the writer
> **＋** `guppi/materialize.py` — the writer of `materialize.yaml` and its decision records
> **＋** `vault/wiki/decisions/decision-case-<N>.md` — the Decision page it writes
> **＋** `estimate-generate-writes-the-decision-page` — the promise whose Criterion this sub-case replaces

> **when:**
> `uv run guppi generate` reaches the first entry of a Case in `materialize.yaml`, or a `decisions` record with no page yet.

> **then:**
> One page `vault/wiki/decisions/decision-case-<N>.md` is written: `case`, `status: current`, one list per kind present — `create`, `update`, `delete`, `defer` — the slugs in ledger order; `source` when a line carries one; `supersedes`; `origin`, `sprint`, `created`; `tags`, the union of the targets' tags; the body `## Problem` and `## Recommend` from `case_text` when it carries them, and `## Deferred` with one `### [[slug]]` per target of a `defer` line and its `purpose` verbatim.
> **＋** A record with `children`, a Case with sub-cases, gets its page before the pages of its sub-cases, with `children` their pages as quoted wikilinks, `tags` the union of theirs and no kind list; each page of a sub-case carries `parent`, its parent's page.
> **＋** A record with no `children` whose `case_text` carries no `given` — the short form of a deferred decision — also gets `## Context` from `case_text`, before `## Problem`.
> **＋** The page is written before the first entry of its lines, so their History lines name it.
> **＋** A `supersedes` sets the earlier page `superseded` and appends to its `superseded_by`. It removes the earlier slug from the `deferred_by` of each target of its `defer` list that a decision line of the superseding Case names; an empty `deferred_by` is dropped.
> **＋** A target of the earlier page's `defer` list that no decision line of the superseding Case names keeps the earlier slug in its `deferred_by`.
> **＋** An existing page is skipped; a `create` marked `exists` writes no page, but the Decision page of its Case is written.
> **＋** A record with `superseded_by` and no `case_text` gets a two-line body: `## Context` `Superseded by [[decision-case-M]] in its own session, before the Spec was approved; the Case left the Spec (case 299).`, `## Problem` `Decided under [[decision-case-M]].`
> **－** The page holds no `## Given`, no `## When` and no `## Criterion`, and no `## Context` when `case_text` carries `given` or the record carries `children`.
> **－** The Decision pages already written are not rewritten.
> **－** The page of a sub-case carries no `## Problem`, and a `case_text` with no `recommend` gives no `## Recommend`.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old:
>     ````
>     The Decision page of a Case is written before its entries and carries the body of every defer (cases 52.4, 186.1);
>     ````
>   - new:
>     ````
>     The Decision page of a Case is written before its entries and carries the body of every defer (cases 52.4, 186.1), and `## Recommend`, the `recommend` of the Case; a Case with sub-cases gets a page of its own before theirs, with `## Problem`, `## Recommend` and `children` and never `## Context`, and the page of each sub-case carries `parent` and no `## Problem` (case 544.7);
>     ````
>   - change: `the Decision page carries Recommend; a Case with sub-cases gets its own page, linked to theirs by children and parent (case 544.7)`
> - [ ] update `estimate-generate-writes-the-decision-page`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — Recommend on the page, a page for a parent Case with children and no Context, parent on a sub-case page and no Problem there (case 544.7)`
> - [ ] `guppi/generate.py`: the Decision page writes `## Recommend`; a record with `children` gets its page first, with no kind list and no `## Context`; a record with `parent` gets the field and no `## Problem`; the docstring says so
> - [ ] `tests/test_generate.py`: a page with `## Recommend`, a parent page with `children` and no `## Context`, with and without a `given` of its own, a sub-case page with `parent` and no `## Problem`, a short-form defer as before
> - [ ] read `estimate-generate-writes-the-decision-page`

> **ratification:**
> ```
> - decision[case 544.7][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 544.7][update][estimate-generate-writes-the-decision-page]{ref:estimate-generate-writes-the-decision-page}
> ```

### Case 544.8 — The Decision schema takes Recommend, parent and children

> **given:**
> `rule-decisions-schema` — the rule whose Render is the schema of a Decision page
> **＋** `vault/wiki/decisions/schema.yaml` — the schema rendered from it
> **＋** `guppi/lint.py` — the reader of the schema
> **＋** `tests/test_schemas.py` — the tests of the schemas
> **＋** `cases/case-<N>.md` — the Case file in the folder of a Decision's `origin`
> **＋** `estimate-decisions-schema-checked` — the promise whose Criterion this sub-case replaces
> **＋** `entity-glossary` — the page whose Render is the glossary, with the row `Decision page`
> **＋** `vault/wiki/glossary.md` — the glossary rendered from it

> **when:**
> `guppi render` writes `vault/wiki/decisions/schema.yaml` from `rule-decisions-schema`, and `guppi lint` reads a page of `vault/wiki/decisions/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, case, status, origin, sprint, created, tags`; optional `create, update, delete, defer, source, supersedes, superseded_by, parent, children`; values `status: current | superseded | archived`; the section `## History` required, `## Context`, `## Problem`, `## Recommend`, `## Given`, `## When`, `## Criterion`, `## Deferred`, `## Note` optional.
> **＋** A Decision page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list or lacking a required section has one finding per defect.
> **＋** A Decision page without `## Context`, and one without `## Problem`, has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds the introduction, the Slug, the fields deliberately absent and the body paragraph; `examples` holds the example page.
> **＋** The file says that the History of a Decision takes `created`, `superseded by` and one `updated:` line of a Case that signs its text after the fact.
> **＋** The file says that the Case file, `cases/case-<N>.md` in the folder of `origin` with N the id of the top-level Case, holds the whole Case and moves into the archive with its session; that a new page carries `## Context` only for a Case without `given` and without sub-cases, the short form of a deferred decision, and in the two-line body of a Case superseded in its own session; that it never carries `## Given`; and that the pages written before keep the sections they carry.
> **＋** The file says that a new page carries `## Problem` and `## Recommend` for a Case without sub-cases and on the page of a Case with sub-cases, which lists their pages in `children` in place of the kind lists; and that the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem`.
> **－** The example page holds no `## Context` and no `## Given`.

> **tasks:**
> - [ ] update `rule-decisions-schema`
>   - old: `optional: [create, update, delete, defer, source, supersedes, superseded_by]`
>   - new: `optional: [create, update, delete, defer, source, supersedes, superseded_by, parent, children]`
>   - old:
>     ````
>     required: ["## Problem", "## History"]
>       optional: ["## Context", "## Given", "## When", "## Criterion", "## Deferred", "## Note"]
>     ````
>   - new:
>     ````
>     required: ["## History"]
>       optional: ["## Context", "## Problem", "## Recommend", "## Given", "## When", "## Criterion", "## Deferred", "## Note"]
>     ````
>   - old:
>     ````
>     `recommend` — if the human accepted the proposal it became `Then`; if they changed it, `Then` holds the change. Either way the original stays in the Case file, `cases/case-<N>.md` in the folder of `origin` (case 513).
>     ````
>   - new:
>     ````
>     `recommend` — no field: the body carries it as `## Recommend` (case 544.8).
>     ````
>   - old:
>     ````
>     The body is the `problem` of the Case that produced it: the one paragraph a reader needs at the end of a link. The rest of the Case — `context`, `recommend`, `given`, `when`, `then`, `tasks`, `ratification` — stays in its Case file.
>     ````
>   - new:
>     ````
>     The body is the `problem` of the Case that produced it — the one paragraph a reader needs at the end of a link — and its `recommend`, the choices made in the rounds, under `## Recommend`. A Case with sub-cases has a page of its own with `## Problem`, the parent's `## Recommend` and `children`, and never `## Context`; the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem` (case 544.8). The rest of the Case — `context`, `given`, `when`, `then`, `tasks`, `ratification` — stays in its Case file.
>     ````
>   - old:
>     ````
>     A Case without `given`, the short form of a deferred decision, has no Case file, so its page keeps `## Context` as well;
>     ````
>   - new:
>     ````
>     A Case without `given` and without sub-cases, the short form of a deferred decision, has no Case file, so its page keeps `## Context` as well;
>     ````
>   - old: `a kind with no line is absent, at least one is present.`
>   - new:
>     ````
>     a kind with no line is absent, at least one is present but on the page of a Case with sub-cases, which carries `children` instead (case 544.8).
>     ````
>   - old:
>     ````
>     one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `create` lines
>     ````
>   - new:
>     ````
>     one of the four, or `children` on the page of a Case with sub-cases; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `create` lines
>     ````
>   - old:
>     ````
>     one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `update` lines
>     ````
>   - new:
>     ````
>     one of the four, or `children` on the page of a Case with sub-cases; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `update` lines
>     ````
>   - old:
>     ````
>     one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `delete` lines
>     ````
>   - new:
>     ````
>     one of the four, or `children` on the page of a Case with sub-cases; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `delete` lines
>     ````
>   - old:
>     ````
>     one of the four; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `defer` lines
>     ````
>   - new:
>     ````
>     one of the four, or `children` on the page of a Case with sub-cases; list of quoted wikilinks `"[[slug]]"`. The slugs of the Case's `defer` lines
>     ````
>   - old:
>     ````
>     optional; list of decision quoted wikilinks `"[[slug]]"`. Back-references, written by the script.
>     ````
>   - new:
>     ````
>     optional; list of decision quoted wikilinks `"[[slug]]"`. Back-references, written by the script.
>       parent: |
>         optional; a decision quoted wikilink `"[[slug]]"`. On the page of a sub-case, the page of its parent Case, written by the script (case 544.8).
>       children: |
>         optional; list of decision quoted wikilinks `"[[slug]]"`. On the page of a Case with sub-cases, the pages of its sub-cases in ledger order, written by the script; such a page carries `children` in place of the kind lists (case 544.8).
>     ````
>   - old:
>     ````
>     Written for a Case without `given`, the short form of a deferred decision, which has no Case file,
>     ````
>   - new:
>     ````
>     Written for a Case without `given` and without sub-cases, the short form of a deferred decision, which has no Case file,
>     ````
>   - old: `required. What required a decision. On a defer, what is unresolved.`
>   - new:
>     ````
>     optional. What required a decision. On a defer, what is unresolved. On the page of a Case without sub-cases and on the page of a Case with sub-cases; the page of a sub-case carries none (case 544.8).
>       "## Recommend": |
>         optional. The `recommend` of the Case as it stands: one item per question of the rounds of `case-guppi` — the question, the latest recommendation, the person's latest answer — one per change asked for on the shown Case, or the one recommendation of a Case with no round. On the page of a sub-case its own items, on the page of a Case with sub-cases the rest; absent on a short-form defer and on the pages written before case 544 (case 544.8).
>     ````
>   - change: `the Decision page carries Recommend; a Case with sub-cases has a page with children in place of the kind lists and no Context, a sub-case page carries parent and no Problem (case 544.8)`
> - [ ] update `estimate-decisions-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — Recommend, parent and children in the schema, Problem optional, Context never on the page of a Case with sub-cases (case 544.8)`
> - [ ] update `entity-glossary`
>   - old:
>     ````
>     body `## Problem`, `## Deferred` for a Case that put something off, and `## History`;
>     ````
>   - new:
>     ````
>     body `## Problem` and `## Recommend`, `## Deferred` for a Case that put something off, and `## History`; a Case with sub-cases has a page of its own with `## Problem`, `## Recommend` and `children`, and the page of a sub-case carries `parent`, its own `## Recommend` when it has one, and no `## Problem` (case 544.8);
>     ````
>   - old:
>     ````
>     `## Context` only for a Case without `given`, such as the short form of a deferred decision,
>     ````
>   - new:
>     ````
>     `## Context` only for a Case without `given` and without sub-cases, such as the short form of a deferred decision,
>     ````
>   - change: `the row Decision page names Recommend and the pages of a parent and a sub-case (case 544.8)`
> - [ ] `tests/test_schemas.py`: a Decision page without `## Problem` and with `## Recommend`, `parent` and `children` has no schema finding
> - [ ] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-decisions-schema-checked`

> **ratification:**
> ```
> - decision[case 544.8][update][rule-decisions-schema]{ref:rule-decisions-schema}
> - decision[case 544.8][update][estimate-decisions-schema-checked]{ref:estimate-decisions-schema-checked}
> - decision[case 544.8][update][entity-glossary]{ref:entity-glossary}
> ```

### Case 544.9 — lint takes the page of a parent Case

> **given:**
> `rule-lint` — the rule of the check of the live pages
> **＋** `guppi/lint.py` — the `decision` and `origin` classes
> **＋** `tests/test_lint.py` — the tests of lint
> **＋** `guppi/materialize.py` — `category_of`, the one table of the prefixes
> **＋** `vault/wiki/` — the live pages lint reads
> **＋** `vault/raw/` — the session folders whose ledgers an `origin` names
> **＋** `vault/archive/` — the archived pages and sessions
> **＋** `raw/<date>[/<HHMM>]/ledger.md#case-N` — the form of an `origin` that names a Case
> **＋** `decision-` — the prefix of the slug of a Decision page
> **＋** `estimate-lint-finds-a-broken-link` — the promise whose Criterion this sub-case replaces

> **when:**
> `uv run guppi lint` follows the links of the live pages under `vault/wiki/`.

> **then:**
> `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
> **＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
> **＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate.
> **＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
> **＋** An `origin` `#case-N` of a Case that has no ledger line of its own is found by a line of one of its sub-cases, `[case N.M]`.
> **＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer` and no `children`, or with `kind` or `target_slug`; a slug of its lists that `category_of` of `guppi/materialize.py` gives a category — the prefix `decision-` included — and that no live or archived page carries.
> **＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.
> **－** A `### case N` line under an Estimate's `## Criterion` is not read as a link.

> **tasks:**
> - [ ] update `rule-lint`
>   - change: `a Decision page with children and no kind list, and the origin of a parent Case found by a line of its sub-case, are no findings (case 544.9)`
> - [ ] update `estimate-lint-finds-a-broken-link`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the page of a parent Case: children in place of the kind lists, its origin found by a line of a sub-case (case 544.9)`
> - [ ] `guppi/lint.py`: the `decision` class takes a page with `children` and no kind list; `check_origin` finds `#case-N` by a line `[case N.` of a sub-case when no line carries `[case N]`; the docstring says so
> - [ ] `tests/test_lint.py`: a parent page with `children` and no kind list, a page with neither, a parent `origin` found by a sub-case line, one with no line of either
> - [ ] read `estimate-lint-finds-a-broken-link`

> **ratification:**
> ```
> - decision[case 544.9][update][rule-lint]{ref:rule-lint}
> - decision[case 544.9][update][estimate-lint-finds-a-broken-link]{ref:estimate-lint-finds-a-broken-link}
> ```

### Case 544.10 — The approved Spec holds recommend

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case into the Spec
> **＋** `guppi/ratified.py` — the writer of a Case's section of `spec.md`
> **＋** `tests/test_ratified.py` — the tests of the hook
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the approved Spec of the session
> **＋** `estimate-spec-write-reaches-the-approved-spec` — the promise whose Criterion this sub-case replaces

> **when:**
> The `Stop` hook `uv run guppi ratified` has written a ratified Case N from its stored answer into the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

> **then:**
> The hook writes the same stored answer of Case N into `spec.md`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
> **＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
> **＋** A task line whose text stood in a replaced section keeps the box it had there.
> **＋** The `context`, `problem` and `recommend` of a sub-case's parent, written into `spec.md` and into the plan file, come from the parent's stored answer, never from the reply.
> **－** Nothing written into `spec.md` is translated or refused for its language.
> **－** A refusal that writes nothing of Case N into the plan file writes nothing of it into `spec.md`.
> **－** On the re-fire (`stop_hook_active`) nothing is written: exit 0.

> **tasks:**
> - [ ] update `estimate-spec-write-reaches-the-approved-spec`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — spec.md holds recommend, the parent's from its stored answer (case 544.10)`
> - [ ] `tests/test_ratified.py`: tests whose names hold `approved_spec` — a Case whose `recommend` reaches `spec.md`, and a parent's `recommend` from its stored answer
> - [ ] read `estimate-spec-write-reaches-the-approved-spec`

> **ratification:**
> ```
> - decision[case 544.10][update][estimate-spec-write-reaches-the-approved-spec]{ref:estimate-spec-write-reaches-the-approved-spec}
> ```

### Case 544.11 — The form of the Case file takes recommend as a list

> **given:**
> `rule-case-protocol` — the schema of a Case, whose Render is `vault/wiki/case-schema.md`
> **＋** `vault/wiki/case-schema.md` — the schema rendered from it
> **＋** `rule-case-check` — its hook writes the Case file
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the Case file the person is sent
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing in the chat
> **＋** `estimate-case-protocol-case-form` — the promise whose Criterion this sub-case replaces

> **when:**
> The hook of `rule-case-check` writes a Case that `case-guppi` built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the main agent sends that file to the person, at its first showing or again.

> **then:**
> The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
> **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-case-protocol-shows-the-built-case`, and the reply ends with a plain question.
> **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
> **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.

> **tasks:**
> - [ ] update `estimate-case-protocol-case-form`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — recommend is the list of the schema, a sub-case with its own (case 544.11)`
> - [ ] read `estimate-case-protocol-case-form`

> **ratification:**
> ```
> - decision[case 544.11][update][estimate-case-protocol-case-form]{ref:estimate-case-protocol-case-form}
> ```
