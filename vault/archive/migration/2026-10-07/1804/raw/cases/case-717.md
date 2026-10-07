## Case 717 — A dispatch of `case-guppi` reads less and keeps its cache longer

> **context:**
> Each dispatch of `case-guppi` reads `vault/wiki/case-schema.md` whole, and that file holds two examples: a whole example Case in the chat form, which `tests/test_case_schema.py` runs the check of `rule-case-check` over, and an example of the `then` block of the Spec, which the agent never writes. The agent reads every other source whole too, and each later turn reads the whole context again from the cache. The cache of a subagent lives five minutes, so an answer after a longer pause, or the findings `/pre-spec` sends back, writes the whole context into the cache again. The main agent measured these costs on the dispatches of this session and reported them; I could not read those transcripts, so no number of theirs stands in this Case.
>
> The person chose the following. Both examples move to a new file, `vault/wiki/case-example.md`, the Render of a new rule `rule-case-example` (Case 717.1). The agent reads that file once in a dispatch, just before its first `Write` of a Case file. It reads whole `case-schema.md`, `ratification.md`, each page the Case changes, the Criterion of each Estimate of such a page, and the case file of each Case of the session that the prompt or a finding of the check names; it reads the rest in parts, a case file of an earlier session included, and makes independent calls in one turn. Its cache lives one hour, set in its agent file only (Case 717.2). The setting `cacheTtl: "1h"` under `experimental` comes from the main agent's report of the documentation of Claude Code; I could not open that documentation. The estimate line of `estimate-case-build-reads-by-need-and-in-parts` records the cache writes of each dispatch by their time to live, and that shows whether the setting takes effect.
>
> Case 717.1 creates `estimate-case-example-passes-the-check` on the new rule with the promise of `estimate-case-protocol-example-passes-the-check`, and deletes the old page: `generate` writes the `estimates` backlink of a target only on a `create`, so the old page cannot move to the new rule. `rule-case-protocol` drops it from its `estimates` by a `set`. The test reads the new file from Work Mode, but the file stands only after the librarian's render, and Retro fixes or reverts a red test (`rule-retro`). So the test reads `case-schema.md` while `case-example.md` does not stand, and a Case of a later session removes that path. The sentences of `rule-case-protocol` that say `case-guppi` reads `case-schema.md` whole stay true. The Criterion of `estimate-case-protocol-loaded` names the section of the `then` block, which stays, and the example is not part of it, so that Criterion stands. Its `purpose` says that the form of a Case stands in one text, the Render of `rule-case-protocol`. That stays true: every rule of the form stays in `case-schema.md`, and `case-example.md` holds only samples that follow those rules and set no rule of their own.
>
> The person chose to write the new reading into the promise of the agent's work, `estimate-case-build-writes-the-case`. Case 716.1 of this session already writes that Criterion back unchanged and sets its `method`, and the check of the file refuses a second wording of one promise in a session. So Case 717.2 creates `estimate-case-build-reads-by-need-and-in-parts` on `rule-case-build` for the new lines, with no limit on tokens, as the person chose. Its `method` follows the method of 716.1, and adds the tool calls and the cache writes. The Criterion of `estimate-case-build-writes-the-case` stays true. The agent still reads `case-schema.md` and `ratification.md` whole and reads each page and file the `given` names, and the new `experimental` field leaves its line on the frontmatter true. Case 716.1 needs no change. The Criterion of `estimate-case-build-checks-the-finished-case` says the agent reads the case file of each Case of the session that the prompt names. The `/pre-spec` check found that a search first would miss a related Case that sets the same moment in other words. The person chose that those case files stay read whole, so that Criterion stays true, and the paragraph of `rule-case-build` on them does not change. The hook of case 711.3 counts only a `Read` of the sentence around a pair as read. A page the Case changes is read whole, and so is the file of each related Case that writes into the same page, so the hook still finds its reads. No other Estimate of `rule-case-build` speaks of what the agent reads in parts. A Glob `vault/**/*reads-by-need*` printed nothing, so that slug is free.
>
> A Glob `vault/**/*case-example*` printed nothing, so `rule-case-example` and `estimate-case-example-passes-the-check` are free. A Grep for `estimate-case-protocol-example-passes-the-check` over `vault/wiki/`, `guppi/`, `tests/` and `.claude/` printed `vault/wiki/log.md`, `vault/wiki/rules/rule-case-protocol.md` and `tests/test_case_schema.py`. I did not read `log.md`. The hit in `rule-case-protocol` is its `estimates` field, which Case 717.1 sets, and the hit in the test is its docstring, which Case 717.1 changes. A Grep for `test_case_schema` over `vault/wiki/`, `guppi/` and `.claude/` printed `vault/wiki/estimates/estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read.md`, `vault/wiki/estimates/estimate-case-protocol-case-form.md` and `vault/wiki/estimates/estimate-case-protocol-example-passes-the-check.md`. The first names the example of `case-schema.md` in its Criterion, so Case 717.3 writes it back with the new file. The hit in `estimate-case-protocol-case-form` is a Result, the record of a past reading, and it stands. The third is the page Case 717.1 deletes. Not done: a limit on the tokens of a dispatch, since only a later session can measure one, and the removal of the old path of the test.

> **problem:**
> A dispatch of `case-guppi` costs more than its work needs. It reads examples it does not use, it reads background sources whole when it needs only a few lines, and it writes its whole context into the cache again after each pause longer than five minutes.

> **recommend:**
> - **Where do the examples of the Case form go?**
>   - Recommended: (a) both examples go to a new file, made from a new rule page; `case-schema.md` keeps all its rules and points to the new file, and the test of the sample Case reads it from there.
>   - Answer: agreed, (a).
> - **When does the agent read the examples file?**
>   - Recommended: (a) once in a dispatch, just before it first writes a Case file; a dispatch that only asks questions never reads it.
>   - Answer: agreed, (a).
> - **What does the agent read whole, and what in parts?**
>   - Recommended: (a) whole: `case-schema.md`, `ratification.md`, each page the Case changes and the promise text of each Estimate of such a page; in parts: case files of other Cases (searched first, read whole on a hit), the brief, the handoff, background pages and code (the functions the Case changes and the places that use them); independent reads in one turn.
>   - Answer: agreed, (a).
> - **Does the cache of `case-guppi` last longer than 5 minutes?**
>   - Recommended: (a) one hour for `case-guppi` only, set in its agent file.
>   - Answer: agreed, (a).
> - **How do we check that the change works?**
>   - Recommended: (a) rewrite the promise of the agent's work and the promise of the sample Case; no limit on tokens; the tokens of each run are recorded as before.
>   - Answer: agreed, (a).
> - **How does the agent read the case files of the related Cases the main agent names?**
>   - Recommended: (a) whole for the Cases the prompt names and the Cases a finding of the check names; a search first, then the whole file on a hit, for other case files.
>   - Answer: agreed, (a).

### Case 717.1 — The examples of the Case form stand in their own file

> **given:**
> `estimate-case-example-passes-the-check`: the new check that the example Case passes the check of a Case file.
> **＋** `rule-case-example`: the new rule whose Render is the file of examples.
> **＋** `vault/wiki/case-example.md`: the file of examples rendered from `rule-case-example`.
> **＋** `rule-case-protocol`: the rule whose Render loses the examples and points to the new file.
> **＋** `vault/wiki/case-schema.md`: the form of a Case rendered from `rule-case-protocol`.
> **＋** `estimate-case-protocol-example-passes-the-check`: the old check of the example, deleted.
> **＋** `tests/test_case_schema.py`: the test that runs the check over the example.
> **＋** `guppi/casecheck.py`: the check of the `SubagentStop` hook of `rule-case-check`.

> **when:**
> `tests/test_case_schema.py` runs under `uv run pytest`. It reads the block tagged `case` in `vault/wiki/case-example.md`, rendered from `rule-case-example`, and runs over it the function of `guppi/casecheck.py` that the `SubagentStop` hook of `rule-case-check` runs over the Cases of a file, in a temporary project that holds the schema files of the vault and the pages the example updates.

> **then:**
> `vault/wiki/case-example.md` holds one block tagged `case`, one Case with sub-cases in the chat form that `case-guppi` writes into its file, and after it one block tagged `then`.
> **＋** The example holds a `create` and an `update` with their sub-points, a `replace` pair whose values hold a backtick in spans padded by one space, a `set` in a fenced block, an `update` of an Estimate whose Criterion it replaces, a read line for each Estimate it creates or replaces, and its ledger lines in a quoted fence under `ratification`.
> **＋** The example's `context` says what the sentence around the match of its `replace` pair names.
> **＋** The paragraph before the block says that the example passes the check of the `SubagentStop` hook of `rule-case-check`, and that the check, not the paragraph, is the source of the limits; it lists no limit.
> **＋** `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, holds no example block and names `vault/wiki/case-example.md` where it sets the chat form and the `then` block.
> **＋** The check gives the example no finding and no note, and the test passes; a change of the check that gives the example a finding or a note fails the test, which prints it.
> **＋** The test reads the example from the file and the checks from `guppi/casecheck.py`, and holds no copy of either.
> **－** While `vault/wiki/case-example.md` does not stand, the test reads the block tagged `case` of `vault/wiki/case-schema.md`; a Case of a later session removes that path.
> **－** While the file the test reads holds no block tagged `case`, both tests of `tests/test_case_schema.py` fail with a message that names the file; no test of the file is skipped.

> **tasks:**
> - [ ] create `rule-case-example`
>   - ref: `rule-plan-mode`
>   - kind: `Leaf`
>   - purpose: `Prevents a Case from being written in a form the check of its file refuses because the agent that writes it saw no example of the form`
>   - enforcement: `render`
>   - governs: `vault/wiki/case-example.md`
>   - render_mode: `full`
>   - tags: `[session, workflow, harness]`
>   - sections.Purpose:
>     ```
>     Prevents a Case from being written in a form the check of its file refuses because the agent that writes it saw no example of the form. Until case 717.1 the examples stood in `case-schema.md`, the Render of [[rule-case-protocol]], which `case-guppi` reads whole on every dispatch, a dispatch that answers only with rounds included, and every later turn of the dispatch read them again from the cache. Here they stand apart, and `case-guppi` reads them once in a dispatch, just before it first writes the file of a Case ([[rule-case-build]]). The example Case passes the check of `rule-case-check`, and the test of its Estimate runs that check over it (case 646).
>     ```
>   - sections.Render:
>     `````
>     <!-- rule-case-example -->
>     # Case — examples
>
>     `wiki/case-example.md` — the Render of `rule-case-example`: two examples of the forms that `case-schema.md` sets. `case-guppi` reads this file once in a dispatch, just before it first writes the file of a Case; the rules of the form stand in `case-schema.md` (case 717.1).
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
>
>     ## The `then` block, by example
>
>     The block below is a `then` block of the Spec in the form that `case-schema.md` sets: a list under each decision type present, one entry per target, `slug` first.
>
>     ```then
>     create:
>       - slug: entity-cart
>         type: entity
>         kind: MOC
>         purpose: Lets a buyer review an order before paying
>         tags: [cart, checkout]
>         sections:
>           Purpose: |
>             Until now items went straight from the catalogue to payment.
>       - slug: estimate-cart-renders-in-time
>         type: estimate
>         ref: entity-cart
>         kind: Research
>         purpose: Whether the cart renders within 200ms, and what dominates the time if not
>         method: measure the render at 10, 50 and 200 line items, against a seeded database
>         tags: [cart, performance]
>     update:
>       - slug: entity-checkout
>         set: {tags: [cart, checkout, payment]}
>         change: the cart precedes payment
>       - slug: estimate-checkout-orders-the-steps
>         set: {status: pending}
>         change: the Criterion replaced whole — the cart precedes payment
>     ```
>     <!-- /rule-case-example -->
>     `````
> - [ ] create `estimate-case-example-passes-the-check`
>   - ref: `rule-case-example`
>   - kind: `QA`
>   - purpose: `Whether the example Case of case-example.md, in the chat form case-guppi writes, passes the check the SubagentStop hook runs over the file of a Case, so the form it shows stays a form the scripts accept`
>   - method: `uv run pytest tests/test_case_schema.py, passed and not skipped; at the Retro of the session that creates it, the new Renders of rule-case-example and rule-case-protocol in the Spec read against the Criterion`
>   - tags: `[session, workflow, harness]`
> - [ ] update `rule-case-protocol`
>   - old:
>     `````
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
>   - new:
>     ```
>     ## The chat form
>
>     `case-guppi` writes a Case into its file in the chat form that the sections, the operands and the language above set. `vault/wiki/case-example.md`, the Render of `rule-case-example`, shows that form by an example Case that passes the check of the `SubagentStop` hook of `rule-case-check`, and `case-guppi` reads it once in a dispatch, just before it first writes the file of a Case (cases 646, 717.1). The limits a form must keep are those of the check: read a finding of the check as the limit it names.
>     ```
>   - old:
>     ````
>     A list under each decision type present, one entry per target, `slug` first.
>
>     ```then
>     create:
>       - slug: entity-cart
>         type: entity
>         kind: MOC
>         purpose: Lets a buyer review an order before paying
>         tags: [cart, checkout]
>         sections:
>           Purpose: |
>             Until now items went straight from the catalogue to payment.
>       - slug: estimate-cart-renders-in-time
>         type: estimate
>         ref: entity-cart
>         kind: Research
>         purpose: Whether the cart renders within 200ms, and what dominates the time if not
>         method: measure the render at 10, 50 and 200 line items, against a seeded database
>         tags: [cart, performance]
>     update:
>       - slug: entity-checkout
>         set: {tags: [cart, checkout, payment]}
>         change: the cart precedes payment
>       - slug: estimate-checkout-orders-the-steps
>         set: {status: pending}
>         change: the Criterion replaced whole — the cart precedes payment
>     ```
>     ````
>   - new: `` A list under each decision type present, one entry per target, `slug` first; `vault/wiki/case-example.md` shows one. ``
>   - set:
>     ```
>     estimates: ["[[estimate-case-protocol-loaded]]", "[[estimate-case-protocol-case-form]]"]
>     ```
>   - change: `the example Case and the example of the then block move to case-example.md, the Render of rule-case-example; the schema names that file; estimate-case-protocol-example-passes-the-check leaves the estimates (case 717.1)`
> - [ ] delete `estimate-case-protocol-example-passes-the-check`
>   - impact: `Its promise moves with the example to estimate-case-example-passes-the-check on rule-case-example; tests/test_case_schema.py stays its test (case 717.1)`
> - [ ] `tests/test_case_schema.py`: the test reads the first block tagged `case` of `vault/wiki/case-example.md`, or of `vault/wiki/case-schema.md` while `case-example.md` does not stand; its message names the file it read; its docstring names `estimate-case-example-passes-the-check` and case 717.1.
> - [ ] `uv run guppi render`: `vault/wiki/case-example.md`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-case-example-passes-the-check`

> **ratification:**
> ```
> - decision[case 717.1][create][rule-case-example]{ref:rule-plan-mode}{tags:session,workflow,harness}
> - decision[case 717.1][create][estimate-case-example-passes-the-check]{ref:rule-case-example}{tags:session,workflow,harness}
> - decision[case 717.1][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 717.1][delete][estimate-case-protocol-example-passes-the-check]{ref:estimate-case-protocol-example-passes-the-check}
> ```

### Case 717.2 — `case-guppi` reads by need and in parts, and keeps its cache for an hour

> **given:**
> `rule-case-build`: the rule whose Render is the agent file of `case-guppi`.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from `rule-case-build`.
> **＋** `estimate-case-build-reads-by-need-and-in-parts`: the new check of what the agent reads, when, and how its cache lives.
> **＋** `vault/wiki/case-example.md`: the file of examples the agent reads before it writes.

> **when:**
> The main agent dispatches `case-guppi` by `.claude/agents/case-guppi.md`, rendered from `rule-case-build`, or sends it a message by `SendMessage`.

> **then:**
> `case-guppi` reads `vault/wiki/case-example.md` once in a dispatch, just before its first `Write` of the file of a Case.
> **＋** It reads whole each page the Case changes and the Criterion of each Estimate such a page lists.
> **＋** It reads in parts, by a Grep with lines of context or a Read with `offset` and `limit`, the case file of a Case of an earlier session, the brief and the handoff of the session, a page it reads only for background, and a module of code, of which it reads the functions the Case changes and the places that call them.
> **＋** It reads whole the case file of each Case of the session that the prompt of its call names, and of each Case of the session that the check of its file names in a finding or a note.
> **＋** It makes the tool calls that do not wait on each other's output in one turn.
> **＋** `.claude/agents/case-guppi.md` sets the cache of the agent to live one hour, by `cacheTtl: "1h"` under `experimental`.
> **－** A dispatch that answers only with rounds does not read `vault/wiki/case-example.md`.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `skills: [grill-me]`
>   - new:
>     ```
>     skills: [grill-me]
>     experimental:
>       cacheTtl: "1h"
>     ```
>   - old: `` Then read the pages the item names — a page is found by a Glob `vault/wiki/**/<slug>.md` — and the code they point to by `governs`, `implementation_ref` or `code_ref`. ``
>   - new: `` Read `vault/wiki/case-example.md` once in a dispatch, just before you first write the file of a Case: it shows the chat form by an example that passes the check of your file; a dispatch that answers only with rounds does not read it (case 717.2). Then read the pages the item names — a page is found by a Glob `vault/wiki/**/<slug>.md` — and the code they point to by `governs`, `implementation_ref` or `code_ref`. Read whole each page the Case changes, the `## Criterion` of each Estimate such a page lists, and the case file of each Case of the session that the paragraphs below name. Read the rest in parts, by a Grep with lines of context or a Read with `offset` and `limit`: the case file of a Case of an earlier session, the brief and the handoff of the session, a page you read only for background, and a module of code, of which you read the functions the Case changes and the places that call them. Make the tool calls that do not wait on each other's output in one turn. ``
>   - change: `case-guppi reads case-example.md just before it first writes a Case file, reads whole only the pages the Case changes, the Criteria of their Estimates and the case files of the related Cases, reads the rest in parts, makes independent calls in one turn, and keeps its cache for an hour (case 717.2)`
> - [ ] create `estimate-case-build-reads-by-need-and-in-parts`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi reads the examples only before it writes a Case, reads whole only the pages the Case changes, the Criteria of their Estimates and the case files of the related Cases, reads the rest in parts, makes independent calls in one turn, and keeps its cache for an hour`
>   - method: `by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; the tool calls, the tokens and the cache writes by their time to live of each dispatch of case-guppi in that session, when there was one, in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
> - [ ] read `estimate-case-build-reads-by-need-and-in-parts`

> **ratification:**
> ```
> - decision[case 717.2][update][rule-case-build]{ref:rule-case-build}
> - decision[case 717.2][create][estimate-case-build-reads-by-need-and-in-parts]{ref:rule-case-build}{tags:session,workflow,harness}
> ```

### Case 717.3 — The check of an unread sentence names the example in its new file

> **given:**
> `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read`: its Criterion written back with the new file of the example.
> **＋** `guppi/casecheck.py`: the check of the `SubagentStop` hook of `rule-case-check`.
> **＋** `tests/test_case_schema.py`: the test that runs the check with no record of an agent.
> **＋** `vault/wiki/case-example.md`: the file whose example the test checks.

> **when:**
> `tests/test_case_schema.py` runs the check of `guppi/casecheck.py` over the example of `vault/wiki/case-example.md`, with no record of an agent.

> **then:**
> The check judges no read for the example.

> **tasks:**
> - [ ] update `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     The `SubagentStop` hook `uv run guppi casecheck --subagent` of `guppi/casecheck.py` checks a file `raw/<date>/<hi HHMM>/cases/case-<N>.md` whose Case carries a `replace` or `reword` pair on a page that stands on disk, and reads the record of the subagent at `agent_transcript_path`.
>
>     Then:
>     For each match of each pair of the Cases of the file — the one match of a `replace`, and each match of a `reword` on each live page — the hook takes the sentence around it on the page as the earlier pairs leave it, by the function of the sentence of `guppi/prespec.py`.
>     **＋** The sentence counts as read when each part of it that no pair wrote stands whole in the outputs of the `Read` calls of the subagent on the page file, the line numbers of the output and the whitespace set aside.
>     **＋** A part of the sentence that a pair of another Case of the session wrote counts as read when it stands whole in the outputs of the `Read` calls of the subagent on the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of that Case.
>     **＋** A sentence not read is a finding of its Case: "case <N>: <slug>: the sentence around a pair was not read whole: <opening>: Read the page around it, and the file of each other Case that wrote into it, and check the pair."
>     **－** The output of a `Grep` call, or of any other tool than `Read`, is no read.
>     **－** A part of the sentence that a pair of the Cases of the file wrote is not judged.
>     **－** A transcript the hook cannot read, and a call of the check with no record of an agent, such as `tests/test_case_schema.py` over the example of `vault/wiki/case-example.md`, judge no read.
>     ```
>   - change: `the Criterion written back with the example of tests/test_case_schema.py in vault/wiki/case-example.md (case 717.3)`
> - [ ] read `estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read`

> **ratification:**
> ```
> - decision[case 717.3][update][estimate-case-check-sends-back-a-pair-whose-sentence-was-not-read]{ref:rule-case-check}
> ```
