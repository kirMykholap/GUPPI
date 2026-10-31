## Case 959 — The sprint as a kind gets an Estimate over all sprints

> **context:**
> `entity-sprint` is the MOC of the sprint as a kind: each sprint page `entity-sprint-<id>` is a Leaf under it, and it carries `core: true`, so it ships in the clean version. Its `estimates` is empty. The cascade of `guppi generate` (`cascade` of `.guppi/guppi/generate.py`, read whole) takes the live Estimates of each `draft` or `built` page and skips a page with none, so `entity-sprint` stays `draft` for good. `is_draft_core` of `.guppi/guppi/pages.py` (read whole, with `is_core`) accepts it, so `check_status` of `.guppi/guppi/lint.py` reports it and `guppi ship` writes no clean version while it stands; the brief of the librarian of session 0128 gives the last `guppi check`: "13 lines, exit 1, each a page with `core: true` that stands `draft`", `entity-sprint` among them. The page itself says that it carries no Estimate because the person named none, and that a measure over all sprints goes there when one is named (case 241). The person chose an Estimate on `entity-sprint` over keeping it out of the clean version, over a MOC with no Estimates following its children, and over not counting a draft page with no Estimates; `rule-entities-schema` governs the choice, since its schema says that `built` follows from every Estimate having passed and that the Estimates of a MOC measure what no child owns. The person chose that the Estimate promises at most one live sprint page and each other sprint page in the archive, read on the real vault. Today `vault/wiki/entities/` holds the one live sprint page `entity-sprint-plugin` and `vault/archive/` the one page `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md`. The guard of one live page is `guppi sprint`: its docstring in `.guppi/guppi/sprint.py` says that two sprint pages give one line on stderr, exit 1 and no file written, and `test_two_sprint_pages_are_an_error_and_nothing_is_written` of `.guppi/tests/test_sprint.py` (read whole) asserts it. `estimate-sprint-checks-the-file` of `rule-sprint` already promises that refusal, by its line that two sprint pages are one line on stderr and exit 1, as with `guppi sprint`; so the Criterion of the new Estimate does not promise it again, and only its method runs that test before the reading, as the guard behind the count of live pages (finding 2.2 of `/pre-spec`). `check_method` of `.guppi/guppi/lint.py` (read whole, with `names_a_moc_form`, `names_test_files`, `missing_test_files`, `sibling_names_a_target` and `is_reading`) gives a MOC's Estimate whose method says `by hand` alone a finding while an Estimate of a child names a test file, and `estimate-sprint-plugin-ci-writes-a-clean-branch` of the child names `.guppi/tests/test_ship.py`; a method that names `pytest` with a test file that exists passes, so the method names `.guppi/tests/test_sprint.py`. The reading is taken at the Retro of this session, so the librarian's run of this session sets `entity-sprint` `built` once it passes. The Estimates of `rule-sprint` and `rule-sprint-close` test their code on a scratch vault, and no code changes here, so they stand. `entity-guppi`, its parent, has Estimates of its own, and the cascade reads no child of a page, so it is untouched. A Grep of `entity-sprint\.md|entities/entity-sprint[^-]|"entity-sprint"` over `.guppi/tests/` printed `.guppi/tests/test_sprint_close.py` and `.guppi/tests/test_sprint.py`; both write the page under a temporary folder, so no test reads the live page. A Glob `vault/**/estimate-sprint-keeps-one-live-page.md` printed nothing, so the slug is free. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> `entity-sprint` has `core: true` and no Estimate, so the cascade never sets it `built`, and `guppi ship` refuses for as long as it stands `draft`.

> **recommend:**
> - **How does `entity-sprint` become `built`?**
>   - Recommended: (a) an Estimate over all sprints, on something that holds across all sprints and that no single sprint page owns.
>   - Answer: agreed, (a).
> - **What does the Estimate of `entity-sprint` measure?**
>   - Recommended: (a) at most one live sprint page, and each other sprint page in the archive, read on the real vault at the Retro of this session.
>   - Answer: agreed, (a).

> **given:**
> `estimate-sprint-keeps-one-live-page`: the new check of the sprint as a kind.
> **＋** `entity-sprint`: the MOC of the sprint as a kind, whose Purpose names its Estimate.
> **＋** `vault/wiki/entities/` and `vault/archive/`: where the live and the archived sprint pages `entity-sprint-<id>` stand.
> **＋** `.guppi/tests/test_sprint.py`: the test of the guard of one live sprint page, which the method of the new check runs.
> **＋** `rule-entities-schema`: `built` follows from the Estimates, and a MOC's Estimates measure what no child owns.

> **when:**
> At the Retro of a session, the sprint pages `entity-sprint-<id>` under `vault/wiki/entities/` and under `vault/archive/` are read.

> **then:**
> At most one sprint page `entity-sprint-<id>` stands under `vault/wiki/entities/`.
> **＋** Each other sprint page `entity-sprint-<id>` stands under `vault/archive/`.
> **－** A vault with no live sprint page, between the close of one sprint and the opening of the next, does not fail this.

> **tasks:**
> - [ ] create `estimate-sprint-keeps-one-live-page`
>   - ref: `entity-sprint`
>   - kind: `QA`
>   - purpose: `Whether the vault holds at most one live sprint page and each other sprint page stands in the archive`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_sprint.py -k two_sprint_pages; by hand, at Retro: a Glob of vault/wiki/entities/entity-sprint-*.md and of vault/archive/**/entities/entity-sprint-*.md read against the Criterion`
>   - tags: `[sprint, workflow]`
> - [ ] update `entity-sprint`
>   - old: `This page carries no Estimate yet — the person named none; a measure over all sprints, which no single sprint owns, goes here when one is named (case 241).`
>   - new: `Its Estimate is a measure over all sprints, which no single sprint owns: at most one sprint page is live, and each other one stands in the archive (as set in case 959).`
>   - change: `the sprint as a kind gets its Estimate over all sprints`
> - [ ] read `estimate-sprint-keeps-one-live-page`

> **ratification:**
> ```
> - decision[case 959][create][estimate-sprint-keeps-one-live-page]{ref:entity-sprint}{tags:sprint,workflow}
> - decision[case 959][update][entity-sprint]{ref:entity-sprint}
> ```
