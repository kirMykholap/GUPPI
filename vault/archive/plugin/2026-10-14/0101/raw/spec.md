<!-- approved 02:14:24 · session 28e2bf37 -->

# Session 0101 — sprint plugin

## Case 808 — A case number stands with its word, and a check reports a bare one in the code

> **context:**
> `guppi ship` builds the clean version of GUPPI that other people install, and removes from it each bracket that holds a pointer to a case, a decision or a session. It knows a reference to a case only by the word `case` or `cases` before the number, by `REFS` of `guppi/ship.py`. Many comments and docstrings of `guppi/` give the number alone, such as `# not the journal, not the records (274.1)` in `guppi/generate.py`, `# 169.1: the reason is for the person` in `guppi/gate.py` and `"""59.2: the frontier of the session's folder (73.4).` in `guppi/prespec.py`, so these numbers reach the clean copy. The handoff of session 2118 noted it (`vault/raw/2026-10-13/2118/handoff.md`, Observations), and the brief carried it to this session. The person chose that each bare number is rewritten at its source in the word form, such as `(case 274.1)`, and that `guppi ship` does not learn the bare number: a bracket that holds only a number is also ordinary code, such as `match.group(1)`, which the copy must keep. The person chose that a new check reports a bare number in a comment or a docstring of a Python file and removes nothing. Case 808.1 adds that check and replaces the Criterion of `estimate-clean-branch-writes-a-clean-copy`, and Case 808.2 rewrites the numbers and replaces the Criterion of `estimate-clean-branch-code-holds-pointers-only-in-brackets`, whose old line that no line of `guppi/` changes but a comment or a docstring would be false while 808.1 changes the code of `guppi/ship.py`. Of that Criterion, 808.2 rewrites two lines on purpose: the line on what `--check` prints now names the bare case number, and the line on what changes now binds only the rewording of the bare numbers.
>
> The searches this rests on. A Grep of `guppi/` for `#.*\(\d+([.,]\s?\d+)*\)`, a bracket of numbers in a comment, printed lines in `guppi/generate.py`, `guppi/cleanup.py`, `guppi/casecheck.py`, `guppi/prespec.py`, `guppi/onward.py`, `guppi/materialize.py`, `guppi/lint.py`, `guppi/ledger.py` and `guppi/ratified.py`. A Grep of `guppi/` for `^\s*#\s*\d{2,4}(\.\d+)*\b|#\s+\d{2,4}(\.\d+)*:|"""\d{2,4}(\.\d+)*:|^\s+\d{2,4}(\.\d+)*:`, a comment or a docstring that opens with a number, printed lines in `guppi/gate.py`, `guppi/generate.py` and `guppi/prespec.py`. A Glob `.claude/**/*.py` printed no file, so the new check judges no file of `.claude/`. A Grep of `Makefile`, `pyproject.toml`, `.gitattributes` and `CLAUDE.md` for `#\s*\d{2,4}(\.\d+)*\b|\(\d{2,4}(\.\d+)*([,–-]\s?\d+(\.\d+)*)*\)` printed `.gitattributes`, whose hits are comments that open with a date such as `# 2026-08-17,`; they stand, since the check judges only a Python file. A Grep of `vault/wiki/` for `\((\d{2,4}(\.\d+)*)(, \d{2,4}(\.\d+)*)*\)` printed `brief.md`, `log.md`, `lesson-transcript-keeps-the-text-before-a-tool-call.md`, `estimate-cleanup-moves.md`, `estimate-prespec-catches-a-command-line-off-form.md` and `estimate-synthesis-keeps-actioned-by-the-mark.md`; a Grep for `^type:|^core:` over the four pages printed only their `type` lines, so none carries `core: true` and none ships, and the pages stay out of this Case, which the other open item of the milestone The clean branch rewords.
>
> By `rule-one-judgment-one-implementation` the new check is one judgment. A Grep of `guppi/` for `import (tokenize|ast)\b|from (tokenize|ast) import|get_docstring|tokenize\.COMMENT` printed nothing, and a Grep of `guppi/` for `comment|docstring`, case left aside, printed `guppi/casecheck.py`, `guppi/materialize.py`, `guppi/render.py` and `guppi/ratified.py`; read around each hit, the one judgment of a comment among them is `yaml_comments` of `guppi/materialize.py`, which `guppi/ratified.py` imports and which judges a YAML comment, another language, while `guppi/render.py` speaks of a file that cannot carry a comment and `guppi/casecheck.py` of its own docstring, so the check is no second copy; it builds the case number on `ID` of `guppi/caseid.py`, as `REFS` does. Its one caller is `leftovers` of `guppi/ship.py`, which both `guppi ship <folder>` and `guppi ship --check` run; `outside`, which `guppi/prespec.py` imports for the new text of a page, does not change, so the Criterion of `estimate-prespec-hook-reports-a-pointer-outside-a-bracket`, which says that pre-spec judges by the judgment `guppi ship` runs, stands: a page is no Python file. A Grep of `tests/` for `ship` printed `tests/test_ship.py`, `tests/test_prespec.py`, `tests/test_lint.py` and `tests/test_schemas.py`; `tests/test_ship.py` builds each tree under a temporary folder, `tests/test_lint.py` copies the `Makefile` and runs it with a fake `uv`, and `tests/test_prespec.py` only asserts that pre-spec imports `outside`, so no test reads a live file the change makes fail. The sentence of `rule-lint` that `guppi ship --check` finds a pointer outside its bracket stays true and names the step, not its whole judgment, which `rule-clean-branch` holds, so it stands. Since `guppi ship <folder>` prints the same lines as `--check`, the run of `.github/workflows/prod.yml` also fails on a bare number until 808.2 rewrites it; both run in the Work Mode of this session. `estimate-sprint-plugin-ci-writes-a-clean-branch`, the Estimate of the sprint page, which stands `pending`, speaks of the same ground in two lines of its Criterion: that no text of the clean version holds a reference to a case or a decision, and that a run whose `uv run guppi ship` exits 1 fails and writes nothing to `prod`. Its Criterion stands as it is. The first line is the promise this Case serves: once 808.2 rewrites the bare numbers in the word form, `guppi ship` removes them from the copy. The second line already covers any reason for exit 1, the new one of 808.1 included. Its `method` reads it by hand in a later session of the sprint, on the CI run by a tag `prod-*`, which Case 809 of this session (`vault/raw/2026-10-14/0101/cases/case-809.md`) puts after the librarian's run that applies its pages. Case 809 creates `estimate-clean-branch-pages-hold-pointers-only-in-brackets` with `ref` `rule-clean-branch`, which adds that Estimate to the `estimates` of the page, while 808.1 changes only one sentence of its `## Purpose`. Its new texts and the new sentence of 808.1 say nothing against each other: 809 leaves the code and the lines of `--review` on `guppi/` to this Case, and this Case leaves the pages to 809. The last `make lint` printed 0 lines and exited 0 (`vault/wiki/brief.md`, Readings at the close); after 808.1 it is red on `guppi/` until 808.2 is done.

> **problem:**
> A case number written with no word before it, such as `(274.1)`, is a pointer that `guppi ship` does not see, so it reaches the clean copy, and nothing reports a new one.

> **recommend:**
> - **How a bare case number leaves the clean copy**
>   - Recommended: (b) write each bare number in the word form at its source, by hand in Work Mode, comments and docstrings only; `guppi ship` stays as it is.
>   - Answer: agreed, (b).
> - **Whether a check stops new bare numbers**
>   - Recommended: (b) `guppi ship --check` reports a bare case number in a comment or a docstring of a Python file, read by Python's own tokenizer, and removes nothing.
>   - Answer: agreed, (b).
> - **How the two changes are checked**
>   - Recommended: (a) replace the Criterion of both existing Estimates, one sub-case each.
>   - Answer: agreed, (a).
> - **Whether the check also reports a docstring that opens with a case number**
>   - Recommended: (a) the check also reports a comment or a docstring that opens with a case number followed by a colon, and a comment whose whole text is a case number.
>   - Answer: (a).

### Case 808.1 — guppi ship reports a bare case number in a comment or a docstring

> **given:**
> `guppi/ship.py`: the clean copy and its check, which gains the judgment of a bare case number.
> **＋** `guppi/caseid.py`: `ID`, the grammar of a case number.
> **＋** `tests/test_ship.py`: the tests of the new judgment.
> **＋** `rule-clean-branch`: the rule of the pointer, which names the bare number.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: its Criterion is replaced whole.

> **when:**
> `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run guppi ship --review <folder>` does the same.
> **＋** Or `uv run guppi ship --check` judges the working tree and writes no folder.

> **then:**
> In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
> **＋** It does the same for each comment or docstring that opens with a case number followed by a colon, such as `# 169.1:` or `"""75.2:`, and for each comment whose whole text is a case number, such as `# 786`.
> **－** It removes no bare case number: the copy holds it as written.
> **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number that opens a comment with no colon after it is no finding.

```then
update:
- slug: rule-clean-branch
  replace:
  - old: a bracket that holds no pointer stays.
    new: a bracket that holds no pointer stays. A case number with no word `case` or `cases` before it, such as `(274.1)`, is no form of a pointer, and `guppi ship` does not remove it; in a comment or a docstring of a Python file it exits 1 on each bracket that holds only case numbers, on each comment or docstring that opens with a case number followed by a colon, and on each comment whose whole text is a case number, and it judges no code outside them.
  change: a case number stands with its word; guppi ship reports a bare one in a comment or a docstring of the code
- slug: estimate-clean-branch-writes-a-clean-copy
  set:
    status: pending
    purpose: 'Whether guppi ship writes only the code, the harness and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket and on a bare case number in a comment or a docstring of a Python file, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes'
  sections:
    Criterion: |-
      When:
      `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
      **＋** Or `uv run guppi ship --review <folder>` does the same.
      **＋** Or `uv run guppi ship --check` judges the working tree and writes no folder.

      Then:
      It writes `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
      **＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays as it is.
      **＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
      **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
      **＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
      **＋** In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
      **＋** It does the same for each comment or docstring that opens with a case number followed by a colon, such as `# 169.1:` or `"""75.2:`, and for each comment whose whole text is a case number, such as `# 786`.
      **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
      **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
      **＋** With `--check` it judges each file it would write outside `vault/` — `guppi/`, `.claude/` and the files at the root of the project — but `uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
      **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
      **－** It writes no file that a page without `core: true` renders in full.
      **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
      **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, in `vault/wiki/case-example.md` or the Render of `rule-case-example`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed.
      **－** It removes no bare case number: the copy holds it as written.
      **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number that opens a comment with no colon after it is no finding.
  change: the Criterion replaced whole — guppi ship reports a bare case number in a comment or a docstring of a Python file
```

```tasks
- [x] `guppi/ship.py`: one judgment of a bare case number, built on `ID` of `guppi/caseid.py`, reads the comments and docstrings of a Python file by the standard `tokenize` module and gives the line and what it found; `leftovers` adds its lines for a `.py` file, and the module docstring names it.
- [x] `tests/test_ship.py`: a bracket of case numbers, a comment and a docstring that open with a case number and a colon, and a comment that is a case number alone each exit 1 and stay in the copy; `match.group(1)` in code and a comment that opens with a count are no finding.
- [x] update `rule-clean-branch`
- [x] update `estimate-clean-branch-writes-a-clean-copy`
- [x] read `estimate-clean-branch-writes-a-clean-copy`
```

### Case 808.2 — The code writes each case number with its word

> **given:**
> `guppi/`: the comments and docstrings that give a bare case number.
> **＋** `Makefile`: a root file the check judges with the code, and the target `make test`.
> **＋** `pyproject.toml`: a root file the check judges with the code.
> **＋** `.gitattributes`: a root file the check judges with the code.
> **＋** `rule-clean-branch`: the rule of the pointer.
> **＋** `.claude/`: the harness, whose lines of `--check` stay out of this promise.
> **＋** `CLAUDE.md`: a root file whose lines of `--check` stay out of this promise.
> **＋** `rule-retro`: where a red line of `make lint` goes.
> **＋** `estimate-clean-branch-code-holds-pointers-only-in-brackets`: its Criterion is replaced whole.

> **when:**
> At Retro of the session, `uv run guppi ship --check` judges the working tree, and `uv run guppi ship --review <folder>` builds the clean version into an empty folder.

> **then:**
> `uv run guppi ship --check` prints no line on a file under `guppi/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
> **－** The rewording of the bare case numbers in `guppi/` changes no line but a comment or a docstring, and `make test` has no failing test that it did not have before the change.
> **－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `make lint` it makes is a note for the handoff by `rule-retro`.

```then
update:
- slug: estimate-clean-branch-code-holds-pointers-only-in-brackets
  set:
    status: pending
    purpose: Whether the code and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, and no case number without the word case before it, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs
  change: the Criterion replaced whole — the code writes each case number with its word
```

```tasks
- [x] `guppi/`: each comment and docstring that gives a case number with no word `case` or `cases` before it — in a bracket, such as `(274.1)`, at its opening, such as `# 169.1:` or `"""75.2:`, or alone, such as `# 786` — is rewritten by hand as a pointer in a bracket of its own at the end of its sentence, such as `(case 274.1)`; no code changes.
- [x] update `estimate-clean-branch-code-holds-pointers-only-in-brackets`
- [x] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`
```

## Case 809 — The shipped pages hold each pointer in a bracket of its own

> **context:**
> `guppi ship` builds the clean version of GUPPI that other people install, and the workflow `.github/workflows/prod.yml` writes it to the branch `prod` on a push of a tag `prod-*`. `guppi ship` removes each bracket that holds a pointer to a case, a decision or a session, and exits 1 on each pointer outside such a bracket, so the run writes nothing while one remains. The run of `guppi ship --review` of session 2118, saved in `vault/raw/2026-10-13/2118/ship-review.txt`, printed 196 lines: 82 on a pointer outside a bracket, in 30 pages with `core: true` and in the `schema.yaml` of four categories rendered from four of them, and 114 on a bracket that holds words beside its pointer, 31 of them on `guppi/`. Many of the pointers outside a bracket tell the history of this repository, such as `since case 272` in `rule-claude-md`. Some brackets with words hold what the sentence needs: in `case-schema.md`, the Render of `rule-case-protocol`, the whole definition of `replace`, `reword` and `rename` stands in brackets that end with a case number, so the clean copy would lose it; many others hold the slug of the rule that sets the behaviour, such as `` (`rule-sprint-close`, case 627.1) ``, which the copy would lose too.
>
> The person chose that each pointer outside a bracket moves into a bracket at the end of its sentence together with the words of history that go with it, so each sentence keeps its meaning here and the copy drops only the history; that a bracket that carries a definition is split so that the definition stays outside, and that the slug of a page with `core: true` moves out of its bracket, such as `as rule-sprint-close sets it (case 627.1)`, while a slug of a page that does not ship stays inside; that the code of `guppi ship` does not change; that the CI run by a tag `prod-*` waits for the librarian's run that applies these pages, in a later session of the sprint, where `estimate-sprint-plugin-ci-writes-a-clean-branch` is read by its own `method`; and that one new Estimate on `rule-clean-branch`, read by hand after that librarian's run, checks the pages. A bracket in this Case stands at the end of its clause, before a semicolon, a colon or a comma, as many brackets of these pages already do, and the clause reads whole without it. The brackets with words that hold only history and no definition or shipped slug stand, such as `(the shape before case 103)`, `(case 182, point 5)`, `(case 167, supersedes 157)` and `` (case 56, `lesson-render-governed-file-updated-as-rule-class-file`) ``; the `(cases 59.1–59.3, 59.6)` of `rule-prespec-hook` stands too.
>
> The review run is from before the librarian's run of session 2118, which applied Cases 806 and 807 to `rule-case-protocol`, `rule-case-build`, `rule-orchestration`, `rule-work-mode`, `rule-where-to-stop` and `rule-lint`. The first four were read whole here, and their new text holds its pointers in brackets. A Grep of `rule-where-to-stop.md` and `rule-lint.md` under `vault/wiki/rules/` for `[^(;,] [Cc]ases? \d|[Ss]essions? \d{4}` printed two lines of `rule-lint.md`, both History lines, which `guppi ship` replaces. The `## How it works` of `rule-skill-hi` names a session by the id `1b191eaf`, which is no pointer to `guppi ship`, since its id of a session is four digits; it stands outside this Case, and the reading of `estimate-sprint-plugin-ci-writes-a-clean-branch` may judge it. The update of `rule-page-generation` leaves its `deferred_by` as it stands.
>
> Case 808 of this session rewrites the bare case numbers of `guppi/` and checks the code by `estimate-clean-branch-code-holds-pointers-only-in-brackets`, and the lines of `--review` on `guppi/` are its promise, not this one. Both Cases write to `rule-clean-branch`: Case 808.1 replaces a sentence of its `## Purpose`, and the `create` of this Case adds the new Estimate to its `estimates` field, which `generate` fills from the `ref`; this Case writes no text of that page, so the two do not touch the same sentence. The other pages this Case changes are no pages of Case 808.
>
> At `/pre-spec`, `guppi prespec --check` found that the Frontier line of this item closes a sprint item with this Case while no update of the sprint page stood here. The person chose that this Case updates `entity-sprint-plugin`: the line of the milestone The clean branch says what remains, so the item stays open on the sprint page and comes back to the next Frontier with that remainder. The update leaves the `deferred_by` of that page, which Case 805 wrote, as it stands. Its `context` leaves bare case numbers in pages to this item: the one in a page with `core: true` that this Case meets, `in 59.8` of `rule-claude-md`, is written `case 59.8` here. The new Estimate carries a `ref`, so no vault query of `ask-guppi` was run; a Glob `vault/**/estimate-clean-branch-pages*` printed nothing, so its slug is free, and the tags `ci` and `plugin` stand in `vault/wiki/tags.md`. An `update` of a `Render` touches no Estimate whose only promise is that the file equals the Render. Two Estimates of these pages promise what a reworded sentence says, and their Criteria stand. The Criterion of `estimate-decisions-schema-checked` promises that `vault/wiki/decisions/schema.yaml` says that a new page carries `## Context` only for the short form of a deferred decision and in the two-line body of a Case superseded in its own session, and that the pages written before keep the sections they carry; the new wording, `An older page keeps the sections it carries` and `kept on the older pages that carry it`, says the same, the case numbers only moved into brackets. The Criterion of `estimate-glossary-terms-defined` promises that the terms the Purpose of `entity-glossary` names as not rows stand in no row; the new Purpose names the same terms as not rows, and the pointer only moved to the end of the clause. No other Estimate of these pages speaks of a sentence this Case rewords, since the rewording changes no behaviour. A Grep of `tests/` for `(Path\(__file__\)|REPO|ROOT|project_root\(\))[^\n]*(vault|wiki|Makefile|parents|parent)` printed `tests/test_case_schema.py`, `tests/test_orchestration.py`, `tests/test_schemas.py`, `tests/test_generate.py`, `tests/test_materialize.py` and `tests/test_lint.py`; the first five read the live `schema.yaml` files, `case-schema.md` or `orchestration.md` for the lists of a schema and for the blocks tagged `case`, `showing` and `defer`, which this Case does not touch, and `tests/test_lint.py` reads the `Makefile`, so no test fails on the new text. The last `make lint` printed 0 lines and exited 0 (`vault/wiki/brief.md`, Flags); this Case changes no code it runs. The `given` holds more than seven lines, since one promise covers every page the review run listed.

> **problem:**
> The pages that ship hold pointers outside a bracket, so `guppi ship` exits 1 and the CI run writes no clean branch, and some brackets that `guppi ship` removes hold a definition or the slug of a shipped rule that the sentence needs.

> **recommend:**
> - **How a sentence with a pointer outside a bracket is rewritten**
>   - Recommended: (a) the pointer and its history words go into one bracket at the end of the sentence.
>   - Answer: agreed, (a).
> - **Which brackets with words change**
>   - Recommended: (a) fix the brackets that carry a definition, and move the slug of a shipped page out of its bracket.
>   - Answer: agreed, (a).
> - **Whether the code of `guppi ship` changes too**
>   - Recommended: (a) pages only; the code stays as it is.
>   - Answer: agreed, (a).
> - **When the CI run takes place**
>   - Recommended: (a) after the librarian's run, in a later session of the sprint.
>   - Answer: agreed, (a).
> - **How the rewording is checked**
>   - Recommended: (a) one new Estimate on `rule-clean-branch` for the pages.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the Frontier closes the sprint item with this Case, so the person was asked whether this Case updates `entity-sprint-plugin` so that the line of the milestone The clean branch says what remains, or the item is put off instead; the person agreed to the update. The findings of `/pre-spec` also asked that `context` name `estimate-glossary-terms-defined` and `estimate-decisions-schema-checked` and say that both Criteria hold, and that it correct what it said of Case 808 and `rule-clean-branch`.
>   - Taken: an `update` of `entity-sprint-plugin` rewrites the milestone line with what remains; `context` names the two Estimates and why their Criteria stand, and says that Case 808 and this Case both write to `rule-clean-branch`, on no common sentence.

> **given:**
> `rule-clean-branch`: the rule of the pointer and of the clean version, the target of the new Estimate.
> **＋** `estimate-clean-branch-pages-hold-pointers-only-in-brackets`: the new check of the pages.
> **＋** `vault/wiki/`: the pages with `core: true`, the `schema.yaml` of each category, `case-schema.md`, `orchestration.md` and `glossary.md`.
> **＋** `.claude/`: the harness files rendered from the pages this Case changes.
> **＋** `guppi/`: the code, whose lines belong to `estimate-clean-branch-code-holds-pointers-only-in-brackets`.
> **＋** `entity-glossary`: the terms, reworded.
> **＋** `entity-sprint`: the sprint as a kind, reworded.
> **＋** `entity-sprint-plugin`: the live sprint page, whose milestone line says what remains.
> **＋** `rule-agent-writing`: reworded.
> **＋** `rule-backlog`: reworded.
> **＋** `rule-brief`: reworded, its Render too.
> **＋** `rule-carry-over`: reworded, its Render too.
> **＋** `rule-case-build`: reworded.
> **＋** `rule-case-check`: reworded.
> **＋** `rule-case-example`: reworded.
> **＋** `rule-case-protocol`: reworded, its Render too.
> **＋** `rule-claude-md`: reworded.
> **＋** `rule-cleanup`: reworded.
> **＋** `rule-decisions-schema`: reworded, its Render too.
> **＋** `rule-documentation`: reworded, its Render too.
> **＋** `rule-end-of-work`: reworded.
> **＋** `rule-entities-schema`: reworded, its Render too.
> **＋** `rule-estimates-schema`: reworded, its Render too.
> **＋** `rule-event-log`: reworded.
> **＋** `rule-git-context`: reworded.
> **＋** `rule-insights-schema`: reworded, its Render too.
> **＋** `rule-internal-context`: reworded.
> **＋** `rule-language`: reworded.
> **＋** `rule-ledger-tail`: reworded.
> **＋** `rule-ledger-write`: reworded.
> **＋** `rule-lessons-schema`: reworded, its Render too.
> **＋** `rule-materialize`: reworded.
> **＋** `rule-orchestration`: reworded, its Render too.
> **＋** `rule-page-generation`: reworded.
> **＋** `rule-page-read`: reworded.
> **＋** `rule-page-schemas`: reworded.
> **＋** `rule-permissions`: reworded.
> **＋** `rule-prespec-hook`: reworded.
> **＋** `rule-raw-archive`: reworded.
> **＋** `rule-render-harness`: reworded.
> **＋** `rule-retro`: reworded, its Render too.
> **＋** `rule-retro-commit`: reworded.
> **＋** `rule-retro-onward`: reworded.
> **＋** `rule-rules-schema`: reworded, its Render too.
> **＋** `rule-search-leaves-out-decisions`: reworded.
> **＋** `rule-skill-grill-me`: reworded.
> **＋** `rule-skill-hi`: reworded, its Render too.
> **＋** `rule-skill-sprint-close`: reworded.
> **＋** `rule-skill-sprint-open`: reworded.
> **＋** `rule-spec-capture`: reworded.
> **＋** `rule-spec-reconcile`: reworded.
> **＋** `rule-spec-write`: reworded.
> **＋** `rule-sprint`: reworded.
> **＋** `rule-synthesis`: reworded.
> **＋** `rule-work-mode`: reworded, its Render too.

> **when:**
> `uv run guppi ship --review <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.

> **then:**
> It prints no line on a pointer outside a bracket of its own in a page under `vault/wiki/` with `core: true`, in the `schema.yaml` of a category or in a file of `.claude/` that such a page renders.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as the history of this repository that a pointer names, when a thing was measured or which session a pointer names.
> **＋** No bracket that `--review` lists on those files holds the definition of a term that its sentence needs, or the slug of a page with `core: true` by which its sentence names the rule that sets what it says.
> **－** Each page under `vault/wiki/` keeps every pointer it held, with the words that go with it, in a bracket, and each sentence keeps its meaning in this repository.
> **－** A line on a file under `guppi/` is no part of this promise.

```then
create:
- slug: estimate-clean-branch-pages-hold-pointers-only-in-brackets
  ref: rule-clean-branch
  kind: QA
  purpose: 'Whether the pages with core: true, the schema.yaml of each category and the files of .claude/ rendered from such pages hold each pointer to a case, a decision or a session in a bracket of its own, so that guppi ship --review prints no line on a pointer outside a bracket there and no bracket it removes holds a definition or the slug of a shipped rule that the sentence needs'
  method: 'by hand, after the librarian''s run that applies case 809: the lines of uv run guppi ship --review into an empty temporary folder on vault/wiki/ and .claude/, read against the Criterion'
  tags:
  - ci
  - plugin
update:
- slug: entity-glossary
  replace:
  - old: 'Not rows, by the decision of case 306.3: C4 model'
    new: 'Not rows: C4 model'
  - old: Librarian Report / Session Digest — their decisions stand in the archived ledgers of 2026-09-08 and 2026-09-09.
    new: Librarian Report / Session Digest (by the decision of case 306.3; their decisions stand in the archived ledgers of 2026-09-08 and 2026-09-09).
  - old: '`create` a page (an Estimate is its own `create`, with `ref` on its target, case 193);'
    new: '`create` a page, an Estimate being its own `create` with `ref` on its target (case 193);'
  - old: a page written before case 513 keeps its Context and Given (case 513)
    new: an older page keeps its Context and Given (one written before case 513, case 513)
  - old: for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file (case 513);
    new: for a Case built by `case-guppi`, its Case file (from session 2026-09-27/1819 on, case 513);
  change: each pointer stands in a bracket of its own, a definition outside it
- slug: entity-sprint
  replace:
  - old: its status kept in the record of the close (`rule-sprint-close`, case 632.3);
    new: its status kept in the record of the close, as `rule-sprint-close` sets it (case 632.3);
  change: the slug of rule-sprint-close stands outside the bracket of its pointer
- slug: entity-sprint-plugin
  replace:
  - old: no session data such as the Frontier or the sprint
    new: 'no session data such as the Frontier or the sprint; what remains: once the librarian''s run applies the rewording of the pages (case 809), the owner pushes a tag `prod-*` on a commit of `plugin`, and the CI run it starts is read by its Estimate'
  change: the milestone The clean branch says what remains after the rewording of the pages
- slug: rule-agent-writing
  replace:
  - old: 'the answer first and the not-done named. Until case 272 the rule was the section `## Style` of the Render of `rule-claude-md`: a standing condition with no page and no Estimate.'
    new: the answer first and the not-done named (until case 272 the rule was the section `## Style` of the Render of `rule-claude-md`, a standing condition with no page and no Estimate).
  change: the history of the rule stands in the bracket of its pointer
- slug: rule-backlog
  replace:
  - old: Prevents a deferred item from dropping out of sight. Before case 451 the brief carried at most seven deferred items, and an item cut off the seven stood on no list the next session read; a Spec conserved by `carry` stood only in the brief `carry` wrote.
    new: Prevents a deferred item from dropping out of sight (before case 451 the brief carried at most seven deferred items, and an item cut off the seven stood on no list the next session read; a Spec conserved by `carry` stood only in the brief `carry` wrote).
  - old: so that the Backlog of a closed sprint stays in the list (`rule-sprint-close`, case 628.12)
    new: so that the Backlog of a closed sprint stays in the list, as `rule-sprint-close` sets it (case 628.12)
  change: each pointer stands in a bracket of its own, the slug of rule-sprint-close outside it
- slug: rule-brief
  replace:
  - old: first the line `open the next sprint — no sprint is open since the close of <id>` (`rule-sprint-close`, case 628.8);
    new: first the line `open the next sprint — no sprint is open since the close of <id>`, as `rule-sprint-close` sets it (case 628.8);
  change: the slug of rule-sprint-close stands outside the bracket of its pointer
- slug: rule-carry-over
  replace:
  - old: and `/box` runs it (`rule-spec-box`, case 591).
    new: and `/box` runs it, as `rule-spec-box` sets it (case 591).
  change: the slug of rule-spec-box stands outside the bracket of its pointer
- slug: rule-case-build
  replace:
  - old: Until case 419.2 the agent was `frame-guppi`, which read the frame of a Case the main agent wrote and returned the contradictions only; whether a subagent pays for its tokens and time, the question of cases 403 and 408, is the method of its Estimate.
    new: Whether a subagent pays for its tokens and time is the method of its Estimate (the question of cases 403 and 408; until case 419.2 the agent was `frame-guppi`, which read the frame of a Case the main agent wrote and returned the contradictions only).
  change: the history of the agent stands in the bracket of its pointer
- slug: rule-case-check
  replace:
  - old: 'Until case 419 no script read a Case before its ratification: the hook of `rule-spec-write` checks it only after the person signed, and a fault of the form was found by the person or at pre-spec ([[insight-case-form-chat-form-read-by-no-script]]).'
    new: The hook of `rule-spec-write` checks a Case only after the person signed it (until case 419 no script read a Case before its ratification, and a fault of the form was found by the person or at pre-spec, [[insight-case-form-chat-form-read-by-no-script]]).
  change: the history of the check stands in the bracket of its pointer
- slug: rule-case-example
  replace:
  - old: Until case 717.1 the examples stood in `case-schema.md`, the Render of [[rule-case-protocol]], which `case-guppi` reads whole on every dispatch, a dispatch that answers only with rounds included, and every later turn of the dispatch read them again from the cache. Here they stand apart, and
    new: The examples stand apart from `case-schema.md`, the Render of [[rule-case-protocol]], which `case-guppi` reads whole on every dispatch, a dispatch that answers only with rounds included (until case 717.1 they stood there, and every later turn of the dispatch read them again from the cache). Here
  change: the history of the examples stands in the bracket of its pointer
- slug: rule-case-protocol
  replace:
  - old: Until case 595 `/hi` loaded the file into the main agent's context with what the main agent does and the one rule; those moved to `rule-orchestration` and `rule-ratification`, with the child `rule-atomicity` and the Estimates of the behaviours that moved, so the main agent no longer carries the form of a Case it does not build. Until case 273 the Render was a section of `CLAUDE.md` and the schema a file edited by hand; the two said the same thing twice and were signed twice.
    new: What the main agent does and the one rule stand in `rule-orchestration` and `rule-ratification`, with the child `rule-atomicity`, so the main agent does not carry the form of a Case it does not build (until case 595 `/hi` loaded this file into the main agent's context with them, and they moved there with the Estimates of the behaviours that moved; until case 273 the Render was a section of `CLAUDE.md` and the schema a file edited by hand, so the two said the same thing twice and were signed twice).
  - old: a task that waits for the person's word before it runs opening its text with `stop:` (`rule-where-to-stop`, case 531.7);
    new: a task that waits for the person's word before it runs opening its text with `stop:`, as `rule-where-to-stop` sets it (case 531.7);
  - old: or pre-spec reports the pair — case 543)
    new: or pre-spec reports the pair) (case 543)
  - old: a slug goes through `rename`, case 274.1)
    new: a slug goes through `rename`) (case 274.1)
  - old: '`origin`, History and Result kept — case 258.1)'
    new: '`origin`, History and Result kept) (case 258.1)'
  - old: which the librarian runs and the command ticks (`rule-sprint-close`, case 628.1)
    new: which the librarian runs and the command ticks, as `rule-sprint-close` sets it (case 628.1)
  change: each pointer stands in a bracket of its own; the definitions of replace, reword and rename and the slugs of shipped rules stand outside it
- slug: rule-claude-md
  replace:
  - old: The section "Migration mode", carried from the hand-written file of 2026-09-12, left with case 288.3, each of its items a Rule with a Render of its own by then; "Commands" left with it — `make style` before a commit is `rule-retro`'s, and "no new dependencies" came with the file in 59.8 and was never decided on its own. `rule-language` and `rule-agent-writing` have this page as their parent since case 272. `rule-case-protocol` was a child from case 66 to case 273, when its Render became `case-schema.md` and its parent `rule-plan-mode`.
    new: '`rule-language` and `rule-agent-writing` have this page as their parent (since case 272; the section "Migration mode", carried from the hand-written file of 2026-09-12, left with case 288.3, each of its items a Rule with a Render of its own by then, and "Commands" left with it — `make style` before a commit is `rule-retro`''s, and "no new dependencies" came with the file in case 59.8 and was never decided on its own; `rule-case-protocol` was a child from case 66 to case 273, when its Render became `case-schema.md` and its parent `rule-plan-mode`).'
  change: the history of the page stands in the bracket of its pointers
- slug: rule-cleanup
  replace:
  - old: and `guppi sprint-close` at the close of a sprint (`rule-sprint-close`, case 627.1).
    new: and `guppi sprint-close` at the close of a sprint, as `rule-sprint-close` sets it (case 627.1).
  change: the slug of rule-sprint-close stands outside the bracket of its pointer
- slug: rule-decisions-schema
  replace:
  - old: from a target page's `deferred_by` (a deferred decision, case 52.3),
    new: from the `deferred_by` of the target page of a deferred decision (case 52.3),
  - old: A page written before case 513 keeps the sections it carries and is not rewritten (case 513).
    new: An older page keeps the sections it carries and is not rewritten (one written before case 513, case 513).
  - old: but for one that a live page names in `deferred_by` or `addressed_by` (`rule-sprint-close`, case 627.1).
    new: but for one that a live page names in `deferred_by` or `addressed_by`, as `rule-sprint-close` sets it (case 627.1).
  - old: for a Case built by `case-guppi` from session 2026-09-27/1819 on, its Case file `cases/case-<N>.md` with every section, N the id of the top-level Case; once the session is archived
    new: for a Case built by `case-guppi`, its Case file `cases/case-<N>.md` with every section, N the id of the top-level Case (from session 2026-09-27/1819 on). Once the session is archived
  - old: and in the two-line body of a Case superseded in its own session (case 299.4); kept on the pages written before case 513; any other Case keeps it in its Case file (case 513).
    new: and in the two-line body of a Case superseded in its own session (case 299.4), and kept on the older pages that carry it (written before case 513); any other Case keeps it in its Case file (case 513).
  - old: absent on a short-form defer and on the pages written before case 544 (case 544.8).
    new: absent on a short-form defer and on the older pages written without it (before case 544, case 544.8).
  - old: 'written by `generate`, before case 513, on the page of a Case that had one: the pages of Cases before 201 carry it by the model of case 52.1, and the pages from case 376 on by case 378.3; the pages of Cases 201 to 375 carry none. A page written after case 513 carries none, and the Case file holds it (case 513).'
    new: 'kept only on older pages that `generate` wrote with it (before case 513, on the page of a Case that had one: the pages of Cases before 201 carry it by the model of case 52.1, and the pages from case 376 on by case 378.3; the pages of Cases 201 to 375 carry none). A newer page carries none, and the Case file holds it (case 513).'
  - old: 'Only on pages written before case 72, which keep it: the Case''s `when`. A page written after case 72 has no `## When` (case 72.2).'
    new: 'Only on older pages, which keep it: the Case''s `when` (written before case 72). A newer page has no `## When` (case 72.2).'
  - old: 'Only on pages written before case 201.2, which keep it: one `- [[estimate-x]] § case N` line per block the Case wrote under the shape before case 193. A page written after carries none:'
    new: 'Only on older pages, which keep it: one `- [[estimate-x]] § case N` line per block the Case wrote in an older shape (written before case 201.2, in the shape before case 193). A newer page carries none:'
  change: each pointer stands in a bracket of its own with the history it names, the slug of rule-sprint-close outside it
- slug: rule-documentation
  replace:
  - old: '`vault/raw/<date>/<hi HHMM>/handoff.md` (the session''s folder, case 73),'
    new: '`vault/raw/<date>/<hi HHMM>/handoff.md` in the session''s folder (case 73),'
  - old: the command runs `guppi cleanup` itself (`rule-sprint-close`, case 628.1).
    new: the command runs `guppi cleanup` itself, as `rule-sprint-close` sets it (case 628.1).
  - old: with the closed sprint marked (`rule-sprint`, case 743.5).
    new: with the closed sprint marked, as `rule-sprint` sets it (case 743.5).
  - old: live or under `vault/archive/` (`rule-backlog`, case 632.2).
    new: live or under `vault/archive/`, as `rule-backlog` sets it (case 632.2).
  change: the session's folder and the slugs of shipped rules stand outside the brackets of their pointers
- slug: rule-end-of-work
  replace:
  - old: and before the librarian (`rule-spec-box`, case 591).
    new: and before the librarian, as `rule-spec-box` sets it (case 591).
  change: the slug of rule-spec-box stands outside the bracket of its pointer
- slug: rule-entities-schema
  replace:
  - old: seen by Obsidian since case 148.1 (case 166.1)
    new: seen by Obsidian (since case 148.1; case 166.1)
  change: each pointer stands in a bracket of its own
- slug: rule-estimates-schema
  replace:
  - old: '`purpose`, `method` and `checked` are the fields of the model of case 182: one line each.'
    new: '`purpose`, `method` and `checked` are one line each (the fields of the model of case 182).'
  - old: Written from the Case since case 193 (case 350).
    new: Written from the Case (since case 193; case 350).
  change: each pointer stands in a bracket of its own
- slug: rule-event-log
  replace:
  - old: a refused call leaves no mark. Until case 136.1 the three skills wrote them through a `!` substitution where `CLAUDE_SESSION_ID` is empty, so every mark read `--------` (case 136.1).
    new: a refused call leaves no mark (until case 136.1 the three skills wrote them through a `!` substitution where `CLAUDE_SESSION_ID` is empty, so every mark read `--------`).
  - old: '**A limit lifted.** Until case 111 the `hi` line carried `--------` and the ledger hook looked for a `hi` after the last `session-start` of its own session, so two sessions open at once could not be told apart; on 2026-09-14 a session restored by `resume` in the same second took the `hi` of the session that typed it. With the stamp on the `hi` line a `hi` of one session never belongs to another (case 111.1).'
    new: '**A limit lifted.** With the stamp on the `hi` line a `hi` of one session never belongs to another, so two sessions open at once are told apart (until case 111 the `hi` line carried `--------` and the ledger hook looked for a `hi` after the last `session-start` of its own session, and on 2026-09-14 a session restored by `resume` in the same second took the `hi` of the session that typed it; case 111.1).'
  change: the history of the marks stands in the bracket of its pointer
- slug: rule-git-context
  replace:
  - old: 'From case 528 to case 787 the repository had no remote: `origin` had been the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start. Since case 787 `origin` is the public repository `GUPPI` on GitHub, and `/hi` still runs no `git pull`.'
    new: '`/hi` runs no `git pull` (from case 528 to case 787 the repository had no remote: `origin` had been the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start; since case 787 `origin` is the public repository `GUPPI` on GitHub).'
  change: the history of the remote stands in the bracket of its pointers
- slug: rule-insights-schema
  replace:
  - old: which archives it (`rule-sprint-close`, case 627.2); a recurrence
    new: which archives it as `rule-sprint-close` sets it (case 627.2); a recurrence
  - old: it is kept for the recurrence until the close of its sprint, which archives it (`rule-sprint-close`, case 627.2).
    new: it is kept for the recurrence until the close of its sprint, which archives it as `rule-sprint-close` sets it (case 627.2).
  change: the slug of rule-sprint-close stands outside the brackets of its pointers
- slug: rule-internal-context
  replace:
  - old: '`orchestration.md` and `ratification.md` are listed since case 595, in place of `case-schema.md`, listed from case 273: they reach'
    new: '`orchestration.md` and `ratification.md` are listed in place of `case-schema.md` (since case 595; `case-schema.md` was listed from case 273): they reach'
  - old: '`glossary.md` is listed since case 288.1: it left the `@` import of `CLAUDE.md`, which every subagent loads and none of them needs.'
    new: '`glossary.md` is listed here and not in the `@` import of `CLAUDE.md`, which every subagent loads and none of them needs (since case 288.1).'
  - old: '`where-to-stop.md` is listed after `orchestration.md` since case 689.1:'
    new: '`where-to-stop.md` is listed after `orchestration.md` (since case 689.1):'
  change: each pointer stands in a bracket of its own
- slug: rule-language
  replace:
  - old: '— English and Russian in this project (case 476.4). Until case 272 the rule was a section of the Render of `rule-claude-md`: a standing condition with no page and no Estimate.'
    new: — English and Russian in this project (case 476.4; until case 272 the rule was a section of the Render of `rule-claude-md`, a standing condition with no page and no Estimate).
  change: the history of the rule stands in the bracket of its pointer
- slug: rule-ledger-tail
  replace:
  - old: Shows at `/hi`, and at `/retro` since case 126, every ledger line
    new: Shows at `/hi` and at `/retro` (since case 126) every ledger line
  change: the pointer stands in a bracket of its own
- slug: rule-ledger-write
  replace:
  - old: opens the next sprint first (`rule-sprint-close`, case 628.3).
    new: opens the next sprint first, as `rule-sprint-close` sets it (case 628.3).
  change: the slug of rule-sprint-close stands outside the bracket of its pointer
- slug: rule-lessons-schema
  replace:
  - old: until the close of its sprint archives a `new` lesson of kind `error` (`rule-sprint-close`, case 627.2).
    new: until the close of its sprint archives a `new` lesson of kind `error`, as `rule-sprint-close` sets it (case 627.2).
  - old: or, a `new` Lesson of kind `error`, at the close of its sprint (`rule-sprint-close`, case 627.2).
    new: or, a `new` Lesson of kind `error`, at the close of its sprint, as `rule-sprint-close` sets it (case 627.2).
  change: the slug of rule-sprint-close stands outside the brackets of its pointers
- slug: rule-materialize
  replace:
  - old: so that the session that opens a sprint belongs to it (`rule-sprint-close`, case 628.3).
    new: so that the session that opens a sprint belongs to it, as `rule-sprint-close` sets it (case 628.3).
  change: the slug of rule-sprint-close stands outside the bracket of its pointer
- slug: rule-orchestration
  replace:
  - old: The session that closes a sprint follows the skill `/sprint-close`, and the session that opens the next sprint the skill `/sprint-open`, which load only in those sessions (`rule-skill-sprint-close`, `rule-skill-sprint-open`, case 743.8).
    new: The session that closes a sprint follows the skill `/sprint-close` of `rule-skill-sprint-close`, and the session that opens the next sprint the skill `/sprint-open` of `rule-skill-sprint-open`, which load only in those sessions (case 743.8).
  - old: whether each finding of `ask-guppi` not closed is fixed or left (`rule-prespec`, case 634.2)
    new: whether each finding of `ask-guppi` not closed is fixed or left, as `rule-prespec` sets it (case 634.2)
  - old: since the record of a Case takes the marks of all its lines (`rule-page-generation`, case 673).
    new: since the record of a Case takes the marks of all its lines, as `rule-page-generation` sets it (case 673).
  change: the slugs of shipped rules stand outside the brackets of their pointers
- slug: rule-page-generation
  replace:
  - old: a milestone item leaves its milestone only by a Case (`rule-sprint`, case 539.1).
    new: a milestone item leaves its milestone only by a Case, as `rule-sprint` sets it (case 539.1).
  change: the slug of rule-sprint stands outside the bracket of its pointer
- slug: rule-page-read
  replace:
  - old: — in session 0051 an agent read the order of the `Stop` hooks from the History of `rule-hook-registry` ([[lesson-hooks-matching-hooks-of-one-event-run-in-parallel]]).
    new: — an agent read the order of the `Stop` hooks from the History of `rule-hook-registry` (in session 0051, [[lesson-hooks-matching-hooks-of-one-event-run-in-parallel]]).
  change: the session stands in the bracket of the lesson
- slug: rule-page-schemas
  replace:
  - old: Prevents the shape of a page category from living in a file nobody ratified. Until case 304 the six `schema.yaml` and their `schema.md` stood outside the graph — no `purpose`, no History, no Estimate, changed by hand by an `update` with `file`.
    new: Prevents the shape of a page category from living in a file nobody ratified (until case 304 the six `schema.yaml` and their `schema.md` stood outside the graph — no `purpose`, no History, no Estimate, changed by hand by an `update` with `file`).
  change: the history of the schemas stands in the bracket of its pointer
- slug: rule-permissions
  replace:
  - old: A Grep whose path was that folder itself asked all the same in session 1448, so a second rule names the folder itself beside the rule for what lies inside it (case 693).
    new: A second rule names the folder itself beside the rule for what lies inside it, since a Grep whose path was that folder itself asked all the same (in session 1448, case 693).
  change: the session stands in the bracket of its pointer
- slug: rule-prespec-hook
  replace:
  - old: the hook runs the same judgment at the exit (case 561.3). Named `pretask` until case 261.
    new: the hook runs the same judgment at the exit (case 561.3; named `pretask` until case 261).
  change: the old name stands in the bracket of its pointer
- slug: rule-raw-archive
  replace:
  - old: the session of the run still left out (`rule-sprint-close`, case 743.1).
    new: the session of the run still left out, as `rule-sprint-close` sets it (case 743.1).
  - old: still gitignored (`rule-sprint-close`, case 743.3).
    new: still gitignored, as `rule-sprint-close` sets it (case 743.3).
  change: the slug of rule-sprint-close stands outside the brackets of its pointers
- slug: rule-render-harness
  replace:
  - old: the renderer runs with lint and as the librarian's step after `cleanup` (case 89.1); the tick of case 226.2 belongs to that step.
    new: the renderer runs with lint and as the librarian's step after `cleanup` (case 89.1), and its tick of the render lines of the Spec belongs to that step (case 226.2).
  change: the pointer stands in a bracket of its own
- slug: rule-retro
  replace:
  - old: '`raw/<date>/<hi HHMM>/spec.md` (the session''s folder, case 73),'
    new: '`raw/<date>/<hi HHMM>/spec.md` in the session''s folder (case 73),'
  - old: a `guppi sprint-close` line (`rule-sprint-close`, case 628.1),
    new: a `guppi sprint-close` line, as `rule-sprint-close` names it (case 628.1),
  change: the session's folder and the slug of rule-sprint-close stand outside the brackets of their pointers
- slug: rule-retro-commit
  replace:
  - old: has no ledger line (`rule-ledger-write`, case 122).
    new: has no ledger line, as `rule-ledger-write` sets it (case 122).
  change: the slug of rule-ledger-write stands outside the bracket of its pointer
- slug: rule-retro-onward
  replace:
  - old: and in session 1834 the run stopped there (case 596).
    new: and the run once stopped there (in session 1834, case 596).
  - old: which Claude Code keeps set from that refusal until the person's next message, as the transcript of session 1237 shows;
    new: which Claude Code keeps set from that refusal until the person's next message (as the transcript of session 1237 shows);
  change: each session stands in a bracket
- slug: rule-rules-schema
  replace:
  - old: so the guard reads the field alike (`rule-sprint`, case 209.7).
    new: so the guard reads the field alike, as `rule-sprint` sets it (case 209.7).
  - old: seen by Obsidian since case 148.1 (case 166.1)
    new: seen by Obsidian (since case 148.1; case 166.1)
  - old: '`case-schema.md` is listed here since case 273; the glossary arrives through'
    new: '`case-schema.md` is listed here (since case 273); the glossary arrives through'
  change: each pointer stands in a bracket of its own, the slug of rule-sprint outside it
- slug: rule-search-leaves-out-decisions
  replace:
  - old: in the reading of session 1343 nine Greps over the wiki carried no exclusion, and one put it first, where it leaves nothing out.
    new: nine Greps over the wiki carried no exclusion, and one put it first, where it leaves nothing out (in the reading of session 1343).
  change: the session stands in a bracket
- slug: rule-skill-grill-me
  replace:
  - old: It served the person's own interviews without a page until case 443.1.
    new: It served the person's own interviews without a page (until case 443.1).
  - old: The question template is an indented code block, the form it took when case 443.1 was written, before case 444 let a fenced value carry a shorter fence.
    new: The question template is an indented code block (the form it took when case 443.1 was written, before case 444 let a fenced value carry a shorter fence).
  change: each pointer stands in a bracket of its own
- slug: rule-skill-hi
  replace:
  - old: is left by the `UserPromptSubmit` hook `guppi event prompt` (`rule-event-log`, case 111.1), which sees the session id;
    new: is left by the `UserPromptSubmit` hook `guppi event prompt` of `rule-event-log`, which sees the session id (case 111.1);
  - old: closed `[x] … · case N` by the opening Case (`rule-sprint-close`, cases 628.7, 769.2);
    new: closed `[x] … · case N` by the opening Case, as `rule-sprint-close` sets it (cases 628.7, 769.2);
  - old: a working file of the session (`rule-permissions`, case 363).
    new: a working file of the session, which `rule-permissions` allows (case 363).
  - old: 'is taken whole and run by `/box` (`rule-spec-box`, case 591):'
    new: 'is taken whole and run by `/box`, as `rule-spec-box` sets it (case 591):'
  - old: 'The skill writes no event line of its own since case 111.4: a `!` substitution never saw `CLAUDE_SESSION_ID` (every `hi` of sessions A–M carried `--------`), so the `hi` line is the `UserPromptSubmit` hook''s, which reads the session id from its payload (`rule-event-log`, case 111.1).'
    new: 'The skill writes no event line of its own (since case 111.4): a `!` substitution never saw `CLAUDE_SESSION_ID` (every `hi` of sessions A–M carried `--------`), so the `hi` line is written by the `UserPromptSubmit` hook of `rule-event-log`, which reads the session id from its payload (case 111.1).'
  change: each pointer stands in a bracket of its own, the slugs of shipped rules outside it
- slug: rule-skill-sprint-close
  replace:
  - old: Until case 743 these steps stood in a paragraph of `orchestration.md`, which every session loads.
    new: These steps stand apart from `orchestration.md`, which every session loads (until case 743 they stood in a paragraph of it).
  - old: which `.claude/agents/librarian-guppi.md` runs ([[rule-sprint-close]], case 628.1).
    new: which `.claude/agents/librarian-guppi.md` runs as [[rule-sprint-close]] sets it (case 628.1).
  change: each pointer stands in a bracket of its own, the link to rule-sprint-close outside it
- slug: rule-skill-sprint-open
  replace:
  - old: Until case 743 nothing set what the opening Case asks, and the steps of the turn of a sprint stood in `orchestration.md`, which every session loads.
    new: The skill sets what the opening Case asks, apart from `orchestration.md`, which every session loads (until case 743 nothing set it, and the steps of the turn of a sprint stood in `orchestration.md`).
  - old: marks the last sprint closed ([[rule-sprint]], case 743.5), and the person may type it too.
    new: marks the last sprint closed, as [[rule-sprint]] sets it (case 743.5), and the person may type it too.
  change: each pointer stands in a bracket of its own, the link to rule-sprint outside it
- slug: rule-spec-capture
  replace:
  - old: the person took that Spec at the Frontier (`rule-spec-box`, case 591).
    new: the person took that Spec at the Frontier, as `rule-spec-box` sets it (case 591).
  change: the slug of rule-spec-box stands outside the bracket of its pointer
- slug: rule-spec-reconcile
  replace:
  - old: 'Since case 441 the hooks alone write the Cases into the plan:'
    new: 'The hooks alone write the Cases into the plan (since case 441):'
  - old: the comparison with a ratified copy that stood here from case 387.3 is gone (case 445.1).
    new: the comparison with a ratified copy that stood here is gone (from case 387.3 to case 445.1).
  - old: 'A payload the hook cannot read: exit 0 with one line on stderr; it never raises. Until case 445.1 the rule was a comparison: `guppi ratified --edit` on `PostToolUse` compared an edited plan with a ratified copy `<plan>.ratified.md` and marked a changed Case in `<plan>.waiting.json` for its showing; the copy, the marks and that hook are gone.'
    new: 'A payload the hook cannot read: exit 0 with one line on stderr; it never raises (until case 445.1 the rule was a comparison: `guppi ratified --edit` on `PostToolUse` compared an edited plan with a ratified copy `<plan>.ratified.md` and marked a changed Case in `<plan>.waiting.json` for its showing; the copy, the marks and that hook are gone).'
  change: the history of the guard stands in the brackets of its pointers
- slug: rule-spec-write
  replace:
  - old: Until case 387 the agent wrote each Case into the plan file itself, translated from the chat, and nobody compared the two. Now `case-guppi` writes the whole Case in English, and a hook copies its stored answer (cases 437, 441).
    new: '`case-guppi` writes the whole Case in English, and a hook copies its stored answer (cases 437, 441; until case 387 the agent wrote each Case into the plan file itself, translated from the chat, and nobody compared the two).'
  change: the history of the hook stands in the bracket of its pointers
- slug: rule-sprint
  replace:
  - old: its status kept in the record of the close (`rule-sprint-close`, case 632.3)
    new: its status kept in the record of the close, as `rule-sprint-close` sets it (case 632.3)
  change: the slug of rule-sprint-close stands outside the bracket of its pointer
- slug: rule-synthesis
  replace:
  - old: its `error` lessons that joined no Insight (`rule-sprint-close`, case 627.5).
    new: its `error` lessons that joined no Insight, as `rule-sprint-close` sets it (case 627.5).
  change: the slug of rule-sprint-close stands outside the bracket of its pointer
- slug: rule-work-mode
  replace:
  - old: the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4).
    new: the librarian runs it, and the command ticks it, as `rule-sprint-close` sets it (case 628.4).
  change: the slug of rule-sprint-close stands outside the bracket of its pointer
```

```tasks
- [x] create `estimate-clean-branch-pages-hold-pointers-only-in-brackets`
- [x] update `entity-glossary`
- [x] update `entity-sprint`
- [x] update `entity-sprint-plugin`
- [x] update `rule-agent-writing`
- [x] update `rule-backlog`
- [x] update `rule-brief`
- [x] update `rule-carry-over`
- [x] update `rule-case-build`
- [x] update `rule-case-check`
- [x] update `rule-case-example`
- [x] update `rule-case-protocol`
- [x] update `rule-claude-md`
- [x] update `rule-cleanup`
- [x] update `rule-decisions-schema`
- [x] update `rule-documentation`
- [x] update `rule-end-of-work`
- [x] update `rule-entities-schema`
- [x] update `rule-estimates-schema`
- [x] update `rule-event-log`
- [x] update `rule-git-context`
- [x] update `rule-insights-schema`
- [x] update `rule-internal-context`
- [x] update `rule-language`
- [x] update `rule-ledger-tail`
- [x] update `rule-ledger-write`
- [x] update `rule-lessons-schema`
- [x] update `rule-materialize`
- [x] update `rule-orchestration`
- [x] update `rule-page-generation`
- [x] update `rule-page-read`
- [x] update `rule-page-schemas`
- [x] update `rule-permissions`
- [x] update `rule-prespec-hook`
- [x] update `rule-raw-archive`
- [x] update `rule-render-harness`
- [x] update `rule-retro`
- [x] update `rule-retro-commit`
- [x] update `rule-retro-onward`
- [x] update `rule-rules-schema`
- [x] update `rule-search-leaves-out-decisions`
- [x] update `rule-skill-grill-me`
- [x] update `rule-skill-hi`
- [x] update `rule-skill-sprint-close`
- [x] update `rule-skill-sprint-open`
- [x] update `rule-spec-capture`
- [x] update `rule-spec-reconcile`
- [x] update `rule-spec-write`
- [x] update `rule-sprint`
- [x] update `rule-synthesis`
- [x] update `rule-work-mode`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] `uv run guppi render`: `vault/wiki/rules/schema.yaml`
- [x] `uv run guppi render`: `vault/wiki/entities/schema.yaml`
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] `uv run guppi render`: `vault/wiki/decisions/schema.yaml`
- [x] `uv run guppi render`: `vault/wiki/lessons/schema.yaml`
- [x] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [x] `uv run guppi glossary`
- [x] read `estimate-clean-branch-pages-hold-pointers-only-in-brackets`
```
