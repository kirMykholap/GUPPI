---
title: "`.claude/rules/ast-boundaries.md` — the first harness file this project generates rather than writes"
type: entity
status: current
authority: generated-rules-file
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/rules/ast-boundaries.md", "scripts/vault-inject.sh"]
tags: [harness, agents, testing]
---

# What it is

**Appeared 2026-08-20.** The first file in this repository that the injector owns **end to end**:
frontmatter carrying the rule page's `paths:` verbatim, a blank line, the generated marker, a blank
line, the rule's slice ([[the-whole-mode-owns-a-file-end-to-end]]).

| Property | |
|---|---|
| Path | `.claude/rules/ast-boundaries.md` |
| Generated from | [[an-ast-boundary-test-is-fixed-at-its-cause-not-in-the-test]], which carries `render: whole` |
| Scope | `paths: ["tests/unit/*boundar*.py"]`, re-measured before the move: 8 files, containing all three importers of `_ast_boundary` |
| Written by | `bash scripts/vault-inject.sh` |
| Delivered by | the native path on a matching read, and the guard branch on a matching Edit or Write ([[the-guard-branch-lives-inside-a-hook-that-already-runs]]) |
| Hand edit | **red** ([[a-hand-edit-to-a-generated-rules-file-is-red]]) |
| Deleted by | the injector, and only because it carries the writer's marker ([[deletion-keys-on-the-marker-and-nothing-else]]) |

# The marker does two jobs at once

`<!-- vault-inject: generated from rule: … - do not edit -->` is **the human's warning** and **the
script's permission to delete**. A file in that directory without it is somebody's hand-written rule
and is never touched, whatever the vault knows about it
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]).

**It costs nothing in context.** An HTML comment is stripped on the native path
([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]) and on the guard path,
measured: 971 bytes on disk against 940 delivered, one line missing and it is the comment
([[a-loss-measured-between-different-quantities-is-not-a-loss]]).

**And it escaped a red verdict from the gate's own marker net by an accident of spelling**, which is
now fixed deliberately ([[a-generated-files-marker-escaped-a-red-verdict-by-an-accident-of-spelling]]).

# What its arrival changed elsewhere

- **`CLAUDE.md` went 145 lines to 139**, and the rules rendering into it went from nine to eight
  ([[the-repository-claude-md-after-the-rules-left-it]]).
- **It is a governed file that can never carry a region**, which is why the coverage criterion was
  reworded rather than the file hidden
  ([[the-criterion-on-governed-files-is-reworded-to-admit-full-generation]]).
- **The advisory reads `a region or whole generation covers 2 of 15`**, and this file is one of the
  two.

# What it is not

**It is not the only file in `.claude/rules/`.** `.claude/rules/_probe-paths.md` stands beside it,
hand-written, backed by no page, delivered by the guard like any other, and blocked from deletion by
the citations pointing at it ([[a-teardown-clause-cannot-see-that-it-has-become-what-it-guards]]).

**And it is not evidence that conditional delivery is settled.** It is one rule, moved to prove the
mechanism rather than to save context ([[the-ast-rule-moves-to-prove-the-mechanism]]), and the two
other rules measured against the movability criterion still fail it
([[a-path-scoped-rule-is-delivered-by-a-read-and-by-nothing-else]]).
