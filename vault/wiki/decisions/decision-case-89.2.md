---
type: decision
case: "89.2"
status: current
update: ["[[rule-close]]", "[[estimate-close-commits]]"]
origin: raw/2026-09-12/ledger.md#case-89.2
sprint: migration
created: 2026-09-12
tags: [harness, workflow, git, librarian]
---

## Context

`guppi render` writes files only at a session start, from the `--sync` hook. The
librarian reaches the renderer through `make lint` alone, whose first step is
`render --check` — it reports and writes nothing. So its commit holds the pages without
the files they render into, `make lint` fails at step one on that commit, and the gap
closes only at the next `/hi`.

## Problem

The files should be written where the pages are made: the error then shows in the same
run and reaches the brief, and the librarian's commit stops contradicting itself. That
changes what the commit holds, and it makes the live clause of a reading that passed
today describe something that can no longer happen.

## Given

`rule-documentation` is the full Render of the librarian agent, its steps numbered: 1
`materialize`, index check, synthesis, 2 `generate`, 3 `cleanup`, then brief and close.
Its How it works says "The close commits only `vault/`, apart from the session's own
commit".
**＋** `rule-close` is a Leaf, `built`, `partial`; its Render says "Commit only paths
under `vault/` … never anything outside `vault/`", and its Estimate
`estimate-close-commits` (`passed`) asks for one commit "touching only vault/ paths".
**＋** The criterion of `estimate-documentation-completes` asks only that the commit be
separate from the session's; it holds no vault-only clause, so no prose of it is touched.
**＋** Every governed file lies under three paths beside the vault: `CLAUDE.md`,
`.claude/settings.json`, and the files under `.claude/agents/` and `.claude/skills/`. So
`git add vault CLAUDE.md .claude` covers them and sweeps nothing else.
**＋** `guppi cleanup` is the last step that changes which pages are live and where they
lie: it moves every `status: archived` page out of `vault/wiki/`, strips archived slugs
from `children` and `estimates`, and rewrites the indexes. `render_units` filters by
`enforcement`, never by `status`, so a render before cleanup would build a file from a
page this run archived, and a full page whose child was archived would splice the
archived text or fail on it. The render belongs after cleanup.
**＋** `run()` builds every output in memory through `plan()` and only then calls
`write_all`, so a `RenderError` leaves nothing written. A pre-flight `--check` would add
no protection, and it cannot serve as a gate: it exits 1 whenever a file merely differs,
which after `generate` is always.
**＋** `.claude/settings.json` is the only governed file a machine parses. If it does not
load, every hook goes with it — the ledger, the event log, the guard, the pretask gate,
the spec capture, `render --sync` — and `defaultMode: plan` with them, silently. Case 85
makes that file an assembly of four pages with the comma between two keys carried in a
child's body, and 89.1 removes the person who used to see the diff at a session start.
**－** The frontmatter of an agent or a skill file is machine-read too. It is short,
stable and barely part of a Render, so 89.4 does not cover it; that would be its own Case.
**－** `git pull` lives inside `/hi`, which runs after the `SessionStart` hooks, so what a
pull brings is rendered only at the following start. Closing that needs a render inside
`/hi` after the pull, and it waits for the pull itself to be decided (sprint, Slice 5).

## Criterion

- [[estimate-close-commits]] § case 89.2

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#case-89.2
