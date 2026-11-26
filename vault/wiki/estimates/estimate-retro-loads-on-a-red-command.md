---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
purpose: Whether the lines Tests and Style of /retro run guppi test and guppi style with --exit-zero, so that a run of either command that finds a failing test or a style finding exits 0, while its line Ledger runs guppi tail with no flag
method: "uv run --project .guppi pytest .guppi/tests/test_commands.py -k exit_zero; by hand, at the Retro of the session that sets this method: the lines Tests, Style and Ledger of .claude/skills/retro/SKILL.md read against the Criterion, recorded in the estimate line"
checked: 2026-11-26
origin: raw/2026-11-02/1337/ledger.md#case-1003.4
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness]
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

2026-11-26, Retro of session 2333, .claude/skills/retro/SKILL.md lines 7, 9 and 11 and uv run --project .guppi pytest .guppi/tests/test_commands.py -k exit_zero: the line Tests runs uv run --project .guppi guppi test --exit-zero, the line Style runs uv run --project .guppi guppi style --exit-zero, the line Ledger runs uv run --project .guppi guppi tail with no flag; the exit_zero tests 3 passed, 8 deselected, so a red run of either command exits 0

## History

- 2026-11-02 created · [[decision-case-1003.4]]
- 2026-11-02 deferred · [[decision-case-1007]]
- 2026-11-27 defer by decision-case-1007 superseded · [[decision-case-1072.1]]
- 2026-11-27 updated: taken up: the Criterion replaced whole, its reading moved to the text of the skill and the --exit-zero tests; the load in the CLI is read by a one-off Estimate of the sprint page; the defer of case 1007 retired · [[decision-case-1072.1]]
- 2026-11-27 status: pending → passed · raw/2026-11-26/2333/ledger.md#L10
