---
title: "The full selftest suite runs in the background while `/retro` proceeds, permanently"
type: decision
status: deprecated
authority: retro-suite-launch
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
superseded_by: "[[the-suite-stops-running-every-session]]"
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", ".claude/skills/retro/SKILL.md"]
tags: [harness, process, testing]
---

# The ruling, 2026-08-26

> **owner:** «запускать полный прогон suite пока идет retro - это очень хорошая идея... Предлагаю
> сделать это постоянным решением.»

**A permanent arrangement rather than one session's convenience.** `/retro` gains a step-0
instruction to launch the full selftest suite in the background before the interrogation begins.

# The argument, which is about his time and not about the suite

**The suite is roughly 38 minutes and the retro is a conversation.** Serialising them spends the
owner's time on nothing: the interrogation does not read the suite's output, and the suite does not
care what the interrogation concludes.

**The recorded totals are 34m8s and 37m44s** ([[vault-scripts]]). **This session took no new
reading** — it launched the run into the background without a timestamp, so `caught 178, missed 0`
carries no wall clock ([[a-background-job-with-buffered-output-cannot-be-told-from-a-dead-one]]).

# What it obliges, and it is not done

**A step-0 line in `.claude/skills/retro/SKILL.md`**, beside the one that already writes the session
dialogue extract ([[the-retro-step]], [[the-session-dialogue-extract]]).

**And a timestamp with the launch**, or the arrangement produces a reading nobody can compare —
which is exactly what it produced on the day it was decided.

# Rejected

**Rejected: running the suite after the retro**, which is the current order and is what he objected
to. **Rejected: not running it at all on a retro day** — the suite is the decider named by
criterion 1 of the open sprint, so a session that skips it cannot report on the criterion.
