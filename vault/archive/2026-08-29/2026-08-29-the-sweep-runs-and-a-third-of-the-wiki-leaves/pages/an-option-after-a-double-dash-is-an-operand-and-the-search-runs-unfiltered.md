---
title: "An option after a double dash is an operand, and the search runs unfiltered"
type: lesson
status: archived
authority: double-dash-operand
basis: measurement
sprint: S3
created: 2026-08-23
sources: ["archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md", "scripts/vault-archive.sh"]
tags: [harness, vault, testing]
---

# The defect, and it stood in a precondition that guards the store

`scripts/vault-archive.sh` wrote:

```
grep -rlF -- "$slug" "$VAULT/wiki" --include='*.md'
```

**`--` ends the options.** Everything after it is an operand, so `--include='*.md'` was a *path* to
search — `grep` reported `No such file or directory` on it, and the `2>/dev/null` beside it
swallowed the message. **The search ran with no filter at all.**

# What the missing filter let through

**`wiki/*/_schema.yaml` carries thirteen real page slugs inside its comment blocks.** So the
`pages` precondition — *refuse to archive a page while no live page names its slug* — counted a
mention in a schema comment as a live page pointing at it
([[vault-archive-sh]]).

**The precondition therefore passed for the wrong reason on any page whose slug a schema comment
happens to quote**, which is precisely the set of pages the schemas were written about: the ones
that decided the fields.

# It was repaired and proved by switching the line back and forth

**Owner's ruling, in one word: «чинить».** He was asked three times across the session before it was
answered, which is its own finding about how a small defect gets deferred by being small.

**Proved in both directions on 2026-08-23**: with the fix, the page is refused with exit 2; without
it, the archiver walks straight past the precondition and reports `cited by 0 page(s)`. That is the
procedure this store already requires of a new verdict — plant it, revert it, read both
([[a-planted-offender-is-proved-by-reading-it-back]],
[[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

# Two habits it costs, and both are cheap

- **Put options before `--`.** `--` exists to protect a *value* that starts with a dash; it is not
  a separator you sprinkle before the last argument.
- **A `2>/dev/null` beside a search is a silencer, and this is what it silences.** The error was
  printed every run and read by nobody, for as long as the line stood
  ([[an-instrument-that-fails-towards-nothing-to-do]]).

**The failure direction is the dangerous one.** A filter that silently matches everything makes a
guard *pass*, and a guard that passes for the wrong reason is indistinguishable from one that works
([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).
