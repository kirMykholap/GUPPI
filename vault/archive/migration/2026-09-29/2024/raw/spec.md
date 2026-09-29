<!-- approved 01:32:33 · session 876c4080 -->

# Spec — session 2024, 2026-09-29

## Case 526 — The pages say what PyYAML does with a `#` after a tab

> **context:**
> When the person puts a decision off, the main agent writes a short Case itself. Its fence tagged `then` holds plain YAML. The `Stop` hook of `rule-spec-write` (`guppi/ratified.py`) refuses the fence when it holds a YAML comment, and `materialize` marks the entries of that Case `incomplete: [comment]`. Both call `then_comments` of `guppi/materialize.py`, which judges each fence by `yaml_comments` (cases 521.1, 521.2). `yaml_comments` counts a `#` at the start of a line or after a space or a tab. Case 521 gave one reason for both characters: YAML drops the rest of the line, so an unquoted value is cut. That reason holds for a space. It does not hold for a tab. PyYAML, the library the scripts use, does not cut the value at a tab before `#`. It refuses the whole block. The handoff of session 1753 says so: "PyYAML does not cut a value at a tab before `#`: it refuses the block." The comment in `tests/test_materialize.py` says the same: "PyYAML cuts the value there; a tab before `#` it refuses to parse". The YAML standard counts a tab as a separator, so the old sentences are true of the language but not of the library we run. The check behaves correctly for both characters, and the tests of both files cover the tab. Only the explanation is wrong.
> The wrong reason stands in the three rule pages, in four places of the code and in one test. In `rule-case-protocol` it is the short-form paragraph, rendered into `case-schema.md`: "YAML reads the rest of the line as a comment". In `rule-spec-write` and `rule-materialize` it reads "YAML drops the rest of the line". In the code, the docstring of `yaml_comments` and the module docstring of `guppi/ratified.py` repeat it. The refusal message of `deferred_section` in `guppi/ratified.py` says "put the value in quotes, since YAML drops the rest of the line". The comment at the call of `then_comments` for a decision entry in `guppi/materialize.py` says "YAML may have cut a value there". In the tests, the comment over the tab parameter `"a\t# b"` in `tests/test_ratified.py` says "YAML reads the rest of the line as a comment, so the value would be cut". This Case corrects every one of them. The person chose in the round that the code and the pages must say the same thing.
> In one round the person accepted every recommendation. Name both outcomes, fix the code text in the same Case, and change no promise. The Case creates no page, so no vault query was run. The text of Case 521 in the Spec of session 1753 and on its Decision pages stays as history. This context records the correction.
> What `case-guppi` found in the frame. `estimate-spec-write-writes-a-defer` and `estimate-materialize-marks-a-comment` define what the function counts, a tab included. Neither says that YAML cuts the value. The line "The entry keeps the values that YAML read, and nothing is invented for the text after the `#`" still holds for a tab: YAML read nothing, and nothing is invented. So both Criteria stand. The other Estimates of `rule-case-protocol`, `rule-spec-write` and `rule-materialize` speak of other behaviour, and they stand too. An `update` of the Render of `rule-case-protocol` touches no Estimate of the live reading (case 378.5). The other hooks on `Stop` in `.claude/settings.json` are `guppi ledger`, `guppi casecheck` and `guppi context`. None of them reads the message. The hook refuses exactly what it refused before, and only the wording of its reason changes. So nothing is refused in between, and no old form is kept. `tests/test_ratified.py` checks only the prefix "put the value in quotes", and the new message keeps it. A changed comment in a test file changes nothing that the test checks. One Case does the whole job: it is one correction of one claim, and its pages have no promise that could fail on its own. Pre-spec found the code comment in `guppi/materialize.py` and the test comment, and it found that the earlier text of this context called `yaml_comments` the function both sides call. This text corrects all three.
> Not done: the function, the refusal and the mark do not change. The Spec of session 1753 and the Decision pages of case 521 keep the old sentence.

> **problem:**
> Three rule pages, `case-schema.md`, the code and one test say that YAML cuts an unquoted value at a `#` after a tab. PyYAML refuses the block there instead. A reader of the pages, the code or the test learns a false fact about the parser the harness runs.

> **given:**
> `rule-case-protocol` — the rule; its Render is the case schema, with the short-form paragraph
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `rule-spec-write` — the rule of the `Stop` hook that refuses a short Case whose `then` block holds a comment
> **＋** `rule-materialize` — the rule of `materialize`, which marks such a Case's entries
> **＋** `guppi/materialize.py` — `then_comments`, which both sides call, and `yaml_comments`, which it uses; the docstring of `yaml_comments`; and the comment at the call of `then_comments` for a decision entry
> **＋** `guppi/ratified.py` — the module docstring on the defer, and the refusal message of `deferred_section`
> **＋** `tests/test_ratified.py` and `tests/test_materialize.py` — the tests of the refusal and the mark; the first holds a comment over the tab case

> **when:**
> An agent or the person reads the short-form paragraph of `vault/wiki/case-schema.md`, the sentence on a comment in `rule-spec-write` or `rule-materialize`, the docstrings and the comment in `guppi/materialize.py` and `guppi/ratified.py`, or the comment over the tab case in `tests/test_ratified.py`.
> **＋** The `Stop` hook `uv run guppi ratified` refuses a short Case whose `then` block holds a comment and writes its reason on stderr.

> **then:**
> Each of these texts says that after a space YAML drops the rest of the line, so an unquoted value is cut there, and that after a tab PyYAML, the library the scripts use, refuses the whole block.
> **＋** Each rule page and each docstring of these texts says that the hook refuses the block in both cases.
> **＋** The refusal on stderr gives the line of the comment and the advice to put the value in quotes, and it names both outcomes.
> **＋** The comment over the tab case in `tests/test_ratified.py` names the refusal by PyYAML. What `tests/test_ratified.py` and `tests/test_materialize.py` check does not change, and they pass.
> **－** What `yaml_comments` of `guppi/materialize.py` counts as a comment does not change. A `#` after a tab is still refused by the hook and still marked `incomplete: [comment]` by `materialize`.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: since YAML reads the rest of the line as a comment and the `Stop` hook of `rule-spec-write` refuses a block that holds one (case 521.4)
    new: since YAML drops the rest of the line at a `#` after a space, PyYAML, the library the scripts use, refuses the whole block at a `#` after a tab, and the `Stop` hook of `rule-spec-write` refuses a block that holds either (cases 521.4, 526)
  change: 'the short form says YAML cuts a value at a # after a space and PyYAML refuses the block at a # after a tab (case 526)'
- slug: rule-spec-write
  replace:
  - old: since YAML drops the rest of the line and no page receives it (case 521.1)
    new: since after a space YAML drops the rest of the line and no page receives it, and after a tab PyYAML, the library the scripts use, refuses the whole block (cases 521.1, 526)
  change: 'the refusal of a comment says YAML cuts a value at a # after a space and PyYAML refuses the block at a # after a tab (case 526)'
- slug: rule-materialize
  replace:
  - old: YAML drops the rest of the line, so the value may be cut;
    new: after a space YAML drops the rest of the line, so the value may be cut, and after a tab PyYAML, the library the scripts use, refuses the whole block;
  change: 'the mark of a comment says YAML cuts a value at a # after a space and PyYAML refuses the block at a # after a tab (case 526)'
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `rule-spec-write`
- [x] update `rule-materialize`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `guppi/materialize.py`: the docstring of `yaml_comments` says that after a space YAML drops the rest of the line, so an unquoted value may be cut, and that after a tab PyYAML refuses the whole block; the comment at the call of `then_comments` for a decision entry names both outcomes
- [x] `guppi/ratified.py`: the module docstring on the defer says the same; the refusal message of `deferred_section` keeps "put the value in quotes" and names both outcomes
- [x] `tests/test_ratified.py`: the comment over the parameters of the refused defer says that YAML cuts `a ## b` and that PyYAML refuses the block of `a\t# b`; no assertion changes
- [x] `uv run pytest tests/test_ratified.py tests/test_materialize.py -k comment`: passes
```

## Case 527 — A glossary row passes when its page says what the term is

> **context:**
> The glossary is the `## Terms` table of `entity-glossary`. Each row holds a term, a one-line meaning and a `where` link to the live page that defines the term. `uv run guppi glossary` renders the table into `vault/wiki/glossary.md`, and `/hi` loads it. `estimate-glossary-terms-defined` promises that each `where` page "defines the term of the row". The reading at the `/hi` of this session, after the librarian's run 1c196e8 that applied case 520, failed on three rows. `rule-hook-registry` does not say what a hook is. The Retro row puts the short defer under `## Retro` in the Spec, but `rule-retro` puts it under `## Deferred`, and so does `case-schema.md`. `rule-harness` does not say what the harness is. Only `case-schema.md`, the Render of `rule-case-protocol`, says it.
> The readings also do not agree on what "defines" means. The reading of session 1753 (L4) failed five rows and accepted the others. A strict pass in this session found eighteen rows whose page defines the term but leaves out some claim of the meaning. One example is Handoff, whose page `rule-handoff` never names `guppi gate`. The pass reported each of these as a claim the page leaves out, not as a claim the page contradicts. `lesson-glossary-one-where-for-a-term-many-schemas-define` shows the cost of the strict reading: a meaning cut down to its one `where` page becomes narrower than the truth.
> In one round the person accepted every recommendation, in their words: "OK, I agree".
> - A row passes when its page says what the term is and nothing in the meaning contradicts that page. Details may rest on other pages.
> - This reading goes into the Criterion, which is replaced whole in 527.2.
> - Hook and Harness get their definitions from a new sentence in the Purpose of their `where` pages.
> - The sentence of `rule-retro` on who writes the short defer stays out of this Case.
>
> Pre-spec found two faults in the ratified text. This answer fixes both.
> - Case 531.1 of this session replaces the Render of `rule-retro` whole. After it, Retro writes no short defer, and the sentence that puts one under `## Deferred` is gone. 531.1 also rewrites the Retro row around the words that 527.1 changes, and its pairs match the row before and after 527.1. After both Cases, the row says that a short defer stands only at the close of Plan Mode, under `## Deferred` in the Spec. That rests on `case-schema.md`, which puts a short defer under the `## Deferred` heading of the plan file. So 527.1 now names `case-schema.md` for this line, not `rule-retro`. The contradiction on who writes a Retro defer goes away with 531.1.
> - The first text of the `rule-harness` sentence listed a closed set of files. That list left out `guppi.toml`, which `rule-guppi-config` renders and whose rule the same Purpose counts. It also left out `vault/wiki/where-to-stop.md`, which Case 531.7 renders from `rules/`. The sentence and the row Harness now define the harness as the files that `guppi render` writes from the pages of `rules/`, and they name some of those files as examples. A new rendered file then needs no change to the row.
>
> What `case-guppi` found in the frame:
> - `estimate-harness-pipeline` reads the Purpose of `rule-harness`. It reads only the three rules, the order of `make lint` and the rules outside any pipeline. The new sentence makes none of that false, so the Estimate is not named.
> - `estimate-hook-registry-rendered` reads the render of `.claude/settings.json`. The Purpose of `rule-hook-registry` is outside its `## Render`, so the file does not change.
> - The Estimates of `rule-glossary` read the render, the check and the ticks, not these rows.
> - The Purpose of `entity-glossary` calls `where` "the live page that defines it". That stays true under the new reading.
> - The near backlog item `rule-page-generation` is deferred by case 469, which is about a supersede of an archived Decision. This Case does not touch it.
>
> The check of the answer notes that one line of the old Criterion is not carried word for word. The change is on purpose. The old line was "Each row names in `where` a `[[slug]]` of a live page, and that page defines the term of the row." In 527.2 it ends "that page says what the term of the row is", which is the reading the person chose. The new `＋` and `－` lines say that a contradiction fails a row and that a claim the page leaves out does not. The line on a term in two rows and the `－` line on the terms that are not rows are carried word for word.
> The open `read` line of this Estimate in the 1753 Spec closes at the librarian's run. The reading of this session ticks it, because `generate` ticks the lines of a slug in every live Spec of `raw/` (case 326). The Case creates no page, so no vault query was run. Not done: the eighteen rows keep the claims their pages leave out.

> **problem:**
> Three rows of the glossary link to a page that does not say what the term is, or that contradicts the row. The Criterion of `estimate-glossary-terms-defined` does not say how strictly "defines the term" reads, so two readings of one table counted different rows as failed.

### Case 527.1 — The rows Hook, Harness and Retro match their pages

> **given:**
> `entity-glossary` — the page whose `## Terms` table this Case changes
> **＋** `vault/wiki/glossary.md` — the render of the table, grouped by the parent MOC of `where`
> **＋** `rule-glossary` — the guard: one link per `where` cell, a live page, no term twice
> **＋** `rule-hook-registry` — the `where` page of Hook, whose Purpose gains what a hook is
> **＋** `rule-harness` — the `where` page of Harness, whose Purpose gains what the harness is
> **＋** `rule-render-harness` — the renderer `guppi render`, which writes the files of the harness from the pages of `rules/`
> **＋** `rule-case-protocol` — its Render `case-schema.md` puts a short defer under the `## Deferred` heading of the Spec

> **when:**
> `uv run guppi glossary` renders `vault/wiki/glossary.md` from the `## Terms` table of `entity-glossary` at the librarian's run, and a reader follows the `where` link of the rows Hook, Harness and Retro.

> **then:**
> The Purpose of `rule-hook-registry` says what a hook is, and the row Hook stands as it is.
> **＋** The Purpose of `rule-harness` says that the harness is the files that `guppi render` writes from the pages of `rules/`, and the row Harness says the same.
> **＋** The row Retro puts the short defer under `## Deferred` in the Spec, as `case-schema.md` does.
> **－** The other rows of the table of `entity-glossary` do not change.
> **－** The Render of `rule-hook-registry` does not change.

```then
update:
- slug: entity-glossary
  replace:
  - old: '| Harness | Hooks, agents, skills rendered from `rules/` pages | [[rule-harness]] |'
    new: '| Harness | The files that `guppi render` writes from the pages of `rules/`, such as `.claude/settings.json` with its hooks, the skills and agents, `CLAUDE.md`, `case-schema.md` and `guppi.toml` | [[rule-harness]] |'
  - old: under `## Retro` in the Spec
    new: under `## Deferred` in the Spec
  change: 'the row Harness defines the harness as the files guppi render writes from rules/; the row Retro puts the short defer under ## Deferred, as case-schema.md does (case 527.1)'
- slug: rule-hook-registry
  replace:
  - old: Prevents a hook from being registered by hand, outside a ratified decision.
    new: Prevents a hook from being registered by hand, outside a ratified decision. A hook is a script that Claude Code runs when an event of the session fires, such as `Stop` or `PreToolUse`; the Rule page behind it names the script in `implementation_ref`.
  change: the Purpose says what a hook is (case 527.1)
- slug: rule-harness
  replace:
  - old: Prevents the tools of the harness from drifting apart from the pages that describe them.
    new: Prevents the tools of the harness from drifting apart from the pages that describe them. The harness is the files that `guppi render` writes from the pages of `rules/`, such as `.claude/settings.json` with its hooks, the skills and agents under `.claude/`, `CLAUDE.md`, `case-schema.md` and `guppi.toml`.
  change: 'the Purpose says what the harness is: the files guppi render writes from the pages of rules/ (case 527.1)'
```

```tasks
- [x] update `entity-glossary`
- [x] update `rule-hook-registry`
- [x] update `rule-harness`
- [x] `uv run guppi glossary`
```

### Case 527.2 — The glossary check reads whether the page says what the term is

> **given:**
> `estimate-glossary-terms-defined` — the promise on the rows of the glossary; its Criterion is replaced whole
> **＋** `entity-glossary` — the page whose `## Terms` table the Estimate reads
> **＋** `rule-glossary` — the guard whose script `uv run guppi glossary` reads the table
> **＋** `rule-lint` — the rule of `guppi lint`, which reads the same table

> **when:**
> `uv run guppi glossary` reads the `## Terms` table of `entity-glossary` at the librarian's run, and `guppi lint` and a reader read the same table.

> **then:**
> Each row names in `where` a `[[slug]]` of a live page, and that page says what the term of the row is.
> **＋** No claim of the meaning of a row contradicts its `where` page.
> **＋** No term stands in two rows.
> **－** A row does not fail because its `where` page leaves out a claim of its meaning.
> **－** The terms that the Purpose of `entity-glossary` names as not rows, C4 model, Delegate and the retired terms, stand in no row.

```then
update:
- slug: estimate-glossary-terms-defined
  set:
    status: pending
  change: the Criterion replaced whole — the where page says what the term is and contradicts no claim of the row; a claim it leaves out does not fail the row (case 527.2)
```

```tasks
- [x] update `estimate-glossary-terms-defined`
- [ ] read `estimate-glossary-terms-defined` — by hand in a later session after the librarian's run: the table of `vault/wiki/glossary.md` against each `where` page, and `make lint`
```

## Case 528 — The remote leaves the repository and `/hi`, and git tracks no raw date folder without a session

> **context:**
> The migration sprint closes when the leftovers of the old repository are gone, or are kept by a decision (`estimate-sprint-migration-leftovers-gone`). Case 510 deleted `vault/parked/` and the August documents under `docs/`. Case 102.1 deleted the old August archive root, with the line `delete: [old-archive]`. A Glob of `vault/archive/2026-*/**` finds nothing, and `vault/archive/` holds only `migration/`. Three things were left: the raw date folders, `git pull` and `gh`.
> At every session start `/hi` runs `git pull --ff-only` (`rule-git-context`) and `gh issue list --limit 5` (`rule-github-issues`). Both fail. The only remote, `origin`, is `c:/PROJECTS/job hunt ai`. That is the product repository this vault was split from. `migration` has no upstream. At the `/hi` of this session the pull printed "There is no tracking information for the current branch", and `gh` printed "To get started with GitHub CLI, please run: gh auth login". A note in the Closed section of `entity-sprint-migration` keeps both off the Frontier (case 268.2). Decisions 11.1 and 11.2 kept the two lines as they were, and cases 220 and 243 put the choice off to the close. `main` tracks `origin/main`, so after the merge of the sprint `/hi` on `main` would pull from the other project. Nothing in `guppi/` or `.claude/` reads the remote.
> Each past date folder under `vault/raw/` holds only `event_log.md`. `.gitignore` excludes it with `vault/raw/*/event_log.md`, and `rule-raw-archive` keeps it there on purpose. So git tracks no such folder, but the Criterion says "`vault/raw/` has no date folder without a session".
> In two rounds the person accepted every recommendation. After the first round they wrote "I agree with the recommendations", and after the second, "I agree".
> - The repository has no remote. `origin` is removed, the `Pull:` and `Open issues:` lines leave `/hi`, and `rule-github-issues` leaves the harness.
> - `rule-git-context` keeps the render, branch and status lines. Its promise that no pull runs mid-session goes with the pull.
> - The date folders stay on disk. The promise reads them by what git tracks.
>
> What `case-guppi` found in the frame:
> - The Criteria of `estimate-hi-no-read-calls` and `estimate-hi-writes-frontier` name `Pull:` and `Open issues:`. 528.3 replaces the first whole. Case 531.11 replaces the second.
> - The Frontier sentence of `rule-skill-hi` on a failed pull reads the sprint note. Case 531.11 removes the sentence, and 528.5 removes the note.
> - `rule-skill-hi` names both commands in `allowed-tools` and in its `description`.
> - `rule-session-start` explains the split into two Leaves by how `git pull` and `gh` fail, and it lists open issues among the sources of the Frontier.
> - `rule-ledger-tail` places its line after `rule-github-issues`.
> - The glossary row Issue points at `rule-github-issues`.
> - Each of these four texts is changed.
> - `cleanup` takes an archived slug out of the `children` and `estimates` lists of live pages (`rule-cleanup`).
>
> These texts stand as they are:
> - `rule-retro` says "`gh` is not available: name a deferred bug in the handoff". That stays true.
> - `rule-rules-schema` shows `rule-github-issues` in an example of an older sprint. It is an example.
> - `vault/wiki/tags.md` gives the tag `git` the meaning "branch, status, pull". The tag still fits `rule-git-context`, and `tags.md` is not a page.
> - `docs/migration/migration-plan.md` names `git pull`. The closing Case deletes it.
> - `rule-render-harness` names "the Render line of /hi after the pull" only in its History.
>
> Sub-case 528.4 changed the Frontier sentence of `rule-skill-hi` and the Criterion of `estimate-hi-writes-frontier`. Case 531.11 of this session superseded it and carries both changes, so 528.4 has left the Spec.
> `rule-git-context` and `rule-github-issues` are backlog items, deferred by cases 220 and 243. The lines of 528.1 and 528.2 that name them carry `{supersedes:case 220}{supersedes:case 243}`, and both pages leave the backlog (case 429).
> The check of the answer notes that some lines of the old Criteria are not carried. Each is left out on purpose:
> - In 528.1, the old lines of `estimate-git-context-current` named "the four commands", the `Pull:` line, a failing pull, and no `git pull` later in the session. The person chose to take the pull out with the remote and to drop the promise on a pull mid-session. The lines on `Render:`, `Branch:` and `Status:` are carried word for word.
> - In 528.3, the old first line of `estimate-hi-no-read-calls` listed `Pull:` and `Open issues:`. The new line is the same without them. The `－` line on read-tool calls is carried word for word.
> - In 528.5, the old archive and raw line of `estimate-sprint-migration-leftovers-gone` becomes two lines: the archive root with its decision named, and the tracked files of `vault/raw/`. "A decision stands on `git pull` … keep as is, or repair" becomes the decision taken: no remote, and neither command in `/hi`. The `－` line "What to do with … those are the Cases of Slice 5" goes, because this Case decides those things. The lines on `vault/parked/`, on `docs/` and on the migration plan are carried word for word.
>
> The check also notes that the first `then` line of 528.3 shares words with 528.1 and 528.2. The three sub-cases hold different promises. 528.3 is the order of the blocks of the first turn. 528.1 is the git lines and the absence of a remote. 528.2 is the archive of the rule and the place of the tail.
> No hook changes, and no reader in code refuses anything between the edit and the render. The Case creates no page, so no vault query was run. The readings of the two `/hi` Estimates of this Case wait for a session after the render. The reading of the leftovers Estimate waits for the close (case 428.1).
> Not done: a remote for backup, the deletion of the migration plan, and the merge of `migration` into `main`.

> **problem:**
> `/hi` runs two commands against a remote that is not this project, and both fail at every session start. The note that keeps them off the Frontier goes away with the sprint. After the merge, `main` would pull from the product repository. The promise on the raw date folders asks that folders git does not track be gone, but `rule-raw-archive` keeps their logs on purpose.

### Case 528.1 — `/hi` runs no `git pull`, and the repository has no remote

> **given:**
> `rule-git-context` — the rule of the git lines of `/hi`
> **＋** `estimate-git-context-current` — its promise, whose Criterion is replaced whole
> **＋** `.claude/skills/hi/SKILL.md` — the skill file the rule renders into
> **＋** `.git/config` — the remote `origin` and the upstream of `main`

> **when:**
> The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the commands of `rule-git-context`.

> **then:**
> The context holds `Render:` with the output of `uv run guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
> **＋** `git remote` prints no remote: `.git/config` holds no `origin`, and `main` has no upstream.
> **－** The skill runs no `git pull`, and the context holds no `Pull:` line.

```then
update:
- slug: rule-git-context
  set:
    purpose: Prevents a session from starting on a branch it does not know
  sections:
    Purpose: |-
      Prevents a session from starting on a branch it does not know.

      **Branch tells us what kind of start this is.** On `main` or a working branch, no plan is
      open. On a plan branch, unfinished work exists and becomes the first Frontier item. This is
      never restated in `brief.md` — git already knows, and a second source of truth eventually
      disagrees with the first.
    Render: |-
      <!-- rule-git-context -->
      Render: !`uv run guppi render --sync`
      Branch: !`git branch --show-current`
      Status: !`git status --short`
      <!-- /rule-git-context -->
    How it works: 'The `Render:` line runs `uv run guppi render --sync` once more inside `/hi`, after the `SessionStart` hook has run it; a diff on that line is a Frontier item like the one of the session start (case 115). The repository has no remote since case 528: `origin` was the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start. `/hi` runs no `git pull`; a Case that adds a remote writes its pull line and its rule again.'
  change: 'taken up: the pull leaves /hi with the remote; the rule keeps the render, the branch and the status; the defers of cases 220 and 243 retired (case 528.1)'
- slug: estimate-git-context-current
  set:
    status: pending
    purpose: At /hi the context holds the render sync, the branch and the status, and the skill runs no git pull
    method: by hand at the /hi of a session after the render, the first turn's context and the output of git remote, written into the estimate line
  change: the Criterion replaced whole — no Pull line, no git pull, no remote; the promise on a pull mid-session gone with the pull (case 528.1)
```

```tasks
- [x] update `rule-git-context`
- [x] update `estimate-git-context-current`
- [x] by hand: `git remote remove origin`, then `git remote` prints nothing
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-git-context-current` — by hand at the /hi of a session after the render
```

### Case 528.2 — `rule-github-issues` leaves the harness

> **given:**
> `rule-github-issues` — the rule of the `Open issues:` line of `/hi`, deleted
> **＋** `estimate-github-issues-listed` — its promise, deleted with it
> **＋** `rule-cleanup` — moves a deleted page to the archive and takes its slug out of `children` and `estimates`
> **＋** `vault/archive/` — where `cleanup` puts the deleted pages
> **＋** `entity-glossary` — the table whose row Issue points at the rule
> **＋** `vault/wiki/glossary.md` — the render of that table
> **＋** `rule-ledger-tail` — its How it works places the `Tail:` line after the rule
> **＋** `rule-git-context` — the block that the `Tail:` line follows after the change

> **when:**
> `uv run guppi cleanup` runs at the librarian's run after the Case is applied, and then `uv run guppi glossary` runs.

> **then:**
> `rule-github-issues` and `estimate-github-issues-listed` stand under `vault/archive/`, and no live page lists them in `children` or `estimates`.
> **＋** The table of `entity-glossary` and `vault/wiki/glossary.md` hold no row Issue.
> **＋** `rule-ledger-tail` places the `Tail:` line after `rule-git-context`.
> **－** The other rows of the table of `entity-glossary` do not change.

```then
update:
- slug: entity-glossary
  replace:
  - old: '| Issue | Tracked on GitHub; never a page, a `ref` only | [[rule-github-issues]] | | Work Mode |'
    new: '| Work Mode |'
  change: 'the row Issue removed: rule-github-issues left the harness with the remote (case 528.2)'
- slug: rule-ledger-tail
  replace:
  - old: after `rule-github-issues`;
    new: after `rule-git-context`;
  change: 'the Tail line follows the git lines: rule-github-issues left the harness (case 528.2)'
delete:
- slug: rule-github-issues
  impact: The Open issues line leaves /hi with the remote; cleanup moves the page to the archive and takes it out of the children of rule-skill-hi; the defers of cases 220 and 243 retired (case 528.2)
- slug: estimate-github-issues-listed
  impact: Its rule is gone; no gh command runs at /hi to read (case 528.2)
```

```tasks
- [x] delete `rule-github-issues`
- [x] delete `estimate-github-issues-listed`
- [x] update `entity-glossary`
- [x] update `rule-ledger-tail`
- [x] `uv run guppi glossary`
```

### Case 528.3 — The frame of `/hi` holds no pull and no issues

> **given:**
> `rule-skill-hi` — the rule that renders the frame of `/hi`, its `description` and its `allowed-tools`
> **＋** `estimate-hi-no-read-calls` — its promise on the blocks of the first turn, whose Criterion is replaced whole
> **＋** `rule-session-start` — the parent that explains the Leaves of `/hi` and the sources of the Frontier
> **＋** `.claude/skills/hi/SKILL.md` — the skill file
> **＋** `rule-internal-context` — the block of the loaded files
> **＋** `rule-git-context` — the block of the git lines
> **＋** `rule-ledger-tail` — the block of the tail

> **when:**
> The person invokes `/hi`, and Claude Code expands `.claude/skills/hi/SKILL.md` before the agent's first turn.

> **then:**
> The context of the first turn holds the output of each block of the skill, in the order of the children of `rule-skill-hi`: the text of the files `rule-internal-context` loads, the lines `Render:`, `Branch:` and `Status:` of `rule-git-context`, and the line `Tail:` of `rule-ledger-tail`.
> **＋** The `allowed-tools` of the skill names `uv run guppi render --sync`, `git branch --show-current`, `git status --short` and `uv run guppi tail`, and neither `git pull` nor `gh`.
> **－** The agent makes no read-tool call to get any of them.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: 'description: Open a working session — sprint, brief, git state, open issues, then the Frontier.'
    new: 'description: Open a working session — sprint, brief, git state, then the Frontier.'
  - old: 'allowed-tools: Bash(git pull --ff-only:*), Bash(uv run guppi render --sync), Bash(git branch --show-current), Bash(git status --short), Bash(gh issue list:*), Bash(uv run guppi tail)'
    new: 'allowed-tools: Bash(uv run guppi render --sync), Bash(git branch --show-current), Bash(git status --short), Bash(uv run guppi tail)'
  - old: <!-- rule-git-context --> <!-- rule-github-issues -->
    new: <!-- rule-git-context -->
  - old: the four children splice into the markers below
    new: the three children splice into the markers below
  - old: '`allowed-tools` names the six `!` commands of the skill'
    new: '`allowed-tools` names the four `!` commands of the skill'
  change: 'the frame without the pull and the issues: description, allowed-tools and the marker of rule-github-issues (case 528.3)'
- slug: estimate-hi-no-read-calls
  set:
    status: pending
  change: the Criterion replaced whole — no Pull and no Open issues line; allowed-tools names neither git pull nor gh (case 528.3)
- slug: rule-session-start
  replace:
  - old: '`git pull` and `gh issue list` fail differently, on merge conflicts versus authentication, so they are separate.'
    new: The git commands fail apart from the imports, so they are a Leaf of their own.
  - old: '`brief.md` + `sprint.md` + open issues, plus'
    new: '`brief.md` + `sprint.md` + the git state and the tail, plus'
  change: 'no pull and no issues at /hi: the git Leaf and the sources of the Frontier (case 528.3)'
```

```tasks
- [x] update `rule-skill-hi`
- [x] update `estimate-hi-no-read-calls`
- [x] update `rule-session-start`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-no-read-calls` — by hand at the /hi of a session after the render
```

### Case 528.5 — The leftovers promise reads what git tracks and names the remote decision

> **given:**
> `estimate-sprint-migration-leftovers-gone` — the promise, whose Criterion is replaced whole
> **＋** `entity-sprint-migration` — the sprint page, its Slice 5 items and its Closed note; `vault/wiki/sprint.md` renders it
> **＋** `rule-raw-archive` — keeps `event_log.md` in `vault/raw/<date>/`
> **＋** `vault/parked/` — the parked pages, deleted by case 510
> **＋** `docs/` — the documents of 2026-08, the rule documents of `docs/migration/`, and `docs/migration/migration-plan.md`
> **＋** `vault/archive/` — the archive and its roots
> **＋** `vault/raw/` — the date folders `vault/raw/<date>/` and their session folders `vault/raw/<date>/<HHMM>/`
> **＋** `.claude/skills/hi/SKILL.md` — the skill file that ran `git pull` and `gh`

> **when:**
> Someone reads the tree of the repository at the close of the sprint.

> **then:**
> `vault/parked/` is absent: its pages were deleted by a decision named in the reading, and git history keeps them.
> **＋** Under `docs/` no 2026-08 document remains, and no rule document of `docs/migration/`; each became a page, was archived, or was deleted by a decision named in the reading.
> **＋** `vault/archive/` has no root outside the folders of its sprints, and the decision that deleted the old root is named in the reading.
> **＋** Every file under `vault/raw/` that git tracks lies in a session folder `vault/raw/<date>/<HHMM>/`.
> **＋** The repository has no remote, and `.claude/skills/hi/SKILL.md` runs neither `git pull` nor `gh`; the decision is named in the reading.
> **－** `docs/migration/migration-plan.md` is outside this promise: the Case that closes the sprint deletes it.
> **－** The `event_log.md` of a past date stays in `vault/raw/<date>/`, as `rule-raw-archive` keeps it, and does not fail this promise.

```then
update:
- slug: estimate-sprint-migration-leftovers-gone
  set:
    status: pending
    purpose: vault/parked/, the 2026-08 documents and the old archive root are gone, git tracks no raw date folder without a session, and the repository has no remote, each by a decision named at the close of the sprint
  change: the Criterion replaced whole — the raw date folders read by what git tracks, the remote removed and git pull and gh out of /hi, the old archive root deleted by case 102.1 (case 528.5)
- slug: entity-sprint-migration
  replace:
  - old: '`vault/parked/` and the documents of 2026-08 under `docs/` deleted (case 510); the old archive root, the empty raw date folders, `git pull` and `gh`, and the reading, at the close'
    new: '`vault/parked/` and the documents of 2026-08 under `docs/` deleted (case 510), the old archive root (case 102.1); the raw date folders read by what git tracks, the remote and `git pull` and `gh` out of `/hi` (case 528); the reading at the close'
  - old: '`make test` green, `migration` merged into `main`; at the close [[rule-git-context]] and [[rule-github-issues]] — the upstream of the branch and the GitHub remote, decisions 11.1, 11.2, defers 220, 243 — read by [[estimate-sprint-migration-leftovers-gone]]'
    new: '`make test` green, `migration` merged into `main`'
  - old: 'Kept without a page: `git pull` in `/hi` without an upstream (decision 11.1); `gh` not logged in, no GitHub remote (11.2) — both decided again at the close (`estimate-sprint-migration-leftovers-gone`).'
    new: '`git pull` and `gh` left `/hi` with the remote of the product repository, kept since decisions 11.1 and 11.2 (case 528).'
  change: 'Slice 5: the raw date folders, git pull and gh decided; the remote removed; the merge item no longer names the two rules (case 528.5)'
```

```tasks
- [x] update `estimate-sprint-migration-leftovers-gone`
- [x] update `entity-sprint-migration`
- [x] `uv run guppi sprint`
- [ ] read `estimate-sprint-migration-leftovers-gone` — by hand on the tree at the close of the sprint
```

## Case 529 — `insight-materialize-estimate-update-lifts-the-criterion-whole` is rejected as fixed, and its pattern names the cause in the past tense

> **context:**
> An Insight page groups lessons that share one cause. It stays `open` in `vault/wiki/backlog.md` until a decision fixes the cause or rejects the page (`rule-insights-schema`). The pattern of `insight-materialize-estimate-update-lifts-the-criterion-whole` says that `lift_criterion` in `guppi/materialize.py` lifts the when and then of a Case into every update of an Estimate and sets the page pending, even when the update changes only one field or one word. That was true in September. Case 296 added `names_a_part`, and case 378.4 made it the rule of the schema. Now an update that names one part of an Estimate changes that part alone, and a `replace` pair inside the Criterion is `incomplete: [criterion]`. So the pattern describes behaviour the code no longer has. The handoff of session 1753 and the brief flag this.
> Case 302.1 set the page `actioned`. The lesson `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` of session 2229 reopened it, because no decision of that session closed its cause (case 284.4). That lesson found that `estimate-generate-writes` and `estimate-generate-walks-dates` held the text of case 211.3 in place of their promises. Cases 489.1 and 489.2 have restored both Criteria. The lesson also says that nothing compares a Criterion with the name and purpose of its page. That is a check on any mismatch between a promise and its page, not this mechanism. Case 302.1 already declined the similar check the page's Proposal suggests.
> In two rounds the person accepted each recommendation, both times with the words "I agree". The page is set `actioned` with this decision in `addressed_by`. The pattern field and the `## Pattern` section get one new text that names the cause in the past tense, and the `## Proposal` section stays as it is.
> What `case-guppi` found in the frame: `rule-insights-schema` requires `addressed_by` on an `actioned` page and holds only the latest decision there. The cascade of `generate` archives the `clustered` children of an `actioned` Insight, so the lesson of session 2229 is archived at the librarian's run. `vault/wiki/backlog.md` lists open Insights only, so the page leaves it at the next `uv run guppi backlog`. Neither Insight nor Lesson pages have Estimates. The one Estimate of `rule-insights-schema`, `estimate-insights-schema-checked`, speaks of the shape of the page, and this Case keeps that shape. No code, hook or reader changes. The Case creates no page, so no vault query was run.
> Not done: a check that compares the Criterion of an Estimate with the name and purpose of its page.

> **problem:**
> An open Insight describes as current a mechanism the code has not had since case 378.4. The index line that the vault search reads says something false, and the page keeps a closed cause in the backlog.

> **given:**
> `insight-materialize-estimate-update-lifts-the-criterion-whole` — the Insight, its status, `addressed_by` and pattern
> **＋** `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` — its `clustered` child of session 2229
> **＋** `rule-insights-schema` — requires `addressed_by` on `actioned` and makes the Insight a mark for a recurrence
> **＋** `vault/wiki/backlog.md` — lists the open Insights

> **when:**
> The librarian's run applies the Case with `uv run guppi generate`, runs `uv run guppi backlog`, and someone reads `insight-materialize-estimate-update-lifts-the-criterion-whole`.

> **then:**
> `insight-materialize-estimate-update-lifts-the-criterion-whole` stands `actioned`, with this decision in `addressed_by`.
> **＋** Its `pattern` field and its `## Pattern` section hold one text, which names in the past tense how an update of one part of an Estimate replaced its whole Criterion.
> **＋** `lesson-generate-replaced-a-ratified-criterion-on-a-field-update` stands `archived`, and it stays in the `children` of the Insight.
> **＋** `vault/wiki/backlog.md` does not list the Insight.
> **－** The `## Proposal` section of `insight-materialize-estimate-update-lifts-the-criterion-whole` does not change.

```then
update:
- slug: insight-materialize-estimate-update-lifts-the-criterion-whole
  set:
    status: actioned
    addressed_by: decision-case-529
    pattern: An update of an Estimate that named one part of the page — a field or a word — replaced the whole Criterion with the when and then of its Case and set the page pending, so the promise the person signed was lost and nothing read the new text against the old before the librarian's run.
  sections:
    Pattern: An update of an Estimate that named one part of the page — a field or a word — replaced the whole Criterion with the when and then of its Case and set the page pending, so the promise the person signed was lost and nothing read the new text against the old before the librarian's run.
  change: 'rejected as fixed: an update that names a part changes that part alone since case 378.4; the pattern names the cause in the past tense; the check of a Criterion against its page''s purpose not taken (case 529)'
```

```tasks
- [x] update `insight-materialize-estimate-update-lifts-the-criterion-whole`
```

## Case 530 — The librarian's reads match what its brief needs, and a refused write is not worked around

> **context:**
> The librarian is the agent that runs after a session and turns its ratified decisions into vault pages. Its frame, the Render of `rule-documentation` in `.claude/agents/librarian-guppi.md`, lists the only things it may read. The brief section that `rule-brief` splices into the same frame asks for facts that no allowed read gives: the Spec lines `generate` ticked, what `cleanup` moved, and, for an Estimate read on the librarian's run, the facts "as the steps of this run before the brief printed or left them" (case 508.4). So every run reads beyond the list, and `estimate-documentation-completes` stays failed. The run of ff62585 read the tail of `log.md`, the head of the old `brief.md`, git diffs and a grep of `sprint.md`. The run of 1c196e8 (lines 2076–2119 of `raw/2026-09-29/event_log.md`) ran `git diff` on Spec, yaml and rule files, grepped the status of three Decision pages, and ran `git status` over `vault/archive`. A `bashguard` refusal (line 2115) stopped it from writing `brief.md` with a heredoc. It then wrote the brief into the scratchpad and copied it into place with `cp`, although it could have written the file with `Write`. The refusal text itself led it there: "Write the script with the Write tool into the scratchpad and run it by path; change a file with Edit" names no tool for writing a whole file. The same run also skipped `uv run guppi archive`. That is left to its own item in a later session, since the frame already demands the step. The main agent records the failed reading of 1c196e8 before the decision lines of this Case, because the ledger hook refuses a reading of an Estimate that a decision line of this session updates (case 428.1). `rule-documentation` stands `draft` with `deferred_by` `[[decision-case-525]]`, which put the item off after case 517. This Case takes it up and retires that defer. Both targets are `update`s with a `ref`, so no vault query was run. In the frame: `log.md` has 4829 lines. `generate` and `cleanup` add a dated line to it for each page they change or move, so its `git diff` before the commit holds only this run's lines. `rule-brief` says "nothing from the previous brief (case 168)", and that stands, because the old brief is read and no fact of it is carried. The opening sentence of the frame, "you write only through the scripts named below", is already qualified by the brief section, which gives the brief to the librarian; it stands. `bashguard` is the only hook on `PreToolUse` of `Bash`. Only an agent reads its refusal text, so the new text needs no old form beside it. The Estimates touched are the two whose Criterion speaks of the change: `estimate-documentation-completes`, which lists the librarian's reads, and `estimate-bash-guard`, which quotes the refusal text. Both Criteria are replaced whole. The bulleted read list of the first becomes one line of allowed reads, and the refusal sentence of the second takes the new text.

> **problem:**
> The librarian's list of allowed reads contradicts the brief section of its own frame, so every run breaks the list and `estimate-documentation-completes` cannot pass. When a hook refuses a write, the refusal text points to the scratchpad and not to `Write`, so the librarian worked around the refusal with `cp` instead of writing the file with the tool the hooks check.

### Case 530.1 — The librarian reads what this run changed, and writes the brief with Write

> **given:**
> `rule-documentation` — the librarian's frame, the Render of `.claude/agents/librarian-guppi.md`
> **＋** `estimate-documentation-completes` — the promise of the librarian's run
> **＋** `rule-brief` — the brief section spliced into the frame; it takes nothing from the previous brief
> **＋** `rule-index-check` — the index check, whose Greps give index lines
> **＋** `rule-synthesis` — the synthesis, whose Greps give index lines
> **＋** `vault/wiki/brief.md` — the brief the librarian rewrites
> **＋** `vault/wiki/log.md` — the log that `generate` and `cleanup` append a dated line to
> **＋** `vault/archive/` — the archive the librarian never searches
> **＋** `vault/archive/**/<slug>.md` — the one Glob allowed over the archive
> **＋** `vault/wiki/decisions/` — the Decision pages the librarian never reads
> **＋** `vault/raw/<date>/<hi HHMM>/spec.md` — the Specs whose unticked lines the librarian reads
> **＋** `guppi/` — the scripts' code, which the librarian may read
> **＋** `tests/` — the scripts' tests, which the librarian may read

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

> **then:**
> `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
> **＋** The librarian read only its inputs — `handoff.md`, the yamls that `guppi materialize` named, the index lines and `tags.md` — and these reads that its frame allows: a file where the harness saved the output of one of its own commands because the output was too long to show; the wiki pages it names in the report, each with the outcome and one of the reasons of its frame; a page under `vault/archive/` found by the Glob `vault/archive/**/<slug>.md` for a slug that a script named in an error, named in the report with the error; the unticked `- [ ]` lines of the `spec.md` files, and the lines this run ticked as its `git diff` shows them; of the ledger, only the count of its lines and the lines the yaml does not account for, named in the report; the output of `git status` and `git diff` on the files the scripts of this run wrote, never over `vault/wiki/decisions/` or `vault/archive/`; `vault/wiki/log.md` only through its `git diff` before the commit; and the old `vault/wiki/brief.md`.
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
> **＋** It wrote `vault/wiki/brief.md` with the `Write` tool. The new brief holds no fact taken from the old brief, and the librarian put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc.
> **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
> **－** It read no other part of a Spec, no plan, no Decision page, no `materialize.yaml` that `guppi materialize` did not name, and no line of `vault/wiki/log.md` outside its `git diff`. The `Makefile`, `guppi/` and `tests/` are the scripts' own files and may be read.
> **－** A hook's refusal of one of its calls is not worked around by another route: the librarian names the refusal in the report and goes on as the refusal says.
> **－** The librarian refuses an instruction of the handoff to repair a yaml entry, to read the ledger beyond the one read above, a Spec beyond its `- [ ]` lines or a Decision page, to search the archive, or to open an archived page that no script named in an error. It names what was asked and why in the report, and the refusal does not stop the run.
> **－** The librarian never searches `vault/archive/`: no Grep, `grep`, `find`, `ls` or `git status` runs over it, and no Glob other than `vault/archive/**/<slug>.md` for a slug a script named in an error.

```then
update:
- slug: rule-documentation
  replace:
  - old: 'When the harness saves the output of one of your commands to a file because the output is too long to show, read that file: it is the output of your command (case 474.1).'
    new: 'When the harness saves the output of one of your commands to a file because the output is too long to show, read that file: it is the output of your command (case 474.1). For the facts the brief takes from what this run left on disk, run `git status` and `git diff` on the files the scripts of this run wrote, never over `vault/wiki/decisions/` or `vault/archive/`. Read `vault/wiki/log.md` only through `git diff -- vault/wiki/log.md`, which before the commit shows only the lines this run added; never `Read`, `tail`, `head` or `grep` it. You may read the old `vault/wiki/brief.md` before you rewrite it; the new brief takes no fact from it. Write `vault/wiki/brief.md` with the `Write` tool, and put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc. A hook that refuses one of your calls is not worked around by another route: name the refusal in the report and go on as the refusal says (case 530.1).'
  - old: nor read `spec.md` beyond its unticked `- [ ]` lines — the ones Readings due and Next session take (cases 200.3, 268.1, 271)
    new: nor read `spec.md` beyond its unticked `- [ ]` lines — the ones Readings due and Next session take — and the lines this run ticked, as its `git diff` shows them (cases 200.3, 268.1, 271, 530.1)
  change: the librarian reads git status and git diff of what this run wrote, log.md only through its diff, and the old brief; it writes the brief with Write and never works around a refusal (case 530.1)
- slug: estimate-documentation-completes
  set:
    status: pending
  change: the Criterion replaced whole — the reads of what this run changed, log.md through its diff, the old brief read, the brief written with Write, no refusal worked around (case 530.1)
```

```tasks
- [x] update `rule-documentation` — the frame allows the reads of what this run changed, names `Write` for the brief, and forbids working around a refusal
- [x] update `estimate-documentation-completes` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-documentation-completes` — `make test-documentation`, then by hand on the librarian's run of a later session, from its transcript and `event_log.md`
```

### Case 530.2 — The bash guard's refusal sends a whole file to Write

> **given:**
> `rule-bash-guard` — the hook on `PreToolUse` of `Bash` that refuses a heredoc
> **＋** `guppi/bashguard.py` — the hook's code, which prints the refusal
> **＋** `tests/test_bashguard.py` — the tests of the refusal and its text
> **＋** `estimate-bash-guard` — the promise of the hook
> **＋** `.claude/settings.json` — the registration; no other hook on `PreToolUse` of `Bash`
> **＋** `raw/<date>/event_log.md` — the log that takes the line of each refusal
> **＋** `/dev/null` — the one redirect target a heredoc may write to

> **when:**
> The agent calls `Bash`, and `uv run guppi bashguard` on `PreToolUse` reads `tool_input.command` of the payload and finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line.

> **then:**
> A body with a backslash, or a marker line that writes a file (`>` or `>>` not to `/dev/null`, `tee`), exits 2 with the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path>>. Write a whole file with the Write tool and change a file with Edit, never through Bash; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
> **＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard refused: <reason>` goes to `raw/<date>/event_log.md`.
> **＋** A `<<<` here-string, a heredoc with no backslash and no file write, a command without a heredoc, another tool — exit 0.
> **＋** A payload the hook cannot read — exit 0 with one line on stderr.
> **－** The hook never raises.

```then
update:
- slug: rule-bash-guard
  replace:
  - old: Write the script with the Write tool into the scratchpad and run it by path; change a file with Edit.
    new: Write a whole file with the Write tool and change a file with Edit, never through Bash; only a script goes into the scratchpad, written with the Write tool and run by path.
  change: the refusal text sends a whole file to Write and only a script to the scratchpad (case 530.2)
- slug: estimate-bash-guard
  set:
    status: pending
  change: the Criterion replaced whole — the refusal text sends a whole file to Write and only a script to the scratchpad (case 530.2)
```

```tasks
- [x] update `rule-bash-guard` — the refusal text sends a whole file to Write
- [x] update `estimate-bash-guard` — the Criterion replaced whole
- [x] `guppi/bashguard.py` — the refusal text and the module docstring carry the new sentence
- [x] `tests/test_bashguard.py` — the refusal tests assert the new sentence whole
- [ ] read `estimate-bash-guard` — `uv run pytest tests/test_bashguard.py`, then the first refusal of a later session, its message read on stderr
```

## Case 531 — Retro runs on to the librarian with no stop, and the person keeps "where to stop"

> **context:**
> Today `/work` runs the Spec and then calls `/retro`. Retro shows the person a report and waits. The report opens with a numbered list of points that need an end. It closes with three parts: Ratified, What got done, and What is not done. The person approves or changes the end of each point. Only then does the agent commit and call `/handoff`, which writes `handoff.md` and dispatches the librarian. The check on that report, `estimate-retro-report-holds-each-fact-once`, has failed at three Retros in a row. Those failures are recorded at ledger lines 2026-09-27/1819 L39, 2026-09-28/1318 L39 and 2026-09-29/1753 L29. The last failure had two causes.
> - The report form asks What got done to name "the commit", but the rule commits only after the approval. The report of session 1753 wrote "commit — after your approval" (translated from Russian), and both commits of that session, dd08a1b and 3520653, came after it. This is a gap in the rule text, not a slip by the agent.
> - Frontier points 1 and 8 named the readings L4, W12 and W15, and What got done listed them again as L4, L23 and L24. The rule's general words ("only what no other part holds") forbid that, but its narrower exception invites it.
>
> The person decided in six rounds. Their words, translated from Russian, were "I agree with the recommendations", "I agree" and "Well, okay, let's try this scheme":
> - What got done names no commit.
> - This Case takes up the redesign of the report that cases 505 and 509 put off.
> - Retro becomes a report of the agent for the agent. From the approved Spec to the librarian the run needs no person, and it stops only where the person is needed.
> - The person keeps three questions: what to do (the Cases), what done means (the Estimates), and where to stop (a new page).
> - `/retro` keeps its name and calls `/handoff` with no stop. The report goes straight into `handoff.md`, which gets one section for each kind of fact and carries no numbers and no ends.
> - The agent commits on green. A red test it cannot fix is saved as a patch and reverted, with a lesson and a line in the handoff note, not a defer. Retro writes no defer.
> - The stops are a fork that changes a contract, a hook refusal the agent cannot follow, an action git cannot undo, and a task that the Spec marks with `stop:`.
> - At pre-spec the person added a fifth stop: `/work` on the branch `main`, which the Render of `rule-work-mode` and `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` already stop on. Their words, translated from Russian: "OK, I agree. We can fix it later if needed."
> - A reading that only the person can take becomes a handoff line marked `needs the person`, with its question. The brief carries it in its own list. `/hi` asks it, and the answer becomes the reading line. Today such a line sat as a plain Work line in all four Frontiers of 2026-09-29 (1134 W53, 1432 W30, 1753 W25, 2024 W23), and nobody asked the person.
> - The mechanism has no counter and no judgment of "progress". The agent runs the tasks, the Work readings and Retro in one turn, using tool calls. It ends that turn with one reply that carries every reading and lesson in a `LEDGER` block. One new `Stop` hook works from the state of files alone. After that reply it sends the agent on to `/handoff`, unless `handoff.md` already stands, the reply follows its own refusal, or the reply opens with `STOP:`.
> - The six checks whose trigger is "the person invokes" `/retro` or `/handoff` are replaced, so that each one covers the agent's call as well. They are `estimate-retro-report-holds-each-fact-once`, `estimate-retro-loads`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-retro-red-in-the-baseline-is-not-charged`, `estimate-handoff-holds-each-fact-once` and `estimate-handoff-dispatches` (531.1–531.6).
>
> What `case-guppi` found in the frame:
> - The ledger hook writes a reply's lines when the reply ends. It writes nothing when `stop_hook_active` is set (`guppi/ledger.py`). The reply that ends Retro is the first end of a reply in its turn, so the flag is false there. The ledger hook therefore needs no change: the round-4 answer on it was given for a mechanism that the person replaced. Only the reply after the new hook's refusal carries the flag, and no ledger line may stand in it. 531.1 and 531.6 say so.
> - The new hook watches for the `retro` mark that `guppi gate` writes at the call of `/retro`, not for "a reply that carried the Retro block". A Retro with no line to write carries no block. With the mark, the window runs from `/retro` until `handoff.md` stands, and a deliberate stop anywhere in that window opens with `STOP:`.
> - `rule-where-to-stop` has no parent. `estimate-session-phases-in-order` promises that `rule-session` has five phases as its children, and a Leaf under `rule-work-mode` is not possible. A partial render goes only into a file whose rendering MOC holds its marker, and `rule-work-mode` is a Leaf. So the page renders its own file, `vault/wiki/where-to-stop.md`, and `/work` imports it with `@`, as `/hi` imports its files. Whether an `@` import expands when the agent calls a skill has not been measured; the reading of 531.7 checks it.
> - Case 528.4 of this session already replaced the Criterion of `estimate-hi-writes-frontier`. To avoid a second whole replacement, 531.11 supersedes 528.4 and carries its pair on `rule-skill-hi` and its Criterion, with the `## Ask` list added. 528.4 leaves the Spec. Frontier line C1 stays closed by the other sub-cases of 528.
> - The Render of `rule-skill-hi` opens "Assemble the Frontier from the above in two lists". The glossary row "`/hi`, Frontier" names issues and two lists. 531.11 changes both, so the row keeps saying what its `where` page says, as 527.2 promises. Its pair anchors on the row's own text. 527.1 and 528.2 change other rows: Harness, Retro and Issue.
> - Case 527.1 of this session rewrites the words "under `## Retro` in the Spec" in the Retro row of `entity-glossary`. The two pairs of 531.1 anchor on the text before and after those words, so they match the row both before and after 527.1 is applied.
> - `rule-prespec` and its check count an open line under `## Cases` as a finding and one under `## Work` as not. An open `## Ask` line is no finding either, so 531.12 changes the code, the skill text and the check.
> - The case-schema sentence on short defers names Retro twice, and `estimate-case-protocol-defers-in-one-reply` names "at Retro". 531.14 changes both.
> - `guppi gate` refuses the agent's `/retro` with "nothing to review" and the advice "then call /retro in the next reply". That asks for a reply to end outside the list of stops, which 531.8 forbids. 531.15 makes the agent's advice say that the refusal is a stop, and the second condition of the stops page counts a hook refusal that says so.
>
> Lines of old Criteria that are not carried, on purpose:
> - "The person invokes `/retro`", "The person invokes `/handoff`" and the old trigger of `/hi` become triggers that name both paths, or the new `## Ask` list.
> - The frontier, its items, its ends and its two count lines go with the report. The old promise of the report also goes: one numbered list, three parts in the close, the close in the same reply as the frontier, and "each fact once". That last promise moves to `estimate-handoff-holds-each-fact-once`.
> - A red that was "ended as a note for the handoff" becomes a line of `## Observations`, and a reverted test becomes a line of `## Debt`.
> - The handoff check's "three parts of the close" and "three section names" become the seven sections, of which the three old names stay.
> - The line "The person can stop the step in the chat" goes: the run is one turn, and a stop follows `vault/wiki/where-to-stop.md`.
> - The reading lines of `/work` were "carried by a later reply ending in text". They now stand in the reply that ends Retro.
> - The brief's two lists become three, and "an item in either `Cases` or `Work`" becomes "an item in one list only".
> - "`Pull:` and `Open issues:` are a Cases item …" goes with the two commands, as 528.4 decided.
> - A defer "in Plan Mode or at Retro" becomes one in Plan Mode. With it go "At Retro no Frontier is shown" and the writing into `spec.md`.
> - In `estimate-retro-commit-gates`, only the end of the "nothing to review" line on the `Skill` path changes; it now names a stop. The mark line is carried whole, with the path of the event log named.
>
> The check also notes lines that share words across sub-cases. They describe one run seen from several promises, each of which can fail apart from the others:
> - Retro as a whole (531.1), its readings (531.2), an expected red (531.3) and a red of the Baseline (531.4);
> - the file `handoff.md` (531.5) and the brief that reads it (531.10);
> - the Frontier's lists (531.11), pre-spec's findings on them (531.12) and the readings at `/hi` (531.13);
> - the gate's marks and refusals (531.15), next to the new hook (531.9) and the event log of `/handoff` (531.6).
>
> These texts stand as they are, and why:
> - `rule-spec-write` and `rule-spec-capture` describe how the `Stop` hook writes a short Case into `spec.md` at Retro. The code keeps that path. No reader refuses anything when it goes unused, and a later Case can remove it.
> - `estimate-case-protocol-ledger-line-form` names "a lesson line the moment the lesson exists" in its trigger. Its promise is the shape of the line, which does not change, and in Plan Mode a lesson is still written at once.
> - `estimate-end-of-work-order`: the order stays true. The commit comes before `/handoff`, and `handoff.md` comes before the librarian. `rule-retro-onward` is added after `rule-carry-over` among the children, and `rule-carry-over` still follows `rule-handoff`.
> - `estimate-glossary-terms-defined` (replaced by 527.2 today) judges every row against its `where` page. The rows that 531.1 and 531.11 change say only what their pages say after this Case.
> - `estimate-hook-registry-rendered` promises only that the file equals the render.
> - The glossary rows Work Mode and Handoff stay true.
> - The Stop hooks that fire on the same event keep their rules: `guppi ratified` and `guppi casecheck` do nothing on the re-fire, and `guppi context` only prints the size.
> - The gate's other refusal on the agent's path — "…end this reply in text with the LEDGER block, then call /<skill> in the next reply" — stays, and so do `rule-ledger-write` and `estimate-ledger-write-lifts`, which quote it. It fires only when a Case of the Spec has no decision line. `/pre-spec` and the hook on `ExitPlanMode` already refuse that before Work Mode starts, so it does not arise in the run.
>
> The vault query found no page on when the agent stops. `rule-orchestration` (draft, put off by case 424) covers how the main agent triages and dispatches, not stops. The new slugs are free: `rule-where-to-stop`, `rule-retro-onward`, `estimate-where-to-stop-stops-only-on-its-conditions`, `estimate-retro-onward-sends-the-agent-to-the-handoff`, `estimate-retro-runs-on-to-the-handoff`. The fitting tags already exist: `session`, `workflow`, `harness`, `hooks`, `render`.
>
> Timing: `.claude/settings.json` and the skills are rendered at the librarian's run. The new hook therefore fires only from the first session after that run, and in the build session `/retro` still runs by its old text. `guppi/prespec.py` and `guppi/gate.py` run from the working tree at once. Accepting an open `## Ask` line refuses nothing, and the gate changes only the words of a refusal that already stands.
>
> Not done: hooks on single actions that cannot be undone, such as `PreToolUse` on `git push`; removing the Retro path of the short-defer writer; a test that the agent follows the text of `vault/wiki/where-to-stop.md`, beyond a reading by hand.

> **problem:**
> The Retro report holds the person up for an approval they give almost every time. It asks for a commit that does not exist yet, and it lists the same facts in two parts. The run from the approved Spec to the librarian has no written rule for when the agent must stop and ask. A reading that only the person can take has no way to reach the person.

### Case 531.1 — Retro reviews, writes its lines, commits and calls `/handoff` with no stop

> **given:**
> `rule-retro` — the page whose Render is the `/retro` skill; it carries the defers of cases 505 and 509
> **＋** `.claude/skills/retro/SKILL.md` — the skill file rendered from `rule-retro`
> **＋** `estimate-retro-report-holds-each-fact-once` — the promise of the Retro report, renamed and replaced whole
> **＋** `rule-end-of-work` — the MOC whose Purpose names the steps of the end of a session
> **＋** `entity-glossary` — the table with the row Retro; `vault/wiki/glossary.md` renders it
> **＋** `rule-where-to-stop` — the conditions on which the run stops, in `vault/wiki/where-to-stop.md`
> **＋** `rule-handoff` — `/handoff`, which writes `raw/<date>/<hi HHMM>/handoff.md`
> **＋** `raw/<date>/<hi HHMM>/work.md` — the Baseline and the Expected red of the session
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec whose boxes Retro sorts

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/spec.md` holds the tasks of the run.

> **then:**
> Retro shows the person no report and asks for no approval: it sorts the boxes of `raw/<date>/<hi HHMM>/spec.md`, reads `raw/<date>/<hi HHMM>/work.md`, takes the readings whose moment has come, and decides which lessons to write.
> **＋** A red test that the agent cannot fix within the ratified work is saved as a patch in the session folder and reverted, with a `lesson[error]` line and a line in `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` that names the patch.
> **＋** The agent commits the work when `make style` is clean and `make test` is green, except for the tests that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` holds.
> **＋** One reply ends Retro: it carries one `LEDGER` block with every reading and lesson of `/work` and Retro, and asks the person nothing.
> **＋** After that reply, in the same turn, the agent commits the session folder and calls `/handoff`.
> **－** Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** Retro stops for the person only on a condition of `vault/wiki/where-to-stop.md`.
> **－** A reading that only the person can take is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question.

```then
update:
- slug: rule-retro
  set:
    purpose: Prevents a session from reaching the librarian on work nobody reviewed
    or on a change that traces to no decision: null
  sections:
    Purpose: 'Prevents a session from reaching the librarian on work nobody reviewed, or on a change that traces to no decision. Retro is an analysis of this session only, written by the agent for the librarian and the next session: it runs in the turn of `/work`, with no stop for the person, and its report is `handoff.md` (case 531.1). The tests and the style check load before the first turn of the skill. The scope rule is mechanical: an edit is allowed when it finishes work a line of this session''s ledger ratified, and is new scope otherwise. Retro opens by two paths, both behind `guppi gate`: the agent''s call on `PreToolUse Skill` at the end of `/work`, and the person''s typed `/retro` on `UserPromptSubmit`; each checks the Spec against the ledger and leaves the mark `retro`, and a refused typed prompt is not expanded (case 169.3, supersedes 150).'
    Render: |-
      <!-- rule-retro -->
      ---
      name: retro
      description: Review this session's work — tests, style, readings, lessons — commit it and go on to /handoff, in the turn that /work runs, with no stop for the person.
      ---


      Tests: !`make test`

      Style: !`make style`

      Ledger: !`uv run guppi tail`

      Retro is an analysis of this session for the librarian and the next session, not planning, and it runs without the person: `/work` calls it in the same turn, and you stop only on a condition of `vault/wiki/where-to-stop.md`, which `/work` loaded (case 531.1). Show no report and ask for no approval. Read `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3). Sort the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73). A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line, a `read` line whose `estimate[...]` stands in the Tail above and a `read` line whose reading you take in this turn wait for the librarian, whose scripts tick them (cases 226, 250, 270); they are not debt. A `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, waits for a later session; it is neither debt nor the librarian's (case 428.4). Another `read` line without its line in the Tail is debt, and so is a box of code, a test, a command or a migration left unticked. The lines of a Case that a `{supersedes:case N}` line of the Tail names are not counted at all; its work stands under the superseding Case (case 282).

      Each finding ends in one of three ways: a `- lesson[...]` line, which you decide on; a `- estimate[...]` line, a reading of an Estimate whose work is finished; or a line of `handoff.md` in the section of its kind, which `/handoff` writes. Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `handoff.md`, and a `create`, `update` or `delete` waits for the next Plan Mode (case 531.1).

      Edit code only when the edit finishes work that traces to a line of this session's ledger.
      Red tests: fix now when the fix finishes ratified work; otherwise save the change with `git diff` into `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session's folder, revert it, write a `- lesson[error][...]` line whose root cause says why Retro was reached with a regression, and name the patch in `## Debt` of `handoff.md`; the commit still needs green. A failing test or a lint finding line that `## Baseline` of `work.md` already holds was red before the work, whatever `## Expected red` names: it is a line of `## Observations` of `handoff.md`, named as red before the work; it is not debt, nothing is fixed or reverted for it, and no lesson is written for it (case 479.4).
      `gh` is not available: name a bug that needs a decision in `## For the next session` of `handoff.md`, so the brief carries it.
      Do not run `make lint` here: the vault is written after handoff, by the librarian. A check that reads a page or a governed file this session's Spec updates — `make lint` or one of its steps, or a hook of the working tree — is red or refuses in Work Mode until the librarian's run writes the page or renders the file, and the `make lint` of that run is its reading: `/work` marks such a red under `## Expected red` of `work.md` when the task that changes the check runs, one line naming the check and the page or file it waits for. A red or a refusal of that check on a page or file a line names is a line of `## Observations` of `handoff.md` that names the check and the page or file it waits for, and it is not debt; a red or a refusal on a page or file no line names is debt, even when another line names the same check, unless `## Baseline` holds its line. In a session with no `work.md`, such a red is a line of `## Observations` by your judgment. A red test is never an expected red: it is fixed or reverted as above (cases 473.1, 479.3).

      Take the readings of the Estimates whose work is finished and that this session neither creates nor updates — by a decision line of its slug, or by an `update` that renames a page to it. A reading measures the Criterion the page carries at the moment of the reading, the one ratified last, and its line is written only when the work that Criterion names is built. What a session changes, it does not measure: an Estimate this session creates or updates has no reading in this session, built or not, and the ledger hook refuses one (case 428.1); the `read` line of its old Criterion in an earlier Spec is not debt and is not read, and the reading of the new Criterion closes it in a later session, at the moment its `method` names (cases 283, 428.3). A reading whose `method` names the person's word is not yours to take: it is a line of `## Ask the person` of `handoff.md`, with the question the person answers (case 531.1). `handoff.md` names every Estimate whose reading cannot be taken yet, and every Estimate this session creates or updates.

      When the review is done, commit the work: `make style` clean, `make test` green but for the tests that `## Baseline` of `work.md` holds. Then end the reply with one `LEDGER` block that holds every reading and lesson of this turn, those of the Work readings of `/work` included; the reply asks the person nothing. When a condition of `vault/wiki/where-to-stop.md` holds at that point, open the reply with `STOP:` and ask the person instead. The hook of `rule-retro-onward` then sends you on: commit the session folder, then call `/handoff`, which writes the report into `handoff.md`. Write no `LEDGER` block after that reply.
      <!-- /rule-retro -->
  change: 'taken up: Retro shows no report and waits for no approval; it writes its readings and lessons in one reply, commits on green and calls /handoff; no short defer; a red test it cannot fix is a patch, a lesson and a Debt line; a reading that needs the person goes to Ask the person of handoff.md; the defers of cases 505 and 509 retired (case 531.1)'
- slug: estimate-retro-report-holds-each-fact-once
  rename: estimate-retro-runs-on-to-the-handoff
  set:
    status: pending
    purpose: Whether /retro reviews the session with no report and no approval, writes every reading and lesson of the turn in one reply, commits on green and calls /handoff in the same turn, writes no defer, and stops only on a condition of vault/wiki/where-to-stop.md
    method: 'by hand at the first run from /work to the librarian after the render: the replies of the turn, the ledger, git log and handoff.md read against the Criterion, recorded in the estimate line'
  change: 'renamed from estimate-retro-report-holds-each-fact-once and the Criterion replaced whole — no report and no approval: one reply of lines, a commit on green, then /handoff; the promise of each fact once moves to estimate-handoff-holds-each-fact-once (case 531.1)'
- slug: rule-end-of-work
  replace:
  - old: 'Three steps: the Retro conversation, the commit gate on the way to handoff, then handoff itself.'
    new: 'Three steps, which the agent runs in the turn of Work Mode with no stop for the person: Retro, the commit gate on the way to handoff, then handoff itself (case 531.1).'
  change: the steps of the end of a session run in the turn of Work Mode with no stop for the person (case 531.1)
- slug: entity-glossary
  replace:
  - old: '`/retro`: an analysis of this session only — the frontier first, then every item ends as a lesson, a reading, a short defer (a Case of `context`, `problem`, `purpose` under'
    new: '`/retro`: an analysis of this session only, called by `/work` in the same turn with no stop for the person — the readings and the lessons in one reply, a commit on green, then `/handoff`, whose `handoff.md` is its report; it writes no short defer, which stands only at the close of Plan Mode, under'
  - old: in the Spec) or a handoff note; edits only finish ratified work; red tests are fixed or reverted into a patch in `raw/`; ends with a commit
    new: in the Spec; edits only finish ratified work; red tests are fixed or reverted into a patch in `raw/`
  change: 'the row Retro: no frontier and no short defer; one reply of lines, a commit on green, then /handoff (case 531.1)'
```

```tasks
- [x] update `rule-retro` — the purpose, the Purpose and the Render replaced: no report, no approval, no defer, one reply of lines, commit on green, then `/handoff`; the defers of cases 505 and 509 retired
- [x] update `estimate-retro-report-holds-each-fact-once` — renamed; the Criterion replaced whole: Retro runs on to the handoff
- [x] update `rule-end-of-work` — the Retro step is no conversation
- [x] update `entity-glossary` — the row Retro, its words around the Spec heading that case 527.1 changes
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [x] `uv run guppi glossary`
- [ ] read `estimate-retro-runs-on-to-the-handoff` — by hand at the first run from `/work` to the librarian after the render
```

### Case 531.2 — The readings of Retro, on the agent's call and on the typed command

> **given:**
> `estimate-retro-loads` — the promise of the readings of Retro, replaced whole
> **＋** `rule-retro` — the Render of `/retro`, whose reading paragraph this promise reads
> **＋** `.claude/skills/retro/SKILL.md` — the skill file rendered from `rule-retro`
> **＋** `/work` — the skill that calls `/retro` at its end, rendered from `rule-work-mode`
> **＋** `rule-ledger-write` — refuses a reading of an Estimate the session creates or updates

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built — rendered, written, run.
> **＋** An Estimate that this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — gets no reading in this session, built or not; the handoff names it as a reading of a later session.
> **＋** The `read` line of its old Criterion in an earlier Spec is not read; the reading of the new Criterion closes it in a later session, at the moment its `method` names.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

```then
update:
- slug: estimate-retro-loads
  set:
    status: pending
  change: the Criterion replaced whole — the trigger is the agent's call at the end of /work or the typed /retro; the readings rule is unchanged (case 531.2)
```

```tasks
- [x] update `estimate-retro-loads` — the Criterion replaced whole: the trigger covers the agent's call at the end of `/work`
- [ ] read `estimate-retro-loads` — by hand at the first run from `/work` to the librarian after the render
```

### Case 531.3 — An expected red is an observation in `handoff.md`

> **given:**
> `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the promise on a red of a check that reads an updated page, replaced whole
> **＋** `rule-retro` — the Render of `/retro`, whose paragraph on `make lint` this promise reads
> **＋** `raw/<date>/<hi HHMM>/work.md` — its `## Expected red` and `## Baseline`
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — its `## Observations` and `## Debt`

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose Spec updates a page or a governed file, and in Work Mode `make lint`, one of its steps, or a hook of the working tree that reads that page or file went red or refused.

> **then:**
> The agent reads `raw/<date>/<hi HHMM>/work.md` if it stands.
> **＋** A red or a refusal of a check on a page or file that a line of `## Expected red` of `work.md` names with that check is a line of `## Observations` of `raw/<date>/<hi HHMM>/handoff.md` that names the check and the page or file it waits for.
> **－** The red is not debt: the agent does not fix it or revert it into a patch.
> **＋** The reading of the check that counts is the `make lint` of the librarian's run, after the page is written and the file rendered.
> **＋** A red or a refusal on a page or file that no line of `## Expected red` names is debt, even when another line names the same check, unless `## Baseline` of `work.md` holds its line.
> **－** In a session with no `work.md`, a red or a refusal of such a check is a line of `## Observations` by the agent's judgment.
> **－** A red test is never an expected red, even when `## Expected red` names it: it is fixed or reverted into a patch by the rule for red tests.

```then
update:
- slug: estimate-retro-red-check-of-an-updated-page-is-a-handoff-note
  set:
    status: pending
    purpose: Whether Retro reads work.md and writes a red or a refusal on a page or file that a line of its Expected red names as a line of Observations of handoff.md, not as debt, while a red on a page or file no line names is debt unless the Baseline holds it, a session with no work.md leaves it to the agent's judgment, and a red test is never an expected red
  change: the Criterion replaced whole — the trigger covers the agent's call; an expected red is a line of Observations of handoff.md, not an item of the frontier; the one-read rule of the frontier goes with the frontier (case 531.3)
```

```tasks
- [x] update `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the Criterion replaced whole: no frontier; the red is an observation of `handoff.md`
- [ ] read `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — by hand at the first run after the render whose `work.md` names a check under `## Expected red`
```

### Case 531.4 — A red of the Baseline is an observation, and the commit does not wait for it

> **given:**
> `estimate-retro-red-in-the-baseline-is-not-charged` — the promise on a red that the Baseline holds, replaced whole
> **＋** `rule-retro` — the Render of `/retro`, whose paragraph on red tests this promise reads
> **＋** `raw/<date>/<hi HHMM>/work.md` — its `## Baseline` and `## Expected red`
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — its `## Observations` and `## Debt`
> **＋** `estimate-guppi-tests-green` — the promise of a green `make test` on the branch

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/work.md` holds a `## Baseline`, and a test fails in the `make test` of Retro, or a lint finding stood in Work Mode.

> **then:**
> Retro counts each failing test and each lint finding line that `## Baseline` holds as red before the work, whatever `## Expected red` names, and writes it as a line of `## Observations` of `raw/<date>/<hi HHMM>/handoff.md`.
> **＋** It is not debt: nothing is fixed or reverted into a patch for it, and it gets no `lesson[error]` line.
> **＋** The commit of Retro needs `make style` clean and `make test` green, except for the failing tests that `## Baseline` holds.
> **＋** A failing test that `## Baseline` does not hold is fixed, or reverted into a patch that `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` names.
> **－** Without `work.md` there is no baseline, and no red is excused as red before the work.
> **－** `estimate-guppi-tests-green` still wants `make test` with no failed test on the branch: a red test of the baseline stays red there.

```then
update:
- slug: estimate-retro-red-in-the-baseline-is-not-charged
  set:
    status: pending
    purpose: Whether Retro writes a failing test or a lint finding that the Baseline of work.md already holds as a line of Observations of handoff.md, not debt, whatever Expected red names, and commits with make test green but for those tests
  change: the Criterion replaced whole — the trigger covers the agent's call; a red of the Baseline is a line of Observations of handoff.md, and a patch of any other red test is named in Debt (case 531.4)
```

```tasks
- [x] update `estimate-retro-red-in-the-baseline-is-not-charged` — the Criterion replaced whole: the trigger covers the agent's call; the red is an observation, a patch is named in Debt
- [ ] read `estimate-retro-red-in-the-baseline-is-not-charged` — by hand at the first run after the render whose `work.md` Baseline holds a failing test or a lint finding line
```

### Case 531.5 — `handoff.md` is the report of Retro, one section for each kind of fact

> **given:**
> `rule-handoff` — the page whose Purpose and Render give the `/handoff` skill and the form of `handoff.md`
> **＋** `.claude/skills/handoff/SKILL.md` — the skill file rendered from `rule-handoff`
> **＋** `estimate-handoff-holds-each-fact-once` — the promise on the form of `handoff.md`, replaced whole
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the file of the report
> **＋** `rule-brief` — the librarian reads `## What actually got done` for Where things stand
> **＋** `rule-retro` — the run that calls `/handoff`

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats; `## Direct instructions to the librarian` holds only what to check first and what may duplicate what.
> **＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
> **＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch, and under them two lines: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates.
> **＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
> **＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
> **－** No Case, box, reading, lesson or observation is named in two sections of `handoff.md`, and the file holds no commit, no number of an item and no end of an item.
> **－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

```then
update:
- slug: rule-handoff
  replace:
  - old: 'The handoff note carries three things no artifact holds: where the person hesitated, what the librarian should check first, and what actually got done.'
    new: 'The handoff note is the report of Retro: it carries what no artifact holds — where the person hesitated and what the librarian should check first — and what got done, the debt, the observations, what the next session decides and what only the person can answer, one section each (case 531.5).'
  sections:
    Render: |-
      <!-- rule-handoff -->
      ---
      name: handoff
      description: Write the handoff note from memory and hand the session to the librarian.
      ---


      Tree: !`git status --porcelain`

      If Tree above is not empty, stop and say "commit first". Otherwise write `vault/raw/<date>/<hi HHMM>/handoff.md` — the session's folder, one document, no `---` (case 73) — headed `# Handoff — <date>, <slice or topic>`. It is the report of Retro, written by the agent for the librarian and the next session (case 531.5), in these sections, in this order:
      - `## Notes from memory`: where the person hesitated, what stayed unclear, which decisions carried caveats.
      - `## Direct instructions to the librarian`: what to check first, what may duplicate what.
      - `## What actually got done`: the ids of the Cases ratified, by the Tail, a Case that a `{supersedes:case N}` line names not counted; the code files and tests changed; the result of `make test` and `make style`; the readings and lessons written, by their ledger line numbers.
      - `## Debt`: each box of the Spec that is debt, and each red test reverted into a patch, with the path of the patch; under them two lines: the count of the boxes that wait for the librarian, and the slugs of the `read` lines whose slug this session creates or updates.
      - `## Observations`: what was noticed in Work Mode and Retro — a bug, a contract that turned out imprecise, a red before the work, an expected red with its check and the page or file it waits for.
      - `## For the next session`: what needs a decision, which Retro does not take.
      - `## Ask the person`: one line per reading that only the person can take — the Estimate by slug, the mark `needs the person`, and the question the person answers.
      A fact stands in one section only: a Case, a box, a reading, a lesson or an observation named in one section is not named in another (cases 468.2, 531.5). The file names no commit, no number of an item and no end of an item. Write it from memory; do not re-read the artifacts. Short or empty sections are normal.

      Then dispatch the `librarian-guppi` agent with one line: `Materialize <date> from vault/raw/<date>/<hi HHMM>/handoff.md.`, the path of the file you just wrote. Wait for its report and show it to the person unchanged. Do not commit after this, and write no `LEDGER` block.
      <!-- /rule-handoff -->
  change: 'handoff.md is the report of Retro: Debt, Observations, For the next session and Ask the person added; no number, no end and no commit; the three old section names kept; the Purpose no longer counts three things (case 531.5)'
- slug: estimate-handoff-holds-each-fact-once
  set:
    status: pending
    purpose: Whether handoff.md, the report of Retro, holds each fact once in the section of its kind — What actually got done, Debt, Observations, For the next session, Ask the person — with no commit, no number and no end, and keeps the three old section names
  change: the Criterion replaced whole — handoff.md is the report of Retro, one section for each kind of fact, no numbers and no ends (case 531.5)
```

```tasks
- [x] update `rule-handoff` — the Purpose corrected and the Render replaced: `handoff.md` is the report of Retro, one section for each kind of fact
- [x] update `estimate-handoff-holds-each-fact-once` — the Criterion replaced whole: the sections of the report
- [x] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [ ] read `estimate-handoff-holds-each-fact-once` — by hand at the first `/handoff` after the render
```

### Case 531.6 — `/handoff` runs on the agent's call and the typed command

> **given:**
> `estimate-handoff-dispatches` — the promise of the steps of `/handoff`, replaced whole
> **＋** `rule-handoff` — the Render of `/handoff`
> **＋** `.claude/skills/handoff/SKILL.md` — the skill file rendered from `rule-handoff`
> **＋** `rule-retro-commit` — `guppi/gate.py`, which refuses `/handoff` on a dirty tree and writes the mark `handoff`
> **＋** `vault/raw/<date>/event_log.md` — the day's event log that holds the mark
> **＋** `vault/raw/<date>/<hi HHMM>/` — the session's folder, where `handoff.md` is written
> **＋** `librarian-guppi` — the agent that `/handoff` dispatches

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, the gate of `guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

> **then:**
> The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
> **＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
> **＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the sections that `rule-handoff` names, with no Read call on the artifacts.
> **＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written, and shows the librarian's report to the person unchanged.
> **－** No commit follows the handoff except the librarian's own, and no reply between the call and the librarian's report carries a `LEDGER` block.

```then
update:
- slug: estimate-handoff-dispatches
  set:
    status: pending
  change: the Criterion replaced whole — the trigger covers the agent's call after the reply that ends Retro; the sections are those of rule-handoff; no LEDGER block before the librarian's report (case 531.6)
```

```tasks
- [x] update `estimate-handoff-dispatches` — the Criterion replaced whole: the agent's call after Retro, the sections of `rule-handoff`
- [ ] read `estimate-handoff-dispatches` — by hand at the first run from `/work` to the librarian after the render
```

### Case 531.7 — One page says where the run stops, and `/work` loads it

> **given:**
> `rule-where-to-stop` — the new page of the stops; its Render is `vault/wiki/where-to-stop.md`
> **＋** `vault/wiki/where-to-stop.md` — the file rendered from it
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions` — the new promise of the stops
> **＋** `rule-work-mode` — the page whose Render is the `/work` skill, which imports the file and stops on the branch `main`
> **＋** `.claude/skills/work/SKILL.md` — the skill file rendered from `rule-work-mode`
> **＋** `rule-case-protocol` — its Render `vault/wiki/case-schema.md` gives the form of a task line
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec whose tasks the run executes
> **＋** `/retro` — the skill of `rule-retro`, whose call opens the window of a `STOP:` reply
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the file whose presence closes that window

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.

> **then:**
> The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
> **＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
> **＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
> **＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
> **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
> **＋** After the person's answer the run goes on from where it stopped.
> **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
> **－** No other point stops the run: a red test, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

```then
create:
- slug: rule-where-to-stop
  type: rule
  kind: Leaf
  purpose: Prevents the run from /work to the librarian from stopping where the person is not needed, or going on where only the person can decide
  enforcement: render
  governs: vault/wiki/where-to-stop.md
  render_mode: full
  tags:
  - session
  - workflow
  - harness
  - render
  sections:
    Purpose: 'Prevents the run from /work to the librarian from stopping where the person is not needed, or going on where only the person can decide. The person keeps three questions: what to do, the Cases of Plan Mode; what done means and how to check it, the Estimates; and where to stop, this page (case 531.7). `/work` loads its text by an import of `vault/wiki/where-to-stop.md`, and the refusal of `rule-retro-onward` names the file. A hook on a single action, such as a push, may enforce a condition later; until then the text in the context is the guard.'
    Render: |-
      <!-- rule-where-to-stop -->
      # Where to stop

      From the approved Spec to the librarian's report the run needs no person: `/work`, the Work readings, `/retro` and `/handoff` run in one turn. Stop and ask the person only on one of these conditions:

      1. A fork that changes a contract: the work needs a choice that no ratified Case makes, so a new Case is needed.
      2. A hook refuses, and its text gives no step you can follow, or says that the refusal is a stop.
      3. An action that git in this repository cannot undo, such as a push to a remote or a deletion outside the repository.
      4. A task of the Spec whose text opens with `stop:`: stop before it runs, and run it after the person's word.
      5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.

      To stop, end the reply with the question to the person. From the call of `/retro` until `handoff.md` stands, open that reply with `STOP:`, so that the hook of `rule-retro-onward` lets it end. Nothing else is a stop: a red test, a reading that only the person can take, an observation or a doubt goes on as a lesson or a line of `handoff.md`, as `/retro` says. After the person's answer, the run goes on from where it stopped.
      <!-- /rule-where-to-stop -->
- slug: estimate-where-to-stop-stops-only-on-its-conditions
  type: estimate
  ref: rule-where-to-stop
  kind: QA
  purpose: 'Whether the run from /work to the librarian stops for the person on each condition of vault/wiki/where-to-stop.md and on no other, with the text loaded by /work and a stop after the call of /retro opening with STOP:'
  method: 'by hand at the first run from /work to the librarian after the render: the context of /work, the replies of the turn and the Spec read against the Criterion, recorded in the estimate line; a condition that does not arise is named as not exercised'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-work-mode
  replace:
  - old: 'Branch: !`git branch --show-current`'
    new: |-
      @vault/wiki/where-to-stop.md

      Branch: !`git branch --show-current`
  change: /work loads the stops of rule-where-to-stop by an import of vault/wiki/where-to-stop.md (case 531.7)
- slug: rule-case-protocol
  replace:
  - old: one-off migration and reading; no `contract` line
    new: one-off migration and reading, a task that waits for the person's word before it runs opening its text with `stop:` (`rule-where-to-stop`, case 531.7); no `contract` line
  change: 'a task line that opens with stop: waits for the person''s word (case 531.7)'
```

```tasks
- [x] create `rule-where-to-stop` — the page of the stops
- [x] update `rule-work-mode` — `/work` imports the stops
- [x] update `rule-case-protocol` — a task that waits for the person opens with `stop:`
- [x] create `estimate-where-to-stop-stops-only-on-its-conditions` — the promise of the stops
- [x] `uv run guppi render`: `vault/wiki/where-to-stop.md`
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-where-to-stop-stops-only-on-its-conditions` — by hand at the first run from `/work` to the librarian after the render
```

### Case 531.8 — The run is one turn, and its lines wait for the reply that ends Retro

> **given:**
> `rule-work-mode` — the page whose Render is the `/work` skill and its step of Work readings
> **＋** `.claude/skills/work/SKILL.md` — the skill file rendered from `rule-work-mode`
> **＋** `estimate-work-mode-takes-the-work-readings` — the promise of the Work readings, replaced whole
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier, whose open `W` lines are the readings
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec whose last task opens the step
> **＋** `rule-case-protocol` — its Render `vault/wiki/case-schema.md` says when a reading or a lesson line is written
> **＋** `rule-ledger-write` — the `Stop` hook that writes the lines of a `LEDGER` block when a reply ends
> **＋** `/retro` — the skill of `rule-retro`, whose last reply carries the lines
> **＋** `vault/wiki/where-to-stop.md` — the stops of `rule-where-to-stop`

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.

> **then:**
> Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
> **＋** A moment of an earlier session, such as the librarian's run, has come.
> **＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and its `estimate[...]` line stands in the `LEDGER` block of the one reply that ends Retro.
> **＋** The tasks, the readings and `/retro` run in one turn, and no reply ends before the reply that ends Retro, except at a stop of `vault/wiki/where-to-stop.md`.
> **－** A reading of an Estimate this session creates or updates is not taken, and its `W` line stays open.
> **－** A reading whose moment has not come is not taken, and its `W` line stays open.
> **－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

```then
update:
- slug: rule-work-mode
  replace:
  - old: Close the line of each reading taken `[x] … · work` in `frontier.md` first, then write its `estimate[...]` line in a `LEDGER` block of a reply that ends in text; tick no `read` box. The person can stop the step in the chat, and the lines not reached stay open (case 508.3). Work Mode ends with `/retro`.
    new: 'Close the line of each reading taken `[x] … · work` in `frontier.md` first; tick no `read` box. Write no `LEDGER` block here: the line of each reading stands in the one reply that ends Retro (case 531.8). Run the tasks, the readings and `/retro` in one turn, with tool calls and no reply that ends, except at a stop that `vault/wiki/where-to-stop.md` names. Work Mode ends by calling `/retro`.'
  change: the tasks, the Work readings and /retro run in one turn; the reading lines go to the reply that ends Retro (case 531.8)
- slug: rule-case-protocol
  replace:
  - old: '`- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson exists — a reading'
    new: '`- estimate[...]` and `- lesson[...]` lines the moment the measurement or the lesson exists, but from `/work` to the end of Retro in the one reply that ends Retro, which carries them all (case 531.8) — a reading'
  change: the reading and lesson lines of the run from /work to the end of Retro stand in the reply that ends Retro (case 531.8)
- slug: estimate-work-mode-takes-the-work-readings
  set:
    status: pending
    purpose: Whether /work, after the last task and in the same turn, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line, leaves its line to the reply that ends Retro, and leaves open the readings this session changes or whose moment has not come
  change: the Criterion replaced whole — the run is one turn; the reading lines stand in the reply that ends Retro; the stop of the step by the person is gone (case 531.8)
```

```tasks
- [x] update `rule-work-mode` — the run in one turn; the lines of the Work readings go to the reply that ends Retro
- [x] update `rule-case-protocol` — the lines of the run wait for the reply that ends Retro
- [x] update `estimate-work-mode-takes-the-work-readings` — the Criterion replaced whole: one turn, the lines in the reply that ends Retro
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-work-mode-takes-the-work-readings` — by hand at the first run from `/work` to the librarian after the render
```

### Case 531.9 — A `Stop` hook sends the agent from the end of Retro to `/handoff`

> **given:**
> `rule-retro-onward` — the new page of the hook
> **＋** `estimate-retro-onward-sends-the-agent-to-the-handoff` — the new promise of the hook
> **＋** `guppi/onward.py` — the hook script, `uv run guppi onward`
> **＋** `guppi/cli.py` — the table of the `guppi` commands
> **＋** `tests/test_onward.py` — the tests of the hook
> **＋** `rule-hook-registry` — the `"hooks"` key of `.claude/settings.json`, where the hook is registered on `Stop`
> **＋** `rule-ledger-write` — `guppi/ledger.py`, the first `Stop` hook, whose session window and folder the hook imports
> **＋** `rule-event-log` — the event log, where `guppi gate` writes the mark `retro`
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — the file whose presence ends the window of the hook
> **＋** `/handoff` — the skill of `rule-handoff` that the refusal names
> **＋** `rule-where-to-stop` — `vault/wiki/where-to-stop.md`, which the refusal names

> **when:**
> The `Stop` hook `uv run guppi onward` receives the payload of the end of a reply of the main agent.

> **then:**
> It exits 2 when the event log of the session's window holds the mark `retro` of this session, `raw/<date>/<hi HHMM>/handoff.md` does not stand, `stop_hook_active` is false, and the reply that ended does not open with `STOP:`.
> **＋** Its reason on stderr tells the agent to commit the session folder and call `/handoff`, and, when a condition of `vault/wiki/where-to-stop.md` holds, to open its reply with `STOP:` and ask the person instead.
> **＋** In every other case it exits 0 and prints nothing: before the mark `retro`, once `handoff.md` stands, on a reply that follows a refusal of a `Stop` hook, and on a reply that opens with `STOP:`.
> **＋** `.claude/settings.json` registers it on `Stop`, after `uv run guppi ledger`, `uv run guppi ratified`, `uv run guppi casecheck` and `uv run guppi context`.
> **－** It counts nothing, reads no test result and calls no model: its judgment is the mark, the file, the flag and the first word of the reply.
> **－** Without a `hi` of the session in the event log, it exits 0.
> **－** It writes no file and no mark.

```then
create:
- slug: rule-retro-onward
  type: rule
  kind: Leaf
  ref: rule-end-of-work
  purpose: Prevents the run from stopping between the reply that ends Retro and /handoff, where no person is needed
  enforcement: hook
  implementation_ref:
  - guppi/onward.py
  - tests/test_onward.py
  - .claude/settings.json
  tags:
  - session
  - workflow
  - hooks
  - harness
  sections:
    Purpose: Prevents the run from stopping between the reply that ends Retro and /handoff, where no person is needed. In Claude Code the end of a reply hands the turn to the person, and the ledger hook writes the lines of a reply only when it ends; so Retro ends one reply with its `LEDGER` block, and this hook sends the agent on to `/handoff` in the same turn (case 531.9). It judges only the state of files and of the payload — the mark `retro` of the session in the event log, the absence of `handoff.md`, the flag `stop_hook_active` and the first word `STOP:` of the reply — and counts nothing, so it fires at most once a turn and cannot loop. A deliberate stop is a reply that opens with `STOP:`, on a condition of `rule-where-to-stop`.
- slug: estimate-retro-onward-sends-the-agent-to-the-handoff
  type: estimate
  ref: rule-retro-onward
  kind: QA
  purpose: Whether guppi onward refuses the end of a reply after the retro mark while handoff.md does not stand, once a turn and not on a reply that opens with STOP:, and is silent otherwise, counting nothing
  method: 'uv run pytest tests/test_onward.py; by hand at the first run from /work to the librarian after the render: the event log, the replies of the turn and handoff.md, recorded in the estimate line'
  tags:
  - session
  - workflow
  - hooks
  - harness
update:
- slug: rule-hook-registry
  replace:
  - old: '"uv run guppi context", "timeout": 30 } ] }'
    new: '"uv run guppi context", "timeout": 30 }, { "type": "command", "command": "uv run guppi onward", "timeout": 30 } ] }'
  change: the Stop hook guppi onward of rule-retro-onward registered after guppi context (case 531.9)
```

```tasks
- [x] create `rule-retro-onward` — the page of the hook
- [x] update `rule-hook-registry` — `guppi onward` registered on `Stop`
- [x] `guppi/onward.py` — the hook: the session window, the stamp and the folder imported from `guppi/ledger.py`; exit 2 with the reason on stderr on the four conditions, exit 0 otherwise
- [x] `guppi/cli.py` — the command `onward` in the table and the docstring's list of hook commands
- [x] `tests/test_onward.py` — a refusal after the mark `retro` with no `handoff.md`; silence before the mark, with `handoff.md`, on `stop_hook_active`, on a reply opening with `STOP:`, and without a `hi`
- [x] create `estimate-retro-onward-sends-the-agent-to-the-handoff` — the promise of the hook
- [x] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-retro-onward-sends-the-agent-to-the-handoff` — `uv run pytest tests/test_onward.py`, and by hand at the first run from `/work` to the librarian after the render
```

### Case 531.10 — The brief carries the readings that need the person in a list of their own

> **given:**
> `rule-brief` — the brief section of the librarian's frame
> **＋** `.claude/agents/librarian-guppi.md` — the agent file it renders into
> **＋** `estimate-brief-written` — the promise of the sections of the brief, replaced whole
> **＋** `vault/wiki/brief.md` — the brief
> **＋** `vault/wiki/backlog.md` — where the deferred items stand instead of a Deferred list
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — its `## For the next session` and `## Ask the person`
> **＋** `rule-carry-over` — the second writer of the brief, in the short shape

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
> **＋** Where things stand, Readings due, Flags and Readings at the close are as before. Flags also name every item `generate` moved to the sprint page's Backlog in the run, and every milestone it dropped.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`. `Cases` is what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md`: the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.
> **＋** An item stands in one list only. A list with no item is the line "none".
> **－** The brief states no decision: the sort by kind is not a judgment of the work.
> **－** The brief of the skill `carry` keeps its short shape, without Next session and without a Deferred list. `rule-brief` and `rule-carry-over` both say so.

```then
update:
- slug: rule-brief
  replace:
  - old: '- Next session: two lists, one line per item, an item in one list only, a list with no item the line "none" (case 268.1). `Cases`, what needs a decision: a handoff flag with a question or a request to change the sprint,'
    new: '- Next session: three lists, one line per item, an item in one list only, a list with no item the line "none" (cases 268.1, 531.10). `Cases`, what needs a decision: a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint,'
  - old: '`Work`, what is done without a decision: every `pending` reading of Readings due by its slug, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree.'
    new: '`Work`, what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree. `Ask the person`, a reading only the person can take: each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them.'
  change: Next session gets a third list, Ask the person, from handoff.md; Cases take its For the next session (case 531.10)
- slug: estimate-brief-written
  set:
    status: pending
  change: the Criterion replaced whole — Next session holds Cases, Work and Ask the person; Cases take For the next session of handoff.md (case 531.10)
```

```tasks
- [x] update `rule-brief` — a third list, Ask the person
- [x] update `estimate-brief-written` — the Criterion replaced whole: three lists in Next session
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [ ] read `estimate-brief-written` — by hand after the first librarian run on the new frame
```

### Case 531.11 — The Frontier gets a list `## Ask`, and has no rule for a failed pull or `gh`

> **given:**
> `rule-skill-hi` — the Frontier text of `/hi`
> **＋** `.claude/skills/hi/SKILL.md` — the skill file
> **＋** `estimate-hi-writes-frontier` — the promise of the Frontier, replaced whole
> **＋** `entity-glossary` — the table with the row "`/hi`, Frontier"; `vault/wiki/glossary.md` renders it
> **＋** `vault/wiki/brief.md` — its Next session, a source of the Frontier
> **＋** `vault/wiki/sprint.md` — the current milestone, a source of the Frontier
> **＋** `vault/wiki/backlog.md` — the backlog and its count
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier file of the session
> **＋** `ask-guppi` — the vault query the `- near` lines do not use

> **when:**
> The person invokes `/hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** Pre-spec finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: Assemble the Frontier from the above in two lists,
    new: Assemble the Frontier from the above in three lists,
  - old: A failed pull or an unavailable `gh` is a Cases item when `sprint.md` names no decision on it, and not an item when it does; neither is a reason to stop. A `failed` reading
    new: A `failed` reading
  - old: '`## Work`, what needs none: the `Work` list of the brief''s Next session; a dirty tree in `Status:`.'
    new: '`## Work`, what needs none: the `Work` list of the brief''s Next session; a dirty tree in `Status:`. `## Ask`, what only the person can answer: the `Ask the person` list of the brief''s Next session, one line per reading with its question (case 531.11).'
  - old: Write the same two lists, under `## Cases` and `## Work`, to
    new: Write the same three lists, under `## Cases`, `## Work` and `## Ask`, to
  - old: '`- [ ] W<n> — <title> · <source>` under `## Work`.'
    new: '`- [ ] W<n> — <title> · <source>` under `## Work`, `` - [ ] A<n> — `<slug>` — <question> · brief `` under `## Ask`.'
  - old: '`/pre-spec` fails on an open line under `## Cases`; a `W` line closes'
    new: '`/pre-spec` fails on an open line under `## Cases`, not on one under `## Work` or `## Ask`; a `W` or an `A` line closes'
  change: 'the Frontier gets the list ## Ask from the brief''s Ask the person, three lists in all; the rule for a failed pull or gh gone, carried from case 528.4 (case 531.11, supersedes 528.4)'
- slug: entity-glossary
  replace:
  - old: the open items it assembles (brief, sprint, backlog, issues, an unfinished plan, the ledger tail) in two lists, the kind of each by its source — Cases, the Plan Mode agenda, and Work, what needs no decision (case 268.2)
    new: the open items it assembles (brief, sprint, backlog, an unfinished plan, the ledger tail) in three lists, the kind of each by its source — Cases, the Plan Mode agenda; Work, what needs no decision; and Ask, the readings only the person can answer (cases 268.2, 531.11)
  change: 'the row /hi, Frontier: no issues, three lists with Ask (case 531.11)'
- slug: estimate-hi-writes-frontier
  set:
    status: pending
  change: 'the Criterion replaced whole — the list ## Ask with lines A<n>; the line on Pull and Open issues gone with the two commands, carried from case 528.4 (case 531.11, supersedes 528.4)'
```

```tasks
- [x] update `rule-skill-hi` — the list `## Ask`; the rule for a failed pull or `gh` gone, carried from case 528.4
- [x] update `entity-glossary` — the row "`/hi`, Frontier": no issues, three lists
- [x] update `estimate-hi-writes-frontier` — the Criterion replaced whole: the list `## Ask`; no line on `Pull:` and `Open issues:`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `uv run guppi glossary`
- [ ] read `estimate-hi-writes-frontier` — by hand at the `/hi` of a session after the render, and the frontier findings of `guppi prespec --check` in `tests/test_prespec.py`
```

### Case 531.12 — Pre-spec lets an `## Ask` line stand open

> **given:**
> `rule-prespec` — the page whose Render is the `/pre-spec` skill
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill file rendered from `rule-prespec`
> **＋** `guppi/prespec.py` — `check_frontier`, which reads the lines of the Frontier
> **＋** `tests/test_prespec.py` — the tests of the frontier findings
> **＋** `estimate-prespec-checks-the-frontier` — the promise of the frontier findings, replaced whole
> **＋** `vault/raw/<date>/<HHMM>/frontier.md` — the Frontier file the check reads

> **when:**
> `uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`.

> **then:**
> A missing file is the finding `frontier: <path> is missing`.
> **＋** An open line under `## Cases` is a finding. An open line under `## Work` or `## Ask` is not.
> **＋** A closed line whose last segment after ` · ` is none of `case N`, `work`, `defer`, `kept` and `defer case N` is a finding.
> **＋** These pairings of box and closer are findings: `[x]` with `defer`, `kept` or `defer case N`, and `[-]` with `case N` or `work`.
> **＋** `defer` is clean only after the source segment `sprint`, the segment before the closer. `kept` is clean only after the source `backlog`. After any other source, each one is a finding.
> **＋** `defer case N` after the source `sprint` or `backlog` is a finding. After another source, it is a finding when there is no `defer` item under Case N.
> **＋** A line closed `case N` is a finding when the plan has no heading of Case N.
> **－** A line that is not a box line, such as `Backlog: N items` or an indented `- near` line, is not read. No line of another session's Frontier file is read.

```then
update:
- slug: rule-prespec
  replace:
  - old: — a line of `## Work` may stand open until its work is done (case 356.1) —
    new: — a line of `## Work` or `## Ask` may stand open until its work is done (cases 356.1, 531.12) —
  change: 'an open line under ## Ask is no finding of pre-spec, as one under ## Work (case 531.12)'
- slug: estimate-prespec-checks-the-frontier
  set:
    status: pending
  change: 'the Criterion replaced whole — an open line under ## Ask is no finding, as one under ## Work (case 531.12)'
```

```tasks
- [x] `guppi/prespec.py` — `check_frontier`: an open line under `## Ask` is no finding, beside `## Work`; the docstring says so
- [x] `tests/test_prespec.py` — an open `A` line under `## Ask` gives no finding; a closed one is judged as any
- [x] update `rule-prespec` — an open `## Ask` line is no finding
- [x] update `estimate-prespec-checks-the-frontier` — the Criterion replaced whole: an open `## Ask` line is no finding
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-checks-the-frontier` — `uv run pytest tests/test_prespec.py`, in a session after this one
```

### Case 531.13 — `/hi` asks the person each `## Ask` line, and the answer is the reading

> **given:**
> `rule-skill-hi` — the page whose Render is the `/hi` skill and its reading step
> **＋** `.claude/skills/hi/SKILL.md` — the skill file
> **＋** `estimate-hi-takes-its-readings` — the promise of the readings at `/hi`, replaced whole
> **＋** `vault/wiki/brief.md` — its Readings due and its list Ask the person
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — its lists `## Work` and `## Ask`
> **＋** `rule-ledger-write` — the hook that writes the reading lines of a `LEDGER` block

> **when:**
> The person types `/hi` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian's run and whose whole method can be done at that moment.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the commands of the method, and reads the librarian's report from the transcript of the previous session.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken as `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** A reading whose `method` also names a later moment is not taken at `/hi`. It is taken at that moment, and its `/hi` part is read then from the session's first turn.
> **－** A reading whose `method` asks for a `/hi` run of its own, such as one outside plan mode, is not taken at `/hi`.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: Wait for the human to pick the order or defer items.
    new: 'Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. When the person answers one, close its line `[x] … · work` in `frontier.md` first, then write its reading line in a `LEDGER` block of the reply, which ends in text, the answer as its result (case 531.13). Wait for the human to pick the order or defer items.'
  change: /hi puts each open Ask line to the person; the answer becomes the reading line (case 531.13)
- slug: estimate-hi-takes-its-readings
  set:
    status: pending
    purpose: Whether /hi takes, in its first reply, each open W reading whose method names /hi or the librarian's run and can be done whole then, puts each open Ask line to the person as a question and writes the answer as its reading line, closes each line it ends, opens no page but the Estimates it reads, and leaves the readings that name a later moment or a /hi run of their own
  change: the Criterion replaced whole — the Ask lines put to the person in the first reply, the answer written as the reading line (case 531.13)
```

```tasks
- [x] update `rule-skill-hi` — the `## Ask` lines put to the person; the answer is the reading line
- [x] update `estimate-hi-takes-its-readings` — the Criterion replaced whole: the `## Ask` lines asked, the answer written as the reading
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [ ] read `estimate-hi-takes-its-readings` — by hand at the first `/hi` after the render whose brief holds an Ask the person line
```

### Case 531.14 — A short defer has one moment, the close of Plan Mode

> **given:**
> `rule-case-protocol` — its Render `vault/wiki/case-schema.md` gives the moments of a short defer
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `estimate-case-protocol-defers-in-one-reply` — the promise of a defer in one reply, replaced whole
> **＋** `rule-spec-write` — the `Stop` hook that writes a short Case into the plan file
> **＋** `rule-retro` — Retro, which puts nothing off
> **＋** `rule-prespec` — `/pre-spec`, which the question after the Frontier names
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier the reply shows
> **＋** `raw/<date>/<hi HHMM>/handoff.md` — its `## For the next session`

> **when:**
> The person asks in the chat to defer an item in Plan Mode.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** The reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** A question follows the Frontier and ends the reply: which open item is next, or, when no line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, whether to run `/pre-spec` of `rule-prespec`.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows that question.
> **－** Retro writes no short defer: what it would put off is a line of `## For the next session` of `raw/<date>/<hi HHMM>/handoff.md`.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: 'It has two moments: the close of Plan Mode, when the person defers the items left open, and Retro, which ratifies no other decision. Either way the person''s words asking for the defer are its ratification'
    new: 'It has one moment: the close of Plan Mode, when the person defers the items left open; Retro runs without the person and puts nothing off — what it would put off is a line of `## For the next session` of `handoff.md` (case 531.14). The person''s words asking for the defer are its ratification'
  - old: heading of the plan file, or of `raw/<date>/<hi HHMM>/spec.md` at Retro — the agent writes none of it (case 421.2) — in Plan Mode then the Frontier
    new: heading of the plan file — the agent writes none of it (case 421.2) — then the Frontier
  change: a short defer has one moment, the close of Plan Mode; Retro puts nothing off (case 531.14)
- slug: estimate-case-protocol-defers-in-one-reply
  set:
    status: pending
  change: the Criterion replaced whole — a defer the person asks for in Plan Mode; Retro writes no short defer (case 531.14)
```

```tasks
- [x] update `rule-case-protocol` — a short defer has one moment
- [x] update `estimate-case-protocol-defers-in-one-reply` — the Criterion replaced whole: a defer in Plan Mode only
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-defers-in-one-reply` — by hand, the first defer the person asks for after the render that leaves no line under `## Cases` of `frontier.md` open
```

### Case 531.15 — The gate's refusal of the agent's `/retro` names a stop, not a next reply

> **given:**
> `estimate-retro-commit-gates` — the promise of the refusals of `guppi gate`, replaced whole
> **＋** `rule-retro-commit` — the page of the hook `guppi gate`
> **＋** `guppi/gate.py` — the hook script, whose advice on the `Skill` path changes
> **＋** `tests/test_gate.py` — the tests of the refusals
> **＋** `rule-where-to-stop` — `vault/wiki/where-to-stop.md`, whose second condition counts a refusal that says it is a stop
> **＋** `vault/raw/<date>/event_log.md` — the day's event log, where the gate writes its marks
> **＋** `/retro` and `/handoff` — the skills the gate refuses and marks
> **＋** `/hi` — the skill the gate lets through with no mark

> **when:**
> `guppi gate` receives a `PreToolUse` payload of a `Skill` call, or a `UserPromptSubmit` payload whose prompt, trimmed, opens with one of the three commands the gate marks, with or without arguments.

> **then:**
> A `/handoff` on a dirty tree, where `git status --porcelain` is not empty, exits 2 with the reason "commit first" on stderr, and the client blocks the call; on a clean tree it exits 0.
> **＋** A `/retro` in a session with a `hi` but no `spec.md` in its folder, no plan file named by the event log and no `- decision[`, `- estimate[` or `- lesson[` line in its window exits 2 with "gate: /retro refused — nothing to review: no Spec and no ledger line in raw/<date>/<HHMM>/. Ratify a Case or write a reading or a lesson first, then type /retro again."; on the `Skill` path the end reads "…first. This refusal is a stop of vault/wiki/where-to-stop.md: end your reply with the question to the person."
> **＋** Otherwise a `/retro` whose Spec holds an item with no decision line of its Case exits 2 with "gate: /retro refused — N item(s) of the Spec have no ledger line (case A). Ask the agent to end its reply with the LEDGER block, then type /retro again".
> **＋** A call it lets through, on either path, writes the same mark `prespec`, `retro` or `handoff` into the day's event log `vault/raw/<date>/event_log.md`; a refusal writes no mark.
> **＋** Any other prompt or skill, `/hi` included, exits 0 with no output and no mark.
> **－** Without a `hi` in the session, the checks of `/retro` do not run.
> **－** On the `Skill` path the refusal "nothing to review" asks for no call in a next reply.

```then
update:
- slug: rule-retro-commit
  replace:
  - old: exit 2 with the reason `nothing to review`, the client blocks the prompt, no mark;
    new: exit 2 with the reason `nothing to review`, the client blocks the prompt, no mark — on the agent's call the reason says that the refusal is a stop of `rule-where-to-stop`, with no call in a next reply (case 531.15);
  change: the refusal nothing to review on the agent's call names a stop, not a call in the next reply (case 531.15)
- slug: estimate-retro-commit-gates
  set:
    status: pending
  change: the Criterion replaced whole — on the Skill path the refusal nothing to review names a stop of vault/wiki/where-to-stop.md, not a call in the next reply (case 531.15)
```

```tasks
- [x] `guppi/gate.py` — the advice of the `Skill` path for "nothing to review" reads "This refusal is a stop of vault/wiki/where-to-stop.md: end your reply with the question to the person."; the docstring says so
- [x] `tests/test_gate.py` — the `Skill` path of "nothing to review" asserts the new advice and no "in the next reply"
- [x] update `rule-retro-commit` — the refusal "nothing to review" on the agent's call is a stop
- [x] update `estimate-retro-commit-gates` — the Criterion replaced whole: the advice of the `Skill` path names a stop
- [ ] read `estimate-retro-commit-gates` — `uv run pytest tests/test_gate.py`, in a session after this one
```

## Deferred

## Case 532 — The lint findings on `rule-spec-box` are put off

> **context:**
> `make lint` reports two findings on `rule-spec-box`: a `schema` finding, since the page lacks the fields `kind` and `estimates`, and an `orphan` finding. The page stands `draft` with `deferred_by` on decisions 207, 219 and 232. The brief of session 1753 names the findings as a Cases item. The person put it off at the close of Plan Mode in session 2024, together with the Slice 5 items of the sprint.

> **problem:**
> `rule-spec-box` breaks the schema of a Rule page and has no parent, so `make lint` stays red on it.

```then
defer:
  - slug: rule-spec-box
    type: rule
    purpose: "make lint reports schema (the fields kind and estimates missing) and orphan on rule-spec-box; put off with the Slice 5 items in session 2024"
```
