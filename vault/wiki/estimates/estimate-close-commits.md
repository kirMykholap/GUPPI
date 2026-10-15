---
type: estimate
kind: QA
status: passed
target: "[[rule-close]]"
purpose: The librarian's run ends in one separate commit of vault, CLAUDE.md, .claude and guppi.toml, with no rendered file left untracked, and a report of twenty lines or fewer
method: "by hand after the next librarian run: git log shows its commit and the paths it touched, git status shows no untracked file the render wrote, and the report is read in the transcript"
checked: 2026-09-29
origin: raw/2026-09-10/ledger.md#case-36.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, git, librarian]
---

## Criterion

When:
After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says.

Then:
`git log` shows one commit after the Retro commit. It takes `vault/`, `CLAUDE.md`, `.claude` and `guppi.toml`: `git add vault CLAUDE.md .claude guppi.toml`.
**＋** It stays one commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`.
**＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as untracked, `guppi.toml` included.
**＋** The report reaches the main agent with the counts, the flags and the lint total, in twenty lines or fewer.
**－** The commit takes no path outside `vault/`, `CLAUDE.md`, `.claude` and `guppi.toml`.

## Result

2026-09-29, by hand at the /hi of session 1432: git log shows f9a27b8 `docs(vault): librarian, 2026-09-29` as the one commit after the Retro commit ab14bec, which is its parent, so no amend; it touches 115 paths under vault/ and 3 under .claude/, none outside vault/, CLAUDE.md, .claude and guppi.toml; git status --short --untracked-files=all prints nothing; the report in the transcript of session 1134 gives the counts, the flags and the lint total in 15 lines

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L93
- 2026-09-12 criterion: case 89.2 added · [[decision-case-89.2]]
- 2026-09-12 updated: the vault-only clause of the criterion names the rendered files too (case 89.2) · [[decision-case-89.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L40
- 2026-09-28 updated: the Criterion replaced whole — the commit takes guppi.toml, and no rendered file stays untracked (case 482) · [[decision-case-482]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L1
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
