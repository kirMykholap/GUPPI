---
type: decision
case: "482"
status: archived
update: ["[[rule-close]]", "[[estimate-close-commits]]"]
origin: raw/2026-09-28/2000/ledger.md#case-482
sprint: migration
created: 2026-09-28
tags: [harness, workflow, git, librarian]
---

## Context

The `render` step writes each rule-controlled file from its Rule page. The librarian then commits with `git add vault CLAUDE.md .claude`, and `rule-close` forbids any path outside those three. Until case 476.1 every rendered file stood under one of those paths. `guppi.toml`, the settings file rendered from `rule-guppi-config`, is written at the repository root. So the librarian's run of 2026-09-28 wrote it and left it untracked (brief, Flags). A fresh clone then has no `guppi.toml`, and the pre-spec language check reports `guppi.toml: missing` there.
The person decided in one round. The commit is widened, and the file stays at the root: moving it into `.claude/` would change `guppi/config.py`, its tests and every page that names the file. The command names `guppi.toml` directly. The render does not print a list of the files it wrote: among the `governs` fields of the Rule pages, `guppi.toml` is the only path outside `vault`, `CLAUDE.md` and `.claude`. A later rendered file outside these paths comes through a Case that widens the commit again. The file that is untracked now goes into this session's Work Mode commit, because its content is what the Rule page already renders. The promise also gains a line that no rendered file stays untracked after the commit.
The frame. The Render of `rule-close` says "never a path outside those three", and the Criterion of `estimate-close-commits` says "No path outside those three". The change makes both false, so the Case changes the Render and replaces the Criterion whole. The old Criterion is in the shape used before case 193: a paragraph cut into short lines, then a block of case 89.2. The check of the answer notes each of its lines as not carried, because the new `when` and `then` rewrite them as whole statements. Their content is carried: a live run, one commit after the Retro commit, `vault/` and the rendered files, the message convention, never `--amend`, and the report with its counts, flags and lint total in twenty lines or fewer. Only "No path outside those three" changes, by the person's decision, to four paths. The update brings the Estimate to the new shape, so it sets `method` and `purpose`, which the page lacks; `rule-estimates-schema` leaves `purpose` out on older pages only until their recut. The docstring of `guppi/render.py` says the librarian commits the rendered files in its own commit (case 89.2). That stays true. The Criterion of `estimate-guppi-config-fills-the-languages` speaks of what the file holds, not of where it is committed, so it is not touched. The decision pages of case 89 quote the old command. They are records and stay as they are.
The reader of the changed text is the librarian agent, not code. It reads `.claude/agents/librarian-guppi.md` after the next render, and nothing refuses in between, so no old form is kept. The Case needs no `create`, so no vault query was run. Not done: the render does not report the files it wrote, and the file does not move.

## Problem

The librarian's commit takes only `vault`, `CLAUDE.md` and `.claude`, and `render` writes `guppi.toml` at the repository root. So the settings file that the checks read is never committed, and a fresh clone lacks it.

## Given

`rule-close` — the librarian's close; its Render holds the commit command and the ban on other paths
**＋** `.claude/agents/librarian-guppi.md` — the librarian's text, rendered from `rule-close`
**＋** `vault/` — the pages the librarian's run writes
**＋** `guppi.toml` — the settings file, written at the repository root
**＋** `rule-guppi-config` — governs `guppi.toml`, rendered in full
**＋** `guppi/render.py` — the renderer that writes the governed files
**＋** `estimate-close-commits` — the promise on the librarian's commit
**＋** `rule-estimates-schema` — a recut page carries `method` and `purpose`

## History

- 2026-09-28 created · raw/2026-09-28/2000/ledger.md#case-482
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
