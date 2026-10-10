---
type: decision
case: "439"
status: archived
update: ["[[rule-skill-hi]]"]
origin: raw/2026-09-26/1745/ledger.md#case-439
sprint: migration
created: 2026-09-26
tags: [session, harness]
---

## Context

`/hi` runs six `!` substitutions before the first turn of the agent, and their output is in the context with no read calls. Since client 2.1.282 in VS Code, the server-side classifier of auto mode checks each substitution. It gives no verdict for a substitution the person typed. The full reason was printed once, in session 1b191eaf: "the request that produced this action did not ask for one". So `/hi` failed at every run, and a fresh `/login` did not help. Commit 54509ed was made with the owner's consent but with no Case. It added an `allowed-tools` line with the six commands to the frontmatter of the Render of `rule-skill-hi`, and one sentence on the cause to `## How it works`. `uv run guppi render` rewrote `.claude/skills/hi/SKILL.md`. `render --check` exited 0, pytest passed, the lint output did not change, and after that `/hi` in this session ran whole. The change has no History line and no Decision.
An `update` that has only `change` applies: `ITEM_KEYS["update"]` of `guppi/materialize.py` holds `change`, and `guppi/generate.py`, which imports it, writes the History line `updated: <change>` with a link to `decision-case-439`. A `replace` pair would fail here, because its `old` is no longer on the page. `sections` would rewrite whole sections for one line.
The other pages and why they stay as they are:
- The Pattern of `insight-hi-skill-substitution-checked-by-a-model-call` names a lapsed login as the cause. Its Proposal says "not an allow entry for the command", and the new cause refutes both. But that Proposal was rejected by Case 246. An Insight changes only by an `update` that actions or rejects it, and this Case makes none, so it stays as it is. The new cause goes into a lesson line in the ratification, and the librarian of the next run links it to this Insight.
- `rule-permissions` allows only the working files of the session in `.claude/settings.json`. The change does not touch its list. The `allowed-tools` of the skill holds only while `/hi` runs, and only the person opens `/hi` (`disable-model-invocation: true`). Two of the six commands write files — `git pull --ff-only` the working tree, `uv run guppi render --sync` the governed files — and the owner allowed them for `/hi`; the `SessionStart` hook runs the same `render --sync` with no permission check. The Criterion of `estimate-permissions` speaks only of the `allow` list in `settings.json`.
- The Criterion of `estimate-hi-no-read-calls` promises the context after `/hi` with no read calls. The change brings this behaviour back but does not change the promise. The Criterion of `estimate-hi-writes-frontier` speaks of the Frontier. No Estimate is touched.
- The Case has no `create`, so no vault query is needed.

## Problem

The change of `rule-skill-hi` and its Render already stand in the vault and in `.claude/skills/hi/SKILL.md`, but no Decision signed them. The question: ratify them after the fact as they stand, so that the History of the page gets a line with a link to the Decision.

## Given

`rule-skill-hi` — the rule whose Render frontmatter and `## How it works` carry the change
**＋** `.claude/skills/hi/SKILL.md` — the skill file rendered from `rule-skill-hi`
**＋** `rule-permissions` — the rule of the allow list in `.claude/settings.json`

## History

- 2026-09-26 created · raw/2026-09-26/1745/ledger.md#case-439
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
