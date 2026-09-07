---
title: "`governs:` is a path from the repository root, and the vault's name is fixed from now on"
type: decision
status: archived
authority: governs-path-resolution
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-a-rule-is-written-once-and-rendered/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md", "scripts/vault-inject.sh", "scripts/vault-check.sh", "job_hunt_ai_vault/CLAUDE.md"]
tags: [harness, vault]
---

# Decided by the owner on 2026-08-17

**`governs:` names one file, written as a path from the repository root, and resolved against
nothing else.** And, in the same breath: **the vault directory's name is fixed from now on** —
renaming it was setup, and setup is over.

**Rejected:** the dual-root resolution that `sources:` uses, and a `repo:` / `vault:` prefix on the
value.

## Why `sources:` may try both roots and this may not

`sources:` asks only **whether a citation resolves**. Both answers are harmless: a path that
resolves under either root is a real file, and the rule was never about which one. `governs:` names
a file **the injector writes**. A path that could mean two files renders into the wrong one, and
the wrong one is a harness file that then instructs an agent.

The difference is the direction of the operation, not the strictness of the rule. **A reader may be
generous; a writer may not.**

## This overrides a standing constraint, and keeps the half that matters

[[the-vault-directory]] (`authority: vault-location`, `basis: code`, still `current`) says **no
script and no page may depend on the vault's directory name**. A rule governing a file inside the
vault must now write that name into `governs:`, so the constraint no longer holds in full.

**What is retired is the constraint on `governs:` alone. Everything else is unchanged, and this is
the sentence that must not be lost:**

- **The scripts go on discovering the vault dynamically.** `vault-check.sh`,
  `vault-catalogue.sh`, `vault-inject.sh` and `.claude/hooks/vault-path.ps1` all keep the "top-level
  directory containing a `wiki/`" idiom, in the exact shape recorded on [[the-vault-directory]],
  including `-not -path './.*'` and `sort` before `head -1`.
- **Only `governs:` names the directory**, and only on a rule page whose destination is inside the
  vault.

Nobody may read "the name is fixed" as permission to remove discovery. The name being stable is a
statement about the owner's intentions; discovery is what makes a rename survivable if he changes
them.

## A green selftest case is now living on borrowed time

`vault-check-selftest.sh` carries a case named **«the vault is renamed»**, and it passes today. The
first rule that governs a file inside the vault will put the directory's name into a `governs:`
line, and that case will go **red** — correctly, and for a reason nobody will remember.

**It is a decision to retire, not a bug to fix**, and it is on the register with its consequence
([[what-the-harness-build-waits-on]]). Recorded here because it will look like a defect to whoever
meets it first.

## How the question reached the owner at all

It was found by a `/pre-task`, which established that `governs:` had **no vault-name-free
spelling** ([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]). Before that, the
session had decided the opposite in writing — dual-root resolution with ambiguity as a hard error —
from a `current` vault page treated as settled fact rather than as a question worth one line to the
owner ([[a-vault-page-is-a-question-to-the-owner-not-a-settled-fact]]).

## The uniqueness clause beside this decision is gone — 2026-08-17

**The vault's schema documented `governs:` as *"required, and unique across current rules"*.** The second
half is removed: the owner deleted the destination-uniqueness verdict from `scripts/vault-check.sh` at
`e478c19`, and the schema line was corrected in the same session at `ba998a0`
([[governs-uniqueness-is-removed-and-the-pair-carries-it]]).

**Nothing about *this* decision changes.** The field still names one destination, still resolves against
the repository root and nothing else, and still may not be spelled two ways. What changed is that a
**destination may be named by more than one rule** — nine rules name `CLAUDE.md` today
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]).

**The borrowed-time selftest case above has not fired yet**, because no rule governs a file inside the
vault; twelve governed files still carry no region at all
([[a-governed-file-with-no-region-is-an-advisory]]).

**And the field is inert outside `wiki/rules/`** — neither rendered nor refused — which is the next thing
about it that has to change ([[a-page-outside-wiki-rules-carrying-governs-is-silently-inert]],
[[governs-becomes-a-property-of-any-page]]).

# The cardinality changed on 2026-08-21, and everything else here stands

**The field takes a bare path or an inline list of them**, so *"`governs:` names one file"* above is
false from that date. **The resolution rule is untouched**: each destination is a path from the
repository root, resolved against nothing else, and for the reason this page gives — a reader may be
generous, a writer may not ([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]],
[[the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership]]).

**The block form is refused by both readers and the owner ruled the refusal red rather than silent.**
That verdict is owed; refusing to parse is what exists.

*(Marked at the ingest of `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# Amendment, 2026-08-25 — the prediction about the renamed-vault case is probably stale

**The case has not fired, and the reason may be that it cannot.** Read off the tree on 2026-08-25:
**no rule page governs `job_hunt_ai_vault/CLAUDE.md`.** All sixteen pages in `wiki/rules/` were read —
eleven govern the repository's `CLAUDE.md`, the rest govern skills, agents, `.claude/rules/` and the
pre-task message.

**And no selftest case in `scripts/vault-check-selftest.sh` or `scripts/hook-selftest.ps1` names a real
rule slug.** The fixtures are synthetic — `probe-rule` and `whole-rule` — so the «the vault is renamed»
case exercises planted pages rather than the corpus. **A real `governs:` line naming the vault
directory therefore need not redden it**, which is the ground for calling the prediction above stale
rather than pending.

**It is about to be testable.** The plan of 2026-08-25 writes the librarian's write-ritual instruction
as a rule page governing `job_hunt_ai_vault/CLAUDE.md`, which would be the first rule to name the vault
directory in `governs:` ([[the-measure-writer-script-and-what-it-refuses-to-do]]). **Nothing is built**,
and whether the case goes red is a reading nobody has taken.

**Everything above this note is unchanged**, including the sentence that discovery may never be removed.
