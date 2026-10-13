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

> **tasks:**
> - [ ] `guppi/ship.py`: one judgment of a bare case number, built on `ID` of `guppi/caseid.py`, reads the comments and docstrings of a Python file by the standard `tokenize` module and gives the line and what it found; `leftovers` adds its lines for a `.py` file, and the module docstring names it.
> - [ ] `tests/test_ship.py`: a bracket of case numbers, a comment and a docstring that open with a case number and a colon, and a comment that is a case number alone each exit 1 and stay in the copy; `match.group(1)` in code and a comment that opens with a count are no finding.
> - [ ] update `rule-clean-branch`
>   - old: `a bracket that holds no pointer stays.`
>   - new: `` a bracket that holds no pointer stays. A case number with no word `case` or `cases` before it, such as `(274.1)`, is no form of a pointer, and `guppi ship` does not remove it; in a comment or a docstring of a Python file it exits 1 on each bracket that holds only case numbers, on each comment or docstring that opens with a case number followed by a colon, and on each comment whose whole text is a case number, and it judges no code outside them. ``
>   - change: `a case number stands with its word; guppi ship reports a bare one in a comment or a docstring of the code`
> - [ ] update `estimate-clean-branch-writes-a-clean-copy`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether guppi ship writes only the code, the harness and the pages with core: true, removes whole each bracket that holds a pointer, writes a link to a page it leaves out as its slug, writes the shipped values, exits 1 on a pointer outside such a bracket and on a bare case number in a comment or a docstring of a Python file, lists the brackets with words under --review, and judges in place under --check each file outside vault/ that it writes"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
>     **＋** Or `uv run guppi ship --review <folder>` does the same.
>     **＋** Or `uv run guppi ship --check` judges the working tree and writes no folder.
>
>     Then:
>     It writes `guppi/`, `.claude/`, `CLAUDE.md`, `Makefile`, `pyproject.toml`, `uv.lock`, `.gitattributes`, the `schema.yaml` of each category, `vault/wiki/tags.md`, each page under `vault/wiki/` with `core: true`, and each file rendered from such a page.
>     **＋** In each file it writes, it removes whole each bracket that holds a pointer — a reference to a case, an id `decision-case-N` or a mention of a session by its id — with every word in it and the space before it, and each `[[decision-case-N]]` link; a bracket that holds no pointer stays as it is.
>     **＋** It writes each other `[[…]]` link of a Markdown file to a page or a file it does not write as the slug in a code span.
>     **＋** Each page it writes carries `origin: guppi`, `sprint: guppi`, the date of the run in `created` and a `## History` of one line that says the page shipped with GUPPI, and its link fields keep only the pages it writes.
>     **＋** It exits 1, and prints the file and the line, for each pointer that stands outside such a bracket, each id of a list of sessions included.
>     **＋** In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
>     **＋** It does the same for each comment or docstring that opens with a case number followed by a colon, such as `# 169.1:` or `"""75.2:`, and for each comment whose whole text is a case number, such as `# 786`.
>     **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
>     **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
>     **＋** With `--check` it judges each file it would write outside `vault/` — `guppi/`, `.claude/` and the files at the root of the project — but `uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
>     **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
>     **－** It writes no file that a page without `core: true` renders in full.
>     **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
>     **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, in `vault/wiki/case-example.md` or the Render of `rule-case-example`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed.
>     **－** It removes no bare case number: the copy holds it as written.
>     **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number that opens a comment with no colon after it is no finding.
>     ```
>   - change: `the Criterion replaced whole — guppi ship reports a bare case number in a comment or a docstring of a Python file`
> - [ ] read `estimate-clean-branch-writes-a-clean-copy`

> **ratification:**
> ```
> - decision[case 808.1][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 808.1][update][estimate-clean-branch-writes-a-clean-copy]{ref:rule-clean-branch}
> ```

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

> **tasks:**
> - [ ] `guppi/`: each comment and docstring that gives a case number with no word `case` or `cases` before it — in a bracket, such as `(274.1)`, at its opening, such as `# 169.1:` or `"""75.2:`, or alone, such as `# 786` — is rewritten by hand as a pointer in a bracket of its own at the end of its sentence, such as `(case 274.1)`; no code changes.
> - [ ] update `estimate-clean-branch-code-holds-pointers-only-in-brackets`
>   - set:
>     ```
>     status: pending
>     purpose: "Whether the code and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, and no case number without the word case before it, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs"
>     ```
>   - change: `the Criterion replaced whole — the code writes each case number with its word`
> - [ ] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`

> **ratification:**
> ```
> - decision[case 808.2][update][estimate-clean-branch-code-holds-pointers-only-in-brackets]{ref:rule-clean-branch}
> ```
