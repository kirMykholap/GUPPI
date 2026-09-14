---
name: hi
description: Open a working session — sprint, brief, git state, open issues, then the Frontier.
disable-model-invocation: true
---
<!-- rule-internal-context -->
@vault/wiki/sprint.md
@vault/wiki/brief.md
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


Assemble the Frontier from the above and present it as a list: tasks, problems, debt
carried over, where the sprint stands; on a plan branch the unfinished plan comes first;
what `guppi render --sync` printed at session start or on the `Render:` line above is an item when it shows a hand edit.
A failed pull or an unavailable `gh` is an item on that list, not a reason to stop. A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian. Write the same list to `vault/raw/<date>/<hi HHMM>/frontier.md` — the session's folder, `HHMM` from the `hi:` line the `UserPromptSubmit` hook put in context (cases 73, 125) — one line per item:
`- [ ] F<n> — <title> · <source>`. Close a line when its item ends: `[x] … · case N`
when ratified, `[x] … · work` when it needs no decision, `[-] … · defer case N` when
deferred; an item the person adds is a new line. `/pre-task` fails on an open line. Wait
for the human to pick the order or defer items. Before any `create`, ask the vault first
(§3 of `vault/wiki/index.md`).
