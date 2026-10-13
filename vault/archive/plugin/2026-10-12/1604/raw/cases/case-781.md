## Case 781 — A reading that cannot run now waits instead of becoming a decision

> **context:**
> Today a check's `method` may hold only what runs in the Case's own session, or the person's answer, and `/pre-spec` reports a method that waits for a later session, the librarian or a `/hi` (case 670.4). The only exception is a check of the live sprint page (case 772.4). So a check that can only be read after an outside event, such as a pull request from a second account, cannot be written. At `/hi`, an open `W` reading that cannot run now becomes a line under `## Cases` that asks the person to fix, replace or archive the check (case 670.6). Case 778 left out two things: checks that wait for an event other than the close of a sprint, and the path the person proposed for a reading `/hi` cannot take. In this Case the person chose that path. A method may wait for an event it names: a part of the method between two `;` that opens with `after`, or with `by hand, after`, and names the event before a colon. `/pre-spec` stops reporting such a part, and a method kept on a live page is treated the same. Retro leaves such a check `pending` while its event has not come, and the handoff names it with its event. At its run the librarian looks for the event, and once it sees it, the reading goes under `Work` or `Ask the person`. An open `W` reading that `/hi` cannot take stays in `Work`. When the handoff names it as not taken, the librarian's brief adds a line to the next session's `Cases` that proposes to defer the check into the backlog. A defer can now mark an Estimate `deferred_by`, so `backlog.md` lists it, and the brief leaves it out of `Work`. Case 780 of this session left out a `/pre-spec` check over the `When` and `Then` of a Criterion; the person chose to leave it out here too.
>
> The frame showed that three of the person's first choices could not hold as written, and the later rounds settled each one. First, a defer marks only a rule, an entity or an insight: `DEFERRABLE` in `guppi/generate.py`, and the format of a check page has no `deferred_by` field. Second, the handoff's own rule and its check say that a check this session creates has no waiting line. Third, `estimate-retro-loads` and `estimate-brief-written` already promise what Retro and the brief do, so they are replaced, not paired with new checks. Each part replaces the Criterion of one existing Estimate, and the Case creates no page. No `create` stands without a `ref`, so no vault query was run.
>
> The new judgment of an event part lives in `guppi/lint.py`, beside `waits_for_another_session`, which calls it; `guppi/prespec.py` imports both. A Grep for ``compile\(.*after|\\bafter`` over `guppi/` printed `guppi/casecheck.py` and `guppi/lint.py`. The hit in `casecheck.py` reads a History line of a cascade, and `FIRST_AFTER` of `lint.py` judges a one-off moment that a reading is tied to, a different judgment, so no code makes this judgment yet. The librarian, Retro and `/hi` judge the event part from the text of their Render, and no code of theirs judges it.
>
> A Grep for `cannot run now|Retro, not read|reading cannot be taken|whose reading cannot` over `vault/wiki/rules/`, `.claude/` and `vault/wiki/orchestration.md` printed `.claude/skills/box/SKILL.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `.claude/skills/handoff/SKILL.md`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/rules/rule-handoff.md`, `vault/wiki/rules/rule-retro.md` and `vault/wiki/rules/rule-spec-box.md`. The skill files are the Renders of the three rules this Case changes, and of `rule-spec-box`. In `rule-spec-box` the words name a reason a conserved Spec cannot run, a moment this Case does not touch.
>
> In `rule-case-protocol` two sentences state the touched behaviour, and both are rewritten. The first is the sentence on what a method holds. The second is the sentence on who takes the `read` line of a check whose moment comes after Work Mode. In `rule-retro` the sentence that sets `failed` on each other Estimate Retro cannot read stays true, because the new exception stands before it, as the sprint-page exception does. The sentence that a `read` line with no reading is debt is bounded the same way. The sentence that a problem seen live in a later session is a lesson gains an exception for the reading of an event check, which a later session takes. In `rule-handoff` one sentence is rewritten. In `rule-brief` three are rewritten: the `Cases` list, the `Work` list, and the sentence after the sprint-close rule. In `rule-skill-hi` two are rewritten: the Cases source of an open `W` line, and the paragraph that makes it a Cases line, which held the two sprint exceptions. The sentences on which pages the reading step opens and on how a `W` line closes stay true. The `fields` of `rule-estimates-schema` gain `deferred_by`, and the docstrings of `guppi/generate.py` name the Estimate. `rule-page-generation` names no category a defer marks, so it takes only a History line. `rule-ask` gives Estimates no index line, so `ask-guppi` does not see a deferred Estimate's `deferred_by`. That stands: `backlog.md` lists it, and `ask-guppi` reaches Estimates through their target. The glossary row of `deferred_by` says the index line carries it, which is false for an Estimate, so Case 781.7 rewrites that row of `entity-glossary`. The rest of that row stays true: an Estimate is a page a `defer` targets. The other rows that touch a defer or an Estimate stay true too: the Estimate row, which says an Estimate has no index and is reached through its target, the Estimate fields row, which like the Rule fields row lists no `deferred_by`, and the `backlog.md` row. No other Case of this session writes into `entity-glossary`. `rule-backlog`, which lists each live page with `deferred_by`, stays true. The Criterion of `estimate-prespec-hook-reports-a-method-that-waits-for-another-session` said `guppi/sprint_close.py` imports the sprint-page predicate. It imports only `SPRINT_PAGE`, so the carried line drops that module and the docstring of `ledger.py` follows. The Criterion of `estimate-hi-writes-frontier` lists the Cases line that Case 781.8 removes from `/hi` among its sources, so Case 781.9 replaces it. Its method, the person's answer after the close of a sprint, stands. In both, the touched line is rewritten, so the check notes it as not carried. Once a defer marks an Estimate, the short Case of a take-back, which writes a `defer` line for each Estimate the Case taken back updates (`rule-orchestration`), marks that Estimate too. The person chose that it stands in the backlog and out of `Work` until a Case takes it up. The Criterion of `estimate-orchestration-takes-back-a-ratified-case` says that generate adds the short Case to each rule, entity and insight page a `defer` line names, which stays true, so it stands. The eleven `＋` lines of `then` in Case 781.6 are the Criterion of `estimate-generate-writes` as it stands, with two lines changed, so the sub-case keeps one promise.
>
> In `estimate-handoff-holds-each-fact-once`, `estimate-generate-writes` and `estimate-estimates-schema-checked`, the Criterion line that the change touches is rewritten, not dropped, so the check notes it as not carried; in `estimate-brief-written` the same holds for the lines of `Next session` and `Work`. These Criteria lose lines on purpose. In `estimate-hi-takes-its-readings`, the `＋` line that writes a Cases line for each other open `W` line is not carried, and the two `－` lines of the sprint exceptions become one line for any reading that cannot run now. `estimate-brief-written` gets a method that reads the new Render at the Retro of this session, as the person chose. Its old method waited for the person's answer after the close of a sprint. The other Estimates keep their methods. The `purpose` of the two `/pre-spec` Estimates and of `estimate-hi-takes-its-readings` states the old promise, so each is set anew.
>
> Tests that read live files: a Grep for `(ROOT|REPO)\s*/\s*"vault"` over `tests/` printed `tests/test_case_schema.py`, `tests/test_schemas.py`, `tests/test_generate.py` and `tests/test_orchestration.py`. A Grep for `(ROOT|REPO)\s*/\s*"\.claude"` over `tests/` printed nothing. `test_case_schema.py` reads the `case` block of `vault/wiki/case-example.md`, which this Case does not change, and the new text of `case-schema.md` adds no such block. `test_schemas.py` builds a page from the `required` and `conditional` lists of the live `estimates/schema.yaml`, so a new optional field with its description under `fields` fails none of its functions. The other two copy the live schemas into a temporary folder, and an added optional field refuses no page. The predicate only accepts more methods, so no live text that it judged clean before becomes a finding. No existing test method in `tests/test_lint.py` or `tests/test_prespec.py` opens a part with `after` before a colon.

> **problem:**
> A check that can only be read after an outside event cannot be written. A reading that `/hi` cannot take turns into a decision at the start of the next session, though nothing about it needs deciding at once.

> **recommend:**
> - **May a check wait for an event other than the close of a sprint?**
>   - Recommended: (b) allow any event the method names; `/pre-spec` stops reporting it, and the brief keeps the reading out of Work until the event has happened.
>   - Answer: agreed, (b).
> - **What should `/hi` do with a Work reading it cannot take?**
>   - Recommended: (b) the path the person proposed: the reading stays in Work, the librarian flags it in the brief, and at the next `/hi` a line proposes to defer it into the backlog.
>   - Answer: agreed, (b).
> - **Should this Case add a `/pre-spec` check on the wording of a check?**
>   - Recommended: (a) leave it out.
>   - Answer: agreed, (a).
> - **How does a check name the event it waits for?**
>   - Recommended: (a) a fixed opening inside the method: a part that opens with "after" and the event, then a colon; one function in `guppi/lint.py` judges it.
>   - Answer: agreed, (a).
> - **Who sees that the event has happened, and who then reads the check?**
>   - Recommended: (a) the librarian at its run looks for the event in the ledger, git log, handoff and files, and once it sees the event puts the reading under Work or Ask; that session's `/hi` or Work Mode reads it.
>   - Answer: agreed, (a).
> - **What does Retro do with a new check whose event has not happened yet?**
>   - Recommended: (a) leave it pending, as for the sprint page; the handoff names it with its event; Retro reads it if the event happens in the same session.
>   - Answer: agreed, (a).
> - **One Case with parts, or two Cases?**
>   - Recommended: (a) one Case with six parts.
>   - Answer: agreed, (a); replaced by the later questions that set the parts again.
> - **How are the new checks on Retro and the librarian read?**
>   - Recommended: (a) at this session's Retro, from the new rule text in the plan.
>   - Answer: agreed, (a).
> - **How does a put-off check reach the backlog?**
>   - Recommended: (a) a defer marks a check `deferred_by` as it marks a rule, the format for check pages allows the field, and the brief leaves a put-off check out of Work; one more part.
>   - Answer: agreed, (a).
> - **The handoff report also changes**
>   - Recommended: (a) one more part: the handoff names a new check whose event has not happened, with its event, and its check is replaced.
>   - Answer: agreed, (a).
> - **Retro's waiting check replaces an existing check**
>   - Recommended: (a) rewrite `estimate-retro-loads` with one more exception, read at this session's Retro.
>   - Answer: agreed, (a).
> - **The two librarian parts share one existing check**
>   - Recommended: (a) merge the two librarian parts into one that replaces the Criterion of `estimate-brief-written`, its method a reading at this session's Retro.
>   - Answer: agreed, (a).
> - **Allowing a check to be put off needs its own part**
>   - Recommended: (a) one more part for the format, which replaces the Criterion of `estimate-estimates-schema-checked`; the Case has eight parts.
>   - Answer: agreed, (a).
> - **What happens to a check whose change is taken back?**
>   - Recommended: (a) a take-back marks the check too: it stands in the backlog and stays out of Work until a Case takes it up.
>   - Answer: agreed, (a).

### Case 781.1 — Pre-spec accepts a method part that waits for a named event

> **given:**
> `rule-case-protocol`: the rule rendered into `vault/wiki/case-schema.md`, which sets what a `method` holds and that pre-spec reports one that waits for a later session, the librarian or `/hi`.
> **＋** `rule-prespec-hook`: the rule of the check of the plan.
> **＋** `guppi/lint.py`: the one predicate of a `method` that waits for another session, and the new predicate of a part that waits for an event.
> **＋** `guppi/prespec.py`: the check of the plan that imports both predicates.
> **＋** `guppi/ledger.py`: the one predicate of a sprint page `entity-sprint-<id>`, which `guppi/prespec.py`, `guppi/materialize.py` and `guppi/sprint.py` import.
> **＋** `tests/test_lint.py` and `tests/test_prespec.py`: the tests of the two predicates and of the check.
> **＋** `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`: its Criterion is replaced whole and its `purpose` set anew.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

> **then:**
> A `method` with a part between two `;` that names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi` gives one line `case N: <create|update> <slug>: method waits for another session — a method holds only what runs in its own session`.
> **＋** The judgment is one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
> **＋** Whether the target is a sprint page is judged by one predicate in `guppi/ledger.py`, which `guppi/prespec.py`, `guppi/materialize.py` and `guppi/sprint.py` import.
> **－** A part that names the person, such as the person's answer at `/hi`, gives no such line.
> **－** A part that opens with `after`, or with `by hand, after`, and names its event before a colon, such as `by hand, after a pull request from a second account: the hook's output read against the Criterion`, waits for that event and gives no such line, whatever event it names, a later session or the librarian's run among them; the predicate of that part is one function in `guppi/lint.py`. A part with the same words but no colon, or one in which `after` does not open the part, still gives the line.
> **－** An Estimate whose target is a sprint page `entity-sprint-<id>` — the `ref` of a `create`, or the `target` that an `update` sets or that the live page holds — gives no such line.
> **－** `uv run guppi lint` of `guppi/lint.py` over the live Estimate pages gives no finding by this predicate.
> **－** The line does not replace the finding of a `method` that names no form or that ties its reading to a one-off moment.

> **tasks:**
> - [ ] update `rule-case-protocol`
>   - old: `` Its `method` holds only what runs in the Case's own session — a test, a command, a probe, or the reading of the Spec at Retro — or the person's answer; a problem seen live in a later session is a lesson, and pre-spec reports a `method` that waits for a later session, a session of a sprint, the session that closes one, the librarian or a `/hi` (case 670.4). ``
>   - new: `` Its `method` holds only what runs in the Case's own session — a test, a command, a probe, or the reading of the Spec at Retro — or the person's answer, or a reading that waits for an event it names; a problem seen live in a later session, outside such a reading, is a lesson, and pre-spec reports a `method` that waits for a later session, a session of a sprint, the session that closes one, the librarian or a `/hi` (case 670.4). A part of a `method` between two `;` that opens with `after`, or with `by hand, after`, and names its event before a colon waits for that event, whatever event it names — a later session or the librarian's run among them — and is no such finding, such as `by hand, after a pull request from a second account: the hook's output read against the Criterion`: Retro leaves its Estimate `pending` until the event, and once the librarian sees the event it puts the reading under `Work`, or under `Ask the person` when its `method` names the person's answer (case 781). ``
>   - old: `` or, for an Estimate of the live sprint page whose work is not done, the Retro of the session that finishes its work or the closing Case of `/sprint-close` (case 772.4), or through one its `context` names ``
>   - new: `` or, for an Estimate of the live sprint page whose work is not done, the Retro of the session that finishes its work or the closing Case of `/sprint-close` (case 772.4), or, for an Estimate whose `method` waits for an event that has not come, the session whose brief puts it under `Work` once the librarian sees the event (case 781), or through one its `context` names ``
>   - change: `a method may wait for an event it names in a part that opens with after and names the event before a colon; pre-spec does not report it (case 781)`
> - [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
> - [ ] `guppi/lint.py`: a new predicate `waits_for_an_event(part)` — true when a part, stripped, opens with `after`, or with `by hand, after`, and holds a colon after the event; `waits_for_another_session` passes such a part by; both docstrings name case 781.
> - [ ] `guppi/prespec.py`: the module docstring and the docstring of the check of a plan's `method` name the part that waits for an event, judged by `lint.waits_for_an_event` through `lint.waits_for_another_session`.
> - [ ] `guppi/ledger.py`: the docstring of `is_sprint_page` names `guppi/prespec.py`, `guppi/materialize.py` and `guppi/sprint.py` as the modules that import it; `guppi/sprint_close.py` imports `SPRINT_PAGE` alone.
> - [ ] `tests/test_lint.py`: in a test whose name holds `waits`, `by hand, after a pull request from a second account: the output read` and `pytest tests/test_x.py; after the librarian's run of a session: brief.md read` are no wait; `by hand after the librarian's run` with no colon, and `by hand at the /hi of the next session after the change: read`, still wait.
> - [ ] `tests/test_prespec.py`: in a test whose name holds `waits`, a `create` and an `update` with `set: {method: …}` whose method part waits for an event give no wait line; the same method with no colon gives it.
> - [ ] update `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`
>   - set:
>     ```
>     status: pending
>     purpose: Whether pre-spec reports a method in the plan that waits for a later session, a session of a sprint, the session that closes one, the librarian or a /hi, by one predicate of guppi/lint.py, and leaves alone a method that names the person, a part that opens with after and names its event before a colon, the method of an Estimate of a sprint page, and the live pages
>     ```
>   - change: `the Criterion replaced whole — a method part that opens with after and names its event before a colon is no finding`
> - [ ] read `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`

> **ratification:**
> ```
> - decision[case 781.1][update][rule-case-protocol]{ref:rule-case-protocol}
> - decision[case 781.1][update][estimate-prespec-hook-reports-a-method-that-waits-for-another-session]{ref:rule-prespec-hook}
> ```

### Case 781.2 — Pre-spec accepts a kept method that waits for a named event

> **given:**
> `rule-prespec-hook`: the rule of the check of the plan.
> **＋** `guppi/prespec.py`: `kept_method_waits`, the check of a method kept on a live page.
> **＋** `guppi/lint.py`: the predicate it shares with the check of a method the plan writes.
> **＋** `guppi/ledger.py`: the one predicate of a sprint page `entity-sprint-<id>`.
> **＋** `tests/test_prespec.py`: the tests of the kept method.
> **＋** `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`: its Criterion is replaced whole and its `purpose` set anew.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads an `update` of an Estimate in the `then` blocks of the plan file that replaces its Criterion whole and carries no `set: {method: …}`, and the `method` of that Estimate's live page.

> **then:**
> When a part of that `method` between two `;` names a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or /hi, and does not name the person, the check gives one line `case N: update <slug>: the method on the page waits for another session — set a method that runs in this session`.
> **＋** The judgment is `waits_for_another_session` of `guppi/lint.py`, the same predicate that judges a `method` the plan writes.
> **－** A part of that `method` that opens with `after`, or with `by hand, after`, and names its event before a colon waits for that event and gives no such line.
> **－** An Estimate whose live page holds a sprint page `entity-sprint-<id>` as its `target`, by the predicate of `guppi/ledger.py`, gives no such line.
> **－** An `update` that sets the Estimate `passed` or `failed` by the person's decision gives no such line.
> **－** An `update` that names a part of the page alone, such as a `set` of another field or a `replace` pair, gives no such line.
> **－** A `method` on the page that waits for no other session, or whose part names the person, gives no such line.

> **tasks:**
> - [ ] `guppi/prespec.py`: the docstring of `kept_method_waits` names the part that waits for an event, which the shared predicate passes by (case 781).
> - [ ] `tests/test_prespec.py`: in a test whose name holds `kept_method`, a live page whose method is `by hand, after a pull request from a second account: the output read` gives no kept-method line on an `update` that replaces the Criterion whole.
> - [ ] update `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`
>   - set:
>     ```
>     status: pending
>     purpose: Whether pre-spec reports a Case that replaces the Criterion of an Estimate whole, writes no method and keeps one on the page that waits for another session, by the one predicate of guppi/lint.py, but for an Estimate of a sprint page and a method part that opens with after and names its event before a colon
>     ```
>   - change: `the Criterion replaced whole — a kept method part that waits for an event it names is no finding`
> - [ ] read `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session`

> **ratification:**
> ```
> - decision[case 781.2][update][estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session]{ref:rule-prespec-hook}
> ```

### Case 781.3 — Retro leaves a check that waits for its event pending

> **given:**
> `rule-retro`: the rule rendered into `.claude/skills/retro/SKILL.md`, which sets the readings of Retro.
> **＋** `estimate-retro-loads`: its Criterion is replaced whole.
> **＋** `entity-sprint-<id>`: the live sprint page, whose Estimates already wait.
> **＋** `raw/<date>/<hi HHMM>/spec.md`, `raw/<date>/<hi HHMM>/work.md`, `raw/<date>/<hi HHMM>/frontier.md` and `raw/<date>/<hi HHMM>/handoff.md`: the session files Retro reads and writes.
> **＋** `/work` and `/sprint-close`: the skill that calls Retro, and the skill whose closing Case reads an Estimate of the sprint page.

> **when:**
> The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built.
> **＋** Each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — is read in the reply that ends Retro, on the Criterion of `raw/<date>/<hi HHMM>/spec.md`: the `when` and `then` of its Case, or the Criterion its item writes.
> **＋** For an Estimate of a rule whose Render a Case of the Spec changes, the reading reads the new text of the Render in `raw/<date>/<hi HHMM>/spec.md` against that Criterion.
> **＋** Each such Estimate that Retro cannot read gets a `failed` line in the same `LEDGER` block, whose result opens with the date and says that Retro did not read it and why.
> **＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as this session's for its boxes, for the scope of an edit and for the readings above.
> **＋** Retro closes the open `W` line of each Estimate it reads or sets `failed` `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`.
> **－** An Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose work is not done yet is neither read, nor put to the person, nor set `failed`: it stays `pending` for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, and its `read` box in `raw/<date>/<hi HHMM>/spec.md` waits for that moment, neither debt nor the librarian's.
> **－** Once its work is done, the Retro of that session reads it, or, when its `method` names the person's answer, names it under `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`.
> **－** An Estimate this session creates or updates whose `method` waits for an event — a part of it that opens with `after`, or with `by hand, after`, and names the event before a colon — and whose event has not come in this session is neither read, nor put to the person, nor set `failed`: it stays `pending`, its `read` box in `raw/<date>/<hi HHMM>/spec.md` waits for that event, neither debt nor the librarian's, and when the event came in this session Retro reads it.
> **－** An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`.
> **－** A reading whose `method` names the person's word is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question, and its `read` line is neither debt nor the librarian's.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `` once its work is done, the Retro of that session reads it, or, when its `method` names the person's answer, names it under `## Ask the person` as below (case 772.2). ``
>   - new: `` once its work is done, the Retro of that session reads it, or, when its `method` names the person's answer, names it under `## Ask the person` as below (case 772.2). An Estimate this session creates or updates whose `method` waits for an event — a part of it that opens with `after`, or with `by hand, after`, and names the event before a colon — and whose event has not come in this session is neither read, nor put to the person, nor set `failed`: it stays `pending`, its `read` line waits for that event and is neither debt nor the librarian's, and `handoff.md` names it with its event; once the librarian sees the event, it puts the reading under `Work`, or under `Ask the person` when its `method` names the person's answer. When the event came in this session, read it (case 781). ``
>   - old: `A problem seen live in a later session is a lesson of that session, not a reading.`
>   - new: `` A problem seen live in a later session is a lesson of that session, not a reading, but for the reading of an Estimate whose `method` waits for an event, which a later session takes once the event has come (case 781). ``
>   - change: `Retro leaves an Estimate whose method waits for an event that has not come pending, its read line neither debt nor the librarian's, and the handoff names it with its event (case 781)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] update `estimate-retro-loads`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an Estimate whose method waits for an event that has not come stays pending, its read line no debt`
> - [ ] read `estimate-retro-loads`

> **ratification:**
> ```
> - decision[case 781.3][update][rule-retro]{ref:rule-retro}
> - decision[case 781.3][update][estimate-retro-loads]{ref:rule-retro}
> ```

### Case 781.4 — The handoff names a check that waits for its event

> **given:**
> `rule-handoff`: the rule rendered into `.claude/skills/handoff/SKILL.md`, which sets `## Debt` of the handoff.
> **＋** `estimate-handoff-holds-each-fact-once`: its Criterion is replaced whole.
> **＋** `rule-retro`: sets which Estimates Retro leaves `pending`.
> **＋** `rule-brief`: reads `## What actually got done` of the handoff.
> **＋** `entity-sprint-<id>`: the live sprint page, whose Estimates already wait.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the report the agent writes.

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
> **＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
> **＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
> **＋** An Estimate this session creates or updates has no such line in `## Debt`: the Retro of `rule-retro` read it or set it `failed`, unless the person's answer is its reading. An Estimate of the live sprint page `entity-sprint-<id>` whose work is not done, which that Retro left `pending`, has its line, its moment the Retro of the session that finishes its work or the close of the sprint. An Estimate whose `method` waits for an event that has not come, which that Retro left `pending`, has its line, its moment that event.
> **＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
> **＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
> **－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
> **－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

> **tasks:**
> - [ ] update `rule-handoff`
>   - old: `` but for an Estimate of the live sprint page whose work is not done, which Retro left `pending`: its line names the Retro of the session that finishes its work or the close of the sprint (case 772.3); ``
>   - new: `` but for an Estimate of the live sprint page whose work is not done, which Retro left `pending`: its line names the Retro of the session that finishes its work or the close of the sprint (case 772.3), and for an Estimate whose `method` waits for an event that has not come, which Retro left `pending`: its line names that event (case 781); ``
>   - change: `Debt names an Estimate whose method waits for an event that has not come, which Retro left pending, with its event (case 781)`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] update `estimate-handoff-holds-each-fact-once`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — Debt names an Estimate that Retro left pending while its event has not come`
> - [ ] read `estimate-handoff-holds-each-fact-once`

> **ratification:**
> ```
> - decision[case 781.4][update][rule-handoff]{ref:rule-handoff}
> - decision[case 781.4][update][estimate-handoff-holds-each-fact-once]{ref:rule-handoff}
> ```

### Case 781.5 — The brief holds a reading until its event and proposes a defer for one not taken

> **given:**
> `rule-brief`: the rule rendered into `.claude/agents/librarian-guppi.md`, which sets the brief.
> **＋** `estimate-brief-written`: its Criterion is replaced whole and its `method` set anew.
> **＋** `vault/wiki/brief.md` and `vault/wiki/backlog.md`: the brief the librarian writes, which `/hi` reads, and the list of what is put off; a contradiction of Flags may stand between pages of `vault/archive/`.
> **＋** `raw/<date>/<hi HHMM>/handoff.md` and `frontier.md`: the report of Retro the brief reads, and the Frontier the short brief copies.
> **＋** `entity-sprint-<id>` and `vault/wiki/sprint.md`: the live sprint page and its view.
> **＋** `rule-sprint-close`: the close of a sprint by `guppi sprint-close --apply`.
> **＋** `rule-carry-over`: the second writer of the brief, the skill `carry`.

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items; they stand in `vault/wiki/backlog.md`. Where things stand, Readings due and Readings at the close are as before, and Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
> **＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, an item in one list only, a list with no item the line "none". `Cases` is what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags, one between pages that stand in `vault/archive/` too, a defect the librarian found, with what and from where; and, for each line of `## Debt` of `handoff.md` that names an Estimate whose reading cannot be taken yet, but one of the live sprint page, one whose `method` names the close of a sprint and one whose `method` waits for an event the librarian has not seen, one line that names the Estimate by slug and proposes to defer it into `vault/wiki/backlog.md`.
> **＋** `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, one whose `method` names the close of a sprint — the session that closes a sprint, its librarian's run or the session after it —, one whose `method` waits for an event the librarian has not seen, one that a line of `Cases` proposes to defer and one of an Estimate with `deferred_by`; the unticked boxes of the Specs but the `read` box of such a reading; a ledger line this run did not apply, a dirty tree.
> **＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint. A check of the live sprint page whose `method` names the person's answer stands there once the Retro of the session that finished its work named it in `handoff.md`.
> **＋** In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer.
> **＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
> **－** A reading left out of `Work` and `Ask the person` keeps its line under Readings due.
> **－** A reading whose `method` waits for an event — a part of it between two `;` that opens with `after`, or with `by hand, after`, and names the event before a colon — stands in Readings due alone until the librarian sees that event in `git log`, in the ledger or `handoff.md` of the session, or in the files its `method` names; then it stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer.
> **－** A contradiction of Flags that a line of `## For the next session` of `handoff.md` already carries gets no second line in `Cases`.
> **－** The brief states no decision: the sort by kind is not a judgment of the work.

> **tasks:**
> - [ ] update `rule-brief`
>   - old: `` a defect you found — what and from where (case 761). ``
>   - new: `` a defect you found — what and from where (case 761); and, for each line of `## Debt` of `handoff.md` that names an Estimate whose reading cannot be taken yet, but one of the live sprint page, one whose `method` names the close of a sprint and one whose `method` waits for an event you have not seen, one line that names the Estimate by slug and proposes to defer it into `backlog.md`, since its session did not take its reading (case 781). ``
>   - old: `` but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page and one whose `method` names the close of a sprint, the unticked boxes of the Specs ``
>   - new: `` but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page, one whose `method` names the close of a sprint, one whose `method` waits for an event you have not seen, one that a line of `Cases` proposes to defer and one of an Estimate with `deferred_by` (case 781), the unticked boxes of the Specs ``
>   - old: `` with the question its `method` names when its `method` names the person's answer (case 772.1). ``
>   - new: `` with the question its `method` names when its `method` names the person's answer (case 772.1). A `method` waits for an event when a part of it between two `;` opens with `after`, or with `by hand, after`, and names the event before a colon, such as `by hand, after a pull request from a second account: the hook's output read against the Criterion`. At each run, look for that event in `git log`, in the ledger and `handoff.md` of the session, and in the files its `method` names; once you see it, its reading stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer; until then it stands in Readings due alone (case 781). ``
>   - change: `the brief holds a reading that waits for an event in Readings due until the librarian sees the event, proposes a defer into the backlog for a reading its session did not take, and leaves a deferred Estimate out of Work (case 781)`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] update `estimate-brief-written`
>   - set:
>     ```
>     status: pending
>     method: "by hand at the Retro of the session that changes it: the new Render of rule-brief in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
>     ```
>   - change: `the Criterion replaced whole — a reading that waits for an event stays in Readings due until the librarian sees it, a reading its session did not take is a Cases line that proposes a defer, and a deferred Estimate stays out of Work`
> - [ ] read `estimate-brief-written`

> **ratification:**
> ```
> - decision[case 781.5][update][rule-brief]{ref:rule-brief}
> - decision[case 781.5][update][estimate-brief-written]{ref:rule-brief}
> ```

### Case 781.6 — A defer marks an Estimate as it marks a rule

> **given:**
> `rule-page-generation`: the rule of `guppi generate`.
> **＋** `guppi/generate.py`: the categories a `defer` marks and the order of an Estimate's fields.
> **＋** `guppi/materialize.py`: writes the yaml that `guppi generate` applies.
> **＋** `tests/test_generate.py`: the tests of `guppi generate`.
> **＋** `estimate-generate-writes`: its Criterion is replaced whole.
> **＋** `estimate-generate-fails-alone`: the Estimate of an entry of a shape the script does not know.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/log.md` and `vault/wiki/tags.md`: the files `guppi generate` reads or appends to; the sprint comes from `vault/wiki/sprint.md`, or from `entity-sprint-<id>` when a unit creates it.
> **＋** `vault/archive/`, outside its `raw/` folders: where an entry finds a page that is not under `vault/wiki/`.

> **when:**
> `guppi generate` applies one entry of a yaml to a page.

> **then:**
> A `create` becomes a page: `type`, the fields of the entry, `status` by category (entity and rule `draft`, estimate `pending`, lesson `new`, insight `open`), `origin`, `sprint` — the `sprint` of the yaml, which `guppi materialize` takes from the first `## <id>` of `sprint.md` or, in a unit whose ledger creates `entity-sprint-<id>`, from that `<id>`, `created` — the yaml's date, `tags`; the body sections from `sections`, `## Purpose` from `purpose` on a rule or an entity; a `ref` lands in the parent's `children` or the target's `estimates` with History `child <slug> added` / `estimate <slug> added`, at the end of the run when the parent comes later in the yaml.
> **＋** An Estimate page carries `purpose`, `method` and `checked` as fields, in that order after `target`, and `deferred_by` after `checked` once a `defer` marks it; `## Criterion` from `sections`; neither `## Context` nor `## Method` is written.
> **＋** A `create` whose slug is a placeholder (`draft`, no `kind`) fills it: `created` and `deferred_by` kept, History `created over placeholder`; any other existing page is a collision, not a rename.
> **＋** An `update` applies `set` to the frontmatter, `sections` as whole replacements, `replace` inside the body (whitespace collapsed, exactly one occurrence), History `updated: <change>`; an `update` of an Estimate with `sections.Criterion` replaces the section whole.
> **＋** An `update`, `estimate`, `delete` or `defer` whose slug is not under `vault/wiki/` finds the page under `vault/archive/` (`raw/` folders excluded) and edits it there.
> **＋** An `estimate` sets `status`, overwrites `## Result`, writes `checked` — the date the `result` opens with, else the yaml's date — and appends History `status: a → b · <ledger pointer>`.
> **＋** A `delete` sets `archived` with History `deleted`; a `delete` outside the vault is a line on stdout, the entry applied, no page written.
> **＋** A `defer` with a page appends the decision slug to `deferred_by` (rule, entity, insight, estimate) with History `deferred`; without a page it writes a placeholder `draft` with the Case's fields and `deferred_by`.
> **＋** A `lesson` writes the lesson only, `source` when the line carries it; no Estimate is created.
> **＋** Every ref field is written as `"[[slug]]"`, a list as `["[[a]]", "[[b]]"]`; a slug without a category prefix stays bare; read through the brackets.
> **＋** A `create` in `insights` applies only with the mark `librarian`; a `delete` of an Insight is refused always.
> **＋** History lines and `log.md` lines carry the date of the run and end with `[[decision-case-N]]` or the ledger pointer; `log.md` is appended after each entry; a tag of `new_tags` lands in `tags.md`, a used and undeclared one goes to stderr.
> **－** No body section is derived from a ref field; a section the entry does not name under `sections` or reach by `replace` is not touched.
> **－** An `update` of an Estimate whose `set` carries `method` drops no section.
> **－** `criterion_block` on an `update` and an entry of kind `remove_criterion` are not applied: a shape the script does not know — the entry fails alone (`estimate-generate-fails-alone`).

> **tasks:**
> - [ ] update `rule-page-generation`
>   - change: `a defer marks an Estimate deferred_by as it marks a rule, an entity or an Insight (case 781)`
> - [ ] `guppi/generate.py`: `DEFERRABLE` holds `estimates`; the `estimates` order of `KEY_ORDER` holds `deferred_by` after `checked`; the module docstring and the docstring of `defer` name the Estimate (case 781).
> - [ ] `tests/test_generate.py`: a `defer` of an existing Estimate appends the decision slug to its `deferred_by`, after `checked`, with History `deferred`; a later `supersedes` that names the page clears it.
> - [ ] update `estimate-generate-writes`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a defer marks an Estimate deferred_by, written after checked`
> - [ ] read `estimate-generate-writes`

> **ratification:**
> ```
> - decision[case 781.6][update][rule-page-generation]{ref:rule-page-generation}
> - decision[case 781.6][update][estimate-generate-writes]{ref:rule-page-generation}
> ```

### Case 781.7 — The format of a check page allows deferred_by

> **given:**
> `rule-estimates-schema`: the rule rendered into `vault/wiki/estimates/schema.yaml`, the format of a check page.
> **＋** `guppi/lint.py`: reads the schema for every page of `vault/wiki/estimates/`.
> **＋** `tests/test_schemas.py`: the tests of the schema, read from the live file.
> **＋** `entity-glossary`: the terms, rendered into `vault/wiki/glossary.md`, whose row of `deferred_by` changes.
> **＋** `estimate-estimates-schema-checked`: its Criterion is replaced whole.

> **when:**
> `guppi render` writes `vault/wiki/estimates/schema.yaml` from `rule-estimates-schema`, and `guppi lint` reads a page of `vault/wiki/estimates/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, status, target, method, origin, sprint, created, tags`; optional `purpose, checked, deferred_by`; values `kind: QA | Research`, `status: pending | passed | failed`; the sections `## Criterion` and `## History` required, `## Result` optional, `## Result` required on `passed` and on `failed`.
> **＋** An Estimate page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect.
> **＋** An Estimate page without a `method` field has the finding `schema: missing field method`.
> **＋** `fields` and `sections` describe each name of these lists; `description` holds, among its paragraphs, the introduction, the `failed` paragraph, the fields deliberately absent, the two kinds, and the Result and Criterion paragraph; `examples` holds the example pages.
> **－** `description`, `fields` and `sections` name no `unmigrated` count, no recut of an older page, no `## Context` or `## Method` section, and no `Given:` kept on an older page.

> **tasks:**
> - [ ] update `rule-estimates-schema`
>   - old: `optional: [purpose, checked]`
>   - new: `optional: [purpose, checked, deferred_by]`
>   - old: `` optional; date. The date of the last reading, or of the person's decision that set the status, which the Case writes (case 669.16): the date the Result opens with, else the date of the reading's unit; written by `generate` on every reading (case 201.1). ``
>   - new:
>     ````
>     optional; date. The date of the last reading, or of the person's decision that set the status, which the Case writes (case 669.16): the date the Result opens with, else the date of the reading's unit; written by `generate` on every reading (case 201.1).
>       deferred_by: |
>         optional; list. The Decision pages whose `defer` puts the reading of this Estimate off into `backlog.md`; written by `generate` on a defer and cleared by it on a later `supersedes`, under the condition that `rule-case-protocol` sets, never by hand (case 781).
>     ````
>   - change: `deferred_by is an optional field of an Estimate page (case 781)`
> - [ ] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
> - [ ] `tests/test_schemas.py`: in a test whose name holds `estimate`, an Estimate page in the shape with `deferred_by` has no schema finding.
> - [ ] update `entity-glossary`
>   - old: `` the index line carries it, so `ask-guppi` reaches the deferred decision (case 52.3) ``
>   - new: `` the index line of a rule, an entity or an Insight carries it, so `ask-guppi` reaches the deferred decision (case 52.3); an Estimate carries it too but has no index line, and `backlog.md` lists a deferred one (case 781) ``
>   - change: `deferred_by: an Estimate may carry it, and backlog.md lists a deferred one (case 781)`
> - [ ] `uv run guppi glossary`
> - [ ] update `estimate-estimates-schema-checked`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — deferred_by is an optional field of an Estimate page`
> - [ ] read `estimate-estimates-schema-checked`

> **ratification:**
> ```
> - decision[case 781.7][update][rule-estimates-schema]{ref:rule-estimates-schema}
> - decision[case 781.7][update][estimate-estimates-schema-checked]{ref:rule-estimates-schema}
> - decision[case 781.7][update][entity-glossary]{ref:entity-glossary}
> ```

### Case 781.8 — A reading /hi cannot take stays in Work

> **given:**
> `rule-skill-hi`: the rule of `/hi`, rendered into `.claude/skills/hi/SKILL.md`, whose reading step changes.
> **＋** `estimate-hi-takes-its-readings`: its Criterion is replaced whole and its `purpose` set anew.
> **＋** `rule-brief`: proposes the defer of a reading its session did not take.
> **＋** `vault/wiki/brief.md` and `raw/<date>/<hi HHMM>/frontier.md`: the brief whose readings `/hi` takes and the Frontier it writes.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> Once it writes `raw/<date>/<hi HHMM>/frontier.md`, and before the reply that shows that Frontier asks the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of the Estimate of each open `W` line, judges from that page whether its reading runs now, and judges each reading it takes against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply that shows that Frontier, which ends in text.
> **＋** In the reply that shows that Frontier, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** An open `W` line whose reading cannot run now stays open under `## Work` and is no line under `## Cases`.
> **－** An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person. It is put at the `/hi` whose `vault/wiki/brief.md` opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint. The agent judges this from the line as `vault/wiki/brief.md` gives it, with no page opened.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens pages: the page of the Estimate of each open `W` line.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` a `failed` reading or a lesson of the Tail; an open `W` line whose reading cannot run now, written by the reading step below (case 670.6); an item the person adds. ``
>   - new: `` a `failed` reading or a lesson of the Tail; an item the person adds. ``
>   - old: `` An open `W` line whose reading cannot run now — its method waits for a moment of an earlier session, for a moment not come, or for a `/hi` run of its own — needs a decision: write one line for it under `## Cases` of `frontier.md`, the Estimate by slug in a code span and the words that its method, its Criterion or the page itself is fixed, replaced or archived, with the source `brief`; its `W` line closes `· case N` when that Case is ratified. A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and waits for that session (case 670.5). A `W` line of an Estimate whose `target` is the live sprint page `entity-sprint-<id>` and whose reading cannot run now stays open under `## Work` too and makes no Cases line: it waits for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, as `rule-retro` sets it; judge this from the `target` of its page, with no judgment of whether its work is done (case 778). ``
>   - new: `` An open `W` line whose reading cannot run now stays open under `## Work` and makes no line under `## Cases` (case 781): a `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, waits for that session (case 670.5); one of an Estimate whose `target` is the live sprint page `entity-sprint-<id>` waits for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, as `rule-retro` sets it (case 778); and `handoff.md` names any other, which the librarian's brief puts to the next session as a line that proposes to defer it into the backlog, as `rule-brief` sets it (case 781). ``
>   - change: `an open W line whose reading cannot run now stays open under Work and makes no Cases line (case 781)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] update `estimate-hi-takes-its-readings`
>   - set:
>     ```
>     status: pending
>     purpose: Whether /hi takes, once it writes the Frontier and before the reply that shows it asks the order, each open W reading whose whole method runs now from files and commands, reads no transcript, leaves each other open W line open under Work with no Cases line, puts each open Ask line to the person but one that waits for the close of a sprint or the session after it, writes the answer as its reading line, and opens no page but the Estimates of its open W lines
>     ```
>   - change: `the Criterion replaced whole — an open W line whose reading cannot run now stays open under Work and is no Cases line`
> - [ ] read `estimate-hi-takes-its-readings`

> **ratification:**
> ```
> - decision[case 781.8][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 781.8][update][estimate-hi-takes-its-readings]{ref:rule-skill-hi}
> ```

### Case 781.9 — The Frontier has no Cases source for a reading /hi cannot take

> **given:**
> `rule-skill-hi`: the rule of `/hi`, whose list of Cases sources Case 781.8 changes.
> **＋** `estimate-hi-writes-frontier`: its Criterion is replaced whole.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`: the files the Frontier is assembled from.
> **＋** `raw/<date>/<hi HHMM>/frontier.md` and `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the Frontier and the case file of the opening Case.
> **＋** `entity-sprint-<id>` and `/sprint-open`: the sprint page an opening Case creates, and the skill of that Case.
> **＋** `vault/wiki/orchestration.md`: sets the short Case of a take-back.
> **＋** `/pre-spec` and `ask-guppi`: the check of open Cases lines, and the search agent `/hi` does not call.

> **when:**
> The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md`, the output of the skill's commands and, in the session that opens a sprint, the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of the opening Case, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, closed `[x] … · case N` by the opening Case of `/sprint-open`; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone of `vault/wiki/sprint.md`, or, while that opening line stands, the items of the first milestone that the `create` of `entity-sprint-<id>` writes under `## Milestones` in the case file of the opening Case, with the source `sprint`; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** A line of the `Cases` of the brief's Next session that names the same item as a line of the current milestone makes no line of its own. The milestone line stands as the sprint page, or the opening Case, gives it, with the source `sprint` alone. The agent judges the sameness by meaning, with no page opened.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`. An item closed `defer` or `kept` has no short Case and no ledger line, but for the short Case of a take-back of a ratified Case, as `vault/wiki/orchestration.md` sets it, and a sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** When the first reply of `/hi` shows the Frontier, the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`, and a `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of `vault/wiki/sprint.md` is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** `/pre-spec` finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `estimate-hi-writes-frontier`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — an open W line whose reading cannot run now is no Cases source`
> - [ ] read `estimate-hi-writes-frontier`

> **ratification:**
> ```
> - decision[case 781.9][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}
> ```
