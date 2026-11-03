<!-- approved 15:22:40 · session 561dc30b -->

# Session 1337 — the acknowledging reply keeps its headings in Russian

## Case 1002 — The acknowledging reply names no heading in English

> **context:**
> After the person ratifies a Case, the main agent writes a reply that acknowledges it, in the form that `vault/wiki/orchestration.md` sets. That text names each part of the reply by its English words in a code span or in bold: the heading `## Case N — ratified`, the labels `Changes:` and `Notes:`, and the heading `## Frontier`. It then tells the agent to translate each one. In session 2227 the agent kept the labels and `## Frontier` in English. Case 997 rewrote the text so that it says first that each heading and label is translated. In session 0254 the agent translated the labels but still kept `## Frontier` in English. So `estimate-orchestration-acknowledging-reply` stands `failed`, and its Result says that the heading `## Frontier` stood in English. Both lessons, `lesson-acknowledging-reply-labels-left-in-english` and `lesson-orchestration-acknowledging-reply-leaves-the-frontier-heading-untranslated`, give the same cause, and `insight-orchestration-acknowledging-reply-keeps-headings-in-english` joins them: the agent copies an English name in a code span as a literal. The person chose to remove that literal. The text of `rule-orchestration` now names each heading and label of the reply by what it says, in the acknowledging reply and in each other reply that shows the Frontier, and gives no English word to copy. The bracket of the first sentence of `## The acknowledging reply` points to this Case, as `case-schema.md` sets it for the new text of a page with `core: true`.
>
> The promise does not change. The Criterion of `estimate-orchestration-acknowledging-reply` already says that each heading and label stands in the language of the chat, and that the English words in the Criterion only name the parts, so its Criterion stands. Its `method` waits for the render that wrote the text of Case 997, and that render has already happened. Its new `method` waits for the render of this text. The Estimate stays `failed` until a reading after that render, and that reading checks this Case. In the same way, the brief of the librarian of session 0254 reports `guppi check` under Flags: `status: a page with core: true that is draft` on `rule-orchestration` and `rule-skill-approve-spec`, and `unread: failed` on `estimate-orchestration-acknowledging-reply`. Those lines stay until that reading passes, in a later session. The insight stays `open`, since no reading has yet shown that the fix holds.
>
> The frame. A Grep of `Changes:|Notes:\*\*|— ratified|## Frontier` over `{vault/wiki,.claude,.guppi/guppi}/**` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/orchestration.md`, `vault/wiki/log.md`, the two lessons, the insight, `estimate-orchestration-acknowledging-reply`, `rule-orchestration`, `.guppi/guppi/generate.py`, `estimate-orchestration-acknowledges-the-opening-with-the-frontier`, `estimate-orchestration-shows-the-frontier-after-a-closed-line` and `estimate-orchestration-says-when-a-rendered-change-lands`. No file of `.claude/` is on that list, so no skill or agent names these headings. The hit in `generate.py` is a docstring of `later_cases` that says Cases were ratified after a reading, so no code reads these headings. The three other Estimates name `## Frontier` or `Changes:` in their Criterion as the reader's name for the part, and the Criterion of `estimate-orchestration-shows-the-frontier-after-a-closed-line` points to the form that `estimate-orchestration-acknowledging-reply` sets, so they stand. The brief, the backlog, the log, the lessons and the insight are records and are not changed. A Grep of `orchestration` over `.guppi/tests/` printed `test_casecheck.py`, `test_onward.py`, `test_orchestration.py` and `test_ratified.py`. Only `test_orchestration.py` reads `vault/wiki/orchestration.md` live, and its function `example` reads only the blocks tagged `showing` and `defer`, which this Case does not change. In `test_onward.py`, `## Frontier` stands only as filler text of a reply. The other replies of `orchestration.md` that are translated, such as the line `**Waiting:**`, are not acknowledging replies and stay out of this Case. The short form names the heading of the Frontier with no English literal, so it stands. The session's ledger holds no `error` lesson, so no line carries a mark.

> **problem:**
> The text tells the agent to translate each heading of the acknowledging reply, but it still names each one by an English literal. Twice the agent copied the English heading of the Frontier into a chat in another language.

> **recommend:**
> - **What fixes the English heading**
>   - Recommended: (b) rewrite `orchestration.md` so that it names the parts without English literals.
>   - Answer: agreed, (b).
> - **Which names the text drops**
>   - Recommended: (a) every heading and label of the reply, and the Frontier heading in each reply that shows the Frontier.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) keep `estimate-orchestration-acknowledging-reply` and its Criterion, and make its reading wait for the render of the new text.
>   - Answer: agreed, (a).

> **given:**
> `rule-orchestration`: the Rule page whose Render sets the acknowledging reply and the replies that show the Frontier.
> **＋** `vault/wiki/orchestration.md`: the file rendered from `rule-orchestration`, loaded by `/hi`.
> **＋** `estimate-orchestration-acknowledging-reply`: the check of the acknowledging reply, whose `method` changes.
> **＋** `CLAUDE.md`: the rule that sets the language of the chat.

> **when:**
> The main agent writes the reply that acknowledges a ratification, or another reply that shows the Frontier, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> Each heading and label of the reply stands in the language of the chat that `CLAUDE.md` sets.
> **＋** `vault/wiki/orchestration.md` names each heading and label of the reply by what it says, with no English word for it in a code span or in bold.
> **－** Slugs, paths, the `LEDGER` tag, the ledger lines and the word `STOP:` keep their own words.

```then
update:
- slug: rule-orchestration
  replace:
  - old: a heading `## Frontier`, its word translated into {{chat_lang}} as `## The acknowledging reply` sets it
    new: a level-two heading that names the Frontier in {{chat_lang}}, as `## The acknowledging reply` sets it
  - old: one heading `## Case N — ratified` naming their ids, one **Changes:** paragraph and one Frontier, each heading and label translated as `## The acknowledging reply` sets it
    new: one heading that says the Cases are ratified and names their ids, one paragraph of the changes and one Frontier, each heading and label written in {{chat_lang}} as `## The acknowledging reply` sets it
  - old: 'its headings and labels too: the words of its headings and labels in this paragraph, in code spans and in bold, are their names in {{documentation_lang}}, and the reply writes each one translated into {{chat_lang}} — the heading `## Case N — ratified`, the labels **Changes:** and **Notes:** and the heading `## Frontier` alike —, while slugs, paths, the `LEDGER` tag, the ledger lines and the word `STOP:` that opens a reply keep their own words, the rest of that line standing in {{chat_lang}} (as set in cases 167 and 997).'
    new: 'each of its headings and labels too: this paragraph names each heading and label by what it says, never by words in {{documentation_lang}} to copy, and the reply writes the words of each in {{chat_lang}}, while slugs, paths, the `LEDGER` tag, the ledger lines and the word `STOP:` that opens a reply keep their own words, the rest of that line standing in {{chat_lang}} (as set in cases 167, 997 and 1002).'
  - old: a heading `## Case N — ratified` and a paragraph **Changes:** — what changes
    new: a level-two heading that says in {{chat_lang}} that Case N is ratified, and a paragraph whose label says in {{chat_lang}} that it holds the changes — what changes
  - old: a paragraph **Notes:** — facts that did not enter the Case
    new: a paragraph whose label says in {{chat_lang}} that it holds notes — facts that did not enter the Case
  - old: a heading `## Frontier` and the lines of `frontier.md` as a checklist
    new: a level-two heading that names the Frontier in {{chat_lang}} and the lines of `frontier.md` as a checklist
  - old: its `## Frontier`, translated as the acknowledging reply sets it above, shows the new Frontier
    new: its heading for the Frontier, written in {{chat_lang}} as the acknowledging reply sets it above, shows the new Frontier
  change: the acknowledging reply and each reply that shows the Frontier name their headings and labels by what they say, with no English word to copy
- slug: estimate-orchestration-acknowledging-reply
  set:
    method: 'by hand, after the librarian''s render that writes into vault/wiki/orchestration.md the paragraph of rule-orchestration that names each heading and label of the acknowledging reply by what it says, with no English word for it in a code span or in bold: an acknowledging reply and a reply that acknowledges Cases ratified together in one answer, each written after that render, each read against the Criterion in the transcript of its session under ~/.claude/projects/'
  change: the reading waits for the render of the text that names each heading and label by what it says
```

```tasks
- [x] update `rule-orchestration`
- [x] update `estimate-orchestration-acknowledging-reply`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/orchestration.md`
```

## Case 1003 — /work and /retro load while a check is red

> **context:**
> When Claude Code loads a skill, it first runs each `!` command of the skill text and pastes the output into the skill. When such a command exits non-zero, Claude Code refuses to load the whole skill. `/work` runs `uv run --project .guppi guppi test` and `uv run --project .guppi guppi check` this way to write its baseline, and `guppi check` exits 1 whenever it finds anything. In the trial on the clone `C:\PROJECTS\GUPPI-trial`, `/box` called `/work`, and line 233 of the transcript `21f5559f-a385-4f16-be94-df02e138242f.jsonl` holds the refusal `` Shell command failed for pattern "!`uv run --project .guppi guppi check`" ``, with the three lines that the check printed. The agent then read the skill file and ran Work Mode by hand. The brief of this repository reports the same check under Readings at the close: `guppi check`: exit 1, 3 lines. So the `/work` of this repository fails to load the same way today. The text of `/work` says that a line can come back empty when its command fails, and that the agent then runs the command itself. Claude Code does not do that. `/retro` runs `guppi test` and `guppi style` the same way, so a red test stops `/retro` from loading, which is exactly when Retro has to fix or revert one. The lesson `lesson-hi-fails-outside-a-git-repository` gives the same cause for `/hi`, and case 851.3 fixed it by `guppi gitstate`, which exits 0 in each case.
>
> The person turned down a skill text where the agent runs the commands by hand, and asked that the tests run by themselves when the skill loads. The person also said that a core page in draft must block CI and the push to prod, not the work. So `guppi test`, `guppi style` and `guppi check` take a flag, `--exit-zero`. With it, a command prints its lines as before, then one last line `exit code: <n>` with the exit code that the run has without the flag, and exits 0. `/work` and `/retro` call their commands with the flag. Without the flag nothing changes. The job `lint` of `.github/workflows/checks.yml` runs `uv run --project .guppi guppi check` with no flag, and `.github/workflows/prod.yml` runs `guppi ship`, which refuses a draft core page. So both stay red on such a page. The finding of a draft core page stays in `guppi lint` (`check_status` of `.guppi/guppi/lint.py`, by `is_draft_core` of `.guppi/guppi/pages.py`), and this Case does not touch it. Moving it out alone would not unblock `/work`, since the failed Estimate is a finding of its own.
>
> The documentation of Claude Code on skills, https://code.claude.com/docs/en/skills, says that a failed command aborts the entire skill invocation and that, with the default `bash` shell, any non-zero exit code counts as a failure. It also says that in auto mode a command that needs approval does not abort the skill: Claude Code itself tells Claude to run it first. So the sentence of `/work` on an empty line is false, and the person chose to drop it. The line `Branch:` keeps `git branch --show-current`, which fails only outside a git repository, where `/hi` already stops the session.
>
> The code. `run` of `.guppi/guppi/commands.py` runs the commands of a key of `guppi.toml` and returns 1 when one is red or when the file or the key is missing. `run_test` and `run_style` call it. `run` of `.guppi/guppi/check.py` runs the six steps and returns 1 when any step is red. A Grep of `exit-zero|exit_zero|"exit:|f"exit` over `.guppi/guppi/` printed nothing, so no code there prints an exit code yet. The flag and the last line live in one function of `commands.py`, and `check.py` imports it, as `rule-one-judgment-one-implementation` sets it. A Grep of `` skills/work|skills/retro|rule-work-mode|rule-retro|rule-lint|rule-guppi-config|!`|guppi\.toml `` over `.guppi/tests/` printed `test_gate.py`, `test_case_schema.py`, `test_config.py`, `test_commands.py`, `test_casecheck.py`, `test_glossary.py`, `test_onward.py`, `test_lint.py`, `test_render.py`, `test_prespec.py`, `test_ship.py` and `test_sprint.py`. None of them reads `.claude/skills/work/SKILL.md`, `.claude/skills/retro/SKILL.md` or the four Rule pages live. Each one writes its own copy in a temporary folder, or only names the slug.
>
> The texts. A Grep of `exits? (non-zero|1) when any|makes the run red|0 only when every` over `{vault/wiki,.claude,.guppi/guppi,.guppi/tests}/**` printed `rule-guppi-config.md`, `rule-lint.md`, `log.md`, `check.py`, `commands.py`, `estimate-guppi-config-runs-the-test-and-style-commands.md` and `estimate-lint-runs-every-step.md`. The Purpose of each Rule page, the docstring of each module, and the Criterion and `purpose` of each Estimate state that exit code, so each one enters a sub-case. The hits in `log.md` and in the History of `rule-lint.md` are records. A Grep of `back empty` over the same paths printed `.claude/skills/work/SKILL.md`, `rule-work-mode.md` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline.md`, and each of them enters Case 1003.3. Under the rule of atomicity, the change makes four promises on four pages: the flag of `guppi test` and `guppi style`, the flag of `guppi check`, the load of `/work` and the load of `/retro`. So the Case has four sub-cases. Case 1003.1 and Case 1003.2 replace the Criteria of `estimate-guppi-config-runs-the-test-and-style-commands` and `estimate-lint-runs-every-step`, whose lines on the exit code the flag makes false. Case 1003.3 replaces the Criterion of `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`, whose line on an empty substitution is false. Each line of the three old Criteria that is not carried word for word stands in the new Criterion with the flag added. The two lines of the old Criterion of `estimate-guppi-config-runs-the-test-and-style-commands` on the key `test` in this repository are joined into one line, and the line of `estimate-lint-runs-every-step` on the Baseline of `/work` goes into its new `when` line on the preamble of `/work`. The lines of Case 1003.1 and Case 1003.2 on the flag share their words, but each one speaks of its own command and its own Estimate. In the same way, the lines of Case 1003.3 and Case 1003.4 on the load each speak of their own skill. So nothing is signed twice. No Estimate of `rule-retro` checks how the skill loads, so Case 1003.4 creates `estimate-retro-loads-on-a-red-command`, and a Glob of `vault/**/estimate-retro-loads-on-a-red-command.md` printed nothing. Three Estimates of `rule-retro` stand as they are. The Criterion of `estimate-retro-loads` checks only the readings of Retro, not how the skill loads. `estimate-retro-red-in-the-baseline-is-not-charged` and `estimate-retro-runs-on-to-the-handoff` speak of a failing test at Retro and of a commit that needs a clean style check and green tests. After the change, Retro still takes those results, now from lines that end with the exit code. So none of those lines becomes false. `estimate-spec-box-runs-a-conserved-spec` says that `/box` calls `/work` with the folder, and that Work Mode, the Work readings, `/retro` and `/handoff` run in one turn. That is the path that failed in the trial. The Case makes it hold while the check is red, so its Criterion stands. The `/pre-spec` run found that the `method` of `estimate-lint-runs-every-step` asked Retro to run `guppi check`, which the Render of `rule-retro` forbids. So the live run of the flag is left to `test_check.py`, which runs `check.run` with the flag. The `/pre-spec` run also found that the flag sentence on `rule-guppi-config` stood before the sentence on a missing file or key. So the flag sentence now follows that sentence and says that it holds in each case. Case 1002 changes `rule-orchestration` and `estimate-orchestration-acknowledging-reply`, and no page of this Case. The session's ledger holds the `error` lesson `lesson-work-skill-fails-to-load-on-a-red-check`, with no mark yet. Case 1003.3 fixes its root cause, so its decision line on `rule-work-mode` carries `{addresses:lesson-work-skill-fails-to-load-on-a-red-check}`.

> **problem:**
> `/work` and `/retro` run commands that exit non-zero when they find something. Claude Code then refuses to load the skill, so Work Mode cannot start while `guppi check` is red, and Retro cannot start while a test is red.

> **recommend:**
> - **How /work gets the baseline when a command is red**
>   - Recommended: (a) a flag on `guppi test`, `guppi check` and `guppi style` that prints the real exit code on a last line and exits 0, and the preamble of `/work` calls the commands with it.
>   - Answer: agreed, (a). In the first round the person turned down the option where the agent runs the commands by hand, and asked that the tests run by themselves.
> - **Where a draft core page stops things**
>   - Recommended: (a) keep the finding in `guppi check`, so CI and the build for prod stay blocked, and only Work Mode stops being blocked.
>   - Answer: agreed, (a). The person said that a draft core page must block CI and the push of the plugin to prod, not the work.
> - **What happens to the Branch line**
>   - Recommended: (a) keep the git line, and drop the sentence about an empty line.
>   - Answer: agreed, (a).
> - **Whether /retro is fixed in the same Case**
>   - Recommended: (a) yes, as a sub-case that changes `rule-retro` the same way.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) replace what `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` promises, test the flag in this session, and read the load after the librarian's render.
>   - Answer: agreed, (a).

### Case 1003.1 — guppi test and guppi style exit 0 with --exit-zero

> **given:**
> `rule-guppi-config`: the Rule page of `guppi test` and `guppi style`, whose Purpose names their exit code.
> **＋** `estimate-guppi-config-runs-the-test-and-style-commands`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/commands.py`: the code of both commands, and the one place of the flag.
> **＋** `.guppi/tests/test_commands.py`: the tests of both commands.
> **＋** `.github/workflows/checks.yml`: the jobs `test` and `style`, which run both commands with no flag.
> **＋** `.claude/skills/work/SKILL.md` and `.claude/skills/retro/SKILL.md`: the skills that run the commands with the flag.
> **＋** `uv run --project .guppi pytest -q .guppi/tests` and `.guppi/pyproject.toml`: the command of the key `test` in this repository and the settings it runs with.

> **when:**
> Someone runs `uv run --project .guppi guppi test` or `uv run --project .guppi guppi style` in a project, as `rule-guppi-config` sets it: by hand, in Work Mode, in Retro, or in the jobs `test` and `style` of `.github/workflows/checks.yml`.
> **＋** Or `.claude/skills/work/SKILL.md` or `.claude/skills/retro/SKILL.md` runs one of them with `--exit-zero` as it loads.

> **then:**
> It reads the list of commands of the key `test`, or of the key `style`, from `guppi.toml` at the root of the project.
> **＋** It runs each command of the list in order, in the folder of the project and with no shell between, each one even after a red one.
> **＋** The output of each command reaches the person whole, and no command gets the stdin of `guppi test` or `guppi style`.
> **＋** Without `--exit-zero`, a single red command makes the run red, and the run is green only when all the listed commands pass.
> **＋** With `--exit-zero`, it prints the same lines, then one last line `exit code: <n>`, where n is the exit code of the run without the flag, and it exits 0.
> **＋** In this repository, the key `test` holds `uv run --project .guppi pytest -q .guppi/tests`, and the key `style` holds `uv run --project .guppi ruff check .` and `uv run --project .guppi ruff format --check .`; that command of `test` runs the tests of `.guppi/tests/` with the settings of `.guppi/pyproject.toml`, the tests marked `live` left out, whether the root of the project holds a `pyproject.toml` of its own or none.
> **＋** The rules, entities and Estimates of the vault and the harness files of `.claude/` call the tests and the style check by these two commands, and never by make.
> **－** When `guppi.toml` is missing or holds no such key, it prints one line that names the file and the key, runs nothing and exits 1; with `--exit-zero` it prints the line `exit code: 1` after it and exits 0.
> **－** The render reads `documentation_lang` and `chat_lang` as before, and a key `test` or `style` does not stop it.

```then
update:
- slug: rule-guppi-config
  replace:
  - old: When `guppi.toml` or the key is missing, it prints one line that names the file and the key, runs nothing and exits 1.
    new: 'When `guppi.toml` or the key is missing, it prints one line that names the file and the key, runs nothing and exits 1. With `--exit-zero`, in each case, a missing file or key included, it prints one last line `exit code: <n>`, the exit code of the run without the flag, and exits 0, so a skill that runs it as a `!` command loads whatever the run finds (as set in case 1003.1).'
  change: guppi test and guppi style take --exit-zero, which prints the exit code on a last line and exits 0
- slug: estimate-guppi-config-runs-the-test-and-style-commands
  set:
    status: pending
    purpose: Whether guppi test and guppi style run the commands that the keys test and style of guppi.toml list, in order and each after a red one, exit non-zero when any is red, and exit 1 with one line when the file or the key is missing; whether with --exit-zero they print the exit code on a last line and exit 0; and whether the command of the key test runs the tests of .guppi/tests with the settings of .guppi/pyproject.toml whatever the root of the project holds
    method: 'uv run --project .guppi pytest .guppi/tests/test_commands.py; by hand, at Retro: uv run --project .guppi guppi test --exit-zero and uv run --project .guppi guppi style --exit-zero in this repository, their last lines and exit codes read, and a Grep for make test and make style over the live rules, entities and Estimates and over .claude/, read against the Criterion'
  change: the Criterion replaced whole — guppi test and guppi style take --exit-zero; purpose and method name it
```

```tasks
- [x] update `rule-guppi-config`
- [x] update `estimate-guppi-config-runs-the-test-and-style-commands`
- [x] `.guppi/guppi/commands.py`: `guppi test` and `guppi style` take `--exit-zero`; one function of this module adds the flag to a parser and, with the flag, prints the last line `exit code: <n>` and returns 0; the docstring names the flag.
- [x] `.guppi/tests/test_commands.py`: with `--exit-zero`, a red command, a green run and a missing key each print the last line with the exit code of the run without the flag and exit 0.
- [x] read `estimate-guppi-config-runs-the-test-and-style-commands`
```

### Case 1003.2 — guppi check exits 0 with --exit-zero

> **given:**
> `rule-lint`: the Rule page of `guppi check`, whose Purpose names its exit code.
> **＋** `estimate-lint-runs-every-step`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/check.py`: the code of `guppi check`.
> **＋** `.guppi/guppi/commands.py`: the one place of the flag, which `check.py` imports.
> **＋** `.guppi/tests/test_check.py`: the tests of `guppi check`.
> **＋** `.claude/agents/librarian-guppi.md` and `.github/workflows/checks.yml`: the librarian's run and the job `lint`, which run `guppi check` with no flag.
> **＋** `.claude/skills/work/SKILL.md`: the skill that runs `guppi check` with the flag.
> **＋** `.guppi/guppi/ship.py`: the module of `guppi ship --check`, the last step, skipped where it is missing.

> **when:**
> Someone runs `uv run --project .guppi guppi check` in a project: by hand, in the librarian's run of `.claude/agents/librarian-guppi.md`, or in the job `lint` of `.github/workflows/checks.yml`.
> **＋** Or `.claude/skills/work/SKILL.md` runs it with `--exit-zero` as it loads.
> **＋** Or `.guppi/tests/test_check.py` runs it in a temporary project whose steps record each call: once with the step `guppi backlog --check` failing, once with every step exiting 0, once with no module `.guppi/guppi/ship.py`, and with `--exit-zero` with a step failing.

> **then:**
> It runs `guppi render --check`, `guppi sprint --check`, `guppi backlog --check`, `guppi glossary --check`, `guppi lint` and `guppi ship --check`, in that order, whether an earlier step exited 0 or not.
> **＋** Each step prints its own lines as it does when it runs alone, so a red step hides no finding of a later step.
> **＋** Without `--exit-zero`, it exits non-zero when any step exits non-zero, and 0 only when every step exits 0.
> **＋** With `--exit-zero`, it prints the same lines, then one last line `exit code: <n>`, where n is the exit code of the run without the flag, and it exits 0.
> **＋** `guppi check` takes the flag and writes that last line by the function of `.guppi/guppi/commands.py` that `guppi test` and `guppi style` use, and holds no copy of it.
> **＋** No live rule, entity or Estimate outside History and Result, and no file of `.claude/`, names make with the target `lint` as the way to run the vault checks.
> **－** Where the module `.guppi/guppi/ship.py` is missing, as in a project that installed GUPPI, it runs the other five steps and prints one line that it skips `guppi ship --check`, and that skip sets no exit code.
> **－** No step reads the stdin of its caller, and it writes nothing to the tree.

```then
update:
- slug: rule-lint
  replace:
  - old: and it exits non-zero when any step is red (case 587).
    new: 'and it exits non-zero when any step is red (case 587). With `--exit-zero` it prints one last line `exit code: <n>`, the exit code of the run without the flag, and exits 0, so `/work` loads while the check finds something, and the librarian''s run and the job `lint` of CI, which run it with no flag, stay red (as set in case 1003.2).'
  change: guppi check takes --exit-zero, which prints the exit code on a last line and exits 0
- slug: estimate-lint-runs-every-step
  set:
    status: pending
    purpose: Whether guppi check runs every step, guppi ship --check last, when an earlier one is red, prints the lines of each, exits non-zero when any step is red, with --exit-zero prints the exit code on a last line and exits 0 by the function guppi test uses, and skips guppi ship --check where the command ship is missing
    method: 'uv run --project .guppi pytest .guppi/tests/test_check.py; by hand, at Retro: a Grep of make with the target lint over the live rules, entities and Estimates and over .claude/, read against the Criterion'
  change: the Criterion replaced whole — guppi check takes --exit-zero; purpose and method name it
```

```tasks
- [x] update `rule-lint`
- [x] update `estimate-lint-runs-every-step`
- [x] `.guppi/guppi/check.py`: `guppi check` takes `--exit-zero` by the function of `.guppi/guppi/commands.py` that adds the flag and prints the last line; the docstring names the flag.
- [x] `.guppi/tests/test_check.py`: with `--exit-zero` and a failing step, every step runs, the last line is `exit code: 1` and the run exits 0; one test asserts that `check.py` uses the function of `commands.py` and holds no copy of it.
- [x] read `estimate-lint-runs-every-step`
```

### Case 1003.3 — /work loads while guppi check is red

> **given:**
> `rule-work-mode`: the Rule page whose Render is `.claude/skills/work/SKILL.md`.
> **＋** `.claude/skills/work/SKILL.md`: the skill `/work`, whose lines Tests and Lint run their commands with `--exit-zero`.
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: its Criterion is replaced whole.
> **＋** `.guppi/guppi/commands.py` and `.guppi/guppi/check.py`: `guppi test` and `guppi check`, which take the flag.
> **＋** `vault/wiki/where-to-stop.md`: the conditions on which the run stops.
> **＋** `rule-spec-box`: `/box`, which calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
> **＋** `rule-prespec-onward`: the hook that sends the agent on until `spec.md` stands.
> **＋** `/retro`: the skill that `/work` calls at its end and that fixes or reverts a new failing test.
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/work.md` and `raw/<date>/<hi HHMM>/handoff.md`: the Spec, the baseline and the handoff of the session.

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
> **＋** Or, while the run of `/work` goes on, the person ratifies a Case built in Work Mode.

> **then:**
> `uv run --project .guppi guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** The skill loads while `uv run --project .guppi guppi check` or `uv run --project .guppi guppi test` finds something: its lines Tests and Lint run both commands with `--exit-zero`, and each line comes back with the output of its command and a last line that names the exit code of its run.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check`, as the last line of Tests and of Lint names it, with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
> **＋** The reply that acknowledges a Case ratified in Work Mode ends the turn, since the hook of `rule-prespec-onward` sends nothing on once `raw/<date>/<hi HHMM>/spec.md` stands; at the person's next message the run goes on from where it stopped.
> **＋** After the reply that acknowledges a Case ratified in Work Mode, and before the first task of that Case, the agent runs `uv run --project .guppi guppi prespec --check` on the plan file of the session, with the session id of its `hi:` line.
> **＋** When that check prints a line that does not open with `note:`, the agent stops as the first condition of `vault/wiki/where-to-stop.md` sets it and sends the finding to the `case-guppi` of that Case; the run goes on after the person ratifies the fixed Case and the check prints no such line.
> **＋** A task of that Case whose work already stands, done under the sub-case the Case replaces, is ticked in `raw/<date>/<hi HHMM>/spec.md` and not run again.
> **＋** A task that changes `uv run --project .guppi guppi check`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `uv run --project .guppi guppi test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
> **＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
> **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
> **－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
> **－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.
> **－** In a `/work` that `/box` calls no Case is ratified, so the check of the plan does not run there: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.

```then
update:
- slug: rule-work-mode
  replace:
  - old: A substitution of the skill can come back empty when the model call that checks it fails, so the agent then runs the command itself.
    new: Its preamble runs `uv run --project .guppi guppi test --exit-zero` and `uv run --project .guppi guppi check --exit-zero`, which print the exit code of their run on a last line and exit 0, since Claude Code refuses to load a skill whose `!` command exits non-zero (as set in case 1003.3).
  - old: 'Tests: !`uv run --project .guppi guppi test`'
    new: 'Tests: !`uv run --project .guppi guppi test --exit-zero`'
  - old: 'Lint: !`uv run --project .guppi guppi check`'
    new: 'Lint: !`uv run --project .guppi guppi check --exit-zero`'
  - old: A line above can come back empty when the check of its command fails. When Branch is empty, run `git branch --show-current` yourself before anything else. When Tests or Lint is empty, run `uv run --project .guppi guppi test` and `uv run --project .guppi guppi check` yourself before the first change, and use their result for the Baseline.
    new: Tests and Lint run with `--exit-zero`, so each exits 0 whatever it finds, and its last line names the exit code of its run, since Claude Code refuses to load a skill whose `!` command exits non-zero (as set in case 1003.3).
  - old: the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check`, then each failing test
    new: the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check`, as the last line of Tests and of Lint above names it, then each failing test
  change: the preamble of /work runs guppi test and guppi check with --exit-zero, so the skill loads while a check is red
- slug: estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline
  set:
    status: pending
    purpose: Whether /work loads while guppi check or guppi test finds something, stops on main, writes the baseline of uv run --project .guppi guppi test and uv run --project .guppi guppi check into work.md before the first change — the exit code of each as the last line of its preamble line names it — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, runs the check of the plan before the first task of a Case ratified in Work Mode, stops on its finding and ticks a task of that Case whose work already stands, and after the last task runs uv run --project .guppi guppi test in full and holds each failing test against the baseline, fixing a new one within ratified work
    method: 'by hand, after the librarian''s render that writes .claude/skills/work/SKILL.md from the Render of rule-work-mode with --exit-zero on its lines Tests and Lint: uv run --project .guppi guppi render --check; .claude/skills/work/SKILL.md read against each line of the Criterion; the first /work that loads after that render while uv run --project .guppi guppi check exits 1, its preamble lines, its work.md and its run of the tasks read in the transcript of its session under ~/.claude/projects/ and in its spec.md and work.md against the Criterion; the lines on a Case ratified in Work Mode read in that transcript where that session ratifies one, otherwise against the text of the skill; recorded in the estimate line with the transcript named'
  change: the Criterion replaced whole — /work loads while guppi check is red, its preamble running guppi test and guppi check with --exit-zero; purpose and method name it
```

```tasks
- [x] update `rule-work-mode`
- [x] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/work/SKILL.md`
- [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
```

### Case 1003.4 — /retro loads while a test is red

> **given:**
> `rule-retro`: the Rule page whose Render is `.claude/skills/retro/SKILL.md`.
> **＋** `.claude/skills/retro/SKILL.md`: the skill `/retro`, whose lines Tests and Style run their commands with `--exit-zero`.
> **＋** `estimate-retro-loads-on-a-red-command`: the new check that `/retro` loads while a test or the style check is red.
> **＋** `.guppi/guppi/commands.py`: `guppi test` and `guppi style`, which take the flag.
> **＋** `/work`: the skill that calls `/retro` at its end.

> **when:**
> The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote that file from `rule-retro`.

> **then:**
> The skill loads whatever `uv run --project .guppi guppi test` and `uv run --project .guppi guppi style` find: its lines Tests and Style run both commands with `--exit-zero`.
> **＋** Each of those lines comes back with the output of its command and a last line that names the exit code of its run, and the agent takes each failing test and each style finding from it.
> **－** The line Ledger runs `uv run --project .guppi guppi tail` as before.

```then
create:
- slug: estimate-retro-loads-on-a-red-command
  ref: rule-retro
  kind: QA
  purpose: Whether /retro loads while guppi test or guppi style finds something, its lines Tests and Style running both commands with --exit-zero and ending with the line that names the exit code
  method: 'by hand, after the librarian''s render that writes .claude/skills/retro/SKILL.md from the Render of rule-retro with --exit-zero on its lines Tests and Style: the text of .claude/skills/retro/SKILL.md read against the Criterion, and the first load of /retro after that render read in the transcript of its session under ~/.claude/projects/, the skill loaded and its lines Tests and Style each ending with the line that names the exit code; recorded in the estimate line with the transcript named'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-retro
  replace:
  - old: The tests and the style check load before the first turn of the skill.
    new: The tests and the style check load before the first turn of the skill, run with `--exit-zero`, which prints the exit code of the run on a last line and exits 0, so a red test does not stop the skill from loading (as set in case 1003.4).
  - old: 'Tests: !`uv run --project .guppi guppi test`'
    new: 'Tests: !`uv run --project .guppi guppi test --exit-zero`'
  - old: 'Style: !`uv run --project .guppi guppi style`'
    new: 'Style: !`uv run --project .guppi guppi style --exit-zero`'
  change: the preamble of /retro runs guppi test and guppi style with --exit-zero, so the skill loads while a test is red
```

```tasks
- [x] update `rule-retro`
- [x] create `estimate-retro-loads-on-a-red-command`
- [x] `uv run --project .guppi guppi render`: `.claude/skills/retro/SKILL.md`
- [ ] read `estimate-retro-loads-on-a-red-command`
```
