---
title: "The schema files leave the one-writer note by a flag of their own, so the pre-task exclusion keeps them"
type: decision
status: current
authority: schema-exception-flag
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-25
created: 2026-08-25
sources: ["archive/2026-08-25/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs/handoffs/2026-08-25-the-twelve-items-are-decided-and-the-owner-names-what-the-discussion-costs.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, vault, agents]
---

# The ruling, 2026-08-25

> **owner:** «1) Убрать wiki/*/_schema.yaml из проверки 2) + 3) окей, правим»

**`wiki/*/_schema.yaml` stops arming the one-writer reminder.** The note tells a writer that the file
has exactly one legal writer, and a decision of 2026-08-19 put those files in the session's hands
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]). So the hook was delivering a
reminder that contradicts a live decision.

# The obvious edit breaks something else, and that is the substance of this page

**`.claude/hooks/ask-the-vault.ps1` sets one flag that three branches read.** `:166` sets `$inWiki`
for any path under the vault's `wiki/` or `archive/`; `:210` prints the one-writer note; `:277`
excludes the vault from the pre-task net.

**Narrowing the flag silently removes a path class from the third**, against the decision that keeps
the vault out of that net ([[the-vault-is-excluded-from-the-pre-task-net]]). **So the exception needs
a separate flag, consumed only by the branch at `:210`.**

# What the hook is, so the exception is not read as a weakening

**It injects a reminder, never blocks, never fails the tool and always exits 0**, and its matcher is
narrow by design — a file carrying a rule, or a file with exactly one legal writer. Its own header
records the reason: a guard on every edit becomes a ritual performed without reading
([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

**The direction of the last repair here was the opposite one.** When the hook was found guarding more
than the rule said, the **rule** was widened rather than the hook narrowed
([[the-hook-was-stricter-than-the-rule-it-enforced]]). This narrows the hook, and it does so because
the rule it enforces has an explicit exception now rather than a wider scope.

# Not done

**The hook is unchanged.** The note's scope narrows the moment the flag is split, and the page that
recorded the scope as untouched carries a dated amendment saying so
([[the-one-writer-note-speaks-once-per-session]]).

# Built 2026-08-26, and both directions were proved

**`.claude/hooks/ask-the-vault.ps1` gains `$isSchema`, read only by the one-writer note.** `$inWiki`
is untouched and still feeds the pre-task exclusion, which is exactly the separation this page
argued for.

**Two mutations, each read from its own run.** Removing the schema exception reddens exactly the two
silence cases. **Applying the rejected repair — narrowing `$inWiki` instead of adding a flag —
silences the note correctly and reddens the pre-task net case.** So the claim that the two consumers
cannot share one variable is now defended by a case rather than by this page
([[a-case-green-before-its-mechanism-is-proved-by-removing-the-guard]]).
