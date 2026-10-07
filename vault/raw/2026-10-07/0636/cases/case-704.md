## Case 704 — The tag orchestration enters tags.md

> **context:**
> The insight `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` carries the tag `orchestration`, and `vault/wiki/tags.md` holds no row for it. `register_tags` of `guppi/generate.py` adds a row only for an entry of `new_tags`, and for each tag that a page written in the run carries and the list does not hold, it prints that the tag is used but not registered. Case 702 gave the Case file a tag line, which the Spec hook of `rule-spec-write` turns into an entry of `new_tags`, and it left the declaration of `orchestration` to this session (Case 702, Q4 (a)). The Spec hook writes a Case only after a reply that carries a decision line, so this Case also changes a page. The person chose a meaning that follows the purpose of `rule-orchestration`, and an `update` of the insight with only `change`, which `generate` turns into one History line. The insight's missing `addressed_by` stays out of this Case. Case 706 of this session sets `addressed_by` on the same insight in the same run, with a History line of its own. So the `－` line of `then` holds for this Case alone: this Case sets no field and no section of the page, and the two Cases do not clash. This Case changes no code, so no reader goes ahead of its text and no old form is kept.
>
> The Case adds no Estimate, by the person's choice. Three Estimates already check the path from a tag line to a row. `estimate-spec-write-reads-a-new-tag` checks that the Spec hook turns a tag line into an entry of `new_tags`. `estimate-materialize-assembles` checks that the `new_tags` of any Case reach the yaml. `estimate-generate-writes` checks that a tag of `new_tags` lands in `tags.md`. This Case uses that path and changes no step of it, so their Criteria stand. An Insight has no Estimates. Case 703 of this session changes `rule-case-check` and `rule-ledger-write`, which this Case does not change. Once its checks stand, the tag line of this ratified Case makes `orchestration` count as declared in this session, as Case 703.1 and 703.2 set.

> **problem:**
> The tag `orchestration` stands on a live page but not in `tags.md`, and the librarian's run warns about it.

> **recommend:**
> - **What the tag `orchestration` means**
>   - Recommended: (a) the main agent's own work in a session, as in `rule-orchestration`: the Frontier, the dispatch of case-guppi, the showing and signing of a Case, the defers; aliases `оркестрация, оркестровка`.
>   - Answer: agreed, (a).
> - **Which page carries the decision line**
>   - Recommended: (a) the insight `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`, with only `change`; its missing `addressed_by` stays a separate item.
>   - Answer: agreed, (a).
> - **What checks that the tag was added**
>   - Recommended: (a) no new Estimate; `context` names `estimate-spec-write-reads-a-new-tag`, `estimate-materialize-assembles` and `estimate-generate-writes` and says why their Criteria stand.
>   - Answer: agreed, (a).

> **given:**
> `vault/wiki/tags.md`: the list of registered tags, which gains the row.
> **＋** `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`: the page that carries the tag, whose History gains a line.
> **＋** `rule-spec-write`: the rule of the Spec hook, which turns the tag line into an entry of `new_tags`.
> **＋** `guppi/generate.py`: `register_tags` writes the row and warns about a used tag the list does not hold.

> **when:**
> The librarian's run applies the yaml of this session by `guppi/generate.py`.

> **then:**
> `vault/wiki/tags.md` holds a row for `orchestration`, its meaning the main agent's own work in a session, and its aliases `оркестрация, оркестровка`.
> **＋** `guppi/generate.py` prints no warning that `orchestration` is used but not registered.
> **＋** The History of `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out` gains one line that its tag `orchestration` is registered.
> **－** This Case changes no field or section of `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`.

> **tasks:**
> - [ ] tag `orchestration`
>   - meaning: `the main agent's own work in a session: the Frontier, the dispatch of case-guppi, the showing and signing of a Case, the defers`
>   - aliases: `оркестрация, оркестровка`
> - [ ] update `insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out`
>   - change: `its tag orchestration is registered in tags.md (case 704)`

> **ratification:**
> ```
> - decision[case 704][update][insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out]{ref:insight-prespec-onward-a-case-ended-with-no-decision-line-stays-out}
> ```
