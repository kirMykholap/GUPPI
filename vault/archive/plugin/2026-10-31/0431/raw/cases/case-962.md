## Case 962 — The open work of Work Mode and of the Spec box stays in the backlog list

> **context:**
> `guppi backlog` writes `vault/wiki/backlog.md`, and it lists each line of the `## Backlog` of each sprint page, the closed ones under `vault/archive/` too. A line of a closed sprint that names a page leaves the list once that page stands `built`, `passed` or `archived` (`deferred` and `finished` of `.guppi/guppi/backlog.py`, read whole, with `item_slugs`, `item_statuses` and `is_done` of `.guppi/guppi/sprint.py`; case 743.4). While it stands, such a line shows only the page's `purpose`, not its own text. The Backlog of the closed sprint `migration` (`vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md`) names on its `rule-work-mode` line the work still open: the test of each Estimate written first and turned green, and the full model the person plans (cases 183, 206, 479.2). Case 961.6 of this session may set `rule-work-mode` `built`, and that line would then leave the list. The same rule already took the `rule-spec-box` line out of the list: `rule-spec-box` stands `built`, and its Purpose says that two cases wait for a second part, a line of that same Backlog. A line that names no page is a note: `item_slugs` reads a page only as a `[[slug]]` before the first ` — `. `deferred` keeps a note of the live sprint always, and a note of a closed sprint until the live sprint holds the same text, whatever the status of any page. `test_a_line_of_a_closed_sprint_leaves_once_taken_or_finished` and `test_the_backlog_of_an_archived_sprint_page_stays_beside_the_live_one` of `.guppi/tests/test_backlog.py` (read at lines 209–276) check this on a made-up vault under `estimate-backlog-renders`. The person chose to keep both pieces of work in sight as note lines on the live sprint page `entity-sprint-plugin`, which already holds such a note for the work taken out of `rule-morph` (case 802). No code changes. The sentence of the Purpose of `rule-work-mode` that says the test of each Estimate written first and the rest of the model are not decided yet stays true. So does the sentence of `rule-spec-box` that points to a line of the Backlog of `entity-sprint-migration`: that line still stands in the archive. A Grep of ``Backlog of `?entity-sprint-migration|second part|written first`` over `vault/wiki/` (with `log.md` and `brief.md` left out) printed `rule-search-leaves-out-decisions.md`, `rule-spec-box.md` and `rule-work-mode.md`. Over `.claude/` it printed `.claude/rules/search-leaves-out-decisions.md`. The hits in the search rules are about an exclusion written first, and they stand. None of the Estimates of `entity-sprint-plugin` checks its Backlog. `estimate-backlog-renders` checks only the mechanism. So the new Estimate on `rule-backlog` reads the live list. As the person said, it is a one-time check of this data, not a promise of lasting behaviour. Whether a one-time Estimate should be told apart from one that promises a behaviour is item C9 of the Frontier, which the main agent takes up after this Case. `rule-backlog` has `core: true` and stands `built`. With a `pending` Estimate it goes back to `draft` at the librarian's run of this session. `guppi check` then gives one more line until a later session reads the Estimate from its Work list. The last brief reports 13 such lines. The method waits for the librarian's run and names the file where its evidence stands, as Case 960 of this session sets it for a method. A Glob `vault/**/estimate-backlog-keeps-*.md` printed nothing, so the slug is free. A Grep of `entity-sprint-plugin|rule-spec-box|rule-work-mode|backlog\.md` over `.guppi/tests/` printed `test_box.py`, `test_backlog.py`, `test_glossary.py`, `test_prespec.py`, `test_ship.py`, `test_sprint.py` and `test_lint.py`. Each one writes its own vault under a temporary folder or names the slug in a string or a docstring, so no test reads the live pages or the live list. Cases 961, 960 and 959 of this session are related: this Case changes no page that they change. The session's ledger holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> A line of a closed sprint's Backlog that names a page leaves the backlog list once that page is `built`, even when it names work beyond the page. The open work of Work Mode would drop out of sight that way, and the second part of the Spec box already has.

> **recommend:**
> - **What happens to the open work of Work Mode?**
>   - Recommended: (a) a note line in the Backlog of the live sprint `entity-sprint-plugin`, in its own words, taken out of `rule-work-mode`.
>   - Answer: agreed, (a).
> - **What happens to the second part of the Spec box?**
>   - Recommended: (a) bring it back the same way as the work of Work Mode, as a note line on the live sprint page.
>   - Answer: agreed, (a).
> - **How is it checked that the list keeps the open work?**
>   - Recommended: (a) a new Estimate on `rule-backlog`, read by hand on the live list after the librarian's run.
>   - Answer: agreed, (a). The person noted that it is a one-time check and asked to discuss telling one-time Estimates apart from those that promise a behaviour; that is a separate Frontier item.

> **given:**
> `entity-sprint-plugin`: the live sprint page, whose `## Backlog` takes the notes.
> **＋** `rule-work-mode` and `rule-spec-box`: the pages the work is taken out of; their text stands.
> **＋** `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md`: the closed sprint page whose Backlog named the work.
> **＋** `rule-backlog`: the rule that keeps a deferred item in sight, the target of the new Estimate.
> **＋** `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`: the new one-time check.
> **＋** `.guppi/guppi/backlog.py` and `vault/wiki/backlog.md`: the script and the list it writes.

> **when:**
> The librarian runs `uv run --project .guppi guppi backlog` over `vault/wiki/` and `vault/archive/`, after the `## Backlog` of `entity-sprint-plugin` holds the notes taken out of `rule-work-mode` and `rule-spec-box`.

> **then:**
> `vault/wiki/backlog.md` holds under `## Deferred` a line with the text of the note on the rest of Work Mode: the test of each Estimate written first and turned green, and the full model the person plans.
> **＋** It holds a line with the text of the note on the second part of the Spec box.
> **＋** Each of these lines stands whatever the status of `rule-work-mode` and of `rule-spec-box`, `built` included.
> **－** The line of `vault/archive/migration/2026-10-10/1555/entities/entity-sprint-migration.md` that names `rule-work-mode` does not keep the work in the list: it may leave once that page stands `built`.

> **tasks:**
> - [ ] update `entity-sprint-plugin`
>   - old: `the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md`
>   - new:
>     ```
>     the categories discussion of session 1119, vault/archive/migration/2026-09-17/1119/raw/categories-discussion.md
>     - The rest of Work Mode past the skill /work: the test of each Estimate written first and turned green, and the full model the person plans; taken out of rule-work-mode (case 962)
>     - The Spec box, its second part: a conserved Spec checked against the pages changed after it was conserved, a Case on such a page built again, ratified again and written into the folder of the conserved Spec, and a conserved Spec taken after other Cases of its session; taken out of rule-spec-box (case 962)
>     ```
>   - change: `the Backlog takes the open work of rule-work-mode and rule-spec-box as notes`
> - [ ] create `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`
>   - ref: `rule-backlog`
>   - kind: `QA`
>   - purpose: `Whether backlog.md shows the open work of Work Mode and the second part of the Spec box, kept as notes of the live sprint page, whatever the status of rule-work-mode and rule-spec-box; a one-time check of this data`
>   - method: `by hand, after the librarian's run of a session in which the Backlog of entity-sprint-plugin holds the notes taken out of rule-work-mode and rule-spec-box: vault/wiki/backlog.md, the file of the repository where the evidence is saved, read against the Criterion in the session whose brief puts the reading under Work, the file named and its lines quoted in the estimate line`
>   - tags: `[sprint, workflow]`
> - [ ] `uv run --project .guppi guppi sprint`
> - [ ] read `estimate-backlog-keeps-the-work-taken-out-of-a-built-page`

> **ratification:**
> ```
> - decision[case 962][update][entity-sprint-plugin]{ref:entity-sprint-plugin}
> - decision[case 962][create][estimate-backlog-keeps-the-work-taken-out-of-a-built-page]{ref:rule-backlog}{tags:sprint,workflow}
> ```
