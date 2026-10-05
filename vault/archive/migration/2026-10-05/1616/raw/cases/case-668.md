## Case 668 — A lesson reopens an Insight that a decision of its own session sets actioned

> **context:**
> This Case replaces Case 663 whole, with the same content the person ratified. The first ratification of 663 left a ledger line that creates the Estimate under its old slug `estimate-synthesis-reads-the-status-the-run-sets`, a ledger line cannot be withdrawn, and only a Case under a new number whose lines carry `{supersedes:case 663}` retires it. At synthesis the librarian hangs each new lesson on an Insight of the same root cause. When that Insight is `actioned`, the lesson reopens it, unless the lesson entry carries `addressed_by`, the mark of a decision of its own session that closed its cause (cases 284.4, 385). The librarian does this on `materialize.yaml` before `guppi generate` runs, so it sees the status on disk, while a decision entry of the same yaml can set the same Insight `actioned`. In the librarian run of session 1343 `insight-workflow-case-schema-silent-on-what-the-scripts-accept` was `open` on disk, and the entry of Case 651.3 set it `actioned`. The lesson `lesson-orchestration-defer-acknowledged-without-its-short-form` (ledger line L43, with no mark) joined it by an `update` with no status. `generate` applied the entries in their order: the History of the Insight holds the line of 651.3 and then the line of the new child. The cascade then archived the lesson, since its Insight stood `actioned`. The lesson neither reopened the Insight nor was marked as closed by a decision. The person chose that the librarian counts an Insight as `actioned` when a decision entry of the same yaml sets it so, and that an unmarked lesson then reopens it. The synthesis entries are appended after the decision entries, so the reopening is applied last, and the cascade finds the Insight `open` and leaves the lesson `clustered`. The addressed_by that the decision entry sets is the one a marked lesson is compared with. At /pre-spec the person bounded the Case to one `materialize.yaml`, the yaml of the lesson's own session: a librarian run takes every yaml that `guppi materialize` names, one per unit, and `estimate-generate-cascades` says that `generate` runs the cascade after all entries of a unit, so a decision in the yaml of another unit is not counted. The person left the Insight and the lesson of session 1343 as they stand: reopening the Insight now would leave it `open` with no live child, which the cascade archives at once. Its fix, Case 651.3, also added to `rule-orchestration` the sentence that the reply that shows a short-form defer carries its `LEDGER` block, which is the step the lesson missed. A Grep of `` when it was `actioned` `` over `vault/wiki/` without `decisions/` printed `vault/wiki/rules/rule-synthesis.md`; the same Grep over `.claude/` printed `.claude/agents/librarian-guppi.md`, its Render, which follows by the render. A Grep of `unless a decision of its own session` over `vault/wiki/` without `decisions/` and `.claude/` printed `vault/wiki/entities/entity-glossary.md` and `vault/wiki/glossary.md`; the row of the status of an Insight changes on `entity-glossary`, and `glossary.md` follows by its command. That row reads as if a decision of the same session were enough without the mark. `rule-insights-schema` already says that only the mark keeps an Insight `actioned`, so it stays true and is not changed. `estimate-glossary-terms-defined` stands: the new row names the mark, as its `where` page `rule-insights-schema` does, and contradicts nothing there. Case 660 of this session changes other rows of `entity-glossary`, the rows of `supersedes` and of the status of a Decision, not this one. `estimate-synthesis-keeps-actioned-by-the-mark` stands with its passed result: its Criterion speaks of an Insight that stands `actioned` before the run, and each of its lines stays true. The new case is checked by a new Estimate of its own. `estimate-synthesis-clusters` stands too: its line on a lesson that joins a live Insight says nothing of the status. A Glob `vault/**/*synthesis-reads*` printed nothing, so the new slug is free.

> **problem:**
> The rule of synthesis does not say whether an Insight that a decision entry of the lesson's own `materialize.yaml` sets `actioned` counts as `actioned` for a lesson that joins it. As a result, a lesson with no mark can join such an Insight with no reopening and go to the archive, as if a decision had closed its cause.

> **recommend:**
> - **Which status the librarian reads when a lesson joins an Insight**
>   - Recommended: (a) the status after the run's decisions: an Insight counts as `actioned` when it stands so on disk or when a decision entry of the same run sets it so; an unmarked lesson reopens it, a marked one keeps it `actioned`, and the brief reports the reopening.
>   - Answer: agreed, (a).
> - **The Insight this already happened to**
>   - Recommended: (a) leave the Insight `actioned` and the lesson archived; the Case says why in its `context`.
>   - Answer: agreed, (a).
> - **The glossary row on the status of an Insight**
>   - Recommended: (a) the row names the mark, and says that an Insight a decision of the same run sets `actioned` counts as `actioned`; the glossary file is rebuilt.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) a new Estimate, `estimate-synthesis-reads-the-status-the-run-sets`, read by hand after the first run in which a lesson joins an Insight a decision of the same run sets `actioned`; `estimate-synthesis-keeps-actioned-by-the-mark` stands with its result.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at /pre-spec, whether the scope is the lesson's own yaml, that is its own session, or every yaml of the librarian run; the person chose the lesson's own yaml.
>   - Taken: every text of the Case says a decision entry of the same `materialize.yaml`, the lesson's own session: the name, `problem`, the glossary row, the new Estimate, renamed `estimate-synthesis-reads-the-status-its-yaml-sets`, and its `purpose`; its `method` names the kind of run, not the first one.

> **given:**
> `estimate-synthesis-reads-the-status-its-yaml-sets`: the new check of the status the synthesis reads.
> **＋** `rule-synthesis`: its Render, the condition on which a lesson reopens an Insight.
> **＋** `.claude/agents/librarian-guppi.md`: the file the Render of `rule-synthesis` is rendered into.
> **＋** `entity-glossary`: the row of the status of an Insight.
> **＋** `vault/raw/<date>/<hi HHMM>/materialize.yaml`: the entries of one session, decisions first and synthesis after.
> **＋** `guppi/generate.py`: applies the entries in their order, and its cascade archives the `clustered` lessons of an `actioned` Insight.
> **＋** `vault/wiki/brief.md`: where the librarian reports the synthesis.

> **when:**
> `librarian-guppi`, at synthesis, hangs a lesson entry on an Insight of the same pattern that stands `open` on disk, while an `update` entry of a decision in the same `materialize.yaml` sets that Insight `actioned` with `addressed_by: decision-case-M`, and `guppi/generate.py` then applies the yaml.

> **then:**
> A lesson entry with no `addressed_by` gives an `update` of the Insight with `children` plus the lesson and `set: {status: open}`.
> **＋** After `guppi/generate.py` runs, the Insight stands `open` and the lesson stands `clustered`, not archived.
> **＋** A lesson entry with `addressed_by: decision-case-N` gives an `update` with no `status`: it carries `set: {addressed_by: decision-case-N}` when case N is later than case M, compared number by number, and no `addressed_by` otherwise; the Insight stays `actioned`.
> **＋** `vault/wiki/brief.md` reports the pair beside the synthesis.
> **－** An Insight that is not `actioned` on disk and that no decision entry of the yaml sets `actioned` takes no `status` from the lesson.

> **tasks:**
> - [ ] create `estimate-synthesis-reads-the-status-its-yaml-sets`
>   - ref: `rule-synthesis`
>   - kind: `QA`
>   - purpose: `Whether a lesson that joins an Insight a decision entry of its own materialize.yaml sets actioned reopens it when it carries no addressed_by, and keeps it actioned when it does`
>   - method: `one reading by hand of the yaml, the Insight page and the brief after a librarian run in which a lesson joins an Insight that a decision entry of the same yaml sets actioned; no date`
>   - tags: `[harness, workflow, librarian]`
> - [ ] update `rule-synthesis`
>   - old: `` when it was `actioned` — `set: {status: open}` ``
>   - new: `` when it was `actioned`, on disk or by an `update` entry of a decision in this yaml that sets it `actioned`, whose `addressed_by` is then the one the Insight names (case 668) — `set: {status: open}` ``
>   - change: `an Insight that a decision entry of the same yaml sets actioned counts as actioned at synthesis (case 668)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] update `entity-glossary`
>   - old: `a new Lesson of the same root cause reopens it unless a decision of its own session closed its cause (case 284.4);`
>   - new: `` a new Lesson of the same root cause reopens it unless its entry carries `addressed_by`, the mark of a decision of its own session that closed its cause (case 284.4); an Insight that a decision of the Lesson's own session sets `actioned`, in the same `materialize.yaml`, counts as `actioned` for that Lesson (case 668); ``
>   - change: `the row of the status of an Insight names the mark and the status a decision of the lesson's own session sets (case 668)`
> - [ ] `uv run guppi glossary`
> - [ ] read `estimate-synthesis-reads-the-status-its-yaml-sets`

> **ratification:**
> ```
> - decision[case 668][create][estimate-synthesis-reads-the-status-its-yaml-sets]{ref:rule-synthesis}{tags:harness,workflow,librarian}{supersedes:case 663}
> - decision[case 668][update][rule-synthesis]{ref:rule-synthesis}{supersedes:case 663}
> - decision[case 668][update][entity-glossary]{ref:entity-glossary}{supersedes:case 663}
> ```
