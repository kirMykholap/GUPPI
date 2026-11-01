<!-- approved 00:58:09 · session 8d8876d7 -->

# Session 2307 — the defects of lint and the readings of Case building

## Case 972 — Pre-spec reports a wait written off its form

> **context:**
> A reading by hand that waits for an event writes it in one form: the part of the `method` between two `;` opens with `after`, or with `by hand, after`, and names its event before a colon. `waits_for_an_event` of `.guppi/guppi/lint.py` judges that form by `EVENT_PART`, matched at the start of the stripped part; `waits_for_a_later_moment` and `check_unread` call it, so a `pending` Estimate whose `method` waits this way earns no `unread` finding, and `waits_for_another_session` calls it, so pre-spec lets such a part pass. A part that holds the form behind another word waits for nothing in either reader. The `method` of `estimate-link-graph-at-session-start-writes-the-file` writes `; and by hand, after the first session start whose .claude/settings.json holds the hook: ...`, and the `## Flags` of `vault/wiki/brief.md` report that lint reads it as a reading that does not wait, `unread: pending`. Pre-spec did not catch it when its Case was built: `waits_for_another_session` reports a part only when `ANOTHER_SESSION` finds a later session, the next session, a session after another, a session of a sprint, the session that closes one, the librarian or `/hi` in it, and this part names none of them. The person chose that the form stays one and that pre-spec reports a part that names its event behind another word, by a new predicate in `.guppi/guppi/lint.py` that `.guppi/guppi/prespec.py` imports, as `rule-one-judgment-one-implementation` sets it. The new predicate is built on `EVENT_PART` and on `waits_for_an_event`: a part in which `EVENT_PART` finds its form after a word boundary, and which `waits_for_an_event` does not accept; so `by hand, after X: ...` and `after X: ...` stay clean, and no second pattern of the form is written. Such a part may also name a moment of the Case's own session, which `vault/wiki/case-schema.md` allows, such as the part `by hand at a Case ratified again ... at the reply that closes the last line under Cases after a later message of the person: the transcript, ...` of the `method` of `estimate-prespec-onward-reads-the-decisions-of-the-session`. So, at the finding of `/pre-spec` on this Case, the person chose that pre-spec prints the line as a note: `plan_findings` of `.guppi/guppi/prespec.py` returns the findings and the notes apart, and `check` prints both and exits 1 only on a finding, so a note sets no exit code and does not hold the exit from Plan Mode. `rule-prespec` already sets that a `note:` line is answered in one line in the chat; the text of the note names the two answers. The note covers the kept `method` too: `kept_method_waits` gives its line for an `update` that replaces the Criterion whole, writes no `method` and keeps the `method` of the live page, and the same `update` of `estimate-link-graph-at-session-start-writes-the-file` would keep its `method` with no line, so the new note reads the kept `method` of such an `update` by the same conditions, but for the sprint page, since a part written off the form is the same fault on any target. The Criterion of `estimate-prespec-hook-reports-a-kept-method-that-waits-for-another-session` stays true: it speaks only of the line `KEPT_WAITS`, which this Case leaves as it is, and the note stands beside it. I read `waits_for_an_event`, `waits_for_another_session`, `waits_for_a_later_moment` and `check_unread` of `.guppi/guppi/lint.py`, and `check_form`, `kept_method_waits`, `plan_findings` and `check` of `.guppi/guppi/prespec.py`. The reading of `estimate-link-graph-at-session-start-writes-the-file` was taken in this session, so that page stops being `pending` at the librarian's run, and this Case does not change its `method`. A Grep of ``^method:.*[a-zA-Z0-9)`'] (by hand, )?after\b[^:;]*\S\s*:`` over `vault/wiki/` printed seven files: `estimate-link-graph-at-session-start-writes-the-file`, `estimate-case-check-sends-back-a-faulty-round`, `estimate-render-harness-reproduces`, `estimate-prespec-onward-reads-the-decisions-of-the-session`, `estimate-hi-takes-a-conserved-spec`, `estimate-skill-pr-review-takes-a-pull-request-whole` and `estimate-case-build-writes-a-plain-round`, all under `vault/wiki/estimates/`. I read the `method` of each: the part of `estimate-skill-pr-review-takes-a-pull-request-whole` opens with `by hand, after` and gives no note; each of the other six holds `after ... :` in a part that does not open with it, and all of them but `estimate-link-graph-at-session-start-writes-the-file` are `passed`. The lint run does not call the predicate, so these live pages get no finding; a Case that writes or keeps such a `method` gets the note. The new note is checked by a new Estimate on `rule-prespec-hook`. Several texts state the form, and each stays true, since the form does not change. They are the sentence of `vault/wiki/case-schema.md` on a part that waits for an event, the Renders of `rule-brief` and `rule-retro`, the Criteria of `estimate-prespec-hook-reports-a-method-that-waits-for-another-session` and `estimate-lint-checks-the-statuses`, and the `method` field of `vault/wiki/estimates/schema.yaml`. The Criterion of `estimate-prespec-hook-reports-a-method-that-waits-for-another-session` says that a part in which `after` does not open the part still gives the line of a method that waits for another session; that stays true, since the new note stands beside that line and does not replace it. The Purpose of `rule-prespec-hook` sends the reader to the module docstring of `.guppi/guppi/prespec.py` for what `--check` compares, and says that a line that opens with `note:` does not block, so the page text is not changed and the docstring gains the new note. The lint run does not call the new predicate, so the classes in the docstring of `.guppi/guppi/lint.py` and the text of `rule-lint` stay as they are. A Grep of `[a-z,;] after\b[^":\n]*\S\s*:` over `test_prespec.py`, `test_casecheck.py`, `test_ratified.py` and `test_lint.py` under `.guppi/tests/` printed three files, `test_lint.py`, `test_prespec.py` and `test_ratified.py`; I read each hit, and none is a `method` of a plan that writes the form behind another word, so no test that compares the whole output of `--check` gains the new note. Item C8 of the Frontier, a word of a code span that lint reads as a slug, touches another class of lint and does not clash with this Case.

> **problem:**
> A `method` that writes its wait for an event behind another word, such as `and by hand, after`, waits for nothing in lint and in pre-spec, and no check says so while the Case can still be fixed.

> **recommend:**
> - **How the wait form is fixed**
>   - Recommended: (b) pre-spec reports the near miss — a new predicate in `.guppi/guppi/lint.py`, imported by pre-spec, finds a part that holds the form but does not open with it; the form stays as it is.
>   - Answer: (b).
> - **How pre-spec reports the near miss**
>   - Recommended: (a) pre-spec prints it as a `note:` line, which sets no exit code, and the main agent answers it in one line in the chat: rewritten into the form, or a moment of the Case's own session that is no wait.
>   - Answer: (a).

> **given:**
> `estimate-prespec-hook-reports-a-wait-off-its-form`: the new check of the note pre-spec prints.
> **＋** `rule-prespec-hook`: the rule of the check of the plan, the target of the new Estimate.
> **＋** `.guppi/guppi/lint.py`: the new predicate, beside `waits_for_an_event` and `EVENT_PART`.
> **＋** `.guppi/guppi/prespec.py`: `plan_findings` gains the new note, `kept_method_waits` shares its reading of the kept `method`, and the module docstring names the note.
> **＋** `.guppi/tests/test_lint.py`: the test of the new predicate.
> **＋** `.guppi/tests/test_prespec.py`: the test of the new note.
> **＋** `rule-one-judgment-one-implementation`: one predicate of the form, which both modules import.

> **when:**
> `uv run --project .guppi guppi prespec --check <plan> --session <id>` of `.guppi/guppi/prespec.py` reads, in the `then` blocks of the plan file, the `method` of a `create` of an Estimate, of an `update` that carries `set: {method: …}`, or, for an `update` of an Estimate that replaces its Criterion whole, writes no `method` and sets no status `passed` or `failed`, the `method` of its live page.

> **then:**
> A `method` with a part between two `;` that names an event before a colon behind another word — `after`, or `by hand, after`, after a word boundary but not at the start of the stripped part, such as `and by hand, after the first session start: the file read` — gives one note `note: case N: <create|update> <slug>: method names its event inside a part — open the part with after, or with by hand, after, or answer that it names a moment of this session`.
> **＋** For the `method` of the live page, the note reads `note: case N: update <slug>: the method on the page names its event inside a part —` and the same words after the dash.
> **＋** The note sets no exit code, so it does not hold the exit from Plan Mode.
> **＋** The judgment is one predicate in `.guppi/guppi/lint.py`, built on the pattern that `waits_for_an_event` matches by, which `.guppi/guppi/prespec.py` imports.
> **－** A part that opens with `after`, or with `by hand, after`, and names its event before a colon gives no such note.
> **－** A part in which `after` stands with no colon after it gives no such note.
> **－** The note does not replace the line of a `method` that waits for another session, of a `method` kept on the page that waits for another session, or of a `method` that names no form or that ties its reading to a one-off moment.
> **－** `uv run --project .guppi guppi lint` of `.guppi/guppi/lint.py` over the live Estimate pages gives no finding by this predicate.

```then
create:
- slug: estimate-prespec-hook-reports-a-wait-off-its-form
  ref: rule-prespec-hook
  kind: QA
  purpose: Whether pre-spec prints a note, with no exit code, for a method part that names its event before a colon behind another word, written by the plan or kept on the page by an update that replaces the Criterion whole, by one predicate of .guppi/guppi/lint.py, and leaves alone a part that opens with after or by hand, after
  method: uv run --project .guppi pytest .guppi/tests/test_prespec.py .guppi/tests/test_lint.py -k off_form
  tags:
  - harness
  - workflow
```

```tasks
- [x] create `estimate-prespec-hook-reports-a-wait-off-its-form`
- [x] `.guppi/guppi/lint.py`: a new predicate of a part of a `method` that names its event behind another word — `EVENT_PART` found after a word boundary in the stripped part and `waits_for_an_event` false — with a docstring that names it the one predicate of this judgment, which pre-spec imports and the lint run does not call.
- [x] `.guppi/guppi/prespec.py`: one function gives the `method` that an `update` keeps — it replaces the Criterion whole by `names_a_part`, writes no `method`, sets no status in `DECIDED`, and its live page holds a `method` — which `kept_method_waits` calls with its own check of the sprint page, and the new notes call for every target; a new function of notes gives the note for a `create` of an Estimate, for an `update` that carries `set: {method: …}` and for that kept `method`, whatever the target; `plan_findings` adds it to its notes; the module docstring, under the notes, and the docstrings of the changed functions name the note and the predicate.
- [x] `.guppi/tests/test_lint.py`: a test whose name holds `off_form` runs the predicate over `and by hand, after X: read`, `read after X: read`, `by hand, after X: read`, `after X: read` and `after X`, true on the first two only.
- [x] `.guppi/tests/test_prespec.py`: a test whose name holds `off_form` checks a plan with a `create` and an `update` whose `method` writes `pytest tests/test_x.py; and by hand, after a pull request from a second account: the output read`, one note each and exit 0, and an `update` that replaces the Criterion whole of a live page with that `method`, one note of the method on the page and exit 0; and with the same part opening with `by hand, after`, no note.
- [x] read `estimate-prespec-hook-reports-a-wait-off-its-form`
```

## Case 973 — A bare link in the Result of the link graph Estimate

> **context:**
> `guppi lint` of `.guppi/guppi/lint.py` reads every `[[…]]` in the body of a live page as a link to a page, after `links_of` deletes each code span by `CODE_SPAN`, and `check_refs` reports a link that no live or archived page carries as a `ref` finding. The `## Flags` of `vault/wiki/brief.md` report the finding `estimates/estimate-link-graph-prints-the-neighbours: ref: body names slug, which no live or archived page carries`, and say its cause is the code spans `[[slug]]` and `## <slug or path>` of the Criterion of that page. That cause is wrong: each `[[slug]]` of the Criterion stands inside a code span, which `links_of` deletes. The bare `[[slug]]` stands in the `## Result` of the page, in the words `field, [[slug]], path-field`. The main agent wrote those words at the Retro of session 1831 in the estimate line at line 30 of `vault/raw/2026-10-31/1831/ledger.md`, and `generate` copied the text of the reading into `## Result` as it stood. Lint works as `estimate-lint-finds-a-broken-link` promises: a body `[[…]]` that names no page is a finding, and one inside a code span is no link. The person chose to fix the text of the page alone: the `update` writes the `## Result` whole again, its text as it stands with the bare `[[slug]]` put in a code span. A `replace` pair cannot do it, since its `old` would hold the bare link, and the check of the case file, `check_bare_links` of `.guppi/guppi/prespec.py`, reports a bare `[[slug]]` in each string of the plan. The new text also puts the mention of the session in a bracket of its own and the command and the output that name a Decision page in code spans, since `check_pointers` of `.guppi/guppi/prespec.py`, by `outside` of `.guppi/guppi/pointers.py`, reported them in the first text as pointers outside a bracket of their own; the readings it records do not change. The `update` names a section other than the Criterion, a part alone, so the status, the `## Criterion` and the `method` of the page stand, as the description of `## Criterion` in `rule-estimates-schema` sets it. The check is a new one-time Estimate with `once: true` on the live sprint page `entity-sprint-plugin`, as `rule-estimates-schema` sets for a check of one state of the data; it is read by hand after the librarian's run that applies the `update`, since `guppi check` sees the change only then, and its `method` reads the output of `guppi check` for the finding and the last change of the file of the page by `git log -p -1` for the Result and the parts that stand, both outputs saved in the estimate line, as the field `method` of `rule-estimates-schema` sets for a reading by hand. The Purpose of `entity-sprint-plugin` says that the sprint is done when every Estimate of the page passes, and lists its goals; it stands, since the new Estimate is read before the close and is no goal of the sprint. A Glob `vault/**/estimate-sprint-plugin-check-*.md` printed nothing, so the slug is free. The blocks of both pages in `.guppi/links.md` name `entity-link-graph`, `rule-case-build`, `rule-skill-grill-me`, `entity-sprint`, the sprint Estimates and the rules of the clean branch, the close, the work mode and the setup; none speaks of the text of a Result, so none changes. A Grep of `estimate-link-graph-prints-the-neighbours|entity-sprint-plugin` over `.guppi/tests/` printed three files: `test_links.py`, where the slug stands in the docstring; `test_prespec.py`, which builds the sprint page in a temporary folder; and `test_lint.py`, where the slug stands in the text of a `method`. No test reads the changed text live. Case 972 changes `.guppi/guppi/lint.py` for a wait in a `method`; this Case changes no code, and the `ref` class stays as it is. The brief is written again at each librarian's run, so its wrong cause is left to that run.

> **problem:**
> A bare `[[slug]]` in the `## Result` of `estimate-link-graph-prints-the-neighbours` names no page, so `guppi check` reports a `ref` finding at each run.

> **recommend:**
> - **What the Case fixes**
>   - Recommended: (a) fix the page text only — the bare `[[slug]]` in the `## Result` of `estimate-link-graph-prints-the-neighbours` put in a code span.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) a one-time Estimate with `once: true` on `entity-sprint-plugin`, read by hand after the librarian's run by `guppi check`.
>   - Answer: (a).

> **given:**
> `estimate-link-graph-prints-the-neighbours`: the page whose `## Result` holds the bare link.
> **＋** `estimate-sprint-plugin-check-finds-no-bare-slug-link`: the new one-time check.
> **＋** `entity-sprint-plugin`: the live sprint page, the target of the new check.
> **＋** `.guppi/guppi/lint.py`: the `ref` class that reads the link, unchanged.
> **＋** `vault/wiki/`: the live pages that the lint reads.
> **＋** `rule-estimates-schema`: a one-time Estimate targets the live sprint page.

> **when:**
> `uv run --project .guppi guppi check` runs the lint of `.guppi/guppi/lint.py` over the live pages of `vault/wiki/`, after the librarian's run that applies the `update` of `estimate-link-graph-prints-the-neighbours`.
> **＋** The last change of the file of `estimate-link-graph-prints-the-neighbours` is read by `git log -p -1` on its path.

> **then:**
> It prints no `ref` line for `estimate-link-graph-prints-the-neighbours`.
> **＋** The `## Result` of `estimate-link-graph-prints-the-neighbours` holds `[[slug]]` inside a code span, and the date, the commands, the counts and the outputs of the readings it records as they stood.
> **－** The status, the `## Criterion` and the `method` of `estimate-link-graph-prints-the-neighbours` do not change.

```then
create:
- slug: estimate-sprint-plugin-check-finds-no-bare-slug-link
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether guppi check prints no ref line for estimate-link-graph-prints-the-neighbours once the bare link of its Result stands in a code span, the rest of that page as it stood
  method: 'by hand, after the librarian''s run that applies the update of estimate-link-graph-prints-the-neighbours: the output of uv run --project .guppi guppi check and the output of git log -p -1 -- vault/wiki/estimates/estimate-link-graph-prints-the-neighbours.md, the diff of the Result and of no field or Criterion, read against the Criterion, both outputs in the estimate line'
  once: true
  tags:
  - sprint
  - harness
update:
- slug: estimate-link-graph-prints-the-neighbours
  sections:
    Result: '2026-10-31, Retro (session 1831): uv run --project .guppi pytest .guppi/tests/test_links.py, 13 passed, each line of the Criterion over a vault in a temporary folder (block form, field, `[[slug]]`, path-field and body-name links outside History, agent, skill and command names of a rendered file to the page that renders or runs them, links in, a file in a named folder, purpose lines of a lesson and an insight, no Decision page, an unknown name exits 1); by hand in Work Mode: uv run --project .guppi guppi links .claude/skills/sprint-open/SKILL.md printed "- out agent case-guppi: rule-case-build — Prevents a Case from being shown before one agent has built it …", and uv run --project .guppi guppi links .claude/agents/case-guppi.md printed "- out skill grill-me: rule-skill-grill-me — Prevents an interview from acting on a plan …"; `guppi links decision-case-966` printed `links: decision-case-966 is neither a live page nor a file`, exit 1'
  change: the bare link of the Result put in a code span, so lint reads no link to a page
```

```tasks
- [x] update `estimate-link-graph-prints-the-neighbours`
- [x] create `estimate-sprint-plugin-check-finds-no-bare-slug-link`
- [ ] read `estimate-sprint-plugin-check-finds-no-bare-slug-link`
```

## Case 974 — The builder reads the readers of the folder of a new file

> **context:**
> When `case-guppi` builds a Case that changes what a step writes, the Render of `rule-case-build` makes it search the rules and `.claude/` for the name of that output and read each step that reads it (cases 924, 966). A reader that takes every file of a folder holds no word of a new file there, so that search misses it. `lesson-case-build-names-a-file-without-the-readers-of-its-folder`, written at the Retro of session 1831, records such a miss: Case 967.3 added the generated file `.guppi/links.md`, and the full test run failed on the test of the live code of `test_ship.py`, since the clean copy would carry the graph; Work Mode added the file to `LEFT_OUT` of `.guppi/guppi/ship.py`. I read in `.guppi/guppi/ship.py` the function `tree_files` whole, which walks a folder by `os.walk` and takes each file but the skipped names, `TREES`, which names the folders as bare names `.guppi` and `.claude`, `LEFT_OUT`, and the lines that call `tree_files` over `TREES` and drop each name of `LEFT_OUT`; `.guppi/.gitignore` holds `links.md`, a second reader of the folder that names the file by its bare name. The person chose that, for each new file that is no page of `vault/wiki/`, the builder searches for the path of each folder that holds it and for the calls that walk a folder, reads the ignore files of git there, and reads each reader that takes every file of such a folder; a page that a `create` adds is left out, since the schema of its category and lint set its readers. The change is a new sentence of the Render, after the sentence of cases 924 and 966, and that sentence stands, since it speaks of a reader that names the output. The rule that governs the choice is `rule-atomicity`: a reader that names the output and a reader that walks a folder can fail apart and need different fixes, so the change is checked by a new Estimate, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, and the Criterion of `estimate-case-build-reads-the-readers-of-a-changed-step` stands with its pending reading. The Criteria of `estimate-case-build-reads-the-link-graph-of-what-it-changes` and `estimate-case-build-reads-each-list-of-a-new-member` speak of the link graph and of a member of a list, and stand. A Glob `vault/**/estimate-case-build-reads-the-readers-of-a-new-file*` printed nothing, so the slug is free; the `create` carries a `ref`, so no vault query runs. The lesson reopened `insight-case-build-changes-a-step-without-reading-its-readers`; the person chose that this Case sets it `actioned`, by the form that its schema sets for a decision of the same session, the bare slug `decision-case-974`. The lesson was written in session 1831, so it takes no `{addresses:...}` mark, and the ledger of this session holds no `error` lesson. The block of `rule-case-build` in `.guppi/links.md` names its Estimates and the rules it links; the block of `.claude/agents/case-guppi.md` names `rule-ask`, `rule-case-build`, `rule-guppi-config`, `rule-lint`, `rule-prespec` and `rule-skill-grill-me`, and links in from `entity-guppi` by `code_ref`; the block of the Insight names its lesson and `rule-plugin-install`. None of them states what the builder reads for a new file, so none changes. `.guppi/tests/test_guppi_package.py` takes every file under `.claude` and `.github/workflows` by `rglob` in `callers`, over `CALLERS`, and reads each one live for the old commands `uv run guppi` and `uv run pytest`; the new sentence names neither. That test is itself a reader of a folder that no search of `.guppi/guppi/` would reach, so, by a finding of `/pre-spec`, the search for the calls that walk a folder covers `.guppi/tests/` too, within the person's choice of what the builder searches. The new sentence keeps its pointer in a bracket at its end, as `vault/wiki/case-schema.md` sets for a page with `core: true`. Item C5, the failed `estimate-case-build-reads-each-list-of-a-new-member`, stays its own item by the person's choice: its miss is a list of members, another behaviour with its own fix.

> **problem:**
> A builder that searches for the readers of a new file by its name misses the code that takes every file of the folder, so the miss shows only when a test fails in Work Mode.

> **recommend:**
> - **What the builder searches for a new file**
>   - Recommended: (a) the paths of the folders that hold the file, the calls that walk a folder, and the ignore files of git, then each reader that takes every file of such a folder.
>   - Answer: (a), by the recommendation.
> - **Which new files the search covers**
>   - Recommended: (a) each new file that is no vault page.
>   - Answer: (a), by the recommendation.
> - **How the change is checked**
>   - Recommended: (a) a new Estimate, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, read by hand after the first `/pre-spec` of a session in which a Case adds such a file.
>   - Answer: (a), by the recommendation.
> - **What happens to the reopened pattern note**
>   - Recommended: (a) this Case sets `insight-case-build-changes-a-step-without-reading-its-readers` `actioned`.
>   - Answer: (a), by the recommendation.
> - **Whether item C5 is part of this Case**
>   - Recommended: (a) apart; C5 stays its own Frontier item.
>   - Answer: (a), by the recommendation.

> **given:**
> `rule-case-build`: the rule whose Render gains the sentence on the readers of a folder.
> **＋** `.claude/agents/case-guppi.md`: the agent file rendered from it.
> **＋** `estimate-case-build-reads-the-readers-of-a-new-files-folder`: the new check of the search.
> **＋** `insight-case-build-changes-a-step-without-reading-its-readers`: the pattern this Case actions.
> **＋** `.guppi/guppi/`: the code searched for the paths of folders and for the calls that walk a folder.
> **＋** `.claude/`: the harness searched for the paths of folders.
> **＋** `vault/wiki/`: the pages; its Rule pages are searched, and a new page there starts no search.
> **＋** `.guppi/tests/`: the tests searched for the calls that walk a folder.

> **when:**
> `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, builds a Case with a task that adds a file that is no page of `vault/wiki/`, and is about to answer with its summary.

> **then:**
> It searches `.guppi/guppi/`, `.claude/` and the Rule pages of `vault/wiki/` for the path of each folder that holds the new file.
> **＋** It searches `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`.
> **＋** It reads each ignore file of git in a folder that holds the new file.
> **＋** It reads each reader that takes every file of a folder that holds the new file.
> **＋** Each reader that the new file makes wrong enters the Case, or the `context` of the Case names it and says why it stands.
> **－** A page that a `create` adds under `vault/wiki/` starts no such search.

```then
create:
- slug: estimate-case-build-reads-the-readers-of-a-new-files-folder
  ref: rule-case-build
  kind: QA
  purpose: Whether case-guppi, when a task of its Case adds a file that is no page, searches for the paths of the folders that hold it and for the calls that walk a folder, reads the ignore files of git there and each reader that takes every file of such a folder, and enters each one the new file makes wrong in the Case or names it in context
  method: 'by hand, after the /pre-spec of the first session whose case-guppi runs on the Render of rule-case-build that holds the sentence on the readers of the folder of a new file and in which a Case adds a file that is no page of vault/wiki/: the agent transcript of the case-guppi of that Case, read for each search and reading of the Criterion, and the findings of ask-guppi at that /pre-spec, read in its agent transcript, for a Case that adds a file and misses a reader of its folder; both under ~/.claude/projects/, the count and the transcripts in the estimate line'
  tags:
  - session
  - workflow
  - harness
  - case-build
update:
- slug: rule-case-build
  replace:
  - old: each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924 and 966).
    new: each one the change makes false enters the Case, or `context` names it and says why it stands (as set in cases 924 and 966). When a task of the Case adds a file that is no page of `vault/wiki/` — a generated file, a module, a test or a harness file — Grep `.guppi/guppi/`, `.claude/` and `vault/wiki/rules/` for the path of each folder that holds it, the bare name of the folder too, Grep `.guppi/guppi/` and `.guppi/tests/` for the calls that walk a folder, such as `os.walk`, `rglob`, `glob` and `iterdir`, and read each `.gitignore` in a folder that holds it, since a reader that takes every file of a folder holds no word of a new file there; read each reader that takes every file of a folder that holds the new file, such as a walk that copies every file of a folder; each one the new file makes wrong enters the Case, or `context` names it and says why it stands (as set in case 974).
  change: case-guppi reads, for a new file that is no page, the readers of each folder that holds it
- slug: insight-case-build-changes-a-step-without-reading-its-readers
  set:
    status: actioned
    addressed_by: decision-case-974
  change: 'actioned: case-guppi reads the readers of each folder that holds a new file that is no page (case 974)'
```

```tasks
- [x] update `rule-case-build`
- [x] `uv run --project .guppi guppi render`: `.claude/agents/case-guppi.md`
- [x] create `estimate-case-build-reads-the-readers-of-a-new-files-folder`
- [x] update `insight-case-build-changes-a-step-without-reading-its-readers`
- [ ] read `estimate-case-build-reads-the-readers-of-a-new-files-folder`
```

## Case 975 — The rules schema names a guard that prevents a case

> **context:**
> The rules schema, `vault/wiki/rules/schema.yaml`, the Render of `rule-rules-schema`, says in its opening that a Rule is a standing condition one case can break, with a guard that refuses that case, and in its Enforcement paragraph that in the harness a thing is a Rule when its code is a guard that refuses a case. Some hook Rules refuse nothing: `rule-link-graph-at-session-start` writes `.guppi/links.md` on `SessionStart` and stops no session on an error, and `rule-librarian-report-copy` copies the librarian's report into `report.md` on `SubagentStop`; both pages, read whole, say so in their Purpose. By the letter of the schema neither is a Rule. The schema also contradicts itself, since its own list of what a hook does names a write that refuses nothing, a hook that appends to `log.md` on every page change. Case 967.3 of session 1831 kept `rule-link-graph-at-session-start` a Rule and left this gap to a later Case, as its `context` and the handoff of that session say. The purpose lines of other hook Rules describe a state the hook keeps rather than a call it refuses, such as `rule-compact-recall`, which puts the texts that `/hi` loads back into the context after a compaction, and `rule-spec-capture`, which keeps the approved Spec in a file of the repository. The person chose that a guard refuses a case or prevents it, a hook preventing it when it writes a file or gives the agent a text, and that the change is checked by the Criterion of `estimate-rules-schema-checked` replaced whole. The rule that governs the change is `rule-rules-schema` itself: the check of a Rule, one case that can refute it and something that stops that case, holds for a hook that keeps the state in place, and the new wording keeps a condition no hook, check or render can detect out of `rules/`. A Grep `its code is a guard|refuses a case|refuses that case|with a guard` over `vault/wiki/` printed `entities/entity-glossary.md`, `glossary.md`, `rules/rule-rules-schema.md` and `rules/schema.yaml`: the two sentences of the Render change by two pairs, the row of Rule in `entity-glossary` changes by one pair, and `glossary.md` and `schema.yaml` are rendered from those pages. The row of the glossary is checked by `estimate-glossary-terms-defined`, whose Criterion says that no claim of the meaning of a row contradicts its `where` page; it stands, since the new row agrees with the new schema. The table of `## Terms` of `entity-glossary`, read whole, holds the row of Rule as one sentence of clauses split by semicolons, and the pair changes its first two clauses alone; the rows of Hook, a script behind a Rule page, and of Estimate, on a Rule a test that the guard works, agree with the new row and stand; no other Case of this session writes into the page. The `purpose` and the `method` of `estimate-rules-schema-checked` state no content of the description, the method reading the live file against the Criterion after a librarian's run, so both stand. `estimate-rules-schema-leaf-carries-no-how-it-works` speaks of the section `## How it works` and stands. `rule-hook-registry`, which registers a new hook only with the hook's Rule, agrees with the new wording. The block `## rule-rules-schema` of `.guppi/links.md` names `entity-glossary` as the one neighbour whose purpose bears on the change; the block `## vault/wiki/rules/schema.yaml` names readers of the file by command, none of which reads the prose of `description`. A Grep `(REPO|ROOT|repo_root|LIVE)[^\n]*(rules|schema)` over `.guppi/tests/` printed `test_case_schema.py`, `test_orchestration.py`, `test_generate.py` and `test_schemas.py`; each reads or copies the live `schema.yaml` for its lists of `properties` and `body`, which this Case does not change, so no test fails on the new text. Cases 972, 973 and 974 of this session change none of these pages. The ledger of this session holds no `error` lesson, so no `{addresses:...}` mark stands.

> **problem:**
> The rules schema says a Rule's guard refuses a case, while hook Rules of the vault, such as the one that writes the graph of links at the start of a session, refuse nothing and only keep a file in place, so the schema and those pages contradict each other.

> **recommend:**
> - **What the rules schema says about a hook that refuses nothing**
>   - Recommended: (b) name any hook that makes a state hold instead of refusing a call: a guard refuses the case or prevents it, and a hook prevents it when it writes a file or gives the agent a text, in the opening of the schema, its Enforcement paragraph and the glossary row of Rule.
>   - Answer: (b), as recommended.
> - **How the change is checked**
>   - Recommended: (a) replace the Criterion of `estimate-rules-schema-checked` whole, with a new line on the opening and the Enforcement paragraph; the glossary row stays with its own Estimate.
>   - Answer: (a), as recommended.

> **given:**
> `rule-rules-schema`: the page whose Render holds the opening and the Enforcement paragraph.
> **＋** `vault/wiki/rules/schema.yaml`: the file rendered from it, which lint reads for each page of `vault/wiki/rules/`.
> **＋** `estimate-rules-schema-checked`: its Criterion is replaced whole.
> **＋** `entity-glossary`: the row of Rule, rendered into `vault/wiki/glossary.md`.

> **when:**
> `guppi render` writes `vault/wiki/rules/schema.yaml` from `rule-rules-schema`, and `guppi lint` reads a page of `vault/wiki/rules/`.

> **then:**
> The file equals the Render. Lint reads from it: required `type, kind, purpose, status, estimates, origin, sprint, created, tags`; optional `enforcement, implementation_ref, governs, render_mode, parent, children, deferred_by, applies_to, core`; values `kind: MOC | Leaf`, `status: draft | built | archived`, `enforcement: hook | check | render`, `render_mode: full | partial`, `core: true`; conditional — `hook` and `check` require `implementation_ref`, `render` requires `governs`, `render_mode` and the section `## Render`, `MOC` requires `children` and forbids `enforcement: hook | check`; the sections `## Purpose` and `## History` required, `## Render` and `## How it works` optional.
> **＋** The file also holds `ordered_children: true`, which lint does not read.
> **＋** A Rule page with these fields, values and sections has no `schema` finding; one lacking a required field, with a value outside the list, with a conditional not met or lacking a required section has one finding per defect; a rule with `applies_to` on a live Entity has none.
> **＋** A Rule page in the shape with `core: true`, `origin: guppi` and `sprint: guppi` has no `schema` finding.
> **＋** `fields` and `sections` describe each name of these lists, `core` among them, and the descriptions of `origin` and `sprint` name the value `guppi` on a page with `core: true` in the clean version; `description` holds the introduction, Ordering, MOCs and enforcement, Enforcement, the sentence on the edge Rule → Entity, the one on the guard of the agent's own conduct and the one on the Estimates that a shipped page brings along; `examples` holds the example pages.
> **＋** That last sentence says that a shipped page arrives with each of its Estimates that passed in the repository it came from and whose `method` names no target of the `Makefile`, and that the receiving project writes its other Estimates through its own Cases.
> **＋** The description of `## How it works` under `sections` says that the section is for a MOC alone and that a Leaf carries none, and no example of a Leaf under `examples` carries the section.
> **＋** The opening of `description` says that a Rule's guard refuses a case or prevents it, and the Enforcement paragraph says that in the harness a guard refuses a case or prevents it, a hook preventing a case when it writes the file, or gives the agent the text, whose absence or age would be that case.
> **－** Neither the opening nor the Enforcement paragraph says that a guard must refuse a call for its page to be a Rule.

```then
update:
- slug: rule-rules-schema
  replace:
  - old: 'A Rule is a standing condition one case can break, with a guard that refuses that case when it occurs. The check: can one case refute it, and is there something to refuse that case?'
    new: 'A Rule is a standing condition one case can break, with a guard that refuses that case when it occurs or prevents it from occurring. The check: can one case refute it, and is there something to refuse or prevent that case?'
  - old: 'In the harness a thing is a Rule when its code is a guard — it refuses a case: a hook, a check, a render that refuses drift.'
    new: 'In the harness a thing is a Rule when its code is a guard — it refuses a case: a hook, a check, a render that refuses drift — or it prevents a case: a hook that writes the file, or gives the agent the text, whose absence or age would be that case, so that the case never occurs, such as a hook that writes a file at the start of a session (as set in case 975).'
  change: a guard refuses a case or prevents it; a hook that writes a file or gives the agent a text is a guard
- slug: entity-glossary
  replace:
  - old: 'with a guard that refuses that case when it occurs; the check: can one case refute it, and is there something to refuse it;'
    new: 'with a guard that refuses that case when it occurs or prevents it from occurring, such as a hook that writes a file the session needs; the check: can one case refute it, and is there something to refuse or prevent it;'
  change: 'the row of Rule: a guard refuses a case or prevents it'
- slug: estimate-rules-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — the opening and the Enforcement paragraph name a guard that prevents a case
```

```tasks
- [x] update `rule-rules-schema`
- [x] update `entity-glossary`
- [x] update `estimate-rules-schema-checked`
- [x] `uv run --project .guppi guppi render`: `vault/wiki/rules/schema.yaml`
- [x] `uv run --project .guppi guppi glossary`
- [x] read `estimate-rules-schema-checked`
```

## Deferred

## Case 976 — The reading of the handoff and the failed readings of Case building put off

> **context:**
> The person put off the items left open at the close of Plan Mode of session 2307. Four of them are Estimates: `estimate-handoff-dispatches`, pending, whose reading the brief named from the transcript of session 0431; and `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-orchestration-names-related-cases-in-the-dispatch` and `estimate-orchestration-shows-the-built-case`, which failed at the Retro of session 0431 and were put off by Case 971. No Case of this session reads the first or changes the text whose miss each of the other three found.

> **problem:**
> No Case of this session settles these four readings.

```then
defer:
  - slug: estimate-handoff-dispatches
    type: estimate
    purpose: "The reading of /handoff from the transcript of session 0431 against its Criterion not taken; put off at the close of Plan Mode of session 2307"
  - slug: estimate-case-build-reads-each-list-of-a-new-member
    type: estimate
    purpose: "A builder ran no search for a member already in a list and missed the docstring list of .guppi/guppi/cli.py; put off again at the close of Plan Mode of session 2307"
  - slug: estimate-orchestration-names-related-cases-in-the-dispatch
    type: estimate
    purpose: "The sentence on a related Case in a dispatch named its new Estimate and not the pages it changes; put off again at the close of Plan Mode of session 2307"
  - slug: estimate-orchestration-shows-the-built-case
    type: estimate
    purpose: "A built Case was shown from an answer of case-guppi whose first line was not **Built:**; put off again at the close of Plan Mode of session 2307"
```
