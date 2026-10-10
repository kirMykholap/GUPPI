---
type: decision
case: "459"
status: archived
update: ["[[estimate-lint-checks-the-method]]", "[[rule-estimates-schema]]"]
supersedes: ["[[decision-case-454]]"]
origin: raw/2026-09-27/1819/ledger.md#case-459
sprint: migration
created: 2026-09-27
tags: [harness, workflow, render, schema]
---

## Context

Lint checks the `method` of each Estimate. For an Estimate of a MOC, a reading by hand passes only if every Estimate of the MOC's children is a reading too, or if a sibling Estimate names a `make <target>` (cases 112.1, 212). The clause stops a MOC's reading from hiding its children's tests. The code is `check_method` in `guppi/lint.py`, and the promise is `estimate-lint-checks-the-method`.
The clause is wrong for `rule-claude-md`. `CLAUDE.md` is its Render in `render_mode: full`, with its three children spliced into their markers. Its one Estimate, `estimate-claude-md-rendered`, is a reading: the file equals the Render and every session loads it. Case 445.4 gave the child `rule-language` the Estimate `estimate-language-spec-prose-in-english`, whose `method` is a pytest over pre-spec. Since then lint prints `method: says by hand while estimate-language-spec-prose-in-english names a test file`. Case 454 deferred the item onto `rule-claude-md`.
Nothing is hidden. By case 378.5, the Estimate of a render rule promises only that the file equals the Render and is loaded. The behaviour a spliced paragraph describes belongs to that child's own Estimate, which is read on its own.
The frame has five MOCs with `enforcement: render` and `render_mode: full`: `rule-claude-md`, `rule-case-protocol`, `rule-skill-hi`, `rule-settings` and `rule-documentation`. The children of `rule-documentation` are code rules with tests. For that reason the person chose the narrow bound: only the Estimates of a child with `enforcement: render` stop counting. The Estimates of any other child still count.
The same clause stands in two more places, and this Case changes both. One is the module docstring of `guppi/lint.py`. The other is the description of `method` that `rule-estimates-schema` renders into `vault/wiki/estimates/schema.yaml`.
The new Criterion keeps every line of the old one. The old third line changes on purpose: it now counts only the counted Estimates of the children. The Leaf finding keeps its exact text. That text stands in quotation marks, not a code span, because the frame check of pre-spec reads a span with a slash as a path.
The Criterion of `estimate-estimates-schema-checked` does not speak of the `method` description, so it is not touched. `estimate-prespec-catches-a-method-without-a-form` leaves the MOC branch to lint, so it still stands. No Estimate of `rule-claude-md` changes, because its promise is unchanged.
The decision line carries `{supersedes:case 454}`, so `generate` clears the defer from `rule-claude-md`. The other lint findings in the brief stay with their own items.

## Problem

Lint reports a contradiction on `estimate-claude-md-rendered` that is not one. The clause of cases 112.1 and 212 counts the tested Estimate of a child whose Render is spliced into its parent's file. That Estimate promises the child's own behaviour, not the file, so the parent's reading hides nothing.

## Given

`estimate-lint-checks-the-method` — the promise of the `method` check of lint.
**＋** `guppi/lint.py` — `check_method`, `children_estimates` and the module docstring, the MOC clause of cases 112.1 and 212.
**＋** `tests/test_lint.py` — the tests of the MOC branch of the `method` check.
**＋** `rule-estimates-schema` — renders the description of `method` into `vault/wiki/estimates/schema.yaml`.
**＋** `Makefile` — the targets a `method` may name.
**＋** `estimate-claude-md-rendered` — the reading of `rule-claude-md` that lint reports today.
**＋** `rule-lint` — the rule the check belongs to.

## History

- 2026-09-27 created · raw/2026-09-27/1819/ledger.md#case-459
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
