## Case 675 — The open question of the whole-Spec check leaves the backlog

> **context:**
> At its first run in a session, `/pre-spec` sends one `ask-guppi` run to read the ratified Cases against the vault and against each other. One run over a large Spec returns only part of the problems: `lesson-prespec-one-ask-guppi-run-samples-the-spec` records a run over a Spec of some twenty sub-cases that found 10 findings, and a later run over the same Spec that found 12: 8 of them stand on sub-cases that stood in the plan at the first run, which that run did not name; 2 stand on sub-cases written from the first run's findings after that run; and 1 is the fix of a finding of the first run. Case 674 went back to one run, for its cost, and kept the open question as the draft `rule-prespec-judges-the-spec-whole` in the backlog (case 674.3): whether the one run needs help on a large Spec, and whether it also asks what the Cases together leave unanswered. The person chose to remove the item: the one run stays as it is, the draft page is not needed even in the backlog, no question on what the Cases leave open together is added, and the person will look at the cost of a run alone. So this Case deletes the draft page and adds no measurement and no Estimate of the cost.
> The vault's answer: the Case creates no page, so no vault query on a `create` ran. The Frontier line has the source `backlog`, and the page carries `deferred_by` the Decision of case 674.3, so the delete line carries `{supersedes:case 674.3}`, as case 671.2 did for the draft it deleted. The skill of `rule-prespec` does not change: its report still lists what the run did not check and never says the whole Spec is checked, which stays true. The lesson stays as the record of the sample, under `insight-prespec-after-findings-loop-unruled`.
> The frame. A Grep `rule-prespec-judges-the-spec-whole` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 3 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md` and `vault/wiki/log.md`. The librarian writes `backlog.md` and `brief.md` from the pages, and `log.md` is history; they were not read, and they stand. The deleted page carries no promise. `estimate-backlog-renders` checks that `## Deferred` of `backlog.md` lists each live page with `deferred_by`; once the page is gone it is not listed, so its Criterion stays true and stands, and it checks this Case. The `make lint` of the librarian's run checks that no live page links to the deleted page.

> **problem:**
> A draft page holds open in the backlog a question the person no longer wants to keep: whether the one `ask-guppi` run of `/pre-spec` needs help on a large Spec, and whether it asks what the Cases together leave unanswered.

> **recommend:**
> - **What to do with the open question now**
>   - Recommended: (b) record the cost of the run at every pre-spec, and decide later; the draft page stays in the backlog.
>   - Answer: the person chose to remove the item: it is not needed even in the backlog, and the person will look at the measurement alone; (a), with the cost left to the person.
> - **Whether the one run asks what the Cases leave open together**
>   - Recommended: (b) do not add it, and drop it from the open question.
>   - Answer: the person removed the whole item, so no such question is added; (b).
> - **Change**
>   - Asked: at pre-spec the person agreed to the fix of a finding: the `context` gave the second run's 12 findings as if all stood in the Spec the first run read, while the lesson says some stood on sub-cases written after that run, so the lesson's own wording is carried into the `context`.
>   - Taken: the `context` gives the 12 findings as the lesson splits them: 8 on sub-cases the first run read, 2 on sub-cases written from its findings after it, 1 on the fix of one of its findings.

> **given:**
> `rule-prespec-judges-the-spec-whole`: the draft page of the backlog item, which this Case deletes.
> **＋** `rule-page-generation`: the rule of `guppi generate`, which deletes the page and retires its defer.
> **＋** `vault/wiki/backlog.md`: the backlog that lists a deferred page with its purpose.
> **＋** `rule-prespec`: the rule of the one `ask-guppi` run at pre-spec, which stays as it is.

> **when:**
> `guppi generate` of `rule-page-generation` applies the decisions of this Case, and `guppi backlog` writes `vault/wiki/backlog.md`.

> **then:**
> `rule-prespec-judges-the-spec-whole` no longer stands under `vault/wiki/`.
> **＋** `vault/wiki/backlog.md` no longer lists it under `## Deferred`.
> **－** `rule-prespec` does not change: its one `ask-guppi` run gets no help on a large Spec and no question on what the Cases leave open together.

> **tasks:**
> - [ ] delete `rule-prespec-judges-the-spec-whole`
>   - impact: `the draft of the backlog leaves; the one ask-guppi run of /pre-spec stays as rule-prespec sets it, with no help on a large Spec and no question on what the Cases leave open together; the person looks at the cost of a run alone; the defer of case 674.3 is retired by the supersedes mark of this line`

> **ratification:**
> ```
> - decision[case 675][delete][rule-prespec-judges-the-spec-whole]{ref:rule-prespec-judges-the-spec-whole}{supersedes:case 674.3}
> ```
