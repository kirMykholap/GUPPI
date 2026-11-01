<!-- approved 03:29:49 · session b91d8531 -->

# Session 0141 — the bare wikilink of a ledger reading line

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

```then
create:
- slug: estimate-ledger-write-refuses-a-bare-link-to-no-page
  ref: rule-ledger-write
  kind: QA
  purpose: Whether the ledger hook refuses a reading or a lesson line whose text holds a bare link that names no page, says why only for the reply just finished, and judges the link by the one function that guppi check and pre-spec share
  method: uv run --project .guppi pytest .guppi/tests/test_ledger.py .guppi/tests/test_lint.py -k bare_link
  tags:
  - session
  - hooks
  - harness
  - ledger
update:
- slug: rule-ledger-write
  replace:
  - old: with no `tags.md` no tag is judged (as set in case 703.2, and in case 827.1).
    new: with no `tags.md` no tag is judged (as set in case 703.2, and in case 827.1). It refuses a fresh reading or lesson line whose text holds a `[[name]]` outside a code span that names no live or archived page, no hub file of `vault/wiki/` and no slug that a `create` decision line of the session creates, judged by the function of `.guppi/guppi/lint.py` that `guppi check` and pre-spec share, with one stderr line for a line of the reply just finished that asks for the name in a code span or for the slug of a page, since the text of such a line reaches a page as it stands and lint reads the name as a broken link (as set in case 977).
  set:
    implementation_ref:
    - .guppi/guppi/ledger.py
    - .guppi/guppi/materialize.py
    - .guppi/guppi/gate.py
    - .guppi/guppi/casecheck.py
    - .guppi/guppi/tags.py
    - .guppi/guppi/lint.py
    - .guppi/tests/test_ledger.py
    - .guppi/tests/test_gate.py
    - .guppi/tests/test_lint.py
    - .claude/settings.json
  change: the hook refuses a reading or a lesson line whose text holds a bare link to no page; lint.py and test_lint.py added to implementation_ref
```

```tasks
- [x] update `rule-ledger-write`
- [x] create `estimate-ledger-write-refuses-a-bare-link-to-no-page`
- [x] `.guppi/guppi/lint.py`: one function gives the names a body link may carry — the stem of each page that `read_category` reads, `archived_slugs` and `hub_files` — and one function gives the names of a text's links outside a code span that it does not hold; `lint()` builds the names of a body link by the first in place of its own `known` and `hubs` for the body, and `links_of` and `check_refs` judge a body link by them.
- [x] `.guppi/guppi/prespec.py`: `known_slugs` gives way to the function of `lint.py`, and `check_bare_links` judges by it, the slugs of the plan's `create` items kept.
- [x] `.guppi/guppi/ledger.py`: a refusal of a fresh `estimate[...]` or `lesson[...]` line by the function of `lint.py`, the slugs of the `create` decision lines of the session's ledger and of the same `Stop` added to the names that pass; its stderr line told once a stretch by `untold`; a lesson line it refuses passed to `unmarked_lessons` with the lines refused for their prefix; a paragraph of the module docstring.
- [x] `.guppi/tests/test_ledger.py`: `bare_link` tests — a reading and a lesson with a bare link to no page refused with one stderr line; a link in a code span, to a live page and to a slug a `create` line of the session creates written; a refused line of an earlier text silent; a lesson refused for its link not held for its mark.
- [x] `.guppi/tests/test_lint.py`: a `bare_link` test that runs lint on a page body, `check_bare_links` on a plan and the hook on a ledger line over the same texts, a `[[schema]]` with a `schema.md` in a category folder among them, and asserts the three answer alike.
- [x] read `estimate-ledger-write-refuses-a-bare-link-to-no-page`
```

## Case 978 — A bare link in the root cause of the bare-link lesson

> **context:**
> `guppi lint` of `.guppi/guppi/lint.py` reads every `[[…]]` in the body of a live page as a link to a page, after `links_of` deletes each code span, and `check_refs` reports a link that no live or archived page carries as a `ref` finding; it reads the frontmatter only for its link fields, and `root_cause` is not one of them. The `## Flags` of `vault/wiki/brief.md` report that `guppi check` printed 15 lines, one of them `lessons/lesson-ledger-reading-writes-a-bare-wikilink: ref: body names slug, which no live or archived page carries`, and that the `## Root cause` of that page, at its line 18, holds the bare `[[slug]]` copied from line 19 of `vault/raw/2026-10-31/2307/ledger.md`. The lesson records that very form: `materialize.py` puts the `root_cause:` text of a lesson line both into the field `root_cause` and into the section `## Root cause`, and `generate` writes them as they stand, so the field holds the same bare link. The field is the purpose line of the page in `.guppi/links.md`, written by `.guppi/guppi/links.py`, and the schema of `rule-lessons-schema` says the section expands the field. Case 973 fixed the same defect on `estimate-link-graph-prints-the-neighbours` by putting the bare link in a code span; this Case does the same on the lesson. The person chose to change the section and the field alike: in each, `[[slug]]` goes into a code span, and the rest of the text, the trigger and the status stand; the History gains the one line that `update` of `generate.py` appends for the `change`, as the `## History` of `rule-lessons-schema` says it is appended by hook. The description of `rule-lessons-schema` says that a Lesson is a recorded fact, not a ratified decision, that does not go through a Case, and that nothing about it is checked again. Both sentences stand. They speak of how a lesson is born and of the fact it records: the ledger hook writes it with no Case, and its trigger is not checked again. This Case leaves the fact as recorded and changes only the form of one link that lint reads, and the one rule of `ratification.md` lets nothing in the vault change without a ratified Decision, as earlier Cases did when they updated lesson pages. The new Estimate is a one-time reading of the data on the sprint page, not a check of the lesson, and the lesson gets no `estimates` field. A `replace` pair cannot do it, since its `old` would hold the bare link, which `check_bare_links` of `.guppi/guppi/prespec.py` reports in the plan; so the `update` writes the section whole by `sections` and the field by `set`, both handled by `update` of `.guppi/guppi/generate.py` for any category, and `SUB_POINT` and `put` of `.guppi/guppi/ratified.py` read a section name with a space. A lesson carries no Estimate, so the check is a new one-time Estimate with `once: true` on the live sprint page `entity-sprint-plugin`, as `rule-estimates-schema` sets for a check of one state of the data; it is read by hand after the librarian's run that applies the `update`, since `guppi check` sees the change only then. `estimate-sprint-plugin-check-finds-no-bare-slug-link` stands: its Criterion speaks only of the page of Case 973. The Purpose of `entity-sprint-plugin` lists the goals of the sprint; it stands, since the new Estimate is no goal and is read before the close. A Glob `vault/**/estimate-sprint-plugin-lesson-*.md` printed nothing, so the slug is free. The block of the lesson in `.guppi/links.md` names one neighbour, `estimate-link-graph-prints-the-neighbours`, whose purpose line speaks of `guppi links` and does not change. A Grep of `lesson-ledger-reading|wiki/lessons` over `.guppi/tests/` printed `test_generate.py` and `test_prespec.py`; each builds a lesson in a temporary folder, and no test reads the live page. This Case changes no code and no hook: whether the ledger hook refuses a reading line with a bare link is Case 977, built at the same time, and this Case does not cover the moment a ledger line is written. Case 977 changes `.guppi/guppi/lint.py` in Work Mode, before the librarian's run of this reading: it moves the judgment of a body link into one function that the hook and `.guppi/guppi/prespec.py` share, and keeps its answer on every input but a `[[schema]]` with a `schema.md` in a category folder. The lesson holds no such link, so lint reads the lesson after that change as it reads it now, and the `when` and `then` of this Case stand. Under Case 977 the hook also refuses an estimate line whose text holds a bare link to no page, so the reading of the new Estimate writes `[[slug]]` in a code span. The lesson stands in the ledger of session 2307, not of this session, so no `addresses` mark is written.

> **problem:**
> A bare `[[slug]]` in the `## Root cause` of `lesson-ledger-reading-writes-a-bare-wikilink` names no page, so `guppi check` reports a `ref` finding at each run, and the field `root_cause` holds the same bare form.

> **recommend:**
> - **What the fix changes on the lesson page**
>   - Recommended: (b) the section and the field alike, the bare `[[slug]]` put in a code span in both.
>   - Answer: agreed, (b).
> - **How the fix is checked**
>   - Recommended: (a) a new one-time Estimate on `entity-sprint-plugin`, read by hand after the librarian's run.
>   - Answer: agreed, (a).

> **given:**
> `lesson-ledger-reading-writes-a-bare-wikilink`: the page whose section and field hold the bare link.
> **＋** `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link`: the new one-time check.
> **＋** `entity-sprint-plugin`: the live sprint page, the target of the new check.
> **＋** `.guppi/guppi/lint.py`: the `ref` class that reads the link.
> **＋** `vault/wiki/`: the live pages that the lint reads.
> **＋** `rule-estimates-schema`: a one-time Estimate targets the live sprint page.

> **when:**
> `uv run --project .guppi guppi check` runs the lint of `.guppi/guppi/lint.py` over the live pages of `vault/wiki/`, after the librarian's run that applies the `update` of `lesson-ledger-reading-writes-a-bare-wikilink`.
> **＋** The last change of the file of `lesson-ledger-reading-writes-a-bare-wikilink` is read by `git log -p -1` on its path.

> **then:**
> It prints no `ref` line for `lesson-ledger-reading-writes-a-bare-wikilink`.
> **＋** The `## Root cause` and the field `root_cause` of `lesson-ledger-reading-writes-a-bare-wikilink` hold `[[slug]]` inside a code span, and the rest of their text as it stood.
> **－** The `## Trigger`, the status and the other fields of `lesson-ledger-reading-writes-a-bare-wikilink` do not change, and its `## History` changes only by the line the update appends.

```then
create:
- slug: estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether guppi check prints no ref line for lesson-ledger-reading-writes-a-bare-wikilink once the bare link of its root cause stands in a code span, in the section and the field, the rest of that page as it stood but the line its History gains
  method: 'by hand, after the librarian''s run that applies the update of lesson-ledger-reading-writes-a-bare-wikilink: the output of uv run --project .guppi guppi check and the output of git log -p -1 -- vault/wiki/lessons/lesson-ledger-reading-writes-a-bare-wikilink.md, the diff of the Root cause and the root_cause field, one line added to the History, and of no other field or section, read against the Criterion, both outputs in the estimate line'
  once: true
  tags:
  - sprint
  - harness
update:
- slug: lesson-ledger-reading-writes-a-bare-wikilink
  set:
    root_cause: 'the main agent wrote a bare `[[slug]]` into the text of an estimate line at the Retro of session 1831, generate copied that text into the ## Result as it stood, and nothing checks the text of a reading for a bare wikilink before it reaches a page, so the librarian''s flag guessed a cause from the page instead of reading the line'
  sections:
    Root cause: 'the main agent wrote a bare `[[slug]]` into the text of an estimate line at the Retro of session 1831, generate copied that text into the ## Result as it stood, and nothing checks the text of a reading for a bare wikilink before it reaches a page, so the librarian''s flag guessed a cause from the page instead of reading the line'
  change: the bare link of the root cause put in a code span, in the section and the field, so lint reads no link to a page
```

```tasks
- [x] update `lesson-ledger-reading-writes-a-bare-wikilink`
- [x] create `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link`
- [ ] read `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link`
```

## Case 979 — The builder recognises a hook, a command and a docstring list as a list and reports its search

> **context:**
> When a Case adds a member to a list that texts spell out one by one, `case-guppi` must search for a member already in that list, so it finds every text that names the members and can update each one. `estimate-case-build-reads-each-list-of-a-new-member` failed at the Retro of session 0431 (ledger line 47 of `vault/archive/plugin/2026-10-31/0431/raw/ledger.md`): the build of Case 956.1 added `guppi libreport` to the `SubagentStop` hooks and ran no such search, so its Case named the module docstring of `.guppi/guppi/cli.py` nowhere. That docstring lists the hook commands; a Grep for `libreport` over that file prints 3 lines, line 3 in that docstring among them. Work Mode later added the command there by hand. The paragraph of case 948.1 was in the agent file at that build: a Grep of its transcript `agent-ad69e15a458d77050.jsonl` for `list that texts spell out one by one` printed 3 lines, all reads of the paragraph, and a Grep for `adds a member|member of a list|new member|already in the list` printed only those reads, so the agent never reasoned about a member. The paragraph names four kinds of list, a key of an item, a kind, a status or a field, and a hook is none of them; and nothing in a finished Case shows whether the search ran. Cases 971 and 976 put the item off. The person chose that the series also names a hook of an event, a command and an item of a list in a comment or docstring of code. The person also chose that `context` names the search, and that the step stays in the check before the summary. This Case changes that sentence of the Render of `rule-case-build`, replaces the Criterion of the failed Estimate, and sets it `pending` with a reading after the first build of a later session whose Case adds a member to a list, since the new text reaches `.claude/agents/case-guppi.md` only at the render of the librarian's run. Its decision line on the Estimate carries one `{supersedes:...}` mark for each of Cases 971 and 976, so both defers are retired. The new Criterion keeps each line of the old one word for word but the `when`, which is replaced on purpose, since its series of kinds of list widens. A Grep for `a key of an item, a kind, a status or a field` over the repository outside `vault/raw/` and `vault/archive/` printed 3 files: `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-reads-each-list-of-a-new-member.md`, so no other text holds the series. A Grep for `case-guppi\.md|rule-case-build\.md|agents/case-guppi` over `.guppi/tests/` printed nothing, so no test reads either file live. In `.guppi/links.md`, the block of `rule-case-build` names `estimate-case-build-checks-the-finished-case`. Its Criterion says that `context` names a search only when the Case rests on it, and it stands: the new sentence names the search as the one that the claim that no text listing the members is missed rests on. The block of the Estimate names `rule-hook-registry` only through its old `method`, which this Case replaces. The block of `.claude/agents/case-guppi.md` names no neighbour that the change makes false. The session's ledger holds no `error` lesson, so no `addresses` mark is written.

> **problem:**
> The builder misses the search for a member already in a list when the list is not one of the four named kinds, and nothing in the Case shows that the search was skipped.

> **recommend:**
> - **What changes so the search runs**
>   - Recommended: (b) name the missed kinds of list (a hook of an event, a command, a list in a comment or docstring of code), and have `context` report the search.
>   - Answer: agreed, (b).
> - **Where the step stands**
>   - Recommended: (a) it stays in the check before the summary.
>   - Answer: agreed, (a).
> - **When the check is read again**
>   - Recommended: (a) read it after the first later build that adds a member to a list.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule whose Render holds the step of the search.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `estimate-case-build-reads-each-list-of-a-new-member`: the failed check of the step, its Criterion replaced whole.
> **＋** `vault/wiki/`: the live pages searched, outside `decisions/`.
> **＋** `.claude/`: the harness searched.
> **＋** `.guppi/guppi/`: the code searched, its comments and docstrings included.
> **＋** `log.md`: the log of the vault, `vault/wiki/log.md`, whose hits are not read.
> **＋** `brief.md`: the brief of the vault, `vault/wiki/brief.md`, whose hits are not read.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that adds a member to a list that texts spell out one by one, such as a key of an item, a kind, a status, a field, a hook of an event, a command or an item of a list in a comment or a docstring of code, and is about to answer with its summary.

> **then:**
> It searches the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already.
> **＋** It reads each hit that lists the members of the list.
> **＋** A hit in a comment or a docstring of code under `.guppi/guppi/` that lists the members is read like a hit in a page.
> **＋** Each text that lists the members and would miss the new member enters the Case, or the `context` of the Case names it and says why it stands.
> **＋** The `context` of the Case names that search: the member it searched for, its pattern, its paths, and each file it printed or the count it printed.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

```then
update:
- slug: rule-case-build
  replace:
  - old: When the Case adds a member to a list that texts spell out one by one — a key of an item, a kind, a status or a field — Grep the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already, since the new member stands in no text yet, and read each hit that lists the members; a hit in a History line, in `log.md` or in `brief.md` is not read; each text that would miss the new member enters the Case, or `context` names it and says why it stands (as set in case 948.1).
    new: When the Case adds a member to a list that texts spell out one by one — a key of an item, a kind, a status, a field, a hook of an event, a command, or an item of a list in a comment or a docstring of code — Grep the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already, since the new member stands in no text yet, and read each hit that lists the members, a comment or a docstring of code included; a hit in a History line, in `log.md` or in `brief.md` is not read; each text that would miss the new member enters the Case, or `context` names it and says why it stands; `context` names that search, with the member it searched for, its pattern, its paths, and each file it printed or the count it printed, since the claim that the Case misses no text that lists the members rests on it (as set in cases 948.1 and 979).
  change: the search for a member already in a list names a hook of an event, a command and a list in a comment or docstring of code, and context names that search
- slug: estimate-case-build-reads-each-list-of-a-new-member
  set:
    status: pending
    purpose: Whether case-guppi, when its Case adds a member to a list that texts spell out one by one, a hook of an event, a command or a list in a comment or docstring of code among them, searches for a member already in the list, enters each text that would miss the new member in the Case or names it in context, and names that search in context
    method: 'by hand, after the first build of case-guppi in a later session whose Case adds a member to a list that texts spell out one by one: the agent transcript of that build under ~/.claude/projects/ read for its search of a member that stands in the list already and the hits it read, and its case file read for each text that lists the members and for the search named in context, both against the Criterion, recorded in one estimate line with the transcript and the case file'
  change: the Criterion replaced whole — the list names a hook of an event, a command and a list in a comment or docstring of code, and context names the search; the purpose and method set anew, the reading after the first build of a later session that adds a member to a list
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] update `estimate-case-build-reads-each-list-of-a-new-member`
- [ ] read `estimate-case-build-reads-each-list-of-a-new-member`
```

## Case 980 — The dispatch that names related Cases is read again in this session

> **context:**
> When the main agent starts `case-guppi` to build the Case of a Frontier item, its prompt names each related Case of the session by its id, one sentence on what it sets and which pages it changes, and the path of its case file, as the dispatch paragraph of the Render of `rule-orchestration` sets it in `## Who builds a Case`. No code checks that prompt; only a reading of the transcript by hand does. `estimate-orchestration-names-related-cases-in-the-dispatch` failed at the Retro of session 0431 (line 46 of `vault/archive/plugin/2026-10-31/0431/raw/ledger.md`): the dispatch of Case 961 named the related Case 960 by its id and path, but its sentence named only the new Estimate of Case 960 and not the pages it changes. Cases 971 and 976 put the Estimate off, and it stands in `backlog.md`, put off in 2 sessions. `rule-estimates-schema` says a `failed` Estimate is debt until a human decides. The person chose to read it again in this session with the Render and the Criterion unchanged, since the text already asks for the pages and the failure was one prompt that left them out. So the `update` sets the Estimate `pending`, writes the Criterion back word for word as the `when` and `then` of this Case, and sets a new `method` that reads, at the Retro of this session, each dispatch of `case-guppi` in the transcript of session 0141, judging only the Cases the Criterion counts as related. The prompt of this very build names Case 979 with the page it changes and the path of its file, and names Cases 977 and 978 with their pages but no path; the main agent judged those two not related, so the method does not count a Case named beyond the related ones. The person also chose to set the `purpose` anew, since it named the id, the sentence and the path but not the pages, which are the part that failed. The decision line carries one `{supersedes:...}` mark for each of Cases 971 and 976, so both defers are retired. The Render of `rule-case-build`, the frame of `case-guppi`, names the related Case by its id, one sentence on what it sets and the path of its case file; it stands, since it sets what the builder reads, and the pages in the sentence serve the main agent's judgment and a builder that may not read the file of a Case built at the same time. In `.guppi/links.md` the block of the Estimate names `rule-orchestration`, `rule-case-protocol`, `rule-estimates-schema` and `estimate-where-to-stop-writes-each-step-whole`; the last three stand there only through the old Result, and none of their purpose lines speaks of the dispatch. A Grep for `names-related-cases` over `.guppi/tests/` printed nothing, so no test reads the page live, and a Grep for `one sentence on what it sets` over `.guppi/guppi/` printed nothing, so no code judges the prompt. The session's ledger holds no `lesson[error]` line, so no `addresses` mark is written.

> **problem:**
> The check that the dispatch names each related Case with the pages it changes failed once and has been put off twice, and its purpose line leaves out the pages that failed.

> **recommend:**
> - **What settles the failed check?**
>   - Recommended: (a) read it again in this session, with no text changed, both defers cleared.
>   - Answer: agreed, (a).
> - **Does the check's purpose line name the pages too?**
>   - Recommended: (a) rewrite the purpose in the same update.
>   - Answer: agreed, (a).

> **given:**
> `estimate-orchestration-names-related-cases-in-the-dispatch`: its `purpose` and `method` change, and its Criterion is written back word for word.
> **＋** `rule-orchestration`: the rule it checks, rendered into `vault/wiki/orchestration.md`.
> **＋** `case-guppi`: the agent the dispatch starts.
> **＋** `raw/<date>/<hi HHMM>/frontier.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the item and the case files the prompt names.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.

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

```then
update:
- slug: estimate-orchestration-names-related-cases-in-the-dispatch
  set:
    status: pending
    purpose: Whether the main agent's prompt to case-guppi names each Case of the session that changes a page the item names, acts at the same moment, or sets the form of a text a check reads, or how the check reads it, where the Case of the item may write text of that kind, by its id, one sentence on what it sets and which pages it changes, and the path of its case file, and each other Case of a batch of items the person took up in one answer
    method: 'by hand, at Retro: each Agent call of the session that dispatched case-guppi for the Case of an item, read in the transcript of the session under ~/.claude/projects/ against the Criterion, only the Cases the Criterion counts as related judged and a Case named beyond them not counted, a related Case left unnamed or named without the pages it changes or the path of its case file counted in the reading line and the transcript named (the dispatches of session 2026-11-01/0141, the dispatch of Case 980 among them)'
  change: the method reads the dispatches of session 0141 at its Retro and the purpose names the pages of a related Case, the Criterion written back unchanged; the defers of cases 971 and 976 retired
```

```tasks
- [x] update `estimate-orchestration-names-related-cases-in-the-dispatch`
- [x] read `estimate-orchestration-names-related-cases-in-the-dispatch`
```

## Case 981 — A summary of case-guppi reaches the main agent only with Built first

> **context:**
> When `case-guppi` finishes a Case, it answers with a summary whose first line is `**Built:**` and the path of the file, and the main agent reads that first line to tell a built Case from a round, a `**Fact:**` answer or a `**Dropped:**` answer. `estimate-orchestration-shows-the-built-case` failed at the Retro of session 0431 (line 45 of `vault/archive/plugin/2026-10-31/0431/raw/ledger.md`): the `case-guppi` of Case 956 answered a change with three paragraphs of prose and `**Built:**` on its fourth line, and the main agent showed that answer as a built Case, where the Render of `rule-orchestration` takes an answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` for a round. Cases 971 and 976 put the Estimate off, and `backlog.md` says it was put off in 4 sessions. The `SubagentStop` check of `rule-case-check` let that answer through: in `.guppi/guppi/casecheck.py`, `subagent` calls `summary_findings` after the files of `cases/` the agent wrote are found by `written_case_files`, and `summary_findings` judges the newest output, from `subagent_outputs`, only when `is_summary` finds it a summary, that is when its first line that is not blank opens with `**Built:**`; any other answer gets no finding on its summary. The person chose to fix the slip where it starts: Case 981.1 makes the same check send back an answer that holds a line opening with `**Built:**` after a first line of other text, once for each text and when the agent wrote a file of `cases/`, so that `case-guppi` answers again with the summary alone, and Case 981.2 sets the failed Estimate `pending` with its Criterion written back word for word and reads it at the Retro of this session; its decision line retires the defers of Cases 971 and 976. The frame of `case-guppi`, `.claude/agents/case-guppi.md` rendered from `rule-case-build`, already says to answer with the summary alone and, on a finding on the summary alone, to answer with the summary again and leave the file as it stands, so it stands. The sentence of the Render of `rule-orchestration` that takes such an answer for a round stays true, and the new check is what keeps it from being met. The new judgment reuses `BUILT_LABEL` and `is_summary` of `.guppi/guppi/casecheck.py`, as `rule-one-judgment-one-implementation` sets it: a Grep for `\*\*Built:\*\*` over `.guppi/guppi/` printed hits in `casecheck.py` alone, so no other module judges a summary. A Grep for `subagent\(|Built|summary_findings|is_summary` over `.guppi/tests/`, `test_casecheck.py` left out, printed nothing, and `test_casecheck.py` builds its files in a temporary folder, so no test that reads a live file reaches the changed code. `test_case_schema.py` imports `casecheck` but calls `check_answer`, which this Case does not change. A Grep for `SubagentStop` over `.claude/` printed `.claude/settings.json`, where `guppi libreport` runs beside the check on the same event; it reads the outputs of the librarian and is not touched. In `.guppi/links.md` the block of `rule-case-check` names `estimate-case-check-sends-back-a-summary-without-the-case-name`, whose Criterion judges the `**Case:**` line of an answer that opens with `**Built:**` and leaves out a round, a `**Fact:**` answer and an answer with no file; it stands, since the new check judges only an answer whose first line does not open with `**Built:**`. The front-matter `purpose` of `rule-case-check` names a summary without the id and the name of its Case; it stays true and is not widened. The `purpose` of `estimate-orchestration-shows-the-built-case` says a Case is built by `case-guppi` and shown by the main agent unchanged; it names no part of the old `method`, so only the `method` is set anew. The answers the new check leaves alone rest on the tests the other checks call: `is_round` and `is_fact` of `.guppi/guppi/casecheck.py`, read whole, know a round by a line opening with `❓` with no Case heading and no `**Fact:**` line before it, and a Fact answer by a line opening with `**Fact:**` before any such line; a Grep for `Dropped` over `.guppi/` printed nothing, so no code judges a `**Dropped:**` answer yet, and the task adds its one constant. `estimate-case-build-writes-the-case`, the check of `rule-case-build`, says in its Criterion that the answer is a summary alone with a first line `**Built:**`, and that sent a finding on its summary alone `case-guppi` answers with the summary again and leaves the file as it stands; its Criterion stands, since the new send-back is a finding on the summary alone that asks for exactly that answer. The check of this file noted that the `then` line of Case 981.2 on an answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` shares most of its words with the `－` line of Case 981.1 on the answers the hook leaves alone; both stand, since the first sets what the main agent shows and is the old Criterion written back word for word, and the second sets which answers the hook does not send back. A Grep for `lesson\[error\]` over the session's ledger printed nothing, so no `addresses` mark is written.

> **problem:**
> An answer of `case-guppi` with prose before its `**Built:**` line reaches the main agent unchecked and is shown as a built Case, and the check of that showing failed and has been put off for four sessions.

> **recommend:**
> - **What settles the failed check?**
>   - Recommended: (a) the hook sends such an answer back, and the check is read again in this session.
>   - Answer: agreed, (a).

### Case 981.1 — The check sends back a summary after text of its own

> **given:**
> `rule-case-check`: its Purpose gains the new send-back.
> **＋** `.guppi/guppi/casecheck.py`: the `SubagentStop` check `guppi casecheck --subagent`, its `subagent` function and module docstring.
> **＋** `.guppi/tests/test_casecheck.py`: the tests of the check.
> **＋** `estimate-case-check-sends-back-a-summary-after-text`: the new check of the send-back.
> **＋** `rule-one-judgment-one-implementation`: the test of a summary lives in one function.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` under `cases/`: the file of a Case that `case-guppi` writes.
> **＋** `.claude/settings.json`: where the hook is registered.

> **when:**
> `case-guppi` stops after it wrote or edited a file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the `SubagentStop` hook `guppi casecheck --subagent` of `.guppi/guppi/casecheck.py`, registered in `.claude/settings.json`, reads its newest output.

> **then:**
> An output whose first line that is not blank does not open with `**Built:**`, and that holds a later line opening with `**Built:**`, its indent set aside, gets a finding that quotes its first line and tells the agent to answer with the summary alone, its first line `**Built:**`, and the hook exits 2.
> **＋** That finding is sent back in the same exit 2 as the findings on the file and on the `**Case:**` line.
> **＋** A summary is known by `is_summary`, a round by `is_round` and a `**Fact:**` answer by `is_fact` of `.guppi/guppi/casecheck.py`, the one test of each that the other checks call, and a `**Dropped:**` answer by its first line that is not blank opening with one constant of that module.
> **－** An output whose text an earlier output of the subagent already holds, trailing spaces aside, is not sent back again for it.
> **－** An output whose first line that is not blank opens with `**Built:**`, a round, a `**Fact:**` answer, a `**Dropped:**` answer and an output with no line opening with `**Built:**` get no such finding.
> **－** A subagent that wrote no file of `cases/` gets no such finding.

```then
create:
- slug: estimate-case-check-sends-back-a-summary-after-text
  ref: rule-case-check
  kind: QA
  purpose: Whether the check of case-guppi sends back an answer that holds a Built line after a first line of other text, once per text, and leaves a summary that opens with Built, a round, a Fact answer and a Dropped answer alone
  method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k summary_after_text
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-case-check
  replace:
  - old: the one reading that `.guppi/guppi/ledger.py` and `.guppi/guppi/generate.py` share (case 703.1).
    new: the one reading that `.guppi/guppi/ledger.py` and `.guppi/guppi/generate.py` share (case 703.1). The check also sends back, once for each text, an answer of `case-guppi` that wrote a file of a Case, that is no round, no `**Fact:**` answer and no `**Dropped:**` answer, and that holds a line opening with `**Built:**` after a first line of other text, so that `case-guppi` answers again with the summary alone, its first line `**Built:**` (as set in case 981.1).
  change: the SubagentStop check sends back an answer with text before its Built line
```

```tasks
- [x] update `rule-case-check`
- [x] create `estimate-case-check-sends-back-a-summary-after-text`
- [x] `.guppi/guppi/casecheck.py`: a function that, for a subagent that wrote a file of `cases/`, judges the newest output by `BUILT_LABEL`, `is_summary`, `is_round`, `is_fact` and a new constant `DROPPED_LABEL`, `**Dropped:**`, the first judgment of a Dropped answer in `.guppi/guppi/`, and gives the finding; `subagent` joins it with the other findings in one exit 2; the module docstring says so beside the paragraph on the name in the summary.
- [x] `.guppi/tests/test_casecheck.py`: tests named `test_subagent_summary_after_text_*` for an answer with prose before `**Built:**` sent back, the same text not sent back twice, a summary that opens with `**Built:**`, a round, a `**Fact:**` answer and a `**Dropped:**` answer passing, and no file written passing.
- [x] read `estimate-case-check-sends-back-a-summary-after-text`
```

### Case 981.2 — The showing of a built Case is read again in this session

> **given:**
> `estimate-orchestration-shows-the-built-case`: its `method` changes, and its Criterion is written back word for word.
> **＋** `rule-orchestration`: the rule it checks, rendered into `vault/wiki/orchestration.md`.
> **＋** `case-guppi`: the agent whose answers the main agent shows.
> **＋** `.claude/skills/grill-me/SKILL.md` and `.claude/skills/wait-what/SKILL.md`: the form of a round and the plain explanation.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`, `raw/<date>/<hi HHMM>/ledger.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the item, the ledger and the file of a Case.
> **＋** `~/.claude/projects/`: the folder of the transcript of the session.
> **＋** `rule-case-check`: the check of a shown Case and of the file of a Case.
> **＋** `rule-prespec-onward`: the hook that counts a Case as ratified and finds a dropped file empty.
> **＋** `estimate-orchestration-starts-ask-guppi-for-a-hook-test`: the check of the start of `ask-guppi` left out of this promise.
> **＋** `/work`, `/box` and `rule-spec-box`: the run in which no Case is built.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: where a fork of that run goes.

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
> **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
> **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
> **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
> **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
> **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into the language of the chat line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in the language of the chat translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in the language of the chat, and a short text in the language of the chat on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
> **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands. In Plan Mode the main agent asks the person no question on it: it sends the other Case to its `case-guppi` by `SendMessage` with the change the line names, and the two Cases are shown together in a batch; in a send of Cases built at the same time it does so after the second pass that `vault/wiki/orchestration.md` sets. Where the `case-guppi` of the other Case answers with a round instead, the round stands in the list of the rounds of the batch, as any round does. In Work Mode it asks the person whether that other Case changes.
> **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
> **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
> **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run --project .guppi guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; outside the start of `ask-guppi` that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads, it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
> **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
> **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
> **－** A start of `ask-guppi` in Work Mode that `estimate-orchestration-starts-ask-guppi-for-a-hook-test` reads is outside this promise.
> **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
> **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
> **－** The main agent writes the heading, the list, the `ratification` and the send of another Case from the summary, and does not read the file of the Case.
> **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
> **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
> **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.

```then
update:
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
    method: 'by hand, at Retro: vault/wiki/orchestration.md read against the Criterion, and the replies of the main agent of the session from each answer of case-guppi to the reply that shows its round or its Case, read in the transcript of the session under ~/.claude/projects/ against the Criterion, a part of the Criterion the session did not meet named as not met, both recorded in one estimate line with the transcript named (the showings of session 2026-11-01/0141)'
  change: the method reads the showings of session 0141 at its Retro, the Criterion written back unchanged; the defers of cases 971 and 976 retired
```

```tasks
- [x] update `estimate-orchestration-shows-the-built-case`
- [x] read `estimate-orchestration-shows-the-built-case`
```
