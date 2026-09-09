---
name: hi
description: Open a working session — sprint, brief, git state, open issues, then the Frontier.
disable-model-invocation: true
---
<!-- rule-skill-hi -->
Recorded: !`uv run guppi event hi --session "${CLAUDE_SESSION_ID:-}"`
Probe: !`echo "${CLAUDE_SESSION_ID:-unset}"`

<!-- rule-internal-context -->
@vault/wiki/sprint.md
@vault/wiki/brief.md
<!-- /rule-internal-context -->

<!-- rule-git-context -->
Pull: !`git pull --ff-only 2>&1 || true`
Branch: !`git branch --show-current`
Status: !`git status --short`
<!-- /rule-git-context -->

<!-- rule-github-issues -->
Open issues: !`gh issue list --limit 5 2>&1 || true`
<!-- /rule-github-issues -->

Assemble the Frontier from the above and present it as a list: tasks, problems, debt
carried over, where the sprint stands; on a plan branch the unfinished plan comes first.
A failed pull or an unavailable `gh` is an item on that list, not a reason to stop. Wait
for the human to pick the order or defer items. Before any `create`, ask the vault first
(§3 of `vault/wiki/index.md`).
<!-- /rule-skill-hi -->
