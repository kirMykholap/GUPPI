## Case 735 — The cart Estimate of the example names a make target

> **context:**
> Case 733 made `/pre-spec` judge the `method` of a MOC's Estimate by its form: only a `make <target>` or a reading `by hand` passes there, and a `tests/` path or `pytest` alone is a finding. Its code turned `make test` red at the Retro of session 0213, since the example Case of `rule-case-example`, rendered into `vault/wiki/case-example.md`, creates `entity-cart` with `kind: MOC` and gives its Estimate `estimate-cart-renders-in-time` a `method` that names only a `pytest` command; `tests/test_case_schema.py` runs the check of the Case file over that example and fails on any finding. The code was saved to `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff` and reverted, and `estimate-prespec-catches-a-method-without-a-form` stands `failed`. The brief plans to change the example and apply the patch in one session, but that order fails again: `guppi/guard.py` refuses a hand edit of a file a Rule page governs, so the new example reaches `vault/wiki/case-example.md` only at the render of the librarian's run, and in Work Mode the patched check would run over the old example; the Retro skill says that a red test is never an expected red and is fixed or reverted. The person chose to change only the example in this session, and to apply the patch, format it with `make style` and read `estimate-prespec-catches-a-method-without-a-form` in a later session, after the render; this Case does none of those three, `rule-prespec` stays `draft` until that reading, and the handoff of this session carries the work. The new `method` is `make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time`: it names a `make` target, so the form a MOC's Estimate takes, and the check judges the form only, not whether a Makefile holds the target. The first pair matches the `method` sub-point of the `create` of `estimate-cart-renders-in-time` in Case 1.2 of the example; the other three match the `kind`, `purpose` and `method` of the entry of the same Estimate in the `then` block example below it, which the person chose to make equal to the item of the example Case. The Criterion of `estimate-case-example-passes-the-check` stands: it promises that the check gives the example no finding and no note as the check stands, and the same test shows that the new example passes the stricter check once the patch applies; it is the one Estimate of `rule-case-example`. A Grep of `cart-renders-in-time|test_cart_view|measure the render` over the repository, `vault/raw/` and `vault/archive/` left out, printed `vault/wiki/brief.md`, `vault/wiki/case-example.md`, `vault/wiki/rules/rule-case-example.md`, `vault/wiki/rules/rule-estimates-schema.md`, `vault/wiki/estimates/estimate-prespec-catches-a-method-without-a-form.md` and `vault/wiki/estimates/schema.yaml`. The hit in `estimate-prespec-catches-a-method-without-a-form` is its Result, which records the failed reading and stands. The hits in `rule-estimates-schema` and its render `schema.yaml` are the example page of a `Research` Estimate, whose target `entity-cart` it gives no `kind`; it is another example, outside the item the person chose, and it stands.

> **problem:**
> The example Case that `case-guppi` copies gives a MOC's Estimate a `method` that names only a `pytest` command, which the stricter check of Case 733 reports, so that check cannot land while the example stands.

> **recommend:**
> - **When is the patch applied?**
>   - Recommended: (a) the example now, the patch in the next session, after the librarian's run renders the example; the pre-spec Estimate stays `failed` until then.
>   - Answer: agreed, (a).
> - **What method does the cart Estimate of the example name?**
>   - Recommended: (a) a make target: `make test-cart`, which runs the `pytest` command; the cart stays a MOC.
>   - Answer: agreed, (a).
> - **Is the cart Estimate in the Spec-block example fixed too?**
>   - Recommended: (a) the same entry as the Case: its `kind`, `purpose` and `method` as in the example Case.
>   - Answer: agreed, (a).
> - **Which Estimate checks the change to the example?**
>   - Recommended: (a) the Criterion of `estimate-case-example-passes-the-check` stands.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-example`: its Render holds the example Case and the `then` block example.
> **＋** `vault/wiki/case-example.md`: the file rendered from `rule-case-example`, which `case-guppi` reads.
> **＋** `estimate-cart-renders-in-time`: the Estimate the example creates, whose `method` changes; no page of the vault.
> **＋** `entity-cart`: the MOC the example creates, the target of that Estimate; no page of the vault.
> **＋** `estimate-case-example-passes-the-check`: the test of the example against the check of the Case file; its Criterion stands.
> **＋** `vault/raw/2026-10-08/0213/patch-prespec-moc-method-form.diff`: the stricter check the new `method` must pass.

> **when:**
> `case-guppi` reads `vault/wiki/case-example.md`, rendered from `rule-case-example`, before it first writes the file of a Case.

> **then:**
> The example Case creates `estimate-cart-renders-in-time` on the MOC `entity-cart` with a `method` that names the `make` target `make test-cart`, which runs the `pytest` command.
> **＋** The `then` block example creates the same Estimate with the `kind`, `purpose` and `method` of the example Case.
> **－** The `pytest` command does not stand alone in the `method` of the cart Estimate in either example.

> **tasks:**
> - [ ] update `rule-case-example`
>   - old: `` method: `uv run pytest tests/test_cart_view.py -k render_time` ``
>   - new: `` method: `make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time` ``
>   - old: `kind: Research`
>   - new: `kind: QA`
>   - old: `purpose: Whether the cart renders within 200ms, and what dominates the time if not`
>   - new: `purpose: Whether the cart shows its items within 200 ms`
>   - old: `method: measure the render at 10, 50 and 200 line items, against a seeded database`
>   - new: `method: make test-cart, which runs uv run pytest tests/test_cart_view.py -k render_time`
>   - change: `the cart Estimate of both examples names a make target, the form a MOC's Estimate takes (case 735)`
> - [ ] `uv run guppi render`: `vault/wiki/case-example.md`

> **ratification:**
> ```
> - decision[case 735][update][rule-case-example]{ref:rule-case-example}
> ```
