---
title: "The one-writer note speaks once per session, and its scope is untouched"
type: decision
status: current
authority: one-writer-note-channel
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [vault, harness, agents]
---

# What changed, and what deliberately did not

**Changed: the channel.** The one-writer reminder in `.claude/hooks/ask-the-vault.ps1` is emitted
once per session instead of once per written page.

**Untouched: the scope.** Which paths arm it is exactly what it was. Narrowing the scope would
reverse the direction the owner chose in [[the-hook-was-stricter-than-the-rule-it-enforced]], where
the hook was found guarding more than the rule said and the **rule** was widened to match rather
than the hook narrowed.

**Rejected: the `--lint` shape** — moving the note behind a flag, the way the tag density advisories
moved ([[the-tag-density-advisories-move-behind-lint]]). **A hook has neither a flag nor an exit
code to hang it on**: it prints into a session's context or it does not.

**Ratified by the owner.**

# Why it needed changing at all

**It had been firing about fifty times per ingest into the librarian's own context**, and it had
been doing so since before the session that found it — **verified as pre-existing rather than
assumed**, from the branch's own history ([[an-alarm-that-fires-when-nothing-is-wrong-is-one-you-learn-not-to-read]]).

**The message had been written for two audiences at once** — *if you are the librarian, this is your
job: proceed* — which is what a hook does when it cannot tell who is writing. That a `PreToolUse`
payload does not say who is writing is already recorded
([[parallel-librarians-break-the-one-writer-property]], [[session-hooks]]), and speaking once is the
cheapest thing available to a guard that cannot address its reader.

# Amendment, 2026-08-25 — the scope is no longer untouched

**The sentence above stands as written and was true on 2026-08-20.** From this date the scope has a
declared exception: `wiki/*/_schema.yaml` no longer arms the note, because a decision of 2026-08-19
put those files in the session's hands
([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]],
[[the-schema-files-leave-the-one-writer-note-by-a-flag-of-their-own]]).

**It is not the narrowing this page rejected.** What stood here is that narrowing *which paths arm
it* would reverse the direction the owner chose, where a hook guarding more than its rule was answered
by widening the rule. **Here the rule itself carries the exception**, so the hook is being brought
back to the rule rather than away from it.

**And the exception is delivered by a flag of its own**, consumed only by the branch that prints the
note — narrowing the shared `$inWiki` flag would silently take the schema files out of the pre-task
net exclusion as well ([[the-vault-is-excluded-from-the-pre-task-net]]).

**Not built.** The hook is unchanged.
