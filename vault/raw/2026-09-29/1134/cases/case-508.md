## Case 508 — Work readings get a trigger at `/hi` and in `/work`

> **context:**
> A reading checks one Estimate against what actually happens and writes the result into the ledger. At `/hi` each `pending` reading becomes a `W` line of the Frontier. Only `/retro` says "take the readings". By then some readings are blocked, because the ledger hook refuses a reading of an Estimate that the same session creates or updates (case 428.1). Other readings are tied to a moment that has already passed. For example, the `method` of `estimate-hi-no-read-calls` names "the /hi of the next session", and the `/hi` reply of this session did not take it; it was read later in the session. So the readings pile up: this session's Frontier opened with 89 reading lines under `## Work`. The librarian is a helper agent and writes no ledger line. Yet the `method` of 32 Estimates names the librarian, counted by a Grep of the `method` lines. The librarian lists these Estimates under Readings due of `vault/wiki/brief.md` with no result. It writes the brief before `guppi archive` and the commit, on purpose: the brief reads the yamls and Specs where they stand, and the librarian may not search `vault/archive/`.
>
> In the rounds the person decided the following:
> - `/hi` takes the readings whose `method` names `/hi` or the librarian's run, in its first reply, and closes their `W` lines there.
> - A reading whose `method` also names a later moment waits for that moment.
> - A reading whose `method` needs a `/hi` run of its own is not taken at `/hi`.
> - `/work` gets a step after the last task that takes every other reading it can, in Frontier order, and the person can stop it.
> - A `W` line that cannot be read stays open.
> - The librarian writes facts, not verdicts: what its run printed or left, on each such Estimate's Readings due line, and the output of `guppi archive` right after that step.
> - The commit reading is taken at the next `/hi` from `git log`, `git status` and the previous transcript.
> - Each behaviour gets a new Estimate.
>
> Frame found by `case-guppi`:
> - The Render of `rule-skill-hi` and the Criterion of `estimate-hi-writes-frontier` both say a `W` line closes "in Work Mode". Closing at `/hi` makes both false, so sub-case 508.2 changes both. A reading taken by `/retro` closes its line at Retro, so the new wording names all three places.
>
> Case 507 and why 508.2 supersedes it:
> - Case 507 of this session replaced the same Criterion whole: at `/hi` the chat shows the Cases as the checklist of `frontier.md`, the detail on an indented line, never as a bold line with a paragraph. The person chose that look from four, and kept `rule-orchestration` out of it.
> - Two whole replacements of one Criterion would sign it twice. So 508.2 supersedes 507 and carries both of its changes: 507's pair on `rule-skill-hi` for the chat look, and its own pair for closing a `W` line.
> - The one Criterion of 508.2 is 507's with two changes. The chat look is described on its own and no longer called the form of the acknowledging reply, since that form folds closed lines and shows no detail line. The `W` closing line is changed.
> - 507 leaves the Spec.
> - Against the Criterion on the page today, two lines are not carried: the old chat line and the old `W` closing line.
>
> Other frame facts:
> - The Render of `rule-skill-hi` assembles the Frontier with "no page opened". That stays: only the new reading step opens the pages of the Estimates it reads.
> - The `W` lines are closed in `frontier.md` before the reply that carries the `LEDGER` block, since that reply ends in text with no tool call after it.
>
> Why some `then` lines look alike:
> - The reading steps of 508.1 at `/hi` and 508.3 in `/work` use similar words on purpose. They are one kind of step at two moments, each with its own promise, and each can fail apart from the other.
> - The line of 508.3 that closes the `W` line before the `LEDGER` reply repeats the matching line of 508.1 on purpose, so that each Estimate reads whole without the other.
> - Some lines of 508.2 share words with 508.1 because both describe `frontier.md`.
>
> These Estimates stand, and why:
> - `estimate-hi-no-read-calls`: the reading calls come after the skill's output is already in context, so they are not calls "to get any of them".
> - `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`: it promises the tasks in order, and its `－` line about ticking no `read` box stays true.
> - `estimate-brief-written`: its Criterion promises the sections, their order and their sources. Each Readings due line keeps its three parts, the Estimate, its `draft` rule and where it is read, one line per Estimate. The facts added at the end of the line are promised by the new Estimate of 508.4.
> - `estimate-documentation-completes`: the librarian opens an Estimate page for "a fact for the brief", which its frame already lists, and the archive output still goes into the report.
>
> What does not change:
> - `rule-retro` keeps its reading paragraph and takes whatever is left.
> - The sentence of `rule-case-protocol`, "a `W` line closes when its work is done", names no phase and stays true.
>
> Vault query: every `create` is an Estimate with a `ref`, so no vault query was needed. A Glob found the three new slugs free.
>
> Timing: no hook changes. The skills are rendered at the librarian's run. `/hi` and `/work` act on the new text from the next session. The librarian of this session runs on the frame it loaded at dispatch, so the new brief facts first appear one run later.

> **problem:**
> A Work reading has no trigger before Retro. Readings tied to `/hi` or to the librarian's run pass without being taken, and the other readings pile up until some are blocked.

> **recommend:**
> Give each reading its moment:
> - `/hi` takes the readings of `/hi` and of the librarian's run, since nothing has changed yet at that point.
> - The librarian leaves the facts of its run in the brief for `/hi` to judge.
> - `/work` takes the rest after the Spec's code is built.
>
> Rejected: `/work` alone (it loses the `/hi` moment), a separate `/read` skill (it needs the person to remember), and the librarian judging its own run.

### Case 508.1 — `/hi` takes the readings of `/hi` and of the librarian's run

> **given:**
> `rule-skill-hi` — the page whose Render is the `/hi` skill and assembles the Frontier with no page opened
> **＋** `.claude/skills/hi/SKILL.md` — the skill file rendered from `rule-skill-hi`
> **＋** `estimate-hi-takes-its-readings` — the promise of the reading step at `/hi`
> **＋** `vault/wiki/brief.md` — loaded at `/hi`; its Readings due carry each `method` and the librarian's facts
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier, whose `W` lines are the readings
> **＋** `rule-ledger-write` — the hook that writes the reading lines of a `LEDGER` block
> **＋** `rule-case-protocol` — a reply that carries a `LEDGER` block ends in text, with no tool call after it

> **when:**
> The person types `/hi` on `UserPromptSubmit`, and the agent writes `raw/<date>/<hi HHMM>/frontier.md`, whose `## Work` holds the `pending` readings of `vault/wiki/brief.md`.

> **then:**
> In its first reply, before the question on the order, the agent takes each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian's run and whose whole method can be done at that moment.
> **＋** It reads what the method names from `vault/wiki/brief.md`, `git log`, `git status` and the commands of the method, and reads the librarian's report from the transcript of the previous session.
> **＋** It opens the page of each Estimate it reads and judges the reading against its `## Criterion`.
> **＋** It closes the `W` line of each reading taken as `[x] … · work` in `raw/<date>/<hi HHMM>/frontier.md`, then writes one `estimate[...]` line per reading in a `LEDGER` block of the reply, which ends in text.
> **－** The Frontier is still assembled with no page opened. Only the reading step opens the pages of the Estimates it reads.
> **－** A reading whose `method` also names a later moment is not taken at `/hi`. It is taken at that moment, and its `/hi` part is read then from the session's first turn.
> **－** A reading whose `method` asks for a `/hi` run of its own, such as one outside plan mode, is not taken at `/hi`.
> **－** At `/hi` the agent changes no page and no file except `raw/<date>/<hi HHMM>/frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi` — the reading step before the question on the order
>   - old: `Wait for the human to pick the order or defer items.`
>   - new: `` Before the question on the order, in the same reply, take each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian's run and whose whole method can be done now: from the brief, `git log`, `git status`, the commands the method names, and the transcript of the previous session for the librarian's report. The Frontier is still assembled with no page opened; this step opens the page of each Estimate it reads and judges the reading against its `## Criterion`. Close those lines `[x] … · work` in `frontier.md` first, then write the reading lines in a `LEDGER` block of the reply, which ends in text. A reading whose `method` also names a later moment waits for that moment, its `/hi` part read then from the session's first turn; a reading whose `method` asks for a `/hi` run of its own is not taken here (case 508.1). Wait for the human to pick the order or defer items. ``
>   - change: `/hi takes the readings of /hi and of the librarian's run in its first reply (case 508.1)`
> - [ ] create `estimate-hi-takes-its-readings` — the promise of the reading step at `/hi`
>   - type: `estimate`
>   - ref: `rule-skill-hi`
>   - kind: `QA`
>   - purpose: `Whether /hi takes, in its first reply, each open W reading whose method names /hi or the librarian's run and can be done whole then, closes its W line and writes its line, opens no page but the Estimates it reads, and leaves the readings that name a later moment or a /hi run of their own`
>   - method: `by hand at the first /hi after the render: the first reply, its tool calls, its LEDGER block and frontier.md read against the Criterion, recorded in the estimate line`
>   - tags: `[session, harness, workflow]`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-takes-its-readings` — by hand, at the first `/hi` of the next session

> **ratification:**
> ```
> - decision[case 508.1][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 508.1][create][estimate-hi-takes-its-readings]{ref:rule-skill-hi}{tags:session,harness,workflow}
> ```

### Case 508.2 — The Frontier at `/hi`: the Cases as a checklist, a `W` line closed where it is read

> **given:**
> `rule-skill-hi` — the page whose Render is the `/hi` skill; it says how the Frontier is shown in the chat and when a `W` line closes
> **＋** `.claude/skills/hi/SKILL.md` — the skill file rendered from `rule-skill-hi`
> **＋** `estimate-hi-writes-frontier` — the promise of the Frontier at `/hi`
> **＋** `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` — the sources of the Frontier
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the file of the Frontier

> **when:**
> The person invokes `/hi`. The agent assembles the Frontier from `vault/wiki/sprint.md`, `vault/wiki/brief.md`, `vault/wiki/backlog.md` and the output of the skill's commands, and closes its lines in Plan Mode.

> **then:**
> The Frontier is written to `raw/<date>/<hi HHMM>/frontier.md` in the lists `## Cases`, with lines `- [ ] C<n> — <title> · <source>`, and `## Work`, with lines `- [ ] W<n> — <title> · <source>`. The title of a line of the current milestone or of the backlog opens with the slug of each of its pages in a code span.
> **＋** The kind comes from the source. Cases: first, on a plan branch, the unfinished plan and each conserved Spec of `vault/wiki/backlog.md`, with the source `backlog`; then the items of the current milestone; the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the ledger's Tail; an item the person adds. Work: the `Work` list of the brief's Next session; a dirty tree by `git status`.
> **＋** The other items of the backlog are not lines. `## Cases` ends with the line `Backlog: N items`, where N is the count in `vault/wiki/backlog.md`. Under a Cases line, an indented line `- near` names by slug each backlog item whose `purpose` is near that line in meaning. The agent judges this from the loaded file, with no `ask-guppi`. An item the person brings onto the Frontier becomes a Cases line with the source `backlog`.
> **＋** A line closes by appending the closer and keeping the source. An item ended closes `[x] … · case N` when decided, or `[x] … · work` when done with no decision. A line of the sprint page left for a later session closes `[-] … · sprint · defer`. An item of the backlog left as it stands closes `[-] … · backlog · kept`. A decision of any other source put off closes `[-] … · defer case N`.
> **＋** An item closed `defer` or `kept` has no short Case and no ledger line. A sprint item never closes `· defer case N`.
> **＋** Only the current milestone gives items. A later milestone and Closed give none, and the sprint page's Backlog reaches the Frontier only through the backlog. A decision line of the Tail is not an item.
> **＋** In the chat the Cases are shown as a checklist. Each line stands as `raw/<date>/<hi HHMM>/frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, with its detail on an indented line under it and the `- near` line under that, and the line `Backlog: N items` comes last. The Work is shown as one block. Only Cases are cut into sub-cases. A `W` that turns out to need a decision closes `· case N`. A `C` that needs none closes `· work`.
> **－** At `/hi` no Case stands in the chat as a bold line, and no Case has its detail as a paragraph.
> **－** `Pull:` and `Open issues:` are a Cases item only when `vault/wiki/sprint.md` names no decision on them.
> **－** Pre-spec finds an open line under `## Cases`. A `W` line stands open until its work is done and closes `· work` where that work is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop the agent from writing `frontier.md`.

> **tasks:**
> - [ ] update `rule-skill-hi` — the Cases shown in the chat as a checklist; a `W` line closed where its work is done
>   - old: `In the chat the Cases are the agenda of Plan Mode, one line each with its detail; the Work is one block; sub-cases are cut in Cases only;`
>   - new: `` In the chat the Cases are the agenda of Plan Mode, shown as a checklist: each line as `frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, its detail on an indented line under it and the `- near` line under that, the line `Backlog: N items` last; no Case stands as a bold line or with its detail as a paragraph (case 508.2); the Work is one block; sub-cases are cut in Cases only; ``
>   - old: ``` `/pre-spec` fails on an open line under `## Cases`; a `W` line closes `· work` when its work is done, in Work Mode (case 356.1). ```
>   - new: ``` `/pre-spec` fails on an open line under `## Cases`; a `W` line closes `· work` when its work is done, where it is done: at `/hi`, in Work Mode or at Retro (cases 356.1, 508.2). ```
>   - change: `the Cases shown in the chat at /hi as a checklist, the detail on an indented line; a W line closes where its work is done, at /hi, in Work Mode or at Retro (case 508.2, supersedes 507)`
> - [ ] update `estimate-hi-writes-frontier` — the Criterion replaced whole: the Cases as a checklist, a `W` line closed where its work is done
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — the Cases shown in the chat at /hi as a checklist, no bold line; a W line closes where its work is done (case 508.2, supersedes 507)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-writes-frontier` — by hand, at the first `/hi` of the next session

> **ratification:**
> ```
> - decision[case 508.2][update][rule-skill-hi]{ref:rule-skill-hi}{supersedes:case 507}
> - decision[case 508.2][update][estimate-hi-writes-frontier]{ref:rule-skill-hi}{supersedes:case 507}
> ```

### Case 508.3 — `/work` takes the Work readings after the last task

> **given:**
> `rule-work-mode` — the page whose Render is the `/work` skill
> **＋** `.claude/skills/work/SKILL.md` — the skill file rendered from `rule-work-mode`
> **＋** `estimate-work-mode-takes-the-work-readings` — the promise of the reading step of `/work`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier, whose open `W` lines are the readings
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec whose tasks run first
> **＋** `rule-ledger-write` — refuses a reading of an Estimate the session creates or updates
> **＋** `rule-retro` — `/retro`, which follows and takes the readings left
> **＋** `rule-case-protocol` — a reply that carries a `LEDGER` block ends in text, with no tool call after it

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.

> **then:**
> Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
> **＋** A moment of an earlier session, such as the librarian's run, has come.
> **＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and a later reply, ending in text, carries its `estimate[...]` line inside a `LEDGER` block.
> **＋** The person can stop the step in the chat, and the lines not reached stay open.
> **－** A reading of an Estimate this session creates or updates is not taken, and its `W` line stays open.
> **－** A reading whose moment has not come is not taken, and its `W` line stays open.
> **－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

> **tasks:**
> - [ ] update `rule-work-mode` — the reading step after the last task
>   - old: `` Work Mode ends with `/retro`. ``
>   - new: `` When the last task is done, take the Work readings before `/retro`: in the order of `frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come; a moment of an earlier session, such as the librarian's run, has come. Leave a reading of an Estimate this session creates or updates, and one whose moment has not come: its line stays open. Close the line of each reading taken `[x] … · work` in `frontier.md` first, then write its `estimate[...]` line in a `LEDGER` block of a reply that ends in text; tick no `read` box. The person can stop the step in the chat, and the lines not reached stay open (case 508.3). Work Mode ends with `/retro`. ``
>   - change: `/work takes the open W readings after the last task, before /retro (case 508.3)`
> - [ ] create `estimate-work-mode-takes-the-work-readings` — the promise of the reading step of `/work`
>   - type: `estimate`
>   - ref: `rule-work-mode`
>   - kind: `QA`
>   - purpose: `Whether /work, after the last task and before /retro, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line and writes its line, and leaves open the readings this session changes or whose moment has not come`
>   - method: `by hand at the first /work after the render: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] read `estimate-work-mode-takes-the-work-readings` — by hand, at the first `/work` of a session after the render

> **ratification:**
> ```
> - decision[case 508.3][update][rule-work-mode]{ref:rule-work-mode}
> - decision[case 508.3][create][estimate-work-mode-takes-the-work-readings]{ref:rule-work-mode}{tags:session,workflow,harness}
> ```

### Case 508.4 — The librarian writes the facts of its run into the brief

> **given:**
> `rule-brief` — the page whose Render is the brief section of the librarian's frame; it adds no decision and no judgment of the work
> **＋** `rule-documentation` — the page whose Render is the librarian's frame, its reasons to open a page and its archive step
> **＋** `.claude/agents/librarian-guppi.md` — the agent file rendered from both
> **＋** `vault/wiki/brief.md` — the brief, whose Readings due carry the facts
> **＋** `estimate-brief-carries-the-run-facts` — the promise of the facts in the brief
> **＋** `rule-raw-archive` — `uv run guppi archive`, the step after the brief
> **＋** `rule-close` — the commit of the librarian's run, its last step
> **＋** `rule-case-protocol` — only the main agent writes ledger lines

> **when:**
> The librarian `librarian-guppi` writes `vault/wiki/brief.md` in its run, and then runs `uv run guppi archive`.

> **then:**
> For each `pending` Estimate whose `method` names the librarian's run, its line under Readings due of `vault/wiki/brief.md` ends with the facts that its `method` and `## Criterion` name, as the steps of the run before the brief printed or left them.
> **＋** After `uv run guppi archive`, the librarian adds its stdout lines at the end of the Readings due line of each `pending` Estimate whose `method` names the archive step, and the close of `rule-close` commits the brief with them.
> **＋** Each Estimate keeps one line under Readings due, with the Estimate, its `draft` rule and where it is read.
> **－** The line compares nothing and carries no passed or failed, and the librarian writes no ledger line.
> **－** The order of the steps does not change: the brief, then `uv run guppi archive`, then the close.
> **－** No line of the brief names the commit of the close.

> **tasks:**
> - [ ] update `rule-brief` — the facts of the run at the end of a Readings due line
>   - old: `` or, when there is none, from the page's `method` (case 200.3); ``
>   - new: `` or, when there is none, from the page's `method` (case 200.3); for an Estimate whose `method` names the librarian's run, at the end of its line the facts its `method` and `## Criterion` name, as the steps of this run before the brief printed or left them, with no comparison and no passed or failed (case 508.4); ``
>   - change: `a Readings due line of an Estimate read at the librarian's run ends with the facts of the run, no verdict (case 508.4)`
> - [ ] update `rule-documentation` — the archive output added to the brief
>   - old: `the units it moved and the units it kept, with the reason, go into the report.`
>   - new: `` the units it moved and the units it kept, with the reason, go into the report. Then add its stdout lines at the end of the Readings due line of each `pending` Estimate whose `method` names the archive step of the librarian's run, before the close commits the brief (case 508.4). ``
>   - change: `the stdout of guppi archive added to the brief for an Estimate that reads it (case 508.4)`
> - [ ] create `estimate-brief-carries-the-run-facts` — the promise of the facts in the brief
>   - type: `estimate`
>   - ref: `rule-brief`
>   - kind: `QA`
>   - purpose: `Whether the brief ends the Readings due line of each pending Estimate read at the librarian's run with the facts its method and Criterion name, the stdout of guppi archive included, with no comparison or verdict, one line per Estimate`
>   - method: `by hand at the /hi of the session after the first librarian run whose frame holds this Render: vault/wiki/brief.md read against the run's report in the previous transcript, recorded in the estimate line`
>   - tags: `[harness, workflow, librarian]`
> - [ ] `uv run guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-brief-carries-the-run-facts` — by hand, at the `/hi` after the first librarian run on the new frame

> **ratification:**
> ```
> - decision[case 508.4][update][rule-brief]{ref:rule-brief}
> - decision[case 508.4][update][rule-documentation]{ref:rule-documentation}
> - decision[case 508.4][create][estimate-brief-carries-the-run-facts]{ref:rule-brief}{tags:harness,workflow,librarian}
> ```
