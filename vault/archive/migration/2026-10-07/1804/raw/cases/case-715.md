## Case 715 — Pre-spec reports a replaced Criterion whose kept method waits for another session

> **context:**
> An Estimate is read through its `method`. Since case 670.4, `guppi/prespec.py` reports a `method` that waits for another session, but only one the plan writes: a `create`, or an `update` with `set: {method: …}`. A Case that replaces the Criterion of an Estimate whole and writes no `method` keeps the `method` on the page, and the page goes `pending`. When that `method` names a later session, the Retro of the Case's own session cannot read it, and the Estimate is left `failed`. This happened to `estimate-orchestration-shows-the-frontier-after-a-closed-line`: case 701.6 replaced its Criterion in session 0425, and the Retro of that session wrote it `failed`, not read (`raw/2026-10-07/0425/ledger.md`, L26). The handoff of session 0636 and the brief carry it as C7. The person chose a report at pre-spec for every Estimate rather than a new `method` for this one; a new Estimate on `rule-prespec-hook`; and no report for an `update` that sets an Estimate `passed` or `failed` by the person's decision, since no reading follows it.
>
> So `estimate-orchestration-shows-the-frontier-after-a-closed-line` keeps its `method`, and the next Case that replaces its Criterion gets the report and must write a `method` that runs in its own session. A Grep for `^method:.*(?i)((later|next)\s+session|session\s+after|librarian|[^\w/]/hi\b)` over `vault/wiki/estimates/` printed 85 files, this Estimate among them; the pattern is close to the predicate of `guppi/lint.py` but does not leave out a part that names the person. These pages stay as they are; the report reaches each one when a Case replaces its Criterion.
>
> The new check sits in `check_form` of `guppi/prespec.py`, inside `judge`, so `/pre-spec`, the check of a Case file of `rule-case-check` and the check after ratification of `rule-spec-write` all run it. It runs from the working tree at once; a Case it refuses goes back to `case-guppi`, and nothing is lost, so no old form is kept. Case 714 of this session adds another finding to `judge` and to the same docstring list; the two findings judge different things and do not clash. The Criterion of `estimate-prespec-hook-reports-a-method-that-waits-for-another-session` reads only the `method` a plan writes, and each of its lines stays true, so it stands; the new branch can fail while that one passes, and its fix differs, so it is a new Estimate. A Grep for `(?i)waits? for (another|a later) session` over `vault/wiki/rules/` printed `rule-case-protocol.md`, and over `.claude/` printed nothing. Its sentence in the Render, that pre-spec reports a `method` that waits for a later session, the librarian or a /hi, stays true and stands. Not done: a `method` that another item of the same plan sets on the page is not read in place of the page's `method`. A Glob `vault/**/*kept-method*` printed nothing, so the new slug is free.

> **problem:**
> A Case that replaces the Criterion of an Estimate whole and keeps a `method` that waits for another session passes pre-spec with no report, and its own Retro leaves the Estimate `failed`.

> **recommend:**
> - **What should the fix cover?**
>   - Recommended: (b) a `/pre-spec` report for every check: a Case that replaces a Criterion with no new `method`, while the page's `method` waits for another session, gets a report; this Estimate's `method` stays until the next Case changes its Criterion.
>   - Answer: agreed, (b).
> - **Which check confirms the new report?**
>   - Recommended: (a) a new check page, `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`, read by a test; the existing check page stays as it is.
>   - Answer: agreed, (a).
> - **Does a Case that sets a check passed or failed by your decision get the report?**
>   - Recommended: (a) no report for it; only a Case that leaves the page `pending` gets the report.
>   - Answer: agreed, (a).

> **given:**
> `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`: the new check of the report.
> **＋** `rule-prespec-hook`: the rule of pre-spec, the target of the Estimate. Unchanged.
> **＋** `guppi/prespec.py`: `check_form`, inside `judge`, and the module docstring.
> **＋** `guppi/lint.py`: `waits_for_another_session` and `method_of`, the predicate and the reader of the field. Unchanged.
> **＋** `tests/test_prespec.py`: the tests of the report.
> **＋** `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`: the check of a `method` the plan writes. Unchanged.
> **＋** `raw/2026-10-07/1804/cases/case-714.md`: adds another finding to `judge` and to the same docstring list.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads an `update` of an Estimate in the `then` blocks of the plan file that replaces its Criterion whole and carries no `set: {method: …}`, and the `method` of that Estimate's live page.

> **then:**
> When a part of that `method` between two `;` names a later session, the next session, a session after another, the librarian or /hi, and does not name the person, the check gives one line `case N: update <slug>: the method on the page waits for another session — set a method that runs in this session`.
> **＋** The judgment is `waits_for_another_session` of `guppi/lint.py`, the same predicate that judges a `method` the plan writes.
> **－** An `update` that sets the Estimate `passed` or `failed` by the person's decision gives no such line.
> **－** An `update` that names a part of the page alone, such as a `set` of another field or a `replace` pair, gives no such line.
> **－** A `method` on the page that waits for no other session, or whose part names the person, gives no such line.

> **tasks:**
> - [ ] create `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`
>   - ref: `rule-prespec-hook`
>   - kind: `QA`
>   - purpose: `Whether pre-spec reports a Case that replaces the Criterion of an Estimate whole, writes no method and keeps one on the page that waits for another session, by the one predicate of guppi/lint.py`
>   - method: `uv run pytest tests/test_prespec.py -k kept_method`
>   - tags: `[harness, workflow]`
> - [ ] `guppi/prespec.py`: in `check_form`, an `update` of an Estimate that names no part by `materialize.names_a_part`, carries no `set.method` and sets no `status` of `passed` or `failed` reads the `method` of the live page by `lint.method_of` and, when `lint.waits_for_another_session` holds, gives the line of the `then`; the module docstring gains the finding in its list.
> - [ ] `tests/test_prespec.py`: tests named `kept_method`: a Criterion replaced with a page `method` that names a later session, the librarian or /hi gives the line; the same with `set: {method: …}` in the item, with `status: passed` or `failed` set by the person's decision, with only a `replace` pair or a `set` of another field, and with a page `method` that names the person or no other session gives none.
> - [ ] read `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`

> **ratification:**
> ```
> - decision[case 715][create][estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session]{ref:rule-prespec-hook}{tags:harness,workflow}
> ```
