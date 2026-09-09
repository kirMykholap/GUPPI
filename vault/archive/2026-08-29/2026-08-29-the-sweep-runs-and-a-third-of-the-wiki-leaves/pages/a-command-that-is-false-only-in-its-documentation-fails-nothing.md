---
title: "A command that is false only in its documentation fails nothing, which is the worst case"
type: lesson
status: archived
authority: false-documented-command
basis: code
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md", "CLAUDE.md", "scripts/vault-check.sh"]
tags: [testing, vault]
---

# The instance: the vault's own schema documents a broken check

Under `### authority`, the vault's `CLAUDE.md` gives this as the way to find contradictions:

```
rg "^authority:" wiki -o | sort | uniq -d
```

**`rg -o` without a capture group prints the matched text**, which here is the literal string
`authority:` — once per match. So the pipeline reports a duplicate **whenever two or more pages
carry the field at all** (133 of 142 on the tree of 2026-08-16) and **never compares the slugs**.
The correct form needs a capture:

```
rg '^authority: *(.*)' -o -r '$1'
```

## Why this is the worst case rather than a typo

**`vault-check.sh` rule 3 implements it correctly** — from frontmatter only, and from `current`
pages only — so the mechanism works and nothing fails. The consequence is entirely one-sided:

- nothing is broken, so nothing reports it;
- the reader who **follows the documentation** runs it, gets a hit that is not a duplicate, and
  learns nothing — or worse, "fixes" a real page to silence it;
- the reader who trusts the documentation over the script believes a check exists in a shape it
  does not have.

A rule that is wrong and *runs* gets found the first time it fires. A rule that is wrong and lives
only in prose is found by a human reading it beside the implementation, which is how all seven of
this project's harness divergences were found ([[no-rule-reads-a-harness-file]]).

## What it generalises to

**A flag that silently changes what a command compares is a class, not an accident.** `-o` looks
like a display option and is a semantic one. The store has met the shape before from the other
side, where an unsupported flag produced a silent zero rather than an error
([[a-measurement-agreeing-with-no-expectation-needs-a-different-instrument]]).

**The librarian does not write the store's rulebook**, so this correction is logged as a miss rather
than applied ([[the-librarian-writes-unattended]]); it is the seventh recorded instance of a harness
file asserting something false, and it travels with the register the field is missing
([[a-field-with-no-register-produces-unique-values-by-default]]).
