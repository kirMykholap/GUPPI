## Case 764 — The checks that wait for a moment of the sprint stay off Work and the Frontier

> **context:**
> The brief lists every `pending` check (Estimate) under `Work` of its Next session, and `/hi` copies each one onto the Frontier as a `W` line; a `W` line that cannot be read now becomes a Cases line that asks to fix, replace or archive the check. So the five checks of `entity-sprint-plugin`, the Definition of done of the sprint, stood as W2 to W6 of this session, and four of them again as C7 to C10, though the work they check is not done; W1, `estimate-sprint-close-next-session-opens-the-sprint`, waits for the session after the close of a sprint. Three texts also hold no exception for a check of a sprint page. `case-schema.md` lets a `method` hold only what runs in the Case's own session (case 670.4). `/retro` sets each Estimate its session creates or updates and cannot read `failed` with `Retro, not read`, while the Retro of session 1713 left the five checks `pending`, as the context of Case 756 said. `waits_for_another_session` of `guppi/lint.py` does not match "a session of the sprint plugin before its close" or "the session that closes", as `lesson-prespec-method-predicate-misses-a-sprint-session` records. The person chose this: a check of the live sprint page stands in no list of Next session and is read at the Retro of the session that finishes its work or by the closing Case of `/sprint-close`; a check whose `method` names the close of a sprint stands in no list until the brief of the run that closes the sprint, Ask lines included; Retro leaves a sprint check whose work is not done `pending`, and the handoff names it; only a check whose target is a sprint page may wait for a later session of its sprint; and pre-spec catches the new words and spares such a check. `vault/wiki/sprint.md` keeps showing the checks of the sprint page under `Done when`, and Readings due of the brief keeps every `pending` check, so none is lost while it waits. Case 764.1 changes the brief, Case 764.2 Retro, Case 764.3 the handoff, Case 764.4 the rule of case 670.4 and the pre-spec check of a written method, and Case 764.5 the pre-spec check of a method kept on the page; each replaces the Criterion of the one Estimate whose Criterion speaks of its change, and sets anew a `purpose` or `method` that states the old promise. Not done, by the person's choice: the method of W1 names a transcript of an earlier session, which `/hi` may not read (case 670.5), and it waits for a Case before the close of `plugin`; and `make lint` keeps its `unread: pending` line for each waiting check. The text of `rule-skill-hi` stands: its sentences that keep an open `W` or `A` line of the close of a sprint waiting for that session stay true, since such a line now reaches the Frontier only from the brief of the closing run, and no check of a sprint page reaches it to become a Cases line; for the same reason the Criterion of `estimate-hi-takes-its-readings` stands. `rule-sprint` and `entity-sprint` say that the Estimates of a sprint page are read before its close, which stays true. Step 3 of `/sprint-close` sorts every `pending` or `failed` Estimate by the kind of its moment, so a check that waits for the session that closes a sprint needs no list of Next session. A Grep `` Retro, not read|set it `failed`|pending` reading|reading cannot be taken yet `` over `vault/wiki/rules/` and `.claude/` printed `vault/wiki/rules/rule-brief.md`, `vault/wiki/rules/rule-handoff.md`, `vault/wiki/rules/rule-retro.md`, `.claude/agents/librarian-guppi.md`, `.claude/skills/handoff/SKILL.md` and `.claude/skills/retro/SKILL.md`: the three rules this Case changes and their renders. A Grep `670\.4` over `vault/wiki/rules/` printed `vault/wiki/rules/rule-case-protocol.md`, whose two sentences Case 764.4 changes, and `vault/wiki/rules/rule-prespec-hook.md`, where it stands in a History line alone. A Grep `ANOTHER_SESSION|closes a sprint|session of the sprint|session that closes` over `guppi/` printed `guppi/lint.py` and `guppi/prespec.py`: the one judgment of the words of a waiting method is `ANOTHER_SESSION` of `guppi/lint.py`, which Case 764.4 widens, and the hit in `guppi/prespec.py` is a finding on a Frontier line, no such judgment. A Grep `SPRINT_PAGE` over `guppi/` printed `guppi/materialize.py` and `guppi/prespec.py`: the test for a sprint page reuses the constant `SPRINT_PAGE` that `guppi/prespec.py` already holds, and the older copy in `guppi/materialize.py`, which judges a ledger line, stands. A Grep `parents\[1\]|parent\.parent` over `tests/` printed `tests/test_generate.py`, `tests/test_case_schema.py`, `tests/test_orchestration.py`, `tests/test_schemas.py`, `tests/test_lint.py` and `tests/test_materialize.py`; they read the `schema.yaml` files, `orchestration.md` and the `Makefile`, and `case-schema.md` only while `case-example.md` does not stand, so no test reads live a file this Case changes. A Grep `session\s+(of\s+(the\s+)?sprint|that\s+closes)` over `tests/` printed nothing, so no test holds a method that the wider predicate judges anew. Of the other Cases of this batch, Cases 766, 767 and 768 point to this rule and change no page this Case changes; Case 767 replaces the Criterion of a sprint-page check and keeps its method, which Case 764.5 spares. Case 765 had no file when this Case was built.

> **problem:**
> Checks that cannot be read before a later moment of the sprint stand under `Work` and on the Frontier in every session, and turn into decision items though nothing is wrong with them. The rule that a check is read in its own session, Retro and pre-spec hold no exception for the checks of a sprint page.

> **recommend:**
> - **When do the sprint page's own checks come back to be read?**
>   - Recommended: (a) no new trigger: the Retro of the session that finishes the work, or the closing Case of `/sprint-close`.
>   - Answer: agreed, (a).
> - **Do Ask lines that wait for a sprint close leave the Frontier too?**
>   - Recommended: (a) yes, the same rule: such a line is left out until the brief written at a sprint close.
>   - Answer: agreed, (a).
> - **What does Retro do with a sprint-page check it cannot read?**
>   - Recommended: (a) it stays pending, and the handoff names it as a check that waits for its work.
>   - Answer: agreed, (a).
> - **Which checks may name a later session of the sprint?**
>   - Recommended: (a) only checks whose target is a sprint page.
>   - Answer: agreed, (a).
> - **How does pre-spec judge the new wording?**
>   - Recommended: (a) the predicate catches a session of a sprint and the session that closes one, and pre-spec spares a check of a sprint page.
>   - Answer: agreed, (a).
> - **What happens to W1, whose reading needs an old transcript?**
>   - Recommended: (a) leave it out of this Case; a later Case fixes its method before the close of `plugin`.
>   - Answer: agreed, (a).
> - **Do the red lines of `make lint` stay for these checks?**
>   - Recommended: (a) they stay.
>   - Answer: agreed, (a).

### Case 764.1 — The brief keeps the waiting checks out of Next session

> **given:**
> `rule-brief`: the rule of the brief, rendered into `.claude/agents/librarian-guppi.md`.
> **＋** `estimate-brief-written`: its Criterion is replaced whole and its method set anew.
> **＋** `vault/wiki/brief.md`: the brief the librarian writes.
> **＋** `entity-sprint-<id>`: the live sprint page, whose checks wait.
> **＋** `vault/wiki/sprint.md`: the rendered sprint, which shows the checks of the sprint page.
> **＋** `vault/wiki/backlog.md`: where the deferred items stand.
> **＋** `vault/archive/`: where the pages of a closed sprint stand.
> **＋** `/hi`: the skill that takes the lists of Next session onto the Frontier.
> **＋** `rule-carry-over`: the second writer of the brief.

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items; they stand in `vault/wiki/backlog.md`. Where things stand, Readings due and Readings at the close are as before, and Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
> **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, an item in one list only, a list with no item the line "none". `Cases` is what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags, one between pages that stand in `vault/archive/` too, a defect the librarian found; with what and from where.
> **＋** `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, and one whose `method` names the close of a sprint — the session that closes a sprint, its librarian's run or the session after it; the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint.
> **＋** In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer.
> **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
> **－** A reading left out of `Work` and `Ask the person` keeps its line under Readings due.
> **－** A contradiction of Flags that a line of `## For the next session` of `handoff.md` already carries gets no second line in `Cases`.
> **－** The brief states no decision: the sort by kind is not a judgment of the work.

> **tasks:**
> - [ ] update `rule-brief`
>   - old: `` `Work`, what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, the unticked boxes of the Specs ``
>   - new: `` `Work`, what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page and one whose `method` names the close of a sprint, the unticked boxes of the Specs ``
>   - old: `` `Ask the person`, a reading only the person can take: each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them. ``
>   - new: `` `Ask the person`, a reading only the person can take: each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint. A `method` names the close of a sprint when it names the session that closes a sprint, its librarian's run or the session after it. A reading of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, or whose `method` names the close of a sprint, stands in Readings due alone and in no list of Next session: the first is read at the Retro of the session that finishes its work or by the closing Case of `/sprint-close`, the second at its moment. In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer (case 764.1). ``
>   - change: `Work and Ask the person of Next session leave out a reading of the live sprint page and one whose method names the close of a sprint, until its moment (case 764.1)`
> - [ ] update `estimate-brief-written`
>   - set:
>     ```
>     status: pending
>     method: "by hand, the person's answer at the /hi after the librarian's run of the session that closes a sprint, on vault/wiki/brief.md of that run and the brief of the run before it: whether Cases hold each contradiction of Flags, one between archived pages too, and once where a line of For the next session carries it, and whether Work and Ask the person leave out a reading of the live sprint page and one whose method names the close of a sprint but in the brief of the closing run, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — Work and Ask the person leave out a reading that waits for a moment of the sprint; the method reads it too`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-brief-written`

> **ratification:**
> ```
> - decision[case 764.1][update][rule-brief]{ref:rule-brief}
> - decision[case 764.1][update][estimate-brief-written]{ref:rule-brief}
> ```

### Case 764.2 — Retro leaves a sprint check whose work is not done pending

> **given:**
> `rule-retro`: the rule of Retro, rendered into `.claude/skills/retro/SKILL.md`.
> **＋** `estimate-retro-loads`: its Criterion is replaced whole.
> **＋** `entity-sprint-<id>`: the live sprint page, whose checks wait.
> **＋** `/work`: the skill that calls Retro.
> **＋** `/sprint-close`: the skill whose closing Case reads the checks still pending.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose Criteria Retro reads.
> **＋** `raw/<date>/<hi HHMM>/work.md`: the file of Work Mode that may name a conserved Spec.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier whose `W` lines Retro closes.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the report of Retro.

> **when:**
> The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built.
> **＋** Each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — is read in the reply that ends Retro, on the Criterion of `raw/<date>/<hi HHMM>/spec.md`: the `when` and `then` of its Case, or the Criterion its item writes.
> **＋** For an Estimate of a rule whose Render a Case of the Spec changes, the reading reads the new text of the Render in `raw/<date>/<hi HHMM>/spec.md` against that Criterion.
> **＋** Each such Estimate that Retro cannot read gets a `failed` line in the same `LEDGER` block, whose result opens with the date and says that Retro did not read it and why.
> **＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as this session's for its boxes, for the scope of an edit and for the readings above.
> **＋** Retro closes the open `W` line of each Estimate it reads or sets `failed` `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`.
> **－** An Estimate whose `target` is the live sprint page `entity-sprint-<id>`, which this session creates or updates and whose work is not done yet, is neither read, nor put to the person, nor set `failed`: it stays `pending` for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`.
> **－** An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`.
> **－** A reading whose `method` names the person's word is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question, and its `read` line is neither debt nor the librarian's.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `` A reading whose `method` names the person's word is not yours to take: ``
>   - new: `` An Estimate whose `target` is the live sprint page, `entity-sprint-<id>`, which this session creates or updates and whose work is not done yet, is neither read, nor put to the person, nor set `failed`: it stays `pending` for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, and `handoff.md` names it with that moment (case 764.2). A reading whose `method` names the person's word is not yours to take: ``
>   - change: `Retro leaves an Estimate of the live sprint page whose work is not done pending, not read and not set failed (case 764.2)`
> - [ ] update `estimate-retro-loads`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an Estimate of the live sprint page whose work is not done stays pending`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-loads`

> **ratification:**
> ```
> - decision[case 764.2][update][rule-retro]{ref:rule-retro}
> - decision[case 764.2][update][estimate-retro-loads]{ref:rule-retro}
> ```

### Case 764.3 — The handoff names a sprint check that waits for its work

> **given:**
> `rule-handoff`: the rule of the handoff, rendered into `.claude/skills/handoff/SKILL.md`.
> **＋** `estimate-handoff-holds-each-fact-once`: its Criterion is replaced whole.
> **＋** `rule-retro`: the Retro whose report the handoff is.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the handoff the agent writes.
> **＋** `entity-sprint-<id>`: the live sprint page, whose checks wait.
> **＋** `rule-brief`: the rule of the brief, which reads the handoff.

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
> **＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
> **＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
> **＋** An Estimate this session creates or updates has no such line in `## Debt`: the Retro of `rule-retro` read it or set it `failed`, unless the person's answer is its reading. An Estimate of the live sprint page `entity-sprint-<id>` whose work is not done, which that Retro left `pending`, has its line, its moment the Retro of the session that finishes its work or the close of the sprint.
> **＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
> **＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
> **－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
> **－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

> **tasks:**
> - [ ] update `rule-handoff`
>   - old: `` an Estimate this session creates or updates has no such line, since Retro read it or set it `failed`; ``
>   - new: `` an Estimate this session creates or updates has no such line, since Retro read it or set it `failed`, but for an Estimate of the live sprint page whose work is not done, which Retro left `pending`: its line names the Retro of the session that finishes its work or the close of the sprint (case 764.3); ``
>   - change: `Debt names an Estimate of the live sprint page that Retro left pending, with its moment (case 764.3)`
> - [ ] update `estimate-handoff-holds-each-fact-once`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — Debt names an Estimate of the live sprint page that Retro left pending`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] read `estimate-handoff-holds-each-fact-once`

> **ratification:**
> ```
> - decision[case 764.3][update][rule-handoff]{ref:rule-handoff}
> - decision[case 764.3][update][estimate-handoff-holds-each-fact-once]{ref:rule-handoff}
> ```

### Case 764.4 — A check of a sprint page may wait for a later session of its sprint

> **given:**
> `rule-case-protocol`: the form of a Case, rendered into `vault/wiki/case-schema.md`, whose rule of case 670.4 gains the exception.
> **＋** `guppi/lint.py`: `ANOTHER_SESSION` and `waits_for_another_session`, the one predicate of a waiting method.
> **＋** `guppi/prespec.py`: the check of the form of an Estimate item and its module docstring.
> **＋** `tests/test_lint.py`: the tests of the predicate.
> **＋** `tests/test_prespec.py`: the tests of the finding.
> **＋** `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`: its Criterion and its `purpose` are set anew.
> **＋** `entity-sprint-<id>`: a sprint page, the target that the exception names.
> **＋** `/hi`: a moment a method may name, which the predicate catches.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

> **then:**
> A `method` with a part between two `;` that names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi` gives one line `case N: <create|update> <slug>: method waits for another session — a method holds only what runs in its own session`.
> **＋** The judgment is one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
> **－** A part that names the person, such as the person's answer at `/hi`, gives no such line.
> **－** An Estimate whose target is a sprint page `entity-sprint-<id>` — the `ref` of a `create`, or the `target` that an `update` sets or that the live page holds — gives no such line.
> **－** `uv run guppi lint` of `guppi/lint.py` over the live Estimate pages gives no finding by this predicate.
> **－** The line does not replace the finding of a `method` that names no form or that ties its reading to a one-off moment.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `` a problem seen live in a later session is a lesson, and pre-spec reports a `method` that waits for a later session, the librarian or a `/hi` (case 670.4). ``
>   - new: `` a problem seen live in a later session is a lesson, and pre-spec reports a `method` that waits for a later session, a session of a sprint, the session that closes one, the librarian or a `/hi` (case 670.4). An Estimate whose target is a sprint page, `entity-sprint-<id>`, is the exception: the sprint page is the Definition of done of its sprint, read before its close, so its `method` may wait for a later session of that sprint, up to the session that closes it (case 764.4). ``
>   - old: `` which the Retro of the Case's own session takes on the Criterion of the Spec (case 670.4), ``
>   - new: `` which the Retro of the Case's own session takes on the Criterion of the Spec (case 670.4), or, for an Estimate of the live sprint page whose work is not done, the Retro of the session that finishes its work or the closing Case of `/sprint-close` (case 764.4), ``
>   - change: `an Estimate of a sprint page may wait for a later session of its sprint, and pre-spec catches a session of a sprint and the session that closes one (case 764.4)`
> - [ ] update `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`
>   - set:
>     ```
>     status: pending
>     purpose: Whether pre-spec reports a method in the plan that waits for a later session, a session of a sprint, the session that closes one, the librarian or a /hi, by one predicate of guppi/lint.py, and leaves alone a method that names the person, the method of an Estimate of a sprint page, and the live pages
>     ```
>   - change: `the Criterion replaced whole — the predicate catches a session of a sprint and the session that closes one, and an Estimate of a sprint page gives no finding`
> - [ ] `guppi/lint.py`: `ANOTHER_SESSION` also matches a session of a sprint and the session that closes, such as "a session of the sprint plugin before its close" and "the session that closes entity-sprint-plugin"; the docstring of `waits_for_another_session` names them.
> - [ ] `guppi/prespec.py`: a function that tells whether a target, its `[[` and `]]` removed, opens with the constant `SPRINT_PAGE`; the check of the form gives no `WAITS` line on a `create` whose `ref`, or an `update` whose target by `estimate_target`, is a sprint page; the module docstring names the new words and the exception.
> - [ ] `tests/test_lint.py`: the test of the one predicate holds a method that names a session of a sprint and one that names the session that closes it among the methods that wait.
> - [ ] `tests/test_prespec.py`: a `create` and an `update` of an Estimate of a sprint page whose method names a session of the sprint before its close give no line; the same method on an Estimate of a rule gives the line.
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] read `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`

> **ratification:**
> ```
> - decision[case 764.4][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 764.4][update][estimate-prespec-hook-reports-a-method-that-waits-for-another-session]{ref:rule-prespec-hook}
> ```

### Case 764.5 — Pre-spec spares a kept method of a sprint check

> **given:**
> `guppi/prespec.py`: `kept_method_waits`, the check of a method kept on the page.
> **＋** `guppi/lint.py`: `waits_for_another_session`, the one predicate of a waiting method.
> **＋** `tests/test_prespec.py`: the tests of the finding.
> **＋** `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`: its Criterion and its `purpose` are set anew.
> **＋** `entity-sprint-<id>`: a sprint page, the target that the exception names.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads an `update` of an Estimate in the `then` blocks of the plan file that replaces its Criterion whole and carries no `set: {method: …}`, and the `method` of that Estimate's live page.

> **then:**
> When a part of that `method` between two `;` names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or /hi, and does not name the person, the check gives one line `case N: update <slug>: the method on the page waits for another session — set a method that runs in this session`.
> **＋** The judgment is `waits_for_another_session` of `guppi/lint.py`, the same predicate that judges a `method` the plan writes.
> **－** An Estimate whose live page holds a sprint page `entity-sprint-<id>` as its `target` gives no such line.
> **－** An `update` that sets the Estimate `passed` or `failed` by the person's decision gives no such line.
> **－** An `update` that names a part of the page alone, such as a `set` of another field or a `replace` pair, gives no such line.
> **－** A `method` on the page that waits for no other session, or whose part names the person, gives no such line.

> **tasks:**
> - [ ] update `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`
>   - set:
>     ```
>     status: pending
>     purpose: Whether pre-spec reports a Case that replaces the Criterion of an Estimate whole, writes no method and keeps one on the page that waits for another session, by the one predicate of guppi/lint.py, but for an Estimate of a sprint page
>     ```
>   - change: `the Criterion replaced whole — a kept method of an Estimate of a sprint page gives no finding, and the predicate names a session of a sprint and the session that closes one`
> - [ ] `guppi/prespec.py`: `kept_method_waits` returns false when the `target` of the live page is a sprint page, by the function of Case 764.4; its docstring says so.
> - [ ] `tests/test_prespec.py`: an `update` that replaces the Criterion of an Estimate of a sprint page whole and keeps a method that names a session of the sprint gives no line; the same kept method on an Estimate of a rule gives the line.
> - [ ] read `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`

> **ratification:**
> ```
> - decision[case 764.5][update][estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session]{ref:rule-prespec-hook}
> ```
