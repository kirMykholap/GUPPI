## Case 529 — `insight-materialize-estimate-update-lifts-the-criterion-whole` is rejected as fixed, and its pattern names the cause in the past tense

> **context:**
> An Insight page groups lessons that share one cause. It stays `open` in `vault/wiki/backlog.md` until a decision fixes the cause or rejects the page (`rule-insights-schema`). The pattern of `insight-materialize-estimate-update-lifts-the-criterion-whole` says that `lift_criterion` in `guppi/materialize.py` lifts the when and then of a Case into every update of an Estimate and sets the page pending, even when the update changes only one field or one word. That was true in September. Case 296 added `names_a_part`, and case 378.4 made it the rule of the schema. Now an update that names one part of an Estimate changes that part alone, and a `replace` pair inside the Criterion is `incomplete: [criterion]`. So the pattern describes behaviour the code no longer has. The handoff of session 1753 and the brief flag this.
> Case 302.1 set the page `actioned`. The lesson `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` of session 2229 reopened it, because no decision of that session closed its cause (case 284.4). That lesson found that `estimate-generate-writes` and `estimate-generate-walks-dates` held the text of case 211.3 in place of their promises. Cases 489.1 and 489.2 have restored both Criteria. The lesson also says that nothing compares a Criterion with the name and purpose of its page. That is a check on any mismatch between a promise and its page, not this mechanism. Case 302.1 already declined the similar check the page's Proposal suggests.
> In two rounds the person accepted each recommendation, both times with the words "I agree". The page is set `actioned` with this decision in `addressed_by`. The pattern field and the `## Pattern` section get one new text that names the cause in the past tense, and the `## Proposal` section stays as it is.
> What `case-guppi` found in the frame: `rule-insights-schema` requires `addressed_by` on an `actioned` page and holds only the latest decision there. The cascade of `generate` archives the `clustered` children of an `actioned` Insight, so the lesson of session 2229 is archived at the librarian's run. `vault/wiki/backlog.md` lists open Insights only, so the page leaves it at the next `uv run guppi backlog`. Neither Insight nor Lesson pages have Estimates. The one Estimate of `rule-insights-schema`, `estimate-insights-schema-checked`, speaks of the shape of the page, and this Case keeps that shape. No code, hook or reader changes. The Case creates no page, so no vault query was run.
> Not done: a check that compares the Criterion of an Estimate with the name and purpose of its page.

> **problem:**
> An open Insight describes as current a mechanism the code has not had since case 378.4. The index line that the vault search reads says something false, and the page keeps a closed cause in the backlog.

> **recommend:**
> Set the page `actioned` with this decision as `addressed_by`, and rewrite its pattern as the cause in the past tense. The page stays in the vault, and a lesson with the same cause can open it again. Keeping it open for the check on a Criterion against its page's purpose was rejected: that is a different problem, and case 302.1 already declined a check of this kind.

> **given:**
> `insight-materialize-estimate-update-lifts-the-criterion-whole` — the Insight, its status, `addressed_by` and pattern
> **＋** `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` — its `clustered` child of session 2229
> **＋** `rule-insights-schema` — requires `addressed_by` on `actioned` and makes the Insight a mark for a recurrence
> **＋** `vault/wiki/backlog.md` — lists the open Insights

> **when:**
> The librarian's run applies the Case with `uv run guppi generate`, runs `uv run guppi backlog`, and someone reads `insight-materialize-estimate-update-lifts-the-criterion-whole`.

> **then:**
> `insight-materialize-estimate-update-lifts-the-criterion-whole` stands `actioned`, with this decision in `addressed_by`.
> **＋** Its `pattern` field and its `## Pattern` section hold one text, which names in the past tense how an update of one part of an Estimate replaced its whole Criterion.
> **＋** `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` stands `archived`, and it stays in the `children` of the Insight.
> **＋** `vault/wiki/backlog.md` does not list the Insight.
> **－** The `## Proposal` section of `insight-materialize-estimate-update-lifts-the-criterion-whole` does not change.

> **tasks:**
> - [ ] update `insight-materialize-estimate-update-lifts-the-criterion-whole`
>   - set: `{status: actioned, addressed_by: decision-case-529, pattern: "An update of an Estimate that named one part of the page — a field or a word — replaced the whole Criterion with the when and then of its Case and set the page pending, so the promise the person signed was lost and nothing read the new text against the old before the librarian's run."}`
>   - sections.Pattern:
>     ```
>     An update of an Estimate that named one part of the page — a field or a word — replaced the whole Criterion with the when and then of its Case and set the page pending, so the promise the person signed was lost and nothing read the new text against the old before the librarian's run.
>     ```
>   - change: `rejected as fixed: an update that names a part changes that part alone since case 378.4; the pattern names the cause in the past tense; the check of a Criterion against its page's purpose not taken (case 529)`

> **ratification:**
> ```
> - decision[case 529][update][insight-materialize-estimate-update-lifts-the-criterion-whole]{ref:insight-materialize-estimate-update-lifts-the-criterion-whole}
> ```
