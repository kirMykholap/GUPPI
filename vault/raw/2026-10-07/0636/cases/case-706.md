## Case 706 — The actioned Insight links to the decision that actioned it

> **context:**
> An Insight page groups lessons that share one cause. When a ratified decision fixes that cause, the page becomes `actioned`, and `rule-insights-schema` then requires the field `addressed_by`, a link to that decision. Case 701.1 set `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` to `actioned` with no `addressed_by`, so `make lint` reports a missing field on the page. `guppi/generate.py` does not fill the field: it writes what the `set` of an `update` gives. Its History already names `decision-case-701.1` as the decision that set the status, and that Decision page stands. The person chose that the field links to `decision-case-701.1`, and that this Case fixes the page only.
>
> A Grep for `conditional` over `guppi/` printed `guppi/lint.py` alone, so only `make lint` checks the requirement, at the librarian's run. A later Case can still set an Insight `actioned` without `addressed_by`, and no check sends it back before ratification; this is left not done, by the person's choice. `estimate-insights-schema-checked` checks the change: its Criterion says that a page with the required fields has no `schema` finding and that `actioned` requires `addressed_by`, and its live reading is `make lint` with no `schema` finding under `wiki/insights/`. This Case changes no schema and no code, so its Criterion stands, and the reading is left to the `make lint` of the librarian's run, which the brief reports. Case 704 of this session updates the same Insight with only `change`; it sets no field, so the two Cases do not clash, and each adds its own History line. No code changes, so no reader goes ahead of its text and no old form is kept.

> **problem:**
> The Insight `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` stands `actioned` with no `addressed_by`, and `make lint` reports it as a missing field.

> **recommend:**
> - **Which decision the field `addressed_by` links to**
>   - Recommended: (a) the part that set the status, `decision-case-701.1`, the decision its History line names.
>   - Answer: agreed, (a).
> - **Whether this Case also adds a check for this mistake**
>   - Recommended: (a) fix the page only; `make lint` still catches the mistake at the librarian's run, and the Case says the check is left not done.
>   - Answer: agreed, (a).

> **given:**
> `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`: the Insight that gains the field.
> **＋** `rule-insights-schema`: the schema that requires `addressed_by` on an `actioned` Insight.
> **＋** `guppi/generate.py`: writes the field from the `set` of the `update`.
> **＋** `guppi/lint.py`: `make lint`, which checks the page against the schema.

> **when:**
> The librarian's run applies the yaml of this session by `guppi/generate.py`, and `make lint` of `guppi/lint.py` reads `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` by the schema of `rule-insights-schema`.

> **then:**
> `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` holds `addressed_by: "[[decision-case-701.1]]"`.
> **＋** `make lint` prints no `schema` finding on `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`.
> **＋** The History of `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` gains one line that it links to the decision that actioned it.
> **－** Its `status` stays `actioned`, and no other field or section changes.

> **tasks:**
> - [ ] update `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`
>   - set:
>     ```
>     addressed_by: "[[decision-case-701.1]]"
>     ```
>   - change: `addressed_by: decision-case-701.1, the decision that set it actioned (case 706)`

> **ratification:**
> ```
> - decision[case 706][update][insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out]{ref:insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out}
> ```
