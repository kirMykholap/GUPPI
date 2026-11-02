---
type: estimate
kind: QA
status: archived
target: "[[entity-link-graph]]"
purpose: Whether guppi links prints, for a page or a file, each neighbour out and in with the kind of link and the purpose line, from the fields, the body, the path fields and the names in the rendered files, and no Decision page
method: "uv run --project .guppi pytest .guppi/tests/test_links.py, which runs the command over a vault in a temporary folder for each kind of link in both directions; and by hand, in Work Mode of this session: the output of uv run --project .guppi guppi links .claude/skills/sprint-open/SKILL.md, which names case-guppi, and of uv run --project .guppi guppi links .claude/agents/case-guppi.md, which names grill-me, read against the Criterion, the output in the estimate line"
origin: raw/2026-10-31/1831/ledger.md#case-967.1
sprint: plugin
created: 2026-10-31
tags: [harness]
---

## Criterion

When:
`uv run --project .guppi guppi links <slug or path>` runs over the live pages of `vault/wiki/` and the text that `guppi render` writes into each file a rule renders.

Then:
It prints the block of that page or file: a line `## <slug or path>`, its purpose line, then one line per neighbour that says `out` or `in`, the kind of link and the neighbour, with the purpose line of a neighbour that is a page.
**＋** A page links out by its fields, and by its `[[slug]]` links outside `## History`, as `links_of` of `.guppi/guppi/lint.py` reads them from the page with its History left out, by each path of its `implementation_ref`, `governs` and `code_ref`, and by each slug of a live page that its body names outside `## History`, in a code span or not.
**＋** A rendered file links out by each name it holds: an agent of `.claude/agents/` anywhere, a skill of `.claude/skills/` after a slash, alone in a code span or in a `skills:` list, and a command of `.guppi/guppi/cli.py` as `guppi <name>`.
**＋** The name of an agent or a skill links to the page that renders its file, and the name of a command to each page whose `implementation_ref` names its module.
**＋** Each link out of one page or file is a link into the other, and a file inside a folder that a page names links into that page.
**＋** The purpose line of a page is its `purpose`, of a lesson its `root_cause` and of an insight its `pattern`.
**－** It reads no page under `vault/wiki/decisions/` and prints no Decision page as a neighbour.
**－** A slug or path that is neither a live page nor a file prints one line that says so, and the command exits non-zero.

## Result

2026-10-31, Retro (session 1831): uv run --project .guppi pytest .guppi/tests/test_links.py, 13 passed, each line of the Criterion over a vault in a temporary folder (block form, field, `[[slug]]`, path-field and body-name links outside History, agent, skill and command names of a rendered file to the page that renders or runs them, links in, a file in a named folder, purpose lines of a lesson and an insight, no Decision page, an unknown name exits 1); by hand in Work Mode: uv run --project .guppi guppi links .claude/skills/sprint-open/SKILL.md printed "- out agent case-guppi: rule-case-build — Prevents a Case from being shown before one agent has built it …", and uv run --project .guppi guppi links .claude/agents/case-guppi.md printed "- out skill grill-me: rule-skill-grill-me — Prevents an interview from acting on a plan …"; `guppi links decision-case-966` printed `links: decision-case-966 is neither a live page nor a file`, exit 1

## History

- 2026-10-31 created · [[decision-case-967.1]]
- 2026-10-31 status: pending → passed · raw/2026-10-31/1831/ledger.md#L30
- 2026-11-01 updated: the bare link of the Result put in a code span, so lint reads no link to a page · [[decision-case-973]]
- 2026-11-02 deleted · [[decision-case-999.1]]
- 2026-11-02 archived · cleanup
