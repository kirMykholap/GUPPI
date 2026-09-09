---
title: "`paths:` is required where it is read, and nowhere else"
type: decision
status: archived
authority: paths-requirement-scope
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "scripts/vault-inject.sh"]
tags: [harness, process, vault]
---

# The ruling, 2026-08-20

> **owner:** «`paths:` - не врем, а правим.»

**`render: whole` used to refuse without `paths:`, unconditionally.** It now refuses only when the
destination is under `.claude/rules/`, which is the only place Claude Code matches that frontmatter
and loads the rule on a read ([[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]).

**Rejected: giving a hook message a `paths:` it does not mean, so that the check would pass.** A
field a machine reads is the last place to put something untrue, and a scope written to satisfy a
check is a scope nobody can later trust.

# Why the requirement keys on the destination and not on the mode

**A rule delivered by a hook message has no file to match.** `render: whole` had acquired a second
kind of destination — `.claude/hooks/messages/pre-task.md`, read by
`.claude/hooks/check-the-plan.ps1` and by nothing else
([[a-pre-task-runs-between-the-plan-and-its-approval]]) — and the mode stopped being a proxy for
*this file's frontmatter is matched by something*.

**Under `.claude/rules/` a missing `paths:` is the error it has always been**: the generated file
would name nothing to match, and the rule would silently never load.

# The refusal was written as one glob and matched none of the paths it guards

**The condition first read `*/.claude/rules/*`**, while `governs:` is a path from the repository
root and arrives as `.claude/rules/x.md` with nothing in front of it
([[governs-is-a-path-from-the-repository-root]]). `paths:` silently became **optional in the one
directory that needs it** ([[a-refusal-written-as-one-glob-can-match-none-of-the-paths-it-guards]]).
Both spellings are now matched, and **a pair of selftest cases holds it**, one per side.

# What it obliges

**A `render: whole` page whose destination is not under `.claude/rules/` carries no `paths:`, and
the file it generates carries no frontmatter block at all** — not an empty one
([[a-generated-rule-file-with-no-paths-carries-no-frontmatter]]).

**[[paths-lives-on-the-vault-page-and-is-written-widest]] is unchanged** where it applies: when the
field exists it is authored on the page and synced verbatim. This decides *when it must exist*, not
what it says.
