---
title: "`*.yaml` is pinned to LF, after the one extension left unpinned cost a debugging pass"
type: decision
status: current
authority: yaml-line-ending-pin
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".gitattributes"]
tags: [harness, vault, record-schema]
---

# Ratified 2026-08-19

> **owner:** «мы везде используем LF».

**`*.yaml text eol=lf` stands in `.gitattributes`**, and the six `_schema.yaml` files were
renormalised with it.

**Rejected: leaving the class unpinned**, which is what stood — and it stood on a measurement. The
schemas' own entity page had recorded on 2026-08-19 that *"the `awk` parse is CR-clean on this host
and the gate stays correct, so the class is not pinned"*, under the file's stated policy that this
project pins a class **after** it has cost something ([[a-file-class-is-pinned-after-it-costs-something]]).

## What it cost, which is why the policy fired

**`.gitattributes` pinned `*.sh`, `*.md`, `*.ps1` and `*.json` and missed `*.yaml`**, and it missed
it for a dateable reason: those lines were written on 2026-08-17 and the schemas were created on
2026-08-19.

**Measured the day it was pinned:** a `git stash push` / `pop` round-trip during an unrelated
investigation turned all six schemas CRLF, and an edit script's LF anchors then matched nothing —
**the same failure the file's own comment already describes**, on the one extension left out of it
([[the-lf-pin-protects-the-blob-and-git-status-is-silent-about-the-working-copy]]).

**`git diff --stat` after the renormalisation shows insertions only**, so nothing about the
repository changed and everything about the working copy did — which is the distinction the existing
comment draws and the reason the pin is not visible in the history the way a content change is.

## Why it matters more here than for an ordinary data file

**`_schema.yaml` is the gate's own input**, read by `awk` and `bash` exactly as the corpus is
([[the-per-folder-frontmatter-schema]]). A CR is a byte inside the field, not a line ending, so an
unpinned schema is a gate that judges a key set whose last member carries an invisible character.

**And this host cannot see the defect.** No CR reaches `awk` here, which is what made the earlier
measurement true and useless as a safety argument
([[no-cr-reaches-awk-on-this-host-and-the-container-is-where-it-bites]]).

## The order was wrong, and that is recorded separately

The pin was written before the owner ratified it:
[[the-yaml-pin-was-written-before-the-owner-ratified-it]].
