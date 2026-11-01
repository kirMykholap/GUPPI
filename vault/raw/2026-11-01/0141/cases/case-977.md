## Case 977 — The ledger hook refuses a reading or a lesson with a bare link to no page

> **context:**
> The `Stop` hook of `rule-ledger-write` copies the record lines of a reply into the session's ledger, and the librarian later copies the free text of a reading or a lesson into a page as it stands: `Vault.estimate` of `.guppi/guppi/generate.py` puts the result of a reading into `## Result` unchanged. Nothing checks that text for a `[[name]]` outside a code span. Lint reads such a name in the body of a page as a link, so a name that is no page reaches the vault and shows up only in the `guppi check` of the librarian's run. `lesson-ledger-reading-writes-a-bare-wikilink` is the example: its own line, line 19 of the ledger of session 2307, held a bare `[[slug]]`, and the brief of that run reports `lessons/lesson-ledger-reading-writes-a-bare-wikilink: ref: body names slug, which no live or archived page carries` among the 15 lines, exit 1, of its `guppi check` (`## Flags` and `## Readings at the close` of `vault/wiki/brief.md`). Case 978 puts that link into a code span in the `## Root cause` and in the field `root_cause` of the page, and its one-time Estimate reads `guppi check` after the librarian's run. This Case leaves the page to Case 978. The tasks of this Case on `.guppi/guppi/lint.py` move the judgment of a body link into one function and keep its answer on every input but a `[[schema]]` with a `schema.md` in a category folder, which no page holds. So the `when` and `then` of Case 978, which read the lesson by that lint after the librarian's run, stand, as its `context` says. The reading of its new Estimate is an estimate line that this hook judges, and Case 978 has it write `[[slug]]` in a code span, so the hook writes it. This Case judges the whole text of a lesson line, and on the lesson page the field `root_cause` and the section `## Root cause` hold the same text, so the hook covers both places that Case 978 fixes by hand. The plan has had this check since case 264.2: `check_bare_links` of `.guppi/guppi/prespec.py`.
>
> The person chose that the hook refuses such a line, that a link passes when it names a live or archived page, a hub file of `vault/wiki/` or a slug that a `create` decision line of the session creates, and that the hook shares the judgment of `guppi check`. For the claim of one judgment I read `links_of`, `hub_files`, `archived_slugs`, `check_refs` and the lines of `lint()` that build `known` and `hubs` in `.guppi/guppi/lint.py`, `plan_prose`, `known_slugs` and `check_bare_links` in `.guppi/guppi/prespec.py`, and `read_category` and `read_page` in `.guppi/guppi/pages.py`. Lint takes as a page the stem of each file of a category folder but `schema`, since `read_category` skips it, and adds `hub_files` for a body link. `known_slugs` takes each stem of a category folder, `schema` included. The two answer differently on `[[schema]]` when a `schema.md` stands in a category folder. A Glob `vault/wiki/*/schema.md` printed nothing, so they answer alike on the vault as it stands. The person chose the answer of lint, so `prespec.py` changes its answer on that input and no other. A Grep `known_slugs` over `.guppi/` printed `.guppi/guppi/prespec.py` alone, so no other caller changes. In `.guppi/guppi/ledger.py` I read `run`, `refused_readings`, `refused_lessons`, `refused_tags`, `unmarked_lessons` and the module docstring: each refusal of a fresh line follows one pattern. The line is not written, and the stderr line goes out once a stretch for a line of the reply just finished. A line refused for its prefix or its tags is passed to `unmarked_lessons` so that it is not held for its mark. The new refusal follows the same pattern.
>
> The `## Criterion` of each Estimate in the `estimates` of `rule-ledger-write` speaks of another refusal or of the window. `estimate-ledger-write-lifts` stands, since its line "A line that a refusal of `rule-ledger-write` refuses does not land while that refusal holds" already covers a new refusal. The Criterion of `estimate-prespec-catches-bare-wikilinks` stands, since it counts as known only a live or archived page and a hub file, and a schema file is no page. The Criterion of `estimate-lint-finds-a-broken-link`, of `rule-lint`, sets the `ref` judgment of a body `[[…]]` that the `lint.py` task moves into one function; it stands, since lint keeps its answer on every input, a body link to a schema file being no page before and after, and the Criterion counts as known only a live or archived page and a file under `vault/wiki/` by stem or path. The `update` of `rule-ledger-write` adds `.guppi/guppi/lint.py` and `.guppi/tests/test_lint.py` to its `implementation_ref`, since the hook imports the judgment and the new Estimate runs that test, as `tags.py` and `casecheck.py` stand there for judgments the hook imports. No Estimate checks the refusal, so this Case creates `estimate-ledger-write-refuses-a-bare-link-to-no-page`. The block `## rule-ledger-write` of `.guppi/links.md` names among its neighbours `rule-ratification`, `rule-orchestration`, `rule-case-build`, `rule-sprint-close`, `rule-session-start` and `entity-glossary`; none of their purpose lines speaks of the text of a reading or a lesson. The table of ledger lines of `rule-ratification` stands, and its open defer by case 907 concerns `PLAIN_SPRINTS` and is not taken up. `.claude/skills/retro/SKILL.md` has the agent answer a refusal of the ledger hook with the refused lines written again, which holds for this refusal. A Grep `rules/rule-ledger-write` over `.guppi/tests/` printed nothing, so no test reads the live page. `uv run --project .guppi guppi test` printed 1856 passed, 6 skipped, 1 deselected at the last close (brief). The session's ledger holds no `lesson[error]` line, and the lesson of session 2307 gets no mark, since its fix is ratified in another session.

> **problem:**
> A reading or a lesson line can carry a `[[name]]` outside a code span that names no page; the hook writes it, the librarian copies it into a page, and the broken link is found only by `guppi check` after it stands in the vault.

> **recommend:**
> - **Where a bare link to no page is stopped**
>   - Recommended: (a) the ledger hook refuses the line, with a new Estimate on `rule-ledger-write`.
>   - Answer: agreed, (a).
> - **What counts as a page for the hook**
>   - Recommended: (a) a live or archived page, a hub file, or a slug that a `create` decision line of the session creates.
>   - Answer: agreed, (a).
> - **Whether a schema file counts as a page**
>   - Recommended: (a) the answer of `guppi check`: a schema file is no page, for all three readers.
>   - Answer: agreed, (a).

> **given:**
> `rule-ledger-write`: the rule of the ledger hook, whose Purpose names each refusal.
> **＋** `estimate-ledger-write-refuses-a-bare-link-to-no-page`: the new check of this refusal.
> **＋** `.guppi/guppi/ledger.py`: the hook.
> **＋** `.guppi/guppi/lint.py`: the one judgment of the names a link may carry.
> **＋** `.guppi/guppi/prespec.py`: the plan check that imports that judgment.
> **＋** `.guppi/tests/test_ledger.py` and `.guppi/tests/test_lint.py`: the tests of the refusal and of the shared judgment.
> **＋** `rule-one-judgment-one-implementation`: one judgment lives in one module.

> **when:**
> The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds, in a `LEDGER` block of a session with a `hi`, a fresh `estimate[...]` or `lesson[...]` line whose text holds a `[[name]]` outside a code span.

> **then:**
> While the name is neither a live or archived page, nor a hub file of the wiki, nor a slug that a `create` decision line of the session's ledger or of the same `Stop` creates, the line is not written.
> **＋** When the line stands in the reply just finished, the hook exits 2 with one stderr line, told once a stretch, that names the link and asks for the name in a code span or for the slug of a page.
> **＋** A refused line of an earlier text is judged again at every `Stop` without a word, and is written at the first `Stop` where each such name passes.
> **＋** One function of `.guppi/guppi/lint.py` judges the names a link outside a code span may carry; `lint.py` reads the body of a page by it, and `.guppi/guppi/prespec.py` and the hook import it.
> **＋** A file `schema.md` in a category folder is no page for lint, for `.guppi/guppi/prespec.py` or for the hook.
> **－** A lesson line refused for its link is not held for its mark.
> **－** A `[[name]]` inside a code span is not judged.

> **tasks:**
> - [ ] update `rule-ledger-write`
>   - old: `` with no `tags.md` no tag is judged (as set in case 703.2, and in case 827.1). ``
>   - new: `` with no `tags.md` no tag is judged (as set in case 703.2, and in case 827.1). It refuses a fresh reading or lesson line whose text holds a `[[name]]` outside a code span that names no live or archived page, no hub file of `vault/wiki/` and no slug that a `create` decision line of the session creates, judged by the function of `.guppi/guppi/lint.py` that `guppi check` and pre-spec share, with one stderr line for a line of the reply just finished that asks for the name in a code span or for the slug of a page, since the text of such a line reaches a page as it stands and lint reads the name as a broken link (as set in case 977). ``
>   - set:
>     ```
>     implementation_ref: [.guppi/guppi/ledger.py, .guppi/guppi/materialize.py, .guppi/guppi/gate.py, .guppi/guppi/casecheck.py, .guppi/guppi/tags.py, .guppi/guppi/lint.py, .guppi/tests/test_ledger.py, .guppi/tests/test_gate.py, .guppi/tests/test_lint.py, .claude/settings.json]
>     ```
>   - change: `the hook refuses a reading or a lesson line whose text holds a bare link to no page; lint.py and test_lint.py added to implementation_ref`
> - [ ] create `estimate-ledger-write-refuses-a-bare-link-to-no-page`
>   - ref: `rule-ledger-write`
>   - kind: `QA`
>   - purpose: `Whether the ledger hook refuses a reading or a lesson line whose text holds a bare link that names no page, says why only for the reply just finished, and judges the link by the one function that guppi check and pre-spec share`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_lint.py -k bare_link`
>   - tags: `[session, hooks, harness, ledger]`
> - [ ] `.guppi/guppi/lint.py`: one function gives the names a body link may carry — the stem of each page that `read_category` reads, `archived_slugs` and `hub_files` — and one function gives the names of a text's links outside a code span that it does not hold; `lint()` builds the names of a body link by the first in place of its own `known` and `hubs` for the body, and `links_of` and `check_refs` judge a body link by them.
> - [ ] `.guppi/guppi/prespec.py`: `known_slugs` gives way to the function of `lint.py`, and `check_bare_links` judges by it, the slugs of the plan's `create` items kept.
> - [ ] `.guppi/guppi/ledger.py`: a refusal of a fresh `estimate[...]` or `lesson[...]` line by the function of `lint.py`, the slugs of the `create` decision lines of the session's ledger and of the same `Stop` added to the names that pass; its stderr line told once a stretch by `untold`; a lesson line it refuses passed to `unmarked_lessons` with the lines refused for their prefix; a paragraph of the module docstring.
> - [ ] `.guppi/tests/test_ledger.py`: `bare_link` tests — a reading and a lesson with a bare link to no page refused with one stderr line; a link in a code span, to a live page and to a slug a `create` line of the session creates written; a refused line of an earlier text silent; a lesson refused for its link not held for its mark.
> - [ ] `.guppi/tests/test_lint.py`: a `bare_link` test that runs lint on a page body, `check_bare_links` on a plan and the hook on a ledger line over the same texts, a `[[schema]]` with a `schema.md` in a category folder among them, and asserts the three answer alike.
> - [ ] read `estimate-ledger-write-refuses-a-bare-link-to-no-page`

> **ratification:**
> ```
> - decision[case 977][update][rule-ledger-write]{ref:rule-ledger-write}
> - decision[case 977][create][estimate-ledger-write-refuses-a-bare-link-to-no-page]{ref:rule-ledger-write}{tags:session,hooks,harness,ledger}
> ```
