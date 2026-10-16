---
type: estimate
kind: QA
status: pending
target: "[[rule-clean-branch]]"
purpose: Whether guppi ship writes sprint.md in the closed form of the sprint guppi, backlog.md and glossary.md by their writers, a brief.md that opens the next sprint and a log.md with its heading alone, so that the checks of those files pass and the first /hi of a new project in a git repository starts /sprint-open
method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton; by hand, after the librarian's run of the session that set this method, with a tag prod-x.y.z in the history of HEAD: in an empty folder that is no git repository, guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, the copy and the folder being those of the reading of estimate-git-context-offers-git-init where that reading runs at the same commit, /guppi:install typed, Claude Code reopened, /hi typed until its git step has run git init -b main, the next /hi typed, and guppi sprint --check, guppi backlog --check and guppi glossary --check run over the copy, read against the Criterion"
checked: 2026-10-16
origin: raw/2026-10-15/0553/ledger.md#case-822.3
sprint: plugin
created: 2026-10-15
tags: [plugin, ci]
---

## Criterion

When:
`uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
**＋** Or, in an empty project, the person installs the plugin `guppi` from such a copy, types `/guppi:install`, reopens Claude Code there and types `/hi`, and types `/hi` again after the git step of `rule-git-context` where the folder is no git repository.

Then:
It writes `vault/wiki/sprint.md` as `closed_form` of `.guppi/guppi/sprint.py` writes it for the sprint `guppi`, so its first `## ` heading carries the mark of a closed sprint.
**＋** It writes `vault/wiki/backlog.md` and `vault/wiki/glossary.md` as `guppi backlog` and `guppi glossary` write them over the clean version, by their own code.
**＋** It writes a `vault/wiki/brief.md` whose `Cases` of its `## Next session` open with the line `open the next sprint — no sprint is open since the close of guppi`, and a `vault/wiki/log.md` that holds its heading and the paragraph under it alone.
**＋** Over the clean version, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check` print nothing and exit 0.
**＋** In that project, the first `/hi` whose `Branch:` line, the output of `uv run --project .guppi guppi gitstate`, names a branch starts `/sprint-open` before the Frontier.
**－** A `/hi` whose `Branch:` line reads `none: this folder is no git repository` is no part of this promise.
**－** It writes no `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` or `log.md` of the project it builds from.

## Result

2026-10-16, Retro of session 0104, tag prod-0.2.0 local: test_ship.py -k skeleton 3 passed; over scratchpad/ship-plugin guppi sprint --check, guppi backlog --check and guppi glossary --check exit 0, sprint.md opens "## guppi — closed", the Cases of brief.md open with "open the next sprint — no sprint is open since the close of guppi", log.md holds its heading and paragraph alone; in C:\PROJECTS\test, an empty folder and no git repository, the first /hi after /guppi:install and a reopen stopped on `Shell command failed for pattern "!`git branch --show-current`": fatal: not a git repository`, so it did not start /sprint-open; after git init, /hi started /sprint-open before the Frontier

## History

- 2026-10-15 created · [[decision-case-822.3]]
- 2026-10-16 updated: the method waits for a tag prod-x.y.z in the history of HEAD, without which guppi ship writes nothing; the Criterion stands · [[decision-case-845]]
- 2026-10-16 status: pending → failed · raw/2026-10-16/0104/ledger.md#L18
- 2026-10-16 deferred · [[decision-case-855]]
- 2026-10-16 defer by decision-case-855 superseded · [[decision-case-859]]
- 2026-10-16 updated: the Criterion replaced whole — the first /hi whose Branch: line names a branch starts /sprint-open, and the /hi of the git step is no part of the promise; the defer of case 855 retired · [[decision-case-859]]
