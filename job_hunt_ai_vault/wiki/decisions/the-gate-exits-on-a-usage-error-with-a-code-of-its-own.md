---
title: "`vault-check.sh` exits on a usage error with a code of its own, which is the house convention"
type: decision
status: current
authority: gate-exit-codes
binding: prohibition
basis: code
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "scripts/vault-check.sh", "scripts/vault-catalogue.sh", "scripts/vault-coverage.sh"]
tags: [harness, vault, testing]
---

# Kept 2026-08-20, having been questioned

**An unknown argument exits 2 and prints what the one legal argument is.** Not a new code:
`vault-catalogue.sh` and `vault-coverage.sh` already exit 2 on a usage error.

**Rejected: ignoring an unrecognised argument.** A flag that silently changes what a command does
— or silently does not — is a class this store already named
([[a-command-that-is-false-only-in-its-documentation-fails-nothing]]). Rejected also: reusing 1,
which would make a usage error indistinguishable from a red vault.

## The boundary it creates is named rather than fixed

**A non-zero exit from this script now means two different events**, and only an accident keeps
them apart ([[a-non-zero-exit-from-the-gate-no-longer-names-one-event]]). Both consumers of the
gate's exit code — `.claude/hooks/check-the-journal.ps1` and `.claude/hooks/lock-the-librarian.ps1`
— read **any** non-zero as *the vault is red*, and neither passes an argument, so it cannot fire
today.

**It is left as a known boundary because the fix is a second reader of one condition**, and this
store has that scar.
