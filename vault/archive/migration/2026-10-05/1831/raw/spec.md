<!-- approved 20:11:31 · session 72240962 -->

# Spec — session 1831, 2026-10-05

## Case 669 — Fifteen Estimates are closed as passed by the person's decision

> **context:**
> Each session reads again the same Estimates and pays for it. Some of them wait for a live event that sessions 1343 and 1616 never brought, though their pytest part is green. Some ask for a long reading of transcripts by hand. Four failed and were put off again and again. The person closes these fifteen as `passed` by decision, not by a reading; a problem seen later comes back as a lesson. The eleven Estimates kept for the close of the sprint, and the eight this session's /hi read `passed`, are not in this Case.
> A state of an Estimate changes today by a reading line or by a Case. A reading line cannot do it here: the hook of `guppi/ledger.py` refuses a reading of a slug that a decision line of the same session creates or updates (case 428.1), and the Spec hook `guppi/ratified.py` writes a Case only after a `LEDGER` block with its decision lines. So each Estimate gets one `update` in this Case. The update sets `status: passed` and `checked`, and writes a new `## Result`. It also writes the page's Criterion back word for word under `sections.Criterion`, since `lift_criterion` of `guppi/materialize.py` replaces the Criterion with the Case's `when` and `then` for an `update` that sets a status and writes none. The new Result opens with the decision and keeps after it the last reading the page held. For `estimate-ask-searches-at-prespec` that reading is L8 of this session's ledger, the `failed` reading of /hi, which the librarian applies before these updates, since the entries go in ledger order. No reading of these pages follows in this session: the hook of Case 670.1 writes a reading of a page the session changes once the mark `retro` stands, but this session's Retro follows its old rendered text and takes no reading of an Estimate the session changes; L8 already stands.
> The decisions that put three of these Estimates off — 647, 657 and 667 on `estimate-case-build-checks-the-finished-case`, 665 on `estimate-case-protocol-case-form`, 666 on `estimate-prespec-confirms-the-findings-once` — each asked whether the frame of an agent or the Criterion changes. Four more stand `current` with one `defer` line each on pages of this Case: 659 on `estimate-case-check-sends-back-a-faulty-case`, 630 on `estimate-spec-write-reaches-the-approved-spec`, and 617 and 622 on `estimate-orchestration-shows-the-built-case`. This Case answers each: the Estimate is closed, and neither the frame nor the Criterion changes. Its decision line on each of these pages carries one `{supersedes:case N}` per decision. A Grep `^deferred_by:` over `vault/wiki/estimates/` printed nothing: `guppi generate` writes `deferred_by` on a rule, an entity or an Insight only, so no field is cleared, and the Decision pages go `superseded`. The Frontier items C1, C5, C6 and C7 of this session are the same four failed Estimates and close with this Case.
> The frame. `case-schema.md` says that `status` is filled mechanically and not written in a Case, and that an `update` of an Estimate carries `set: {status: pending}`. `rule-estimates-schema` says that the first line of a Result is the date of a reading and its command or place, that `checked` is the date of the last reading, that a `failed` Estimate goes to the archive when no one decides to fix it, and that a check that keeps failing is a Lesson. The code already lets an `update` set its own status (`lift_criterion` of `guppi/materialize.py`, case 194.1). By the person's answer at pre-spec, Case 669.16 changes both Renders so that their text and the code say the same. A Grep of the fifteen slugs over `vault/wiki/`, with `decisions/`, `log.md` and `brief.md` left out, printed 45 occurrences in 25 files. Most name a slug as a record: the `estimates` lists and History lines of the target rules, History lines of Estimates, lessons and an Insight. The others stand in a Criterion or a Result. The Result lines of `estimate-plan-mode-names-its-estimates`, `estimate-retro-loads`, `estimate-work-mode-takes-the-work-readings`, `estimate-generate-writes` and `estimate-materialize-assembles` are records of a past reading and stand. The Criterion lines of `estimate-case-protocol-case-form` and `estimate-ask-searches-at-prespec` point to another Estimate by its slug, which stays true. The Criterion line of `estimate-case-check-sends-back-a-faulty-case` keeps an old path of the check "until a reading of `estimate-case-build-writes-the-case` passes live". The same Grep over `guppi/`, `tests/` and `.claude/` printed `guppi/casecheck.py`, which holds the same condition, and `tests/test_prespec.py`, a comment that names its Estimate. The condition stands, since this Case takes no reading; the old path stays until a Case of a later session removes it. A Grep of the `- [ ] read` lines of these slugs over `vault/raw/` printed 31 lines in 13 files, among them unticked lines of `raw/2026-10-05/1616/spec.md` and `raw/2026-10-05/0311/spec.md`. They stand unticked: `generate` ticks a read line only for a reading, and the brief of `librarian-guppi` lists only an Estimate that stands `pending` or `failed`. When every live Estimate of a target rule stands `passed`, the cascade of `generate` sets that rule `built`, as `estimate-generate-cascades` promises. `estimate-lint-checks-the-statuses` makes each `pending` or `failed` Estimate a finding `unread`, and a `passed` page with no `## Result` a `status` finding; each page of this Case leaves the first and carries a Result. Both Criteria stand. `estimate-sprint-close-settles-unread-estimates` settles what stands `pending` or `failed` at the close of the sprint; this Case acts before that close, so its Criterion stands too.
> The check of this Case is `estimate-generate-writes`, which stands `passed`: its Criterion says that an `update` applies `set` to the frontmatter and `sections` as whole replacements. That is all this Case asks of the scripts, so its Criterion stands. The check of 669.16 is `estimate-materialize-changes-a-named-part-alone`, which stands `passed`: its Criterion says that an `update` item that carries `set.status` keeps the status it set and the Criterion it writes under `sections: Criterion`. The new sentences of the Renders say the same, so its Criterion stands. `estimate-case-protocol-loaded` promises that `case-schema.md` equals its Render and holds the form, and `estimate-estimates-schema-checked` that lint reads `schema.yaml` as rendered and that its `description` keeps its paragraphs; the changed sentences keep both true. The person asked for one Case. The check of `rule-case-check` counts each `update` that sets the state of an Estimate as one promise, so the Case holds one sub-case per Estimate, 669.1 to 669.15, under one parent, and 669.16 brings the two schemas in line with them. The `then` lines of the sub-cases share most of their words, and the check notes this: each sub-case does the same act on another page, and only the slug differs; 669.16 writes into the schemas the same act as a rule, so its lines on the Result and on `checked` echo theirs. The notes stand, since the check that asks for the split leaves no other form. The parent's `given`, which 669.1 to 669.15 share, holds more than seven lines for that reason.
> Case 670 of this session sets that Retro reads each Estimate the session creates or updates, or sets it `failed` (670.2), and that the handoff lists none of them as a reading that waits (670.3). Its exception leaves alone an `update` that sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, so it covers these fifteen in later sessions. In this session Retro and the handoff still follow their old rendered text, and by it `handoff.md` would name the fifteen as readings of a later session. Case 669.16 therefore holds a task that `handoff.md` of this session names none of them so, and names the file of Case 670 in its `given`. Case 670.4 and Case 671.2 update `rule-case-protocol` too, in the paragraph on a `create` of an Estimate, in the paragraph on the boxes of the Spec and in the Splitting section; the pairs of 669.16 stand in other sentences, and the new texts do not contradict each other.

> **problem:**
> Fifteen Estimates come back at every session as readings due. Some wait for an event that does not come, some cost a long reading by hand, and four failed and were put off again and again. The person decided to close them all as `passed`, and to treat a problem seen later as a lesson.

> **recommend:**
> - **How the Case sets the 15 checks to passed**
>   - Recommended: (a) one change per check in this Case: the state set to `passed` and the date to today, a result text written, and the promise written back word for word; complete on its own and dependent on no Case not yet written.
>   - Answer: agreed, (a).
> - **What the result text of each check says**
>   - Recommended: (a) the person's decision first, then the last reading kept unchanged, so the known faults stay on the page.
>   - Answer: agreed, (a).
> - **Whether the known faults of the four failed checks become lessons now**
>   - Recommended: (a) no lesson now; a lesson is written only when a fault is seen again in later work.
>   - Answer: agreed, (a).
> - **What happens to the put-off decisions on three of the checks**
>   - Recommended: (a) this Case retires them: the change on each of the three pages marks each put-off decision on it as replaced by this Case.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at pre-spec the main agent put to the person that the text of `case-schema.md` and of the Estimate schema forbids a Case to set the status of an Estimate, while the code allows it; the person agreed to option (a), a new sub-case that updates `rule-case-protocol` and `rule-estimates-schema` so that a Case may, by the person's decision, set an Estimate `passed` or `failed` with its Criterion written back unchanged, its Result opening with the date and the place of the decision, and `checked` the date of the decision.
>   - Taken: Case 669.16 makes these changes, and holds the task that this session's `handoff.md` names none of the fifteen as a reading that waits; 669.6, 669.7 and 669.10 also retire the decisions that put their Estimates off, by the answer to the question on put-off decisions.

### Case 669.1 — The check that pre-spec catches a superseded Case is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-prespec-catches-a-superseded-case` at the librarian's run of the session.

> **then:**
> `estimate-prespec-catches-a-superseded-case` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-prespec-catches-a-superseded-case` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-prespec-catches-a-superseded-case` stand as they were.
> **－** No reading line is written for `estimate-prespec-catches-a-superseded-case`: the state comes from the decision.

```then
update:
- slug: estimate-prespec-catches-a-superseded-case
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `uv run guppi prespec --check <plan> --session <id>` reads a plan and the record lines of the session's window, and a decision line of the window carries `{supersedes:case N}`.

      Then:
      A `{supersedes:case N}` in the session's window while `## Case N` or `### Case N` still stands in the plan is a finding `case N: superseded by case M, still in the plan`.
      **＋** A heading of a sub-case of Case N, at any depth, that still stands in the plan is the same finding under the number of that sub-case.
      **＋** A decision line of Case N or of a sub-case of Case N, N superseded by a line of the window, is no finding "no Case N heading", needs no item in the plan and asks for no `tasks` block.
      **＋** A `{supersedes:case N.M}` covers Case N.M and its own sub-cases; the parent with its other sub-cases stays.
      **＋** Whether a tag covers a Case is judged by `in_family` of `guppi/materialize.py`, the function that the Spec hook and `guppi materialize` read the tag by.
      **－** A `{supersedes:case N}` on a Case of an earlier session — a defer taken up — finds no heading N in the plan and is no finding.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-09-29, uv run pytest tests/test_prespec.py -k supersed: 8 passed; live, the /pre-spec of session 1432, whose window holds {supersedes:case 511.2} on the lines of Case 512: both runs print no finding on 511.2, the plan holds no ### Case 511.2 heading, its decision lines ask for no item, and Case 511 stands with 511.1; the finding of a superseded Case still in the plan was not met live'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-prespec-catches-a-superseded-case`
```

### Case 669.2 — The check that Retro leaves out the sub-cases of a superseded Case is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` at the librarian's run of the session.

> **then:**
> `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and says that no reading was taken before it.
> **＋** The Criterion, `purpose` and `method` of `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` stand as they were.
> **－** No reading line is written for `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`: the state comes from the decision.

```then
update:
- slug: estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      The skill of `rule-retro` sorts the boxes of a session whose ledger holds a decision line carrying `{supersedes:case N}`, Case N having sub-cases with decision lines, and the skill of `rule-handoff` then writes `handoff.md`.

      Then:
      Retro counts no line of Case N or of any of its sub-cases as debt.
      **＋** The `## What actually got done` section of `handoff.md` lists neither Case N nor any of its sub-cases among the Cases ratified.
      **－** A tag that names Case N.M leaves out N.M and its own sub-cases only; the parent and its other sub-cases are counted.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. No reading was taken before it.'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case`
```

### Case 669.3 — The check that synthesis reads the status its yaml sets is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-synthesis-reads-the-status-its-yaml-sets` at the librarian's run of the session.

> **then:**
> `estimate-synthesis-reads-the-status-its-yaml-sets` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-synthesis-reads-the-status-its-yaml-sets` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and says that no reading was taken before it.
> **＋** The Criterion, `purpose` and `method` of `estimate-synthesis-reads-the-status-its-yaml-sets` stand as they were.
> **－** No reading line is written for `estimate-synthesis-reads-the-status-its-yaml-sets`: the state comes from the decision.

```then
update:
- slug: estimate-synthesis-reads-the-status-its-yaml-sets
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `librarian-guppi`, at synthesis, hangs a lesson entry on an Insight of the same pattern that stands `open` on disk, while an `update` entry of a decision in the same `materialize.yaml` sets that Insight `actioned` with `addressed_by: decision-case-M`, and `guppi/generate.py` then applies the yaml.

      Then:
      A lesson entry with no `addressed_by` gives an `update` of the Insight with `children` plus the lesson and `set: {status: open}`.
      **＋** After `guppi/generate.py` runs, the Insight stands `open` and the lesson stands `clustered`, not archived.
      **＋** A lesson entry with `addressed_by: decision-case-N` gives an `update` with no `status`: it carries `set: {addressed_by: decision-case-N}` when case N is later than case M, compared number by number, and no `addressed_by` otherwise; the Insight stays `actioned`.
      **＋** `vault/wiki/brief.md` reports the pair beside the synthesis.
      **－** An Insight that is not `actioned` on disk and that no decision entry of the yaml sets `actioned` takes no `status` from the lesson.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. No reading was taken before it.'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-synthesis-reads-the-status-its-yaml-sets`
```

### Case 669.4 — The check that the case check requires a backlog item decided on its page is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-case-check-requires-a-backlog-item-decided-on-its-page` at the librarian's run of the session.

> **then:**
> `estimate-case-check-requires-a-backlog-item-decided-on-its-page` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-case-check-requires-a-backlog-item-decided-on-its-page` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-case-check-requires-a-backlog-item-decided-on-its-page` stand as they were.
> **－** No reading line is written for `estimate-case-check-requires-a-backlog-item-decided-on-its-page`: the state comes from the decision.

```then
update:
- slug: estimate-case-check-requires-a-backlog-item-decided-on-its-page
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` reads the Cases of that file, the session's `vault/raw/<date>/<hi HHMM>/frontier.md`, and the pages of the vault.

      Then:
      For each open line of the Frontier whose source is `backlog`, each page that its title names in a code span and that carries `deferred_by` is checked against each top-level Case N of the file that, itself or through a sub-case, names that page on a decision line other than a `defer`.
      **＋** Case N gets a finding for each Decision M of the page's `deferred_by` when no Case among Case N and its sub-cases in the file both names the page on such a line and carries `{supersedes:case M}`. The finding names the Frontier line, the page and the missing mark. The hook exits 2, and `case-guppi` fixes the file.
      **＋** The judgment is the function of `guppi/prespec.py` that the pre-spec check runs, imported, not copied.
      **－** A Case of the file that names no such page, a file while no open line of the source `backlog` stands, and a page without `deferred_by` get no finding of this check.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-09-28, `uv run pytest tests/test_casecheck.py -k backlog` 6 passed; by hand, session 0000: the first answers of case-guppi on items taken from the backlog — C5 (`insight-case-build-promise-lines-compared-by-no-check`, no `deferred_by`) and C6 (`insight-workflow-code-live-before-the-page-it-reads`, `deferred_by` 238), C6 answered with `{supersedes:case 238}` on 473.2, the line that names the page; the store holds both Cases with no finding, as the Criterion says'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-case-check-requires-a-backlog-item-decided-on-its-page`
```

### Case 669.5 — The check that the case check shows only the checked Case is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-case-check-shows-only-the-checked-case` at the librarian's run of the session.

> **then:**
> `estimate-case-check-shows-only-the-checked-case` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-case-check-shows-only-the-checked-case` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-case-check-shows-only-the-checked-case` stand as they were.
> **－** No reading line is written for `estimate-case-check-shows-only-the-checked-case`: the state comes from the decision.

```then
update:
- slug: estimate-case-check-shows-only-the-checked-case
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

      Then:
      `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same.
      **＋** Under the heading of a top-level Case, one `ratification` whose fence holds the ledger lines of its sub-cases, as the list of a showing holds them, is read as the showing of each sub-case whose id a line names: the lines that name that id are compared with the `ratification` of that sub-case in the store, and a stored line that is missing or a line the store lacks is a difference.
      **＋** A section the reply does not show is not compared: a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the stored text and `raw/<date>/<hi HHMM>/cases/case-<N>.md` equals the store, as `estimate-case-check-refuses-a-changed-case-file` sets it.
      **＋** The name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared.
      **＋** A Case the store does not hold, a Case that differs in a compared section, a Case stored with findings, a Case whose file differs from the store, or a Case with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2, the reason and the findings on stderr.
      **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
      **＋** The Spec hook `guppi/ratified.py` judges a showing by the same comparison, and a sending by the same reading of the transcript, both imported from `guppi/casecheck.py`.
      **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared and need no sending.
      **－** On the re-fire (`stop_hook_active`) it exits 0.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-10-02, uv run pytest tests/test_casecheck.py -k stop: 25 passed; by hand, session 1834: the Stop check refused the first showing of case 595, whose ratification fence stood outside the quoted section, with "case 595: its ratification differ from the answer of case-guppi"; the showing again with the fence inside the blockquote passed'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-case-check-shows-only-the-checked-case`
```

### Case 669.6 — The check that the case check sends back a faulty Case is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-case-check-sends-back-a-faulty-case` at the librarian's run of the session.

> **then:**
> `estimate-case-check-sends-back-a-faulty-case` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-case-check-sends-back-a-faulty-case` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-case-check-sends-back-a-faulty-case` stand as they were.
> **＋** No decision that put off `estimate-case-check-sends-back-a-faulty-case` stands `current`.
> **－** No reading line is written for `estimate-case-check-sends-back-a-faulty-case`: the state comes from the decision.

```then
update:
- slug: estimate-case-check-sends-back-a-faulty-case
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `SubagentStop` fires when `case-guppi` stops; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

      Then:
      `uv run guppi casecheck --subagent` takes each file under the `cases/` folder of a session folder, judged by `is_case_file` of `guppi/casecheck.py`, that a `Write` or `Edit` call of the subagent in `agent_transcript_path` names, and reads its Cases as the file stands now.
      **＋** A file whose Cases `<plan>.checked.json` already holds with the same text, line ends and trailing spaces aside, and with no findings is not checked or stored again, so the time of its store stands.
      **＋** Any other such file is checked whole: each Case is read in the chat form by the functions of `guppi/ratified.py`, its section of the Spec is built in memory as the Spec hook writes it, and `judge` of `guppi/prespec.py` runs over them, the decision lines of the `ratification` fences standing for the ledger and, with the session's window, giving the categories whose schema rule the session changes.
      **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
      **＋** Each Case of the file is stored, its text as the file holds it, with its findings and the time of the store, in `<plan>.checked.json`; the hook does not write that file.
      **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` fixes the file and stops again, whatever `stop_hook_active` says.
      **＋** Until a reading of `estimate-case-build-writes-the-case` passes live, a transcript that names no such file and whose newest output holds a Case heading is read the old way: that output is checked and stored as the Cases of a file are, and with no finding the hook writes it into `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the whole file when it holds the top-level Case, the section of each sub-case otherwise. A Case of a later session removes this path.
      **－** A finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged file is not sent back twice.
      **－** An output of the subagent with no Case heading — a summary, a round or a `**Fact:**` answer — is not read as a Case; the form of a round is the promise of `estimate-case-check-sends-back-a-faulty-round`.
      **－** A subagent of another type, and a transcript the hook cannot read, get none of these checks, and nothing is stored. A session with no plan file is not sent back for a fault of a Case.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-10-04, the Work readings of session 0112: `uv run pytest -q tests/test_casecheck.py -k subagent` 72 passed, 45 deselected; live in session 0112 (transcript b76bfabb): the SubagentStop hook sent back the answer of Case 625 (agent a309e5b8dc383eed8) with "casecheck: case 625: /box is not named in its given; case 625: /pre-spec is not named in its given", and case-guppi answered again; the store glimmering-waddling-wigderson.checked.json holds 624, 625, 626, 626.1 and 626.2, each with its agent_id, the time of the store and no findings; cases/case-625.md was written at 02:24:10.05 after its store at 02:24:09.93, and cases/case-626.md, holding 626, 626.1 and 626.2, at 02:30:50.09 after its store at 02:30:49.96; a live round after a built Case: agent ad744674f53077ad2 built Case 626 at 02:09:40 and, sent the findings of /pre-spec, answered with the round Q6 at 02:23:52, which no hook feedback followed; the store and the file now hold the answer of 02:30:49, so their state between the round and that answer was not recorded and rests on the tests; not exercised: a `**Fact:**` answer'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-case-check-sends-back-a-faulty-case`
```

### Case 669.7 — The check that the Spec write reaches the approved Spec is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-spec-write-reaches-the-approved-spec` at the librarian's run of the session.

> **then:**
> `estimate-spec-write-reaches-the-approved-spec` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-spec-write-reaches-the-approved-spec` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and says that no reading was taken before it.
> **＋** The Criterion, `purpose` and `method` of `estimate-spec-write-reaches-the-approved-spec` stand as they were.
> **＋** No decision that put off `estimate-spec-write-reaches-the-approved-spec` stands `current`.
> **－** No reading line is written for `estimate-spec-write-reaches-the-approved-spec`: the state comes from the decision.

```then
update:
- slug: estimate-spec-write-reaches-the-approved-spec
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      The `Stop` hook `uv run guppi ratified` has written a ratified Case N from the text stored under it into the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

      Then:
      The hook writes the same stored text of Case N into `spec.md`: the heading, `context`, `problem`, `recommend`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
      **＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
      **＋** A task line whose text stood in a replaced section keeps the box it had there.
      **＋** The `context`, `problem` and `recommend` of a sub-case's parent, written into `spec.md` and into the plan file, come from the text stored under the parent, never from the reply.
      **＋** With `stop_hook_active` set, the hook writes into `spec.md` as without it, as `estimate-spec-write-answers-a-refusal` sets it.
      **－** Nothing written into `spec.md` is translated or refused for its language.
      **－** A refusal that writes nothing of Case N into the plan file writes nothing of it into `spec.md`.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. No reading was taken before it.'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-spec-write-reaches-the-approved-spec`
```

### Case 669.8 — The check of the vault query before a create is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-ask-query-before-a-create` at the librarian's run of the session.

> **then:**
> `estimate-ask-query-before-a-create` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-ask-query-before-a-create` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and says that no reading was taken before it.
> **＋** The Criterion, `purpose` and `method` of `estimate-ask-query-before-a-create` stand as they were.
> **－** No reading line is written for `estimate-ask-query-before-a-create`: the state comes from the decision.

```then
update:
- slug: estimate-ask-query-before-a-create
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `case-guppi`, following `.claude/agents/case-guppi.md`, builds a Case that proposes a `create` without a `ref` and, before it answers, runs itself the vault query of `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

      Then:
      It starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
      **＋** A page that already holds the thing is found by meaning, whether the person's words name it in Russian or in English, and the `context` of the Case names its slug.
      **＋** A proposal that crosses a rule or a lesson, such as a `SessionStart` hook meant to block, names that rule or lesson in the `context`.
      **＋** The slug the Case writes is checked by a Glob over `vault/archive/`, and the `context` says it is free, live with its category, or archived at its path by the Decision that the archived page's `origin` names.
      **＋** An archived page is opened only when the question names its slug and asks what it said or why it was withdrawn.
      **－** The archive is not searched by meaning: a page the `context` names as existing or near is a live page.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. No reading was taken before it.'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-ask-query-before-a-create`
```

### Case 669.9 — The check that case-guppi writes the Case is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-case-build-writes-the-case` at the librarian's run of the session.

> **then:**
> `estimate-case-build-writes-the-case` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-case-build-writes-the-case` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-case-build-writes-the-case` stand as they were.
> **－** No reading line is written for `estimate-case-build-writes-the-case`: the state comes from the decision.

```then
update:
- slug: estimate-case-build-writes-the-case
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it by `SendMessage` the person's answers to a round, or the person's question or change on a Case it built.
      **＋** Or the hook of `rule-case-check` sends it findings on the file of its Case or on its summary.

      Then:
      `case-guppi` starts with `.claude/skills/grill-me/SKILL.md` in its context by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, and reads `vault/wiki/case-schema.md` and `vault/wiki/ratification.md` whole before it answers.
      **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
      **＋** It reads each page and file the `given` names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`; each contradiction is fixed in the Case, or the `context` says why it stands.
      **＋** While a fork is open — the bound, the alternative, the promise, the split, the exceptions or what is left not done — its answer is a round of questions in the form of `.claude/skills/grill-me/SKILL.md`, in English, with no Case heading and nothing else but the context of a first round.
      **＋** The first round on an item opens, before its first question, with one prose paragraph under the label `**Context:**`: what the item is about, what the thing does today and where it goes wrong, and what the round decides — a sentence per part where one is enough, a part with nothing to say left out.
      **＋** When no fork is open, it writes the Case whole in English in the chat form of `vault/wiki/case-schema.md`, its ledger lines in the form of `vault/wiki/ratification.md`, from the heading to the fence of `ratification` and nothing else, into `raw/<date>/<hi HHMM>/cases/case-<N>.md` by `Write`, N the id of the top-level Case.
      **＋** Its answer is then a summary alone: a first line `**Built:**` and the path of the file; a second line `**Case:**` with the id and the name of the top-level Case as the heading of the file writes them, a Case with sub-cases included; then one list item per Case and sub-case with its id and name, the Estimate that checks it and one line on what that Estimate checks, and under the item its ledger lines in an untagged fence, as the file holds them.
      **＋** When the `context` of a Case says that another Case of the session should change instead, the item of that Case in the summary carries a line `**Other Case:**` that names the other Case and the change it needs.
      **＋** Sent findings by the hook on the file, or asked for a change by a message, it changes the file by `Edit` of the lines that change and answers with the summary again; sent a finding on its summary alone, it answers with the summary again and leaves the file as it stands; asked by a message that opens a fork, it answers with a round.
      **＋** A round may come at the first answer on an item, after a message on a Case it built, and in Work Mode when a ratified Case is built again.
      **＋** It runs on `model: opus` with `effort: medium`, the tools Read, Grep, Glob, Write and Edit, and `permissionMode: acceptEdits`, so it writes its file with no prompt while the session is in Plan Mode.
      **－** The `**Case:**` line is no Markdown heading, so the hook of `rule-case-check` does not read the summary as a Case.
      **－** It does not write the whole Case again to fix a finding or make a change.
      **－** A later round on the item, a round after a message on a Case it built and a round in Work Mode carry no context.
      **－** The context carries no Case heading, so the hook of `rule-case-check` neither checks nor stores the round as a Case; it judges only the form of the questions of the round, not its context.
      **－** It writes no file but the file of its Case, and no ledger line.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-10-03, by hand at the Work readings of session 0317, the dispatches of case-guppi in Plan Mode read against their transcripts under subagents/ and the chat: `.claude/agents/case-guppi.md` carries model opus, effort medium, tools Read, Grep, Glob and skills [grill-me]; each of the three agents read vault/wiki/case-schema.md and vault/wiki/ratification.md whole as its first two calls; an item with a fork (611, 612, 613) was answered by a round in the grill-me form, the first round on each item opening with a `**Context:**` paragraph and the later rounds (612 Q6, Q7–Q9; 613 Q6–Q7, Q8–Q9) with none, then by the Case alone; Case 612 makes a create without a ref (`rule-sprint-close`) and its context gives the vault query of ask-guppi (exists none, near, rules, tags); Case 611 changes the Stop hook of guppi casecheck and its builder grepped `.claude/settings.json` for the Stop hooks, the context naming the six commands on Stop; no file and no ledger line written by case-guppi. Tokens and seconds per dispatch: 611 round 61,745 / 70.6 s, Case 99,751 / 200.4 s, rebuild after pre-spec 116,156 / 84.9 s; 612 round 74,257 / 158.4 s, Q6 76,735 / 19.8 s, Q7–Q9 91,142 / 67.5 s, Case 168,393 / 342.6 s, rebuild 179,771 / 70.5 s; 613 round 94,175 / 153.7 s, Q6–Q7 103,885 / 50.5 s, Q8–Q9 109,831 / 40.9 s, Case 184,880 / 468.4 s, rebuild 201,458 / 110.7 s'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-case-build-writes-the-case`
```

### Case 669.10 — The check that the main agent shows the built Case is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-orchestration-shows-the-built-case` at the librarian's run of the session.

> **then:**
> `estimate-orchestration-shows-the-built-case` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-orchestration-shows-the-built-case` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-orchestration-shows-the-built-case` stand as they were.
> **＋** No decision that put off `estimate-orchestration-shows-the-built-case` stands `current`.
> **－** No reading line is written for `estimate-orchestration-shows-the-built-case`: the state comes from the decision.

```then
update:
- slug: estimate-orchestration-shows-the-built-case
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      The main agent takes up a Frontier item, the person answers a round of questions, answers a shown Case with a question or a change, or asks for a plain explanation of the agent's text — by `/wait-what` on `UserPromptSubmit` or in words — or a ratified Case changes and is shown again, in Plan Mode or in Work Mode, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`.

      Then:
      The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
      **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case that is not a request for a plain explanation.
      **＋** A request for a plain explanation of a round, of the short text on a Case or of a reply the main agent answers itself by `.claude/skills/wait-what/SKILL.md`; it sends the `case-guppi` of the Case a `SendMessage` only to ask for a fact of the Case, and `case-guppi` answers with the fact alone, under a first line `**Fact:**` and with no Case heading.
      **＋** An answer with no first line `**Built:**` and no first line `**Fact:**` is a round of questions: the main agent shows it in the chat translated into Russian line by line, slugs, paths and quotations unchanged, each quotation in its blockquote — the `**Context:**` paragraph that opens the first round on an item translated in place before the first question, each question in the order and with the number of the answer, opening with its `❓ **Qn** - **<title>**:` line of `.claude/skills/grill-me/SKILL.md` and closing with its `➡️` line, its title, body and recommended answer translated in place, nothing merged, dropped or added between the questions, the agent's own text after the last question and one horizontal rule; no Case is shown, no file is sent, and no step of confirmation follows the last round.
      **＋** The main agent shows a built Case at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the file `case-guppi` wrote and the hook of `rule-case-check` checked. In the same reply it writes the heading of the top-level Case: its id, and its name in Russian translated from the `**Case:**` line of the summary `case-guppi` answered with. Under the heading it writes one list with an item per Case and sub-case of the summary: its id, its name in Russian, and a short text in Russian on what done means and how it is checked, taken from the Estimate the summary names for it. Then it writes one `ratification` with the ledger lines of every Case of the list as the summary holds them, and its own text after one horizontal rule. A summary in which a Case names no such Estimate goes back to its `case-guppi` by `SendMessage` before the Case is shown.
      **＋** A Case whose item in the summary carries a line `**Other Case:**` is shown as it stands, and the main agent asks the person whether that other Case is built again.
      **＋** A reply that shows a Case and that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the summary holds it; a reply that shows a round and that the `Stop` check refuses is followed, before the person answers, by a reply that shows the round again with nothing before its `**Context:**` paragraph or its first question.
      **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new file is sent and ratified again; the main agent edits no Case in the plan file or under `cases/`.
      **＋** An item that needs no decision the main agent closes alone, with no dispatch; it dispatches `ask-guppi` only at pre-spec, one run per top-level Case at its first run, never to build a Case, and asks a run again only to confirm its own findings.
      **－** The main agent writes the heading, the list, the `ratification` and the question on another Case from the summary, and does not read the file of the Case.
      **－** The heading carries no name of the main agent's own and not the words of the Frontier item.
      **－** The main agent writes no context of its own before the first question of a round.
      **－** The main agent writes no `given`, `when`, `then` or `tasks` of a built Case into the chat.
      **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch and no file.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-10-05, by hand at the Work readings of session 1343, Cases 650–656 against transcript f5706873: the plan file was written with its title line before the first dispatch; seven case-guppi dispatched with the Case id, the Frontier item, its source and the person''s words; twelve rounds sent back by SendMessage verbatim and shown in Russian in order, first rounds with their Context; eight showings, each by SendUserFile display render of its case file, a Russian heading, one list per Case and sub-case of the summary with what done means and its Estimate, the ledger lines as the summary held them, the agent''s text after one rule; no Stop refusal of a showing; failed on one clause: the heading of Case 653 rendered Frontier item C3, not the Case''s name, its summary holding items for 653.1 and 653.2 only; the first showing of 650 put the ratification under a bare `**ratification:**` line with a plain fence, later ones as a quote block; not exercised: a plain explanation, a Fact reply, an `**Other Case:**` line, a Stop refusal of a showing'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-orchestration-shows-the-built-case`
```

### Case 669.11 — The check that every agent leaves out the Decision pages is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-search-leaves-out-decisions-in-every-agent` at the librarian's run of the session.

> **then:**
> `estimate-search-leaves-out-decisions-in-every-agent` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-search-leaves-out-decisions-in-every-agent` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-search-leaves-out-decisions-in-every-agent` stand as they were.
> **－** No reading line is written for `estimate-search-leaves-out-decisions-in-every-agent`: the state comes from the decision.

```then
update:
- slug: estimate-search-leaves-out-decisions-in-every-agent
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      A session starts after `uv run guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Read, or Grep with a `path` that is `vault/wiki/decisions/` or lies in it.

      Then:
      `.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
      **＋** The text of a Decision page reaches one of these agents only by a Read of its path or by a Grep whose `path` is `vault/wiki/decisions/` or lies in it, for a reason of `.claude/agents/ask-guppi.md` in `ask-guppi` and `case-guppi` — a page of its answer carries `deferred_by`, or the question asks why something was decided — and for no reason in the main agent.
      **－** An `addressed_by` that names a Decision page is no reason to read it.
      **－** Whether a Grep over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
      **－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
      **－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page pending: 2026-10-05, at the /hi of session 1343, by hand: the transcripts of session 0311 (6d53e05d) after the render by case 640 at the librarian''s run of session 0109 — the main agent, case-guppi a565a08d267ecaa66, a1cf96ac9df5edd1c, a7b182c9a1f27f641, ask-guppi a055d35695650c13f, af56f988c579ddc06, af7cde916f5b24293: .claude/rules/search-leaves-out-decisions.md stands in all seven contexts; 9 Greps whose path is vault/, vault/wiki/ or the repository root carry no !**/decisions/** in their glob — main agent 1 (path vault, glob **/{handoff,work}.md), a565a08d267ecaa66 1 (path vault, no glob), a1cf96ac9df5edd1c 1 (root, {guppi/**,tests/**}), a7b182c9a1f27f641 5 (vault/wiki with globs of named files twice, root *.py three times), af56f988c579ddc06 1 (root, *.py, named in its own answer); none printed a line of a page under vault/wiki/decisions/; Reads of a Decision page: a565a08d267ecaa66 decision-case-442, the deferred_by of rule-ledger-write, a reason of .claude/agents/ask-guppi.md; a1cf96ac9df5edd1c decision-case-432, the addressed_by of insight-workflow-case-schema-silent-on-what-the-scripts-accept, neither reason of that frame; the main agent read none'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-search-leaves-out-decisions-in-every-agent`
```

### Case 669.12 — The check that case-guppi checks the finished Case is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-case-build-checks-the-finished-case` at the librarian's run of the session.

> **then:**
> `estimate-case-build-checks-the-finished-case` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-case-build-checks-the-finished-case` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-case-build-checks-the-finished-case` stand as they were.
> **＋** No decision that put off `estimate-case-build-checks-the-finished-case` stands `current`.
> **－** No reading line is written for `estimate-case-build-checks-the-finished-case`: the state comes from the decision.

```then
update:
- slug: estimate-case-build-checks-the-finished-case
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, has built a Case and is about to answer with it.

      Then:
      It puts each option the person chose in its rounds, or the person's own words where they answered outside the options, beside the `then` and `recommend` of the Case, and the Case holds each one; where the frame shows after a round that a chosen option cannot hold as written, its answer is a round on that point, not a Case with another behaviour.
      **＋** For each page whose text the change makes false, it searches the live pages of the vault, leaving out the Decision pages, and the code, for the page's slug, and reads each hit that `given` does not name around the line of the hit; for a fact that no slug marks, it reads the index lines of the recipe of `.claude/agents/ask-guppi.md` and judges them by meaning.
      **＋** When the change sets what happens at a moment — a reply, a hook event, a command — it searches `vault/wiki/rules/` and `.claude/` for the words that name that moment, reads each passage of each hit that sets a form or a behaviour at that moment, and the Case either does not cover that moment or names the other rule in `given`.
      **＋** It reads the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of each Case of the session that the prompt of its call names, and no other Case of the session; where that Case changes a page the Case changes or sets what happens at the same moment, the Case does not cover that moment or names the case file in `given`, and its new text of that page does not contradict the text of that Case.
      **＋** When the Case replaces the Criterion of an Estimate, it reads the `purpose` and `method` of that Estimate, and the same `update` sets anew each one that states the old promise.
      **＋** Each hit that the change makes false enters the Case, or its `context` says why it stands.
      **＋** The `context` names a search only when the Case rests on it: a search with a hit that enters the Case, a search with a hit that stands and needs the reason why, or a search that a claim that no text says something rests on; a search that found nothing to change and that no claim rests on is left out.
      **＋** A claim of `context` about a text names the search it rests on: its pattern, the paths it ran over, and each file the search printed, a file it does not read included, or the count it printed; just before it answers, it runs each search that `context` names again, with the pattern and the paths that `context` writes, and the files and counts in `context` are the ones that run printed, not the files it read during the build; it claims nothing the search did not print.
      **＋** It reads side by side the finished new texts of all its sub-cases that change one page, and the Case holds no contradiction between them.
      **－** A hit in a History line, in `log.md` or in `brief.md` is not read.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson; the defers of cases 647, 657 and 667 retired. The last reading before it, which left the page failed: 2026-10-05, in the Work Mode of session 0109, by hand: the first answers of the four ask-guppi runs at the /pre-spec of session 0109, one per top-level Case 638, 639, 640 and 641, each built by case-guppi after the render of .claude/agents/case-guppi.md by case 636: 0 Cases departing from a chosen option; 1 page whose text the change makes false missed (640: estimate-harness-pipeline lists the rules in no pipeline that the Purpose of rule-harness names); 4 rules bearing on the same moment missed (638: rule-agent-writing; 640: rule-page-read, rule-documentation with the librarian''s frame, rule-claude-md) and 1 lesson (640: lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction); 1 clash with a Case named in the prompt (640: its context on the broken-rule line of Case 639); 0 Estimates whose purpose or method kept a dropped promise; 4 claims of context the vault or the transcripts do not bear out (638: the sentence counts and the lists of the 636 confirmation, both taken from the main agent''s prompt; 639: two lists where the Result names one; 640: the librarian''s `git` allowance); 0 searches in context the Case does not rest on; 0 contradicting sub-cases, no Case had sub-cases; besides, 2 Estimates not named that cover the new target of 641 (estimate-harness-make-runs-in-both-shells, estimate-tests-clock-pinned)'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson; the defers of cases 647, 657 and 667 retired (case 669)
```

```tasks
- [x] update `estimate-case-build-checks-the-finished-case`
```

### Case 669.13 — The check of the form of a Case is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-case-protocol-case-form` at the librarian's run of the session.

> **then:**
> `estimate-case-protocol-case-form` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-case-protocol-case-form` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-case-protocol-case-form` stand as they were.
> **＋** No decision that put off `estimate-case-protocol-case-form` stands `current`.
> **－** No reading line is written for `estimate-case-protocol-case-form`: the state comes from the decision.

```then
update:
- slug: estimate-case-protocol-case-form
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `case-guppi` writes a Case it built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the hook of `rule-case-check` checks it, and the main agent sends that file to the person, at its first showing or again.

      Then:
      The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
      **＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
      **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
      **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
      **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
      **＋** `tasks` holds no `by hand` box whose moment comes after Work Mode of the Case's own session — the librarian's run of that session or a later session; such a check stands as the reading of an Estimate or is left to the `make lint` of the librarian's run.
      **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
      **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-orchestration-shows-the-built-case`, and the reply ends with a plain question.
      **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
      **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson; the defer of case 665 retired. The last reading before it, which left the page failed: 2026-10-05, by hand at the Work readings of session 1343, cases/case-650.md to case-656.md against vault/wiki/case-schema.md: headings, sub-cases in one file, sections in the order of the table each one blockquote, context opening with the mechanism, recommend as the table sets, ＋/－ lines, tasks naming each Estimate with sub-points and no by-hand box after Work Mode, one untagged fence of ledger lines, a plain question at each showing, no complaint of the person; failed: `given` holds two things on a line in 650.1, 650.2 (`guppi/ratified.py` and `tests/test_ratified.py`), 653.1 and 654, and states state in 656 ("on the allow list", "with `permissionMode: acceptEdits`") and 653.1; `then` of 652 holds a count ("both tests of `tests/test_case_schema.py` fail"); the passed reading of 2026-10-03 accepted paired `given` lines of the same form in cases 607–610'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson; the defer of case 665 retired (case 669)
```

```tasks
- [x] update `estimate-case-protocol-case-form`
```

### Case 669.14 — The check that pre-spec confirms the findings once is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-prespec-confirms-the-findings-once` at the librarian's run of the session.

> **then:**
> `estimate-prespec-confirms-the-findings-once` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-prespec-confirms-the-findings-once` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held.
> **＋** The Criterion, `purpose` and `method` of `estimate-prespec-confirms-the-findings-once` stand as they were.
> **＋** No decision that put off `estimate-prespec-confirms-the-findings-once` stands `current`.
> **－** No reading line is written for `estimate-prespec-confirms-the-findings-once`: the state comes from the decision.

```then
update:
- slug: estimate-prespec-confirms-the-findings-once
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      `/pre-spec` has reported findings that sent Cases of the plan back, and every `case-guppi` that got a finding has answered with its Case built again, with `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec` and `.claude/agents/ask-guppi.md` rendered from `rule-ask`.

      Then:
      The main agent sends each `ask-guppi` run whose findings sent a Case back the Cases built again on them, by `SendMessage`, all in one message, and asks only whether each of its findings is closed.
      **＋** For each finding of its own, under the finding's number, each `ask-guppi` answers with a line that holds `closed` or `not closed`, and under it at most a short paragraph of up to three sentences on why.
      **＋** After the findings stands one list of what the agent did not check in confirming them. The list says "none" when it checked all of it and its searches broke no rule. Its last lines name each rule that a search of the agent broke, one line each, and say whether a verdict rests on what that search printed. Then stands a list of the paths of the files the agent read, and nothing else stands before or after.
      **＋** The main agent asks the person a question after the confirmation, in the shape of `.claude/skills/grill-me/SKILL.md`: whether each finding not closed is fixed or left; it sends a finding to be fixed to the `case-guppi` of its Case.
      **＋** It then shows every Case built again in one reply, for one ratification, and writes what the confirmation found closed and not closed in its own text after the horizontal rule.
      **－** The message of the main agent invites no new finding and no new judgment of a Case beyond those findings.
      **－** No Case goes to `ask-guppi` a second time, and no new `ask-guppi` is dispatched.
      **－** The answer of `ask-guppi` names no new finding; it runs no Grep, the Grep of the rules included, and reads only the Cases built again and the pages its findings name.
      **－** After that ratification the hook of `rule-prespec-onward` sends the agent to the check and the exit, as before.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson; the defer of case 666 retired. The last reading before it, which left the page failed: 2026-10-05, by hand at the Work readings of session 1343, the /pre-spec of session 1343 after the render by case 638 (commit 7b089086): seven ask-guppi in one message; the findings to six case-guppi in one message (653 put off by the person''s answer); the six runs whose findings sent a Case back asked in one message only whether each finding is closed; each made one Read of its case file, no Grep and no new finding; a verdict line under each finding; one list of what was not checked and the files read; finding 656-1.1 not closed put to the person as a grill-me question, left by the person; the six Cases shown in one reply for one ratification; no second dispatch; failed: under one finding each, the runs on 650 (3.1), 652 (1.1) and 654 (1.1) wrote four sentences, more than the three allowed'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson; the defer of case 666 retired (case 669)
```

```tasks
- [x] update `estimate-prespec-confirms-the-findings-once`
```

### Case 669.15 — The check of the searches of ask-guppi at pre-spec is closed as passed

> **when:**
> `guppi generate` of `rule-page-generation` applies the update of this Case to `estimate-ask-searches-at-prespec` at the librarian's run of the session.

> **then:**
> `estimate-ask-searches-at-prespec` stands `passed`, with `checked` set to the date of the decision.
> **＋** The `## Result` of `estimate-ask-searches-at-prespec` opens with the person's decision, taken without a reading, says that a problem seen later in what it promises comes back as a lesson, and keeps after it the last reading the page held or this session's ledger wrote.
> **＋** The Criterion, `purpose` and `method` of `estimate-ask-searches-at-prespec` stand as they were.
> **－** No reading line is written for `estimate-ask-searches-at-prespec`: the state comes from the decision.

```then
update:
- slug: estimate-ask-searches-at-prespec
  set:
    status: passed
    checked: 2026-10-05
  sections:
    Criterion: |-
      When:
      At the first run of `/pre-spec` in a session, the main agent dispatches `ask-guppi` through the `Agent` tool with the plan file and the questions of `.claude/skills/pre-spec/SKILL.md`, and the agent follows `.claude/agents/ask-guppi.md` as rendered from `rule-ask`.

      Then:
      The agent starts with the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, then runs one Grep per other category the question touches.
      **＋** After those Greps it runs further Greps and Reads as a finding needs, including the search behind a count that a `context` states.
      **＋** A count of a `context` whose search covers `vault/wiki/decisions/` is not run again and is no finding.
      **－** Whether a Grep of the agent over a folder that holds `vault/wiki/decisions/` leaves that folder out is outside this promise: `estimate-search-leaves-out-decisions-by-the-grep-hook` reads it.
      **－** Whether a Read of the agent, or a Grep inside `vault/wiki/decisions/`, reaches a Decision page only for a reason of its frame is outside this promise: `estimate-search-leaves-out-decisions-in-every-agent` reads it.
    Result: '2026-10-05, Plan Mode of session 1831, case 669: set passed by the person''s decision, without a reading; a problem seen later in what this Estimate promises comes back as a lesson. The last reading before it, which left the page failed: 2026-10-05, /hi of 1831, the ask-guppi transcripts of the /pre-spec of 1616 (6360af9f, 17:39) and 1343 (f5706873, 15:25), after the render of ask-guppi.md at 03:09; every run opened with the Grep ^(purpose|deferred_by): over vault/wiki/rules/; in 1616 the run on 664 Read rule pages and Estimates and ran no Grep of lessons, insights or entities, the run on 661 grepped insights alone; in 1343 the runs on 650, 651, 652, 653 and 656 ran Reads of rule and estimate pages before their last category Grep'
  change: set passed by the person's decision, without a reading; the Criterion kept; a problem seen later comes back as a lesson (case 669)
```

```tasks
- [x] update `estimate-ask-searches-at-prespec`
```

### Case 669.16 — The schemas let a Case set an Estimate passed or failed by the person's decision

> **given:**
> `rule-case-protocol`: the Render of the Case form, whose sentences on an `update` of an Estimate and on the derivable fields change.
> **＋** `vault/wiki/case-schema.md`: the file rendered from it, which `case-guppi` reads whole.
> **＋** `rule-estimates-schema`: the Render of the Estimate schema, whose sentences on a `failed` Estimate, on `checked` and on the Result change.
> **＋** `vault/wiki/estimates/schema.yaml`: the file rendered from it, which lint reads.
> **＋** `guppi/materialize.py`: keeps the status and the Criterion an `update` item writes.
> **＋** `raw/2026-10-05/1831/handoff.md`: the report of this session's Retro.
> **＋** `raw/2026-10-05/1831/cases/case-670.md`: 670.4 updates `rule-case-protocol`, and 670.2 and 670.3 set the readings at Retro and the handoff.
> **＋** `raw/2026-10-05/1831/cases/case-671.md`: 671.2 updates the Splitting section of `rule-case-protocol`.

> **when:**
> `case-guppi` reads `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, or `guppi lint` reads `vault/wiki/estimates/schema.yaml`, rendered from `rule-estimates-schema`, for a Case that sets an Estimate `passed` or `failed` by the person's decision.

> **then:**
> `vault/wiki/case-schema.md` says that by the person's decision a Case may set an Estimate `passed` or `failed` by an `update` that writes the page's Criterion back unchanged under `sections: Criterion` and writes `sections: Result`.
> **＋** The first line of the Result of such an Estimate is the date and the place of the decision, the person's decision and its case, and the last reading the page held follows it.
> **＋** The `checked` of such an Estimate is the date of the decision, and `vault/wiki/case-schema.md` names its `status` and `checked` as the derivable fields such a Case writes.
> **＋** `vault/wiki/estimates/schema.yaml` says that the person may close a `failed` Estimate by such a decision, and that a check that keeps failing is a Lesson unless the person closes it so.
> **＋** `raw/2026-10-05/1831/handoff.md` names none of the Estimates that 669.1 to 669.15 close as a reading that waits.
> **－** `guppi/materialize.py` does not change: an item that sets a status keeps it, and the Criterion it writes stands.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: 'An `update` of an Estimate carries `slug`, `set: {status: pending}` and `change`; the scripts replace its Criterion with the Case''s `when` and `then`, or keep the text the item wrote under `sections: Criterion` (case 204).'
    new: 'An `update` of an Estimate carries `slug`, `set: {status: pending}` and `change`; the scripts replace its Criterion with the Case''s `when` and `then`, or keep the text the item wrote under `sections: Criterion` (case 204). By the person''s decision a Case may instead set an Estimate `passed` or `failed`: its `update` carries `set: {status: passed, checked: <date>}`, or `failed`, the page''s Criterion written back unchanged under `sections: Criterion`, and `sections: Result`, whose first line is the date and the place of the decision — `the person''s decision, case N` — before the last reading the page held; `checked` is the date of the decision (case 669.16).'
  - old: are filled mechanically and are not written here.
    new: are filled mechanically and are not written here, but for the `status` and `checked` of an Estimate that a Case sets by the person's decision (case 669.16).
  change: a Case may set an Estimate passed or failed by the person's decision, its Criterion written back unchanged, its Result opening with the date and the place of the decision (case 669.16)
- slug: rule-estimates-schema
  replace:
  - old: until a human decides. Absent a decision to fix
    new: 'until a human decides. The person may decide to close it: a Case then sets it `passed` or `failed` by that decision, its Criterion written back unchanged (case 669.16). Absent a decision to fix'
  - old: a check that keeps failing is a Lesson, not a counter.
    new: a check that keeps failing is a Lesson, not a counter, unless the person closes it by decision (case 669.16).
  - old: 'The date of the last reading:'
    new: 'The date of the last reading, or of the person''s decision that set the status, which the Case writes (case 669.16):'
  - old: or the place of a live reading; the result follows (case 199).
    new: or the place of a live reading; the result follows (case 199). On a status set by the person's decision, the first line is the date and the place of the decision — `the person's decision, case N` — and the last reading the page held follows (case 669.16).
  change: 'the person may close an Estimate by decision: its Result opens with the date and the place of the decision, and checked is that date (case 669.16)'
```

```tasks
- [x] update `rule-case-protocol`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] update `rule-estimates-schema`
- [x] `uv run guppi render`: `vault/wiki/estimates/schema.yaml`
- [x] `raw/2026-10-05/1831/handoff.md`: names none of the Estimates that 669.1 to 669.15 close as a reading that waits.
```

## Case 670 — An Estimate is read in the session that changes it

> **context:**
> When a Case creates an Estimate or replaces its Criterion, the scripts set the page `pending`. The ledger hook of `guppi/ledger.py` then refuses a reading of that slug for the whole session (case 428.1). Retro leaves the reading to a later session, and most methods name a live moment there, "by hand in a later session". Each `/hi` takes these readings again as Work lines and reads old transcripts to judge them. Session 1616 left 13 Estimates pending, and the `/hi` of this session spent one agent of about 112k tokens on transcripts. The loop never closes, because every change makes a new pending Estimate.
> The person chose to break it. Retro reads each Estimate the session creates or updates, in the same session, on the Criterion of the Spec, and the hook lets that reading through once Retro has opened (670.1). A rule whose Render changes is read on the new text of the Spec, since its harness file follows only at the librarian's render. A reading that needs the person's word stays the one exception and is asked at the next `/hi`. Retro sets any other Estimate it cannot read `failed`, with the reason, so the next `/hi` shows it once as a Case (670.2). The handoff no longer lists these Estimates as readings that wait (670.3). A method holds only what runs in its own session, and pre-spec reports a new method that waits for another session; the check is a predicate in `guppi/lint.py` that `guppi/prespec.py` imports, and lint does not run it over the live pages, so old methods give no new finding (670.4). `/hi` reads no transcript: it takes only the readings it can run now, and turns each other open Work line into a Cases line. The 11 Estimates of the close of the sprint migration are left as they are (670.5). The list of the sources of a Cases line names that new kind (670.6). The Work readings of `/work` still leave an Estimate the session changes, and its Work line now closes at Retro (670.7). No hook checks that Retro read each Estimate. A forgotten one stays `pending`, and the next `/hi` takes it, or turns it into a Cases line.
> The librarian applies a reading of the same session in the right order. `materialize` keeps the order of the ledger. A reading folds into the `create` of its page (`fold_estimate`). An `update` that replaces a Criterion sets `pending` (`lift_criterion`), and a reading line later in the ledger becomes its own entry after it. `generate` applies the entries in order, so the reading of Retro sets the final status.
> Case 669 of this session sets fifteen Estimates `passed` by the person's decision. Each of its `update` items sets `passed` and writes the Criterion back unchanged under `sections.Criterion`. The person answered that this Case leaves such an Estimate alone, so Retro neither reads it nor sets it `failed`. The exception holds only for an `update` that sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged. An ordinary replacement of a Criterion also carries a status, `set: {status: pending}`, and writes no `sections.Criterion` (`lift_criterion`), so Retro reads it. The same exception covers an `update` that names one part of the page alone, such as a `method`. That update writes no new Criterion and sets no status, so the Spec holds no new promise to read. Case 669 changes no page this Case changes. Its update of `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` keeps a Criterion about superseded Cases, which this Case does not touch.
> In this session, the code of 670.1 and 670.4 is live once Work Mode writes it. Retro and `/hi` still follow their old rendered text until the librarian renders it. The Render of `rule-retro` says that an Estimate this session creates or updates gets no reading in this session. So the ledger hook would let a reading through at this session's Retro, after the mark `retro`, but the old Retro text takes none. This session's Retro takes no reading of this Case's Estimates, of the Estimate of Case 671.1 or of the fifteen of Case 669. The next `/hi` takes each Estimate of this Case and of Case 671.1 as a Work line it can run now: the code Estimates by pytest, and the render Estimates from the rendered file their methods name. `estimate-work-mode-takes-the-work-readings` of 670.7 gets a method of the same form as the render Estimates. `estimate-hi-writes-frontier` of 670.6 keeps its method, which waits for the close of the sprint, as 670.5 allows. The ledger hook only refuses less than before, so no line is lost between the code and the render.
> The frame. A Grep `later session` over `{.claude/**,guppi/**,vault/wiki/rules/**,vault/wiki/*.md}` printed 21 files: `vault/wiki/brief.md`, `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/orchestration.md`, `.claude/agents/case-guppi.md`, `vault/wiki/case-schema.md`, `.claude/skills/carry/SKILL.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/rules/rule-materialize.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-case-build.md`, `guppi/casecheck.py`, `guppi/prespec.py`, `vault/wiki/rules/rule-case-protocol.md`, `guppi/ledger.py`, `vault/wiki/rules/rule-skill-hi.md`, `vault/wiki/rules/rule-spec-box.md`, `vault/wiki/rules/rule-carry-over.md`, `guppi/box.py` and `guppi/spec.py`. The hits in `rule-retro`, `rule-orchestration`, `rule-case-protocol` and `guppi/ledger.py` enter this Case, and their rendered files follow them. The hit in `rule-skill-hi` and its skill file says that a line of the sprint page left for a later session closes `· sprint · defer`; 670.5 does not change that, so it stands. The passages 670.5 replaces speak of an earlier session. The hits in `rule-carry-over`, `rule-spec-box`, `.claude/skills/carry/SKILL.md`, `guppi/box.py`, `guppi/spec.py` and `guppi/prespec.py` speak of a conserved Spec or a sprint item that a later session takes, so they stand. The hit in `rule-case-build`, `.claude/agents/case-guppi.md` and `guppi/casecheck.py` says that a Case of a later session removes an old form of code, so it stands. The hit in `rule-materialize` is a History line, and `brief.md` and `log.md` were not read. A Grep `creates or updates` over the same paths printed 16 files: `.claude/skills/work/SKILL.md`, `.claude/skills/retro/SKILL.md`, `vault/wiki/orchestration.md`, `.claude/skills/handoff/SKILL.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-retro.md`, `vault/wiki/rules/rule-materialize.md`, `vault/wiki/rules/rule-orchestration.md`, `vault/wiki/rules/rule-handoff.md`, `guppi/ratified.py`, `guppi/materialize.py`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-spec-write.md`, `guppi/ledger.py`, `vault/wiki/rules/rule-work-mode.md` and `vault/wiki/rules/rule-ledger-write.md`. The hit in `rule-handoff` enters 670.3. The hit in `rule-work-mode` and its skill enters 670.7: the Work readings still leave an Estimate the session changes, and Retro now reads it and closes its line. The hits in `rule-spec-write`, `rule-materialize`, `guppi/materialize.py` and `guppi/ratified.py` speak of a schema rule that the session changes, and the hits in `rule-ledger-write` and `rule-case-protocol` are History lines; all of these stand. A Grep `^method:.*(closes (a|the) sprint|close of a sprint|closes it)` over the 11 Estimate pages of the close of the sprint migration under `vault/wiki/estimates/` printed 11 occurrences in 11 files, so the exception of 670.5 covers each of them by the words of its method.
> The Estimates. `estimate-retro-runs-on-to-the-handoff` stands. It promises that Retro takes the readings whose moment has come and leaves the person's readings to `## Ask the person`, and both stay true. `estimate-case-protocol-case-form` stands, and Case 669 writes its Criterion back. Its line says that a check after Work Mode is the reading of an Estimate or is left to `make lint`. 670.4 keeps that sentence of `case-schema.md` and only adds that Retro takes the reading. `estimate-hi-writes-frontier` stands. It says that a Work line which needs a decision closes `· case N`, and 670.5 uses that close. `estimate-lint-reports-a-method-tied-to-a-one-off-moment` stands, since its finding is not replaced. `estimate-prespec-catches-a-method-without-a-form` stands. It promises the pre-spec finding on the `method` of a `create`, or of an `update` with `set: {method: …}`, that names no form, by a predicate lifted out of `guppi/lint.py`. 670.4 reads the same input and adds a finding beside it in the same way, and its last line keeps the finding of no form. The other Stop hooks in `.claude/settings.json` (`guppi ratified`, `guppi casecheck`, `guppi context`, `guppi onward` and `guppi onward --plan`) judge no reading line. `guppi onward` reads the refusals of the ledger hook. At Retro the hook still refuses a lesson without its prefix and a line it cannot read, and `rule-retro` (case 596) and `guppi/onward.py` answer such a refusal as before. Only the refusal of a reading of a changed Estimate stops at the mark.

> **problem:**
> Every change of an Estimate leaves it `pending`. Its reading is barred in the session that made the change and waits for a live moment in another session, so each `/hi` pays to read the same Estimates again, and the list never empties.

> **recommend:**
> - **When does the ledger hook let a reading of a changed Estimate through?**
>   - Recommended: (a) from the opening of Retro, by the existing `retro` mark; before it the hook still refuses.
>   - Answer: agreed, (a).
> - **How does Retro read an Estimate of a rule whose text is rendered into a harness file?**
>   - Recommended: (a) Retro reads the new text in the Spec against the Criterion; the render and `make lint` check the file, and a problem seen later is a lesson.
>   - Answer: agreed, (a).
> - **What happens to an Estimate whose method needs your word?**
>   - Recommended: (a) the one exception: Retro leaves it under `## Ask the person`, and the next `/hi` asks it once, with no transcript.
>   - Answer: agreed, (a).
> - **What does `/hi` do with an old open reading whose method waits for a moment in another session?**
>   - Recommended: (a) remove the transcript step: `/hi` takes only the readings it can run now, and any other open Estimate becomes one Cases line; the readings of the sprint migration's close stay as they are.
>   - Answer: agreed, (a).
> - **What makes sure Retro reads, or sets `failed`, each Estimate the session changed?**
>   - Recommended: (b) Retro's text alone, with `/hi` as the net for a forgotten reading.
>   - Answer: agreed, (b).
> - **Does a check report a new method that waits for another session?**
>   - Recommended: (a) pre-spec reports it in the Spec, by a predicate in `guppi/lint.py` that `guppi/prespec.py` imports; a method whose reading is the person's answer is the exception, and lint over the live pages stays as it is.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: from the summary of Case 669, the main agent asked whether this Case should leave alone an Estimate whose `update` in this session sets its status itself and does not change its Criterion, so the fifteen of Case 669 stay `passed`; the person agreed, (a).
>   - Taken: 670.2 neither reads nor sets `failed` an Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, nor one whose `update` names one part of the page alone.

### Case 670.1 — The ledger hook writes a reading of a changed Estimate once Retro has opened

> **given:**
> `guppi/ledger.py`: the `Stop` hook that writes the ledger lines.
> **＋** `guppi/onward.py`: holds `retro_marked`, the judgment of the mark `retro`.
> **＋** `tests/test_ledger.py`: the tests of the hook.
> **＋** `rule-ledger-write`: the rule of the hook.
> **＋** `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`: its Criterion is replaced whole.
> **＋** `estimate-ledger-write-lifts`: sets how a stderr line is told once a stretch.
> **＋** `rule-orchestration`: its Render tells the main agent when a reading line is written.
> **＋** `vault/wiki/orchestration.md`: the file rendered from it.

> **when:**
> The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `estimate[<slug>]` line in a `LEDGER` block of the session, and a decision line `create` or `update` of `<slug>` stands in the session's ledger or among the lines the hook writes on the same `Stop`.

> **then:**
> While the event log of the session's window holds no mark `retro` of this session after its `hi`, the line is not written: the reading waits for Retro.
> **＋** Once that mark stands, the line is written as any other reading of the `Stop`.
> **＋** The mark is judged by `retro_marked` of `guppi/onward.py`, imported, the one judgment of the mark.
> **＋** A line of a reply written before the mark stays refused, and the hook skips it at every later `Stop` without a word.
> **＋** A reading of the old slug of a page that an `update` of this session renames falls under the same rule: the decision line names the old slug.
> **＋** When a refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line, which names the Case and says that the reading is taken at the Retro of this session.
> **＋** The other lines of the `Stop` are written as before.
> **－** A reading of a slug that no decision line `create` or `update` of this session names is written as before; a `defer` line of the slug does not refuse it.
> **－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

```then
update:
- slug: rule-ledger-write
  change: the hook refuses a reading of an Estimate that a decision line of the session creates or updates only before the mark retro of the session (case 670.1)
- slug: rule-orchestration
  replace:
  - old: — a reading of an Estimate that a decision line of this session creates or updates waits for a later session, and the ledger hook refuses it (case 428.1) —
    new: — a reading of an Estimate that a decision line of this session creates or updates stands in that reply too, and the ledger hook refuses it before Retro opens (case 670.1) —
  change: a reading of an Estimate the session changes is written in the reply that ends Retro; the ledger hook refuses it only before Retro opens (case 670.1)
- slug: estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session
  set:
    status: pending
    purpose: Whether the ledger hook refuses a reading of an Estimate that a decision line of the same session creates or updates until the Retro of that session opens, writes it after, and says why only for the reply just finished
  change: the Criterion replaced whole — the reading is refused only before the mark retro of the session (case 670.1)
```

```tasks
- [x] `guppi/ledger.py`: `refused_readings` refuses a reading of a slug the session changes only before the mark `retro` of the session, judged by `retro_marked` of `guppi/onward.py`, imported inside the function; a line of a reply written before the mark stays refused; the stderr line and the docstring say that the reading is taken at the Retro of this session.
- [x] `tests/test_ledger.py`: a reading of a changed slug is refused before the mark and written after it; a line of a reply before the mark stays refused after it; the stderr line names Retro.
- [x] update `rule-ledger-write`
- [x] update `rule-orchestration`
- [x] `uv run guppi render`: `vault/wiki/orchestration.md`
- [x] update `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
- [x] read `estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session`
```

### Case 670.2 — Retro reads each Estimate the session changes, or sets it failed

> **given:**
> `rule-retro`: the Render of the Retro skill, whose paragraph on readings changes.
> **＋** `.claude/skills/retro/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-retro-loads`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec whose Criteria Retro reads.
> **＋** `raw/<date>/<hi HHMM>/work.md`: names a conserved Spec that `/box` runs.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: names a reading that needs the person.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: holds the `W` line of an Estimate Retro reads.

> **when:**
> The agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built.
> **＋** Each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — is read in the reply that ends Retro, on the Criterion of `raw/<date>/<hi HHMM>/spec.md`: the `when` and `then` of its Case, or the Criterion its item writes.
> **＋** For an Estimate of a rule whose Render a Case of the Spec changes, the reading reads the new text of the Render in `raw/<date>/<hi HHMM>/spec.md` against that Criterion.
> **＋** Each such Estimate that Retro cannot read gets a `failed` line in the same `LEDGER` block, whose result opens with the date and says that Retro did not read it and why.
> **＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as this session's for its boxes, for the scope of an edit and for the readings above.
> **＋** Retro closes the open `W` line of each Estimate it reads or sets `failed` `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`.
> **－** An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`.
> **－** A reading whose `method` names the person's word is not taken: it is a line of `## Ask the person` of `raw/<date>/<hi HHMM>/handoff.md`, with its question, and its `read` line is neither debt nor the librarian's.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

```then
update:
- slug: rule-retro
  replace:
  - old: and for the readings this session does not take; the ledger hook sees only this session's own lines, so this text is the guard (case 591)
    new: and for the readings of the Estimates this session creates or updates; the ledger hook sees only this session's own lines (cases 591, 670.2)
  - old: A `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, waits for a later session; it is neither debt nor the librarian's (case 428.4).
    new: A `read` line whose `failed` line you write in this turn waits for the librarian as a reading does. A `read` line of an Estimate whose reading only the person can take, named under `## Ask the person` of `handoff.md`, waits for the person; it is neither debt nor the librarian's (case 670.2).
  - old: 'What a session changes, it does not measure: an Estimate this session creates or updates has no reading in this session, built or not, and the ledger hook refuses one (case 428.1); the `read` line of its old Criterion in an earlier Spec is not debt and is not read, and the reading of the new Criterion closes it in a later session, at the moment its `method` names (cases 283, 428.3). A reading whose `method` names the person''s word is not yours to take: it is a line of `## Ask the person` of `handoff.md`, with the question the person answers (case 531.1). `handoff.md` names every Estimate whose reading cannot be taken yet, and every Estimate this session creates or updates.'
    new: 'Read each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — in this turn, on the Criterion of the Spec: the `when` and `then` of its Case, or the Criterion its item writes; the ledger hook writes such a reading only after Retro opens (cases 670.1, 670.2). For an Estimate of a rule whose Render a Case of the Spec changes, read the new text of the Render in the Spec against that Criterion: the harness file follows at the librarian''s render, and its `make lint` checks the file. An Estimate whose `update` sets `passed` or `failed` by the person''s decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`. The `read` line of an old Criterion in an earlier Spec is not debt and is not read (case 283). A reading whose `method` names the person''s word is not yours to take: it is a line of `## Ask the person` of `handoff.md`, with the question the person answers (case 531.1). Each other Estimate this session creates or updates that you cannot read gets a `failed` line in the same `LEDGER` block, its result opening with the date, the words `Retro, not read` and the reason; the next session shows it as a Case. Close the open `W` line of each Estimate you read or set `failed` `[x] … · work` in `frontier.md` (case 670.7). A problem seen live in a later session is a lesson of that session, not a reading. `handoff.md` names every Estimate whose reading cannot be taken yet.'
  change: Retro reads each Estimate the session creates or updates on the Criterion of the Spec, or sets it failed; a reading that needs the person waits for the person (case 670.2)
- slug: estimate-retro-loads
  set:
    status: pending
    method: by hand, the text of .claude/skills/retro/SKILL.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-retro in the Spec, read against the Criterion, recorded in the estimate line
  change: the Criterion replaced whole — Retro reads each Estimate the session creates or updates on the Criterion of the Spec, or sets it failed (case 670.2)
```

```tasks
- [x] update `rule-retro`
- [x] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
- [x] update `estimate-retro-loads`
- [x] read `estimate-retro-loads`
```

### Case 670.3 — The handoff lists no Estimate the session changed as a reading that waits

> **given:**
> `rule-handoff`: the Render of the handoff skill, whose line on `## Debt` changes.
> **＋** `.claude/skills/handoff/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-handoff-holds-each-fact-once`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/handoff.md`: the report of Retro the skill writes.
> **＋** `rule-retro`: reads or sets `failed` each Estimate the session changes.
> **＋** `rule-brief`: reads `## What actually got done`.

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, on a clean tree, and the agent runs `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff` and writes `raw/<date>/<hi HHMM>/handoff.md`.

> **then:**
> `raw/<date>/<hi HHMM>/handoff.md` is the report of Retro: under `# Handoff — <date>, <slice or topic>` it holds, in order, `## Notes from memory`, `## Direct instructions to the librarian`, `## What actually got done`, `## Debt`, `## Observations`, `## For the next session` and `## Ask the person`.
> **＋** `## Notes from memory` holds only where the person hesitated, what stayed unclear and which decisions carried caveats. `## Direct instructions to the librarian` holds only what to check first and what may duplicate what, and lists no reading that waits.
> **＋** `## What actually got done` holds the ids of the Cases ratified, the code files and tests changed, the result of `make test` and `make style`, and the readings and lessons written, by their ledger line numbers.
> **＋** `## Debt` holds each box of the Spec that is debt and each red test reverted into a patch, with the path of the patch. Under them stands a line with the count of the boxes that wait for the librarian. Then comes one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for. These lines stand in the section and are not debt.
> **＋** An Estimate this session creates or updates has no such line in `## Debt`: the Retro of `rule-retro` read it or set it `failed`, unless the person's answer is its reading.
> **＋** `## Observations` holds what was noticed in Work Mode and Retro, a red before the work and an expected red among them; `## For the next session` holds what needs a decision.
> **＋** `## Ask the person` holds one line per reading that only the person can take: the Estimate by slug, the mark `needs the person` and the question the person answers.
> **－** No statement stands twice: a Case, box, reading, lesson or observation that one section names stands in another section only with what that section's kind adds about it, such as a caveat or what to check first, and no section says again what another section says of it. The file holds no commit, no number of an item and no end of an item.
> **－** The section names `## Notes from memory`, `## Direct instructions to the librarian` and `## What actually got done` stay, so `rule-brief` reads `## What actually got done` as before.

```then
update:
- slug: rule-handoff
  replace:
  - old: 'then one line per Estimate whose reading cannot be taken yet, each one this session creates or updates among them, except one that `## Ask the person` holds: its slug and the moment its reading waits for; these lines stand in the section and are not debt (case 624).'
    new: 'then one line per Estimate whose reading cannot be taken yet, except one that `## Ask the person` holds: its slug and the moment its reading waits for; an Estimate this session creates or updates has no such line, since Retro read it or set it `failed`; these lines stand in the section and are not debt (cases 624, 670.3).'
  change: 'the Debt section lists no Estimate the session creates or updates as a reading that waits: Retro reads it or sets it failed (case 670.3)'
- slug: estimate-handoff-holds-each-fact-once
  set:
    status: pending
    method: one reading by hand of .claude/skills/handoff/SKILL.md as rendered, or, at the Retro of the session that changes it, of the new Render of rule-handoff in the Spec, against the Criterion, recorded in the estimate line
  change: the Criterion replaced whole — Debt lists no Estimate the session creates or updates as a reading that waits (case 670.3)
```

```tasks
- [x] update `rule-handoff`
- [x] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
- [x] update `estimate-handoff-holds-each-fact-once`
- [x] read `estimate-handoff-holds-each-fact-once`
```

### Case 670.4 — Pre-spec reports a method that waits for another session

> **given:**
> `rule-case-protocol`: the Render of the Case form, which sets what a `method` holds.
> **＋** `vault/wiki/case-schema.md`: the file rendered from it.
> **＋** `rule-prespec-hook`: the rule of the pre-spec check.
> **＋** `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`: the new check of this promise.
> **＋** `guppi/lint.py`: holds the predicate.
> **＋** `guppi/prespec.py`: the pre-spec check that calls it.
> **＋** `tests/test_prespec.py`: the tests of the finding.
> **＋** `tests/test_lint.py`: the tests of the predicate.
> **＋** `/hi`: the command that opens a session, which a method may name.

> **when:**
> `uv run guppi prespec --check <plan> --session <id>` of `guppi/prespec.py` reads the `method` of a `create` of an Estimate, or of an `update` that carries `set: {method: …}`, in the `then` blocks of the plan file.

> **then:**
> A `method` with a part between two `;` that names a later session, the next session, a session after another, the librarian or `/hi` gives one line `case N: <create|update> <slug>: method waits for another session — a method holds only what runs in its own session`.
> **＋** The judgment is one predicate in `guppi/lint.py`, which `guppi/prespec.py` imports.
> **－** A part that names the person, such as the person's answer at `/hi`, gives no such line.
> **－** `uv run guppi lint` of `guppi/lint.py` over the live Estimate pages gives no finding by this predicate.
> **－** The line does not replace the finding of a `method` that names no form or that ties its reading to a one-off moment.

```then
create:
- slug: estimate-prespec-hook-reports-a-method-that-waits-for-another-session
  ref: rule-prespec-hook
  kind: QA
  purpose: Whether pre-spec reports a method in the plan that waits for a later session, the librarian or a /hi, by one predicate of guppi/lint.py, and leaves a method that names the person and the live pages alone
  method: uv run pytest tests/test_prespec.py tests/test_lint.py -k waits
  tags:
  - harness
  - workflow
update:
- slug: rule-case-protocol
  replace:
  - old: 'or the text the item writes under `sections: Criterion` (cases 188, 194.1). A rule with several promises'
    new: 'or the text the item writes under `sections: Criterion` (cases 188, 194.1). Its `method` holds only what runs in the Case''s own session — a test, a command, a probe, or the reading of the Spec at Retro — or the person''s answer; a problem seen live in a later session is a lesson, and pre-spec reports a `method` that waits for a later session, the librarian or a `/hi` (case 670.4). A rule with several promises'
  - old: through the `read` line of one the Case creates or sets `pending` or through one its `context` names,
    new: through the `read` line of one the Case creates or sets `pending`, which the Retro of the Case's own session takes on the Criterion of the Spec (case 670.4), or through one its `context` names,
  change: a method holds only what runs in the Case's own session, or the person's answer; Retro takes the read line of the Case's own Estimate (case 670.4)
```

```tasks
- [x] update `rule-case-protocol`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `guppi/lint.py`: a predicate `waits_for_another_session` over the parts of a `method` between `;`, with its docstring; `check_moment` and the lint run do not call it.
- [x] `guppi/prespec.py`: the check of the form of an Estimate item calls `waits_for_another_session` on the `method` of a `create` and of an `update` that sets one, and the module docstring names the finding.
- [x] `tests/test_lint.py`: the predicate is true for a later session, the next session, a session after another, the librarian and `/hi`, and false for a part that names the person and for a method of the session itself.
- [x] `tests/test_prespec.py`: the finding on a `create` and on an `update` with `set: {method: …}`, none on a method that names the person, and the other method findings unchanged.
- [x] create `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`
- [x] read `estimate-prespec-hook-reports-a-method-that-waits-for-another-session`
```

### Case 670.5 — /hi reads no transcript and turns an unreadable Work line into a Case

> **given:**
> `rule-skill-hi`: the Render of the `/hi` skill, whose reading step changes.
> **＋** `.claude/skills/hi/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-hi-takes-its-readings`: its Criterion is replaced whole.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier `/hi` writes.
> **＋** `vault/wiki/brief.md`: holds the `pending` readings and the Ask list.

> **when:**
> The person types `/hi` of `.claude/skills/hi/SKILL.md` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md` and whose `## Ask` holds its readings that only the person can take.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose whole method runs now.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the files and commands the method names.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **＋** For each other open `W` line, whose reading cannot run now, it writes one line under `## Cases` of `raw/<date>/<hi HHMM>/frontier.md` that names the Estimate by slug and asks to fix its method, replace its Criterion or archive it; the `W` line closes `· case N` when that Case is ratified.
> **＋** In the same reply, before the question on the order, it puts each open `A` line to the person as a question: the Estimate by slug and its question.
> **＋** When the person answers one, the agent closes its `A` line `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md` first, then writes its `estimate[...]` line, the answer as its result, in a `LEDGER` block of the reply, which ends in text.
> **－** It reads no transcript of an earlier session.
> **－** A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and is no Cases line.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: 'Before the question on the order, in the same reply, take each reading of an open `W` line whose whole method can be done now: each moment its `method` names is this `/hi` or has come in an earlier session (case 613.2). Read what the method names from the brief, `git log`, `git status` and the commands the method names, and each moment of an earlier session — the librarian''s run, `/retro`, `/handoff` or any other — from the transcript of the latest session that held it: the event logs `vault/raw/<date>/event_log.md` name each session by the first characters of its id, and its transcript is the file of Claude Code whose name opens with that id; read each part of the method from the session where its moment came.'
    new: 'Before the question on the order, in the same reply, take each reading of an open `W` line whose whole method runs now, from files and commands alone: the brief, `git log`, `git status`, and the files and the commands the method names; read no transcript of an earlier session (case 670.5).'
  - old: A reading with a moment that has come in no session yet, or whose transcript Claude Code no longer holds, waits for its next moment, and its line stays open; a reading whose `method` asks for a `/hi` run of its own is not taken here (cases 508.1, 613.2).
    new: 'An open `W` line whose reading cannot run now — its method waits for a moment of an earlier session, for a moment not come, or for a `/hi` run of its own — needs a decision: write one line for it under `## Cases` of `frontier.md`, the Estimate by slug in a code span and the words that its method, its Criterion or the page itself is fixed, replaced or archived, with the source `brief`; its `W` line closes `· case N` when that Case is ratified. A `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, stays open under `## Work` and waits for that session (case 670.5).'
  - old: a `failed` reading or a lesson of the Tail; an item the person adds.
    new: a `failed` reading or a lesson of the Tail; an open `W` line whose reading cannot run now, written by the reading step below (case 670.6); an item the person adds.
  change: '/hi reads no transcript: it takes the readings it can run now, and an open Work line it cannot read becomes a Cases line, but those of the close of a sprint (cases 670.5, 670.6)'
- slug: estimate-hi-takes-its-readings
  set:
    status: pending
    purpose: Whether /hi takes, in its first reply, each open W reading whose whole method runs now from files and commands, reads no transcript, writes a Cases line for each other open W line but those of the close of a sprint, puts each open Ask line to the person and writes the answer as its reading line, and opens no page but the Estimates it reads
    method: by hand, the text of the skill file rendered from rule-skill-hi, or, at the Retro of the session that changes it, the new Render of rule-skill-hi in the Spec, read against the Criterion, recorded in the estimate line
  change: the Criterion replaced whole — /hi reads no transcript, and an open Work line it cannot read becomes a Cases line (case 670.5)
```

```tasks
- [x] update `rule-skill-hi`
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] update `estimate-hi-takes-its-readings`
- [x] read `estimate-hi-takes-its-readings`
```

### Case 670.6 — The Frontier names an unreadable Work line among the sources of a Cases line

> **given:**
> `estimate-hi-writes-frontier`: its Criterion is replaced whole.
> **＋** `rule-skill-hi`: its Render lists the sources of a Cases line, changed by 670.5.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: the Frontier `/hi` writes.
> **＋** `vault/wiki/sprint.md`: the sprint, whose current milestone gives items.
> **＋** `vault/wiki/brief.md`: the brief, whose Next session gives items.
> **＋** `vault/wiki/backlog.md`: the backlog, whose items the Frontier counts.

> **when:**
> The person invokes `/hi` of `rule-skill-hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, `## Work`, with lines `- [ ] W<n> — <title> · <source>`, and `## Ask`, with lines `` - [ ] A<n> — `<slug>` — <question> · brief ``. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line; then, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an open `W` line whose reading cannot run now, written by the reading step of `/hi`; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`. Ask: the `Ask the person` list of the brief's Next session.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** While the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, no conserved Spec and no item of the current milestone is a Cases line, and each conserved Spec stays in `vault/wiki/backlog.md`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** Pre-spec finds an open line under `## Cases`. A `W` or an `A` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

```then
update:
- slug: estimate-hi-writes-frontier
  set:
    status: pending
  change: the Criterion replaced whole — an open W line whose reading cannot run now is a source of a Cases line (case 670.6)
```

```tasks
- [x] update `estimate-hi-writes-frontier`
- [ ] read `estimate-hi-writes-frontier`
```

### Case 670.7 — The Work line of an Estimate the session changes closes at Retro

> **given:**
> `rule-work-mode`: the Render of the `/work` skill, whose step of the Work readings changes.
> **＋** `.claude/skills/work/SKILL.md`: the skill file rendered from it.
> **＋** `estimate-work-mode-takes-the-work-readings`: its Criterion is replaced whole.
> **＋** `/retro`: the Retro that reads each Estimate the session changes and closes its line, by 670.2.
> **＋** `/box`: runs a conserved Spec and calls `/work` with its folder.
> **＋** `vault/raw/<date>/<HHMM>/`: the folder of a conserved Spec.
> **＋** `raw/<date>/<hi HHMM>/spec.md`: the Spec Work Mode runs.
> **＋** `raw/<date>/<hi HHMM>/frontier.md`: holds the `W` lines.
> **＋** `vault/wiki/where-to-stop.md`: the conditions of a stop.

> **when:**
> The agent calls `/work` of `rule-work-mode` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.
> **＋** Or `/box` called `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, and the last task of that folder's `spec.md` is done.

> **then:**
> Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
> **＋** A moment of an earlier session, such as the librarian's run, has come.
> **＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and its `estimate[...]` line stands in the `LEDGER` block of the one reply that ends Retro.
> **＋** The tasks, the readings and `/retro` run in one turn, and no reply ends before the reply that ends Retro, except at a stop of `vault/wiki/where-to-stop.md`.
> **－** A reading of an Estimate this session creates or updates is not taken in this step: its `W` line stays open until `/retro` reads that Estimate or sets it `failed`, and closes the line.
> **－** With a folder from `/box`, a reading of an Estimate that a decision line of that folder's `ledger.md` creates or updates is not taken in this step either, and Retro closes its `W` line the same way.
> **－** A reading whose moment has not come is not taken, and its `W` line stays open.
> **－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

```then
update:
- slug: rule-work-mode
  replace:
  - old: 'and one whose moment has not come: its line stays open.'
    new: 'and one whose moment has not come: its line stays open; Retro reads an Estimate this session or that folder creates or updates, or sets it `failed`, and closes its line (case 670.7).'
  change: the Work line of an Estimate the session changes stays open until Retro reads it and closes it (case 670.7)
- slug: estimate-work-mode-takes-the-work-readings
  set:
    status: pending
    method: by hand, the text of the skill file rendered from rule-work-mode, or, at the Retro of the session that changes it, the new Render of rule-work-mode in the Spec, read against the Criterion, recorded in the estimate line
  change: the Criterion replaced whole — the Work line of an Estimate the session changes closes at Retro (case 670.7)
```

```tasks
- [x] update `rule-work-mode`
- [x] `uv run guppi render`: `.claude/skills/work/SKILL.md`
- [x] update `estimate-work-mode-takes-the-work-readings`
- [x] read `estimate-work-mode-takes-the-work-readings`
```

## Case 671 — A ratified Case built again without a target of its lines goes back for a new number

> **context:**
> When the person ratifies a Case, the ledger gets one decision line per page the Case creates or changes. The ledger only grows, and only a `{supersedes:case N}` mark retires a line. Today the check of the file `case-guppi` writes, `shape_findings` of `guppi/casecheck.py` (case 610.1), sends back a ratified Case only when its layout of sub-cases changed. A Case built again under its number with a target renamed or dropped passes that check, and the Spec hook then refuses the old line, by `check_lines` of `guppi/prespec.py`. In session 1616 the create of Case 663 was renamed under its number, the hook refused "case 663: line [create][estimate-synthesis-reads-the-status-the-run-sets] has no item in the plan", and Case 668 had to supersede 663 (`lesson-case-build-renamed-a-slug-of-a-ratified-case-under-its-old-number`). Session 2300 met the same fault with a dropped create (`lesson-ledger-a-dropped-item-needs-a-superseding-sub-case`). The two lessons are the children of `insight-ledger-ratified-line-never-withdrawn`.
> The person chose that the check sends such a Case back with a new number and the marks, as it does for a change of layout. The person also chose to delete the draft `rule-ledger-line-withdrawn-on-re-ratification`, which case 594 put off, and which proposed that a second ratification withdraws the old lines. Case 671.1 adds the check, under a new Estimate, and closes the Insight. Case 671.2 adds the renamed or dropped target to the Splitting section of `case-schema.md`, and deletes the draft rule. Its delete line carries `{supersedes:case 594}`, so that it retires the defer of the page.
> The new check judges an item by `line_has_item` of `guppi/prespec.py`, which is the judgment the Spec hook runs. It takes the new number from `new_number` of `guppi/casecheck.py`, so its number and its marks agree with the finding of the layout check. It skips a number with no section or with sub-cases in the file, since the layout check already gives that Case its finding. It skips a `defer` line, as the layout check does. The check only sends a Case back before ratification, so no ledger line is lost and no old form is kept. `casecheck --subagent` is the one hook on `SubagentStop` in `.claude/settings.json`.
> The Estimates. `estimate-case-check-sends-back-a-ratified-case-in-another-shape` stands. Its Criterion speaks of the layout, and its last line says that a Case in its layout gets no finding of that check, which stays true. `estimate-case-check-sends-back-a-faulty-case` and `estimate-case-check-sends-back-a-clash-with-another-case` judge other faults and stand. For 671.2, `estimate-case-protocol-loaded` stands. It promises that `case-schema.md` equals the Render of `rule-case-protocol` and holds the form, the sub-cases among it, and a sentence added to that section keeps both true. The send-back that the sentence describes is checked by the Estimate of 671.1. The deleted page carries no promise, and the `make lint` of the librarian's run checks that no live page links to it.
> The frame. Case 670.4 of this session updates `rule-case-protocol` by `replace` pairs in its paragraphs on a `create` of an Estimate and on the boxes of the Spec. A sub-case of Case 669 updates its paragraph on an `update` of an Estimate. The pair of 671.2 is in the Splitting section, so no Case touches another's text. The pair adds a sentence of its own, since the layout check and its Estimate mean the layout alone by "another shape". The finding tells `case-guppi` to change the number by `Edit`, as the frame of `case-guppi` in `rule-case-build` sets for any finding on the file, and `estimate-case-build-writes-the-case` stands. The finding of the layout check (case 610.1) still says to build the Case again under the new number, and a later Case may align its words. This session's Retro still follows its old rendered text until the librarian renders Case 670, so it takes no reading of the Estimate of 671.1. The next `/hi` takes that reading by its pytest `method`. A Grep `rule-ledger-line-withdrawn-on-re-ratification` over `{vault/wiki/**,guppi/**,.claude/**,tests/**}` printed 4 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md` and `vault/wiki/insights/insight-ledger-ratified-line-never-withdrawn.md`. The librarian writes `backlog.md` and `brief.md` from the pages, and `log.md` is history, so these three stand. The `## Proposal` of the Insight says that the draft stands in the backlog, which the delete makes false, so the update of 671.1 replaces those words. A Grep `new number|another shape` over `{vault/wiki/rules/**,vault/wiki/*.md,.claude/**,guppi/**}` printed 8 files: `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/case-schema.md`, `vault/wiki/log.md`, `guppi/casecheck.py`, `vault/wiki/rules/rule-case-protocol.md`, `vault/wiki/rules/rule-spec-write.md` and `vault/wiki/rules/rule-glossary.md`. The hits in `rule-case-protocol`, its file `case-schema.md` and `guppi/casecheck.py` enter this Case. The hit in `rule-spec-write` is a History line. The hit in `rule-glossary` speaks of a row of the glossary table. `brief.md`, `backlog.md` and `log.md` were not read. These four stand.

> **problem:**
> A Case ratified in the session and built again under its number with a target renamed or dropped passes every check until the Spec hook refuses its old line. A whole new Case then has to supersede it.

> **recommend:**
> - **How the gap is closed**
>   - Recommended: (a) the check of a rebuilt Case also sends it back when a ledger line of one of its numbers has no item under that number, with the new number and the marks, and the draft `rule-ledger-line-withdrawn-on-re-ratification` is deleted.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) a new Estimate under `rule-case-check` with its own tests; the Estimate of the layout check stays as it is.
>   - Answer: agreed, (a).

### Case 671.1 — The check sends back a ratified Case built again without the item of one of its lines

> **given:**
> `estimate-case-check-sends-back-a-ratified-case-without-a-target`: the new check of this promise.
> **＋** `rule-case-check`: the rule of the check of the file `case-guppi` writes.
> **＋** `guppi/casecheck.py`: the check, which holds `shape_findings` and `new_number`.
> **＋** `guppi/prespec.py`: holds `line_has_item`, the judgment of the Spec hook.
> **＋** `tests/test_casecheck.py`: the tests of the check.
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md`: the file of a Case that `case-guppi` writes and the check reads.
> **＋** `raw/<date>/<hi HHMM>/ledger.md`: the session's ledger, whose decision lines the check reads.
> **＋** `insight-ledger-ratified-line-never-withdrawn`: the Insight this Case closes.

> **when:**
> `SubagentStop` fires when `case-guppi` stops after it wrote or edited `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and `uv run guppi casecheck --subagent` of `guppi/casecheck.py` reads the Cases of that file and the decision lines of the session's `raw/<date>/<hi HHMM>/ledger.md`.

> **then:**
> For each number of the family of a top-level Case N in the file that has a section in the file and no sub-case under it, the hook reads the decision lines of that number in the session's ledger, of a kind other than `defer`.
> **＋** A line whose kind and slug has no item under that number, in the `then` block that the hook builds from the file, gives Case N a finding. The judgment of an item is `line_has_item` of `guppi/prespec.py`, imported.
> **＋** The finding names the number and the line, and tells `case-guppi` to build the Case under the number that `new_number` of `guppi/casecheck.py` gives. Its decision lines carry one `{supersedes:case N}` for the number N, and one `{supersedes:case M}` for each number M of the family that has a decision line.
> **＋** The hook exits 2 with the finding on stderr. `case-guppi` fixes the file by `Edit`: it puts the item back, or it changes the number in the headings and the ledger lines and adds the marks. It does not write the whole Case again.
> **－** A `defer` line gives no finding of this check.
> **－** A number with no section in the file, or with a sub-case in the file, gets no finding of this check.
> **－** A Case whose items hold each decision line of its numbers gets no finding of this check, whatever items it adds.

```then
create:
- slug: estimate-case-check-sends-back-a-ratified-case-without-a-target
  ref: rule-case-check
  kind: QA
  purpose: Whether a Case that has decision lines in the session and comes back from case-guppi under its number without the item of one of those lines goes back to case-guppi with a new number to build it under
  method: uv run pytest tests/test_casecheck.py -k dropped_target
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: insight-ledger-ratified-line-never-withdrawn
  set:
    status: actioned
    addressed_by: decision-case-671.1
  replace:
  - old: (rule-ledger-line-withdrawn-on-re-ratification stands in the backlog)
    new: (rule-ledger-line-withdrawn-on-re-ratification was deleted by case 671.2)
  change: 'actioned: the check of the file case-guppi writes sends back a ratified Case built again without the item of one of its lines, with the new number and the marks (case 671.1)'
```

```tasks
- [x] `guppi/casecheck.py`: a function `target_findings` gives `(top-level case, finding)` for each decision line other than `defer` of the session's ledger on a number of the family that has a section in the answer and no sub-case in it, whose kind and slug `line_has_item` of `guppi/prespec.py`, imported, does not find in that number's `then` block; the finding names the number, the line, the new number by `new_number` and the marks as `shape_findings` writes them, and tells `case-guppi` to put the item back or to change the number in the headings and the ledger lines by `Edit` and add the marks, never writing the whole Case again; `check_answer` adds its findings where `store` is given, beside `shape_findings`; the module docstring and the docstring of `check_answer` name it (case 671.1).
- [x] `tests/test_casecheck.py`: tests `-k dropped_target`: a file whose Case renames the slug of a ratified `create` under its number is sent back with the new number and the marks; a file that drops an item of a ratified line is sent back; a file that keeps each item and adds one passes; a dropped `defer` item gives no finding of this check; a number with no section, or with sub-cases, gets only the finding of `shape_findings`.
- [x] create `estimate-case-check-sends-back-a-ratified-case-without-a-target`
- [x] update `insight-ledger-ratified-line-never-withdrawn`
- [x] read `estimate-case-check-sends-back-a-ratified-case-without-a-target`
```

### Case 671.2 — The schema names a renamed or dropped target among the Cases built under a new number

> **given:**
> `rule-case-protocol`: the Render of the Case form, whose Splitting section changes.
> **＋** `vault/wiki/case-schema.md`: the file rendered from it, which `case-guppi` reads whole.
> **＋** `rule-ledger-line-withdrawn-on-re-ratification`: the draft rule put off by case 594, which this Case deletes.

> **when:**
> `case-guppi` reads `vault/wiki/case-schema.md`, rendered from `rule-case-protocol`, before it builds again a Case that has decision lines in the session's ledger.

> **then:**
> The Splitting section says, in a sentence apart from the Cases built again in another shape, that a Case that comes back in its shape without the item of one of its decision lines, its target renamed or dropped, is built under a new number too.
> **＋** The section says that the check of the file `case-guppi` writes sends such a build back and names the new number, and that `case-guppi` changes the number by `Edit` and does not write the whole Case again.
> **－** `rule-ledger-line-withdrawn-on-re-ratification` no longer stands as a draft for withdrawing the old lines.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: names the new number (case 610.1).
    new: names the new number (case 610.1). A Case that has a decision line in the session's ledger and comes back in its shape, but without the item of one of those lines under its number — the target of that line renamed or dropped — is built under a new number too, its decision lines carrying the same marks; the check of the file case-guppi writes sends it back with the new number, and case-guppi changes the number in the headings and the ledger lines by `Edit` and adds the marks, never writing the whole Case again (case 671.1).
  change: 'Splitting: a Case built again under its number without the item of one of its decision lines takes a new number too (case 671.2)'
delete:
- slug: rule-ledger-line-withdrawn-on-re-ratification
  impact: the draft rule of the backlog leaves; a ratified Case built again without a target takes a new number that supersedes it, and the check of case 671.1 sends back one that keeps its number; the defer of case 594 is retired by the supersedes mark of this line
```

```tasks
- [x] update `rule-case-protocol`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] delete `rule-ledger-line-withdrawn-on-re-ratification`
```
