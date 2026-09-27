<!-- approved 17:49:48 · session b52dee54 -->

# Spec — session 1255, 2026-09-27

## Case 449 — Story sections judged by the person, counts kept out of given, when and then

> **context:**
> The `## Language` section of `vault/wiki/case-schema.md` is the Render of `rule-case-protocol`. It allows a case number in `context` or `problem` only when the Case is about that case. It allows no count of items, no line number and no quotation there unless the Case is about one. `estimate-case-protocol-case-form` promises the same rules, and it failed again in session 2300. The context of Case 446 cited cases 378.5 and 428.1 as sources and counted "three places". The problem of Case 445 cited case 410. The case-number rule also conflicts with `CLAUDE.md`, which asks for a real source.
> The person decided the following. The story sections never enter an Estimate, so they must be short and readable. The person's complaint is their test, not a script. So far the only complaint is their length. The rules on case numbers, counts, line numbers and quotations leave the story sections. A count goes stale in `given`, `when` and `then`, because `when` and `then` become a Criterion. So the count rule moves there. A number that states a condition stays.
> Since Case 452, a built Case reaches the person as the file `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the chat holds a short Russian text and the `ratification`. So the Criterion names the file as the place where the form stands, and a new `purpose` says so. The chat keeps the wording of `estimate-case-protocol-shows-the-built-case`, which Case 452.4 signed. The Purpose of `rule-case-check` and the docstring of `guppi/casecheck.py` say that no script checks a count in a story section. They now say that the person judges the text of those sections, while the check still requires the sections and their order. This Case actions `insight-case-form-chat-form-read-by-no-script` and rejects its proposal for the story sections. No page is created, so no vault query was run. `estimate-case-protocol-case-form` stays `pending` until a later session reads it.

> **problem:**
> The rules on case numbers and counts in `context`, `problem` and `recommend` fail at almost every reading. The case-number rule conflicts with the rule to name a real source. Neither rule serves the person, whose only complaint is the length of `context`. Meanwhile, nothing keeps counts out of `given`, `when` and `then`, where they go stale.

> **given:**
> `rule-case-protocol` — its Render `vault/wiki/case-schema.md`, the `## Language` section on the story sections and on `given`, `when` and `then`
> **＋** `.claude/agents/case-guppi.md` — the agent that builds the Case, unchanged
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file that holds a built Case
> **＋** `estimate-case-protocol-case-form` — the promise of the form of a built Case
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of what the chat shows, unchanged
> **＋** `rule-case-check` — the hook that writes the file, and its Purpose, which names what the check does not read
> **＋** `guppi/casecheck.py` — the check on `SubagentStop`, whose docstring says the same
> **＋** `insight-case-form-chat-form-read-by-no-script` — the Insight this Case actions

> **when:**
> The hook of `rule-case-check` writes a Case that `case-guppi` built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and the main agent sends that file to the person, at its first showing or again.

> **then:**
> The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
> **＋** `context`, `problem` and `recommend` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — and the person raised no complaint in the session about their length or clarity.
> **＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
> **＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
> **＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
> **＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
> **＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-case-protocol-shows-the-built-case`, and the reply ends with a plain question.
> **＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole.
> **－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: '; the list of what the Case touches is `given` (case 378.1); a case number stands in `context` or `problem` only when the Case is about that case; no line numbers and no quotation unless the Case is about one; no count of items — lines, pages, Estimates, Cases — unless the Case is about that count: a count goes stale first, and what can be counted a script counts; `problem` says'
    new: '; the list of what the Case touches is `given` (case 378.1); `context`, `problem` and `recommend` explain briefly — a sentence per part where one is enough, a part with nothing to say left out — and may name a case number as the source of a claim; no script judges them: the person does, and a complaint of their length or clarity is what changes them (case 449); `problem` says'
  - old: '`then` holds behaviour only; the bookkeeping is `tasks`.'
    new: '`then` holds behaviour only; the bookkeeping is `tasks`. `given`, `when` and `then` hold no count of items — pages, lines, Estimates, Cases, tests — since `when` and `then` become the Criterion of an Estimate and a count goes stale there first; a number that states a condition or a limit, such as more than 400 000 tokens, stands (case 449).'
  change: the story sections explain briefly, may name a case number as a source, and are judged by the person; the rules on counts, line numbers and quotations in them removed; no count of items in given, when and then (case 449)
- slug: estimate-case-protocol-case-form
  set:
    status: pending
    purpose: A built Case carries the whole contract in given, when and then, in the file the person is sent
  change: the Criterion replaced whole — the form stands in the file of a built Case; context, problem and recommend brief plain prose judged by the person's complaint, a case number, a count, a line number or a quotation there no fault; no count of items in given, when and then (case 449)
- slug: rule-case-check
  replace:
  - old: a count in a story section is not among them — no script tells a count from other words
    new: 'the text of the story sections — `context`, `problem` and `recommend` — is not among them, only their presence and their order: the person judges the text (case 449)'
  change: the Purpose says the person judges the text of the story sections, while the check requires them and their order (case 449)
- slug: insight-case-form-chat-form-read-by-no-script
  set:
    status: actioned
    addressed_by: decision-case-449
  change: 'actioned: the proposal for the story sections rejected — the person judges the text of context, problem and recommend, and no script reads it; the order of the sections and ratification are checked since case 419.3 (case 449)'
```

```tasks
- [x] update `rule-case-protocol` — two `replace` pairs in the `## Language` section of the Render
- [x] update `estimate-case-protocol-case-form` — the Criterion replaced whole, the purpose set
- [x] update `rule-case-check` — one `replace` pair in the Purpose
- [x] update `insight-case-form-chat-form-read-by-no-script` — actioned
- [x] `guppi/casecheck.py` — the docstring: the text of the story sections is not checked, the person judges it
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-case-form` — by hand in a later session
```

## Case 450 — The agent's text judged by the person's complaint

> **context:**
> `rule-agent-writing` renders the section `## How the agent writes` into `CLAUDE.md`: keep the facts, name a real source, make no claim wider than its output, write short active sentences, give the answer first, name what is not done. Its one promise, `estimate-agent-writing-followed`, is read by the agent against its own replies. Its last two readings failed. Each time, one claim in a long session did not match a file. In session 2300 a reply said the ledger gained amended lines of 445.6. The ledger hook runs after the reply and adds no line it already holds, so only the line of 445.7 was new. Another reply gave W32 a closer meant only for sprint items, and the next reply corrected it. The rule text already forbids both slips. The test failed, not the text.
> The person decided the following. The section `## How the agent writes` stays as it is. The Criterion is replaced whole, and the person's complaint becomes the test, as Case 449 did for the story sections. A slip that the agent corrected itself is no fault. The W32 slip stays out of this Case, because the Frontier file never held the wrong closer. The form of the Frontier is promised by `estimate-hi-writes-frontier`. Its check, `estimate-prespec-checks-the-frontier`, is changed by Case 451.2 of this session, which also refuses a closer that does not agree with its source.
> This Case creates no page, so no vault query was run. `CLAUDE.md` is rendered again by Case 452.5 for its `## Language` section. The section this rule renders does not change, so `estimate-claude-md-rendered` is not touched.

> **problem:**
> The promise of `rule-agent-writing` rests on the agent reading its own replies. It fails whenever one claim in a long session slips, even a slip the agent corrected. No reading finds the text of the rule wrong. The test does not serve the person, who is the reader the rule exists for.

> **given:**
> `estimate-agent-writing-followed` — the promise of the rule, whose Criterion this Case replaces whole
> **＋** `rule-agent-writing` — the rule, whose Render is the section `## How the agent writes`
> **＋** `CLAUDE.md` — the file the session loads, which holds that section

> **when:**
> A session starts with `CLAUDE.md` loaded, and the agent writes a text — a reply, a page, a commit message, a document.

> **then:**
> The person raised no complaint in the session that the agent's text broke the section `## How the agent writes` of `CLAUDE.md` — a claim with no real source or wider than the output it rests on, a sales pitch, a long or passive sentence, an answer not given first, a not-done left implied.
> **－** A slip in the agent's text that the agent found and corrected itself, with no complaint of the person, is no fault.
> **－** The code the agent writes is not a text of this rule; `make style` judges the code.

```then
update:
- slug: estimate-agent-writing-followed
  set:
    status: pending
    purpose: The agent's text holds to the section How the agent writes of CLAUDE.md, and the person's complaint is the test
    method: by hand in a later session — the person's messages of one session read for a complaint about the agent's text, against the section in CLAUDE.md
  change: the Criterion replaced whole — the person's complaint is the test of the agent's text, a slip the agent corrected itself no fault (case 450)
```

```tasks
- [x] update `estimate-agent-writing-followed` — the Criterion replaced whole, the purpose and the method set
- [ ] read `estimate-agent-writing-followed` — by hand in a later session
```

## Case 451 — One standard for putting an item off, and a backlog that holds every deferred item

> **context:**
> A Frontier line closes with a box and a closer, which is the last segment after ` · `. Today an item is put off in three ways, and each leaves a different trace:
> - A sprint item passed over closes `[-] … · sprint`. It gets no Case, and `generate` moves it to the sprint page's `## Backlog` after three such sessions in a row.
> - A decision put off closes `[-] … · defer case N`, with a short-form Case and `deferred_by` on its page.
> - An item of the brief's Deferred list left as it stands closes `[-] … · deferred · kept`, and the brief carries it on.
>
> `prespec.check_frontier` ties the box to the closer only for `sprint` and `kept`. So in session 2300 a brief item could take the closer `sprint` and pass. The brief's Deferred list holds at most seven items, and an item cut off the seven drops out of sight. A Spec conserved by `carry` stands only in the brief that `carry` writes.
> The person decided one standard:
> - `[x]` is an item ended: `case N` when decided, `work` when done with no decision.
> - `[-]` is an item put off: `· sprint · defer` for a sprint item, with no Case, as case 356.2 set; `· backlog · kept` for a backlog item left as it stands, with no Case; `· defer case N` for a new decision put off.
> - The check ties the box, the closer and the source in both directions.
> - `vault/wiki/backlog.md` holds every deferred item. `guppi backlog` writes it, under a new rule `rule-backlog`. It holds the conserved Specs with their targets, and a line for each page with `deferred_by`, each open Insight and each line of the sprint page's `## Backlog`, with its `purpose` and a count of the sessions that put it off.
> - `sprint.md` stops showing `## Backlog`.
> - The brief drops its Deferred list and its cap.
> - `/hi` loads the backlog. The Frontier writes the backlog's count, names the backlog items near a Frontier item, and puts each conserved Spec first under `## Cases`.
> - Open Insights compete for nothing: they stand in the backlog like any other item.
> - The librarian and `carry` run `guppi backlog`, and `make lint` runs its `--check`.
>
> The vault query found no page that holds every deferred item. The near pages are `rule-sprint` and `rule-brief`. `rule-vault-layout` requires a rule that names the new file, and `rule-one-judgment-one-implementation` requires the count to use the Frontier reader of the sprint move. The new slugs are free and the tags exist.
> Beyond the agreed sub-cases, the frame and pre-spec added these: `rule-internal-context` (451.12), `rule-documentation` (451.13), `rule-harness` (451.14), and the Estimate of the rendered schema of Insights (451.15), each with the Estimate that speaks of it.
> These stand, for the reasons given:
> - `case-schema.md` and the Purpose of `rule-skill-hi` name what `/hi` loads without `backlog.md`, and so does the Criterion of `estimate-hi-no-read-calls`. None of them claims the list is complete. The `Given:` list of `estimate-vault-layout-holds` gives examples.
> - `estimate-case-protocol-defers-in-one-reply` speaks of `· defer case N`, which stays.
> - `estimate-case-protocol-loaded` promises only that the file equals its Render.
>
> This session's Frontier closes with the old closers, because the new check is built in Work Mode. Frontier files of earlier sessions are not rewritten.

> **problem:**
> An item is put off in three ways with three different traces, and the check misses a closer given to the wrong source. The brief's cap of seven drops deferred items out of sight, and a conserved Spec stands only in a brief. The person wants one standard for putting an item off, and one place that holds every deferred item.

### Case 451.1 — The closers of a Frontier line, and the Frontier drawn from the backlog

> **given:**
> `rule-skill-hi` — the Render of `/hi`: how the Frontier is assembled and how its lines close
> **＋** `.claude/skills/hi/SKILL.md` — the skill file rendered from it
> **＋** `rule-case-protocol` — its Render: the paragraph on Plan Mode and the Frontier, and the short form
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `estimate-hi-writes-frontier` — the promise of the Frontier, whose Criterion this sub-case replaces whole
> **＋** `vault/wiki/backlog.md` — the file the Frontier reads the backlog from
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md` — the other files `/hi` loads
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier file of the session

> **when:**
> The person invokes `/hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, and `## Work`, with lines `- [ ] W<n> — <title> · <source>`. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a list with their detail, the backlog count and the near items; the Work is shown as one block; sub-cases are cut in Cases only. A `W` that turns out to need a decision closes `· case N`; a `C` that needs none closes `· work`.
> **－** `Pull:` and `Open issues:` are a Cases item only when `vault/wiki/sprint.md` names no decision on them.
> **－** Pre-spec finds an open line under `## Cases`. A `W` line stands open until its work is done and closes `· work` in Work Mode. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

```then
update:
- slug: rule-skill-hi
  replace:
  - old: on a plan branch the unfinished plan, first; the items of the sprint's current milestone
    new: on a plan branch the unfinished plan, and each conserved Spec `backlog.md` names, one line each with the source `backlog`, first; the items of the sprint's current milestone
  - old: the `Cases` list of the brief's Next session; the brief's Deferred list; a hand edit shown by `Render:`
    new: the `Cases` list of the brief's Next session; a hand edit shown by `Render:`
  - old: '`## Work`, what needs none: the `Work` list of the brief''s Next session; a dirty tree in `Status:`.'
    new: '`## Work`, what needs none: the `Work` list of the brief''s Next session; a dirty tree in `Status:`. The other items of `backlog.md` are no lines of their own: `## Cases` ends with the line `Backlog: N items`, N the items `backlog.md` counts, and under a Cases line an indented line `- near` names, by slug in a code span, each backlog item whose `purpose` is near that line in meaning — the agent''s own judgment from `backlog.md` in its context, no `ask-guppi`; an item the person brings onto the Frontier is a Cases line of its own, source `backlog`, its title opening with its slug in a code span, so that `guppi backlog` counts it (case 451.1).'
  - old: '(case 314.1): `[x] … · case N` when ratified, `[x] … · work` when it needs no decision, `[-] … · defer case N` when deferred, `[-] … · sprint` when the item is a line of the sprint page left for a later session — no decision, no `deferred_by` (case 310.5), never `· defer case N` (case 356.2); `[-] … · deferred · kept` when an item of the brief''s Deferred list, source `deferred`, is left deferred as it stands — no Case, no ledger line, the brief carries it on (case 421.4);'
    new: '(case 314.1). `[x]` is an item ended: `[x] … · case N` when ratified, `[x] … · work` when it needs no decision. `[-]` is an item put off: `[-] … · sprint · defer` when the item is a line of the sprint page left for a later session — no Case, no ledger line, no `deferred_by`, never `· defer case N` (cases 310.5, 356.2); `[-] … · backlog · kept` when an item of `backlog.md` is left as it stands — no Case, no ledger line, it stays in the backlog; `[-] … · defer case N` when a decision of any other source is put off — a short-form Case and its ledger line, and its target enters `backlog.md` through `deferred_by` (case 451.1);'
  change: the Frontier closes a line [x] for an item ended and [-] for one put off — sprint · defer, backlog · kept, defer case N; conserved Specs first, the backlog counted and its near items named (case 451.1)
- slug: rule-case-protocol
  replace:
  - old: close its line in the reply that ends the item — `· case N` when ratified, `· work` when it needed no decision, `· defer case N` when deferred, `[-] … · sprint` for an item of the sprint left for later — never `· defer case N` (case 356.2) — and `[-] … · deferred · kept` for an item of the brief's Deferred list left as it stands (case 421.4).
    new: 'close its line in the reply that ends the item — `[x]` for an item ended: `· case N` when ratified, `· work` when it needed no decision; `[-]` for an item put off: `[-] … · sprint · defer` for an item of the sprint left for later — no Case, never `· defer case N` (case 356.2) — `[-] … · backlog · kept` for an item of `backlog.md` left as it stands, and `[-] … · defer case N` for a decision of any other source put off (case 451.1).'
  - old: 'An item of the brief''s Deferred list left as it stands is no decision: no short Case, no ledger line; its Frontier line closes `[-] … · deferred · kept`, the page keeps its `deferred_by`, and the brief carries the item on (case 421.4).'
    new: 'An item of `backlog.md` left as it stands is no decision: no short Case, no ledger line; its Frontier line closes `[-] … · backlog · kept`, its source stays as it is — the `deferred_by` of its page, the `open` status of its Insight, or its line in the sprint page''s `## Backlog` — and the item stays in the backlog, its count grown by one (cases 421.4, 451.1). The target of a short Case enters `backlog.md` through the `deferred_by` that `generate` writes.'
  change: the closers of a Frontier line — [x] an item ended, [-] put off as sprint · defer, backlog · kept or defer case N; an item of backlog.md left as it stands keeps its source (case 451.1)
- slug: estimate-hi-writes-frontier
  set:
    status: pending
  change: the Criterion replaced whole — the closers of the standard, conserved Specs first, the backlog counted and its near items named, no Deferred list of the brief (case 451.1)
```

```tasks
- [x] update `rule-skill-hi` — four `replace` pairs in the Render
- [x] update `rule-case-protocol` — two `replace` pairs in the Render
- [x] update `estimate-hi-writes-frontier` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-hi-writes-frontier` — by hand at the first `/hi` of a later session
```

### Case 451.2 — The check ties the box, the closer and the source

> **given:**
> `rule-prespec` — the Render of `/pre-spec`: the sentence on the findings of the Frontier
> **＋** `.claude/skills/pre-spec/SKILL.md` — the skill file rendered from it
> **＋** `guppi/prespec.py` — `check_frontier`, the check, and its docstring
> **＋** `tests/test_prespec.py` — the tests of the check
> **＋** `estimate-prespec-checks-the-frontier` — the promise of the check, whose Criterion this sub-case replaces whole
> **＋** `vault/raw/<date>/<HHMM>/frontier.md` — the Frontier the check reads

> **when:**
> `uv run guppi prespec --check <plan>` reads the session's `vault/raw/<date>/<HHMM>/frontier.md`.

> **then:**
> A missing file is the finding `frontier: <path> is missing`.
> **＋** An open line under `## Cases` is a finding. An open line under `## Work` is not.
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
  - old: closed by a Case the plan does not hold, or closed `[x]` whose closer — the last segment after ` · ` — is `sprint`; `[-] … · sprint` is clean, a sprint item left for a later session, no Case and no `defer` needed (case 310.6), `[-] … · deferred · kept` is clean, an item of the brief's Deferred list left as it stands, and `kept` on an `[x]` box or after another source is a finding (case 421.3), and a line whose source segment is `sprint` closed `· defer case N` is a finding — a sprint item is not deferred (case 356.2),
    new: 'closed by a Case the plan does not hold or `· defer case N` with no `defer` item under Case N, or whose box and closer — the last segment after ` · ` — disagree: `[x]` takes only `case N` or `work`, an item ended, and `[-]` only `defer`, `kept` or `defer case N`, an item put off; `defer` alone is clean only after the source segment — the one before the closer — `sprint`, a sprint item left for a later session, and `kept` only after the source `backlog`, an item of `backlog.md` left as it stands; `defer case N` after the source `sprint` or `backlog` is a finding — neither is deferred by a Case (cases 356.2, 451.2),'
  change: the Frontier check ties the box, the closer and the source both ways — defer after sprint, kept after backlog, defer case N after any other source (case 451.2)
- slug: estimate-prespec-checks-the-frontier
  set:
    status: pending
    purpose: The Frontier of the session exists and every closed line has a box and a closer that agree with its source
  change: the Criterion replaced whole — the box, the closer and the source checked both ways (case 451.2)
```

```tasks
- [x] update `rule-prespec` — one `replace` pair in the Render
- [x] update `estimate-prespec-checks-the-frontier` — the Criterion replaced whole
- [x] `guppi/prespec.py` — `check_frontier`: the closers `case N`, `work`, `defer`, `kept`, `defer case N`; the box checked against the closer; `defer` only after `sprint`, `kept` only after `backlog`, `defer case N` a finding after either; the closer `sprint` and the source `deferred` gone; the docstring
- [x] `tests/test_prespec.py` — a test per pairing of box and closer, per source of `defer`, `kept` and `defer case N`, and a `Backlog: N items` line and a `- near` line left unread; the tests of `sprint` and `kept` moved to the new closers
- [x] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [x] read `estimate-prespec-checks-the-frontier` — `uv run pytest tests/test_prespec.py` in a later session
```

### Case 451.3 — A sprint line put off closes `sprint · defer`

> **given:**
> `estimate-prespec-binds-a-sprint-line` — the promise on a sprint line, whose Criterion this sub-case replaces whole
> **＋** `rule-prespec` — the rule it is a promise of
> **＋** `guppi/prespec.py` — `check_frontier`, which binds a decided sprint line to an `update` of the sprint page
> **＋** `tests/test_prespec.py` — the tests selected by `-k sprint`
> **＋** `entity-sprint-<id>` — the sprint page

> **when:**
> `uv run guppi prespec --check <plan>` reads a line of the session's Frontier whose source segment, the one before the closer, is `sprint`.

> **then:**
> A line closed `[x] … · sprint · case N` needs an `update` item of `entity-sprint-<id>` under Case N, in the parent or in any sub-case. Without one, it is the finding `frontier: C<n> closes a sprint item with case N, no update of the sprint page under Case N`.
> **＋** A line closed `[-] … · sprint · defer` needs nothing and is no finding. The item stays in its milestone until `generate` moves it to the `## Backlog` of `entity-sprint-<id>` after three such sessions in a row.
> **－** A line whose source segment is not `sprint` is read by the other checks of the Frontier. The word inside the slug of a title is not the source.

```then
update:
- slug: estimate-prespec-binds-a-sprint-line
  set:
    status: pending
    purpose: A Frontier line of the sprint closed by a Case is a finding of prespec --check unless that Case updates the sprint page; a line left [-] with sprint · defer needs nothing
    method: uv run pytest tests/test_prespec.py -k sprint — a line `· sprint · case N` with and without an update of entity-sprint-<id> under Case N, a `[-] … · sprint · defer` line, a line whose source segment is not `sprint` while the word stands inside the slug of its title
  change: the Criterion replaced whole — a sprint line put off closes [-] · sprint · defer (case 451.3)
```

```tasks
- [x] update `estimate-prespec-binds-a-sprint-line` — the Criterion replaced whole
- [x] `tests/test_prespec.py` — `test_a_left_sprint_item_closes_with_sprint` on a line `[-] … · sprint · defer`
- [x] read `estimate-prespec-binds-a-sprint-line` — `uv run pytest tests/test_prespec.py -k sprint` in a later session
```

### Case 451.4 — `rule-backlog`: one file that holds every deferred item

> **given:**
> `rule-backlog` — the new rule, the guard of the backlog file
> **＋** `rule-documentation` — its parent, the phase of the librarian
> **＋** `vault/wiki/backlog.md` — the file the rule governs
> **＋** `guppi/backlog.py` — the script `guppi backlog`, which writes it
> **＋** `guppi/cli.py` — where the command is registered
> **＋** `tests/test_backlog.py` — the tests of the script
> **＋** `estimate-backlog-renders` — the new promise of the render
> **＋** `guppi/materialize.py` — the reader of the Cases and `then` blocks of a Spec, reused
> **＋** `guppi/generate.py` — `frontier_marks`, the Frontier reader of the sprint move, reused
> **＋** `entity-sprint-<id>` — the sprint page, whose `## Backlog` is a source
> **＋** `vault/raw/`, `vault/archive/` — where the Frontier files and the conserved Specs stand
> **＋** `rule-one-judgment-one-implementation` — one reader of a Frontier line and one of a Spec
> **＋** `entity-glossary` — the terms: a row for the backlog, and the rows on the brief, on an Insight and on `/hi`
> **＋** `rule-insights-schema` — its Render says where an open Insight reaches the person
> **＋** `vault/wiki/insights/schema.yaml` — the file rendered from it

> **when:**
> `uv run guppi backlog` runs over `vault/wiki/`, `vault/raw/` and `vault/archive/`. The librarian runs it after `guppi sprint`, and the skill `carry` runs it after it writes `carry.md`.

> **then:**
> The script writes `vault/wiki/backlog.md`: the heading `# Backlog`, the line `N items`, then `## Conserved Specs` and `## Deferred`.
> **＋** `## Conserved Specs` holds each session folder under `vault/raw/` that holds `carry.md`. Each has one line that names its `spec.md` and its Cases. Under that line stands one line per item of its `then` blocks, with the kind and the slug, read by the Spec reader of `guppi/materialize.py`.
> **＋** `## Deferred` holds one line per item. The items are each live page with a `deferred_by` that is not empty, each Insight whose `status` is `open`, and each line of the `## Backlog` of `entity-sprint-<id>`. A line holds the slug, the page's `purpose` (for an Insight, its `pattern` and `severity`) and the count. A Backlog line that names no page stands by its text.
> **＋** The count of an item is the number of sessions whose `frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names its slug in a code span of its title. It is read by `generate.frontier_marks`, the reader of the sprint move.
> **＋** `N` counts the conserved Specs and the lines of `## Deferred`. A slug that stands under a conserved Spec does not stand again under `## Deferred`, and a slug of two sources stands once.
> **＋** A folder whose `carry.md` is gone shows nothing. Its defers enter `## Deferred` through `deferred_by` once `materialize` and `generate` have applied them.
> **－** The script writes no page of `vault/wiki/` and no file but `vault/wiki/backlog.md`. The governed-files hook refuses a hand edit of that file.

```then
create:
- slug: rule-backlog
  type: rule
  kind: Leaf
  purpose: 'Prevents a deferred item from dropping out of sight: a defer, an open Insight, a sprint item without a turn or a conserved Spec that no list shows to the next session'
  enforcement: check
  implementation_ref:
  - guppi/backlog.py
  - tests/test_backlog.py
  governs: vault/wiki/backlog.md
  tags:
  - session
  - workflow
  - harness
  - librarian
  - sprint
  sections:
    Purpose: 'Prevents a deferred item from dropping out of sight. Before case 451 the brief carried at most seven deferred items, and an item cut off the seven stood on no list the next session read; a Spec conserved by `carry` stood only in the brief `carry` wrote. `vault/wiki/backlog.md` is not a document: `guppi backlog` writes it from what the vault already stores — each session folder under `raw/` that holds `carry.md`, with the targets of its Spec; each live page with `deferred_by`; each open Insight; each line of the `## Backlog` of the sprint page — one line per item with its `purpose`, or an Insight''s `pattern` and `severity`, and the count of the sessions whose Frontier put it off. The count reads the Frontier files by `generate.frontier_marks`, the reader of the sprint move, and the Specs by the reader of `materialize`, one judgment in one module (`rule-one-judgment-one-implementation`). The librarian runs the script after `guppi sprint`, and `carry` after it writes `carry.md`; `/hi` loads the file, and the Frontier writes its count and names the items near a Frontier item. An item leaves when its source changes: a Case that decides it supersedes its defer, an Insight is actioned, a line leaves the sprint page''s `## Backlog`, or the session that finishes a conserved Spec deletes `carry.md`. `governs` names the file, so the governed-files hook refuses a hand edit; `guppi backlog --check` renders in memory and names the file when it differs, and `make lint` runs it.'
- slug: estimate-backlog-renders
  type: estimate
  kind: QA
  purpose: guppi backlog writes backlog.md from the conserved Specs, the pages with deferred_by, the open Insights and the Backlog of the sprint page, each item with its purpose and its count
  method: uv run pytest tests/test_backlog.py, plus one reading of vault/wiki/backlog.md after the librarian's run
  tags:
  - harness
  - sprint
  ref: rule-backlog
update:
- slug: entity-glossary
  replace:
  - old: surfaces in the brief's Deferred list and is the target
    new: stands in `backlog.md` while `open` and is the target
  - old: '| The handover between sessions, written by the librarian — deferred items capped at 7, ranked by Insight severity then postponements, leaving out what the sprint page names — or by `/carry`, which conserves a Spec and keeps the previous list whole (case 200.2) | [[rule-brief]] |'
    new: |-
      | The handover between sessions, written by the librarian or by `/carry`, which conserves a Spec (case 200.2); no Deferred list — the deferred items stand in `backlog.md` (case 451.8) | [[rule-brief]] |
      | `backlog.md` | Every deferred item in one file, written by `guppi backlog`: the conserved Specs with their targets, then each page with `deferred_by`, each open Insight and each line of the sprint page's `## Backlog`, with its `purpose` or `pattern` and the count of the sessions that put it off; `/hi` loads it, writes its count and names the items near a Frontier item (case 451.4) | [[rule-backlog]] |
  - old: the open items it assembles (brief, sprint, issues, an unfinished plan, the ledger tail)
    new: the open items it assembles (brief, sprint, backlog, issues, an unfinished plan, the ledger tail)
  change: the term backlog.md added; the brief without a Deferred list, an open Insight in the backlog, the backlog among the sources of the Frontier (case 451.4)
- slug: rule-insights-schema
  replace:
  - old: It reaches the human through the Deferred list of `brief.md` and becomes an ordinary ratified Case there.
    new: It stands in `backlog.md` while `open`, and becomes an ordinary ratified Case when the person brings it onto a Frontier (case 451.4).
  change: an open Insight stands in backlog.md, a Case when the person brings it onto a Frontier (case 451.4)
```

```tasks
- [x] create `rule-backlog`
- [x] create `estimate-backlog-renders`
- [x] update `entity-glossary` — three `replace` pairs in `## Terms`
- [x] update `rule-insights-schema` — one `replace` pair in the Render
- [x] `guppi/backlog.py` — the script: the sources, the two sections, the count by `generate.frontier_marks`, the Specs by the reader of `guppi/materialize.py`, `--check`
- [x] `guppi/cli.py` — the command `backlog`
- [x] `tests/test_backlog.py` — each source, a slug of two sources once, a slug under a conserved Spec not repeated, the count over `raw/` and the archive, a folder without `carry.md`, no page written
- [x] `uv run guppi render`: `vault/wiki/insights/schema.yaml`
- [x] `uv run guppi glossary`
- [x] read `estimate-backlog-renders` — after the librarian's run of a later session
```

### Case 451.5 — `guppi backlog --check` in `make lint`

> **given:**
> `estimate-backlog-checks-the-file` — the new promise of the check
> **＋** `rule-backlog` — the rule it is a promise of
> **＋** `guppi/backlog.py` — the flag `--check`
> **＋** `tests/test_backlog.py` — the tests of the check
> **＋** `Makefile` — the target `lint`
> **＋** `rule-lint` — its Purpose names the checks `make lint` runs before lint
> **＋** `vault/wiki/backlog.md` — the file compared

> **when:**
> Someone runs `uv run guppi backlog --check`, by hand or through `make lint`.

> **then:**
> When `vault/wiki/backlog.md` differs from the render of its sources, the check prints one line on stdout that names the file and exits 1. When it is the same, the check is silent and exits 0. The file is written in neither case.
> **＋** `make lint` runs it after `sprint --check` and before `glossary --check`.
> **－** `make lint` writes nothing to the tree.

```then
create:
- slug: estimate-backlog-checks-the-file
  type: estimate
  kind: QA
  purpose: guppi backlog --check names backlog.md when it differs from the render of its sources, exit 1, and writes nothing
  method: uv run pytest tests/test_backlog.py, plus make lint after the librarian's run — no backlog line
  tags:
  - harness
  - sprint
  ref: rule-backlog
update:
- slug: rule-lint
  replace:
  - old: '`make lint` runs it after `render --check`, `sprint --check` and `glossary --check`; all four only report'
    new: '`make lint` runs it after `render --check`, `sprint --check`, `backlog --check` and `glossary --check`; all five only report'
  change: make lint runs backlog --check (case 451.5)
```

```tasks
- [x] create `estimate-backlog-checks-the-file`
- [x] update `rule-lint` — one `replace` pair in the Purpose
- [x] `Makefile` — `uv run guppi backlog --check < /dev/null` in `lint`, after `sprint --check`; the help line of the target
- [x] `tests/test_backlog.py` — `--check` on a file equal to the render and on one that differs; nothing written
- [x] read `estimate-backlog-checks-the-file` — after the librarian's run of a later session
```

### Case 451.6 — `sprint.md` no longer shows the Backlog

> **given:**
> `rule-sprint` — its Purpose describes the file `guppi sprint` writes
> **＋** `guppi/sprint.py` — the script and its docstring
> **＋** `tests/test_sprint.py` — the tests of the render
> **＋** `estimate-sprint-renders-the-backlog` — the promise of the render, whose Criterion this sub-case replaces whole
> **＋** `entity-sprint-<id>` — the sprint page the script reads
> **＋** `vault/wiki/sprint.md` — the file it writes
> **＋** `vault/wiki/backlog.md` — where the page's `## Backlog` is shown now

> **when:**
> `uv run guppi sprint` runs with a live page `entity-sprint-<id>` and reads its `estimates`, `## Purpose`, `## Milestones` and `## Closed`.

> **then:**
> The file `vault/wiki/sprint.md` holds, in order: `# Sprint`; `## <id>`; Purpose; `**Done when**`, one line per Estimate; then `## Milestones`; then `## Closed` as it is. Under `## Milestones`: a closed milestone is one line `### [x] <name>`. The current one is the heading `### [ ] <name>` and each item with its status and `deferred_by`. Each later one is one line `### [ ] <name> — N items: ` with its items separated by commas; an item with a wikilink stands as `[[slug]]`, an item without one by its text, with no tick and no status.
> **＋** Every heading of the file stands between blank lines: a blank line follows each `### ` line, collapsed or whole.
> **＋** An item is ticked by the statuses of every page its `[[slug]]` before the first ` — ` names. It is `[x]` when each is `built`, `passed` or `archived`, with the statuses after ` · ` in the order of the slugs. A wikilink after the ` — ` is text. A line with no wikilink before the ` — ` is a note, `- [ ] <text>`, never ticked, and it keeps its milestone open.
> **＋** A milestone is closed when every item is `[x]`. With no item it is open.
> **－** The `## Backlog` of the page is not written into the file. `vault/wiki/backlog.md` shows it.
> **－** A slug with no live or archived page gives one line on stderr and exit 1, and the file is not written. `--check` compares this same render.
> **－** The script writes no page of `vault/wiki/`, `entity-sprint-<id>` included.

```then
update:
- slug: rule-sprint
  replace:
  - old: (case 236) — and the `## Backlog`, the items without a turn, as a list;
    new: (case 236); the `## Backlog` of the page, the items without a turn, is not rendered here — `guppi backlog` shows it in `backlog.md` (case 451.6);
  change: sprint.md no longer shows the Backlog; backlog.md does (case 451.6)
- slug: estimate-sprint-renders-the-backlog
  set:
    status: pending
  change: the Criterion replaced whole — the Backlog of the page is not rendered into sprint.md (case 451.6)
```

```tasks
- [x] update `rule-sprint` — one `replace` pair in the Purpose
- [x] update `estimate-sprint-renders-the-backlog` — the Criterion replaced whole
- [x] `guppi/sprint.py` — the render without `## Backlog`; the docstring
- [x] `tests/test_sprint.py` — the render without `## Backlog`; a slug of the Backlog without a page no longer an error of `guppi sprint`
- [x] `uv run guppi sprint`
- [x] read `estimate-sprint-renders-the-backlog` — `uv run pytest tests/test_sprint.py` and the rendered `sprint.md` after the librarian's run of a later session
```

### Case 451.7 — The sprint move counts the lines put off under the new closers

> **given:**
> `estimate-sprint-moves-a-passed-over-item` — the promise of the move, whose Criterion this sub-case replaces whole
> **＋** `rule-sprint` — the rule it is a promise of
> **＋** `entity-sprint-<id>` — the sprint page whose items move
> **＋** `vault/raw/`, `vault/archive/` — where the Frontier files stand

> **when:**
> `uv run guppi generate` has applied every entry of the run and has run the cascade.

> **then:**
> For every item under `## Milestones` of `entity-sprint-<id>`, the script reads the `frontier.md` of `vault/raw/` and `vault/archive/`, from the newest session to the oldest by date and `HHMM`. It counts the lines whose title, the text before the first ` · `, holds one of the item's slugs in a code span.
> **＋** A `[-]` line adds one. That is an item put off, closed `· sprint · defer`, `· backlog · kept` or `· defer case N`. An `[x]` line stops the count. A session without such a line is passed by.
> **＋** At a count of 3 or more, the item's line leaves its milestone, unchanged, for the end of `## Backlog`.
> **＋** The History of the sprint page gets the line `moved to the Backlog: <slug> passed over in <N> sessions in a row — <HHMM>, … · generate`, and stdout gets one line on the move.
> **－** An open `[ ]` line is not counted.
> **－** A note is not counted and not moved; a note is a line with no `[[slug]]` before the ` — `. The items of `## Backlog` and `## Closed` are not counted.

```then
update:
- slug: estimate-sprint-moves-a-passed-over-item
  set:
    status: pending
  change: the Criterion replaced whole — a line put off under the closers of case 451, Given lifted into When and Then (case 451.7)
```

```tasks
- [x] update `estimate-sprint-moves-a-passed-over-item` — the Criterion replaced whole
- [x] read `estimate-sprint-moves-a-passed-over-item` — `uv run pytest tests/test_generate.py` and the History of the sprint page after the librarian's run of a later session
```

### Case 451.8 — The brief without a Deferred list

> **given:**
> `rule-brief` — the frame of the brief: its Purpose and its Render
> **＋** `.claude/agents/librarian-guppi.md` — the agent file its Render splices into
> **＋** `estimate-brief-written` — the promise of the brief, whose Criterion this sub-case replaces whole
> **＋** `vault/wiki/brief.md` — the file the librarian writes
> **＋** `vault/wiki/backlog.md` — where the deferred items stand now
> **＋** `rule-carry-over` — the second writer of the brief

> **when:**
> The librarian rewrites `vault/wiki/brief.md` at the end of its run.

> **then:**
> The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
> **＋** It holds no Deferred list and no cap on deferred items. They stand in `vault/wiki/backlog.md`.
> **＋** Where things stand, Readings due, Flags and Readings at the close are as before. Flags also name every item `generate` moved to the sprint page's Backlog in the run, and every milestone it dropped.
> **＋** Next session holds `Cases` and `Work`. `Cases` is what needs a decision: a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, with what and from where. `Work` is what is done without a decision: every `pending` reading of Readings due by its slug, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
> **＋** An item stands in either `Cases` or `Work`, never in both. A list with no item is the line "none".
> **－** The brief states no decision: the sort by kind is not a judgment of the work.
> **－** The brief of the skill `carry` keeps its short shape, without Next session and without a Deferred list. `rule-brief` and `rule-carry-over` both say so.

```then
update:
- slug: rule-brief
  replace:
  - old: '[[brief]] is a shop window, not storage: every deferred item lives on as a page — a draft placeholder, or the open Insight itself — and the vault query before a `create` finds it there. So the deferred list is capped, the flags are not, and nothing in the brief is a decision.'
    new: '[[brief]] is a shop window, not storage: every deferred item lives on as a page — a draft placeholder, or the open Insight itself — and `backlog.md` lists them all, so the brief carries no Deferred list (case 451.8); the flags have no cap, and nothing in the brief is a decision.'
  - old: '- Deferred: at most seven items — one per target of a `defer` entry in the yamls the walk named, every item of the previous brief''s list whose decision no `supersedes` retired, and every Insight whose `status` is `open` — but never a target the sprint page names, under a milestone or in its Backlog: the sprint is its window, and its count of briefs does not grow (case 229.4). Rank by `severity` — the Insight''s own, or that of the Insight related to a deferred Case — then by the number of briefs the item has stood in: the previous brief''s count plus one. An Insight''s line carries its slug, its `severity`, its `pattern` and its Proposal in one or two sentences; in Plan Mode it is a Case whose `recommend` starts from that Proposal, and it ends in an `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written the same way, or a `defer` with the Insight as its target. - Flags, no limit:'
    new: '- Flags, no limit:'
  - old: Deferred is the previous brief's list as it stands plus the `defer` items of this Spec by slug, less the targets the sprint page names (case 229.4); Flags say what the vault does not know about this session; no cap of seven and no ranking (case 190.4).
    new: so is the Deferred list — the conserved Spec and its targets stand in `backlog.md`; Flags say what the vault does not know about this session (cases 190.4, 451.8).
  change: the brief carries no Deferred list and no cap; the deferred items stand in backlog.md (case 451.8)
- slug: estimate-brief-written
  set:
    status: pending
  change: the Criterion replaced whole — no Deferred list, the deferred items in backlog.md (case 451.8)
```

```tasks
- [x] update `rule-brief` — three `replace` pairs, in the Purpose and the Render
- [x] update `estimate-brief-written` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] read `estimate-brief-written` — by hand after the librarian's run of a later session
```

### Case 451.9 — `carry` writes the backlog, and a brief without a Deferred list

> **given:**
> `rule-carry-over` — the Render of the skill `carry`
> **＋** `.claude/skills/carry/SKILL.md` — the skill file rendered from it
> **＋** `estimate-carry-over-writes` — the promise of the skill, whose Criterion this sub-case replaces whole
> **＋** `vault/wiki/brief.md` — the brief it rewrites in the short shape
> **＋** `vault/wiki/backlog.md` — the file `guppi backlog` writes, with the conserved Spec and its targets
> **＋** `vault/raw/` — the session folder it marks with `carry.md`
> **＋** `/retro`, `/handoff` — phases the skill does not run

> **when:**
> The agent calls the skill `/carry` on `PreToolUse Skill`, after the person answered "conserve" at the fork `ExitPlanMode` prints. The person never types it.

> **then:**
> The skill reads the tree. When the tree holds changes outside the session folder and `vault/wiki/brief.md`, the skill stops and says that work was done and the ordinary exit applies.
> **＋** Otherwise it rewrites `vault/wiki/brief.md` in the short shape, with no Deferred list.
> **＋** It puts `carry.md` into the session folder: one line, a flag for `materialize` and `guppi backlog`, not a document. The session that finishes the work deletes it.
> **＋** It runs `uv run guppi backlog`, and `vault/wiki/backlog.md` then shows the conserved Spec with its targets.
> **＋** It runs `make style` and commits `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`.
> **－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`, and it writes no decision. It writes no page of `vault/wiki/`.
> **－** The work stays sequential, session after session: one conserved Spec, no parallel work.
> **－** `.claude/skills/carry/SKILL.md` equals the Render of the page and is not edited by hand.

```then
update:
- slug: rule-carry-over
  replace:
  - old: rewrite the brief, mark the session folder, commit; run nothing else.
    new: rewrite the brief, mark the session folder, run `guppi backlog`, commit; run nothing else.
  - old: no Readings due, no Next session, no Readings at the close; Deferred is the previous brief's list as it stands plus the `defer` items of this Spec by slug, less the targets the sprint page names (case 229.4); Flags say what the vault does not know about this session. No cap, no ranking.
    new: no Readings due, no Next session, no Readings at the close, no Deferred list — the conserved Spec and its targets stand in `backlog.md` (case 451.9); Flags say what the vault does not know about this session.
  - old: Its presence tells `guppi materialize` to pass the unit by.
    new: Its presence tells `guppi materialize` to pass the unit by, and `guppi backlog` to show the Spec under its conserved Specs. Then run `uv run guppi backlog`; every line on its stderr goes into the reply.
  - old: 'commit `vault/raw/` and `vault/wiki/brief.md`:'
    new: 'commit `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`:'
  - old: write no page under `vault/wiki/` but the brief.
    new: write no page under `vault/wiki/` but the brief; `vault/wiki/backlog.md` is written by `guppi backlog` alone.
  change: carry writes the brief without a Deferred list, runs guppi backlog and commits backlog.md (case 451.9)
- slug: estimate-carry-over-writes
  set:
    status: pending
    purpose: /carry writes the brief and the mark and runs guppi backlog and nothing else
  change: the Criterion replaced whole — no Deferred list, guppi backlog run and backlog.md committed (case 451.9)
```

```tasks
- [x] update `rule-carry-over` — five `replace` pairs in the Render
- [x] update `estimate-carry-over-writes` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
- [ ] read `estimate-carry-over-writes` — the render and one live reading of a conserved session
```

### Case 451.10 — The acknowledging reply shows every line put off

> **given:**
> `estimate-case-protocol-acknowledging-reply` — the promise of the reply, whose Criterion this sub-case replaces whole
> **＋** `rule-case-protocol` — its Render: the paragraph on the acknowledging reply
> **＋** `vault/wiki/case-schema.md` — the file rendered from it
> **＋** `rule-ledger-write` — the ledger hook that the `LEDGER` block of the reply goes to

> **when:**
> The person ratifies a Case, or ratifies again a Case shown again after its ratification, and the agent writes the reply that acknowledges it.

> **then:**
> The reply has four parts, in this order. First, the `LEDGER` block. Second, the heading `## Case N — ratified` and a paragraph `Changes:` that says what changes, in one or two sentences. Third, a paragraph `Notes:` with facts that did not enter the Case, left out when there are none. Last, the heading `## Frontier`, the lines of `frontier.md` as a checklist, and the question which item is next. In the checklist the closed lines are folded into one, the open ones stand one per line with a short title, and the lines put off stand as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`.
> **＋** For a Case with sub-cases, one reply acknowledges every sub-case ratified: one `LEDGER` block with all their lines, one heading `## Case N — ratified` that names the ids, one Frontier.
> **＋** The reply that acknowledges a re-ratification carries the `LEDGER` block with the decision lines of each Case ratified again, as at its first ratification.
> **＋** The headings and labels are in the language of the chat.
> **＋** No tool call follows the `LEDGER` block in the same reply.
> **－** The ledger hook of `rule-ledger-write` does not append a repeated decision line a second time.
> **－** When a `Stop` hook other than the ledger hook of `rule-ledger-write` refuses the reply with exit 2, the agent's answer to the refusal is a reply of its own and may call tools. The `LEDGER` block stands written.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: the deferred as `[-] … · defer case N`
    new: the lines put off as `[-] … · sprint · defer`, `[-] … · backlog · kept` or `[-] … · defer case N`
  change: the acknowledging reply shows every line put off by its closer (case 451.10)
- slug: estimate-case-protocol-acknowledging-reply
  set:
    status: pending
  change: the Criterion replaced whole — the lines put off shown by the closers of case 451 (case 451.10)
```

```tasks
- [x] update `rule-case-protocol` — one `replace` pair in the Render
- [x] update `estimate-case-protocol-acknowledging-reply` — the Criterion replaced whole
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] read `estimate-case-protocol-acknowledging-reply` — by hand, the first acknowledging reply of a later session
```

### Case 451.11 — The layout of the vault names the backlog file

> **given:**
> `rule-vault-layout` — its Purpose names each file at the root of `wiki/`
> **＋** `vault/wiki/backlog.md` — the new file at the root
> **＋** `rule-backlog` — the rule that governs it

> **when:**
> The person or an agent reads the Purpose of `rule-vault-layout`, and `uv run guppi lint` reads the vault.

> **then:**
> The Purpose names `vault/wiki/backlog.md` among the records a script keeps by a named rule, written by `guppi backlog` under `rule-backlog`.
> **＋** `guppi lint` gives no `layout` finding on `vault/wiki/backlog.md`, because `rule-backlog` names it in `governs`.

```then
update:
- slug: rule-vault-layout
  replace:
  - old: 'or a record a script keeps by a named rule: `brief.md` by the frame of `rule-brief`,'
    new: 'or a record a script keeps by a named rule: `backlog.md` from `guppi backlog` under `rule-backlog`, `brief.md` by the frame of `rule-brief`,'
  change: backlog.md named among the files at the root of wiki/ (case 451.11)
```

```tasks
- [x] update `rule-vault-layout` — one `replace` pair in the Purpose
```

### Case 451.12 — `/hi` loads the backlog

> **given:**
> `rule-internal-context` — the `@` lines that `/hi` loads
> **＋** `.claude/skills/hi/SKILL.md` — the skill file its Render splices into
> **＋** `estimate-internal-context-loaded` — the promise of the load, whose Criterion this sub-case replaces whole
> **＋** `vault/wiki/backlog.md` — the file added to the load
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/case-schema.md`, `vault/wiki/glossary.md` — the files loaded already

> **when:**
> The person invokes `/hi`.

> **then:**
> The text of `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/case-schema.md` and `vault/wiki/glossary.md` is in the context of the first turn, in that order, without a read call.
> **＋** The glossary and the backlog reach a session through this block alone. After a compaction, their paths are in the list of `guppi recall`.
> **－** A subagent, such as `librarian-guppi`, `ask-guppi` or one of Work Mode, carries neither of them. Its prompt names what it needs.

```then
update:
- slug: rule-internal-context
  sections:
    Render: |-
      <!-- rule-internal-context -->
      @vault/wiki/sprint.md
      @vault/wiki/backlog.md
      @vault/wiki/brief.md
      @vault/wiki/case-schema.md
      @vault/wiki/glossary.md
      <!-- /rule-internal-context -->
  change: /hi loads backlog.md after sprint.md (case 451.12)
- slug: estimate-internal-context-loaded
  set:
    status: pending
    purpose: The text of sprint.md, backlog.md, brief.md, case-schema.md and glossary.md is present in the first turn's context after /hi, without a read call
  change: the Criterion replaced whole — backlog.md loaded by /hi (case 451.12)
```

```tasks
- [x] update `rule-internal-context` — the Render whole
- [x] update `estimate-internal-context-loaded` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
- [x] read `estimate-internal-context-loaded` — by hand at the `/hi` of a later session
```

### Case 451.13 — The librarian runs `guppi backlog`

> **given:**
> `rule-documentation` — the frame of the librarian: its steps after `cleanup`
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from it
> **＋** `estimate-documentation-completes` — the promise of the phase, whose Criterion this sub-case replaces whole
> **＋** `rule-index-check`, `rule-synthesis` — the index lines of the librarian's frame
> **＋** `guppi/`, `tests/`, `Makefile` — the scripts' own files the librarian may read
> **＋** `vault/archive/` — the archive the librarian does not read

> **when:**
> `librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

> **then:**
> `make test-documentation` is green: materialize, generate and cleanup as one pipeline.
> **＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
> **＋** The librarian read only the following, and nothing else:
> - `handoff.md`, the yamls, the index lines and `tags.md`;
> - the wiki pages it names in the report, each with the outcome and one of the reasons of its frame (same or near; a candidate cluster; a script's error; a fact for the brief);
> - the unticked `- [ ]` lines of the `spec.md` files, for Readings due and Next session;
> - of the ledger, only the count of its lines and the lines the yaml does not account for, named in the report.
>
> It read no other part of a Spec, and no plan, Decision page or archive file. The `Makefile`, `guppi/` and `tests/` are the scripts' own files and may be read.
> **＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
> **＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
> **＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
> **－** The librarian refuses an instruction of the handoff to repair a yaml entry, or to read the ledger beyond the one read above, a Spec beyond its `- [ ]` lines, a Decision page or the archive. It names what was asked and why in the report, and the refusal does not stop the run.
> **－** The ban on reading `vault/archive/` stays.

```then
update:
- slug: rule-documentation
  replace:
  - old: 5. Run `uv run guppi sprint`. It writes `vault/wiki/sprint.md` from the sprint page by the statuses of this run. Every line on its stderr is a flag.
    new: 5. Run `uv run guppi sprint`. It writes `vault/wiki/sprint.md` from the sprint page by the statuses of this run. Then run `uv run guppi backlog`. It writes `vault/wiki/backlog.md` from the conserved Specs, the pages with `deferred_by`, the open Insights and the `## Backlog` of the sprint page. Every line on the stderr of either is a flag.
  change: the librarian runs guppi backlog after guppi sprint (case 451.13)
- slug: estimate-documentation-completes
  set:
    status: pending
  change: the Criterion replaced whole — guppi backlog after guppi sprint, Given lifted into When and Then (case 451.13)
```

```tasks
- [x] update `rule-documentation` — one `replace` pair in the Render
- [x] update `estimate-documentation-completes` — the Criterion replaced whole
- [x] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
- [x] read `estimate-documentation-completes` — `make test-documentation` and the live reading of the librarian's run of a later session
```

### Case 451.14 — The order of `make lint` holds the backlog check

> **given:**
> `rule-harness` — its Purpose gives the order of the checks in `make lint`
> **＋** `estimate-harness-pipeline` — the promise of that order, whose Criterion this sub-case replaces whole
> **＋** `rule-sprint`, `rule-backlog` — the rules whose checks run in `make lint`
> **＋** `rule-documentation` — the parent of both
> **＋** `Makefile` — the targets `lint` and `test-harness`

> **when:**
> `make lint` and `make test-harness` run, and someone reads the Purpose of `rule-harness`.

> **then:**
> The Purpose says that three rules belong to no phase of the session: the renderer, the page `settings.json` is assembled from, and lint. With them, the checks of `rule-sprint` and `rule-backlog` run in `make lint`, in this order: the harness files against their pages, the sprint file against its page, the backlog file against its sources, the glossary file against its page, then the pages.
> **＋** The Purpose names the rules that belong to it and run in no pipeline: the schemas of the pages, the layout of the vault, the hook that refuses a hand edit of a rendered file, the hook that refuses a heredoc with a backslash or a file write, the page `CLAUDE.md` is rendered from, the pinned clock of the tests, the hook that shows the size of the context, and the hooks that read a page of the vault without its History.
> **＋** `make test-harness` is green. The steps of `make lint` before `guppi lint` (`render --check`, `sprint --check`, `backlog --check` and `glossary --check`) exit 0 with no output on the committed tree. `guppi lint` is read by its own Estimates.

```then
update:
- slug: rule-harness
  replace:
  - old: 'They run together in `make lint`, with the check of `rule-sprint` (a child of `rule-documentation`) between them, in this order: the harness files are checked against their pages, the sprint file against its page, the glossary file against its page, then the pages (cases 227, 306.5).'
    new: 'They run together in `make lint`, with the checks of `rule-sprint` and `rule-backlog` (children of `rule-documentation`) between them, in this order: the harness files are checked against their pages, the sprint file against its page, the backlog file against its sources, the glossary file against its page, then the pages (cases 227, 306.5, 451.14).'
  change: the order of make lint holds backlog --check after the sprint file (case 451.14)
- slug: estimate-harness-pipeline
  set:
    status: pending
  change: the Criterion replaced whole — backlog --check in the order of make lint (case 451.14)
```

```tasks
- [x] update `rule-harness` — one `replace` pair in the Purpose
- [x] update `estimate-harness-pipeline` — the Criterion replaced whole
- [x] read `estimate-harness-pipeline` — `make test-harness` and the live reading of `make lint` in a later session
```

### Case 451.15 — The promise of the schema of Insights holds the changed sentence

> **given:**
> `estimate-insights-schema-checked` — the promise of the schema, whose Criterion this sub-case replaces whole
> **＋** `rule-insights-schema` — the rule it is a promise of, whose Render 451.4 changes
> **＋** `vault/wiki/insights/schema.yaml` — the file rendered from it, which lint reads
> **＋** `tests/test_schemas.py` — the tests of the schema on the live file
> **＋** `vault/wiki/insights/schema.md` — the former file, which no longer exists

> **when:**
> `uv run guppi render` writes `vault/wiki/insights/schema.yaml` from `rule-insights-schema`, and `uv run guppi lint` reads a page of `vault/wiki/insights/` by the keys of that file.

> **then:**
> The file equals the Render. Lint reads these from it:
> - required: `type, pattern, status, children, severity, origin, sprint, created, tags`;
> - optional: `addressed_by, deferred_by`;
> - values: `status: open | actioned | archived`;
> - single: `addressed_by`;
> - conditional: `actioned` requires `addressed_by`;
> - `computed: [severity]`;
> - sections: `## Pattern` and `## History` required, `## Proposal` optional.
>
> **＋** An Insight page with these fields, values and sections has no `schema` finding. A page that lacks a required field, holds a value outside the list, misses a conditional or lacks a required section has one finding per defect.
> **＋** The prose of the former `schema.md` stands in the file as data:
> - `description`: the introduction, the Threshold, Reopening and the Slug, verbatim, except one sentence of the introduction. That sentence now says that an open Insight stands in `backlog.md` and becomes a Case when the person brings it onto a Frontier.
> - `fields` and `sections`: the rows of the tables, whole.
> - `examples`: the example page.
> - `fields.addressed_by` names one decision, the latest; a list is not its shape.
>
> **－** `vault/wiki/insights/schema.md` does not exist.

```then
update:
- slug: estimate-insights-schema-checked
  set:
    status: pending
  change: the Criterion replaced whole — one sentence of the introduction changed by case 451.4, Given lifted into When and Then (case 451.15)
```

```tasks
- [x] update `estimate-insights-schema-checked` — the Criterion replaced whole
- [x] read `estimate-insights-schema-checked` — `uv run pytest tests/test_schemas.py -k insights` and `make lint` in a later session
```

## Case 452 — A built Case sent to the person as a file, not retyped in the chat

> **context:**
> Today `case-guppi` answers with a Case, and the `SubagentStop` hook `guppi casecheck --subagent` checks the Case and stores it in `<plan>.checked.json`. The main agent then retypes the Case whole into the chat, with its name, `context`, `problem` and `recommend` translated into Russian. The `Stop` comparison refuses a retyped showing that differs from the stored answer, but only after the person has seen it. A long Case is a heavy text for the agent to copy and for the person to read on a phone. The person tested `SendUserFile` with `display: render` and read the file on the phone. The person decided the following. The hook writes the answer into `raw/<date>/<hi HHMM>/cases/case-<N>.md` in English, and only when the answer has no findings. The agent sends that file. The chat holds a short Russian text for each Case and sub-case, plus its ledger lines. Rounds stay in the chat. The Spec hook asks for a sending made after the newest store. The `Stop` check refuses a shown Case that has no sending in the same turn. This Case closes C9.
> This Case creates no page, so no vault query was run. The frame showed three consequences. The Spec hook no longer needs a showing whole. The `Stop` comparison covers only the sections a reply shows. The sentences of `rule-case-protocol`, `rule-case-check`, `rule-case-build` and `rule-language` that put the Case or its translation in the chat change. `estimate-case-protocol-case-form` is not touched here: Case 449 is built again so that its Criterion names the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` and what the chat shows, and so that it sets the page's `purpose`. `estimate-case-build-writes-the-case` stays, because `case-guppi` still writes no file. `estimate-spec-write-writes-a-defer` stays, because the short form is out of this Case.
> Not done: sending the plan file or `spec.md` at pre-spec, the short form, and the acknowledging reply stay as they are. No guard stops the main agent from writing a file under `cases/`.

> **problem:**
> The main agent retypes each built Case into the chat, so a showing can differ from the answer, and a long Case costs the agent and the person a large text. What shows a built Case to the person, and what do the checks require in its place?

### Case 452.1 — The check writes the file of a Case that passed

> **given:**
> `rule-case-check` — the `How it works` section on `SubagentStop`, and its Purpose
> **＋** `estimate-case-check-sends-back-a-faulty-case` — the promise of the check and the store
> **＋** `guppi/casecheck.py` — `subagent`, the store, and the new writer of the file
> **＋** `guppi/ratified.py` — the reading of the chat form the check uses
> **＋** `guppi/prespec.py` — `judge`, run over the answer
> **＋** `tests/test_casecheck.py` — the tests of `subagent`
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file of a built Case
> **＋** `rule-case-build` — `case-guppi` writes no file

> **when:**
> `SubagentStop` fires when `case-guppi` answers; its payload carries `last_assistant_message`, `agent_transcript_path` and `stop_hook_active`, and it may fire twice after one message to the subagent, the second time after a `SubagentHandback` call, with `stop_hook_active` true though no hook exited 2.

> **then:**
> `uv run guppi casecheck --subagent` takes as the answer the newest output of the subagent in `agent_transcript_path` that holds a Case heading — the `message` input of a `SubagentHandback` tool call or the text of an assistant message, whichever stands later — or `last_assistant_message` when `agent_transcript_path` is not readable or holds no such output.
> **＋** It reads each Case of the answer in the chat form, by the functions of `guppi/ratified.py`, builds each Case's section of the Spec in memory, as the Spec hook writes it, and runs `judge` of `guppi/prespec.py` over them, the decision lines of the `ratification` fence standing for the ledger.
> **＋** The categories whose schema rule the session changes, whose `create` and `defer` items `judge` does not judge by their keys, it takes from the decision lines of the `ratification` fences and of the session's window.
> **＋** It checks the chat form besides: the sections in the order of the schema, none missing that the schema requires, and a `ratification` that holds one untagged fence of ledger lines and nothing else.
> **＋** Each Case of the answer is stored, its text as the answer holds it, with its findings and the time of the store, in `<plan>.checked.json` beside the plan file of the session.
> **＋** When no Case of the answer has findings, it writes the Cases of the answer, as the store holds their text, into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case: the file is replaced whole when the answer holds the top-level Case, and only the section of a sub-case is replaced when the answer holds that sub-case alone.
> **＋** A finding exits 2 with the findings on stderr, each naming its Case, and `case-guppi` answers again, whatever `stop_hook_active` says.
> **－** An answer with a finding writes no file, and a finding for a Case whose text the store already holds with findings is stored again and exits 0, so an unchanged answer is not sent back twice.
> **－** An answer with no Case heading, an answer of another agent, or a session with no plan file is not sent back and exits 0; the first two are not checked, stored or written.

```then
update:
- slug: rule-case-check
  replace:
  - old: ; its prose the main agent translates for the chat (case 441).
    new: ; the Case reaches the person in a file the hook writes from the answer that passed them (case 452.1).
  - old: Each Case of the answer is stored, with its findings, in `<plan>.checked.json` beside the plan file of the session, a later answer for the same id replacing it.
    new: Each Case of the answer is stored, with its findings and the time of the store, in `<plan>.checked.json` beside the plan file of the session, a later answer for the same id replacing it. When no Case of the answer has findings, the hook writes the Cases of the answer, as the store holds their text, into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case — the file replaced whole, or only the section of a sub-case the answer holds alone; `case-guppi` itself writes no file (case 452.1).
  change: the check writes the file of a Case that passed, from the text it stores, and stores the time of the store (case 452.1)
- slug: estimate-case-check-sends-back-a-faulty-case
  set:
    status: pending
    method: uv run pytest tests/test_casecheck.py -k subagent, then by hand the first answer of case-guppi the hook sends back and the first file of cases/ it writes
  change: the Criterion replaced whole — the time of the store, and the file of a Case with no findings written from the stored text (case 452.1)
```

```tasks
- [x] update `rule-case-check` — one `replace` pair in the Purpose, one in `How it works`
- [x] update `estimate-case-check-sends-back-a-faulty-case` — the Criterion replaced whole
- [x] `guppi/casecheck.py` — `subagent` stores the time of the store and writes `raw/<date>/<hi HHMM>/cases/case-<N>.md` from the stored text when no Case has findings; one function names the path of the file; the docstring
- [x] `tests/test_casecheck.py` — the file written from the stored text, replaced whole, a sub-case section replaced alone, no file on a finding, the time in the store
- [ ] read `estimate-case-check-sends-back-a-faulty-case` — by hand in a later session
```

### Case 452.2 — The Stop check compares what the chat shows and requires the sending

> **given:**
> `rule-case-check` — the `How it works` section on `Stop`
> **＋** `estimate-case-check-shows-only-the-checked-case` — the promise of the comparison on `Stop`
> **＋** `guppi/casecheck.py` — `against_store`, `mechanical_parts`, `stop`, and the new reading of a `SendUserFile` call
> **＋** `guppi/ratified.py` — the Spec hook, which imports the comparison and the reading of a sending
> **＋** `tests/test_casecheck.py` — the tests of `stop`
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file a reply must send
> **＋** `rule-one-judgment-one-implementation` — the Spec hook imports the comparison and the reading of a sending

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

> **then:**
> `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line once line ends and trailing spaces are the same.
> **＋** A section the reply does not show is not compared: a showing of the heading, a short text and `ratification` alone passes when its `ratification` equals the answer.
> **＋** The name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared.
> **＋** A Case the store does not hold, a Case that differs in a compared section, a Case stored with findings, or a Case with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2, the reason and the findings on stderr.
> **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
> **＋** The Spec hook `guppi/ratified.py` judges a showing by the same comparison, and a sending by the same reading of the transcript, both imported from `guppi/casecheck.py`.
> **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared and need no sending.
> **－** On the re-fire (`stop_hook_active`) it exits 0.

```then
update:
- slug: rule-case-check
  replace:
  - old: is compared with the Case of the same id in `<plan>.checked.json` in its `given`, `when`, `then`, `tasks` and `ratification`, line by line
    new: is compared with the Case of the same id in `<plan>.checked.json` in each of its `given`, `when`, `then`, `tasks` and `ratification` that the reply shows, line by line
  - old: the name of its heading, its `context`, `problem` and `recommend`, which the main agent translates, are not compared (case 441);
    new: the name of its heading, its `context`, `problem` and `recommend`, and text under the heading outside its sections are not compared (cases 441, 452.2);
  - old: A Case the store does not hold, one that differs, or one stored with findings exits 2 with the reason and the findings on stderr.
    new: A Case the store does not hold, one that differs, one stored with findings, or one with no `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md` in the turn of the reply, N the id of its top-level Case, exits 2 with the reason and the findings on stderr; the Spec hook imports the same reading of a sending (case 452.2).
  change: the Stop comparison covers the sections a reply shows, the prose is not translated, and a shown Case needs a sending of its file in the same turn (case 452.2)
- slug: estimate-case-check-shows-only-the-checked-case
  set:
    status: pending
  change: the Criterion replaced whole — only the shown sections compared, and a sending of the file required in the turn (case 452.2)
```

```tasks
- [x] update `rule-case-check` — three `replace` pairs in `How it works`
- [x] update `estimate-case-check-shows-only-the-checked-case` — the Criterion replaced whole
- [x] `guppi/casecheck.py` — `against_store` compares the shown sections only; one function reads the `SendUserFile` calls of a transcript; `stop` refuses a shown Case with no sending of its file in the turn; the docstring
- [x] `tests/test_casecheck.py` — a showing of `ratification` alone that passes, one that differs, a shown Case with no sending, a sending of another file, the acknowledging reply not judged
- [ ] read `estimate-case-check-shows-only-the-checked-case` — by hand in a later session
```

### Case 452.3 — The Spec hook writes a Case the person was sent

> **given:**
> `rule-spec-write` — the `How it works` section
> **＋** `estimate-spec-write-copies-the-ratified-case` — the promise of the write from the stored answer
> **＋** `guppi/ratified.py` — the reading of the transcript and the refusal before the write
> **＋** `tests/test_ratified.py` — the tests of the write
> **＋** `guppi/casecheck.py` — the comparison and the reading of a sending, imported
> **＋** `guppi/materialize.py` — `tagged_blocks` and `item_keys`, the one reading of the blocks and the keys
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec the hook also writes
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file the person was sent

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads `<plan>.checked.json` beside the plan file for the answer of `case-guppi` stored under Case N, and the session's transcript for the `SendUserFile` calls on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and for the last earlier reply that shows Case N with at least one of its sections.

> **then:**
> The hook writes the stored answer of Case N into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `given`, `when` and `then` as the answer holds them; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points; `recommend` and `ratification` are not written.
> **＋** Each of the two blocks opens and closes with a fence of backticks one longer than the longest run of backticks that opens a line inside it, three at the least, which `tagged_blocks` of `guppi/materialize.py` reads back whole; the same fence rule holds for the blocks it writes into `raw/<date>/<hi HHMM>/spec.md` once it stands, and for the `then` block of a short-form defer under `## Deferred`.
> **＋** No `SendUserFile` call on the file of Case N made after the time the store holds for Case N: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A last showing of Case N that differs from the stored answer in a section it shows — by the one comparison `uv run guppi casecheck` makes on `Stop`, imported from `guppi/casecheck.py` — a store with no Case N, or a Case N stored with findings: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
> **＋** A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives the kind and the category of its item, or a value that holds a backtick in an outer span not padded on both sides, is refused: exit 2 with `` `<key>`: not a key of <kind> <slug> `` or `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
> **＋** No plan file in the event log, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys.
> **－** A reply with no showing of Case N is no refusal when the file of Case N was sent after the store.

```then
update:
- slug: rule-spec-write
  replace:
  - old: it reads the session's transcript for the last earlier reply that shows `## Case N —` whole and `<plan>.checked.json` for the answer of `case-guppi` stored under Case N by `rule-case-check`; a showing that differs from that answer — by the one comparison of `guppi/casecheck.py` on `Stop`, imported — a store with no Case N, or a Case N stored with findings is a refusal
    new: it reads `<plan>.checked.json` for the answer of `case-guppi` stored under Case N by `rule-case-check`, and the session's transcript for a `SendUserFile` call on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, and for the last earlier reply that shows Case N with a section; no such call made after the time of the store (case 452.3), a showing that differs from that answer in a section it shows — by the one comparison of `guppi/casecheck.py` on `Stop`, imported with its reading of a sending — a store with no Case N, or a Case N stored with findings is a refusal
  - old: the plan file named by `gate.plan_path`
    new: the plan file named by `plan_path` of the ledger module
  - old: No plan file, no showing, or a sub-point it cannot read
    new: No plan file, or a sub-point it cannot read
  change: the Spec hook writes a Case whose file was sent after its newest store and no longer needs a showing whole; the function that names the plan file named right (case 452.3)
- slug: estimate-spec-write-copies-the-ratified-case
  set:
    status: pending
  change: the Criterion replaced whole — a sending of the file after the newest store in place of a showing whole (case 452.3)
```

```tasks
- [x] update `rule-spec-write` — three `replace` pairs in `How it works`
- [x] update `estimate-spec-write-copies-the-ratified-case` — the Criterion replaced whole
- [x] `guppi/ratified.py` — the refusal with no sending of the file after the time of the store, the showing condition dropped, the reading of a sending imported from `guppi/casecheck.py`
- [x] `tests/test_ratified.py` — a Case written after a sending with no showing, refused with no sending, refused with a sending older than the store, a sub-case judged by the file of its parent
- [x] read `estimate-spec-write-copies-the-ratified-case` — by hand in a later session
```

### Case 452.4 — The main agent sends the file and writes a short text

> **given:**
> `rule-case-protocol` — its Render `vault/wiki/case-schema.md`: the `## Sections` section with its table, `## Who builds a Case` and `## Splitting`
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing of a built Case
> **＋** `rule-case-build` — its Purpose and its Render `.claude/agents/case-guppi.md`, which say how the Case is shown
> **＋** `rule-case-check` — the hooks that write the file and refuse a showing with no sending
> **＋** `insight-case-show-built-case-retyped-by-hand` — the Insight this sub-case actions
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file the main agent sends

> **when:**
> The main agent takes up a Frontier item, the person answers a round of questions or answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call, after the plan file stands with its title line; nothing of the Case stands in the chat before the answer.
> **＋** The person's answers to a round go to the same `case-guppi` by `SendMessage`, verbatim and untranslated, and so does a question or a change of the person on a shown Case.
> **＋** An answer with no Case heading is a round of questions: the main agent shows it in the chat translated into Russian, slugs, paths and quotations unchanged, and no Case is shown and no file is sent; no step of confirmation follows the last round.
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
  - old: — in the chat at every showing, the name in the language of the chat; in the Spec the same heading in English;
    new: — in the file of the Case at every showing and in the Spec, in English; in the chat the same heading, the name in Russian, over the short text of the Case (case 452.4);
  - old: In the chat a blockquote with the checklist, and under a line whose item writes content that content as sub-points
    new: In the file of the Case a blockquote with the checklist, and under a line whose item writes content that content as sub-points
  - old: A Case not yet ratified is shown again whole.
    new: A Case not yet ratified is sent again whole, in its file (case 452.4).
  - old: Its new answer is shown again whole,
    new: Its new answer is sent again whole, in its file,
  - old: The agent shows the Case of the answer whole, at every showing, its name, `context`, `problem` and `recommend` translated into Russian and the rest unchanged, its own text after one horizontal rule; a showing that the `Stop` comparison of `rule-case-check` refuses as different from the answer is followed, before the person answers, by a reply that shows the answer whole, translated the same way;
    new: 'The agent shows the Case of the answer at every showing by `SendUserFile` with `display: render` on `raw/<date>/<hi HHMM>/cases/case-<N>.md`, N the id of the top-level Case, the file the `SubagentStop` hook of `rule-case-check` writes from the answer; in the same reply, under the heading of each Case and sub-case, it writes a short text in Russian on what the Case changes and the `ratification` section as the answer holds it, never its `given`, `when`, `then` or `tasks`, then its own text after one horizontal rule; a reply that the `Stop` check of `rule-case-check` refuses is followed, before the person answers, by a reply that sends the file and shows the `ratification` as the answer holds it (case 452.4);'
  - old: A Case with sub-cases is shown in one reply — the parent's `context`, `problem`, `recommend`, then every sub-case whole
    new: A Case with sub-cases is shown in one reply — its file holds the parent's `context`, `problem`, `recommend`, then every sub-case whole, and the chat a short text under each heading
  change: a built Case is shown by the file the hook writes, sent by SendUserFile, with a short Russian text and its ratification in the chat; the headings, the tasks, a showing again and a Case with sub-cases follow (case 452.4)
- slug: estimate-case-protocol-shows-the-built-case
  set:
    status: pending
    method: by hand, the Cases of a session at its close, their context against the Agent calls and their showings against the SendUserFile calls of the transcript
  change: the Criterion replaced whole — the Case sent as the file the hook writes, a short Russian text and the ratification in the chat, nothing retyped (case 452.4)
- slug: rule-case-build
  replace:
  - old: the main agent shows it with its name, `context`, `problem` and `recommend` translated into Russian and the rest unchanged ([[rule-case-protocol]]), and the hooks of `rule-case-check` check it before the showing and compare the showing with it in all but that prose (case 441).
    new: the hook of `rule-case-check` checks it and writes it into a file of the session, which the main agent sends the person with a short Russian text ([[rule-case-protocol]]), and the `Stop` hook compares what the chat shows of it with the answer (cases 441, 452.4).
  - old: the main agent shows it to the person with that prose translated into Russian and the rest unchanged, and the person ratifies it.
    new: a hook writes your answer into a file that the main agent sends the person, who reads it in English, and the person ratifies it.
  change: the Case of case-guppi reaches the person as the file the hook writes, not translated in the chat (case 452.4)
- slug: insight-case-show-built-case-retyped-by-hand
  set:
    status: actioned
    addressed_by: decision-case-452.4
  change: 'actioned: the hook writes the stored answer into a file the main agent sends, and the chat holds only a short text and the ratification, which the Stop comparison guards (case 452.4)'
```

```tasks
- [x] update `rule-case-protocol` — `replace` pairs in `## Sections` and its table, `## Who builds a Case` and `## Splitting` of the Render
- [x] update `estimate-case-protocol-shows-the-built-case` — the Criterion replaced whole
- [x] update `rule-case-build` — one `replace` pair in the Purpose, one in the Render
- [x] update `insight-case-show-built-case-retyped-by-hand` — actioned
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [x] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-protocol-shows-the-built-case` — by hand in a later session
```

### Case 452.5 — The language of a built Case: English in the file, a short Russian text in the chat

> **given:**
> `rule-language` — its Purpose and its Render, the `## Language` section of `CLAUDE.md`
> **＋** `estimate-language-followed` — the promise of the language of the repository and the chat
> **＋** `rule-case-protocol` — its Render `vault/wiki/case-schema.md`, the `## Language` section on the chat
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec, in English
> **＋** `raw/<date>/<hi HHMM>/cases/case-<N>.md` — the file that holds a built Case in English

> **when:**
> A session starts with `CLAUDE.md`, and the agent writes into the repository or into the chat.

> **then:**
> Everything written into the repository — code, identifiers, comments, pages, commit messages, documents, the approved Spec in `raw/<date>/<hi HHMM>/spec.md` — is English.
> **＋** The chat with the owner is Russian: the short text on each Case and sub-case that goes with its file, the name in its heading, a round of questions of `case-guppi` translated from the answer, and the agent's own text.
> **＋** A Case built by `case-guppi` is English whole — its name, `context`, `problem`, `recommend`, `given`, `when`, `then`, `tasks` and `ratification` — in `raw/<date>/<hi HHMM>/cases/case-<N>.md`, and its name, `context` and `problem` are English in `raw/<date>/<hi HHMM>/spec.md`.
> **＋** The ledger lines of a Case's `ratification` stand in the chat in English as the file holds them, and its `given`, `when`, `then` and `tasks` enter `raw/<date>/<hi HHMM>/spec.md` unchanged.
> **＋** Slugs, field names, ledger lines, paths and quotations from pages stay as they are in either language; English technical terms are not transliterated into Cyrillic.
> **－** A short-form Case of `vault/wiki/case-schema.md` is not Russian in the chat: it stands there in English, as `raw/<date>/<hi HHMM>/spec.md` holds it.
> **－** The rule speaks of the language, not of the Case form: the form is `vault/wiki/case-schema.md`.

```then
update:
- slug: rule-language
  set:
    purpose: Keeps the repository in English and the chat with the owner in Russian, a built Case English whole in the file sent to the person, with slugs, paths and quotations unchanged in either
  replace:
  - old: A Case is discussed in Russian, its `given`, `when`, `then` and `tasks` written in English in the chat (cases 123, 387.1);
    new: A Case is discussed in Russian and read in English, whole, in the file the agent sends the person (cases 123, 387.1, 452.5);
  - old: 'Russian for chat with the owner: the name of a Case, its `context`, `problem` and `recommend` are Russian in the chat, and its name, `context` and `problem` are English in the Spec; its `given`, `when`, `then` and `tasks` are English in the chat, the words that enter the Spec and the vault unchanged;'
    new: Russian for chat with the owner; a Case is English whole — its name, `context`, `problem` and `recommend` too — in the file the agent sends the person and in the Spec, and the chat holds a short Russian text on each Case and sub-case, its ledger lines in English as the file holds them;
  change: a built Case is English whole in the file sent to the person; the chat holds a short Russian text and the ledger lines (case 452.5)
- slug: estimate-language-followed
  set:
    status: pending
  change: the Criterion replaced whole — a built Case English whole in its file, a short Russian text in the chat (case 452.5)
- slug: rule-case-protocol
  replace:
  - old: Russian in the chat with the owner for the name of a Case it built, its `context`, `problem` and `recommend` — the main agent translates them from the answer — a round of questions of `case-guppi`, translated the same way, and the agent's own text; `given`, `when`, `then`, `tasks` — lines and sub-points — and `ratification` stand in the chat as the answer holds them, the words the vault will hold (cases 387.1, 441).
    new: A Case it built reaches the person whole in English, in the file `raw/<date>/<hi HHMM>/cases/case-<N>.md` that the agent sends (case 452.4). Russian in the chat with the owner for the short text on each Case and sub-case that goes with the file, the name in its heading, a round of questions of `case-guppi`, translated from the answer, and the agent's own text; the ledger lines of `ratification` stand in the chat as the answer holds them, the words the vault will hold (cases 387.1, 441, 452.5).
  change: the chat holds a short Russian text and the ledger lines of a built Case; the Case is English whole in its file (case 452.5)
```

```tasks
- [x] update `rule-language` — one `replace` pair in the Purpose, one in the Render, and the `purpose` field
- [x] update `estimate-language-followed` — the Criterion replaced whole
- [x] update `rule-case-protocol` — one `replace` pair in the `## Language` section of the Render
- [x] `uv run guppi render`: `CLAUDE.md`
- [x] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-language-followed` — by hand in a later session
```

## Case 453 — The guard refuses the agent's edit of the file of a built Case

> **context:**
> Case 452.1 has the `SubagentStop` hook `guppi casecheck --subagent` write each passed answer of `case-guppi` into a file under `raw/<date>/<hi HHMM>/cases/`. The main agent sends that file to the person. No hook stops the main agent from writing or editing that file with `Edit`, `Write` or `MultiEdit`. So the person could read a text that differs from the stored answer, sign it, and then get the stored answer in the Spec. The context of Case 452 named this as not done.
> `guppi ratified --guard` of `rule-spec-reconcile` already runs on `PreToolUse` of those tools. It refuses the agent's edit of the plan file and of the store `<plan>.checked.json`, which only hooks write. The person decided that the same guard refuses every edit of any file under the `cases/` folder of a session folder. The guard judges the path by one function of `guppi/casecheck.py`, which the writer of Case 452.1 also uses, as `rule-one-judgment-one-implementation` requires. So this Case is built after 452.1. `.claude/settings.json` and `rule-hook-registry` do not change, because the hook is already registered on these tools. The governed-files hook was not chosen: it matches only the fixed paths that `governs` names.
> This Case creates no page, so no vault query was run. In the frame, the line of `estimate-spec-reconcile-refuses-an-edit-of-the-plan` that leaves every file outside `.claude/plans/` unjudged becomes false, so its Criterion is replaced whole. `estimate-case-check-sends-back-a-faulty-case` speaks of the writer of the file, not of an edit by the agent, so it stays. `estimate-governed-files-hook-refuses` speaks of governed paths, so it stays. The sentence of `vault/wiki/case-schema.md` on the hook that refuses an edit of the plan stays true.
> Not done: a write through a shell still passes. `guppi bashguard` refuses only a heredoc that writes into a file, so an `echo` redirect in Bash or a `Set-Content` in PowerShell into `cases/` is not refused.

> **problem:**
> The main agent can write or edit the file of a built Case that the person reads and signs. Then the text the person ratified can differ from the stored answer that the Spec hook writes. Which guard refuses that edit, and on which paths?

> **given:**
> `rule-spec-reconcile` — the rule of the guard, its Purpose and `How it works`
> **＋** `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — the promise of the guard, whose Criterion this Case replaces whole
> **＋** `guppi/ratified.py` — `guard_refusal` and `guard`, the `PreToolUse` hook
> **＋** `guppi/casecheck.py` — the one predicate on a path under a `cases/` folder, next to the writer of the file
> **＋** `guppi/ledger.py` — the one judgment of a plan file, and `plan_path`
> **＋** `tests/test_ratified.py` — the tests of the guard
> **＋** `rule-case-check` — its `SubagentStop` hook, which writes the file of a built Case
> **＋** `.claude/plans/` — the folder of the plan file and its store
> **＋** `vault/raw/<date>/<HHMM>/cases/` — the folder of the files of built Cases

> **when:**
> The agent calls `Edit`, `Write` or `MultiEdit` on a file, and `uv run guppi ratified --guard` on `PreToolUse` reads the path and the content of the call.

> **then:**
> The hook refuses every `Edit` and `MultiEdit` of a plan file, and every `Write` of a plan file that exists: exit 2 with the reason on stderr, which Claude Code shows the agent, and the call does not run.
> **＋** A `Write` of a plan file that does not exist is let through when its content, trimmed, is one line that opens with `# `; a `Write` with any other content is refused the same way.
> **＋** Every `Edit`, `Write` or `MultiEdit` of a store `<plan>.checked.json` is refused the same way.
> **＋** Every `Edit`, `Write` or `MultiEdit` of a file under the `cases/` folder of a session folder `vault/raw/<date>/<HHMM>/`, whatever its name and whether it exists or not, is refused the same way; the reason names the file and says that the hook of `rule-case-check` alone writes it.
> **＋** A file under that folder is judged by one function of `guppi/casecheck.py`, which the writer of the file uses too; a plan file is a `.md` file under `.claude/plans/`, judged by one function of `guppi/ledger.py` that `plan_path` uses too.
> **＋** A refusal writes one line of the refusal to the day's event log and no `tool` line, so `plan_path` of `guppi/ledger.py` still names the plan file.
> **－** An edit of a file outside `.claude/plans/` and outside the `cases/` folder of a session folder is not judged by this hook, and the `SubagentStop` hook of `rule-case-check` writes the file with no tool call, which this hook does not judge.
> **－** A payload the hook cannot read: exit 0 with one line on stderr.
> **－** No `PostToolUse` hook compares an edit of the plan: `uv run guppi ratified --edit` and the marks `<plan>.waiting.json` are gone.

```then
update:
- slug: rule-spec-reconcile
  replace:
  - old: The agent writes only the title line that creates the plan, and a hook refuses any other edit of it before it lands;
    new: The agent writes only the title line that creates the plan, and a hook refuses any other edit of it, and any edit of the file of a built Case that the person is sent, before it lands (case 453);
  - old: 'The hook refuses every `Edit` and `MultiEdit` of a plan file or a store, every `Write` of a store, and every `Write` of a plan file that exists:'
    new: 'The hook refuses every `Edit` and `MultiEdit` of a plan file or a store, every `Write` of a store, every `Write` of a plan file that exists, and every `Edit`, `Write` and `MultiEdit` of a file under the `cases/` folder of a session folder under `vault/raw/` — the file of a built Case that the `SubagentStop` hook of `rule-case-check` writes from the stored answer, judged by one function of `guppi/casecheck.py` that its writer uses too (case 453):'
  - old: The hooks of `rule-spec-write` and `rule-case-check` write the plan and the store with no tool call, and this hook does not judge them.
    new: The hooks of `rule-spec-write` and `rule-case-check` write the plan, the store and the files of `cases/` with no tool call, and this hook does not judge them; a write through a shell is not judged here (case 453).
  set:
    implementation_ref:
    - guppi/ratified.py
    - guppi/ledger.py
    - guppi/casecheck.py
    - tests/test_ratified.py
    - .claude/settings.json
  change: the guard also refuses the agent's edit of a file under the cases/ folder of a session folder, judged by one function of guppi/casecheck.py (case 453)
- slug: estimate-spec-reconcile-refuses-an-edit-of-the-plan
  set:
    status: pending
    purpose: An edit by the agent of the plan file, its store or a file of a built Case under cases/ is refused, the one Write that creates the plan with its title line excepted
    method: uv run pytest tests/test_ratified.py -k guard; by hand, one probe Write of a file under cases/ in a later session, refused and in the event log
  change: the Criterion replaced whole — a file under the cases/ folder of a session folder refused like the store (case 453)
```

```tasks
- [x] update `rule-spec-reconcile` — one `replace` pair in the Purpose, two in `How it works`, and `implementation_ref` set
- [x] update `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — the Criterion replaced whole
- [x] `guppi/casecheck.py` — one predicate: a path under the `cases/` folder of a session folder under `vault/raw/`; the path function of the writer of Case 452.1 stays inside it
- [x] `guppi/ratified.py` — `guard_refusal` refuses every `Edit`, `Write` and `MultiEdit` of a path the predicate of `guppi/casecheck.py` names, with its reason; the docstrings of the module, `guard_refusal` and `guard`
- [x] `tests/test_ratified.py` — an `Edit`, a `MultiEdit`, a `Write` of a new file and of an existing file under `cases/` refused and logged; a file of another name under `cases/` refused; a `cases/` folder outside a session folder let through
- [x] read `estimate-spec-reconcile-refuses-an-edit-of-the-plan` — `uv run pytest tests/test_ratified.py -k guard` and one probe by hand in a later session
```

## Deferred

## Case 454 — the method of `estimate-claude-md-rendered` against a test file of `estimate-language-spec-prose-in-english`

> **context:**
> `make lint` reports a contradiction: the `method` of `estimate-claude-md-rendered` says the reading is by hand, while `estimate-language-spec-prose-in-english`, an Estimate of `rule-language`, whose Render sits in `CLAUDE.md`, names a test file.

> **problem:**
> Whether the method of `estimate-claude-md-rendered` changes, or the lint finding is wrong. The person defers it to a later session.

```then
defer:
- slug: rule-claude-md
  type: rule
  purpose: The method of estimate-claude-md-rendered says by hand while estimate-language-spec-prose-in-english names a test file; lint reports the pair as a contradiction
```

## Case 455 — two copies of one section reader

> **context:**
> `materialize.case_text` and `ratified.quoted_sections` both read the sections of a Case, and both judge fences by the same functions. The handoff of session 2300 named them as two copies of one judgment.

> **problem:**
> `CLAUDE.md` calls a second copy of one judgment a defect. Which module keeps the reader, and which imports it. The person defers it to a later session.

```then
defer:
- slug: rule-one-judgment-one-implementation
  type: rule
  purpose: materialize.case_text and ratified.quoted_sections are two copies of one section reader of a Case
```

## Case 456 — a `read` box of a deleted Estimate stays unticked

> **context:**
> Case 445.4 deleted `estimate-prespec-checks-the-ratified-copy`. Its `read` box in `archive/migration/2026-09-26/1745/raw/spec.md` line 413 stays unticked, because no reading of a deleted page will stand in the ledger, and Retro counts it as debt.

> **problem:**
> Whether `generate` ticks or drops the `read` line of an Estimate a `delete` removes, or the box is left as it stands. The person defers it to a later session.

```then
defer:
- slug: rule-page-generation
  type: rule
  purpose: A read box of an Estimate that a delete removed stays unticked in its Spec, since no reading of it will stand in the ledger
```
