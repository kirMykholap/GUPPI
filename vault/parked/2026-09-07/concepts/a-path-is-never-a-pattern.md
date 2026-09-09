---
title: "A path is never a pattern, and a `sources:` line is the only place a rewrite may touch"
type: concept
status: current
authority: path-rewrite-mechanism
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-archive.sh"]
tags: [vault, harness, process]
---

# Finding is `grep -F`, rewriting is `awk`

`scripts/vault-archive.sh` never hands a path to a regular-expression engine
([[vault-archive-sh]]). It finds with `grep -F` and rewrites with `awk`'s `index()` and `substr()`.

**A path is full of characters that mean something else to a regex** — the dot most of all — and
escaping it is a step that can silently fail. It did: the first version escaped for `sed`, the
backslashes were lost on the way into the file, and `probe/RUNBOOK.md` became `probe&RUNBOOK&md`
([[a-literal-backslash-does-not-survive-a-heredoc-in-this-shell]],
[[an-instrument-that-fails-towards-nothing-to-do]]).

# The substitution is restricted to lines that BEGIN with `sources:`

```awk
index($0, "sources:") == 1
```

**On such a line a path is an address by construction. Anywhere else it may be a quotation** — and
nothing in the text of a path tells the two apart
([[sed-cannot-tell-an-address-from-a-quotation]]).

An **indented** line that merely looks like frontmatter is therefore left alone, because `index`
returns 2 or more. That is the defect the store already records, **spared by construction rather
than by care**.

# Proved on a fixture carrying all three cases at once

| planted | wanted | got |
|---|---|---|
| a real `sources:` line naming the old path | rewritten | rewritten |
| two prose sentences naming the same path | untouched | untouched |
| an indented line that looks like frontmatter | untouched | untouched |

**Prose is left behind on purpose.** A page recording history is supposed to name a path that no
longer exists, and the residual is an advisory's job rather than a rewriter's
([[a-path-detector-for-prose-references]], [[a-rewriter-must-be-paired-with-a-detector]]).
