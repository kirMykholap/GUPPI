## Case 938 — The dispatch names a Case that set the form of a text a check reads

> **context:**
> When the main agent dispatches `case-guppi` for an item, it names the related Cases of the session, and `case-guppi` reads no other Case of the session. Today `## Who builds a Case` of `rule-orchestration` counts a Case as related when it changes a page the item names or sets what happens at the same moment, such as a reply, a hook event or a command. A Case of another subject that sets the form of a text one check reads falls outside that test. In session 1713, Case 927 reworded the `method` of `estimate-harness-make-runs-in-both-shells` so that `guppi check` no longer read a word as a target of the `Makefile`. Case 929 was then dispatched with Case 927 named as not related, and wrote the same kind of wording into the `method` of another Estimate. `/pre-spec` found it, as `lesson-orchestration-dispatch-named-a-case-of-the-same-wording-not-related` records. The person chose to add one kind of related Case: a Case that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind.
>
> The Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch` speaks of this test, and its first `－` line says that a Case outside the old test need not stand in the prompt, which the change makes false. So this Case replaces its Criterion whole. That line is not carried word for word: in the new Criterion it also leaves out a Case that sets no form of a text of a kind the Case of the item may write. Every other line of the old Criterion is carried as it stands. Its `purpose` states the old test and its `method` names a reading of session 2249, so both are set anew. The new `method` waits for the first dispatch under the new Render in which such a Case stands. `insight-case-build-sibling-texts-unchecked-before-the-showing` is about sibling Cases on one subject built apart, which the main agent had named related, so it stands. Case 937.2 also updates `rule-orchestration`, but under `## Plan Mode and the Frontier`. This Case changes one clause under `## Who builds a Case`, and the two texts do not speak of the same thing.
>
> A Grep for `related` over `vault/wiki/` with `log.md` left out printed 13 files: `brief.md`, `orchestration.md`, `lessons/schema.yaml`, the lesson above, `rule-case-protocol`, `rule-synthesis`, `rule-case-build`, `rule-orchestration`, `estimate-orchestration-passes-a-change-to-an-item-not-built`, `rule-lessons-schema`, `estimate-case-build-checks-the-finished-case`, `estimate-case-build-reads-by-need-and-in-parts` and `estimate-orchestration-names-related-cases-in-the-dispatch`. The same Grep over `.claude/` printed `.claude/agents/case-guppi.md`. `rule-case-build` and its render `case-guppi.md` say only that the main agent judges which Cases are related, which stays true. `estimate-orchestration-passes-a-change-to-an-item-not-built` names a Case that wrote a line `**Other Case:**` as a related Case, which stays true. The hits in `rule-case-protocol` and `estimate-case-build-checks-the-finished-case` are History lines. `estimate-case-build-reads-by-need-and-in-parts` speaks of reading the case files of related Cases, which stays true. In `rule-synthesis`, `rule-lessons-schema` and `lessons/schema.yaml` the word is `unrelated` or `related lessons`, which this Case does not touch. A Grep for `orchestration\.md|rule-orchestration` over `.guppi/tests` printed `test_onward.py` and `test_orchestration.py`. `test_orchestration.py` reads only the blocks tagged `showing` and `defer` of the live `orchestration.md`, which this Case leaves as they are. `test_onward.py` only names `orchestration.md` in the text of a hook. The new text carries no pointer to a Case, since `rule-orchestration` has `core: true` and the clause stands inside a long sentence. The session's ledger holds no `lesson[error]` line. The lesson above is of session 1713, so no line carries `{addresses:...}`.

> **problem:**
> The test of related Cases leaves out a Case that set the form of a text a check reads. So a later Case that writes text of that kind is built without it, and it can bring back the form that the earlier Case fixed.

> **recommend:**
> - **Which Cases the test of related Cases adds**
>   - Recommended: (b) a Case that sets the form of a text a check reads, or how the check reads it, when the item's Case may write text of that kind.
>   - Answer: agreed, (b).
> - **How the change is checked**
>   - Recommended: (a) replace the Criterion of `estimate-orchestration-names-related-cases-in-the-dispatch`, with its `purpose` and `method` set anew.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: its Render sets the test of related Cases under `## Who builds a Case`.
> **＋** `vault/wiki/orchestration.md`: rendered from `rule-orchestration`.
> **＋** `estimate-orchestration-names-related-cases-in-the-dispatch`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose item the dispatch names.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the case file of a related Case.

> **when:**
> The main agent dispatches `case-guppi` by an `Agent` call to build the Case of an item of `raw/<date>/<hi HHMM>/frontier.md`, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The prompt of the call names each Case of the session, ratified or already shown, that changes a page the item names or sets what happens at the same moment as the item: the same kind of reply, the same hook event or the same command.
> **＋** The prompt also names each Case of the session, ratified or already shown, that sets the form of a text a check reads, or how the check reads it, when the Case of the item may write text of that kind, such as the `method` of an Estimate.
> **＋** Each such Case stands in the prompt by its id, one sentence on what it sets and which pages it changes, and the path of its case file `raw/<date>/<hi HHMM>/cases/case-<N>.md`.
> **＋** When the item is one of two or more items that one answer of the person took up, the prompt also names each other Case of that batch by its id and its Frontier item, and by the path of its case file where that file stands.
> **＋** The main agent judges which Cases of the session are related, and the prompt does not send `case-guppi` to search the Cases of the session.
> **－** A Case of the session that changes no page the item names, acts at another moment, sets no form of a text of a kind the Case of the item may write and is no Case of the same batch need not stand in the prompt.
> **－** A Case that only writes a text a check reads, and sets no form of it, is not related by that text alone.
> **－** When no Case of the session is related and the item is taken up alone, the prompt names none and holds the Case id, the Frontier item with its source and the person's words.

> **tasks:**
> - [ ] update `rule-orchestration`
>   - old: `that changes a page the item names or sets what happens at the same moment, such as a reply, a hook event or a command, by its id,`
>   - new: `` that changes a page the item names, sets what happens at the same moment, such as a reply, a hook event or a command, or sets the form of a text that a check reads, or how the check reads it, where the Case of the item may write text of that kind, such as the `method` of an Estimate that `uv run --project .guppi guppi check` reads, by its id, ``
>   - change: `a Case that sets the form of a text a check reads, or how the check reads it, is related to an item whose Case may write text of that kind`
> - [ ] update `estimate-orchestration-names-related-cases-in-the-dispatch`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names, acts at the same moment, or sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind, by its id, one sentence on what it sets and the path of its case file, and each other Case of a batch of items the person took up in one answer
>     method: "by hand, after the first dispatch of case-guppi under the new Render of rule-orchestration in which a Case of the session sets the form of a text a check reads and the Case of the item may write text of that kind: the Agent call of that dispatch in its transcript, read against the Criterion; a related Case left unnamed counted in the reading line"
>     ```
>   - change: `the Criterion replaced whole — a Case that sets the form of a text a check reads is related to an item whose Case may write text of that kind; purpose and method set anew`
> - [ ] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
> - [ ] read `estimate-orchestration-names-related-cases-in-the-dispatch`

> **ratification:**
> ```
> - decision[case 938][update][rule-orchestration]{ref:rule-orchestration}
> - decision[case 938][update][estimate-orchestration-names-related-cases-in-the-dispatch]{ref:rule-orchestration}
> ```
