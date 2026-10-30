---
type: estimate
kind: QA
status: pending
target: "[[rule-close]]"
purpose: The librarian's run ends in one separate commit of vault and each file the render writes, by the close command as its frame writes it, with no rendered file left modified or untracked
method: "uv run --project .guppi pytest .guppi/tests/test_render.py -k paths, on Windows too, where the test that runs guppi render --paths as a child process reads its output as bytes; by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: git log shows the commit of that run and the paths it touched, and git status shows no file the render wrote as modified or untracked"
checked: 2026-10-30
origin: raw/2026-09-10/ledger.md#case-36.1
sprint: migration
created: 2026-09-10
tags: [harness, workflow, git, librarian]
---

## Criterion

When:
After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

Then:
`uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, each line ended by a bare line feed with no carriage return, on Windows too, and writes nothing.
**＋** The close command, as `.claude/agents/librarian-guppi.md` writes it, passes each path of that list to `git add` as the path stands, with no filter added to it.
**＋** `git log` shows one commit after the Retro commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`.
**＋** The commit takes `vault/` and each file of that list: `git add vault $(uv run --project .guppi guppi render --paths)`.
**＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as modified or untracked.
**－** The commit takes no path that neither `vault/` nor that list names.
**－** In a project without `rule-plugin-install`, the list and the commit name no `plugin/skills/install/SKILL.md`.

## Result

2026-10-30, at the /hi of session 2341, from the librarian's run of session 1930 as its saved chat and its report show it: the close command as rule-close writes it failed at its first run, `git add` exiting 128 with "fatal: pathspec '.claude/agents/ask-guppi.md?' did not match any files", since guppi render --paths printed CRLF on Windows; the librarian re-ran it with tr -d '\r' on the path list, and that run made 07181305; the passed reading of this session read the end state alone

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L93
- 2026-09-12 criterion: case 89.2 added · [[decision-case-89.2]]
- 2026-09-12 updated: the vault-only clause of the criterion names the rendered files too (case 89.2) · [[decision-case-89.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L40
- 2026-09-28 updated: the Criterion replaced whole — the commit takes guppi.toml, and no rendered file stays untracked (case 482) · [[decision-case-482]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L1
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-16 updated: the Criterion replaced whole — the commit takes vault and each file that guppi render --paths prints · [[decision-case-857]]
- 2026-10-26 deferred · [[decision-case-885]]
- 2026-10-29 defer by decision-case-885 superseded · [[decision-case-903.1]]
- 2026-10-29 updated: the Criterion replaced whole without the report, which estimate-close-reports-in-twenty-lines checks; the method waits for a librarian's run that holds the Render of rule-close, and reads no transcript · [[decision-case-903.1]]
- 2026-10-30 status: pending → passed · raw/2026-10-29/2341/ledger.md#L1
- 2026-10-30 status: passed → failed · raw/2026-10-29/2341/ledger.md#L8
- 2026-10-30 updated: the Criterion replaced whole — guppi render --paths ends each line with a bare line feed, on Windows too, and the close command passes each path to git add as it stands · [[decision-case-914]]
