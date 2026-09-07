---
title: "The feedback line carries its target inside the bracket, and never between the kind and the colon"
type: decision
status: current
authority: feedback-target-grammar
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: the-feedback-line-carries-its-target-in-the-bracket
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", ".claude/hooks/catch-the-feedback.ps1"]
tags: [harness, process, vault]
---

# Context

**A decision now declares its target** ([[a-decision-declares-its-target-and-the-handshake-closes-it]]),
and the feedback channel is where a decision reaches the librarian. So a `decision:` line has to carry
the target too, or the librarian writes the page without it and the field is filled by guesswork.

**Case 2.5 as first put wrote `target <kind>:<slug>` between the kind and the rest of the line.** That
grammar is already forbidden: a prohibition fixed the destination into **brackets straight after the
kind**, chosen against a word in that position precisely because it breaks the catcher's parser
([[a-measure-line-names-its-destination-in-brackets-after-the-kind]]).
`.claude/hooks/catch-the-feedback.ps1:226` anchors its his-words guard immediately after the kind.

# The question

**Where in a feedback line does the target go?**

# How it works after

**Inside the bracket**, as `target:<kind>:<slug>`, alongside the destination the bracket already
carries — so a line reads `- decision: [proposal:decision-lifecycle target:rule:some-slug] …`. The
hook validates only the **kind** and passes the bracket through as free text, so the scheme needs no
change to the parser.

**It renders into three files and not one**:
[[speak-the-feedback-in-the-turn-and-the-hook-files-it]] governs `CLAUDE.md`, the `vault-ask` skill
and the handoff skill. **And it needs a case in `scripts/hook-selftest.ps1`** against
`catch-the-feedback.ps1:226`, because the change is exactly in the region that guard anchors on.

# Recommendation

**Put it in the bracket**, which the session did not do when it first put Case 2.5 and which
`/pre-task` corrected before anything was written.

# Ratification

**The owner selected it** by approving the plan of 2026-08-30, having ratified Case 2.5 in the form
that had the grammar wrong. **The correction is `/pre-task`'s, not the session's**, and it is one of
the four findings that were errors in what the session had already told him.

**Not built.**

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
