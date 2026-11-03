---
type: estimate
kind: QA
status: passed
target: "[[rule-close]]"
purpose: The librarian's run ends in one separate commit of vault and each file the render writes, by the close command as its frame writes it, with no rendered file left modified or untracked
method: "uv run --project .guppi pytest .guppi/tests/test_render.py -k paths, on Windows too, where the test that runs guppi render --paths as a child process reads its output as bytes; by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: git log shows the commit of that run and the paths it touched, and git status shows no file the render wrote as modified or untracked"
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, git, librarian]
core: true
---

## Criterion

When:
After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

Then:
`uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, each line ended by a bare line feed with no carriage return, on Windows too, and writes nothing.
**＋** The close command, as `.claude/agents/librarian-guppi.md` writes it, passes each path of that list to `git add` as the path stands, with no filter added to it.
**＋** `git log` shows the librarian's commit as one commit after the Retro commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`; only the commit of `report.md` that `/handoff` or `/box` makes follows it.
**＋** The commit takes `vault/` and each file of that list: `git add vault $(uv run --project .guppi guppi render --paths)`.
**＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as modified or untracked.
**－** The commit takes no path that neither `vault/` nor that list names.
**－** In a project without `rule-plugin-install`, the list and the commit name no `plugin/skills/install/SKILL.md`.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
