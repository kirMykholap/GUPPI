---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
purpose: Whether the lines Tests and Style of /retro run guppi test and guppi style with --exit-zero, so that a run of either command that finds a failing test or a style finding exits 0, while its line Ledger runs guppi tail with no flag
method: "uv run --project .guppi pytest .guppi/tests/test_commands.py -k exit_zero; by hand, at the Retro of the session that sets this method: the lines Tests, Style and Ledger of .claude/skills/retro/SKILL.md read against the Criterion, recorded in the estimate line"
checked: 2026-11-26
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi render` writes `.claude/skills/retro/SKILL.md` from the Render of `rule-retro`.
**＋** `uv run --project .guppi pytest .guppi/tests/test_commands.py -k exit_zero` runs.

Then:
The line Tests of `.claude/skills/retro/SKILL.md` runs `uv run --project .guppi guppi test --exit-zero`, and its line Style runs `uv run --project .guppi guppi style --exit-zero`.
**＋** With that flag, a run of either command that finds a failing test or a style finding exits 0.
**－** The line Ledger runs `uv run --project .guppi guppi tail` as before, with no flag.

## Result

2026-11-26, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
