---
type: rule
kind: MOC
purpose: Prevents a session from being loaded piecemeal by read-tool calls
status: draft
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: full
parent: "[[rule-session-start]]"
children: ["[[rule-internal-context]]", "[[rule-git-context]]", "[[rule-ledger-tail]]"]
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, harness]
core: true
---

## Purpose

Prevents a session from being loaded piecemeal by read-tool calls. Bash substitutions in a
skill body resolve before the agent's first turn, so the context is simply present — there
is no step the agent can forget or reorder. The `hi` mark in the event log is left by the `UserPromptSubmit` hook `guppi event prompt` of `rule-event-log`, which sees the session id; the skill's own `!` substitution could not. A command typed by the person does not pass through the `Skill` tool, so no `PreToolUse` hook sees it. It puts `brief` and `sprint` into the context before the first turn.

## Render

<!-- rule-skill-hi -->
---
name: hi
description: Open a working session — sprint, brief, git state, then the Frontier.
disable-model-invocation: true
allowed-tools: Bash(uv run guppi render --sync), Bash(git branch --show-current), Bash(git status --short), Bash(uv run guppi tail)
---
<!-- rule-internal-context -->
<!-- rule-git-context -->
<!-- rule-ledger-tail -->


When the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, start `/sprint-open` first, as the hook on `/hi` says: the opening Case comes before the Frontier; before the reply that acknowledges it, assemble and write the Frontier below and take its readings, and that reply shows it and puts the questions of its `A` lines, as `vault/wiki/orchestration.md` sets that reply. Assemble the Frontier from the above in three lists, the kind of each item by its source and no page opened. `## Cases`, what needs a decision: first, when the first line of the `Cases` of the brief's Next session opens with `open the next sprint`, that line, closed `[x] … · case N` by the opening Case, as `rule-sprint-close` sets it; then, on a plan branch, the unfinished plan, and each conserved Spec `backlog.md` names, one line each with the source `backlog` — but none while that opening line stands: the session that opens a sprint takes no conserved Spec, which waits in `backlog.md` for the next session; the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed; while that opening line stands, no item of `sprint.md`, which shows the new sprint only after the librarian's run, but the items of the first milestone that the `create` of `entity-sprint-<id>` writes under `## Milestones` in the case file `raw/<date>/<hi HHMM>/cases/case-<N>.md` of the opening Case, each with the source `sprint`; the `Cases` list of the brief's Next session, but for a line that names the same item as a line of the current milestone, which makes no line of its own: the milestone line stands as the sprint page gives it, with the source `sprint` alone, and the agent judges the sameness by meaning from the sprint page and the brief in its context, no page opened; a hand edit shown by `Render:`; a `failed` reading or a lesson of the Tail; an item the person adds. `## Work`, what needs none: the `Work` list of the brief's Next session; a dirty tree in `Status:`. `## Ask`, what only the person can answer: the `Ask the person` list of the brief's Next session, one line per reading with its question. The other items of `backlog.md` are no lines of their own: `## Cases` ends with the line `Backlog: N items`, N the items `backlog.md` counts, and under a Cases line an indented line `- near` names, by slug in a code span, each backlog item whose `purpose` is near that line in meaning — the agent's own judgment from `backlog.md` in its context, no `ask-guppi`; an item the person brings onto the Frontier is a Cases line of its own, source `backlog`, its title opening with its slug in a code span, so that `guppi backlog` counts it. In the chat the Cases are the agenda of Plan Mode, shown as a checklist: each line as `frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, its detail on an indented line under it and the `- near` line under that, the line `Backlog: N items` last; no Case stands as a bold line or with its detail as a paragraph; the Work is one block; sub-cases are cut in Cases only;
the hand edit is what `guppi render --sync` printed at session start or on the `Render:` line above.
A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian. Write the same three lists, under `## Cases`, `## Work` and `## Ask`, to `vault/raw/<date>/<hi HHMM>/frontier.md` — the session's folder, `HHMM` from the `hi:` line the `UserPromptSubmit` hook put in context — one line per item:
`- [ ] C<n> — <title> · <source>` under `## Cases`, `- [ ] W<n> — <title> · <source>` under `## Work`, `` - [ ] A<n> — `<slug>` — <question> · brief `` under `## Ask`. An item of the sprint's milestone is a line of its own whose title opens with the slug of each page it names, each in a code span — ``- [ ] C1 — `rule-x`, <milestone> · sprint``. Close a line when its item ends, the closer appended and the source kept — `- [x] C2 — <title> · sprint · case 315`. `[x]` is an item ended: `[x] … · case N` when ratified, `[x] … · work` when it needs no decision. `[-]` is an item put off: `[-] … · sprint · defer` when the item is a line of the sprint page left for a later session — no Case, no ledger line, no `deferred_by`, but for the short Case of a take-back that `orchestration.md` sets, never `· defer case N`; `[-] … · backlog · kept` when an item of `backlog.md` is left as it stands — no Case, no ledger line, but for the short Case of a take-back that `orchestration.md` sets, it stays in the backlog; `[-] … · defer case N` when a decision of any other source is put off — a short-form Case and its ledger line, and its target enters `backlog.md` through `deferred_by`, or a Case of the conserved Spec the session takes, as below; an item the person adds is a new Cases line; a `W` that turns out to need a decision closes `· case N`, a `C` that needs none closes `· work`. `/pre-spec` fails on an open line under `## Cases`, not on one under `## Work` or `## Ask`; a `W` or an `A` line closes `· work` when its work is done, where it is done: at `/hi`, in Work Mode or at Retro. Claude Code's plan mode does not stop this: the agent writes `frontier.md` and closes its lines while plan mode is on — a working file of the session, which `rule-permissions` allows. Before the question on the order, in the same reply, take each reading of an open `W` line whose whole method runs now, from files and commands alone: the brief, `git log`, `git status`, and the files and the commands the method names; read no transcript of an earlier session. The Frontier is still assembled with no page opened; this step opens the page of the Estimate of each open `W` line, judges from it whether its reading runs now, and judges each reading it takes against its `## Criterion`. Close those lines `[x] … · work` in `frontier.md` first, then write the reading lines in a `LEDGER` block of the reply, which ends in text. An open `W` line whose reading cannot run now stays open under `## Work` and makes no line under `## Cases`: a `W` line of an Estimate whose `method` names the session that closes a sprint, or the session after that close, waits for that session; one of an Estimate whose `target` is the live sprint page `entity-sprint-<id>` waits for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, as `rule-retro` sets it; and `handoff.md` names any other, which the librarian's brief puts to the next session as a line that proposes to defer it into the backlog, as `rule-brief` sets it. Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. An `A` line whose question names the session that closes a sprint, or the session after that close, stays open under `## Ask` and is not put to the person: it is put at the `/hi` whose brief opens the `Cases` of its Next session with `open the next sprint`, or in the session the person names as the one that closes the sprint; judge this from the line as the brief gives it, no page opened. When the person answers one, close its line `[x] … · work` in `frontier.md` first, then write its reading line in a `LEDGER` block of the reply, which ends in text, the answer as its result. Wait for the human to pick the order or defer items. Every Case is built by `case-guppi` (`rule-case-build`). A conserved Spec on `## Cases` is taken whole and run by `/box`, as `rule-spec-box` sets it: take it only while the session's ledger holds no decision line other than a `defer`, and ratify no Case after it but a short-form defer; close its line `[x] … · work`; create the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path `backlog.md` names; close the other open lines under `## Cases` as left — a line whose target a `defer` item of that Spec puts off closes `[-] … · defer case N`, N being the Case of that Spec that holds the item, with no short-form Case and no ledger line of this session — and go on to `/pre-spec`.
<!-- /rule-skill-hi -->

## How it works

Rendered in full into the skill file; the three children splice into the markers below, in
the order they are listed. Editing the skill directly is meaningless once the renderer
exists (Slice 2) — the next render overwrites it. Until then the file and this page are two
copies of one text, kept identical by hand.

`disable-model-invocation: true` in the frontmatter: only the person opens a working session, and only in plan mode: the hook of `rule-event-log` refuses a `/hi` whose `permission_mode` is not `plan`, missing or empty included, writes no `hi` line, and Claude Code blocks the prompt. `defaultMode: plan` in `.claude/settings.json` does not hold when the mode changes before `/hi`; a session begun outside plan mode once wrote its plan file under a second name. A session repaired without `/hi` stays possible: it holds no Case. `allowed-tools` names the four `!` commands of the skill: since client 2.1.282 the Bash check is server-side and a `!` substitution the person types gets no verdict ("The server-side auto mode classifier gave no verdict for Bash: the request that produced this action did not ask for one", session 1b191eaf, 2026-09-26), so a command no rule allows is refused and `/hi` does not open; a matching rule needs no classifier. The skill writes no event line of its own: a `!` substitution never saw `CLAUDE_SESSION_ID` (every `hi` of sessions A–M carried `--------`), so the `hi` line is written by the `UserPromptSubmit` hook of `rule-event-log`, which reads the session id from its payload.

## History

- 2026-10-14 shipped with GUPPI
