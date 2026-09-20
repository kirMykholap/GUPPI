---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: A bare `[[slug]]` in the plan file that names no page is a finding of pre-spec before the Spec is approved
method: pytest tests/test_prespec.py, the tests of check_bare_links
origin: raw/2026-09-20/0958/ledger.md#case-264.2
sprint: migration
created: 2026-09-20
tags: [session, workflow, harness, tests]
---

## Criterion

Given:
The conditions of the parent.
**＋** `prespec --check` prints one line per finding on the plan file and exits 1 when it printed any; `tests/test_prespec.py` fixes every class of finding.

When:
The person invokes `/pre-spec`, and `guppi prespec --check <plan> --session <id>` reads the plan file.

Then:
One line `case N: [[slug]] outside a code span names no page` is printed for every `[[slug]]` in the plan file outside a code span — in the blockquotes and in the strings of the `then` blocks — that has no live or archived page.
**＋** A slug a `create` of the same plan carries, and a hub file of `wiki/` by its stem or its path, are not a finding.
**＋** One line per slug and Case, however many times it stands.
**－** A `[[slug]]` inside backticks, and inside a fenced block tagged other than `then`, is not read.
**－** `lint` does not change: the finding on the page stands when the text reached it anyway.

## Result

2026-09-20, `uv run pytest -q tests/test_prespec.py` after the build: 60 green, eight new — a bare `[[decision-case-N]]` in a blockquote is one line `case 1: [[decision-case-N]] outside a code span names no page`, the same in backticks none, a live page, an archived page and the hub `[[index]]` none, a slug a `create` of the plan carries none, one slug twice in a Case one line, a `[[slug]]` in a `change` string of the `then` block read, one in a `tasks` fence or an untagged fence not read; live, `uv run guppi prespec --check` on this session's plan (nine Cases) printed nothing and exited 0, every placeholder of the plan in a code span

## History

- 2026-09-20 created · [[decision-case-264.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L26
