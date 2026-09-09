---
title: "`paths:` lives on the vault page, the injector syncs it, and it is written with the widest true pattern"
type: decision
status: archived
authority: paths-scope-source
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-inject.sh"]
tags: [harness, vault, agents]
---

# Where the scope is written — owner, 2026-08-18

**`paths:` is a field of the vault page, and the injector syncs it into the destination's
frontmatter.** The rule's scope is part of the rule, and the rule is written once
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

**This is what `render:` lacked when it was refused** — a writer and a reader
([[render-was-not-introduced]]). A field that is neither written by a script nor read by one is a
per-page invention ([[a-field-earns-its-place-by-being-read-or-by-being-a-checksum]]).

**Obliges: a writer *and* a checker.** A one-way sync means a hand edit in the destination is never
noticed, which is the whole failure class the region mechanism was built against
([[the-injector-walks-pages-to-files-and-the-check-walks-files-to-pages]]).

**Frontmatter is not a region and the marker mechanism cannot reach it** — a paired HTML comment
cannot live inside a YAML block. That is a second, independent argument for generating those files
whole ([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).

# The widest true pattern, because the cost is asymmetric

**Over-matching costs a little context. Under-matching costs a rule that does not arrive** — and it
arrives at nobody with no error anywhere, which is the failure a path scope is most likely to
produce ([[a-scoped-rule-fires-on-a-read-and-an-edit-implies-one]]).

**The instance that proves it is inside the proposal for the first move.** It recorded
`tests/unit/*boundary*.py` as "six files, measured"; six files do match, but the set the AST rule
exists to protect is the files importing `_ast_boundary`, and the glob reaches **one of the three**
— `test_normalize_boundaries.py` and `test_parser_boundaries.py` are spelled in the plural and fall
outside a pattern demanding `boundar-y`. Corrected on the page
([[moving-a-rule-into-claude-rules-with-a-paths-scope]],
[[a-page-that-says-measured-can-carry-a-figure-nobody-measured]]).
