---
title: "A guard is removed whole or the proof is not a proof, and `if false` runs the other branch"
type: lesson
status: archived
authority: mutation-completeness
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/vault-check.sh"]
tags: [harness, testing, vault]
---

# The mutation that proved nothing

**A first attempt to disable rule 15 of `scripts/vault-check.sh` replaced `if [ ! -f … ]` with
`if false`.** That does not remove the rule: it runs the `else` branch, which still invokes the
check. The reading was muddied rather than negative.

**The proof was redone through `git stash`**, which removes the change whole and — on this
particular day — also avoided the file round-trip that had just corrupted the same file
([[a-file-round-tripped-through-pythons-text-mode-loses-a-literal-carriage-return]]).

# Why the shortcut is tempting and wrong

**`if false` looks like "turn this off"**, and on a guard with no `else` it is. On a two-branch
condition it selects the other branch, so the mutation tests a different code path and reports on it
as though it were the absence of the rule.

**The verification a mutation owes is that the case it targets goes red.** Here it did not go red
in a way that could be read, which is the signal that the mutation was wrong rather than the rule
([[a-case-green-before-its-mechanism-is-proved-by-removing-the-guard]],
[[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

# The method that stands

**Remove the whole guard, by stash or by deleting the block, and re-run.** A conditional flipped in
place is not a removal, and this repository's own selftest discipline — every case proved to fail
before it is believed — depends on the mutation being total.
