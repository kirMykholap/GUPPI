## Case 948 — case-guppi reads each text that lists the members of a list it adds to

> **context:**
> `estimate-case-build-reads-the-readers-of-a-changed-step` checks the sentence of case 924 in the Render of `rule-case-build`: a Case that changes what a step writes, copies or shows searches for the name of that output and reads each step that reads it. Its reading at the Retro of session 2005, line 54 of `vault/raw/2026-10-30/2005/ledger.md`, came out `failed`: at the `/pre-spec` of session 1713, finding 1.2 was Case 931, which added `drop` to the keys of a page `update` and left two texts that list those keys one by one, the sentence of `case-schema.md` on the sub-point keys that the hook of `rule-spec-write` reads, and the sentence of `rule-materialize` that lists the keys the lift carries. Both texts were fixed in that session: the file of Case 931, built again after `/pre-spec`, holds a second pair on `rule-case-protocol` that adds `drop` to that list, and line 30 of `vault/wiki/case-schema.md` now holds `drop` among the keys; Case 935.1 added `drop` to the sentence of `rule-materialize`, and that page's History holds the line of `decision-case-935.1`. So no Case is needed for the two texts. The miss has one shape: a new member of a list is a word no text holds yet, so a search for it finds nothing, while a search for a member already in the list finds each text that lists them; the file of Case 931 built again says that a Grep of `` `rename` `` over `vault/wiki` printed both texts. The sentence of case 924 names outputs and paths, and the sentence of case 784 names a field, term or command whose behaviour changes; neither names a new member of a list, and both stand, since the new sentence adds to them and changes neither. A finding of `/pre-spec` named `estimate-case-build-checks-the-finished-case`, which I read: its When is `case-guppi` about to answer with a built Case, and one line of its Then is the search for the name of each field, term or command whose behaviour the Case changes, the sentence of case 784; its `purpose` and `method` count what `ask-guppi` still finds at `/pre-spec` among the checks they list. Its Criterion stands: the new sentence changes none of the searches it lists, and a search for the name of a changed thing cannot find a list that a new member is missing from, since that member stands in no text yet. The new search is a promise of its own: it can fail while the search of case 784 passes, and the fix is another sentence, so by the rule of atomicity in `ratification.md` it gets its own Estimate, not a line added to that Criterion. The rule on a failed Estimate is line 35 of `rule-estimates-schema`: a `failed` Estimate is debt until a human decides, and archival is the default absent a decision to fix. The person chose to fix it: Case 948.1 adds to the Render one sentence on a new member of a list and creates `estimate-case-build-reads-each-list-of-a-new-member` to check it; a Glob `vault/**/*list*member*` printed nothing, so the slug is free. Case 948.2 sets the failed Estimate `pending` again, its Criterion written back word for word, its `purpose` kept since it states the same promise, and its `method` set anew to wait for the `/pre-spec` of the first session on the new Render. The brief reports the last `guppi check` under `## Flags`: `estimate-case-build-reads-the-readers-of-a-changed-step: unread: failed`. In `.guppi/guppi/lint.py` I read `check_unread`, `waits_for_a_later_moment`, `waits_for_an_event` with `EVENT_PART` and `ANOTHER_SESSION`, `method_of`, `tied_to_a_one_off_moment` with `is_reading` and `FIRST_AFTER`: a `failed` Estimate is always an `unread` finding, and a `pending` one is none when a part of its `method` between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon; the new methods hold such a part, and no part that holds `by hand` names a first thing after the render or the change. The check of this file noted that two `then` lines of Case 948.2 share most of their words with lines of Case 948.1: the line on what enters the Case and the `－` line on History, `log.md` and `brief.md`. They stand, since they are lines of the promises of two Estimates: Case 948.2 writes back the Criterion of the old Estimate word for word, and Case 948.1 states the same bounds for the texts that list the members of a list. A Grep of `case-guppi\.md|rule-case-build|agents/` over `.guppi/tests` printed `test_guppi_package.py`, where the hit is a sentence of its docstring, and no test reads `.claude/agents/case-guppi.md` live. `insight-case-build-changes-a-step-without-reading-its-readers` stands `actioned`, its fix the sentence of case 924, which this Case keeps. The session's ledger holds no `error` lesson.

> **problem:**
> The reading of `estimate-case-build-reads-the-readers-of-a-changed-step` failed: a Case that added a key to a list missed two texts that list the keys, since no instruction of `case-guppi` names a search for the members already in a list, and the failed Estimate is debt.

> **recommend:**
> - **What does this Case do with the failed reading?**
>   - Recommended: (a) widen the instruction for a new member of a list that texts spell out, with a new Estimate.
>   - Answer: (a).
> - **What happens to the failed Estimate?**
>   - Recommended: (a) it waits again for a new reading, its promise word for word, its method on the next `/pre-spec`.
>   - Answer: agreed, (a).
> - **When is the new instruction checked?**
>   - Recommended: (a) at the Retro of this session and at the next `/pre-spec`.
>   - Answer: agreed, (a).

### Case 948.1 — case-guppi searches for a member already in a list it adds to

> **given:**
> `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, gains the sentence on a new member of a list.
> **＋** `estimate-case-build-reads-each-list-of-a-new-member`: the new check of that sentence.
> **＋** `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/`: the texts the search runs over.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that adds a member to a list that texts spell out one by one — a key of an item, a kind, a status or a field — and is about to answer with its summary.

> **then:**
> It searches the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already.
> **＋** It reads each hit that lists the members of the list.
> **＋** Each text that lists the members and would miss the new member enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `rule-case-build`
>   - old: `` `context` names it and says why it stands (as set in case 924). ``
>   - new: `` `context` names it and says why it stands (as set in case 924). When the Case adds a member to a list that texts spell out one by one — a key of an item, a kind, a status or a field — Grep the live pages of `vault/wiki/` outside `decisions/`, `.claude/` and `.guppi/guppi/` for a member that stands in the list already, since the new member stands in no text yet, and read each hit that lists the members; a hit in a History line, in `log.md` or in `brief.md` is not read; each text that would miss the new member enters the Case, or `context` names it and says why it stands (as set in case 948.1). ``
>   - change: `case-guppi searches for a member already in a list its Case adds to, and reads each text that lists the members`
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
> - [ ] create `estimate-case-build-reads-each-list-of-a-new-member`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether case-guppi, when its Case adds a member to a list that texts spell out one by one, searches for a member already in the list and enters each text that would miss the new member in the Case, or names it in context`
>   - method: `by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line; after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on a new member of a list: the findings of ask-guppi at that /pre-spec read for a Case that adds a member to a list and misses a text that lists the members, the count in the estimate line`
>   - tags: `[session, workflow, harness, case-build]`
> - [ ] read `estimate-case-build-reads-each-list-of-a-new-member`

> **ratification:**
> ```
> - decision[case 948.1][update][rule-case-build]{ref:rule-case-build}
> - decision[case 948.1][create][estimate-case-build-reads-each-list-of-a-new-member]{ref:rule-case-build}{tags:session,workflow,harness,case-build}
> ```

### Case 948.2 — The reading of the readers of a changed step waits for the next /pre-spec

> **given:**
> `estimate-case-build-reads-the-readers-of-a-changed-step`: set `pending`, its Criterion written back, its `method` set anew.
> **＋** `rule-case-build`: its Render, `.claude/agents/case-guppi.md`, holds the sentence on the readers of a changed step.
> **＋** `vault/wiki/rules/` and `.claude/`: the texts the search runs over.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.

> **then:**
> It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
> **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
> **＋** Each step or skill that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A hit in a History line, in `log.md` or in `brief.md` is not read.

> **tasks:**
> - [ ] update `estimate-case-build-reads-the-readers-of-a-changed-step`
>   - set: `{status: pending, method: "by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on a new member of a list: the findings of ask-guppi at that /pre-spec read for a Case that changes a step and misses a step or skill that reads its output or does the same step, the count in the estimate line"}`
>   - sections.Criterion:
>     ```
>     When:
>     `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case that changes what a step of a skill, an agent or a hook writes, copies or shows, or adds a path on which a step does so, and is about to answer with its summary.
>
>     Then:
>     It searches `vault/wiki/rules/` and `.claude/` for the name of that output — a line such as `Branch:`, a file or a list — and for the name of the step.
>     **＋** It reads each step and skill that reads that output or does the same step, the steps after it in the same text and the new path its own Case adds included.
>     **＋** Each step or skill that the change makes false enters the Case, or the `context` of the Case names it and says why it stands.
>     **－** A hit in a History line, in `log.md` or in `brief.md` is not read.
>     ```
>   - change: `pending again after the failed reading of session 2005, the Criterion written back unchanged; the method waits for the /pre-spec of the first session on the Render with the sentence on a new member of a list`
> - [ ] read `estimate-case-build-reads-the-readers-of-a-changed-step`

> **ratification:**
> ```
> - decision[case 948.2][update][estimate-case-build-reads-the-readers-of-a-changed-step]{ref:rule-case-build}
> ```
