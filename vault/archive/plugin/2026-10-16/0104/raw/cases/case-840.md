## Case 840 — The example of a path pair names no path of GUPPI

> **context:**
> When a Case renames a word or a path everywhere, `guppi generate` runs a `reword` over every live rule, entity and Estimate. Case 819.1 moved the tests of GUPPI from `tests/` to `.guppi/tests/` this way. `.guppi/tests/test_guppi_package.py`, the test of `estimate-guppi-package-runs-from-its-own-folder`, fails when a live page still names a bare `tests/` in a part that a `reword` changes, and it finds it by `reword_pattern` and `Vault.reword_text` of `.guppi/guppi/generate.py`. Case 819.2 wrote `tests/` as the example of a path pair into the Purpose of `rule-page-generation` and into the Criterion of `estimate-generate-rewords`, after the `reword` in ledger order. So the test is red, and the Estimate was read `failed` at line 5 of the ledger of session 1959 and put off by case 837. The brief of the librarian of session 1959 (`vault/wiki/brief.md`, `## Readings at the close`) reports the last run: `uv run --project .guppi guppi test`: 1 failed, 1714 passed, 6 skipped, 1 deselected (exit 1); the failure is `test_guppi_package.py::test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]`. The Result of the Estimate names the same two pages as the only hits. The person chose a neutral example, `docs/` → `site/docs/`. That pair names no path of GUPPI, so the test cannot match it, and it keeps the same matching: `docs/intro.md` changes, and `site/docs/` and `cart/docs/` stay as they are.
>
> The rule that governs the change is the one `case-schema.md` sets: a part inside a Criterion is refused, and a promise changes only by a Criterion replaced whole (case 378.4). So Case 840.1 replaces the Criterion of `estimate-generate-rewords` whole. The behaviour stays the same and only the example changes, and the Estimate goes back to `pending`. The check of the Case file sends one note for each line of the old Criterion that the new one does not carry; the line with the `tests/` example is such a line, and it changes on purpose. Its `method` loses the part by hand: that part waits for the librarian's run that applied the `reword` of `rule-guppi-package`, which ran in session 1959, and its outcome stands in the Result. `.guppi/tests/test_generate.py` checks the matching of a path pair with `tests/` (`test_reword_pattern_reads_a_path_pair_from_the_start_of_a_path` among others). The new example is the same matching on another folder, so no new test is added. No code changes. The docstrings of `.guppi/guppi/generate.py` keep `tests/` as their example, since the test reads only the live pages. Of the other Estimates of `rule-page-generation`, none speaks of the example, and they stand. The defer of case 793 on `rule-page-generation` is about a form of `update` that removes a section; this Case does not settle it, and it stands.
>
> The pages change at the librarian's run of this session, not before. A reading of `test_guppi_package.py` at this session's Retro would still be red. So Case 840.2 sets `estimate-guppi-package-runs-from-its-own-folder` `pending` with its Criterion unchanged, takes up the defer of case 837, and gives it a `method` that waits for that librarian's run. This settles Frontier item C3 as well. No `create` stands in the Case, so no query of the vault for a free slug was run.

> **problem:**
> Two live pages use the path `tests/` as the example of a path pair of `reword`, and the Criterion of `estimate-guppi-package-runs-from-its-own-folder` forbids such a path on a live page. Its test stays red, and the Estimate stays `failed` and put off.

> **recommend:**
> - **How do we settle the clash between the example and the test?**
>   - Recommended: (a) change the example to a neutral folder, such as `docs/` → `site/docs/`, in both pages; the Criterion of `estimate-generate-rewords` replaced whole and set `pending`.
>   - Answer: agreed, (a).
> - **Does this Case also re-read the failed Estimate (item C3)?**
>   - Recommended: (a) yes, as a second part of this Case: the Estimate set `pending` with its Criterion unchanged, the defer taken up, and a `method` that waits for the librarian's run of the session that changes the example.
>   - Answer: agreed, (a).
> - **What does the reading of `estimate-generate-rewords` run once its Criterion is replaced?**
>   - Recommended: (a) keep only the test, `pytest .guppi/tests/test_generate.py`, read at this session's Retro.
>   - Answer: agreed, (a).

### Case 840.1 — The example of a path pair is a neutral folder

> **given:**
> `estimate-generate-rewords`: its Criterion is replaced whole, and its `method` is set anew.
> **＋** `rule-page-generation`: the rule of `guppi generate`, whose Purpose names the example of a path pair.
> **＋** `.guppi/guppi/generate.py`: `guppi generate` and the matching of a `reword` pair.
> **＋** `.guppi/guppi/prespec.py`: the preview of `uv run --project .guppi guppi prespec --check`.
> **＋** `.guppi/tests/test_generate.py`: the test of the reading.
> **＋** `.guppi/tests/test_guppi_package.py`: the test that finds a path of GUPPI outside `.guppi/` on a live page.
> **＋** `vault/wiki/`: the live pages that a `reword` changes, beside `vault/archive/` and `vault/raw/`, which it never touches.
> **＋** `docs/`: the example folder of a path pair, with `site/docs/`, `docs/intro.md`, `site/docs/intro.md` and `cart/docs/`, paths of no real project.

> **when:**
> `guppi generate` applies an `update` entry whose item carries `reword`, a list of `{old, new}` pairs.

> **then:**
> A pair whose `old` does not end with `/` is replaced as a whole word, with no letter, digit, `_` or `-` right before or after it.
> **＋** A pair whose `old` ends with `/`, such as `docs/`, is replaced as the start of a path: where no letter, digit, `_`, `-`, `.` or `/` stands right before it, whatever follows it, so the pair `docs/` → `site/docs/` turns `docs/intro.md` into `site/docs/intro.md` and leaves `site/docs/` and `cart/docs/` as they are.
> **＋** The replace runs on every live page of the folders `rules`, `entities` and `estimates` of `vault/wiki/`, in every section but History and Result and in the fields `purpose` and `method`, and a pair whose `old` ends with `/` runs in the fields `implementation_ref`, `governs` and `code_ref` too.
> **＋** Each page touched gets one History line `reworded: old → new · [[decision-case-N]]`, and stdout has one line per page with the count.
> **＋** The other keys of the item — `set`, `replace`, `sections`, `change` — apply to the page itself as before; an item that carries `reword` alone is content and applies.
> **＋** `uv run --project .guppi guppi prespec --check` previews each pair by the same matching as `guppi generate`.
> **－** A pair with no hit on any live page fails the entry with the reason, and so does a pair whose `new` is absent from the text of the page of the item: its `purpose`, `governs`, `implementation_ref`, Purpose and Render, compared without regard to case. Nothing is applied.
> **－** The Decision pages, the lessons and the Insights, `vault/archive/`, `vault/raw/`, `log.md`, `brief.md` and `sprint.md` are not touched; the status of no Estimate changes.

> **tasks:**
> - [ ] update `rule-page-generation`
>   - old: `` A pair whose `old` ends with `/`, such as `tests/`, is the start of a path ``
>   - new: `` A pair whose `old` ends with `/`, such as `docs/`, is the start of a path ``
>   - change: `the example of a path pair is docs/, a folder that names no path of GUPPI`
> - [ ] update `estimate-generate-rewords`
>   - set:
>     ```
>     status: pending
>     method: uv run --project .guppi pytest .guppi/tests/test_generate.py on a temp vault whose pages hold paths in their text and their link fields
>     ```
>   - change: `the Criterion replaced whole — the example of a path pair is docs/ → site/docs/; the method keeps the test alone`
> - [ ] read `estimate-generate-rewords`

> **ratification:**
> ```
> - decision[case 840.1][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 840.1][update][estimate-generate-rewords]{ref:rule-page-generation}
> ```

### Case 840.2 — The package Estimate is read again after the new example lands

> **given:**
> `estimate-guppi-package-runs-from-its-own-folder`: set `pending`, its Criterion kept, its `method` set anew.
> **＋** `rule-guppi-package`: the rule that the Estimate checks.
> **＋** `decision-case-837`: the decision that put the Estimate off.
> **＋** `.guppi/tests/test_guppi_package.py`: the test of the reading.
> **＋** `.claude/settings.json`: the hooks of a session of the repository of GUPPI.
> **＋** `vault/wiki/`: the live pages that the test reads.

> **when:**
> In the repository of GUPPI, after the move of the code and the render of the harness, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.

> **then:**
> No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
> **－** The Decision pages, the lessons and the Insights keep the old command and the old paths, since they are records.

> **tasks:**
> - [ ] update `estimate-guppi-package-runs-from-its-own-folder`
>   - set:
>     ```
>     status: pending
>     method: "by hand, after the librarian's run of the session that changes the example of a path pair in rule-page-generation: uv run --project .guppi pytest .guppi/tests/test_guppi_package.py, then a session opened in this repository, /hi typed there, and the output of its hooks read against the Criterion"
>     ```
>   - sections.Criterion:
>     ```
>     When:
>     In the repository of GUPPI, after the move of the code and the render of the harness, a session of Claude Code opens and its hooks, skills and agents run the code of GUPPI, and `uv run --project .guppi pytest` runs the tests of `.guppi/tests/`.
>     **＋** `uv run --project .guppi guppi ship <folder>` builds the clean version, as `rule-clean-branch` sets it.
>
>     Then:
>     The package `guppi`, its `pyproject.toml`, its lock file `uv.lock`, its tests and a `.gitignore` that holds `.venv/` stand under `.guppi/`, and `.guppi/pyproject.toml` declares pytest and ruff for the tests.
>     **＋** Each hook of `.claude/settings.json`, and each command of a skill, an agent, the `Makefile` and `.github/workflows/prod.yml` that runs the code of GUPPI or its tests, runs it through `uv run --project .guppi`, and no hook prints an error.
>     **＋** No live rule, entity or Estimate names a command that runs the code of GUPPI or its tests through `uv run` without `--project .guppi` outside History and Result, and none names a path of that code or those tests outside `.guppi/`.
>     **＋** `.guppi/tests/test_guppi_package.py` fails on such a command in a file of `.claude/`, the `Makefile`, `.github/workflows/` or a live rule, entity or Estimate, and on such a path in such a page, found by the matching of `reword` of `guppi generate`.
>     **＋** Each module that finds its own refusals in the transcript by the command of its hook finds them under the command with `--project .guppi` and under the command without it.
>     **＋** The Bash and PowerShell guards judge `uv run --project .guppi python` as they judge `uv run python`, and `guppi lint` takes a test path under `.guppi/tests/` in a `method` as it takes one in the folder of tests of the project's own code.
>     **＋** The clean version holds no `pyproject.toml` and no `uv.lock` at its root.
>     **－** The repository of GUPPI keeps at its root, until a Case of a later session removes them, the `pyproject.toml` and `uv.lock` of a development project that takes the package from `.guppi/`, so a command without `--project .guppi` still runs at its root and no hook of a running session fails.
>     **－** The Decision pages, the lessons and the Insights keep the old command and the old paths, since they are records.
>     **－** The examples of a project of the person's own in `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` keep a path of tests of that project, with no `.guppi/`.
>     ```
>   - change: `read again after the example of a path pair changes in rule-page-generation and estimate-generate-rewords; the Criterion stands, the method waits for the librarian's run that writes the new example`
> - [ ] read `estimate-guppi-package-runs-from-its-own-folder`

> **ratification:**
> ```
> - decision[case 840.2][update][estimate-guppi-package-runs-from-its-own-folder]{ref:rule-guppi-package}{supersedes:case 837}
> ```
