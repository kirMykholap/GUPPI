## Case 646 — The Case schema shows the form case-guppi writes, by an example a test checks

> **context:**
> `case-guppi` reads `vault/wiki/case-schema.md` before it writes a Case. The page describes the chat form in prose. Its one example is the `then` block of the Spec, a form `case-guppi` never writes. When the agent writes a form the scripts do not accept, the `SubagentStop` check sends the Case back. Earlier in this session the first build of Case 644 was sent back for an `old` value that held a backtick in an unpadded span, for a `new` that then had no `old` before it, and for paths in `then` that `given` did not name. The whole Case was then written again, though the page already stated both rules. Case 432 chose not to copy the limits of the scripts into the schema, because a second copy of a judgment is a defect from its first day. The person chose a way that keeps that reason: one example Case in the chat form under its own heading after `## Language`, and a test that runs the check of the `SubagentStop` hook over it and fails on any finding or note. This is the second form that `CLAUDE.md` allows under "One judgment, one implementation". The new Estimate `estimate-case-protocol-example-passes-the-check` stands on that test. The paragraph before the example lists no limit. It says that the check is the source of the limits and that the example passes it. The prose limits the page already states, and the Spec example, stay as they are. The example is the cart decision of the Spec example in the chat form. Like the Spec example, it updates `estimate-checkout-orders-the-steps` and creates `estimate-cart-renders-in-time`. It adds a `replace` pair whose values hold a backtick in padded spans, and its `context` says what the sentence around that match names, as `estimate-case-protocol-case-form` asks.
>
> The test reads the rendered `vault/wiki/case-schema.md`, and the example lands there only at the librarian's generate and render. `rule-retro` lets no red test pass to the commit, and `rule-work-mode` allows an expected red only for `make lint`, one of its steps or a hook. So, as the person chose, the test is skipped with a reason while the file holds no block tagged `case`. This follows `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`. A Case of a later session removes the skip after the reading of the new Estimate passes.
>
> The person also chose to fix, on this page alone, the sentences that call the reply of `case-guppi` its answer. A Grep of `answer` over `vault/wiki/case-schema.md` printed 10 lines. Lines 28, 68, 76, 80 and 84 speak of the reply of `case-guppi` or of a check of it, and they enter the Case as five `replace` pairs. The other five speak of the person's answer, the vault's answer, a question answered, or the moment the agent answers, and they stand. The pair on line 68 says that a file that differs from its stored text is refused, as 645.5 sets it, so the case file of 645 is named in `given`. Each behaviour these pairs describe has an Estimate that another Case of this session replaces. This Case leaves those Estimates to those Cases, so that no promise is signed in two wordings:
> - Line 80 describes the backlog check, whose Estimate is `estimate-case-check-requires-a-backlog-item-decided-on-its-page`.
> - Line 84 describes the check of a Case built again in another shape, whose Estimate is `estimate-case-check-sends-back-a-ratified-case-in-another-shape`.
> - Line 68 describes the copy into the Spec, whose Estimate is `estimate-spec-write-copies-the-ratified-case`.
>
> As the main agent reports, Case 645, now built again, replaces the first two Criteria so that their moment is the file `case-guppi` writes. 644.2 replaces the third, so that it speaks of the text stored under Case N. `estimate-spec-write-refuses-a-changed-case-file` (645.5) and `estimate-case-check-sends-back-a-faulty-case` (645.2) check the rest. Case 645 does not change `rule-case-protocol`. Its 645.10 replaces the Criterion of `estimate-case-protocol-case-form`, which speaks of the form of a file, and the example now follows it, so this Case does not touch that Estimate. `estimate-case-protocol-loaded` stands: its Criterion lists what the file holds without saying that nothing else stands there, and the new paragraph repeats no paragraph of `orchestration.md` or `ratification.md`.
>
> A Grep of `case-schema|rule-case-protocol` over `vault/wiki/**/*.md`, `.claude/**` and `guppi/**`, with `!**/decisions/**`, printed 60 files. I did not read the hits in `brief.md` or `log.md`. In each other file I read the lines around each hit. None says what the schema holds in a way that this Case makes false. The new Estimate carries a `ref`, so the vault query of `ask-guppi` was not run. A Glob `vault/**/*example*` printed only `vault/wiki/lessons/lesson-wait-what-invents-an-example.md`, so the slug is free.
>
> Not done:
> - The Insight `insight-workflow-case-schema-silent-on-what-the-scripts-accept` stays open and is not touched. Two of its lessons are about forms the main agent writes, which `orchestration.md` sets.
> - `orchestration.md` still calls the reply of `case-guppi` the answer.
> - The test keeps its skip until a Case of a later session removes it.

> **problem:**
> The Case schema describes the chat form in prose and shows no example of it. The agent writes forms that the check sends back, even where the prose states the rule. The question was how the schema shows the form without an untested second copy of the checks, whether this Case also fixes the page's wording about the agent's answer, and what happens to the Insight.

> **recommend:**
> - **How the page describes the form**
>   - Recommended: (a) a worked example, kept true by a test: one example Case in the form `case-guppi` writes, with a sub-case, `old` and `new` pairs, a padded value with a backtick, a fenced `set`, a `create` with its fields, a `given` that names each path its `when` and `then` use, and a `ratification` fence. A test runs the stop check over it and fails on any finding, and a new Estimate stands on that test. The prose limits stay.
>   - Answer: agreed, (a).
> - **The word "answer" on the page**
>   - Recommended: (a) fix them in this Case, on `case-schema.md` alone: its sentences speak of the file `case-guppi` writes and the text the check stored, and `orchestration.md` waits for a later Case.
>   - Answer: agreed, (a).
> - **What happens to the Insight**
>   - Recommended: (b) leave the Insight open and untouched until a later Case covers the main agent's forms too.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: the pre-spec check found that a test red in Work Mode cannot pass Retro. The person chose that the test is skipped, with a reason, while `case-schema.md` holds no `case` block, runs and passes after the librarian's render, and that a later Case removes the skip.
>   - Taken: a `－` line of `then` sets the skip, and the test task and `context` follow.
> - **Change**
>   - Asked: the pre-spec check found that the example did not say what the sentence around its `replace` match names, and gave no update of `estimate-checkout-orders-the-steps` where the Spec example gives one. The person agreed to the recommended fix.
>   - Taken: the example's `context` says what that sentence names, and Case 1.1 of the example updates and reads `estimate-checkout-orders-the-steps`.
> - **Change**
>   - Asked: the pre-spec check found that the paragraph before the example restated limits of the check, one of them wrongly, with no test behind it. The person agreed that the paragraph lists no limit.
>   - Taken: the paragraph says only that the example passes the check of the `SubagentStop` hook and that the check is the source of the limits. The `then` line on a paragraph naming each limit is gone.
> - **Change**
>   - Asked: the pre-spec check found that the pairs on lines 68, 80 and 84 describe behaviours whose Estimates this Case did not name. The person agreed to name them and to leave them to the Cases that replace them.
>   - Taken: `context` names `estimate-case-check-requires-a-backlog-item-decided-on-its-page` and `estimate-case-check-sends-back-a-ratified-case-in-another-shape`, left to Case 645, and `estimate-spec-write-copies-the-ratified-case`, left to 644.2.

> **given:**
> `rule-case-protocol`: the rule whose Render is `vault/wiki/case-schema.md`.
> **＋** `vault/wiki/case-schema.md`: the form of a Case, which `case-guppi` reads before it writes one.
> **＋** `estimate-case-protocol-example-passes-the-check`: the new check of the example.
> **＋** `tests/test_case_schema.py`: the test that runs the check over the example.
> **＋** `guppi/casecheck.py`: the check of the Cases of a file, which the test imports.
> **＋** `rule-case-check`: its `SubagentStop` hook runs that check over the file of a Case.
> **＋** `rule-one-judgment-one-implementation`: one test runs the example and the check over the same input.
> **＋** `raw/2026-10-05/0311/cases/case-645.md`: the ratified Case whose file and store the new wording names.

> **when:**
> `tests/test_case_schema.py` runs under `uv run pytest`. It reads the block tagged `case` in `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, and runs over it the function of `guppi/casecheck.py` that the `SubagentStop` hook of `rule-case-check` runs over the Cases of a file. It runs in a temporary project that holds the schema files of the vault and the pages the example updates.

> **then:**
> `vault/wiki/case-schema.md` holds, under its own heading after its `## Language` section, one block tagged `case`: one Case with sub-cases, in the chat form that `case-guppi` writes into its file.
> **＋** The example holds a `create` and an `update` with their sub-points, a `replace` pair whose values hold a backtick in spans padded by one space, a `set` in a fenced block, an `update` of an Estimate whose Criterion it replaces, a read line for each Estimate it creates or replaces, and its ledger lines in a quoted fence under `ratification`.
> **＋** The example's `context` says what the sentence around the match of its `replace` pair names.
> **＋** The paragraph before the block says that the example passes the check of the `SubagentStop` hook of `rule-case-check`, and that the check, not the paragraph, is the source of the limits; it lists no limit.
> **＋** The check gives the example no finding and no note, and the test passes.
> **＋** A change of the check that gives the example a finding or a note fails the test, which prints it.
> **＋** The test reads the example from `vault/wiki/case-schema.md` and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/case-schema.md` holds no block tagged `case`, the test is skipped with a reason that names the file; a Case of a later session removes the skip after the reading of `estimate-case-protocol-example-passes-the-check` passes.
> **－** The Spec example and the limits that the prose of `vault/wiki/case-schema.md` already states stay as they are.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `a Case off this form is not written, and the hook says why (cases 159, 387.2).`
>   - new:
>     `````
>     a Case off this form is not written, and the hook says why (cases 159, 387.2).
>
>     ## The chat form, by example
>
>     The Case below is written in the chat form that `case-guppi` writes into its file. A test runs over it the check that the `SubagentStop` hook of `rule-case-check` runs over that file, and fails on any finding or note, so the example passes that check as the check stands (case 646). The limits a form must keep are those of the check, not of this paragraph: copy the form of the example, and read a finding of the check as the limit it names.
>
>     ````case
>     ## Case 1 — The cart stands before payment
>
>     > **context:**
>     > Until now items went straight from the catalogue to payment, and a buyer could not review an order. The person chose a cart between the two. The pair on `entity-checkout` changes the one sentence of its Purpose that names where the buyer pays; there it names the payment step, which now follows the cart. The Criterion of `estimate-checkout-orders-the-steps` speaks of the order of the steps, so Case 1.1 replaces it. A Glob `vault/**/*cart*` printed nothing, so both new slugs are free.
>
>     > **problem:**
>     > A buyer pays for an order without seeing it whole.
>
>     > **recommend:**
>     > - **Where the cart stands**
>     >   - Recommended: (a) between the catalogue and payment.
>     >   - Answer: agreed, (a).
>
>     ### Case 1.1 — The cart stands before payment
>
>     > **given:**
>     > `entity-cart`: the new page of the cart.
>     > **＋** `entity-checkout`: the page of payment, which names the cart.
>     > **＋** `estimate-checkout-orders-the-steps`: its Criterion is replaced whole.
>
>     > **when:**
>     > A buyer with items in `entity-cart` opens `entity-checkout`.
>
>     > **then:**
>     > The buyer sees each item of the order and its price.
>     > **＋** The buyer pays only after the cart is shown.
>     > **－** An empty cart does not open `entity-checkout`.
>
>     > **tasks:**
>     > - [ ] create `entity-cart`
>     >   - type: `entity`
>     >   - kind: `MOC`
>     >   - purpose: `Lets a buyer review an order before paying`
>     >   - tags: `[cart, checkout]`
>     >   - sections.Purpose: `Until now items went straight from the catalogue to payment.`
>     > - [ ] update `entity-checkout`
>     >   - old: `` the buyer pays at `/checkout/pay` ``
>     >   - new: `` the buyer reviews the cart, then pays at `/checkout/pay` ``
>     >   - set:
>     >     ```
>     >     tags: [cart, checkout, payment]
>     >     ```
>     >   - change: `the cart precedes payment`
>     > - [ ] update `estimate-checkout-orders-the-steps`
>     >   - set: `{status: pending}`
>     >   - change: `the Criterion replaced whole — the cart precedes payment`
>     > - [ ] read `estimate-checkout-orders-the-steps`
>
>     > **ratification:**
>     > ```
>     > - decision[case 1.1][create][entity-cart]{tags:cart,checkout}
>     > - decision[case 1.1][update][entity-checkout]{ref:entity-checkout}
>     > - decision[case 1.1][update][estimate-checkout-orders-the-steps]{ref:entity-checkout}
>     > ```
>
>     ### Case 1.2 — The cart renders in time
>
>     > **given:**
>     > `estimate-cart-renders-in-time`: the new check of the time the cart takes to show.
>     > **＋** `entity-cart`: the page of the cart.
>     > **＋** `src/cart/view.py`: the view of the cart.
>
>     > **when:**
>     > A buyer opens the cart of `src/cart/view.py` with 10, 50 or 200 items.
>
>     > **then:**
>     > The cart shows all its items within 200 ms.
>     > **－** A cart of more than 200 items is not bound by this time.
>
>     > **tasks:**
>     > - [ ] create `estimate-cart-renders-in-time`
>     >   - ref: `entity-cart`
>     >   - kind: `QA`
>     >   - purpose: `Whether the cart shows its items within 200 ms`
>     >   - method: `uv run pytest tests/test_cart_view.py -k render_time`
>     >   - tags: `[cart, performance]`
>     > - [ ] `src/cart/view.py`: the cart reads its items in one query.
>     > - [ ] read `estimate-cart-renders-in-time`
>
>     > **ratification:**
>     > ```
>     > - decision[case 1.2][create][estimate-cart-renders-in-time]{ref:entity-cart}{tags:cart,performance}
>     > ```
>     ````
>     `````
>   - old: `the Spec is written from the {{documentation_lang}} answer and the {{documentation_lang}} short form`
>   - new: `the Spec is written from the {{documentation_lang}} text of the Case file that the check stored and the {{documentation_lang}} short form`
>   - old: `` it copies the Case as `case-guppi` answered it — the answer the check of `rule-case-check` stored, never a showing that differs from it, which is refused (case 437) ``
>   - new: `` it copies the Case as `case-guppi` wrote it into its file — the text the check of `rule-case-check` stored, never a showing or a file that differs from it, which is refused (cases 437, 645.5) ``
>   - old: `passes on the person's words and shows its answer is`
>   - new: `passes on the person's words and shows the Case it built is`
>   - old: `` the check of the answer of `case-guppi` sends back a Case that names the page of an open `backlog` line when no Case among it and its sub-cases in the answer both names ``
>   - new: `` the check of the file `case-guppi` writes sends back a Case that names the page of an open `backlog` line when no Case among it and its sub-cases in the file both names ``
>   - old: `The check of the answer of case-guppi sends back a build`
>   - new: `The check of the file case-guppi writes sends back a build`
>   - change: `the schema shows the chat form by an example that a test runs the check over, and names the file case-guppi writes, not its answer, as what the check reads and the Spec copies (case 646)`
> - [ ] create `estimate-case-protocol-example-passes-the-check`
>   - ref: `rule-case-protocol`
>   - kind: `QA`
>   - purpose: `Whether the example Case of case-schema.md, in the chat form case-guppi writes, passes the check the SubagentStop hook runs over the file of a Case, so the form it shows stays a form the scripts accept`
>   - method: `uv run pytest tests/test_case_schema.py, passed and not skipped`
>   - tags: `[session, workflow, harness]`
> - [ ] `tests/test_case_schema.py`: reads the block tagged `case` from `vault/wiki/case-schema.md`, and skips with a reason that names the file while it holds none. It seeds a temporary project with the `schema.yaml` files of `vault/wiki/`, an `entity-checkout` page that holds the anchor of the example's pair, and an `estimate-checkout-orders-the-steps` page whose Criterion holds only lines that the example's `when` and `then` carry. It runs the function of `guppi/casecheck.py` that the `SubagentStop` check runs over the Cases of a file (today `check_answer`) and asserts no finding and no note, printing them when any stands. A second test makes one padded span of the example unpadded and asserts the finding.
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-protocol-example-passes-the-check`

> **ratification:**
> ```
> - decision[case 646][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 646][create][estimate-case-protocol-example-passes-the-check]{ref:rule-case-protocol}{tags:session,workflow,harness}
> ```
