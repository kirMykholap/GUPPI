## Case 651 — orchestration.md names the summary of case-guppi and shows by tested examples the forms the main agent writes

> **context:**
> `orchestration.md` tells the main agent what to do in a session. It still calls the reply of `case-guppi` "the answer", from the time that reply held the whole Case. Since case 645, `case-guppi` writes the Case into its file and replies with a summary: the path, and for each Case its id, name, Estimate and ledger lines in a plain fence. Now "the answer" can mean the summary, the file or the text the check stored. The page also leaves out two exact forms that the checks read. It says that the `ratification` of a showing holds the ledger lines "as the answer holds them". The `Stop` check reads only the quote block under `> **ratification:**`, so in session 1834 of 2026-10-02 the main agent put the fence outside the quote and the check refused the showing (`lesson-case-showing-ratification-fence-outside-the-blockquote`). The page says the `then` block of a short-form defer carries "slug, type and purpose". The hook of `rule-spec-write` reads only a list of items, so in session 0109 of 2026-10-05 a single mapping was refused twice (`lesson-orchestration-short-defer-then-block-written-as-a-mapping`). Both lessons are children of `insight-workflow-case-schema-silent-on-what-the-scripts-accept`. Case 646 left that Insight open until a later Case covered the forms the main agent writes.
>
> The person chose the following. Each meaning gets its own word: the summary, the file, and the text the check stored. Only `orchestration.md` changes. The two forms are shown by examples that a test runs the checks over, as case 646 did for `case-schema.md`. Only the two forms of the lessons are covered. The work is three sub-cases. The tests skip until the librarian's render. The example of a showing is a parent with two sub-cases, and its heading is in English because the page is documentation. The Insight is set `actioned` by this Case. A Grep of `answer` over `vault/wiki/rules/rule-orchestration.md` counted 8 lines. The hits on lines 38, 42, 44 and 46 that name a reply of `case-guppi`, the file it writes, or what the check stored from that file enter Case 651.1 as fourteen `replace` pairs, the first reply on an item from which a round may come among them. Line 32 names the person's answer and line 56 the main agent's answer to a refusal, so they stand. Lines 84 and 94 are History. The other hits on lines 38 and 46 name the person's answers, `case-guppi` answering as a verb, or the recommended answer of a question, the option a round recommends, and they stand.
>
> What the frame showed. `estimate-orchestration-shows-the-built-case` already calls the reply "the summary" and reads the showing that the new words describe, so it checks 651.1 and its Criterion stands. `estimate-orchestration-defers-in-one-reply` speaks of "a fence tagged `then` with one `defer` item per target", which the example of 651.3 bears out, so it stands. `estimate-orchestration-signs-a-batch-together` keeps its own words "an answer of a `case-guppi`", which the new page text does not make false, and `estimate-orchestration-forwards-a-discussion-question` keeps "the answer" for the `**Fact:**` reply the page now calls "that reply", with the same meaning. `estimate-prespec-gathers-the-answers-after-findings` sets the loop of `rule-prespec` whose steps the batch sentence of `orchestration.md` takes, which 651.1 rewords. Its words "while an answer is out" and "until every `case-guppi` it sent has answered with its Case" keep their meaning beside the new words of the page. Its line on "the showing that `vault/wiki/orchestration.md` sets" stays true, and that is the showing the example of 651.2 shows. So its Criterion stands. `estimate-guppi-tests-green` says that a skipped test is not a failure, so `make test` stays green while the new tests of `tests/test_orchestration.py` skip, and it stands. `estimate-orchestration-loaded`, `estimate-case-protocol-loaded` and `estimate-ratification-loaded` say that no paragraph of `orchestration.md` repeats one of `case-schema.md` or `ratification.md`. The new paragraphs and examples are worded apart from the example of `case-schema.md`, with another subject and other ledger lines. The checks the examples pass are not changed: `estimate-case-check-refuses-text-outside-the-list` and `estimate-spec-write-writes-a-defer` stand. The tests read text that lands only at the librarian's generate and render. `rule-retro` lets no red test pass, so, as the person chose and as `tests/test_case_schema.py` does, each test skips with a reason while the page holds no block of its tag. A Case of a later session removes the skips after the readings pass.
>
> The searches this Case rests on. A Grep of `rule-orchestration|orchestration\.md` over the repository root, with the glob `!**/decisions/** !**/raw/** !**/archive/** !**/log.md !**/brief.md`, printed 38 files. I read each hit outside History lines, and none says something that this Case makes false. A Grep of `short form|the summary` over `vault/wiki/rules/` printed 6 files: `rule-orchestration`, `rule-case-protocol`, `rule-spec-write`, `rule-case-build`, `rule-decisions-schema` and `rule-compact-recall`. Over `.claude/` it printed `.claude/agents/case-guppi.md`. `rule-spec-write` sets how the hook reads a short-form defer, and it is named in `given` of 651.3 and unchanged. `rule-case-build` and the agent file set the summary that `case-guppi` writes, a moment before the main agent's showing, and they stand. `rule-case-protocol` and `rule-decisions-schema` point to `orchestration.md` for the short form, and `rule-compact-recall` speaks of the summary of a compaction. A Glob `vault/**/*example*` printed `vault/wiki/lessons/lesson-wait-what-invents-an-example.md` and `vault/wiki/estimates/estimate-case-protocol-example-passes-the-check.md`, so both new slugs are free. Both new Estimates carry a `ref`, so the vault query of `ask-guppi` was not run. The Insight is set `actioned` with `addressed_by: decision-case-651.3`, the bare form that case 636 used. The cascade of `generate` then archives its `clustered` children, among them `lesson-case-build-closes-a-sprint-item-without-the-sprint-page` and `lesson-case-build-splits-a-case-whose-line-stands`. A new lesson of the same kind reopens it.
>
> The check sent back notes, and they stand. Three `then` lines of 651.3 share most of their words with 651.2: the paragraph before the block, the test that holds no copy, and the skip. Each sub-case still sets its own promise. 651.2 covers the block tagged `showing` and the `Stop` check of `rule-case-check`. 651.3 covers the block tagged `defer` and the hook of `rule-spec-write`.
>
> Not done:
> - `rule-case-check`, `rule-spec-write`, the other Estimates and the code keep the word "answer", the refusal of the `Stop` comparison included.
> - The acknowledging reply gets no example.
> - The tests keep their skips until a Case of a later session removes them.

> **problem:**
> `orchestration.md` calls the reply of `case-guppi` "the answer" while that reply is now a summary, and it states the `ratification` of a showing and the `then` block of a short-form defer in words that the main agent has twice read into a form the checks refuse. The question was which words replace "the answer", how far the change reaches, how the two forms are shown and checked, and what happens to the Insight.

> **recommend:**
> - **Which word replaces "the answer"**
>   - Recommended: (a) a word for each meaning: the summary where the main agent reads the reply of `case-guppi`, the file where the Case is sent, and the text the check stored where the Spec hook reads; a round and a Fact reply keep their names.
>   - Answer: agreed, (a).
> - **How far the change reaches**
>   - Recommended: (a) only `orchestration.md`; the other pages and the code keep their words.
>   - Answer: agreed, (a).
> - **How the page states the two forms**
>   - Recommended: (b) an example checked by a test that runs the checks over it and fails on any refusal.
>   - Answer: agreed, (b).
> - **Which forms the page covers**
>   - Recommended: (a) the `ratification` of a showing and the `then` block of a short-form defer, the two the lessons name.
>   - Answer: agreed, (a).
> - **One check or one per form**
>   - Recommended: (a) three sub-cases: the rewording, checked by `estimate-orchestration-shows-the-built-case` as it stands; the example of a showing with a new Estimate; the example of a short-form defer with a new Estimate.
>   - Answer: agreed, (a).
> - **What the test does before the page holds the example**
>   - Recommended: (a) skip until the render, with a reason that names `orchestration.md`; a Case of a later session removes the skip after the readings pass.
>   - Answer: agreed, (a).
> - **What the example of a showing shows**
>   - Recommended: (a) a parent with two sub-cases: the heading, a list of two items, one `ratification` quote block with the lines of both, the horizontal rule and the agent's own text.
>   - Answer: agreed, (a), with the heading of the example in English, since the example is part of the documentation.
> - **What happens to the open Insight**
>   - Recommended: (a) mark it `actioned`, addressed by this Case.
>   - Answer: agreed, (a).

### Case 651.1 — orchestration.md names the summary, the file and the stored text of case-guppi

> **given:**
> `rule-orchestration`: the rule whose Render is `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: what the main agent does, loaded by `/hi`.
> **＋** `rule-case-build`: the summary, the round and the `**Fact:**` reply of `case-guppi`. Unchanged.
> **＋** `rule-case-check`: its check stores the text of the file of a Case. Unchanged.
> **＋** `rule-spec-write`: its hook writes a Case from that stored text. Unchanged.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a built Case.

> **when:**
> The main agent reads `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, to show a summary, a round or a `**Fact:**` reply of `case-guppi`.

> **then:**
> The page calls the reply of `case-guppi` that opens with `**Built:**` the summary, and the main agent writes the list and the `ratification` of a showing from the summary and sends back a summary in which a Case gives no Estimate.
> **＋** The page calls the Case sent at a showing and at a showing again the file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and what the hook of `rule-spec-write` writes the text the check of `rule-case-check` stored from that file.
> **＋** A reply of `case-guppi` with no first line `**Built:**` and no first line `**Fact:**` is a round, and the page names it so.
> **－** No sentence of `vault/wiki/orchestration.md` calls a reply of `case-guppi` the answer; the person's answers keep that word.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `the main agent shows that answer translated into {{chat_lang}}`
>   - new: `the main agent shows that reply translated into {{chat_lang}}`
>   - old: `The agent shows the Case of the answer at every showing`
>   - new: `` The agent shows the Case `case-guppi` built at every showing ``
>   - old: `an item per Case and sub-case of the answer, its id`
>   - new: `an item per Case and sub-case of the summary, its id`
>   - old: `of every Case of the list as the answer holds them, never its`
>   - new: `of every Case of the list as the summary holds them, never its`
>   - old: `an answer in which a Case gives no such Estimate goes back`
>   - new: `a summary in which a Case gives no such Estimate goes back`
>   - old: `` shows the `ratification` as the answer holds it (case 452.4) ``
>   - new: `` shows the `ratification` as the summary holds it (case 452.4) ``
>   - old: `an answer with no first line`
>   - new: `` a reply of `case-guppi` with no first line ``
>   - old: `with the number of the answer`
>   - new: `with the number the round gives it`
>   - old: `Its new answer is sent again whole, in its file`
>   - new: `Its new file is sent again whole`
>   - old: `writes a Case only from its stored answer after a reply`
>   - new: `` writes a Case only from the text the check of `rule-case-check` stored from its file after a reply ``
>   - old: `` a round of questions of `case-guppi`, translated from the answer, ``
>   - new: `` a round of questions of `case-guppi`, translated, ``
>   - old: `` the ledger lines of `ratification` stand in the chat as the answer holds them ``
>   - new: `` the ledger lines of `ratification` stand in the chat as the summary holds them ``
>   - old: `while an answer is out`
>   - new: `` while a `case-guppi` of the batch has not replied ``
>   - old: `a round may come at the first answer on an item`
>   - new: `a round may come at the first reply on an item`
>   - change: `the reply of case-guppi is named the summary, the Case sent is its file, and the Spec hook reads the text the check stored from that file (case 651.1)`
> - [ ] `uv run guppi render`: `vault/wiki/orchestration.md`

> **ratification:**
> ```
> - decision[case 651.1][update][rule-orchestration]{ref:rule-orchestration}
> ```

### Case 651.2 — orchestration.md shows a showing by an example the Stop check passes

> **given:**
> `estimate-orchestration-showing-example-passes-the-check`: the new check of the example of a showing.
> **＋** `rule-orchestration`: the rule whose Render is `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: the page that holds the example.
> **＋** `tests/test_orchestration.py`: the new test that runs the check over the example.
> **＋** `guppi/casecheck.py`: `outside_the_list`, `showings` and `against_store`, the functions the `Stop` check runs over a reply that shows a Case.
> **＋** `rule-case-check`: its `Stop` check of a showing. Unchanged.
> **＋** `rule-one-judgment-one-implementation`: one test runs the example and the check over the same input.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `showing` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it the functions of `guppi/casecheck.py` that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, with a store whose sub-cases hold the ledger lines the example's `ratification` gives them.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## Showing and signing a Case`, one block tagged `showing`: a reply that shows a Case with two sub-cases, its heading, one list with an item per sub-case, one `ratification` and the agent's own text after one horizontal rule.
> **＋** The `ratification` of the example is a quote block: the line `> **ratification:**`, then the fence and the ledger lines of both sub-cases, each line opening with `> `.
> **＋** The example is in English; the paragraph before the block says that in the chat the heading, the names and the short texts stand in the language of the chat, that the file goes by `SendUserFile` in the same reply, and that the example passes the `Stop` check of `rule-case-check`, which is the source of the limits; it lists no other limit.
> **＋** The check finds no text outside the list and the `ratification`, reads the `ratification` as the showing of each sub-case it names, and finds no difference from the store, and the test passes.
> **＋** The example with the lines of its fence not quoted gives the finding of a text outside the list, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `showing`, the test is skipped with a reason that names the file; a Case of a later session removes the skip after the reading of `estimate-orchestration-showing-example-passes-the-check` passes.

> **tasks:**
> - [ ] create `estimate-orchestration-showing-example-passes-the-check`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the example of a showing in orchestration.md passes the Stop check of a reply that shows a Case, so the form the main agent copies stays a form the check accepts`
>   - method: `uv run pytest tests/test_orchestration.py -k showing_example, passed and not skipped`
>   - tags: `[session, workflow, harness]`
> - [ ] update `rule-orchestration`
>   - old: `Retro counts the unticked (case 59.3).`
>   - new:
>     `````
>     Retro counts the unticked (case 59.3).
>
>     ### A showing, by example
>
>     The block below is the text of a reply that shows a Case with two sub-cases, written after the `SendUserFile` call that sends its file. Its `ratification` is a quote block: the fence and each ledger line stand on lines that open with `> `, while the summary of `case-guppi` gives the same lines in a plain fence. In the chat the heading, the names and the short texts stand in {{chat_lang}}; the example is in {{documentation_lang}}, as the vault is. A test runs over the example the functions that the `Stop` check of `rule-case-check` runs over a reply that shows a Case, and fails on any refusal, so the example keeps to that check as the check stands (case 651.2). Copy its form; a refusal of the check names the limit a showing broke.
>
>     ````showing
>     ## Case 7 — Members get a reminder before a booking
>
>     - 7.1 — The reminder goes out a day before. Done when `estimate-booking-sends-a-reminder` passes: a test books a slot and finds one reminder queued a day before it.
>     - 7.2 — A cancelled booking sends no reminder. Done when `estimate-booking-skips-a-cancelled-reminder` passes: a test cancels a booked slot and finds no reminder queued.
>
>     > **ratification:**
>     > ```
>     > - decision[case 7.1][create][estimate-booking-sends-a-reminder]{ref:entity-booking}{tags:booking,email}
>     > - decision[case 7.1][update][entity-booking]{ref:entity-booking}
>     > - decision[case 7.2][create][estimate-booking-skips-a-cancelled-reminder]{ref:entity-booking}{tags:booking,email}
>     > ```
>
>     ---
>
>     Do you ratify 7.1 and 7.2, or only some of them?
>     ````
>     `````
>   - change: `the reply that shows a Case has an example that a test runs the Stop check of rule-case-check over (case 651.2)`
> - [ ] `tests/test_orchestration.py`: reads the first block tagged `showing` from `vault/wiki/orchestration.md` by `fence_opening` and `closes_fence` of `guppi/materialize.py`, its lines as they stand, and skips with a reason that names the file while it holds none. It builds a store whose entry for each sub-case id that a ledger line of the example names holds that sub-case's heading and a `ratification` of its own lines, read by `fence_ledger_lines`. Tests `-k showing_example`: `outside_the_list` finds nothing; `showings` reads a showing for each sub-case id and `against_store` finds no difference for each; the example with the `> ` taken off the lines of its fence makes `outside_the_list` return a line.
> - [ ] read `estimate-orchestration-showing-example-passes-the-check`

> **ratification:**
> ```
> - decision[case 651.2][create][estimate-orchestration-showing-example-passes-the-check]{ref:rule-orchestration}{tags:session,workflow,harness}
> - decision[case 651.2][update][rule-orchestration]{ref:rule-orchestration}
> ```

### Case 651.3 — orchestration.md shows a short-form defer by an example the Spec hook writes

> **given:**
> `estimate-orchestration-defer-example-passes-the-hook`: the new check of the example of a short-form defer.
> **＋** `rule-orchestration`: the rule whose Render is `vault/wiki/orchestration.md`.
> **＋** `vault/wiki/orchestration.md`: the page that holds the example.
> **＋** `tests/test_orchestration.py`: the test that runs the hook over the example.
> **＋** `guppi/ratified.py`: `write_defers` and `key_judge`, what the `Stop` hook runs over a defer-only Case.
> **＋** `rule-spec-write`: its hook writes a short-form defer under `## Deferred`. Unchanged.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept`: the Insight this Case acts on.

> **when:**
> `tests/test_orchestration.py` runs under `uv run pytest`. It reads the block tagged `defer` in `vault/wiki/orchestration.md`, rendered from `rule-orchestration`, and runs over it, as the text of a reply, the functions of `guppi/ratified.py` that the `Stop` hook of `rule-spec-write` runs over a defer-only Case, in a temporary project that holds the schema files of the vault and a plan file, with one `defer` record for each item of the example.

> **then:**
> `vault/wiki/orchestration.md` holds, under its own heading at the end of `## The short form — deferred decisions`, one block tagged `defer`: a Case in the short form with its heading, `context`, `problem` and a fence tagged `then` whose `defer:` holds a list, one item per target, each item opening with `- slug:` and carrying `type` and `purpose`.
> **＋** The paragraph before the block says that the reply that shows the Case carries its `LEDGER` block with one `defer` line per item, and that the example passes the `Stop` hook of `rule-spec-write`, which is the source of the limits; it lists no other limit.
> **＋** The hook writes the example under `## Deferred` of the plan file with no error, and the test passes.
> **＋** The example with its `defer:` items written as one mapping gives the error that no fence tagged `then` holds its `defer` items, and the test asserts it.
> **＋** The test reads the example from `vault/wiki/orchestration.md` and the hook from `guppi/ratified.py`, and holds no copy of either.
> **＋** `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stands `actioned`, addressed by this Case.
> **－** While `vault/wiki/orchestration.md` holds no block tagged `defer`, the test is skipped with a reason that names the file; a Case of a later session removes the skip after the reading of `estimate-orchestration-defer-example-passes-the-hook` passes.

> **tasks:**
> - [ ] create `estimate-orchestration-defer-example-passes-the-hook`
>   - ref: `rule-orchestration`
>   - kind: `QA`
>   - purpose: `Whether the example of a short-form defer in orchestration.md passes the Stop hook that writes a defer-only Case into the Spec, so the form the main agent copies stays a form the hook accepts`
>   - method: `uv run pytest tests/test_orchestration.py -k defer_example, passed and not skipped`
>   - tags: `[session, workflow, harness]`
> - [ ] update `rule-orchestration`
>   - old: `` A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5). ``
>   - new:
>     `````
>     A `create`, `update` or `delete` at Retro waits for the next Plan Mode (cases 52.2, 56, 59.5).
>
>     ### A short-form defer, by example
>
>     The block below is a deferred decision in the short form as a reply shows it; the same reply carries its `LEDGER` block, with one `defer` line per item. A test runs over the example the functions that the `Stop` hook of `rule-spec-write` runs over a defer-only Case, and fails on any error, so the example keeps to that hook as the hook stands (case 651.3). Copy its form; an error of the hook names the limit a short Case broke.
>
>     ````defer
>     ## Case 8 — The export of old bookings put off
>
>     > **context:**
>     > The person put off the export of bookings older than a year at the close of Plan Mode. No Case of this session sets the form of the export.
>
>     > **problem:**
>     > No Case of this session decides how an owner exports old bookings.
>
>     ```then
>     defer:
>       - slug: entity-booking-export
>         type: entity
>         purpose: "Lets an owner export the bookings older than a year; put off at the close of Plan Mode"
>     ```
>     ````
>     `````
>   - change: `the short form of a defer has an example that a test runs the Stop hook of rule-spec-write over (case 651.3)`
> - [ ] update `insight-workflow-case-schema-silent-on-what-the-scripts-accept`
>   - set: `{status: actioned, addressed_by: decision-case-651.3}`
>   - change: `actioned: case-schema.md and orchestration.md show the forms case-guppi and the main agent write by examples that a test runs the checks over (cases 646, 651)`
> - [ ] `tests/test_orchestration.py`: reads the first block tagged `defer` from `vault/wiki/orchestration.md` the same way, and skips with a reason that names the file while it holds none. It seeds a temporary project with the `schema.yaml` files of `vault/wiki/` and an empty plan file, and builds one `defer` record of the Case of the example for each slug of its `then` items. Tests `-k defer_example`: `write_defers` with `key_judge` returns no error and the plan file holds the Case under `## Deferred`; the example with its items rewritten as one mapping under `defer:` returns the error `no fence tagged then with its defer items`.
> - [ ] read `estimate-orchestration-defer-example-passes-the-hook`

> **ratification:**
> ```
> - decision[case 651.3][create][estimate-orchestration-defer-example-passes-the-hook]{ref:rule-orchestration}{tags:session,workflow,harness}
> - decision[case 651.3][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 651.3][update][insight-workflow-case-schema-silent-on-what-the-scripts-accept]{ref:insight-workflow-case-schema-silent-on-what-the-scripts-accept}
> ```
