## Case 811 — guppi ship reports a list of bare case numbers at the opening of a comment or a docstring

> **context:**
> `guppi ship` builds the clean copy of GUPPI, and `bare_numbers` of `guppi/ship.py` makes it exit 1 on a case number with no word `case` before it in a comment or a docstring of a Python file (case 808.1). It catches a bracket of case numbers joined by a comma, a semicolon, `and` or a dash, by `BARE_BRACKET`; an opening of one case number and a colon, by `BARE_OPENING`; and a comment that is one case number alone, by `BARE_ALONE`. A comment or a docstring that opens with a list of case numbers and a colon, such as `387.4, 445.4, 476.3:`, is no finding: the handoff of session 0101 reports one that was reworded by hand all the same. The person chose that the opening and the comment alone take a list of case numbers with the same joining words as the bracket, and that the Criterion of `estimate-clean-branch-writes-a-clean-copy` is replaced whole. `rule-one-judgment-one-implementation` governs the pattern: one list of case numbers serves the bracket, the opening and the comment alone in `guppi/ship.py`. A Grep `bare|BARE_` over `guppi/` printed `guppi/ledger.py`, `guppi/generate.py`, `guppi/pages.py`, `guppi/prespec.py`, `guppi/render.py` and `guppi/ship.py`; only `guppi/ship.py` judges a bare case number in a comment or a docstring, since `BARE_CASE` of `guppi/prespec.py` judges a ledger line with no word `case` in its first bracket, and the other hits use the word for a slug, a ledger line, a wikilink, a task word or a splice, so the task adds no second copy. A Grep `(#|""")\s*\d+(\.\d+)*\s*(,|;|and\b|[-–])\s*\d` over `guppi/` printed nothing, so no comment or docstring there opens with a list of case numbers today, and `uv run guppi ship --check` and `make lint`, which printed 0 lines and exited 0 at the close of the last session by `## Readings at the close` of `brief.md`, stay clean after the change; the Criterion of `estimate-clean-branch-code-holds-pointers-only-in-brackets` promises no bare case number under `guppi/`, so it stands, and a task runs `uv run guppi ship --check` once the code changes. In `rule-clean-branch` the one sentence of its Purpose that lists the shapes of a bare case number names one case number only, so a pair changes it. A Grep `guppi ship.*(number|comment|docstring)|(number|comment|docstring).*guppi ship` over `vault/wiki/rules/` printed `rule-clean-branch.md` and `rule-case-protocol.md`; the hit in `rule-case-protocol` sets the bracket of a pointer in the new text of a page with `core: true`, not a bare case number, so it stands. The new Criterion keeps each line of the old one but two, which it rewords on purpose: the line of the opening and the comment alone, which now takes a list of case numbers, and the line of what is no finding, which now names a list of numbers with words and no colon. The `purpose` of the Estimate says that it exits 1 on a bare case number in a comment or a docstring, which stays true, and its `method` stays a test run. A Grep `ship|clean-branch|clean_branch` over `tests/` outside `tests/test_ship.py` printed `tests/test_lint.py`, `tests/test_schemas.py` and `tests/test_prespec.py`; none reads the live `rule-clean-branch` or the Estimate, and the test of `tests/test_lint.py` runs `make lint` with a fake `uv`.

> **problem:**
> A comment or a docstring of the code that opens with a list of case numbers and a colon, or that is such a list alone, reaches the clean copy with no finding, though one case number in the same place is a finding.

> **recommend:**
> - **Should an opening with a list of case numbers and a colon be caught?**
>   - Recommended: (a) yes, with the same joining words as the bracket — a comma, a semicolon, `and` or a dash — read by one shared pattern.
>   - Answer: agreed, (a).
> - **Should a comment that is only a list of case numbers be caught too?**
>   - Recommended: (a) yes, with the same joining words.
>   - Answer: agreed, (a).
> - **How is the change checked?**
>   - Recommended: (a) replace the Criterion of `estimate-clean-branch-writes-a-clean-copy` whole, read in this session by `uv run pytest tests/test_ship.py` with a new test of the list shapes.
>   - Answer: agreed, (a).

> **given:**
> `guppi/ship.py`: the clean copy and its check, whose judgment of a bare case number gains the list.
> **＋** `tests/test_ship.py`: the tests of the judgment.
> **＋** `rule-clean-branch`: the rule of the clean copy, which lists the shapes of a bare case number.
> **＋** `estimate-clean-branch-writes-a-clean-copy`: its Criterion is replaced whole.
> **＋** `rule-one-judgment-one-implementation`: one pattern of a list of case numbers for every shape.

> **when:**
> `uv run guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or `uv run guppi ship --review <folder>` does the same.
> **＋** Or `uv run guppi ship --check` judges the working tree and writes no folder.

> **then:**
> In a comment or a docstring of a Python file it writes, it exits 1, and prints the file and the line, for each bracket that holds only case numbers, joined by a comma, a semicolon, `and` or a dash, such as `(274.1)` or `(513, 544.7)`.
> **＋** It does the same for each comment or docstring that opens with one or more case numbers joined the same way, followed by a colon, such as `# 169.1:`, `"""75.2:` or `# 387.4, 445.4:`, and for each comment whose whole text is one or more case numbers joined the same way, such as `# 786` or `# 387.4, 445.4`.
> **－** It removes no bare case number: the copy holds it as written.
> **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number or a list of numbers that opens a comment with words and no colon after it, such as `# 3, 4 tries`, is no finding.

> **tasks:**
> - [ ] `guppi/ship.py`: one pattern of a list of case numbers, joined by a comma, a semicolon, `and` or a dash, serves `BARE_BRACKET`, `BARE_OPENING` and `BARE_ALONE`; the opening and the comment alone take the list, and the module docstring and the comment above the patterns say so.
> - [ ] `tests/test_ship.py`: a comment and a docstring that open with a list of case numbers and a colon, and a comment that is a list of case numbers alone, each exit 1 and stay in the copy; a comment that opens with a list of numbers and words with no colon is no finding.
> - [ ] `uv run guppi ship --check`: prints no line after the change.
> - [ ] update `rule-clean-branch`
>   - old: `on each comment or docstring that opens with a case number followed by a colon, and on each comment whose whole text is a case number,`
>   - new: `on each comment or docstring that opens with one or more case numbers, joined as in such a bracket, followed by a colon, and on each comment whose whole text is one or more case numbers joined the same way,`
>   - change: `guppi ship reports a list of bare case numbers at the opening of a comment or a docstring, or alone in a comment`
> - [ ] update `estimate-clean-branch-writes-a-clean-copy`
>   - set:
>     ```
>     status: pending
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
>     **＋** It does the same for each comment or docstring that opens with one or more case numbers joined the same way, followed by a colon, such as `# 169.1:`, `"""75.2:` or `# 387.4, 445.4:`, and for each comment whose whole text is one or more case numbers joined the same way, such as `# 786` or `# 387.4, 445.4`.
>     **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
>     **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
>     **＋** With `--check` it judges each file it would write outside `vault/` — `guppi/`, `.claude/` and the files at the root of the project — but `uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
>     **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
>     **－** It writes no file that a page without `core: true` renders in full.
>     **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
>     **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, in `vault/wiki/case-example.md` or the Render of `rule-case-example`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed.
>     **－** It removes no bare case number: the copy holds it as written.
>     **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number or a list of numbers that opens a comment with words and no colon after it, such as `# 3, 4 tries`, is no finding.
>     ```
>   - change: `the Criterion replaced whole — guppi ship reports a list of bare case numbers at the opening of a comment or a docstring, or alone in a comment`
> - [ ] read `estimate-clean-branch-writes-a-clean-copy`

> **ratification:**
> ```
> - decision[case 811][update][rule-clean-branch]{ref:rule-clean-branch}
> - decision[case 811][update][estimate-clean-branch-writes-a-clean-copy]{ref:rule-clean-branch}
> ```
