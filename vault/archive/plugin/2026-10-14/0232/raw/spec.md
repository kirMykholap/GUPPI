<!-- approved 03:10:22 · session cfcb07e8 -->

# Session 0232 — sprint plugin

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

```then
update:
- slug: rule-clean-branch
  replace:
  - old: on each comment or docstring that opens with a case number followed by a colon, and on each comment whose whole text is a case number,
    new: on each comment or docstring that opens with one or more case numbers, joined as in such a bracket, followed by a colon, and on each comment whose whole text is one or more case numbers joined the same way,
  change: guppi ship reports a list of bare case numbers at the opening of a comment or a docstring, or alone in a comment
- slug: estimate-clean-branch-writes-a-clean-copy
  set:
    status: pending
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
      **＋** It does the same for each comment or docstring that opens with one or more case numbers joined the same way, followed by a colon, such as `# 169.1:`, `"""75.2:` or `# 387.4, 445.4:`, and for each comment whose whole text is one or more case numbers joined the same way, such as `# 786` or `# 387.4, 445.4`.
      **＋** It exits 1 when a file it writes holds a section between the markers of a page without `core: true`.
      **＋** With `--review` it also prints the file, the line and the bracket for each bracket it removes that holds words beside its pointers, and those lines set no exit code.
      **＋** With `--check` it judges each file it would write outside `vault/` — `guppi/`, `.claude/` and the files at the root of the project — but `uv.lock`, which it does not clean, as it would write it, prints the same lines for it, exits 1 on any, and writes nothing.
      **－** It writes no page without `core: true`, nothing of `vault/raw/`, `vault/archive/` or `.github/`, and no `sprint.md`, `backlog.md`, `brief.md`, `log.md` or `guppi.toml`.
      **－** It writes no file that a page without `core: true` renders in full.
      **－** A case id inside a code span of a Markdown file, or after `[case ` or `#case-`, is the form of a line, not a reference.
      **－** A case id inside a fenced block of a Markdown file, inside a code span of the text of a `schema.yaml`, in `vault/wiki/case-example.md` or the Render of `rule-case-example`, or after `:case `, is the form of a sample or of a line: it is neither removed nor printed.
      **－** It removes no bare case number: the copy holds it as written.
      **－** It judges no code of a Python file outside its comments and docstrings for a bare case number, such as `match.group(1)`, and a number or a list of numbers that opens a comment with words and no colon after it, such as `# 3, 4 tries`, is no finding.
  change: the Criterion replaced whole — guppi ship reports a list of bare case numbers at the opening of a comment or a docstring, or alone in a comment
```

```tasks
- [x] `guppi/ship.py`: one pattern of a list of case numbers, joined by a comma, a semicolon, `and` or a dash, serves `BARE_BRACKET`, `BARE_OPENING` and `BARE_ALONE`; the opening and the comment alone take the list, and the module docstring and the comment above the patterns say so.
- [x] `tests/test_ship.py`: a comment and a docstring that open with a list of case numbers and a colon, and a comment that is a list of case numbers alone, each exit 1 and stay in the copy; a comment that opens with a list of numbers and words with no colon is no finding.
- [x] `uv run guppi ship --check`: prints no line after the change.
- [x] update `rule-clean-branch`
- [x] update `estimate-clean-branch-writes-a-clean-copy`
- [x] read `estimate-clean-branch-writes-a-clean-copy`
```

## Case 812 — The id of a new Case comes only with the session's stamp and its plan file

> **context:**
> The main agent takes the number of a new top-level Case from `uv run guppi caseid --next`, which prints the next free id and holds it in the store of the session's plan file, so that the next run prints the id after it. `guppi/caseid.py` finds the session by its stamp, which `session_stamp` of `guppi/event.py` takes from `--session` or a hook payload; a Bash call has no payload, so without the option the stamp is `--------`, `session_dir` and `plan_path` of `guppi/ledger.py` find no folder and no plan file, and the command prints an id it does not hold and counts it without the session's ledger and Case files. With a stamp that finds no plan file, a wrong stamp or a plan file not yet created, it prints the id too, holds nothing and exits 0. `orchestration.md` (twice) and `ratification.md` name the command without the option, and last session it printed one id twice, as `lesson-caseid-held-no-id-without-the-session-option` records. The person chose that the pages name `--session <stamp>`, the stamp of the `hi:` line, that the command refuses to run without it, as `guppi box` does, and, at `/pre-spec`, that it refuses a stamp with no plan file too: a Grep of `add_argument\("--session"` over `guppi/` printed `guppi/box.py` (`required=True`), `guppi/caseid.py`, `guppi/event.py` and `guppi/prespec.py`. The rule weighed against the option of reading the newest `hi` line of the event log is the one that `resolve_session` of `guppi/prespec.py` states for the same stamp: the session is never guessed, since a parallel session writes its own `hi` into the same log and after midnight today's log holds none (case 213.1). The change adds no judgment of a text, only a required option of the parser and a refusal.
> This Case replaces case 810, ratified in this session, after three findings of `/pre-spec`. First, its placeholder `<id>` would have clashed with the sprint `<id>` of the same sentence of `ratification.md`, which names the opening Case of a sprint `<id>-1`, so the stamp is `<stamp>`. Second, `estimate-orchestration-shows-the-built-case` promises the Work Mode dispatch under the id that `uv run guppi caseid --next` prints, a run that now prints no id, and its `method` reads the new Render of `rule-orchestration` at Retro, so Case 812.2 replaces its Criterion; that is a second promise, so the Case is built again with sub-cases under a new number, its decision lines marked `{supersedes:case 810}`. Third, the refusal of a stamp with no plan file. Since the command then refuses before the plan file stands, the Render sentence that has the main agent create the plan file before the first dispatch now says before its first run of the command; the Then of `estimate-orchestration-shows-the-built-case`, which names the dispatch after the plan file stands, stays true. A Grep of `title line` over `vault/wiki/` printed `orchestration.md`, `log.md`, `rule-ask.md`, `rule-spec-reconcile.md`, `rule-skill-hi.md`, `rule-orchestration.md`, `rule-case-check.md`, `estimate-orchestration-shows-the-built-case.md`, `rule-prespec.md`, `estimate-ask-finds.md`, `estimate-prespec-reconciles.md`, `estimate-hi-takes-a-conserved-spec.md`, `estimate-spec-reconcile-refuses-an-edit-of-the-plan.md`, `estimate-prespec-checks-the-frontier.md`, `estimate-case-check-sends-back-a-faulty-round.md` and `estimate-case-check-requires-each-question-of-the-rounds.md`, and over `.claude/` it printed `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md` and `.claude/agents/ask-guppi.md`. `log.md` is not read. Of the rest, only `orchestration.md` and `rule-orchestration.md` set when the plan file of a session that builds Cases is created. `rule-skill-hi`, its estimate and its skill set only the plan file of a conserved Spec, which builds no Case. The others speak of the title line that names a conserved Spec, of the guard that lets that line through, or of the title line of a question.
> `estimate-ratification-case-id-carries-the-sprint` checks the command, and its Criterion names it without the option, so its Criterion is replaced whole, written under `sections`, and its `purpose` names the option; its `method`, `uv run pytest tests/test_caseid.py` and the reading of the new Renders in `spec.md` at Retro, stands. Five lines of the old Criterion are not carried word for word: three now name `--session` — the run of the main agent, the sprint the command takes and the id it holds — and two name case 788.2 where they said this Case, since in a Criterion replaced by case 812 those words would name case 812, which brought in no sprint ids. A Grep of `caseid` over `vault/wiki/` printed `brief.md`, `ratification.md`, `orchestration.md`, `log.md`, `lesson-caseid-held-no-id-without-the-session-option.md`, `rule-orchestration.md`, `rule-ratification.md`, `estimate-orchestration-shows-the-built-case.md`, `estimate-case-check-sends-back-a-case-number-held-by-another-agent.md`, `estimate-spec-box-refuses-a-stale-spec.md`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape.md` and `estimate-ratification-case-id-carries-the-sprint.md`; over `.claude/` it printed nothing. `brief.md` and `log.md` are not read. `estimate-case-check-sends-back-a-case-number-held-by-another-agent`, `estimate-case-check-sends-back-a-ratified-case-in-another-shape` and `estimate-spec-box-refuses-a-stale-spec` speak of the store entry, of `next_id` and of the grammar of an id, which do not change, so they stand. The lesson gets no mark, since it was written in another session; it quotes the old message of the command as what it printed then, so it stands. A Grep of `orchestration\.md|ratification\.md` over `tests/` printed `tests/test_ship.py`, `tests/test_ledger.py` and `tests/test_orchestration.py`: the first reads a copy under a temporary folder, the second only names the file in a message, and the third reads only the blocks tagged `showing` and `defer`, which this Case does not touch, so they stand. A Grep of `caseid\.run|"caseid"` over `tests/` printed `tests/test_caseid.py` and `tests/test_casecheck.py`; both run the command with `--session` over a session whose plan file stands, so they pass the new refusals.

> **problem:**
> The command that numbers a new Case is written without the option that tells it the session, and without it, or without the plan file of that session, the command prints an id that it does not hold and that may already be taken.

> **recommend:**
> - **Where should the command get the session id when you start a new Case?**
>   - Recommended: (c) the pages name `--session <id>`, and the command refuses to run without it.
>   - Answer: agreed, (c).
> - **Which check should prove the fix?**
>   - Recommended: (a) rewrite the text of `estimate-ratification-case-id-carries-the-sprint` whole.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: a finding of `/pre-spec` — the placeholder `<id>` of the stamp clashes with the sprint `<id>` of the same sentence of `ratification.md`.
>   - Taken: the stamp is written `<stamp>` in every new text.
> - **Change**
>   - Asked: a finding of `/pre-spec` — `estimate-orchestration-shows-the-built-case` promises the dispatch under the id of a run that now prints no id.
>   - Taken: Case 812.2 replaces its Criterion, and the Case is built again with sub-cases under a new number.
> - **Change**
>   - Asked: a finding of `/pre-spec`, put to the person — with a stamp that finds no plan file the command still prints an id it does not hold; the person agreed that it refuses: prints no id and exits 1, and the main agent creates the plan file before it takes a number.
>   - Taken: the refusal stands in the `then` and the Criterion of Case 812.1, with a task for the code and its test, and the Render has the plan file created before the first run of the command.

### Case 812.1 — The command takes the session's stamp and refuses without its plan file

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, gives the command for a new top-level Case.
> **＋** `rule-ratification`: its Render, `vault/wiki/ratification.md`, states what the command does.
> **＋** `guppi/caseid.py`: the command `guppi caseid --next`.
> **＋** `tests/test_caseid.py`: the tests of the command.
> **＋** `estimate-ratification-case-id-carries-the-sprint`: its Criterion is replaced whole.

> **when:**
> The main agent runs `guppi/caseid.py` by `uv run guppi caseid --next` before it dispatches a new top-level Case, with `vault/wiki/orchestration.md` and `vault/wiki/ratification.md` rendered from `rule-orchestration` and `rule-ratification`.

> **then:**
> `vault/wiki/orchestration.md` and `vault/wiki/ratification.md` give the command as `uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of the session.
> **＋** `vault/wiki/orchestration.md` has the main agent create the plan file of the session with its title line before its first run of the command.
> **＋** With `--session` and the plan file of the session of that stamp, `guppi/caseid.py` prints and holds the next id of that session, as before.
> **－** Without `--session`, `guppi/caseid.py` prints no id: it prints its usage error and exits 2.
> **－** With `--session` and no plan file of the session of that stamp, `guppi/caseid.py` prints no id, holds nothing, prints one line on stderr and exits 1.

```then
update:
- slug: rule-orchestration
  replace:
  - old: for a new top-level Case the id that `uv run guppi caseid --next` prints and holds
    new: for a new top-level Case the id that `uv run guppi caseid --next --session <stamp>` prints and holds, `<stamp>` the stamp of the `hi:` line of the session
  - old: and creates the plan file with its title line before the first dispatch of the session.
    new: and creates the plan file with its title line before its first run of `uv run guppi caseid --next --session <stamp>` in the session, since the command prints no id without that file.
  - old: under the id that `uv run guppi caseid --next` prints, with the path of the file of the ratified Case
    new: under the id that `uv run guppi caseid --next --session <stamp>` prints, with the path of the file of the ratified Case
  change: 'the command for the id of a new Case carries --session with the stamp of the hi: line, and the plan file stands before its first run'
- slug: rule-ratification
  replace:
  - old: '`uv run guppi caseid --next` prints the id of the next Case of the open sprint and holds it'
    new: '`uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of the session, prints the id of the next Case of the open sprint and holds it in the store of the session''s plan file, and prints no id without `--session` or without that plan file'
  change: guppi caseid --next takes --session, and prints no id without it or without the plan file of the session
- slug: estimate-ratification-case-id-carries-the-sprint
  set:
    status: pending
    purpose: Whether every reader of a Case id takes an id that carries its sprint and a plain id from before sprint ids alike, and guppi caseid --next --session <stamp> prints and holds the next id of the open sprint, which the main agent uses, and prints no id without --session or without the plan file of the session
  sections:
    Criterion: |-
      When:
      `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py` or `guppi/materialize.py` reads a Case id in a ledger line, a heading of a Case file, a file name `case-<id>.md` or an `origin`.
      **＋** The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, runs `uv run guppi caseid --next --session <stamp>`, `<stamp>` the stamp of the `hi:` line of its session, before it dispatches a new top-level Case.
      **＋** Or `uv run guppi caseid --next` runs without `--session`, or with a stamp whose session has no plan file.

      Then:
      A Case id of a sprint opened after case 788.2 is the sprint id, a hyphen and the number of the Case in that sprint, from 1, with a dot for each sub-case level, such as `kir-plugin-12.1`, and its Case file is `case-<id>.md` of its top-level Case.
      **＋** The readers read a Case id through `guppi/caseid.py`, which takes both forms and reads the sprint id as the text before the last hyphen ahead of the number.
      **＋** The sprints `migration` and `plugin`, opened before case 788.2, keep plain ids to their close, by a fixed list in `guppi/caseid.py`.
      **＋** The main agent creates the plan file of its session with its title line before its first run of the command.
      **＋** `uv run guppi caseid --next --session <stamp>` takes the open sprint from the `create` decision line of a sprint page in `raw/<date>/<hi HHMM>/ledger.md` of the session of that stamp, else from the first heading of `vault/wiki/sprint.md`, and prints the next id of that sprint.
      **＋** It holds the id it prints in `<plan>.checked.json` of the plan file of that session, under that id, with no `agent_id` and no text, so that the next run prints the id after it.
      **＋** The main agent dispatches each new top-level Case with the id that the command printed, but the opening Case of a sprint, whose id `/sprint-open` sets.
      **－** Without `--session` the command prints no id: it prints its usage error and exits 2.
      **－** With a stamp whose session has no plan file, the command prints no id, holds nothing, prints one line on stderr and exits 1.
      **－** An id with no sprint part, such as `785.1`, stays a Case from before sprint ids, and no page, file or citation is renamed.
  change: 'the Criterion replaced whole — guppi caseid --next takes --session with the stamp of the hi: line, and prints no id without it or without the plan file of the session'
```

```tasks
- [x] update `rule-orchestration`
- [x] update `rule-ratification`
- [x] update `estimate-ratification-case-id-carries-the-sprint`
- [x] `guppi/caseid.py`: the option `--session` is required; with no plan file of the session the command prints one line on stderr that names the missing plan file, prints no id, holds nothing and exits 1; the docstring says both.
- [x] `tests/test_caseid.py`: a test that a run of `guppi caseid --next` without `--session` exits 2 and prints no id, and a test that a run with `--session` over a session with no plan file exits 1, prints no id and writes no store.
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] `uv run guppi render`: `vault/wiki/ratification.md`
- [x] read `estimate-ratification-case-id-carries-the-sprint`
```

### Case 812.2 — The Work Mode dispatch names the command with the stamp

> **given:**
> `rule-orchestration`: its Render, `vault/wiki/orchestration.md`, sets the Work Mode dispatch of a new Case.
> **＋** `estimate-orchestration-shows-the-built-case`: its Criterion is replaced whole.

> **when:**
> In Work Mode a ratified Case of the approved Spec must change, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

> **then:**
> The main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session.

```then
update:
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.
      **＋** Or the person puts off or keeps the item of a Case that `case-guppi` built and that is not ratified, or drops that Case so that the item ends another way.
      **＋** Or the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified.
      **＋** Or, in Work Mode, a ratified Case of the approved Spec must change: the work meets a choice it did not make, the person asks for a change, or the main agent finds its text wrong or too narrow.

      Then:
      The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
      **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
      **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
      **＋** An answer with no first line `**Built:**`, `**Fact:**` or `**Dropped:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, its label naming its Case and its item of `raw/<date>/<hi HHMM>/frontier.md` when the round is one of a batch, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
      **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
      **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
      **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses — its file not sent, or a showing that differs from the checked text — is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it.
      **＋** A round or a Case shown with a text of the main agent's own before it or outside its list is not refused and is not shown again: `rule-case-check` tells the agent of it at the person's next message, and the agent keeps the form from the next showing on.
      **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
      **＋** In Work Mode, when a ratified Case of the approved Spec must change, the main agent dispatches `case-guppi` for a new top-level Case under the id that `uv run guppi caseid --next --session <stamp>` prints, `<stamp>` the stamp of the `hi:` line of the session, with the path of the file of the ratified Case, the sub-case of it that must change and the reason, shows the new Case as any built Case, and the person ratifies it.
      **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run over the whole plan at its first run, never to build a Case, and asks that run again only to confirm its own findings.
      **＋** When the person puts off or keeps the item of a Case that `case-guppi` built and that has no decision line in `raw/<date>/<hi HHMM>/ledger.md`, or drops that Case so that the item ends another way, the main agent sends the drop by `SendMessage` to the `case-guppi` of that Case, and the turn of the person's words ends with one line under the bold label `**Waiting:**`, translated, and nothing else. The agent goes on with the item only in the turn that the answer `**Dropped:**` of that `case-guppi` opens, so that the hook of `rule-prespec-onward` finds the file of the Case empty at the end of every later reply.
      **＋** The drop adds no closer: the line of the item in `raw/<date>/<hi HHMM>/frontier.md` closes by one of the closers of `vault/wiki/orchestration.md`, as fits what the person chose — `[x] … · work`, `[x] … · case N` of another Case, `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
      **＋** When the person drops a change to a ratified Case that its `case-guppi` made after the Case was last ratified, the main agent sends the drop to that `case-guppi` by `SendMessage`. `case-guppi` undoes the change and answers with the summary of the Case in its ratified form. The main agent shows the Case again as after a change, and the person ratifies it again, the acknowledging reply carrying the same decision lines, so that the hook of `rule-prespec-onward` counts the Case as ratified.
      **－** In Work Mode the main agent sends no Case of the approved Spec back to its `case-guppi` to be built again under its own number; only a Case ratified in that Work Mode, none of whose tasks has run, changes that way.
      **－** In a `/work` that `/box` calls, no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.
      **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
      **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
      **－** The main agent writes no context of its own before the first question of a round. The label that names the Case of a round in a batch is no such context.
      **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
      **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
      **－** The file of a Case with a decision line in `raw/<date>/<hi HHMM>/ledger.md` is never emptied: it keeps the `context` and `given` that its Decision page leaves there.
  change: 'the Criterion replaced whole — the Work Mode dispatch names guppi caseid --next with --session and the stamp of the hi: line'
```

```tasks
- [x] update `estimate-orchestration-shows-the-built-case`
- [x] read `estimate-orchestration-shows-the-built-case`
```
