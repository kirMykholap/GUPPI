## Case 868 — A test over a live file passes on the old text and the new

> **context:**
> A Case can change code that reads a text and, in the same session, the text itself: a page, or a file rendered from a page. The code runs from the working tree as soon as Work Mode edits it. The page changes at the librarian's run, and the rendered file at the render after it. So the new code reads the old text in between. `insight-workflow-code-live-before-the-page-it-reads` collects the lessons of this pattern. Most of its forms are now covered. `rule-retro` and `rule-work-mode` turn the red of a check such as `uv run --project .guppi guppi check`, listed under `## Expected red` of `work.md`, into a note for the handoff (cases 473.1, 479.3). `rule-case-build` makes a reader that would lose what it refuses keep the old form (case 473.2), and makes `case-guppi` judge each task by the state of the code and the pages when it runs (case 797.1). That covers the lessons of the reading moment, of the preview and of the key another Case adds. One form stays open: `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian`. In session 1739 Case 819.1 changed `.guppi/tests/test_guppi_package.py`, which reads the files of `.claude/` and the live pages. Its tests were red at Retro, waiting for the render, and the commit went in with them red. Two texts disagree on such a test. `rule-case-build` says that a reader that only goes red keeps no old form and that its red is a note for the handoff. `rule-retro` says that a red test is never an expected red and is fixed or reverted, and that the commit needs green. The workflow `.github/workflows/checks.yml` also runs `uv run --project .guppi guppi test`. The person chose to action the Insight: such a test passes on the old text and on the new one until the text lands, and a Case of a later session removes the old text.
>
> The rule that governs the choice is `rule-retro`, whose sentence on red tests stands: under this Case no task leaves a test red until the librarian's run. The option of an expected red test would have broken it. The last test run was read in the brief, under Readings at the close: `uv run --project .guppi guppi test`: 1722 passed, 6 skipped, 1 deselected (exit 0).
>
> In `rule-case-build`, read whole, three sentences state the behaviour. The sentence of case 754 puts each place where the new text would fail a test into the Case as a task that changes the test or the text. It stays true, and the new sentence sets how that task writes the test. The sentence of case 473.2 on a reader that loses what it refuses stays true. The sentence on a reader that only goes red would cover a test, and so it gains the sentence that excludes a test. The sentence of case 797.1 on the moment of a check stays true. The Criterion of `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` holds that `－` line, so this Case replaces the Criterion whole and sets its `purpose` and `method` anew, since both name only the reader. The Criterion of `estimate-case-build-reads-the-test-code-over-a-changed-text` promises the reading of the test code and that each failing place enters the Case as a task. How that task writes the test is the replaced Criterion, so that Criterion stands. The Criterion of `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check` (case 736.1) promises that each text of a live file that a changed check would refuse enters the Case. When the Case changes that text, a test that runs the new check over the live file is red on the old text until the text lands. So the new sentence and the replaced Criterion also cover a test that fails because the Case changes the code of a check it runs. That Criterion says nothing of how the test is written, so it stands (/pre-spec, ask-guppi). Two lines of the old Criterion are rewritten, not dropped, and the check notes them as not carried. The `When` line now also names a test and the live file it reads. The line on the removal of the old form now also names the old text in the test. The new `method` waits for the first Case built under the new Render, so the Retro of this session leaves the Estimate `pending`.
>
> A Grep for `only goes red|red test is never|note for the handoff` over `vault/wiki/`, `.claude/` and `.guppi/` printed these files:
> `.claude/skills/work/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/agents/case-guppi.md`, `vault/wiki/log.md`, `vault/wiki/lessons/lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian.md`, `vault/wiki/rules/rule-case-build.md`, `vault/wiki/insights/insight-workflow-code-live-before-the-page-it-reads.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/rules/rule-handoff.md`, `vault/wiki/estimates/estimate-clean-branch-code-holds-pointers-only-in-brackets.md`, `vault/wiki/rules/rule-work-mode.md`, `vault/wiki/estimates/estimate-retro-red-check-of-an-updated-page-is-a-handoff-note.md`, `vault/wiki/estimates/estimate-case-build-keeps-the-old-form-until-the-writer-is-live.md` and `.guppi/tests/test_guppi_package.py`.
> The two skills, `rule-retro`, `rule-work-mode` and `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` speak of the red of a check, and `rule-retro`, its skill and that Estimate add that a red test is never an expected red. The new rule agrees with both, so they stand. `estimate-clean-branch-code-holds-pointers-only-in-brackets` speaks of the red of `uv run --project .guppi guppi check`, so it stands. The hit in `rule-handoff` is a History line, and `log.md` is a record. The lesson and the Insight are records that this Case closes. The docstring of `.guppi/tests/test_guppi_package.py` says that the red of its tests before the render is a note for the handoff, which the new rule makes false, so a task rewords it.
>
> Tests that read live files. A Grep for `(ROOT|REPO)\s*/\s*"(vault|\.claude)"` over `.guppi/tests/` printed `test_case_schema.py`, `test_guppi_package.py`, `test_generate.py`, `test_orchestration.py` and `test_schemas.py`. Only `test_guppi_package.py` reads a file this Case changes. It reads every file under `.claude/`, `.claude/agents/case-guppi.md` included, and the live rule and Estimate pages, and fails on `uv run guppi`, `uv run pytest`, or `guppi/` and `tests/` where a `reword` would change them. The new texts name only `.guppi/tests/`, the form the live pages already hold while that test passes, so they stand.
>
> The Insight leaves the backlog by an `update` to `actioned` with `addressed_by: decision-case-868`, as its schema sets it (case 712). It has no `deferred_by`, so no `{supersedes:...}` mark is needed. Its `clustered` children go to the archive by the cascade of `generate`. Case 865 of this session changes hooks and the text they read. It is not exposed to this pattern: its hooks refuse only a new kind of `defer`, so nothing they accept today is lost, and its context says that `test_orchestration.py` still passes on the rendered `orchestration.md`. It does not change `rule-case-build`. When this Case was built, no case file of Cases 869 to 872 of the same batch stood.

> **problem:**
> A Case may change a test that reads a live file which the same session changes. The test is red from Work Mode until the librarian's run, while `rule-retro` lets no red test stand. `rule-case-build` still calls that red a note for the handoff.

> **recommend:**
> - **What should happen to this Insight?**
>   - Recommended: (a) action it: a test that reads a live file which the same session changes accepts both the old and the new text until the text lands, and a Case of a later session removes the old form.
>   - Answer: agreed, (a).

> **given:**
> `rule-case-build`: the rule of `case-guppi`, rendered into `.claude/agents/case-guppi.md`.
> **＋** `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`: its Criterion, `purpose` and `method` are replaced.
> **＋** `.guppi/tests/`: the tests, some of which read a live file of `vault/` or `.claude/`.
> **＋** `.guppi/tests/test_guppi_package.py`: a test over live files, whose docstring names its red before the render.
> **＋** `rule-retro`: the rule that lets no red test stand and makes the red of a check a note for the handoff.
> **＋** `estimate-case-build-reads-the-test-code-over-a-changed-text`: the Estimate of the reading of a test over a changed text, which stands.
> **＋** `estimate-case-build-reads-the-texts-a-test-runs-through-a-changed-check`: the Estimate of the reading of a live file that a test runs through a changed check, which stands.
> **＋** `insight-workflow-code-live-before-the-page-it-reads`: the Insight this Case actions.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes a reader in code and the text or the writer that reader reads, or a test of `.guppi/tests/` or the code of a check that test runs, and a live file of `vault/` or `.claude/` that the test reads, where the code and the test run from the working tree at once and the text lands at the librarian's run or the render.

> **then:**
> Where the reader refuses in between and what it refuses is lost, such as a hook that refuses a ledger line, the `then` of the Case says that the reader accepts the old form beside the new one until a reading of the writer passes live.
> **＋** Where the test would fail on the text of the file before the change or after it, whether the Case changes the test, the code of a check the test runs or the file, a task of the Case makes the test pass on the text before the change and on the text after it, until the text lands.
> **＋** The removal of the old form from the reader, after that reading, and of the old text from the test, after the text lands, is left to a Case of a later session.
> **－** A reader that only goes red, such as `uv run --project .guppi guppi check`, keeps no old form: its red is a note for the handoff by `rule-retro`.
> **－** A test of `.guppi/tests/` is no such reader: by `rule-retro` a red test is never an expected red, so no task leaves the test red until the librarian's run.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` A reader that only goes red, such as `uv run --project .guppi guppi check`, keeps no old form: its red is a note for the handoff by `rule-retro`. ``
>   - new: `` A reader that only goes red, such as `uv run --project .guppi guppi check`, keeps no old form: its red is a note for the handoff by `rule-retro`. A test of `.guppi/tests/` that reads a live file of `vault/` or `.claude/` is no such reader, since `rule-retro` lets no red test stand: where the Case changes that test, the code of a check that test runs, or the file by a page `update` or by the render of its rule, and the test would fail on the text of the file before the change or after it, a task of the Case makes the test pass on the text before the change and on the text after it until the text lands, and a Case of a later session removes the old text from the test (as set in case 868). ``
>   - change: `a test over a live file that the same session changes passes on the old text and the new until the text lands; its red is no note for the handoff (case 868)`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] update `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
>   - set:
>     ```
>     status: pending
>     purpose: Whether a Case that changes a reader and the text it reads, where the reader loses what it refuses before the text lands, keeps the old form in its then until the writer is measured live, and whether a Case that changes a test over a live file, or the code of a check it runs, while the same session changes that file, makes the test pass on the old text and the new until the text lands
>     method: "by hand, after the first Case case-guppi builds under the Render of rule-case-build that names a test over a live file, which changes a reader in code and the text or the writer it reads, or a test of .guppi/tests/ or the code of a check it runs, and a live file the test reads: the then and tasks of that Case read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — a test over a live file that the same session changes passes on the old text and the new until the text lands`
> - [ ] read `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
> - [ ] `.guppi/tests/test_guppi_package.py`: the paragraph of the module docstring that says the tests over `.claude/` and the pages are red until the librarian's run and that this red is a note for the handoff now says that these tests were red then (case 819.1), and that a test like these now passes on the text before the change and on the text after it until the text lands, as `rule-case-build` sets it (case 868).
> - [ ] update `insight-workflow-code-live-before-the-page-it-reads`
>   - set:
>     ```
>     status: actioned
>     addressed_by: decision-case-868
>     ```
>   - change: `actioned: a test over a live file that the same session changes passes on the old text and the new until the text lands, in rule-case-build (case 868)`

> **ratification:**
> ```
> - decision[case 868][update][rule-case-build]{ref:rule-case-build}
> - decision[case 868][update][estimate-case-build-keeps-the-old-form-until-the-writer-is-live]{ref:rule-case-build}
> - decision[case 868][update][insight-workflow-code-live-before-the-page-it-reads]{ref:insight-workflow-code-live-before-the-page-it-reads}
> ```
