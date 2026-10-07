## Case 726 — The check of pre-spec notes a page that one Case changes and another puts off

> **context:**
> At `/pre-spec` one `ask-guppi` agent reads the plan once, at the first run of the session. The Render of `rule-prespec` tells it that a Case of the plan that changes a page another Case of the plan defers is a finding (case 186.2). A later run dispatches no `ask-guppi`, and `guppi prespec --check` has no such check. At the `/pre-spec` of session 1804 the person put off Cases 720 and 721 during the loop, after the one `ask-guppi` run, as the handoff of that session records. Case 721 put off `rule-orchestration` and `rule-case-protocol`, which Cases 713 and 717.1 of the same plan update, and nothing reported the pair. The handoff told the librarian to apply the updates and let the defer add `deferred_by`, so the pair did no harm there. In this session Case 722.3 updates `rule-case-protocol` and puts it off again in the same sub-case, on purpose.
>
> Case 726.1 makes `guppi prespec --check` print a `note:` line for such a pair at every run, a change and a defer inside one top-level Case aside. A note sets no exit code, so the hook of `rule-prespec-hook` does not block the exit on it. `split_cases` of `guppi/materialize.py` reads every Case heading of the plan, so a short Case under `## Deferred` is read too. The note is printed by `plan_findings` of `guppi/prespec.py` alone. `guppi/casecheck.py` imports `promise_notes`, not the new judgment, so the check of the file of a Case prints no such note. With the one exception, the plan of this session gives no such note: 722.3 holds both its change and its defer. Case 726.1 creates its own Estimate. `estimate-prespec-notes-a-long-chain` checks another note, and `estimate-prespec-hook-gates` says only that a `note:` line does not block; its Criterion stands.
>
> Case 726.2 takes the pair off the list of what `ask-guppi` judges. It rewrites the sentence of the Render of `rule-prespec`, and it replaces whole the Criterion of `estimate-prespec-reconciles`, whose last line says the pair is still a finding. That Criterion is carried whole but for that line, which the check of this file notes as not carried. The same check notes that the dispatch line of 726.2 shares most of the words of two `then` lines of 726.1. All three lines speak of `## Deferred` and of `defer` items, but the dispatch line sets what `ask-guppi` reads and the two lines set what the script notes, so they stay as they are. Its `method` reads the new Render against the Criterion and does not state the old promise, so it stands; the page has no `purpose` field. The dispatch keeps the instruction that `ask-guppi` reads the slugs of the `defer` items of a Case under `## Deferred`, since its first question still asks whether the Cases contradict each other. A Grep of `another Case of (this|the) plan defers` over `vault/wiki/` printed `vault/wiki/rules/rule-prespec.md` and `vault/wiki/estimates/estimate-prespec-reconciles.md`, and over `.claude/` it printed `.claude/skills/pre-spec/SKILL.md`, the Render of `rule-prespec`. Each enters this Case. The `context` of Case 722 and of Case 725 of this session say that `/pre-spec` calls such a pair a finding. They stand: they give the reason for a choice made under the rule as it stood, and a note still shows such a pair.

> **problem:**
> A Case that changes a page which another Case of the same plan puts off is judged only by the one `ask-guppi` run at the first `/pre-spec`. A defer added later in the loop is never checked, and a pair the person wants is called a finding.

> **recommend:**
> - **Who reports a page that one Case changes and another Case puts off**
>   - Recommended: (b) the script reports it as a note at every run; it does not block the exit from Plan Mode.
>   - Answer: agreed, (b).
> - **A Case that changes a page and puts the same page off itself**
>   - Recommended: (a) no note when the change and the put-off stand in one Case; a Case with sub-cases counts as one.
>   - Answer: agreed, (a).
> - **Whether the helper agent still judges the pair**
>   - Recommended: (a) only the script judges it; the sentence leaves the instructions of the helper agent, and its check gets its last line rewritten.
>   - Answer: agreed, (a).
> - **What checks that the note works**
>   - Recommended: (a) a new check of its own, `estimate-prespec-notes-a-page-another-case-defers`, read by a test in this session.
>   - Answer: agreed, (a).

### Case 726.1 — The check prints a note for a page one Case changes and another puts off

> **given:**
> `estimate-prespec-notes-a-page-another-case-defers`: the new check of this note.
> **＋** `rule-prespec`: the rule of `/pre-spec`, whose check prints the notes.
> **＋** `guppi/prespec.py`: `plan_findings`, which gathers the notes of `--check`, and the module docstring, which says what the check compares.
> **＋** `tests/test_prespec.py`: the tests of the check on a made-up plan.
> **＋** `rule-prespec-hook`: the `ExitPlanMode` hook, which a note does not block.
> **＋** `guppi/casecheck.py`: the check of the file of a Case, which imports other notes of `guppi/prespec.py`.

> **when:**
> `uv run guppi prespec --check` reads the plan file of the session, where the `then` block of one Case holds a `defer` item of a page and the `then` block of another top-level Case holds a `create`, `update` or `delete` item of the same page.
> **＋** Or `tests/test_prespec.py` runs it over a made-up plan.

> **then:**
> The check prints one line that opens with `note:` for each page and pair of Cases, and it names the Case that changes the page, the page and the Case that puts it off.
> **＋** A short Case under `## Deferred` of the plan file counts as a Case that puts the page off.
> **＋** The note is no finding: it does not change the exit code, and the hook of `rule-prespec-hook` does not block the exit from Plan Mode on it.
> **＋** The agent answers the note in one line in the chat, and the person may change a Case or keep the pair.
> **－** A Case and its sub-cases are one Case here: a change and a defer of one page inside one top-level Case give no note.
> **－** A page that only `defer` items name gives no note.
> **－** The check of the file of a Case by `guppi/casecheck.py` prints no such note.

> **tasks:**
> - [ ] create `estimate-prespec-notes-a-page-another-case-defers`
>   - ref: `rule-prespec`
>   - kind: `QA`
>   - purpose: `Whether guppi prespec --check prints a note, at every run and without blocking, for a page that one Case of the plan changes and another top-level Case of the plan puts off`
>   - method: `uv run pytest tests/test_prespec.py -k defers_a_page`
>   - tags: `[session, workflow, harness]`
> - [ ] `guppi/prespec.py`: a note function, called by `plan_findings`, prints one `note:` line per page that a `defer` item of one top-level Case and a `create`, `update` or `delete` item of another top-level Case name; the module docstring says so under its notes.
> - [ ] `tests/test_prespec.py`: `defers_a_page` tests — an update of a page and a defer of it under two Cases give one note and exit 0; a short Case under `## Deferred` gives the same note; an update and a defer under two sub-cases of one Case give none.
> - [ ] read `estimate-prespec-notes-a-page-another-case-defers`

> **ratification:**
> ```
> - decision[case 726.1][create][estimate-prespec-notes-a-page-another-case-defers]{ref:rule-prespec}{tags:session,workflow,harness}
> ```

### Case 726.2 — ask-guppi no longer judges a page one Case changes and another puts off

> **given:**
> `rule-prespec`: its Render sets what `ask-guppi` judges at `/pre-spec`.
> **＋** `.claude/skills/pre-spec/SKILL.md`: the file rendered from `rule-prespec`.
> **＋** `estimate-prespec-reconciles`: its Criterion is replaced whole.
> **＋** `rule-ask` and `.claude/agents/ask-guppi.md`: the agent dispatched at the first run, and its rendered file.
> **＋** `rule-spec-write` and `vault/raw/<date>/<hi HHMM>/frontier.md`: the hook that writes a Case built again into the plan, and the Frontier of the session.
> **＋** `rule-skill-hi`: the rule that sets the title line of a plan that names a conserved Spec.
> **＋** `estimate-prespec-notes-a-page-another-case-defers`: the check of the note that now holds the pair.

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

> **then:**
> The agent runs `uv run guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in `vault/raw/<date>/<hi HHMM>/frontier.md` or in a line of the session's ledger is fixed there, and the command runs again until it prints no finding.
> **＋** At the first run of `/pre-spec` in the session, the agent dispatches one `ask-guppi` over the plan, or over the conserved Spec that the plan's title line names, as `rule-skill-hi` sets that line, with the absolute path of the plan file, the instruction to judge every Case outside `## Deferred` with its sub-cases, and the instruction to read for each such Case its `context`, `when`, `then` and `then` block and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
> **＋** Three questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out.
> **＋** The agent answers the findings with one report before any Case is sent back: the list of what the `ask-guppi` run did not check; each finding numbered, with the fix it proposes or why it is already known, the findings that need the person apart from those that do not, and the decisions it needs from the person; after the Cases built again on the findings are ratified, it does not call `/pre-spec` again, but runs the check, fixes what it prints, and exits Plan Mode when the check prints no finding.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call.
> **－** No second `ask-guppi` is dispatched at the first run, and a later run of `/pre-spec` in the session dispatches none.
> **－** The report never says that the whole Spec is checked.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read, and `ask-guppi` is not asked whether a Case changes a page that another Case of the plan defers: `uv run guppi prespec --check` notes such a pair at every run, as `estimate-prespec-notes-a-page-another-case-defers` sets it.

> **tasks:**
> - [ ] update `rule-prespec`
>   - old: `A Case of this plan that changes a page another Case of this plan defers is still a finding (case 186.2).`
>   - new: `` A Case of this plan that changes a page another Case of this plan defers is no question for `ask-guppi`: the check prints such a pair as a `note:` line at every run, a change and a defer inside one top-level Case aside (cases 186.2, 726.1). ``
>   - change: `a page one Case changes and another Case puts off is a note of the check, no longer a finding of ask-guppi (case 726.2)`
> - [ ] update `estimate-prespec-reconciles`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — ask-guppi is not asked about a page one Case changes and another puts off; the check notes it (case 726.2)`
> - [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
> - [ ] read `estimate-prespec-reconciles`

> **ratification:**
> ```
> - decision[case 726.2][update][rule-prespec]{ref:rule-prespec}
> - decision[case 726.2][update][estimate-prespec-reconciles]{ref:rule-prespec}
> ```
