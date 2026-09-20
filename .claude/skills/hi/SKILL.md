---
name: hi
description: Open a working session — sprint, brief, git state, open issues, then the Frontier.
disable-model-invocation: true
---
<!-- rule-internal-context -->
@vault/wiki/sprint.md
@vault/wiki/brief.md
@vault/wiki/case-schema.md
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
`- [ ] C<n> — <title> · <source>` under `## Cases`, `- [ ] W<n> — <title> · <source>` under `## Work`. Close a line when its item ends: `[x] … · case N`
when ratified, `[x] … · work` when it needs no decision, `[-] … · defer case N` when
deferred; an item the person adds is a new Cases line; a `W` that turns out to need a decision closes `· case N`, a `C` that needs none closes `· work`. `/pre-spec` fails on an open line. Wait
for the human to pick the order or defer items. Before any `create`, ask the vault first
(§3 of `vault/wiki/index.md`).
