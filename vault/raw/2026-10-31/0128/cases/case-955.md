## Case 955 — The shape of GUPPI is settled by the sprint plugin

> **context:**
> `decision-case-616` put off a question on `entity-guppi`: whether GUPPI goes on as it is, shrinks to a core, or gives way to native Claude features. The person put it off to go to work, before the sprint `plugin` opened. The backlog lists the item by the page's `purpose`, so it reads as a description of GUPPI and its parts, but the description is not what was put off. The sprint `plugin` has since set that GUPPI ships as a Claude Code plugin, as its goal on `vault/wiki/sprint.md` says. The person chose to close the question as settled by that sprint: GUPPI goes on as a harness and ships as a plugin. The text of `entity-guppi` stays as it is. The page gets an `update` with only `change`, and its decision line carries `{supersedes:case 616}`, so the defer of the page is retired and the item leaves the backlog. The README of the milestone The plugin is not touched; `estimate-sprint-plugin-readme-describes-the-project` speaks of `README.md`, not of this page, so its Criterion stands. The only Estimate of the page, `estimate-guppi-tests-green`, checks the test suite and not the defer, so its Criterion stands, and the person chose a new Estimate that reads the retired defer after the librarian's run. A Grep `entity-guppi\b|entity-guppi\.md` over `.guppi/tests/` printed only `test_glossary.py`, which writes its own copy of the page, so no test reads the changed page live. A Glob `vault/**/*guppi-keeps-no-defer*` printed nothing, so the new slug is free. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> The question of the future shape of GUPPI stands open in the backlog, while the sprint `plugin` already works on the answer that GUPPI goes on and ships as a plugin.

> **recommend:**
> - **What to do with the put-off question**
>   - Recommended: (a) close it as settled by the sprint plugin.
>   - Answer: (a).
> - **Which Estimate checks that the question is closed**
>   - Recommended: (a) a new Estimate on `entity-guppi`, `estimate-guppi-keeps-no-defer-of-its-shape`.
>   - Answer: (a).

> **given:**
> `vault/wiki/entities/entity-guppi.md`: the page of GUPPI, `entity-guppi`, whose defer is retired.
> **＋** `decision-case-616`: the Decision page that put off the question of the shape of GUPPI.
> **＋** `vault/wiki/backlog.md`: the list of the put-off items.
> **＋** `estimate-guppi-keeps-no-defer-of-its-shape`: the new check that the defer is retired.

> **when:**
> After the librarian's run that applies the Case that retires the defer of `decision-case-616`, a reader opens `vault/wiki/entities/entity-guppi.md` and `vault/wiki/backlog.md`.

> **then:**
> The `deferred_by` of `entity-guppi` does not name `decision-case-616`.
> **＋** The `## Deferred` of `vault/wiki/backlog.md` holds no line for `entity-guppi`.
> **－** The `## Purpose` of `entity-guppi` does not change.

> **tasks:**
> - [ ] update `entity-guppi`
>   - change: `the question of the future shape of GUPPI is settled by the sprint plugin: GUPPI goes on as a harness and ships as a Claude Code plugin`
> - [ ] create `estimate-guppi-keeps-no-defer-of-its-shape`
>   - ref: `entity-guppi`
>   - kind: `QA`
>   - purpose: `Whether entity-guppi keeps no defer of the question of its future shape and the backlog lists no line for it, once the librarian's run applies the Case that retires the defer`
>   - method: `by hand, after the librarian's run that applies the Case: vault/wiki/entities/entity-guppi.md and vault/wiki/backlog.md read against the Criterion`
>   - tags: `[harness, workflow]`
> - [ ] read `estimate-guppi-keeps-no-defer-of-its-shape`

> **ratification:**
> ```
> - decision[case 955][update][entity-guppi]{ref:entity-guppi}{supersedes:case 616}
> - decision[case 955][create][estimate-guppi-keeps-no-defer-of-its-shape]{ref:entity-guppi}{tags:harness,workflow}
> ```
