---
type: decision
case: "287"
status: current
create: ["[[rule-compact-recall]]", "[[estimate-compact-recall-reloads]]"]
update: ["[[rule-session-start]]", "[[rule-hook-registry]]"]
origin: raw/2026-09-21/0019/ledger.md#case-287
sprint: migration
created: 2026-09-21
tags: [session, hooks, harness, workflow, render]
---

## Context

`/hi` brings `sprint.md`, `brief.md`, `case-schema.md` (and the glossary after C4.1) into the first turn through the `@` lines of the skill; `CLAUDE.md` lives in the system prompt. When the client compacts the context, `CLAUDE.md` is read again from disk, but the body of an invoked skill comes back capped at 5,000 tokens — after a compaction the Case schema, the Frontier and the Spec stand in the context only as far as the summary kept them. Two hooks run on `SessionStart`, both without a matcher: `guppi event session-start` (writes `session-start compact`; the `hi` window survives, case 14) and `guppi render --sync`. Nothing brings the session's load back. A hook's stdout over 10,000 characters is saved to a file, so the hook prints paths and the Frontier, not the texts.
The vault: no page on compaction, `rule-compact-recall` free; the nearest is `rule-internal-context` (`built`), whose `estimate-internal-context-loaded` measures the first turn after `/hi`, not a compaction — not touched; `rule-session-start` (`built`, MOC) takes a fourth child, its `estimate-session-start-context` not touched; `rule-hook-registry` (`built`) — the registration, `estimate-hook-registry-rendered` measures the file against the page, its Criterion unchanged.

## Problem

After a compaction a working session goes on in Plan Mode or Work Mode without the Case schema, without the Frontier and without the exact text of the Spec — the agent works from a summary. A hook is needed that, after `compact`, brings back into the context what `/hi` brought at the start.

## History

- 2026-09-21 created · raw/2026-09-21/0019/ledger.md#case-287
