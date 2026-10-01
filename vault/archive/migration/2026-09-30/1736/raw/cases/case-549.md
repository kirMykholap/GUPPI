## Case 549 — The texts on `deferred_by` point to `rule-case-protocol` for when a supersede clears a defer

> **context:**
> A page carries `deferred_by`, a list of the Decision pages whose `defer` put off work on it. While that list is not empty, the page stands in `backlog.md`. `guppi generate` adds a decision to the list on a `defer`. It takes the decision out only on the pages that a decision line of the later, superseding Case names (case 467.3). So when one earlier Case put off two pages and a later Case supersedes it but names one of them, the other page keeps the defer and stays in the backlog. Several texts describe this rule. Some say that any `supersedes` clears the field: the glossary row `deferred_by`, two sentences each in `rule-rules-schema` and `rule-entities-schema`, the field text of `rule-insights-schema`, and the module docstring of `guppi/materialize.py`. Others state the condition in full: `rule-case-protocol`, whose Render is `case-schema.md`; the glossary row `ref`, `slug`, `supersedes`, corrected by case 541; a clause of `rule-prespec`; and a sentence of `rule-backlog`. The schema texts are rendered into the `schema.yaml` file of each folder, the glossary into `glossary.md`, and `rule-prespec` into the skill file of `/pre-spec`. At case 541 the person chose to leave the looser texts. The handoff of session 1306 carried them on as an open item, and the person now takes them up. The person chose to keep the condition on one page only, `rule-case-protocol`, and to have every other vault text point to it instead of repeating it.
> The texts were found by Greps of `vault/wiki/`: for `clear` in any case, for `deferred_by`, and for the words of the condition (`only from the pages`, `names its page`, `both names the page`), plus a Grep of `guppi/` for `deferred_by`. History lines, `log.md`, `brief.md` and the Decision pages were not read. Some hits stand as they are. `rule-case-check`, the docstrings of `guppi/prespec.py` and `guppi/casecheck.py`, and the check that `rule-prespec` describes all say what a check reports, not when `generate` clears a defer. The Criteria of `estimate-generate-writes-the-decision-page` and `estimate-prespec-requires-a-backlog-item-decided-on-its-page` state the behaviour that their readings measure, and a promise must state what it checks. The docstrings of `guppi/generate.py` describe the code that clears the field. The docstring of `guppi/materialize.py` is wrong today, not made wrong by this Case: it says a `{supersedes}` takes the slug out of the target's `deferred_by`, and it does not say that `generate` does this or on what condition. It enters the Case as a docstring fix, with no test.
> This Case holds only `update` items, so no vault query was run. It adds no hook and changes no reader of a text. No old form needs to be kept. The Estimates of the changed pages were read, and none is touched. `estimate-glossary-terms-defined` asks that no row contradict its `where` page. The row `deferred_by` and its page `rule-rules-schema` change the same way, and the row `ref`, `slug`, `supersedes` points to its own `where` page. The `-schema-checked` Estimates of the three schemas list what each file holds, not the words of the `deferred_by` text. In the Insight one, the rows of the tables stay whole, one text per field. The Estimates of `rule-prespec` and `rule-backlog` speak of what the check reports and of the render. They do not speak of the reason clause or of when an item leaves. The `given` holds more than seven lines because each changed page stands beside the file it renders into. The Case stays whole because one condition holds for every text: each one points to `rule-case-protocol`. A wrong text is fixed the same way in each place, and no promise is touched.

> **problem:**
> The rule for when a supersede clears a defer is written in full on several pages. Some copies leave out the condition that the superseding Case names the page, so they contradict `rule-case-protocol` and the code. The fix must remove the copies that repeat the rule, so that the condition stands in one place and the other texts point to it.

> **recommend:**
> - **Which texts change**
>   - Recommended: the three pages the item names and the Insight schema too, so that every live text that describes clearing `deferred_by` is covered.
>   - Answer: agreed.
> - **How the texts state the condition**
>   - Recommended: each text states the condition in its own words.
>   - Answer: the person asked why the texts should not point to one place instead. One judgment written in several places is several implementations of it. The next question settled this.
> - **Where the condition stands, and what the other texts say**
>   - Recommended: the condition stands on `rule-case-protocol`, and the texts point to it.
>   - Answer: agreed. The person also asked to take in two remarks. First, the glossary row `ref`, `slug`, `supersedes`, which states the condition in full, also becomes a pointer. Second, the other full copies are checked: each vault text either points to `rule-case-protocol` or stands with a reason given in `context`.

> **given:**
> `entity-glossary` — the table of terms whose rows `deferred_by` and `ref`, `slug`, `supersedes` this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, loaded at the start of every working session
> **＋** `rule-rules-schema` — the Rule schema, which describes `deferred_by`
> **＋** `vault/wiki/rules/schema.yaml` — its render, read by lint and by the writer of a Rule page
> **＋** `rule-entities-schema` — the Entity schema, which describes `deferred_by`
> **＋** `vault/wiki/entities/schema.yaml` — its render, read by lint and by the writer of an Entity page
> **＋** `rule-insights-schema` — the Insight schema, which describes `deferred_by`
> **＋** `vault/wiki/insights/schema.yaml` — its render, read by lint and by the librarian
> **＋** `rule-prespec` — the skill `/pre-spec`, whose check of a backlog item gives the condition as its reason
> **＋** `.claude/skills/pre-spec/SKILL.md` — the render of `rule-prespec`
> **＋** `rule-backlog` — says when an item leaves `backlog.md`
> **＋** `guppi/materialize.py` — its module docstring describes what a `{supersedes}` does to `deferred_by`
> **＋** `guppi/generate.py` — the code that clears `deferred_by`
> **＋** `rule-case-protocol` — the page that states the condition, which the other texts point to

> **when:**
> A reader reads `vault/wiki/glossary.md` at the start of a session, `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml` or `vault/wiki/insights/schema.yaml` when a page is written, `.claude/skills/pre-spec/SKILL.md` when the skill runs, `rule-backlog` or `guppi/materialize.py`, after the librarian's run wrote the rendered files from their pages.

> **then:**
> The rows `deferred_by` and `ref`, `slug`, `supersedes` of `entity-glossary` and of `vault/wiki/glossary.md` say that `guppi generate` clears a defer on a later `supersedes` under the condition that `rule-case-protocol` sets, and do not state the condition themselves.
> **＋** The text on `deferred_by` in `rule-rules-schema`, `rule-entities-schema` and `rule-insights-schema`, and in `vault/wiki/rules/schema.yaml`, `vault/wiki/entities/schema.yaml` and `vault/wiki/insights/schema.yaml`, says the same, both in the field text and in the sentence on ref fields of the Rule and Entity schemas.
> **＋** `.claude/skills/pre-spec/SKILL.md`, rendered from `rule-prespec`, gives the reason for its check of a backlog item by the same pointer, and `rule-backlog` says by the same pointer when an item leaves `backlog.md`.
> **＋** The module docstring of `guppi/materialize.py` says that `generate` takes the slug of a superseded decision out of a target's `deferred_by` under the condition that `rule-case-protocol` sets.
> **＋** `rule-case-protocol` states the condition, and no text that this Case changes states it again.
> **－** The check that `rule-prespec` describes does not change: it reports the same Frontier lines and pages as before.
> **－** `guppi/generate.py` and the docstrings of its code do not change.

> **tasks:**
> - [ ] update `entity-glossary` — the rows `deferred_by` and `ref`, `slug`, `supersedes` point to `rule-case-protocol` for the condition
>   - old: `` written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; ``
>   - new: `` written by `guppi generate` on a defer and cleared by it on a later `supersedes` of that one, under the condition that `rule-case-protocol` sets; ``
>   - old: `` `generate` clears a defer only from the pages that a decision line of the superseding Case names (cases 200.2, 429, 467.3) ``
>   - new: `` `generate` clears a defer under the condition that `rule-case-protocol` sets (cases 200.2, 429, 467.3) ``
>   - change: `the rows deferred_by and ref, slug, supersedes: a supersede clears a defer under the condition that rule-case-protocol sets (case 549)`
> - [ ] update `rule-rules-schema` — the sentence on ref fields and the field `deferred_by` point to `rule-case-protocol`
>   - old: `` cleared on a `supersedes` by `guppi generate`, never by hand ``
>   - new: `` cleared on a `supersedes` by `guppi generate`, under the condition that `rule-case-protocol` sets, never by hand ``
>   - old: `` Written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; ``
>   - new: `` Written by `guppi generate` on a defer and cleared by it on a later `supersedes` of that one, under the condition that `rule-case-protocol` sets; ``
>   - change: `deferred_by is cleared on a supersedes under the condition that rule-case-protocol sets (case 549)`
> - [ ] update `rule-entities-schema` — the sentence on ref fields and the field `deferred_by` point to `rule-case-protocol`
>   - old: `` cleared on a `supersedes` by `guppi generate`, never by hand ``
>   - new: `` cleared on a `supersedes` by `guppi generate`, under the condition that `rule-case-protocol` sets, never by hand ``
>   - old: `` Written by `guppi generate` on a defer, cleared when a later Case `supersedes` that one; ``
>   - new: `` Written by `guppi generate` on a defer and cleared by it on a later `supersedes` of that one, under the condition that `rule-case-protocol` sets; ``
>   - change: `deferred_by is cleared on a supersedes under the condition that rule-case-protocol sets (case 549)`
> - [ ] update `rule-insights-schema` — the field `deferred_by` points to `rule-case-protocol`
>   - old: `` set by `generate`, cleared by a `supersedes` (case 124.2) ``
>   - new: `` set by `generate` and cleared by it on a later `supersedes`, under the condition that `rule-case-protocol` sets (case 124.2) ``
>   - change: `deferred_by is cleared on a supersedes under the condition that rule-case-protocol sets (case 549)`
> - [ ] update `rule-prespec` — the reason of the check of a backlog item points to `rule-case-protocol`
>   - old: `` `generate` clears a defer only from the pages the superseding Case names (case 467.1) ``
>   - new: `` `generate` clears a defer under the condition that `rule-case-protocol` sets (case 467.1) ``
>   - change: `the reason of the backlog check points to rule-case-protocol for when generate clears a defer (case 549)`
> - [ ] update `rule-backlog` — when an item leaves points to `rule-case-protocol`
>   - old: `a Case that decides it names its page on a decision line and supersedes its defer (case 467.3)`
>   - new: `` a Case that decides it supersedes its defer under the condition that `rule-case-protocol` sets (case 467.3) ``
>   - change: `an item leaves when a Case supersedes its defer under the condition that rule-case-protocol sets (case 549)`
> - [ ] `guppi/materialize.py`: the module docstring says that a `{supersedes:case N}` makes the earlier decision `superseded`, and that `generate` takes its slug out of a target's `deferred_by` under the condition that `rule-case-protocol` sets (case 52.3)
> - [ ] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/entities/schema.yaml`
> - [ ] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] `uv run guppi glossary`

> **ratification:**
> ```
> - decision[case 549][update][entity-glossary]{ref:entity-glossary}
> - decision[case 549][update][rule-rules-schema]{ref:rule-rules-schema}
> - decision[case 549][update][rule-entities-schema]{ref:rule-entities-schema}
> - decision[case 549][update][rule-insights-schema]{ref:rule-insights-schema}
> - decision[case 549][update][rule-prespec]{ref:rule-prespec}
> - decision[case 549][update][rule-backlog]{ref:rule-backlog}
> ```
