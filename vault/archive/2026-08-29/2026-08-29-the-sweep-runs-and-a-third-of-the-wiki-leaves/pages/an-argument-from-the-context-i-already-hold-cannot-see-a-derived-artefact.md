---
title: "An argument from \"my context already holds it\" cannot see a derived artefact"
type: lesson
status: archived
authority: context-argument-blindness
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "scripts/session-dialogue.py"]
tags: [process, agents, harness]
---

# The incident, 2026-08-26

**The session argued against reading `.superpowers/sdd/session-dialogue.md` whole at `/retro`**, on
the ground that nothing had been compacted, so its own context already held everything the extract
contained. **The owner refused and the reading was done in the same turn.**

**It found a defect the conversation never contained**: the extract's attention list groups by filed
block rather than by line, so five of that session's own feedback marks sit under the wrong heading
([[the-grouping-defect-in-the-dialogue-extract-is-an-s3-harness-line]]).

# Why the argument was wrong in principle and not just unlucky

**The extract is not a copy of the conversation.** It is the conversation **plus a list a script
generated from it**, and no amount of un-compacted context contains a thing that was computed after
the fact.

**The general form:** a context window holds what was said and what was read. It does not hold what a
tool would print about them. Any argument of the shape *I already have this* has to be checked
against what the artefact contains that its input did not
([[generated-text-can-lie-about-the-mechanism-that-generates-it]]).

# The cost, on the record

**About 26,000 tokens per retro**, which the owner accepted explicitly and filed under the new
optimisation topic rather than under this argument
([[the-session-extract-is-read-whole-at-every-retro]],
[[optimisation-becomes-a-conversation-topic-of-its-own]]).
