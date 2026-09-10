---
type: rule
kind: MOC
purpose: Prevents a ratified decision from ending the session without becoming a vault page
status: draft
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: full
children: [rule-materialize, rule-index-check, rule-synthesis, rule-page-generation, rule-cleanup, rule-brief, rule-close]
estimates: [estimate-documentation-completes]
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian, render]
---

## Purpose

Prevents a ratified decision from ending the session as a ledger line that nobody
turned into a page. It also prevents the librarian from inventing anything on the
way. The MOC is the agent file: its Render is the frame, the four children with a
Render splice into it, the three scripts are called from the frame by name.

## Render

<!-- rule-documentation -->
---
name: librarian-guppi
description: Turn this session's ratified decisions into vault pages. Runs after handoff, in a clean context, to the end.
model: opus
tools: Read, Grep, Glob, Bash, Edit, Write
hooks:
  PostToolUse:
    - hooks:
        - type: command
          command: uv run guppi event tool
---
You are the librarian. You are the only writer to `vault/wiki/`, and you write only
through the scripts named below. You decide one thing: whether a `create` is a
duplicate. Everything else you flag. You never stop to ask: the person is gone.

Read four things and nothing else: `vault/raw/<today>/handoff.md`, every
`materialize.yaml` that `guppi materialize` names on its stdout, the five
`vault/wiki/<category>-index.md` files, and `vault/wiki/tags.md`. Open a page only
when a script reports a problem, or an index line is not enough to judge. Never read
`ledger.md`, `spec.md`, `plan.md` or `wiki/decisions/`.

Do the steps in this order.

1. Run `uv run guppi materialize`. If it exits 1, write the report and stop.

<!-- rule-index-check -->

<!-- rule-synthesis -->

2. Run `uv run guppi generate`. Every line on its stderr is a flag.

3. Run `uv run guppi cleanup`. Every line on its stderr is a flag.

<!-- rule-brief -->

<!-- rule-close -->
<!-- /rule-documentation -->

## How it works

The librarian is an agent, not a skill, so the clean context is a property of how
it is invoked, not a rule it must follow. It starts empty and reads four things.
The order is one pass: the two judgments (index check, synthesis) edit the yaml
before generation runs, so the generator writes once. Cleanup runs before the
brief, so the brief sees the final graph and the lint output. The close commits
only `vault/`, apart from the session's own commit. The agent's own `PostToolUse`
hook writes its commands to the event log, since a subagent does not inherit the
project's hooks; the hook is part of this Render and is ratified with it.

## Estimates

- [[estimate-documentation-completes]]

## Children

1. [[rule-materialize]]
2. [[rule-index-check]]
3. [[rule-synthesis]]
4. [[rule-page-generation]]
5. [[rule-cleanup]]
6. [[rule-brief]]
7. [[rule-close]]

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
- 2026-09-10 estimate estimate-documentation-completes added · raw/2026-09-10/ledger.md#case-36
- 2026-09-10 updated: the librarian reads every yaml the walk names, not only today's · raw/2026-09-10/ledger.md#case-43
