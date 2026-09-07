---
title: "A `.claude/rules/` file is generated whole by a script and deleted only by its own marker"
type: decision
status: current
authority: generated-file-ownership
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls/handoffs/2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.md", "scripts/vault-inject.sh"]
tags: [harness, vault, testing]
---

# Decided 2026-08-18, on the `/grill-me` that took the move to an empty frontier

**A file in `.claude/rules/` is generated whole, not region-carrying.** Its destination would be
frontmatter plus rule text with nothing hand-written around it, and **a region exists to protect an
insert into a file that has its own life** ([[a-region-is-a-paired-comment-named-for-a-rule]]). A
file with no life of its own does not need protecting; it needs owning.

**This is the `whole` delivery mode**, designed earlier and still unbuilt
([[the-harness-is-built-by-a-script-and-guarded-by-a-gate]],
[[the-governed-set-is-swept-and-markdown-by-property]]). **Its check is free**: regenerate and
compare, which is the question rule 12 already asks of every region
([[a-check-asks-by-running-the-writer-it-checks]]). The design is
[[generating-a-claude-rules-file-whole-from-its-vault-page]].

## Generation, rewriting and deletion belong to a script — owner

> **owner: "then we guarantee our system works rather than hoping."**

**Not a new script — a mode inside `vault-inject.sh`**, because a third command is a third place to
forget it ([[the-command-list-moves-into-a-makefile]]).

**Deletion is guarded: the script deletes only files carrying its own generated-marker.** That
marker does two jobs at once — it is the human's warning not to hand-edit, and it is the script's
permission to remove. **A file without it is never touched, whatever the vault thinks of it.**

## Hand-writing is forbidden only where a page backs the file — owner

> **owner: hand-writing is forbidden only in `.claude/rules/` files backed by a vault page.**

**A file in that directory with no page behind it is legitimate, not garbage.** Somebody may put a
rule there by hand and never involve the vault, and the store has no standing to delete it. That is
exactly why deletion keys on the marker rather than on the absence of a page: *"the vault does not
know about this file"* and *"this file is mine to remove"* are different statements, and only the
second one licenses a delete.

**What it obliges:** the marker's presence is the only fact the deleting branch may read, and a
selftest case owes it a file that carries no marker and survives a run.
