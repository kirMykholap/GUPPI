## Case 712 — A Case names a decision of its own session in addressed_by by the bare slug

> **context:**
> An `actioned` Insight names in `addressed_by` the decision that fixed it, and the field description of `rule-insights-schema` asks for a quoted wikilink. A Case that actions an Insight in its own session names its own decision, whose page `generate` writes only at the librarian's run. Until then the link check of `guppi/prespec.py`, which the check of the Case file shares, refuses it: in session 0636 it printed `casecheck: case 710.2: [[decision-case-710.1]] outside a code span names no page`, so Cases 710.2 and 711.3 wrote the bare slug against the words of the schema. The pages came out right all the same: `frontmatter` of `guppi/generate.py` writes every ref field as a quoted wikilink, whatever form the entry holds (case 148.1), and both Insights now hold `"[[decision-case-710.1]]"` and `"[[decision-case-711.3]]"`. The same fact answers the flag of the brief that the handoff said bare and the disk says quoted. The librarian's synthesis writes the field bare too, by `estimate-synthesis-reads-the-status-its-yaml-sets`. So only the words are wrong: the person chose to say in the field description that such a Case writes the bare slug and `generate` adds the brackets, and to leave the link check as it is, so that it still catches a link to a page that will never exist. `estimate-generate-writes` already checks that every ref field is written as a quoted wikilink, and its Criterion stands. `estimate-insights-schema-checked` checks that `vault/wiki/insights/schema.yaml` equals the Render and that `fields.addressed_by` names one decision; both stay true, so its Criterion stands. `estimate-prespec-catches-bare-wikilinks` speaks of the link check, which does not change.

> **problem:**
> The schema asks a Case for a quoted wikilink in `addressed_by`, and the checks before ratification refuse that link when the decision is of the same session; a Case cannot follow both.

> **recommend:**
> - **Which side changes so that a Case can name a decision of its own session**
>   - Recommended: (a) change the words of the Insight schema: the field description says that the page holds the quoted wikilink, that a Case writes the bare decision slug, and that the page writer adds the brackets; no code changes.
>   - Answer: agreed, (a).

> **given:**
> `rule-insights-schema`: the schema whose field description of `addressed_by` gains the sentence.
> **＋** `vault/wiki/insights/schema.yaml`: the Render of the schema, written again by the render.
> **＋** `guppi/generate.py`: writes every ref field as a quoted wikilink. Unchanged.
> **＋** `guppi/prespec.py`: the link check that refuses a link to a page that does not exist. Unchanged.
> **＋** `estimate-generate-writes`: checks the quoted wikilink of every ref field. Its Criterion is unchanged.
> **＋** `estimate-insights-schema-checked`: checks the Render of the schema. Its Criterion is unchanged.

> **when:**
> `case-guppi` reads the field description of `addressed_by` in `vault/wiki/insights/schema.yaml` to write a Case that sets an Insight `actioned` by a decision of its own session.

> **then:**
> The description says that such a Case writes the bare slug of the decision, and that `guppi/generate.py` writes the field on the page as the quoted wikilink.
> **＋** The description still says that the page holds the quoted wikilink.
> **－** The link check of `guppi/prespec.py` does not change.

> **tasks:**
> - [ ] update `rule-insights-schema`
>   - old: `a list is not a shape of this field, and of two Cases of one plan only one actions the Insight (case 361).`
>   - new: `a list is not a shape of this field, and of two Cases of one plan only one actions the Insight (case 361). A Case that actions the Insight by a decision of its own session writes the bare slug, decision-case-<N>, since that decision page is written only at the librarian's run and the checks before ratification refuse a link to a page that does not exist yet; generate writes the field on the page as the quoted wikilink (case 712).`
>   - change: `a Case names a decision of its own session in addressed_by by the bare slug; generate adds the brackets (case 712)`
> - [ ] `uv run guppi render`: `vault/wiki/insights/schema.yaml`

> **ratification:**
> ```
> - decision[case 712][update][rule-insights-schema]{ref:rule-insights-schema}
> ```
