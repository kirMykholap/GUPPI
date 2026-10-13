<!-- approved 17:13:25 · session 6f2e6cde -->

# Session 1426 — sprint plugin

## Case 795 — The GUPPI repository becomes an entity, and a single rule needs a link

> **context:**
> A new rule page that holds one rule (a `Leaf`) gets its `parent` from the `ref` of its decision line. Case 794 created `rule-github-repository` with no `ref`, so the page has no `parent`, no page lists it, and `make lint` prints it as an orphan. The librarian's script marked the entry `incomplete: [parent]` (line 41 of `raw/2026-10-12/2349/materialize.yaml`). The check before ratification never reported it, so Case 787.1 and Case 794 both passed without a parent. That check reports by `create_lacks` of `guppi/materialize.py`, which judges only the fields of `REQUIRED`. The parent of a `Leaf` rule is judged by a second test inside `_lift_item`, which `guppi/prespec.py` does not call. The test that runs both sides leaves `parent` out on purpose. Yet `estimate-prespec-hook-reports-a-create-without-a-required-field`, now `passed`, promises a finding for every field that the lift names under `incomplete`.
>
> The person chose that no grouping rule page fits. The rules of the GUPPI repository can differ from the rules of a repository of someone who uses GUPPI, so the repository is an entity of its own, and the rule guards it. Case 795.1 creates `entity-guppi-repository` as a part of `entity-guppi`, and `rule-github-repository` names it in `applies_to`. The cascade of `guppi/generate.py` then writes the rule into the `rules` of the entity, so a live page names the rule in its frontmatter and the orphan line goes. The rule gets no `parent`, as `rule-sprint-close` has none and links only to `entity-sprint`. `rules/schema.yaml` lists `parent` as optional on a rule, and its description of the field does not make it required, so it stands. The person also chose that the check accept such a rule. In Case 795.2, a `Leaf` rule lacks its parent only when it has neither a `ref` nor an `applies_to`, and `create_lacks` judges this for both sides.
>
> Vault answer for the new slug. A Glob `vault/**/entity-*repo*.md` printed nothing, so `entity-guppi-repository` is free. The index lines of `vault/wiki/entities/` hold no page on a repository, and the tags `github`, `ci` and `git` stand in `tags.md`. `entity-guppi` carries `deferred_by` Case 616: the future shape of GUPPI is put off. Adding a part the person named does not decide that question, so the defer stands, and no line of this session's Frontier puts it up. The purpose of `entity-guppi` names its parts, and so does one sentence of its Purpose. Case 795.1 changes both. `vault/wiki/backlog.md` repeats that purpose in its Deferred line, and the librarian's `uv run guppi backlog` writes it again in the same run. A Grep `entity-guppi[^-]` over `vault/wiki/` printed `backlog.md`, `log.md`, `rules/rule-rules-schema.md`, `rules/schema.yaml`, `rules/rule-harness.md`, `rules/rule-glossary.md`, `entities/entity-sprint.md`, `entities/entity-glossary.md` and `estimates/estimate-guppi-tests-green.md`. `log.md` is not read. The rest name `entity-guppi` as the entity of `rule-harness`, as the parent of the sprint and the glossary, as the target of `estimate-guppi-tests-green`, or in an example of the field `applies_to`, and the change makes none of them false.
>
> What checks each part. `rule-github-repository` has no Estimate, and a link between pages is no promise of the rule. So by the person's answer, the orphan line is left to the `make lint` of the librarian's run, which the brief reports (case 606.1). The Estimate that already checks the change of Case 795.1 is `estimate-lint-finds-a-broken-link` of `rule-lint`. Its Criterion makes lint report a live entity, rule or estimate that no other live page names in its frontmatter as `orphan`. It also makes lint report an entity whose `rules` differs from the live rules whose `applies_to` names it. Case 795.1 changes neither judgment, only the pages lint reads, so that Criterion stands and the Estimate is not set `pending`. Case 795.2 replaces the Criterion of `estimate-prespec-hook-reports-a-create-without-a-required-field` whole and sets it `pending`. Its `purpose` and its `method` (`-k required_field`) do not state the old exception, so they stand, and the new tests carry `required_field` in their names. The Criterion carries over each line of the old one word for word, and adds the two lines on the parent of a `Leaf` rule.
>
> One judgment. A Grep `Leaf` over `guppi/` printed `guppi/casecheck.py`, `guppi/lint.py`, `guppi/materialize.py` and `guppi/prespec.py`. Only `materialize.py` judges the parent of a `Leaf`. The others name a `Leaf` in docstrings on the method of an Estimate, on a nested Estimate and on a Leaf section. A Grep `applies_to` over `guppi/` printed `guppi/generate.py`, `guppi/lint.py` and `guppi/pages.py`. Those judge the `applies_to` of live pages: the backlink `rules`, and whether it names an entity. None judges what a `create` lacks. So `create_lacks` holds the judgment, and both the lift and `check_required` call it. Pre-spec reads the `ref` of a `create` from its item or from its decision line, as the tests of the check do.
>
> Tests. A Grep `entity-guppi|guppi-repository` over `tests/` printed `tests/test_glossary.py`, which writes its pages under a temporary folder, so no test reads a page Case 795.1 changes. A Grep `kind: Leaf|"kind": "Leaf"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_casecheck.py`, `tests/test_render.py`, `tests/test_lint.py`, `tests/test_materialize.py`, `tests/test_glossary.py`, `tests/test_ratified.py`, `tests/test_guard.py`, `tests/test_generate.py`, `tests/test_pages.py` and `tests/test_prespec.py`. Of these, only `tests/test_prespec.py` passes a `Leaf` rule `create` with no `ref` to `check_required`, in the tests of the required field. Its other plans carry a `ref` on the item or on the decision line. The `Leaf` creates of `tests/test_materialize.py` keep their marks, since the lift only stops marking a rule that has an `applies_to`. The other files write live-looking pages, not `create` items.

> **problem:**
> `rule-github-repository` stands with no link from any page, so lint prints it as an orphan. The check before ratification lets a new single rule through with no parent, though the librarian's script marks it incomplete and an Estimate promises the finding.

> **recommend:**
> - **Which page should be the parent of `rule-github-repository`?**
>   - Recommended: (a) `rule-harness`, with its Purpose sentence on its members changed.
>   - Answer: none of the options fits. The rules of the GUPPI repository and the rules of the repository of someone who uses GUPPI can differ; this is more like an entity, the GUPPI repository, which has its own rules. Replaced by the question **Where should the entity of the GUPPI repository stand?**
> - **Should this Case also make the check before ratification report a missing parent?**
>   - Recommended: (b) fix the page, and close the gap in a second sub-case.
>   - Answer: (b).
> - **How is the fix of the page confirmed?**
>   - Recommended: (a) the librarian's `make lint`, with no Estimate.
>   - Answer: (a).
> - **Where should the entity of the GUPPI repository stand?**
>   - Recommended: (a) a new entity `entity-guppi-repository` under `entity-guppi`, which `rule-github-repository` names in `applies_to`.
>   - Answer: agreed, (a).
> - **Does `rule-github-repository` still need a parent rule page?**
>   - Recommended: (a) no parent rule; the link to the entity is enough.
>   - Answer: agreed, (a).
> - **What should the check before ratification report for a new single rule?**
>   - Recommended: (a) report a single rule with neither a parent nor an entity link, by one shared function.
>   - Answer: agreed, (a).

### Case 795.1 — The GUPPI repository is an entity that its rule guards

> **given:**
> `entity-guppi-repository`: the new page of the GUPPI repository on GitHub.
> **＋** `entity-guppi`: the top entity, whose parts gain the repository.
> **＋** `rule-github-repository`: the rule of the repository, which names the new entity in `applies_to`.
> **＋** `guppi/lint.py`: `make lint`, whose `orphan` finding the change clears.

> **when:**
> The librarian's run applies the decisions of this session, and its `make lint` reads `rule-github-repository`, `entity-guppi-repository` and `entity-guppi`.

> **then:**
> `make lint` prints no `orphan` line for `rule-github-repository`.
> **＋** `rule-github-repository` names `entity-guppi-repository` in `applies_to`, and `entity-guppi-repository` lists the rule in `rules`.
> **＋** `entity-guppi` lists `entity-guppi-repository` in `children`, and its `purpose` and its Purpose name the repository as one of its parts.
> **－** `rule-github-repository` gets no `parent`, and no rule page lists it in `children`.

```then
create:
- slug: entity-guppi-repository
  ref: entity-guppi
  type: entity
  kind: Leaf
  purpose: The repository of GUPPI on GitHub, with rules of its own that a repository of another person who uses GUPPI need not share
  tags:
  - github
  - ci
  - git
  sections:
    Purpose: 'The repository of GUPPI on GitHub, as a thing of its own. Its rules are those of `rule-github-repository`, which names this page in `applies_to`: the rulesets on `main` and `prod`, the workflow of checks, and the approval of the runs of an outside contributor. A person who uses GUPPI keeps a repository of their own, whose rules may differ, so these rules belong to this repository and not to GUPPI as a whole (case 795.1).'
update:
- slug: rule-github-repository
  set:
    applies_to:
    - entity-guppi-repository
  change: the rule guards entity-guppi-repository, so a live page names it (case 795.1)
- slug: entity-guppi
  set:
    purpose: GUPPI as the thing this repository builds — the harness and the vault it keeps; its parts the sprint, the glossary and the repository of GUPPI on GitHub
  replace:
  - old: 'Its parts the person named: the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`) — the things of the vault that are content, not rules.'
    new: 'Its parts the person named: the sprint as a kind (`entity-sprint`) and the glossary (`entity-glossary`), the things of the vault that are content, not rules, and the repository of GUPPI on GitHub (`entity-guppi-repository`), whose rules are its own (case 795.1).'
  change: the repository of GUPPI on GitHub is a part (case 795.1)
```

```tasks
- [ ] create `entity-guppi-repository`
- [ ] update `rule-github-repository`
- [ ] update `entity-guppi`
```

### Case 795.2 — Pre-spec reports a single rule created with no link

> **given:**
> `guppi/materialize.py`: `create_lacks`, the one judgment of what a `create` lacks, and `_lift_item`, which marks `incomplete` by it.
> **＋** `guppi/prespec.py`: `check_required`, which reports by `create_lacks`.
> **＋** `tests/test_prespec.py`: the tests of the required field, and the test that runs both sides over the same items.
> **＋** `estimate-prespec-hook-reports-a-create-without-a-required-field`: its Criterion is replaced whole.
> **＋** `rule-prespec-hook`: the rule whose Estimate it is.
> **＋** `rule-case-check`: its check of a case file runs `judge`.
> **＋** `rule-spec-write`: its check after ratification runs `judge`.

> **when:**
> `judge` of `guppi/prespec.py` — run by `uv run guppi prespec --check <plan> --session <id>`, by the check of a case file of `rule-case-check` or by the check after ratification of `rule-spec-write` — reads a `create` item of a page of `rules`, `entities`, `estimates` or `insights` in the `then` blocks.

> **then:**
> A `create` item that lacks a field which `guppi materialize` would name under `incomplete` gives one finding that names the Case, the slug and the missing field.
> **＋** A `create` of a rule of kind `Leaf` with no `ref`, on its item or on its decision line, and no `applies_to` lacks the field `parent`: `judge` gives its finding, and `guppi materialize` names `parent` under `incomplete`.
> **＋** A `create` of a rule of kind `Leaf` with an `applies_to` and no `ref` lacks no `parent`, on either side.
> **＋** The list of required fields and the judgment of what is missing are one function of `guppi/materialize.py`, which the lift and `guppi/prespec.py` both call.
> **＋** A field counts as present when the item writes it as a key or under `sections`, and the tags count as present when the item or its decision line carries them.
> **－** The finding never names `type`, since the lift fills it from the category.
> **－** An Estimate with no `method` gives no second finding beside the one of the form of its method.
> **－** A `defer`, an `update` or a `delete` item gives no such finding.

```then
update:
- slug: estimate-prespec-hook-reports-a-create-without-a-required-field
  set:
    status: pending
  change: the Criterion replaced whole — the parent of a Leaf rule, or its applies_to, is judged by create_lacks on both sides (case 795.2)
```

```tasks
- [x] `guppi/materialize.py`: `create_lacks` takes the `ref` of the item or of its decision line, and names `parent` for a rule of kind `Leaf` with neither a `ref` nor an `applies_to`; `_lift_item` drops its own test of the parent and marks by `create_lacks` alone.
- [x] `guppi/prespec.py`: `check_required` passes `create_lacks` the `ref` of the item, or of the decision line of its Case and slug.
- [x] `tests/test_prespec.py`: the rule items of the tests of the required field that stand for another field carry a `ref`. Two new tests, their names holding `required_field`, cover a `Leaf` rule with neither a `ref` nor an `applies_to`, which gives the finding of `parent`, and one with an `applies_to` alone, which gives none. The test that runs both sides over the same items stops leaving out `parent`, and gains a `Leaf` rule with an `applies_to` and one with a `ref`.
- [ ] update `estimate-prespec-hook-reports-a-create-without-a-required-field`
- [ ] read `estimate-prespec-hook-reports-a-create-without-a-required-field`
```

## Case 796 — A script fed inline to an interpreter is refused before a shell call

> **context:**
> In Work Mode of session 2349 the agent changed `guppi/materialize.py` with a Python script typed inline in a Bash call. The event log of 2026-10-13 holds the command at 03:26:00: `python - <<'EOF' from pathlib import Path p = Path("guppi/materialize.py") ...`. The check before a Bash call, `uv run guppi bashguard` of `rule-bash-guard`, refuses a heredoc for two reasons only: a backslash in its body, or a marker line that writes a file. A heredoc fed into Python with neither reason passes. The hook after the call, `rule-shell-write-check`, then turned the CRLF line endings that the script wrote back into LF. This is the third such case. The archived `insight-workflow-file-changed-through-a-shell-command` records two Python heredocs that rewrote `guppi/onward.py`, in sessions 0211 and 0425, and one PowerShell call that rewrote a session file. Case 710.1 answered with the repair after the call, and the agent's choice came back. So the cause of `lesson-work-mode-edited-a-source-file-through-the-shell` is that nothing refuses an inline script before it runs. The one place that sends the agent to Edit is the refusal message of the Bash check.
>
> The person chose a refusal before the call, in both shells. Case 796.1 adds a third reason to the Bash check: a heredoc whose marker line runs an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`). Case 796.2 creates `rule-powershell-guard`, a new check before a PowerShell call that refuses a here-string piped into one of those interpreters. A script run by path and a script passed by `-c` or `-e` still pass in both shells. In PowerShell, a quoted string, a variable or the output of a command piped into an interpreter also still passes. These are left not done by the person's answers.
>
> The pages. `rule-bash-guard` is a `Leaf` that still holds `## How it works`. `rules/schema.yaml` says that such a section leaves at the page's next touch (cases 193, 200.2). No form of an `update` removes a section: Case 793 of session 2349 put that form off. By the person's answer, a one-off task in Work Mode removes the section by hand, as case 589.2 did for `rule-case-check`. The section's facts already stand in the docstring of `guppi/bashguard.py`. The section's sentence that a heredoc with no backslash whose output goes to a pipe or the screen passes becomes false with Case 796.1, and the section leaves with it. The Purpose of `rule-harness` names its members, among them the hook that refuses a heredoc with a backslash or a file write, and it counts them as eleven. Case 796.1 adds the third reason there. Case 796.2 adds the new check and makes the count twelve. The Criterion of `estimate-harness-pipeline` names a subset of those members, the Bash check among them by its two old reasons. The new Purpose still names that check, with one reason more, so the Criterion stands. The Criterion of `estimate-bash-guard` states what the check refuses and lets through, so Case 796.1 replaces it whole. Its `purpose` states the old promise and is set anew. Its `method` names only the tests and a live refusal, so it stands. Case 796.2 creates `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`. Case 796.2 changes the Render of `rule-hook-registry`. The Criterion of `estimate-hook-registry-rendered` promises that the `"hooks"` key of `.claude/settings.json` equals that Render byte for byte, and that every hook the harness runs is registered by one of its lines. The new hook gets its line in the Render in the same `update`, so the promise holds as written and the Criterion stands. An `update` of a Render touches no Estimate of the live reading (case 378.5), and the librarian's `render --check` reads it again. The registration on `PowerShell` is read by the `method` of the new Estimate after the librarian's run renders the file, since the target of that Estimate has no Render of its own. The `then` lines of the two sub-cases match each other on purpose, since each one sets the same kind of refusal for one of the two shells. They name different hooks, messages and log lines, so nothing is signed twice. The two lines of the old Criterion of `estimate-bash-guard` that name only two reasons are not carried word for word: Case 796.1 replaces them with lines that name three.
>
> What the frame showed. A Grep `bashguard|bash-guard|PowerShell` over `vault/wiki/` (with `log.md` and `brief.md` left out) printed `estimates/estimate-bash-guard.md`, `rules/rule-bash-guard.md`, `lessons/lesson-work-mode-edited-a-source-file-through-the-shell.md`, `estimates/estimate-harness-make-runs-in-both-shells.md`, `rules/rule-hook-registry.md`, `rules/rule-harness.md`, `rules/rule-shell-write-check.md` and `estimates/estimate-shell-write-check-repairs-and-reports.md`. The same Grep over `.claude/` printed `.claude/settings.json`. The Purpose of `rule-shell-write-check` says that the Bash guard reads only heredocs before a Bash call, and the docstring of `guppi/shellwrite.py` says the same. Both stay true. The Criterion of `estimate-shell-write-check-repairs-and-reports` speaks of the hook after a call, which no part of this Case changes. `estimate-harness-make-runs-in-both-shells` runs `make` from PowerShell and pipes no here-string. A Grep `heredoc|here-string|interpreter` over `vault/wiki/` printed `brief.md` and `log.md`, which are not read, and `lessons/lesson-work-mode-edited-a-source-file-through-the-shell.md`, `rules/rule-documentation.md`, `rules/rule-shell-write-check.md`, `rules/rule-harness.md`, `rules/rule-hook-registry.md`, `rules/rule-bash-guard.md`, `lessons/lesson-bash-tool-heredoc-escapes-interpreted.md`, `estimates/estimate-harness-pipeline.md`, `estimates/estimate-documentation-completes.md` and `estimates/estimate-bash-guard.md`. `rule-documentation` and `estimate-documentation-completes` forbid the librarian to put a file under `vault/` by a heredoc, which stays true. `lesson-bash-tool-heredoc-escapes-interpreted` sends a multi-line edit script to the scratchpad, run by path, which both checks let through. A Grep `<<|@'|@"|\| *python` over `.claude/` printed nothing, so no harness text tells an agent to run a command that the new checks refuse. On `PreToolUse`, `.claude/settings.json` registers `guppi prespec` on `ExitPlanMode`, `guppi gate` on `Skill`, `guppi guard` and `guppi ratified --guard` on `Edit|Write|MultiEdit`, `guppi bashguard` on `Bash`, `guppi pageread` on `Read` and `guppi grepguard` on `Grep`. None of them runs on `PowerShell`.
>
> One judgment. A Grep `python3?\b.*-|interpreter|INTERPRET|\bnode\b|PowerShell` over `guppi/` printed `guppi/bashguard.py`, `guppi/shellwrite.py` and `guppi/event.py`. They hold only a docstring on how the shell layer treats escapes, the tool names of the repair hook, and a note on a byte-order mark. No function of either side judges an interpreter today. Case 796.1 adds that one function to `guppi/bashguard.py`, and `guppi/powershellguard.py` imports it, so no second copy is written. A Grep `settings\.json|rule-bash-guard|rule-hook-registry|rule-harness|estimate-bash-guard` over `tests/` printed `tests/test_bashguard.py`, `tests/test_guard.py`, `tests/test_ratified.py`, `tests/test_render.py`, `tests/test_glossary.py` and `tests/test_pages.py`. Each one writes its files under a temporary folder or names the slug in a docstring, so no test reads the live pages or the live `.claude/settings.json` that this Case changes. In `tests/test_bashguard.py`, the commands `CLEAN_PIPE` and `NULL_ONLY` feed `python` and are expected to pass, so Case 796.1 changes them. A Glob `vault/**/*powershell*` printed only `vault/archive/migration/2026-10-07/0636/lessons/lesson-session-frontier-rewritten-through-powershell.md`, so both new slugs are free. The lesson is of session 2349, so no decision line carries `{addresses:...}` (case 284.2).

> **problem:**
> An agent can rewrite a source file with a script typed inline and fed to an interpreter in a Bash or PowerShell call, and no check refuses it before it runs. The repair after the call fixes the line endings but not the choice, and the same choice has rewritten a source file in three sessions.

> **recommend:**
> - **Where the fix lives**
>   - Recommended: (a) the check before a Bash call also refuses a heredoc fed into an interpreter.
>   - Answer: (a).
> - **PowerShell calls**
>   - Recommended: (a) Bash only, with the PowerShell gap named as not done.
>   - Answer: (b) Bash and PowerShell.
> - **Where the PowerShell check lives**
>   - Recommended: (a) a new rule beside the Bash one, both checks importing one list of interpreters.
>   - Answer: agreed, (a).
> - **What the PowerShell check refuses**
>   - Recommended: (a) a here-string piped into an interpreter.
>   - Answer: agreed, (a).
> - **A script passed by a flag**
>   - Recommended: (a) leave it out, named as not done.
>   - Answer: agreed, (a).
> - **The section on how the Bash check works**
>   - Recommended: (a) remove the section by hand, once.
>   - Answer: agreed, (a).

### Case 796.1 — The Bash check refuses a heredoc fed into an interpreter

> **given:**
> `guppi/bashguard.py`: the check before a Bash call, and the one judgment of an interpreter.
> **＋** `tests/test_bashguard.py`: the tests of the check.
> **＋** `rule-bash-guard`: the rule of the check; its Purpose changes and its `## How it works` leaves.
> **＋** `estimate-bash-guard`: its Criterion is replaced whole.
> **＋** `rule-harness`: its Purpose names the check by what it refuses.
> **＋** `/dev/null`: the one redirect target that is no file write.
> **＋** `raw/<date>/event_log.md`: the log a refusal is written to.

> **when:**
> The agent calls `Bash`, and `uv run guppi bashguard` on `PreToolUse` reads `tool_input.command` of the payload and finds every heredoc (`<<` or `<<-`, the marker quoted or not) and its body up to the closing line.

> **then:**
> A heredoc whose body holds a backslash, whose marker line writes a file (`>` or `>>` not to `/dev/null`, `tee`), or whose marker line runs an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`) as one of its commands exits 2 with the reason on stderr: `bashguard: heredoc refused — <a backslash in its body | it writes <path> | it feeds <interpreter>>. Write a whole file with the Write tool and change a file with Edit, never through Bash; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
> **＋** Before the refusal one line `- HH:MM:SS <stamp> bashguard refused: <reason>` goes to `raw/<date>/event_log.md`.
> **＋** A `<<<` here-string, a heredoc with no backslash, no file write and no interpreter on its marker line, a command without a heredoc, another tool — exit 0.
> **＋** A payload the hook cannot read — exit 0 with one line on stderr.
> **－** An interpreter that runs a script by path, or takes it by `-c` or `-e`, is no reason to refuse.
> **－** The hook never raises.

```then
update:
- slug: rule-bash-guard
  set:
    purpose: Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool
  sections:
    Purpose: 'Prevents a heredoc from carrying a backslash escape, writing a file or feeding a script to an interpreter through the Bash tool. On this Windows machine the tool''s shell layer interprets backslash escapes inside a heredoc body before the interpreter reads it, whatever the quoting of the marker; three sessions (H, L, M) broke edit scripts that way with the lesson live, and a heredoc that writes a file fails on quotes in its body. A heredoc with neither, fed to Python, rewrote a source file in three more sessions, and `Path.write_text` left CRLF line endings in it (`insight-workflow-file-changed-through-a-shell-command`, `lesson-work-mode-edited-a-source-file-through-the-shell`): a source file changes by Edit, and a script goes into the scratchpad and runs by path. A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. A script run by path or passed by `-c` or `-e` passes. The mechanism stands in the docstring of `guppi/bashguard.py`, and a PowerShell call is the rule `rule-powershell-guard` (cases 127, 796.1).'
  change: a heredoc whose marker line runs an interpreter is refused; How it works removed by hand, a one-off, its facts in the docstring of guppi/bashguard.py (case 796.1)
- slug: estimate-bash-guard
  set:
    status: pending
    purpose: A heredoc with a backslash, a file write or an interpreter it feeds is refused before it runs, with a message that sends the agent to Write and Edit and says the refusal is no finding
  change: the Criterion replaced whole — a heredoc fed into an interpreter is refused (case 796.1)
- slug: rule-harness
  replace:
  - old: the hook that refuses a heredoc with a backslash or a file write,
    new: the hook that refuses a heredoc with a backslash, a file write or an interpreter it feeds,
  change: the Bash guard named with its third reason (case 796.1)
```

```tasks
- [x] `guppi/bashguard.py`: one function judges whether a marker line runs an interpreter of the list, as its first command or after a `|`, `&&`, `||` or `;`, and names it; `refusal` gives `it feeds <interpreter>` after the backslash and the file write; the docstring gains the new reason and keeps every fact of the `## How it works` that leaves the page.
- [x] `tests/test_bashguard.py`: `python - <<'EOF'`, `uv run python - <<EOF` and `cat <<EOF | node` are refused with `it feeds <interpreter>` and logged; `python -c "print(1)"` and `python script.py` pass; `CLEAN_PIPE` and `NULL_ONLY` feed `cat` in place of `python` and still pass.
- [x] `vault/wiki/rules/rule-bash-guard.md`: a one-off in Work Mode, before the librarian's run: the section `## How it works`, heading and text, removed by hand.
- [ ] update `rule-bash-guard`
- [ ] update `estimate-bash-guard`
- [ ] update `rule-harness`
- [ ] read `estimate-bash-guard`
```

### Case 796.2 — A PowerShell check refuses a here-string piped into an interpreter

> **given:**
> `rule-powershell-guard`: the new rule of the check before a PowerShell call.
> **＋** `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`: the new check of the rule.
> **＋** `guppi/powershellguard.py`: the new check.
> **＋** `guppi/bashguard.py`: the one judgment of an interpreter, which the new check imports.
> **＋** `guppi/cli.py`: the command `powershellguard`.
> **＋** `tests/test_powershellguard.py`: the tests of the new check.
> **＋** `rule-hook-registry`: the hook entry on `PreToolUse` of `PowerShell`, rendered into `.claude/settings.json`.
> **＋** `rule-harness`: its Purpose names the new rule.
> **＋** `raw/<date>/event_log.md`: the log a refusal is written to.

> **when:**
> The agent calls `PowerShell`, and `uv run guppi powershellguard` of `guppi/powershellguard.py` on `PreToolUse` reads `tool_input.command` of the payload and finds every here-string: the text from a line that ends with `@'` or `@"` to a line that opens with `'@` or `"@`.

> **then:**
> A here-string whose closing line pipes it into an interpreter (`python`, `python3`, `py`, `uv run python`, `node`, `perl` or `ruby`) exits 2 with the reason on stderr: `powershellguard: here-string refused — it is piped into <interpreter>. Write a whole file with the Write tool and change a file with Edit, never through PowerShell; only a script goes into the scratchpad, written with the Write tool and run by path. The refusal is this guard working as designed, not an event of the session: do not report it at Retro.`
> **＋** Before the refusal one line `- HH:MM:SS <stamp> powershellguard refused: <reason>` goes to `raw/<date>/event_log.md`.
> **＋** `guppi/powershellguard.py` judges the interpreter by the function of `guppi/bashguard.py` that the Bash check calls, and keeps no list of its own.
> **＋** `.claude/settings.json` registers the hook on `PreToolUse` with the matcher `PowerShell`, by the Render of `rule-hook-registry`.
> **＋** A here-string not piped into an interpreter, a command without a here-string, another tool — exit 0; a payload the hook cannot read — exit 0 with one line on stderr.
> **－** A quoted string, a variable or the output of a command piped into an interpreter, a script run by path, and a script passed by `-c` or `-e` are no reason to refuse.
> **－** The hook never raises.

```then
create:
- slug: rule-powershell-guard
  type: rule
  kind: Leaf
  purpose: Prevents a here-string from feeding a script to an interpreter through the PowerShell tool
  enforcement: hook
  implementation_ref:
  - guppi/powershellguard.py
  - tests/test_powershellguard.py
  - .claude/settings.json
  tags:
  - hooks
  - harness
  sections:
    Purpose: Prevents a here-string from feeding a script to an interpreter through the PowerShell tool. A script fed inline to Python rewrote a source file in three sessions, and `Path.write_text` left CRLF line endings in it (`insight-workflow-file-changed-through-a-shell-command`, `lesson-work-mode-edited-a-source-file-through-the-shell`). `rule-bash-guard` refuses such a heredoc before a Bash call; a here-string piped into an interpreter is the same script in PowerShell, and no check saw it before the call. A lesson the agent has to remember is not a rule; a `PreToolUse` hook cannot be skipped. The interpreters are judged by the one function of `guppi/bashguard.py`, so both checks answer alike. A quoted string, a variable or the output of a command piped into an interpreter, a script run by path, and a script passed by `-c` or `-e` pass. The mechanism stands in the docstring of `guppi/powershellguard.py` (case 796.2).
- slug: estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter
  ref: rule-powershell-guard
  kind: QA
  purpose: A here-string piped into an interpreter is refused before a PowerShell call runs, with a message that sends the agent to Write and Edit and says the refusal is no finding
  method: 'uv run pytest tests/test_powershellguard.py; after the librarian''s run of this session renders rule-hook-registry: the PowerShell entry of .claude/settings.json read against the Criterion'
  tags:
  - hooks
  - harness
update:
- slug: rule-hook-registry
  replace:
  - old: '"command": "uv run guppi bashguard", "timeout": 30 } ] },'
    new: |-
      "command": "uv run guppi bashguard", "timeout": 30 } ] },
      { "matcher": "PowerShell",
        "hooks": [ { "type": "command", "command": "uv run guppi powershellguard", "timeout": 30 } ] },
  change: guppi powershellguard registered on PreToolUse of PowerShell (case 796.2)
- slug: rule-harness
  replace:
  - old: Eleven more belong here
    new: Twelve more belong here
  - old: the hook that repairs or names a file a shell call left
    new: the hook that refuses a PowerShell here-string piped into an interpreter, the hook that repairs or names a file a shell call left
  - old: 640, 710.1).
    new: 640, 710.1, 796).
  change: the PowerShell guard named among the rules in no pipeline (case 796.2)
```

```tasks
- [ ] create `rule-powershell-guard`
- [ ] create `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`
- [x] `guppi/powershellguard.py`: the `PreToolUse` hook on `PowerShell`: it finds every here-string, refuses one whose closing line pipes it into an interpreter by the function of `guppi/bashguard.py`, logs the refusal by `guppi.event` before it says it, and never raises; its docstring holds the mechanism.
- [x] `guppi/cli.py`: the command `powershellguard`, and its name in the list of hook commands of the docstring.
- [x] `tests/test_powershellguard.py`: `@'` and `@"` here-strings piped into `python -`, `uv run python -` and `node` are refused with the reason and logged; a here-string piped into `Out-File` or to the screen, a quoted string piped into `python`, `python script.py`, a `Bash` payload and an unreadable payload pass; `cli.main(["powershellguard"])` dispatches to the hook.
- [ ] update `rule-hook-registry`
- [ ] update `rule-harness`
- [ ] `uv run guppi render`: `.claude/settings.json`
- [ ] read `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`
```

## Case 797 — A Case is judged by the state at the moment its check or reading runs

> **context:**
> Every check of a Case file and of the Spec in Plan Mode runs the code as it stands before the Work Mode of the session changes it, and a page or a rendered file changes at the librarian's run or at the render, or earlier only by a one-off task by hand in Work Mode, such as the removal of a section that Case 796.1 makes. The instructions of `case-guppi` do not say this. So the agent can judge a Case by the state at the end of the session. `lesson-case-build-chose-a-key-its-own-session-adds` records one case: Case 787.2 used the key `drop` that Case 792 of the same session would add, and the check of the Case file refused it. `lesson-case-reading-moment-before-the-render-it-reads` has the same cause: the agent set a reading of Case 761 for a moment before the render of the file it reads. Both lessons are `clustered` under `insight-workflow-code-live-before-the-page-it-reads`, which stands `open` in the backlog.
>
> By the person's answers, Case 797.1 adds one sentence to the Render of `rule-case-build`. The sentence makes the agent judge each form a task writes, the moment of a reading and what that reading will find by the state at the moment the check or the reading runs. Where a Case needs a form that another Case of the same session adds, the agent asks the person in a round. The new Estimate `estimate-case-build-judges-by-the-state-at-the-moment` checks this, by hand, once such a Case comes. Its `method` waits for that event in the form of case 781. The insight stays `open`, because `lesson-prespec-preview-expected-before-generate-applies-the-readings` is about the main agent, and this Case does not touch the main agent.
>
> `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` is `passed`. Its last line says that the insight stands `actioned` and leaves the backlog, which has not been true since the synthesis of 2026-10-10 reopened it. Case 797.2 replaces that Criterion whole. The new Criterion copies each other line word for word and drops that line. The `purpose` of that Estimate does not name the insight, so it stands. Its `method`, a reading by hand at a Case that changes a reader and the text it reads, waits for that event but does not name it in the form of case 781, so `rule-retro` would want it read at this session's Retro, where no Case of this session fits. By the findings of `/pre-spec`, Case 797.2 sets the `method` anew in that form, with the same reading, so that Case 799 of this session counts it as waiting.
>
> The frame. The new sentence goes after the sentence on a reader that only goes red, in the paragraph on the frame of the Case. No sentence of `rule-case-build` says to judge by the end state of the session. The sentence on a reader that keeps the old form (case 473.2) covers a reader and its text that land at different moments, and the new sentence agrees with it. The other Estimates of `rule-case-build` speak of other behaviours, so their Criteria stand. Case 795 of this session changes `guppi/materialize.py` and `guppi/prespec.py`, not `rule-case-build`, and the check it changes runs at the same moment as before. A Grep `case-guppi\.md|rule-case-build` over `tests/` printed nothing, so no test reads the agent file or the page live. The new Estimate has a `ref`, so no vault query was run for it, and a Glob `vault/**/estimate-case-build-judges-by-the-state*` printed nothing, so the slug is free.

> **problem:**
> `case-guppi` can build a Case by the state at the end of the session: it can use a form that only the session's own Work Mode makes valid, or time a reading before the text it reads changes. A passed Estimate of `rule-case-build` also states that an open insight is closed.

> **recommend:**
> - **How wide should the new instruction to `case-guppi` be?**
>   - Recommended: (b) every judgment about a moment: the form a check reads, the moment of a reading and what it will find, judged by the state at that moment.
>   - Answer: agreed, (b).
> - **What should `case-guppi` do when a Case needs a form that another Case of the same session adds?**
>   - Recommended: (b) ask the person in a round, with the form the code accepts now as a possible recommended answer.
>   - Answer: agreed, (b).
> - **What should happen to the group page and to the out-of-date line about it?**
>   - Recommended: (a) remove the line from the Criterion of the Estimate and read it again; the insight stays open.
>   - Answer: agreed, (a).
> - **How should the new instruction be checked?**
>   - Recommended: (a) a new Estimate, read by hand when such a Case comes up.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by the findings of `/pre-spec`, the new sentence names a one-off task by hand in Work Mode, such as the removal of a section in Case 796.1, as a way a page changes before the librarian's run; and the `method` of `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` names its event in the form of case 781.
>   - Taken: the sentence of Case 797.1 and `context` name such a task; Case 797.2 sets the `method` anew as `by hand, after` the first such Case, with the same reading.

### Case 797.1 — case-guppi judges a Case by the state at the moment its check or reading runs

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, gains the sentence.
> **＋** `estimate-case-build-judges-by-the-state-at-the-moment`: the new check of the sentence.
> **＋** `rule-case-check`: the check of the Case file, which runs the code as it stands.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case whose task writes a form of an update or whose Estimate sets the moment of a reading, while another Case of the same session changes the code that judges that form or the page or file that reading reads.

> **then:**
> `case-guppi` judges the form, the moment of the reading and what the reading will find by the state of the code and the pages at the moment the check or the reading runs, not by the state at the end of the session.
> **＋** A task of the Case writes only a form of an update that the code accepts when the check of `rule-case-check` runs.
> **＋** Where the Case needs a form of an update that another Case of the same session adds, `case-guppi` asks the person in a round whether the Case uses a form the code accepts now or leaves that change to a Case of a later session.

```then
create:
- slug: estimate-case-build-judges-by-the-state-at-the-moment
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi judges the forms, the moments of readings and what they will find by the state of the code and the pages at the moment the check or the reading runs, and asks the person when a Case needs a form another Case of the same session adds
  method: 'by hand, after case-guppi builds a Case whose form or reading depends on another Case of the same session: the Case file, or the round before it, read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: 'A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`.'
    new: 'A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`. Each check of your file and of the Spec runs the code as it stands when it runs, in Plan Mode before the Work Mode of the session changes it, and a page or a rendered file changes at the librarian''s run or the render, or earlier only by a one-off task by hand in Work Mode that a Case names: judge each form a task writes, the moment of a reading and what that reading will find by the state of the code and the pages at the moment the check or the reading runs, never by the state at the end of the session; where a Case needs a form of an update that another Case of the same session adds, ask in a round whether the Case uses a form the code accepts now or leaves that change to a Case of a later session (case 797.1).'
  change: case-guppi judges a Case by the state of the code and the pages at the moment its check or reading runs, and asks in a round when a Case needs a form another Case of the session adds (case 797.1)
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] create `estimate-case-build-judges-by-the-state-at-the-moment`
- [ ] read `estimate-case-build-judges-by-the-state-at-the-moment`
```

### Case 797.2 — The Criterion of the old-form Estimate no longer states the insight closed

> **given:**
> `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`: its Criterion is replaced whole.
> **＋** `rule-case-build`: the rule whose Estimate it is.
> **＋** `rule-retro`: the rule whose handoff note takes the red of a reader that only goes red.

> **when:**
> `case-guppi` builds a Case that changes a reader in code and the text or the writer that reader reads, where the reader runs from the working tree at once and the text lands at the librarian's run or the render.

> **then:**
> Where the reader refuses in between and what it refuses is lost, such as a hook that refuses a ledger line, the `then` of the Case says that the reader accepts the old form beside the new one until a reading of the writer passes live.
> **＋** The removal of the old form is left to a Case of a later session, after that reading.
> **－** A reader that only goes red, such as `make lint`, keeps no old form: its red is a note for the handoff by `rule-retro`.

```then
update:
- slug: estimate-case-build-keeps-the-old-form-until-the-writer-is-live
  set:
    status: pending
    method: 'by hand, after the first Case case-guppi builds that changes a reader in code and the text or the writer it reads: the then of that Case read against the Criterion, recorded in the estimate line'
  change: the Criterion replaced whole — the line that put the insight actioned is dropped, since the insight was reopened; the method names its event (case 797.2)
```

```tasks
- [ ] update `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
- [ ] read `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`
```

## Case 798 — case-guppi reads the governing rule and the last output of a check before it recommends an option

> **context:**
> `case-guppi` reads the rule that a text breaks, and judges each option of its round against it, only when the item reports a defect (case 780). On any other item, nothing tells it to read the rule that governs what an option changes, or what a check printed at its last run. Case 787 shows where this goes wrong. It was a new feature, so the defect-only sentence did not apply. The agent recommended `style`, `test` and `lint` as required checks on `main` and read neither the lint lines of the Baseline nor `rule-lint`, whose Purpose calls red a signal, not a gate. Lint was red on GitHub, no outside pull request could merge, and Case 794 replaced 787.1. `lesson-case-build-made-an-always-red-check-required` records this. With `lesson-case-build-recommended-a-trigger-that-keeps-the-defect`, it is `clustered` under `insight-case-build-recommends-without-reading-the-governing-rule`, which stands `open` in `backlog.md`.
>
> By the person's answers, Case 798.1 widens the case 780 sentence in the Render of `rule-case-build` from defect items to every item, and adds that `context` names the rule. It also replaces the Criterion and the `purpose` of `estimate-case-build-judges-options-against-the-broken-rule`. That Estimate is `passed` and its Criterion covers only an item that reports a defect. The new Criterion does not carry three lines of the old one: its `When` on an item that reports a defect, its first `Then` line on the rule the defect breaks, and its line on an option that leaves a part of the text breaking the rule. Each is replaced by a wider line that covers every item and still names the defect case, so no part of the old promise is lost. Its `method`, a reading of the new Render in the Spec at the Retro of the session, states no promise and stands. Case 798.2 adds a sentence: where an option rests on whether a check passes, `case-guppi` reads what that check printed at its last run, as the brief reports it. The new Estimate `estimate-case-build-reads-the-last-output-of-a-check` checks this. Plan Mode cannot run `make lint`. The librarian writes its last lines under `## Flags` of `vault/wiki/brief.md` and the counts of `make test` and `make lint` under `## Readings at the close`, as `rule-brief` sets. Case 798.1 sets the insight `actioned`, since the two sentences together change the step that both lessons blame. The Criteria do not state the insight, because Case 797.2 had to remove such a stale line from another Estimate of `rule-case-build`.
>
> The frame. In the Render of `rule-case-build`, the one sentence that states this behaviour is the case 780 sentence. Other sentences speak of contradictions in pages and of what done means. The change leaves them true. The Criteria of the other Estimates of `rule-case-build` speak of other behaviours, so they stand. Case 797.1 of this session adds one sentence to the frame paragraph of the same Render, and this Case changes the next paragraph. No pair of the two Cases shares a sentence. The two sentences part where another Case of the session changes the check or the pages it reads. The last output in the brief is the state at the librarian's last run. Case 797.1 judges by the state when the check runs. This session holds such Cases: Case 795.1 clears the `orphan` line of `rule-github-repository` from `make lint`, and Case 799 drops the `unread: pending` line of an Estimate whose `method` waits for a later moment. So the new sentence of Case 798.2 says that, where another Case of the session changes the check or the pages it reads, the sentence of Case 797.1 holds (pre-spec finding). Under `rule-raw-archive`, the librarian moves an applied session whole into `vault/archive/`, and the Render of `rule-case-build` opens `vault/archive/` by slug only. A handoff has no slug, so the handoff of the last session is often out of reach. The person chose the brief alone as the source of the last output. A Grep `reports a defect|rule the defect breaks|governing rule` over `vault/wiki/` and `.claude/` printed `.claude/agents/case-guppi.md`, `vault/wiki/rules/rule-case-build.md` and `vault/wiki/estimates/estimate-case-build-judges-options-against-the-broken-rule.md`. This Case changes all three. A Grep `estimate-case-build-judges-options-against-the-broken-rule|insight-case-build-recommends-without-reading-the-governing-rule` over the repository outside `vault/raw/` and `vault/archive/` printed six files. `vault/wiki/brief.md` and `vault/wiki/log.md` were not read. `uv run guppi backlog` writes `vault/wiki/backlog.md` again from the open Insights at the librarian's run. The `estimates` list of `vault/wiki/rules/rule-case-build.md` stands. The `insight` field of the two lessons stands until the cascade of `generate` archives them. A Grep `case-guppi\.md|rule-case-build|judges-options-against-the-broken-rule` over `tests/` printed nothing, so no test reads the agent file or the pages live. The new Estimate has a `ref`, so no vault query was run. A Glob `vault/**/estimate-case-build-reads-the-last-output*` printed nothing, so the slug is free.

> **problem:**
> `case-guppi` can recommend an option that breaks the rule governing what the option changes, or that rests on a check that is red today. It reads the governing rule only on an item that reports a defect, and it never reads the last output of a check. A Case built on such a recommendation has to be replaced.

> **recommend:**
> - **What must `case-guppi` read before it recommends an option?**
>   - Recommended: (b) on every item, the rule that governs what each option changes, and, where an option rests on whether a check passes, what that check printed at its last run, as the brief reports it; `context` names both.
>   - Answer: agreed, (b).
> - **What happens to the group page of the two lessons?**
>   - Recommended: (a) this Case sets the group page `actioned`.
>   - Answer: agreed, (a).
> - **How is the new instruction checked?**
>   - Recommended: (a) two parts: widen the Criterion of the existing check to every item, and add a new check for the last output of a check.
>   - Answer: agreed, (a).
> - **When is each check read?**
>   - Recommended: (a) at this session's Retro, on the new instruction text.
>   - Answer: agreed, (a).
> - **What if the brief shows no output for the check an option rests on?**
>   - Recommended: (a) look in the brief and the handoff of the last session; where neither shows it, the `**After:**` line of the option and `context` say so, and the option may still be recommended.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: by a finding of `/pre-spec`, the person agreed that `case-guppi` reads the last output of a check only in the brief, the `make lint` lines under `## Flags` and `make test` under `## Readings at the close`, since the handoff of the last session is usually moved to the archive; where the brief shows none, the option and `context` say so.
>   - Taken: Case 798.2 drops the handoff from its sentence, `given`, `then` and the `purpose` of its Estimate.
> - **Change**
>   - Asked: by a finding of `/pre-spec`, the sentence of Case 798.2 must not contradict the sentence of Case 797.1 where another Case of the session changes the check or the pages it reads.
>   - Taken: the sentence and the `then` of Case 798.2 say that, in that case, the option is judged by the state at the moment the check runs, as Case 797.1 sets it; `context` no longer claims that the last output is that state.

### Case 798.1 — case-guppi reads the governing rule on every item

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, widens the sentence on the rule a defect breaks.
> **＋** `estimate-case-build-judges-options-against-the-broken-rule`: its Criterion and `purpose` are replaced.
> **＋** `insight-case-build-recommends-without-reading-the-governing-rule`: set `actioned`.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of the `**After:**` line of an option.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case on a Frontier item and writes a round with options.

> **then:**
> Before it recommends an option, it finds the rule that governs what each option changes, or the rule the defect breaks where the item reports a defect, and reads the passage of that rule, which it names in the `context`.
> **＋** It judges each option of the round against that rule over the whole text the option leaves; for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes.
> **＋** An option that breaks that rule, or leaves a part of that text breaking it, may stand in the round; its `**After:**` line names that part, and `case-guppi` does not recommend that option.
> **－** The `**After:**` line keeps the form of `.claude/skills/grill-me/SKILL.md`: the part left is a plain sentence inside its text.

```then
update:
- slug: rule-case-build
  replace:
  - old: 'When the item reports a defect — a text that breaks a rule — find the rule it breaks and read its passage, and judge each option of your round against that rule over the whole text the option leaves: for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes; an option that leaves a part of that text breaking the rule may stand, its `**After:**` line names that part in a plain sentence, and you do not recommend it (case 780).'
    new: 'On every item, before you recommend an option, find the rule that governs what each option changes — where the item reports a defect, a text that breaks a rule, the rule it breaks — and read its passage, and judge each option of your round against that rule over the whole text the option leaves: for a Criterion, each line of its `When` and `Then` and its `method`, not only the words the item quotes; an option that breaks the rule, or leaves a part of that text breaking it, may stand, its `**After:**` line names that part in a plain sentence, and you do not recommend it; `context` names the rule (cases 780, 798.1).'
  change: case-guppi reads the rule that governs what each option changes on every item, not only on an item that reports a defect, and context names it (case 798.1)
- slug: estimate-case-build-judges-options-against-the-broken-rule
  set:
    status: pending
    purpose: Whether case-guppi, on every item, finds the rule that governs what each option of its round changes, the rule a defect breaks where the item reports one, judges each option against it over the whole text the option leaves, names in the After line of an option the part it leaves breaking the rule without recommending it, and names that rule in context
  change: the Criterion and purpose replaced whole — the rule that governs what an option changes is read on every item, not only on an item that reports a defect (case 798.1)
- slug: insight-case-build-recommends-without-reading-the-governing-rule
  set:
    status: actioned
    addressed_by: decision-case-798.1
  change: 'actioned: case-guppi reads the rule that governs what each option changes on every item, and the last output of a check an option rests on (cases 798.1, 798.2)'
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] update `estimate-case-build-judges-options-against-the-broken-rule`
- [ ] update `insight-case-build-recommends-without-reading-the-governing-rule`
- [ ] read `estimate-case-build-judges-options-against-the-broken-rule`
```

### Case 798.2 — case-guppi reads the last output of a check an option rests on

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, gains the sentence on the last output of a check.
> **＋** `estimate-case-build-reads-the-last-output-of-a-check`: the new check of the sentence.
> **＋** `vault/wiki/brief.md`: its `## Flags` and `## Readings at the close` hold the last output of `make lint` and `make test`.
> **＋** `rule-brief`: the rule that writes those sections at the librarian's run.
> **＋** `.claude/skills/grill-me/SKILL.md`: the form of the `**After:**` line of an option.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, writes a round with an option that rests on whether a check passes, such as `make lint`, `make test` or a check on GitHub.

> **then:**
> Before it recommends that option, it reads what that check printed at its last run, as `## Flags` and `## Readings at the close` of `vault/wiki/brief.md` report it, judges the option against that output, and quotes it with its source in the `context`.
> **＋** Where another Case of the same session changes that check or the pages it reads, it judges the option by the state at the moment the check runs, as `rule-case-build` sets it for such a Case, and not by the last output alone.
> **＋** Where the brief does not report that output, the `**After:**` line of the option and the `context` say that its last output was not read.
> **－** An option whose last output was not read may still be recommended.

```then
create:
- slug: estimate-case-build-reads-the-last-output-of-a-check
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi, before it recommends an option that rests on whether a check passes, reads what that check printed at its last run, from the brief, judges the option against it, or by the state at the moment the check runs where another Case of the session changes the check or the pages it reads, and names it in context, or says in the After line and context that the output was not read
  method: 'by hand at the Retro of this session: the new Render of rule-case-build in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line'
  tags:
  - session
  - workflow
  - harness
update:
- slug: rule-case-build
  replace:
  - old: 'Each Case and sub-case answers what done means and how it is checked:'
    new: 'Where an option rests on whether a check passes, such as `make lint`, `make test` or a check on GitHub, read before you recommend it what that check printed at its last run, as `## Flags` and `## Readings at the close` of `vault/wiki/brief.md` report it, and judge the option against that output; where another Case of the session changes that check or the pages it reads, judge the option by the state at the moment the check runs, as the paragraph on the frame sets it (case 797.1); `context` names that output, and where the brief does not report it, the `**After:**` line of the option and `context` say that its last output was not read, and the option may still be recommended (case 798.2). Each Case and sub-case answers what done means and how it is checked:'
  change: case-guppi reads what a check printed at its last run, from the brief, before it recommends an option that rests on that check (case 798.2)
```

```tasks
- [ ] update `rule-case-build`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] create `estimate-case-build-reads-the-last-output-of-a-check`
- [ ] read `estimate-case-build-reads-the-last-output-of-a-check`
```

## Case 799 — Lint does not mark red a check whose reading waits for a later moment

> **context:**
> `make lint` prints one red line for each Estimate that stands `pending` or `failed`, whatever its reading waits for, and the run fails when any line is printed, on GitHub too. The Purpose of `rule-lint`, the rule that governs this, says that a `pending` Estimate is red until its reading (case 182). Under `## Flags` of `vault/wiki/brief.md`, the librarian's last run printed `make lint, 12 lines`. Ten of them are `unread: pending` lines of Estimates whose `method` names a later moment: an event, such as the first `/merge-main` that leaves a conflicted page, a session of the sprint `plugin` before its close, the session that closes it, or the session after a close. Most of these lines cannot be cleared before their moment, so the same lines come back in every brief. Lint never finds the event either. It judges the words of a `method`, not whether its moment has come. That is the brief's job. By `rule-brief`, the librarian lists every `pending` or `failed` Estimate under Readings due at each run, looks for the event a `method` waits for in `git log`, the ledger, the handoff and the files the `method` names, and puts the reading under `Work` once it sees the event. A reading of the live sprint page waits for the Retro of the session that finishes its work, or for the closing Case of `/sprint-close`, which puts each Estimate that is still unread to the person. The short brief that `carry` writes has no Readings due. The next run of the librarian writes the full list again, so this gap stands.
>
> By the person's answers, lint gives no `unread` finding for a `pending` Estimate when any part of its `method` waits for a later moment. It stays red for a `failed` Estimate and for a `pending` one whose `method` has no such part. A reading is recorded once, as a whole, so it cannot be taken before its latest part. Lint does not tell whether the moment has come. A reading whose event has come is put up by the `Work` list of the brief, not by lint. `estimate-ask-finds` is such a reading: its event has come, the brief puts it under `Work`, and lint leaves it out. The same holds for `estimate-hi-writes-frontier`, whose second part, a test, could run now, while its first part waits for the close of the sprint. A part of a `method` between two `;` waits for a later moment when it opens with `after`, or with `by hand, after`, and names its event before a colon, or when it names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`. Over the methods of the ten Estimates, as the pages hold them, each one has such a part. The Purpose of `rule-lint` changes its sentence on red. Its first sentence, on a reading that nobody took, stays true. Lint still marks a `pending` Estimate red when no part of its `method` waits for a later moment, and the `Work` list of the brief puts up a reading whose moment has come, so no such page sits unnoticed. The Criterion and the `purpose` of `estimate-lint-checks-the-statuses` state the old promise, so this Case replaces both, and the Criterion carries over its lines on `status` and `deferred` word for word. Two lines of the old Criterion are not carried, on purpose. Its `When` now names the `method` of each Estimate too, since the new judgment reads it. Its `unread` line, on every Estimate that is `pending` or `failed`, is replaced by the lines on a `failed` Estimate, on a `pending` one whose `method` has no part that waits for a later moment, and on a `method` that waits for a later moment. Its `method`, `uv run pytest tests/test_lint.py`, states no promise and stands. The Criteria of the other Estimates of `rule-lint` speak of other classes, so they stand.
>
> Two of the red lines are left to other Cases. The `orphan` line of `rule-github-repository` goes by Case 795.1 of this session, which changes pages and not the code of lint. The person chose to take up the line `rules/rule-morph: deferred: 4 times since case 239` as an item of its own, so this Case leaves it out. The person also chose to read `estimate-git-context-current` in Work Mode of this session. Its method waits for the first `/hi` after the first push to GitHub. The brief says that `main` and `plugin` were pushed in session 2349, so the `/hi` of this session is that moment, and a later session would miss it.
>
> One judgment. A Grep `ANOTHER_SESSION|waits_for_an_event|waits_for_another_session` over `guppi/` printed `guppi/lint.py` and `guppi/prespec.py`. In `guppi/lint.py`, `waits_for_an_event` judges a part that waits for an event it names, and `ANOTHER_SESSION` is the pattern of a later session. The new predicate of `guppi/lint.py` calls both, so it adds no second copy of either. `guppi/prespec.py` imports `waits_for_another_session`, which judges something else: whether a `method` breaks the limit to its own session. It is false for a part that names an event or the person, since those parts are allowed. The new predicate is true for both, since such a reading still waits. The two answer different questions on purpose, so neither stands for the other. The librarian makes its judgment of an event in prose, as an agent, so there is no code for a test to run beside lint. A Grep `waits for|later session` over `guppi/` printed `guppi/lint.py`, `guppi/ledger.py`, `guppi/box.py`, `guppi/gate.py`, `guppi/casecheck.py`, `guppi/prespec.py`, `guppi/generate.py` and `guppi/spec.py`. Outside `guppi/lint.py` and `guppi/prespec.py`, no hit judges the `method` of an Estimate.
>
> Tests and texts. A Grep `unread: (pending|failed)` over `tests/` printed `tests/test_lint.py` and `tests/test_generate.py`. Their Estimates carry the method `pytest tests/test_x.py`, which waits for nothing, so their `unread` lines stand. A Grep `rule-lint|estimate-lint-checks-the-statuses|estimate-git-context-current` over `tests/` printed `tests/test_lint.py`, whose only hit is its docstring. It seeds its pages under a temporary folder, so no test reads a page this Case changes. A Grep `\bunread\b|red until` over `vault/wiki/` and `.claude/` printed 19 files under `vault/wiki/` and `.claude/skills/sprint-close/SKILL.md`. `brief.md` and `log.md` were not read. `rule-lint` and `estimate-lint-checks-the-statuses` change here. The pages of the sprint close and their Estimates speak of an Estimate that a close carries or archives unread. That is a status, not a line of lint. The other hits stand in a Result or a History line. So the change makes none of them false.

> **problem:**
> `make lint` marks red every Estimate that is not yet read, also one whose reading cannot be taken before a later event or session. The same red lines are carried from session to session, and lint stays red on GitHub, though most of them cannot be cleared before their moment.

> **recommend:**
> - **What should lint do with a pending check that waits for a later event?**
>   - Recommended: (a) lint leaves out a check whose reading waits for a later moment; the brief still lists it under Readings due and moves it to Work when its event comes, and the sprint close still puts each one left to the person.
>   - Answer: agreed, (a), after the person asked how such an event is found later and what shows that an Estimate has not passed.
> - **Should the check of the git context be read in this session?**
>   - Recommended: (a) read it in this session's Work Mode.
>   - Answer: agreed, (a).
> - **What happens to `rule-morph`, the decision that keeps being put off?**
>   - Recommended: (a) take it up as its own item in this session; this Case leaves it out.
>   - Answer: (a), added as a separate item.
> - **Must every part of a check's method wait before lint leaves it out, or is one waiting part enough?**
>   - Recommended: (b) one waiting part is enough, since a check is read once as a whole; the brief's Work list, not lint, puts up a reading whose moment has come.
>   - Answer: agreed, (b).
> - **Change**
>   - Asked: rewrite the two places of `context` that still spoke of a reading that is due, to the rule as it works.
>   - Taken: `context` now says that lint marks a `pending` Estimate red only when no part of its `method` waits, and that the `Work` list of the brief puts up a reading whose moment has come.

> **given:**
> `guppi/lint.py`: `check_unread`, and the new predicate of a `method` that waits for a later moment.
> **＋** `tests/test_lint.py`: the tests of the class `unread`.
> **＋** `rule-lint`: the rule of lint, whose Purpose says when a `pending` Estimate is red.
> **＋** `estimate-lint-checks-the-statuses`: its Criterion and `purpose` are replaced.
> **＋** `rule-brief`: the brief lists every `pending` Estimate under Readings due and puts a reading under `Work` once its event comes.
> **＋** `estimate-git-context-current`: read by its method in Work Mode of this session.
> **＋** `vault/wiki/`: the live pages that lint reads.
> **＋** `/hi`: the skill that opens a session, a moment that a `method` may name.

> **when:**
> `uv run guppi lint` reads the `status` of the live pages under `vault/wiki/` and the `method` of each Estimate.

> **then:**
> `status`: a `built` entity or rule with an Estimate not `passed`, a `draft` one with every Estimate `passed`; a page without Estimates is not judged.
> **＋** `status`: an Estimate `passed` or `failed` without `## Result`; an Estimate whose `target` is not an entity or a rule, or does not list it in `estimates`.
> **＋** `unread`: every Estimate `failed`, and every Estimate `pending` whose `method` does not wait for a later moment, one finding each, `unread: <status>`.
> **＋** A `method` waits for a later moment when a part of it between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon, or names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi`.
> **＋** `deferred`: a placeholder — a rule or entity with `deferred_by` and none of `kind`, `estimates`, `tags` — earns one finding `deferred: <N> times since case <M>` in place of its `schema` findings on those fields and of `orphan`; a page with `deferred_by` whose fields are in place earns none.
> **－** A `pending` Estimate whose `method` waits for a later moment earns no `unread` finding.
> **－** A `failed` Estimate earns its `unread` finding whatever its `method` says.

```then
update:
- slug: rule-lint
  replace:
  - old: a `pending` Estimate is red until its reading (case 182, point 13), and a placeholder is red
    new: a `pending` Estimate is red until its reading, but for one whose `method` waits for a later moment — an event it names, a later session, a session of a sprint, the session that closes one, the librarian or `/hi` — since the brief lists it under Readings due and puts it under Work once its moment comes, and a `failed` one is red until it is read again (cases 182, 799); a placeholder is red
  change: a pending Estimate whose method waits for a later moment is no longer red; a failed one still is (case 799)
- slug: estimate-lint-checks-the-statuses
  set:
    status: pending
    purpose: A status its Estimates do not support, a failed Estimate, a pending Estimate whose reading does not wait for a later moment, and a placeholder are findings of lint
  change: the Criterion and purpose replaced whole — a pending Estimate whose method waits for a later moment earns no unread finding (case 799)
```

```tasks
- [x] `guppi/lint.py`: a new predicate, `waits_for_a_later_moment`, is true when a part of a `method` between two `;` waits for an event by `waits_for_an_event`, or names a later moment by `ANOTHER_SESSION`; `check_unread` gives no finding for a `pending` Estimate whose `method` it holds; the docstring of the class `unread` says so.
- [x] `tests/test_lint.py`: tests whose names hold `unread`: a `pending` Estimate whose method waits for an event before a colon, one whose method names a session of a sprint before its close and one whose method names the session after a close give no finding; a `pending` one whose method is a reading at the Retro of its own session, and a `failed` one whose method waits for an event, each give `unread`.
- [ ] update `rule-lint`
- [ ] update `estimate-lint-checks-the-statuses`
- [ ] read `estimate-lint-checks-the-statuses`
- [x] by hand, in Work Mode of this session: `estimate-git-context-current` read by its method — the context of the first turn of this session's `/hi`, the output of `git remote -v` and `.claude/skills/hi/SKILL.md` against its Criterion; the main agent writes the estimate line.
```
