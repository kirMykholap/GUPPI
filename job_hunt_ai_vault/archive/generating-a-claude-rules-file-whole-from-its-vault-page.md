---
title: "Generating a `.claude/rules/` file whole from its vault page: the mode, the marker and the checker"
type: proposal
status: deprecated
basis: human
sprint: S2
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-inject.sh", "scripts/vault-check.sh"]
tags: [harness, vault, testing]
superseded_by: [[the-whole-mode-owns-a-file-end-to-end]]
---

# Designed 2026-08-18 to an empty frontier, and not built

**The decision this builds is [[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]].**
This page carries what it would take. Nothing here exists on disk: `vault-inject.sh` renders regions
and knows nothing about generating a file.

**The `whole` mode was named long before this** as the way `settings.json` and the `.ps1` hooks
would ever be governed, since neither syntax admits an HTML comment
([[the-harness-is-built-by-a-script-and-guarded-by-a-gate]],
[[the-governed-set-is-swept-and-markdown-by-property]]). A `.claude/rules/` file is its first real
customer, and it needs the mode for a different reason: not that a marker cannot be written, but
that there is nothing around the text to protect.

## What the mode writes

| Part of the generated file | Where it comes from |
|---|---|
| `paths:` frontmatter | the vault page's own `paths:`, synced ([[paths-lives-on-the-vault-page-and-is-written-widest]]) |
| the rule text | the page's `<!-- text -->` slice, the same one a region would receive ([[what-travels-from-a-rule-page-is-a-marked-slice]]) |
| a generated-marker | emitted by the writer; it is the file's warning and the script's permission |

**The check is free**: regenerate into a temporary file and compare byte for byte. That is the
question rule 12 already asks by running the writer it checks
([[a-check-asks-by-running-the-writer-it-checks]]), and the comparison must not be made through a
command substitution ([[a-command-substitution-strips-the-newline-a-gate-compares]]).

## Deletion, which is the part with teeth

**The script deletes only what carries its marker.** A file in `.claude/rules/` with no marker is
somebody's hand-written rule and is never touched, whatever the vault knows about it. **The verdict
owed in `vault-check.sh`** is the mirror: a marked file whose page is gone — the leftover case rule
11 already reasons about from the other direction
([[the-address-verdict-catches-the-leftover-copy-not-the-wrong-file]]).

## What is open

- **The marker's spelling and whether it costs anything.** If HTML comments in a rules file reach
  the model, a *generated, do not edit* banner is context spent on every matching read; if they are
  stripped, it is free. **Probe 3 decides it** ([[the-conditional-delivery-probe]]).
- **What the checker does with a hand edit it finds** — red, or advisory, is not decided
  ([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]).
- **Whether the mode is selected by a field on the page or by the shape of `governs:`.** The delivery
  mode as a field was sketched when `render:` was refused and nothing has chosen since
  ([[render-was-not-introduced]]).

## What not building it costs

**The AST move cannot land**, because its destination is a generated file
([[the-ast-rule-moves-to-prove-the-mechanism]]). Unconditional delivery stands meanwhile and breaks
nothing ([[moving-a-rule-into-claude-rules-with-a-paths-scope]]).

Retired with `superseded_by:` the day it is built or refused, once nothing on it lives only here
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]],
[[proposals-are-a-folder-not-a-status]]).

# Built 2026-08-19 and retired 2026-08-20, with where each part went

**All three open questions are closed, and the ruling that closed the middle one landed before this
retirement** — retiring the page first would have archived a live open question along with
everything else on it.

| What lived here | Where it lives now |
|---|---|
| what the mode writes, and that the form is defined once in the writer | [[the-whole-mode-owns-a-file-end-to-end]] |
| the free check — regenerate and compare byte for byte | that page, and [[a-check-asks-by-running-the-writer-it-checks]] unchanged |
| deletion keying on the marker, and the mirror verdict owed in the gate | [[deletion-keys-on-the-marker-and-nothing-else]] — and the mirror verdict needed no new rule |
| **open: the marker's spelling and whether it costs anything** | **closed by measurement.** The comment is stripped on both delivery paths, so the banner is free ([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]) |
| **open: what the checker does with a hand edit — red, or advisory** | **closed by ruling, 2026-08-19**: [[a-hand-edit-to-a-generated-rules-file-is-red]] |
| **open: whether the mode is selected by a field or by the shape of `governs:`** | **closed by ruling**: a field, and `governs:`-shape selection was rejected ([[render-is-reinstated-and-required-now-that-another-mode-has-a-writer]]) |
| what not building it cost — the AST move could not land | discharged: [[the-guard-is-built-and-the-ast-move-went-ahead-behind-it]] |

**What the build added that this page did not have**: a missing destination *directory* is a
problem while a missing destination *file* is the normal first state; and the residual in the
deletion sweep, which is written beside the code rather than here.

**Retired under the policy rather than by a call on this page**
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).
