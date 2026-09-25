---
name: hi
description: Open a working session — sprint, brief, git state, open issues, then the Frontier.
disable-model-invocation: true
---
<!-- rule-internal-context -->
@vault/wiki/sprint.md
@vault/wiki/brief.md
@vault/wiki/case-schema.md
@vault/wiki/glossary.md
<!-- /rule-internal-context -->

<!-- rule-git-context -->
Pull: !`git pull --ff-only 2>&1 || true`
Render: !`uv run guppi render --sync`
Branch: !`git branch --show-current`
Status: !`git status --short`
<!-- /rule-git-context -->

<!-- rule-github-issues -->
Open issues: !`gh issue list --limit 5 2>&1 || true`
<!-- /rule-github-issues -->

<!-- rule-ledger-tail -->
Tail: !`uv run guppi tail`
<!-- /rule-ledger-tail -->


Assemble the Frontier from the above in two lists, the kind of each item by its source and no page opened (case 268.2). `## Cases`, what needs a decision: on a plan branch the unfinished plan, first; the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3); the `Cases` list of the brief's Next session; the brief's Deferred list; a hand edit shown by `Render:`; a `failed` reading or a lesson of the Tail; an item the person adds. `## Work`, what needs none: the `Work` list of the brief's Next session; a dirty tree in `Status:`. In the chat the Cases are the agenda of Plan Mode, one line each with its detail; the Work is one block; sub-cases are cut in Cases only;
the hand edit is what `guppi render --sync` printed at session start or on the `Render:` line above.
A failed pull or an unavailable `gh` is a Cases item when `sprint.md` names no decision on it, and not an item when it does; neither is a reason to stop. A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian. Write the same two lists, under `## Cases` and `## Work`, to `vault/raw/<date>/<hi HHMM>/frontier.md` — the session's folder, `HHMM` from the `hi:` line the `UserPromptSubmit` hook put in context (cases 73, 125) — one line per item:
`- [ ] C<n> — <title> · <source>` under `## Cases`, `- [ ] W<n> — <title> · <source>` under `## Work`. An item of the sprint's milestone is a line of its own whose title opens with the slug of each page it names, each in a code span — ``- [ ] C1 — `rule-x`, <milestone> · sprint`` — so that `generate` counts it (case 354.3). Close a line when its item ends, the closer appended and the source kept — `- [x] C2 — <title> · sprint · case 315` (case 314.1): `[x] … · case N`
when ratified, `[x] … · work` when it needs no decision, `[-] … · defer case N` when
deferred, `[-] … · sprint` when the item is a line of the sprint page left for a later session — no decision, no `deferred_by` (case 310.5), never `· defer case N` (case 356.2); `[-] … · deferred · kept` when an item of the brief's Deferred list, source `deferred`, is left deferred as it stands — no Case, no ledger line, the brief carries it on (case 421.4); an item the person adds is a new Cases line; a `W` that turns out to need a decision closes `· case N`, a `C` that needs none closes `· work`. `/pre-spec` fails on an open line under `## Cases`; a `W` line closes `· work` when its work is done, in Work Mode (case 356.1). Claude Code's plan mode does not stop this: the agent writes `frontier.md` and closes its lines while plan mode is on — a working file of the session (`rule-permissions`, case 363). Wait
for the human to pick the order or defer items. Every Case is built by `case-guppi` (`rule-case-build`).
