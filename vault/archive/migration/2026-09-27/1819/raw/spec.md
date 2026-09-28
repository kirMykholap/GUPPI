<!-- approved 20:18:32 · session 938809b2 -->

# Spec — session 1819, 2026-09-27

## Case 457 — `make` runs its recipes under a POSIX shell from PowerShell too

> **context:**
> The `Makefile` sets `SHELL := /usr/bin/sh`. Its header comment says that every recipe closes its own stdin, because a PowerShell child that inherits stdin from make hangs. Every recipe but `help` ends in `< /dev/null`. `help` runs awk over `$(MAKEFILE_LIST)` and has no redirect. On this machine, `make` is the native Windows GNU make at `C:/ProgramData/chocolatey/bin/make.exe`. Windows has no `/usr/bin/sh` path, so make looks for `sh.exe` on `PATH`. Under Git Bash, `PATH` holds Git's `usr/bin`, so every target runs. Under PowerShell, `sh` is not on `PATH` (the main agent read `(Get-Command sh).Source` as empty). Make then falls back to `cmd.exe`. There `< /dev/null` names no file, and the single quotes of the awk program of `help` do not quote. The handoff of session 1255 saw the failure on `make style`. Nobody has reproduced it yet, because Plan Mode runs no make.
> The person chose these answers in the rounds: the Makefile finds a POSIX shell by itself, a new Estimate on `rule-harness` holds the promise, and make stops with a message when it finds no such shell. `help` gets `< /dev/null` because the header comment already requires it of every recipe, not because of a new choice. No page governs the Makefile as a whole. `rule-lint` names it in `implementation_ref`, and its Purpose sentence that no target writes to the tree stays true. `estimate-harness-pipeline` is about the order and the exit of `make lint` and `make test-harness`, not their shell, so it stays as it is. The Criterion of `estimate-tests-clock-pinned` stands. Its line "The `Makefile` does not change" belongs to the fixture of case 145.1 and means that the fixture needed no new target. This Case does not touch that fixture or what `make test` collects, and replacing that Criterion would set a sound promise `pending` again. The skills `retro` and `carry` call `make` and need no change of text. The slug `estimate-harness-make-runs-in-both-shells` is free. The `create` carries a `ref`, so no vault query ran.

> **problem:**
> From PowerShell, make runs its recipes under `cmd.exe`. That shell cannot read `< /dev/null` or the quoted awk program of `help`. So `make style` fails there, and every other target should fail the same way. The agent can run the checks only through Bash, and nothing says so.

> **given:**
> `Makefile` — the shell its recipes run under; its header comment requires every recipe to close stdin
> **＋** `/usr/bin/sh` — the `SHELL` of the `Makefile` outside Windows
> **＋** `/dev/null` — the device each recipe of the `Makefile` reads its stdin from
> **＋** `C:/ProgramData/chocolatey/bin/make.exe` — the native Windows GNU make that reads it
> **＋** `estimate-harness-make-runs-in-both-shells` — the new promise
> **＋** `rule-harness` — the MOC of the harness tools, the target of the promise

> **when:**
> On Windows, someone runs `make help`, `make style`, `make test` or `make lint` of the `Makefile` from PowerShell and from Git Bash. `C:/ProgramData/chocolatey/bin/make.exe` reads the `Makefile`.

> **then:**
> Make runs each recipe under a POSIX `sh`, with stdin read from `/dev/null`. Each target gives the same exit code from PowerShell as from Git Bash.
> **＋** When make finds no POSIX `sh` on Windows, it stops before any recipe runs, with one message that names the missing shell and the places it searched.
> **－** Make never runs a recipe of the `Makefile` under `cmd.exe`.
> **－** No recipe of the `Makefile` reads the stdin of its caller, and no target writes to the working tree.
> **－** Outside Windows, the `SHELL` of the `Makefile` stays `/usr/bin/sh`.

```then
create:
- slug: estimate-harness-make-runs-in-both-shells
  type: estimate
  kind: QA
  purpose: make help, make style, make test and make lint run their recipes under a POSIX sh from PowerShell as from Git Bash, and stop with a message when no sh is found
  method: by hand, make help, make style, make test and make lint from PowerShell and from Git Bash on Windows, at the first session after the change
  tags:
  - harness
  - workflow
  ref: rule-harness
```

```tasks
- [x] create `estimate-harness-make-runs-in-both-shells`
- [x] `Makefile` — reproduce the failure of `make style` from PowerShell first. Then, on Windows only, set `SHELL` to a POSIX `sh` that make finds without Git's `usr/bin` on `PATH`, and stop with one message when none is found. Keep `/usr/bin/sh` elsewhere and every stdin redirect from `/dev/null`. Add the redirect to the `help` recipe. Add one sentence to the header comment on the shell.
- [x] by hand — `make help`, `make style`, `make test` and `make lint` from PowerShell and from Git Bash: the same exit code in both, no `cmd.exe` error
- [x] read `estimate-harness-make-runs-in-both-shells` — by hand, at the first session after the change
```

## Case 458 — A round of questions keeps its grill-me form when it is shown in Russian

> **context:**
> When `case-guppi` has a fork open, it answers with a round of questions in the form of `.claude/skills/grill-me/SKILL.md`. Each question opens with `❓ **Qn** - **<title>**:` and closes with a `➡️` line that holds the recommended answer. The main agent translates the round into Russian and shows it. In session 1819, for Case 457, the main agent rebuilt the rounds into its own bold headings and a "Recommendation" line, and the markers were gone (`lesson-case-show-grill-round-reformatted-in-translation`). The Render of `rule-case-protocol` says only that a round is shown "translated into Russian, slugs, paths and quotations unchanged". It names no form to keep, and no hook reads a round: `casecheck --subagent` does not check or store an answer that has no Case heading, and the `Stop` hook compares only Cases.
> In the rounds, the person chose three answers. The rule is text only, with no hook. The round is kept line by line. The promise is the replaced Criterion of `estimate-case-protocol-shows-the-built-case`, whose round line already speaks of the showing. Its purpose is that a built Case is shown unchanged, and its method is by hand on the showings of a session, so its method stays. The Render sentence "In the chat one horizontal rule at most, after the Case or its last sub-case" would forbid a horizontal rule after a round, so the Case changes it too. `estimate-case-protocol-loaded` promises only that the file equals the Render, so it is not touched (case 378.5). `estimate-language-followed` speaks of the language of a round, not its form, so it stays as it is. `.claude/skills/grill-me/SKILL.md` and `.claude/agents/case-guppi.md` already write the form, so they do not change. No `create`, so no vault query ran.

> **problem:**
> The main agent can meet the rule and still lose the form of a round: it translates the round but rebuilds its questions into its own headings. The person then sees the questions without the `❓ **Qn**` and `➡️` markers. The agent's recommended answer also no longer stands apart from the question. No sentence of the vault tells the main agent to keep that form.

> **given:**
> `rule-case-protocol` — its Render, the paragraphs "Who builds a Case" and "Language", where a round is shown
> **＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing, its Criterion replaced whole
> **＋** `.claude/agents/case-guppi.md` — the agent that builds a Case and writes a round
> **＋** `.claude/skills/grill-me/SKILL.md` — the form of a question in a round
> **＋** `rule-case-check` — the hooks that write the file of a Case and compare its showing
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a Case that the main agent sends
> **＋** `.claude/agents/ask-guppi.md` — the vault query the main agent dispatches at pre-spec

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions or answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case.
> **＋** An answer with no Case heading is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged — each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
> **＋** The main agent shows the Case of an answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file the hook of `rule-case-check` wrote from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, then its own text after one horizontal rule.
> **＋** A reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is sent and ratified again; the main agent edits no Case in the plan file.
> **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` once, at pre-spec, and not before a showing.
> **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: which the agent shows translated into Russian, slugs, paths and quotations unchanged, and no Case is shown
    new: which the agent shows translated into Russian line by line, slugs, paths and quotations unchanged — each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule — and no Case is shown
  - old: after the Case or its last sub-case, and only when the agent's own text follows
    new: after the Case, its last sub-case or the last question of a round, and only when the agent's own text follows
  change: a round of questions of case-guppi is shown in Russian line by line, each question keeping its ❓ **Qn** and ➡️ lines (case 458)
- slug: estimate-case-protocol-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — a round is shown in Russian line by line, in the form of grill-me (case 458)
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `estimate-case-protocol-shows-the-built-case`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-shows-the-built-case` — by hand, the rounds shown in a session after the render, against the answers of `case-guppi` in the transcript
```

## Case 459 — Lint does not count the Estimates of a render child against a MOC's reading

> **context:**
> Lint checks the `method` of each Estimate. For an Estimate of a MOC, a reading by hand passes only if every Estimate of the MOC's children is a reading too, or if a sibling Estimate names a `make <target>` (cases 112.1, 212). The clause stops a MOC's reading from hiding its children's tests. The code is `check_method` in `guppi/lint.py`, and the promise is `estimate-lint-checks-the-method`.
> The clause is wrong for `rule-claude-md`. `CLAUDE.md` is its Render in `render_mode: full`, with its three children spliced into their markers. Its one Estimate, `estimate-claude-md-rendered`, is a reading: the file equals the Render and every session loads it. Case 445.4 gave the child `rule-language` the Estimate `estimate-language-spec-prose-in-english`, whose `method` is a pytest over pre-spec. Since then lint prints `method: says by hand while estimate-language-spec-prose-in-english names a test file`. Case 454 deferred the item onto `rule-claude-md`.
> Nothing is hidden. By case 378.5, the Estimate of a render rule promises only that the file equals the Render and is loaded. The behaviour a spliced paragraph describes belongs to that child's own Estimate, which is read on its own.
> The frame has five MOCs with `enforcement: render` and `render_mode: full`: `rule-claude-md`, `rule-case-protocol`, `rule-skill-hi`, `rule-settings` and `rule-documentation`. The children of `rule-documentation` are code rules with tests. For that reason the person chose the narrow bound: only the Estimates of a child with `enforcement: render` stop counting. The Estimates of any other child still count.
> The same clause stands in two more places, and this Case changes both. One is the module docstring of `guppi/lint.py`. The other is the description of `method` that `rule-estimates-schema` renders into `vault/wiki/estimates/schema.yaml`.
> The new Criterion keeps every line of the old one. The old third line changes on purpose: it now counts only the counted Estimates of the children. The Leaf finding keeps its exact text. That text stands in quotation marks, not a code span, because the frame check of pre-spec reads a span with a slash as a path.
> The Criterion of `estimate-estimates-schema-checked` does not speak of the `method` description, so it is not touched. `estimate-prespec-catches-a-method-without-a-form` leaves the MOC branch to lint, so it still stands. No Estimate of `rule-claude-md` changes, because its promise is unchanged.
> The decision line carries `{supersedes:case 454}`, so `generate` clears the defer from `rule-claude-md`. The other lint findings in the brief stay with their own items.

> **problem:**
> Lint reports a contradiction on `estimate-claude-md-rendered` that is not one. The clause of cases 112.1 and 212 counts the tested Estimate of a child whose Render is spliced into its parent's file. That Estimate promises the child's own behaviour, not the file, so the parent's reading hides nothing.

> **given:**
> `estimate-lint-checks-the-method` — the promise of the `method` check of lint.
> **＋** `guppi/lint.py` — `check_method`, `children_estimates` and the module docstring, the MOC clause of cases 112.1 and 212.
> **＋** `tests/test_lint.py` — the tests of the MOC branch of the `method` check.
> **＋** `rule-estimates-schema` — renders the description of `method` into `vault/wiki/estimates/schema.yaml`.
> **＋** `Makefile` — the targets a `method` may name.
> **＋** `estimate-claude-md-rendered` — the reading of `rule-claude-md` that lint reports today.
> **＋** `rule-lint` — the rule the check belongs to.

> **when:**
> `uv run guppi lint` reads the `method` of each live Estimate: the field, or `## Method` on a page of the old shape.

> **then:**
> For an Estimate of a Leaf, a `tests/` file that exists, the word `pytest`, a `make <target>` of the `Makefile`, or `by hand` passes; else the finding "method: names no tests/ file, pytest or make target and is not a reading".
> **＋** A named `tests/` file that does not exist, or a `make <target>` the `Makefile` does not hold, is a finding.
> **＋** For an Estimate of a MOC, a `make <target>` of the `Makefile` passes whatever stands beside it; `by hand` without one passes when every counted Estimate of the children is a reading or a sibling Estimate names a `make <target>` of the `Makefile`; else a finding.
> **＋** On a MOC with `render_mode: full`, the Estimates of a child with `enforcement: render` are not counted.
> **＋** `estimate-claude-md-rendered` gets no `method` finding.
> **－** On a MOC with `render_mode: full`, the Estimates of a child without `enforcement: render` are counted.
> **－** On a MOC without `render_mode: full`, the Estimates of every child are counted, a child with `enforcement: render` included.

```then
update:
- slug: estimate-lint-checks-the-method
  set:
    status: pending
  change: 'the Criterion replaced whole — on a MOC with render_mode: full the Estimates of a child with enforcement: render are not counted (case 459)'
- slug: rule-estimates-schema
  replace:
  - old: and `by hand` passes only when every child's Estimate is a reading or a sibling Estimate of the MOC names such a target.
    new: 'and `by hand` passes only when every child''s Estimate is a reading or a sibling Estimate of the MOC names such a target; on a MOC with `render_mode: full` the Estimate of a child with `enforcement: render` is not counted, since that child''s Render is part of the parent''s file and its Estimate promises the child''s own behaviour (cases 378.5, 459).'
  change: 'the method of a MOC''s Estimate: the Estimates of a render child of a full MOC are not counted (case 459)'
```

```tasks
- [x] update `estimate-lint-checks-the-method`: the Criterion replaced whole
- [x] update `rule-estimates-schema`: the description of `method` in the Render
- [x] `guppi/lint.py`: in the MOC branch of `check_method`, skip the Estimates of a child with `enforcement: render` when the MOC has `render_mode: full`; the module docstring, in the `method` class, and the docstrings of `check_method` and `children_estimates` name the exception and case 459
- [x] `tests/test_lint.py`: a full MOC with a reading over a render child whose Estimate names a test file passes; the same MOC over a child without `enforcement: render` gives the finding; a MOC without `render_mode: full` over a render child gives the finding
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] read `estimate-lint-checks-the-method`: `uv run pytest tests/test_lint.py`, then `make lint` prints no `method` finding on `estimate-claude-md-rendered`
```

## Case 460 — A lesson slug carries its prefix: the page renamed, the ledger hook refusing a slug without it, one table of prefixes

> **context:**
> A lesson reaches the vault straight from its ledger line. The ledger hook writes any `lesson[...]` line from a `LEDGER` block. `lesson_entry` in `guppi/materialize.py` sends the line to the lessons folder because it is a lesson record, not because of its slug. `generate` then writes the page under the slug as written. Lint checks that `type` matches the folder and that the `slug` matches the filename, but it never checks the prefix. So ledger line 54 of session 1255 put `harness-senduserfile-renders-a-markdown-file-on-the-phone` into the vault without its `lesson-` prefix, and nothing reported it. A Glob over the six category folders finds no other live page without its category prefix.
> The prefix table is kept twice. `category_of` in `guppi/materialize.py` reads six prefixes, and `generate` imports that table. `guppi/lint.py` keeps its own copy of five prefixes, without `decision-`, for `check_decision` alone. So a `decision-` slug in a Decision list is a page for `materialize`, but lint does not look it up. `CLAUDE.md` calls a second copy of one judgment a defect. The deferred `decision-case-455` covers a different pair of functions.
> The lesson is `new`, and no live page links to it. `brief.md` and `log.md` name it, but they are records. The rules of the lessons schema say a lesson goes through no Case. That covers its birth, not a later change: the one rule still requires a Case to rename a page. The old slug has no prefix, so `materialize` marks the entry of 460.1 `category: unknown` and `incomplete: [category]` (case 320). `generate` still applies it: `Vault.update` finds the page in any folder, and `rename` requires the new slug to open with `lesson-`. `apply` ticks the line of every applied entry, whatever its category. The docstring of `guppi/generate.py` says the opposite, so 460.1 corrects it.
> `estimate-sprint-migration-file-route-gone` promises that a line with no prefix lands `category: unknown` and that `generate` "reports an error instead of 'applied by hand'". That line records the end of the file route. The code never failed an `update` or a `delete` of an unknown category (`test_a_delete_of_an_unknown_category_is_outside_the_vault`), and 460.1 relies on the `update` applying. The person chose to leave that Estimate as it is. The session 1255 entry is marked `applied`, so no rerun creates the old page again.
> The refusal of 460.5 goes beside the refusal of case 428.1 in the same hook. The other `Stop` hooks, `guppi ratified`, `guppi casecheck` and `guppi context`, do not read the slug of a lesson line, and `.claude/settings.json` does not change. The Criterion of `estimate-ledger-write-lifts` promises that every `- lesson[` line lands. That becomes false, so 460.4 replaces it whole with an exception, as case 428.2 did for 428.1. `case-schema.md` makes no claim that every lesson line lands, so it stays as it is. `rule-ledger-write` carries `deferred_by` `decision-case-442`, which is about another gap of the same hook, and 460 leaves it open. 460.3 replaces the Criterion of `estimate-lint-finds-a-broken-link` whole: every old line is kept word for word, and only the `decision` line changes. Live Decision lists name four `decision-` slugs: `decision-case-130.1`, `decision-case-140` and `decision-case-347` are live, and `decision-case-130.2` is archived. So I expect no new finding, but I have not run `make lint`. `rule-vault-layout` and `estimate-vault-layout-holds` are not touched, because the lint layout option was not chosen. The one `create` carries `ref: rule-ledger-write`, so no vault query ran. A Glob found the new Estimate slug and the new lesson slug free.
> 460.5 supersedes 460.2 of the first ratification. The ledger is append-only and still holds the three lines of 460.2, among them an update of `estimate-ledger-write-lifts`, which is now the work of 460.4. The text of the refusal is unchanged. 460.2 leaves the Spec (case 299.1), and its entries are marked superseded.
> In the rounds, the person chose these answers: the rename, a check in the ledger hook, and one table of prefixes; the prefix is added and nothing else changes; a new Estimate for the refusal, with the Criterion of `estimate-ledger-write-lifts` replaced in a sub-case of its own; lesson lines only, with the exceptions of case 428.1; the migration Estimate left as it is; the docstring of `generate` corrected.

> **problem:**
> One lesson page has no `lesson-` prefix, and nothing on the path from the ledger line to the page checks the prefix of a lesson slug. The table that judges a prefix also lives in two modules that already disagree on `decision-`.

### Case 460.1 — The SendUserFile lesson takes the `lesson-` prefix

> **given:**
> `harness-senduserfile-renders-a-markdown-file-on-the-phone` — the lesson page that is renamed
> **＋** `lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone` — the slug the page takes
> **＋** `guppi/generate.py` — applies the `update` and its `rename`, and ticks the line of an applied entry
> **＋** `guppi/materialize.py` — lifts the decision line into an entry
> **＋** `rule-lessons-schema` — the slug of a lesson: `lesson-`, then the area, then the cause
> **＋** `rule-vault-layout` — the filename is the slug
> **＋** `vault/wiki/brief.md` — a record that names the old slug
> **＋** `vault/wiki/log.md` — a record that names the old slug

> **when:**
> The librarian runs `uv run guppi generate` over the Spec of this session.

> **then:**
> The lesson page stands under the slug `lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone`, and no page stands under `harness-senduserfile-renders-a-markdown-file-on-the-phone`.
> **＋** Its History gains a `renamed from` line with the old slug and an `updated:` line with the change, each pointing to case 460.1.
> **＋** Its `origin`, `status`, `kind`, `root_cause`, `source`, `tags`, `## Trigger` and `## Root cause` stay as they were.
> **－** `vault/wiki/brief.md`, `vault/wiki/log.md` and the ledger lines keep the old slug, because they are records.

```then
update:
- slug: harness-senduserfile-renders-a-markdown-file-on-the-phone
  rename: lesson-harness-senduserfile-renders-a-markdown-file-on-the-phone
  change: the lesson- prefix added to the slug (case 460.1)
```

```tasks
- [x] update `harness-senduserfile-renders-a-markdown-file-on-the-phone`: the slug takes the `lesson-` prefix
- [x] `guppi/generate.py`: the module docstring says what `apply` does — an applied entry ticks its line whatever its category, an entry with no category (`unknown`) included; only a `lesson` entry and a failed entry tick nothing — and names case 460.1
```

### Case 460.3 — Lint judges the prefixes in a Decision list by the one table of `materialize`

> **given:**
> `estimate-lint-finds-a-broken-link` — the promise of the links lint follows; its Criterion is replaced whole
> **＋** `guppi/lint.py` — `check_decision` and its own prefix table
> **＋** `guppi/materialize.py` — `category_of`, the one table of prefixes
> **＋** `tests/test_lint.py` — the tests of the `decision` class
> **＋** `vault/wiki/` — the live pages lint reads
> **＋** `rule-one-judgment-one-implementation` — one judgment lives in one module

> **when:**
> `uv run guppi lint` reads the lists `create`, `update`, `delete` and `defer` of each Decision page under `vault/wiki/`.

> **then:**
> `check_decision` gives each slug of the lists its category by `category_of` of `guppi/materialize.py`, the prefix of a Decision page included.
> **＋** A slug with a category that no live or archived page carries is a `decision` finding.
> **－** A slug without a prefix known to `category_of` is not looked up.
> **－** The other classes of lint answer as before.

```then
update:
- slug: estimate-lint-finds-a-broken-link
  set:
    status: pending
  sections:
    Criterion: |-
      When:
      `uv run guppi lint` follows the links of the live pages under `vault/wiki/`.

      Then:
      `ref`: a slug in `parent`, `children`, `estimates`, `target`, `insight`, `addressed_by`, `deferred_by`, `applies_to`, `rules` or in a body `[[…]]` that no live or archived page carries; a body `[[…]]` may name a file under `vault/wiki/` by stem or path; a `[[…]]` inside a code span is no link.
      **＋** `ref`: an `applies_to` naming a page that is not an Entity; an Entity whose `rules` differs from the live rules whose `applies_to` names it, the difference as `+slug` and `-slug`.
      **＋** `ref`: a `[[slug]]` under a Decision page's `## Criterion` that is no live or archived Estimate; a `### case N` block under an Estimate's `## Criterion` with no live or archived `decision-case-N`.
      **＋** `origin`: an `origin` `raw/<date>[/<HHMM>]/ledger.md#case-N` or `#L<n>` whose ledger stands in neither `vault/raw/` nor `vault/archive/`, or in both, or holds no such case or line; an `origin` of another form on a page that is not an Insight.
      **＋** `decision`: a Decision page with none of `create`, `update`, `delete`, `defer`, or with `kind` or `target_slug`; a slug of its lists that `category_of` of `guppi/materialize.py` gives a category — the prefix `decision-` included — and that no live or archived page carries.
      **＋** `orphan`: a live entity, rule or estimate that no other live page names in its frontmatter; a Decision, a Lesson, an Insight and a placeholder never.
  change: the Criterion replaced whole — the prefixes of a Decision list are judged by category_of of guppi/materialize.py, decision- included (case 460.3)
```

```tasks
- [x] update `estimate-lint-finds-a-broken-link`: the Criterion replaced whole, every line kept but the `decision` one
- [x] `guppi/lint.py`: `check_decision` imports `category_of` from `guppi/materialize.py`, and the module's own `PREFIXES` table is removed; the docstring of the `decision` class names case 460.3
- [x] `tests/test_lint.py`: a Decision list that names a missing slug with the prefix of a Decision page gives the `decision` finding; one that names a live or archived Decision page gives none; a slug without a known prefix is not looked up
- [x] by hand — `make lint` on the live vault: no new `decision` finding
- [x] read `estimate-lint-finds-a-broken-link`: `uv run pytest tests/test_lint.py` in a later session
```

### Case 460.4 — A lesson line refused for its slug does not land

> **given:**
> `estimate-ledger-write-lifts` — the promise that the lines of a `LEDGER` block land; its Criterion is replaced whole
> **＋** `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger
> **＋** `guppi/ledger.py` — the hook
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `tests/test_gate.py` — the tests of the gate's advice
> **＋** `raw/<hi date>/<hi HHMM>/ledger.md` — the ledger of the session
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` — the refusal of a reading, an exception
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the refusal of a lesson slug, an exception

> **when:**
> The `Stop` hook `uv run guppi ledger` fires at the end of a turn of the main agent, with `transcript_path` and `last_assistant_message` in its payload; or `guppi gate` refuses a `Skill` call for an item of the Spec without a ledger line.

> **then:**
> In a session with a `hi` recorded, every line `- decision[`, `- estimate[`, `- lesson[` inside a `LEDGER` block of any text of the main agent in the transcript, the reply just finished included, lands in `raw/<hi date>/<hi HHMM>/ledger.md` with the time of writing, once — a body already in the ledger of any session is not written again.
> **＋** A block in a text followed by a tool call in the same turn reaches the ledger at the next `Stop` of the session, with the time of that `Stop`; the reply that ends in the text lands it now.
> **＋** The gate's advice to the agent reads "The text before a tool call waits for the next Stop: end this reply in text with the LEDGER block, then call /<skill> in the next reply."
> **－** An `estimate[...]` line the hook refuses by `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session` does not land.
> **－** A `lesson[...]` line the hook refuses by `estimate-ledger-write-refuses-a-lesson-without-its-prefix` does not land.
> **－** Without a `hi`: exit 2 with the reason, the ledger untouched; with `stop_hook_active`: exit 0, nothing written.
> **－** The last turn of a session that ends in a tool call has no `Stop` after it; its lines are a finding of Retro, not of the hook.

```then
update:
- slug: estimate-ledger-write-lifts
  set:
    status: pending
  change: the Criterion replaced whole — a lesson line refused for its slug does not land (case 460.4)
```

```tasks
- [x] update `estimate-ledger-write-lifts`: the Criterion replaced whole
- [x] read `estimate-ledger-write-lifts`: `uv run pytest tests/test_ledger.py tests/test_gate.py` in a later session
```

### Case 460.5 — The ledger hook refuses a lesson line whose slug lacks `lesson-`

> **given:**
> `rule-ledger-write` — the rule of the `Stop` hook that writes the ledger
> **＋** `guppi/ledger.py` — the hook, beside the refusal of case 428.1
> **＋** `guppi/materialize.py` — `category_of`, the one table of prefixes, and `parse_line`
> **＋** `tests/test_ledger.py` — the tests of the hook
> **＋** `estimate-ledger-write-refuses-a-lesson-without-its-prefix` — the new promise
> **＋** `rule-one-judgment-one-implementation` — one judgment lives in one module
> **＋** `rule-lessons-schema` — the slug of a lesson

> **when:**
> The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session. `category_of` of `guppi/materialize.py` does not put its slug under the lessons folder: the slug does not start with the lesson prefix.

> **then:**
> The line is not written.
> **＋** The other lines of the `Stop` are written as before.
> **＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — a lesson slug starts with lesson-, then the area, then the cause: write the line again with the prefix."
> **＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
> **－** A lesson line whose slug starts with the lesson prefix is written as before. A line already in the ledger of any session is not judged again.
> **－** `estimate[...]` and `decision[...]` lines are not judged by their prefix.
> **－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

```then
create:
- slug: estimate-ledger-write-refuses-a-lesson-without-its-prefix
  type: estimate
  kind: QA
  purpose: Whether the ledger hook refuses a lesson line whose slug does not open with lesson-, and says why only for the reply just finished
  method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
  tags:
  - session
  - hooks
  - harness
  - ledger
  ref: rule-ledger-write
update:
- slug: rule-ledger-write
  replace:
  - old: 'A reading of the new slug of a rename is not caught here: no decision line names it.'
    new: 'A reading of the new slug of a rename is not caught here: no decision line names it. A lesson names its category (case 460.5): a `lesson[<slug>]` line whose slug `category_of` of `guppi/materialize.py` does not put under `lessons` — a slug that does not open with `lesson-` — is not written, since `materialize` sends a lesson line to `lessons/` by its record, not by its slug, and a slug with no prefix reached the vault that way (session 1255, ledger line 54); as for a refused reading, the hook exits 2 with one stderr line per refused line only when the line stands in the reply just finished, skips an older one without a word, and writes the other lines as before.'
  change: the ledger hook refuses a lesson line whose slug lacks lesson- (case 460.5)
```

```tasks
- [x] create `estimate-ledger-write-refuses-a-lesson-without-its-prefix`
- [x] update `rule-ledger-write`: the refusal of a lesson slug without its prefix in `## How it works`
- [x] `guppi/ledger.py`: a function that returns the fresh `lesson[...]` lines whose slug `category_of` does not put under `lessons`, read by `parse_line` and `category_of` imported inside the function as `changed_by_session` does; `run` drops them with the refused readings, prints the stderr line for each one in the reply just finished, and exits 2 when either refusal speaks; the module docstring names case 460.5
- [x] `tests/test_ledger.py`: a lesson line without `lesson-` in the finished reply is not written, and the hook exits 2 with the stderr line; the same line in an earlier text is skipped silently; a `lesson-` line and the other lines of the `Stop` are written; a lesson line already in a ledger is not judged; an estimate or decision line without a prefix is not refused by this check
- [x] read `estimate-ledger-write-refuses-a-lesson-without-its-prefix`: `uv run pytest tests/test_ledger.py` in a later session
```

## Case 461 — A defer reply in Plan Mode ends with the Frontier and the question of what comes next

> **context:**
> When the person asks to put off an item, the main agent writes the short Case and its `LEDGER` line in one reply. The `Stop` hook of `rule-spec-write` then writes the short Case under `## Deferred`. `estimate-case-protocol-defers-in-one-reply` promises that in Plan Mode "the reply ends with the Frontier". It failed on the reading of session 1745 and failed again on the reading of session 1255. In 1255, the defer reply for Cases 454–456 was right in every other part. But the defers came at the close of Plan Mode, when no line was open, and a paragraph that proposed `/pre-spec` with a question followed the Frontier. The edit of the plan file seen in 1745 is now refused by the hook of Case 445.1.
> The Render of `rule-case-protocol` says only that the agent "asks nothing about it", meaning the defer. The acknowledging reply ends with "the question which item is next". So the defer reply is the only reply that must end with no question, even when `/pre-spec` is the only next step. In the rounds the person chose these points. The promise changes, not the reply: the defer reply ends as the acknowledging reply does, and no hook is added. `rule-orchestration` stays in `backlog.md` as it stands. The acknowledging reply is not changed. It has the same gap when the Case closes the last open line, and that is left not done: its reading (Frontier W8) can show whether it matters.
> Of the other Estimates of the rule, `estimate-case-protocol-loaded` promises only that the file equals the Render (case 378.5). `estimate-case-protocol-shows-the-built-case` speaks of the short form only as written by the main agent in English. `estimate-case-protocol-acknowledging-reply` speaks of the acknowledging reply. None of them is touched. The `replace` pair of this Case is in the paragraph "The short form — deferred decisions". The pairs of Case 458 are in "Who builds a Case" and "Language", so the anchors do not meet. No `create`, so no vault query ran.

> **problem:**
> The Criterion forbids any text after the Frontier in a defer reply. At the close of Plan Mode no line is open, and the person needs to know what comes next. So the agent writes a question after the Frontier, and the Estimate fails on a reply that did what the person needed. The wording that fails is the promise, and a stricter Render would fail again for the same reason.

> **given:**
> `rule-case-protocol` — its Render, the paragraph "The short form — deferred decisions", where the defer reply is described
> **＋** `vault/wiki/case-schema.md` — the file rendered from `rule-case-protocol`
> **＋** `estimate-case-protocol-defers-in-one-reply` — the promise of the defer reply, its Criterion replaced whole
> **＋** `rule-spec-write` — the `Stop` hook that writes the short Case into the plan file and `spec.md`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier whose line the defer reply closes
> **＋** `rule-prespec` — `/pre-spec`, the next step when no line under `## Cases` is open

> **when:**
> The person asks in the chat to defer an item, in Plan Mode or at Retro.

> **then:**
> In the same reply the agent shows the Case in the short form — `context`, `problem` and a fence tagged `then` with one `defer` item per target, no other section — and carries its `LEDGER` block, one `defer` line per target, with no tool call after it.
> **＋** The agent writes nothing of the Case into the plan file or `spec.md`: the `Stop` hook of `rule-spec-write` writes it.
> **＋** The person's words asking for the defer are its ratification: no question asks for it.
> **＋** In Plan Mode the reply shows the Frontier of `raw/<date>/<hi HHMM>/frontier.md` after the Case, with the line of the item closed `[-] … · defer case N`.
> **＋** In Plan Mode a question follows the Frontier and ends the reply: which open item is next, or, when no line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` is open, whether to run `/pre-spec` of `rule-prespec`.
> **＋** A wording the person corrects is a new short Case with `{supersedes:case N}` on its line, shown the same way.
> **－** No text follows that question.
> **－** At Retro no Frontier is shown.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: in Plan Mode then the Frontier with the line closed `[-] … · defer case N` — and asks nothing about it;
    new: in Plan Mode then the Frontier with the line closed `[-] … · defer case N` and, last, a question — which open item is next or, when no line under `## Cases` is open, whether to run `/pre-spec` — with no text after it; it asks nothing about the defer itself (case 461);
  change: the defer reply in Plan Mode ends with the Frontier and a question of what comes next, the open item or /pre-spec (case 461)
- slug: estimate-case-protocol-defers-in-one-reply
  set:
    status: pending
  change: the Criterion replaced whole — in Plan Mode a question of what comes next follows the Frontier and ends the defer reply (case 461)
```

```tasks
- [x] update `rule-case-protocol`
- [x] update `estimate-case-protocol-defers-in-one-reply`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-defers-in-one-reply` — by hand, the first defer the person asks for after the render
```

## Case 462 — One reader of the sections of a Case, in `guppi/materialize.py`

> **context:**
> Two functions read the `> **name:**` blockquotes of a Case into name → text: `case_text` in `guppi/materialize.py` and `quoted_sections` in `guppi/ratified.py`. They are the same walk, line for line. The only difference is the set of names: `case_text` fixes the seven sections, and `quoted_sections` takes the names as an argument. Both judge a fence by `fence_opening` and `closes_fence` of `materialize`. `materialize` uses its copy through `case_texts`, which `prespec` also calls. `ratified` and `casecheck` use the other copy. A fix to one walk does not reach the other, and the test in `tests/test_materialize.py` that runs both over one text catches a difference only for the input it holds. `CLAUDE.md` calls such a second copy a defect. Case 455 deferred the item onto `rule-one-judgment-one-implementation`.
> The reader cannot live in `ratified`, because `ratified` imports `materialize` and the reverse import would be a cycle. It cannot live in `guppi/pages.py`, because `materialize` imports `pages` and the fence functions live in `materialize`. The person chose that `materialize` keeps one function, `quoted_sections(lines, names)`; that `case_text` goes; and that `ratified` and `casecheck` import the function from `materialize`, with no re-export.
> The frame has one contradiction. The `When` of `estimate-materialize-judges-a-fence` lists `case_text` of `guppi/materialize.py` and `quoted_sections` of `guppi/ratified.py` among the readers of a fence, and the change makes that false. A Criterion changes only whole, so this Case replaces it whole with the list corrected. The person chose not to add a separate promise for the one reader. The guard against a second copy stays what `rule-one-judgment-one-implementation` has: its text in `CLAUDE.md` and the by-hand reading of the diff in `estimate-one-judgment-one-implementation-followed`. That Estimate is not touched, because the change makes its Criterion true and makes none of it false. The Render of the rule does not change either.
> `estimate-materialize-assembles` speaks of the `case_text` key of the yaml record, not the function. The key keeps its name, so that Estimate stands. The page of `rule-materialize` does not name either function. The fence paragraph of the `materialize.py` docstring names `quoted_sections` of `guppi/ratified.py`, and Work Mode corrects it. The `given` names `guppi/prespec.py` and `guppi/ledger.py` only because the Criterion lists their readers, so it holds eight `＋` lines.
> The decision line carries `{supersedes:case 455}`, so `generate` clears the defer from `rule-one-judgment-one-implementation`. Two things are not done here. The Case does not sweep `guppi/` for other duplicate judgments: a grep for `SECTION_START` and `QUOTE.match` found no third section reader. Case 460.3 takes the `PREFIXES` pair in `lint`.

> **problem:**
> One judgment, how the sections of a Case are read, lives in two functions in two modules. The two can drift apart while the tests still pass. The fence Estimate names both functions as separate readers, so it would be false once they merge.

> **given:**
> `estimate-materialize-judges-a-fence` — the promise that every reader of a fence judges it by the functions of `guppi/materialize.py`.
> **＋** `guppi/materialize.py` — the fence functions, `case_text`, `case_texts` and the docstring that lists the readers of a fence.
> **＋** `guppi/ratified.py` — `quoted_sections`, the second copy of the section reader, and its callers.
> **＋** `guppi/casecheck.py` — imports `quoted_sections` from `guppi/ratified.py`; its check of `ratification` reads a fence.
> **＋** `guppi/prespec.py` — `plan_prose`, a reader of a fence the Criterion lists.
> **＋** `guppi/ledger.py` — `ledger_lines`, a reader of a fence the Criterion lists.
> **＋** `tests/test_materialize.py` — the fence test that runs `case_text` and `ratified.quoted_sections` over one text.
> **＋** `tests/test_ratified.py` — the tests that call `ratified.quoted_sections`.
> **＋** `rule-one-judgment-one-implementation` — the rule that calls a second copy of one judgment a defect.

> **when:**
> A hook or a script reads a text that holds a fence: `then_blocks`, `tagged_blocks`, `quoted_sections` and `criterion_text` of `guppi/materialize.py`, `fenced_value` of `guppi/ratified.py`, `plan_prose` of `guppi/prespec.py`, the check of `ratification` in `guppi/casecheck.py`, or `ledger_lines` of `guppi/ledger.py`.

> **then:**
> A line opens a fence when, after at most three spaces of indent inside the block it stands in (a quote, a sub-point of `tasks`), it starts with a run of three or more backticks or three or more tildes.
> **＋** The fence closes only on a line of the same character whose run is at least as long as the opening run, with nothing after the run but spaces.
> **＋** A line with a shorter run, a run of the other character, or a word after its run stays inside the fence as content.
> **＋** A fenced value under a sub-point of `tasks` that holds a shorter fence of the same character is read whole, together with the inner fence.
> **＋** Every one of these readers takes the judgment from the functions of `guppi/materialize.py`, and they all give the same answer for the same text.
> **－** No reader keeps a fence pattern of its own: the `FENCE` of `guppi/ledger.py`, the `OPEN_FENCE` of `guppi/ratified.py`, and the tests on three backticks in `guppi/ratified.py` and `guppi/casecheck.py` are removed.

```then
update:
- slug: estimate-materialize-judges-a-fence
  set:
    status: pending
  change: the Criterion replaced whole — quoted_sections of guppi/materialize.py is the one reader of the sections of a Case; case_text and the copy in guppi/ratified.py removed (case 462)
```

```tasks
- [x] update `estimate-materialize-judges-a-fence`: the Criterion replaced whole
- [x] `guppi/materialize.py`: move `quoted_sections(lines, names)` here from `guppi/ratified.py`; remove `case_text`; `case_texts` calls `quoted_sections(lines, CASE_SECTIONS)`; the fence paragraph of the docstring names `quoted_sections` among the readers of this module and no longer under `guppi/ratified.py`
- [x] `guppi/ratified.py`: remove `quoted_sections` and import it from `guppi/materialize.py`, with no re-export
- [x] `guppi/casecheck.py`: import `quoted_sections` from `guppi/materialize.py`
- [x] `tests/test_materialize.py`: the fence test asserts `materialize.quoted_sections` once; the calls of `case_text` and `ratified.quoted_sections` are removed
- [x] `tests/test_ratified.py`: the calls of `ratified.quoted_sections` become calls of `materialize.quoted_sections`
- [x] `uv run pytest`: the whole suite passes
- [x] read `estimate-materialize-judges-a-fence`: `uv run pytest tests/test_materialize.py -k fence` in a later session
```

## Case 463 — A delete ticks the read lines of the Estimate it removes

> **context:**
> After `generate` applies an entry, it ticks the matching lines of the Spec. A `delete` entry ticks only its own line, `- [ ] delete `<slug>``, in the section of its Case (`tick_spec`, case 226.1). A `read` line is ticked only by a reading: an `estimate` entry, or a `create` with a folded reading. `tick_read` then ticks the line in every live Spec of `vault/raw/`. It skips the Cases ratified after the reading and the superseded Cases (cases 270.1, 280, 286, 326). When a later Case deletes an Estimate, no reading of it will ever stand in the ledger, so its `read` box stays `[ ]`. The librarian's Next session `Work` list then names that box as work to do until its Spec is archived.
> Case 456 deferred this onto `rule-page-generation`. The box it saw was `- [ ] read `estimate-prespec-checks-the-ratified-copy`` of Case 441.5, which Case 445.4 deleted. That box stands in `vault/archive/migration/2026-09-26/1745/raw/spec.md`. The person chose to leave it as it is. `generate` does not read the archive, and case 326 keeps an archived open line as the record of a task nobody performed.
> The person decided the following. A `delete` entry ticks the `read` lines of its slug by the same ticker as a reading. It uses both skips: superseded Cases in every Spec, and, in the Spec beside the yaml, Cases whose first decision entry has a greater ledger `line` than the delete. The second skip matters because an `update` can bring an archived page back (case 105.3). A Case ratified after the delete may then carry a new `read` line of that slug, and the delete must not close it.
> In the Purpose of `rule-page-generation`, the first pair replaces the list of entries that tick the `read` lines, which is the subject of the sentence on the reading ticks. The second pair replaces the skip of a Case ratified after the reading, in the same sentence. Each anchor stands once in the Purpose.
> Of the Estimates of the rule, only `estimate-generate-ticks-the-spec` speaks of the ticks, so this Case replaces its Criterion whole. `estimate-generate-writes-the-decision-page` names `delete` only as a list of the Decision page, and the change leaves that list alone.
> `rule-retro` stands. Retro counts only the boxes of its own session's Spec. The librarian ticks such a line after Retro, as it does the lines of a reading.
> This Case creates no page, so no vault query was run. The decision line carries `{supersedes:case 456}`, so `generate` clears the defer from `rule-page-generation`.

> **problem:**
> A `read` box of an Estimate that a `delete` removed never closes. No reading of a deleted page will stand in the ledger, so `generate` never ticks the line. The librarian's `Work` list then names work that nobody can do.

> **given:**
> `estimate-generate-ticks-the-spec` — the promise of the ticks of the Spec, whose Criterion this Case replaces whole
> **＋** `rule-page-generation` — its Purpose, the sentence on the ticks of the Spec
> **＋** `guppi/generate.py` — `tick` and `tick_read`, and the paragraph on the Spec in the docstring of the module
> **＋** `tests/test_generate.py` — the tests of the ticks
> **＋** `materialize.yaml` — the entries `generate` applies, with their `line` and their `superseded_by` marks
> **＋** `vault/raw/<date>/<HHMM>/spec.md` — the live Specs whose lines are ticked
> **＋** `vault/archive/` — the archived Specs, which are not read

> **when:**
> `uv run guppi generate` applied an entry of `materialize.yaml` and marked it `applied`.

> **then:**
> For a `create`, `update`, `delete` or `defer` entry, in the `spec.md` of the same unit, the first unticked line `` - [ ] <kind> `<slug>` `` in the section of the entry's Case becomes `- [x]`. Nothing else in the file changes. Each further entry of one kind and slug in one Case ticks the next such line, in order.
> **＋** For an `estimate` entry, a `create` entry with `folded` and a `delete` entry, every unticked line `` - [ ] read `<slug>` `` of every `spec.md` under `vault/raw/` becomes `- [x]`. The Spec beside the yaml comes first, then the Specs of the other session folders, oldest first.
> **＋** In the Spec beside the yaml, for an `estimate` or a `delete` entry, a `read` line in the section of a Case whose first decision entry carries a `line` greater than the entry's `line` is not the entry's line, and the search goes on.
> **＋** In any Spec, a `read` line in the section of a Case whose entries are marked `superseded_by` is not the entry's line. For the Spec beside the yaml, the marks come from the run's entries. For another Spec, they come from the `materialize.yaml` beside it. With no yaml beside a Spec, nothing is skipped there.
> **＋** A `create` entry with `folded` ticks both its page line and its `read` line. The filter by `line` does not apply to it, and the filter by `superseded_by` does.
> **＋** A `delete` entry ticks both its page line in its own Case and the `read` lines of its slug.
> **－** A line, a section or a Spec not found raises no error and prints nothing on stderr. The entry is `applied` all the same.
> **－** A `lesson` entry and an entry marked `failed` tick no line. A `delete` that fails leaves the `read` lines of its slug as they stand.
> **－** A `spec.md` under `vault/archive/` is not read.

```then
update:
- slug: rule-page-generation
  replace:
  - old: an `estimate` entry, or a `create` with a folded reading, every unticked
    new: an `estimate` entry, a `create` with a folded reading, or a `delete`, whose Estimate no reading will ever reach (case 463), every unticked
  - old: stands after the reading in the ledger
    new: stands after the reading or the `delete` in the ledger
  change: a delete ticks the read lines of its slug across the live Specs of raw/, with the skips of a reading (case 463)
- slug: estimate-generate-ticks-the-spec
  set:
    status: pending
    purpose: generate ticks the page line of a Case in the Spec beside its yaml, and the read line of a reading or of a deleted Estimate across the Specs of raw/ — never a line of a later or a superseded Case
  change: the Criterion replaced whole — a delete entry ticks the read lines of its slug, with the skips of a reading (case 463)
```

```tasks
- [x] update `rule-page-generation`: two `replace` pairs in the Purpose
- [x] update `estimate-generate-ticks-the-spec`: the Criterion replaced whole
- [x] `guppi/generate.py`: in `tick`, a `delete` entry also calls `tick_read` over `raw_specs` with the skip of `later_cases` by its `line` and the skip of `superseded_cases`; the docstrings of `tick` and `tick_read` and the paragraph on the Spec in the docstring of the module name case 463
- [x] `tests/test_generate.py`: tests that a `delete` of an Estimate ticks its `read` lines in the Spec beside the yaml and in an older Spec of `vault/raw/`; that a `read` line of a Case ratified after the delete stays open; that a `read` line of a superseded Case stays open; that a failed `delete` ticks nothing; and that a Spec under `vault/archive/` stays unchanged
- [x] read `estimate-generate-ticks-the-spec`: `uv run pytest tests/test_generate.py` in a later session
```
