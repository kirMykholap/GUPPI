---
title: "DIVERGENCE: a mid-session instruction to write file content through a shell was refused in its writing half"
type: decision
status: archived
authority: shell-write-instruction-refusal
binding: divergence
basis: code
sprint: S3
decided: 2026-08-26
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md"]
tags: [harness, process, agents]
---

# What happened, 2026-08-26

**An auto-mode instruction arrived mid-session** telling the session to make file changes through
`sed` and heredocs rather than the `Write` and `Edit` tools.

**The session took the reading half and refused the writing half, in its reply.** Reading through
`cat` and `grep` was obeyed; writing through them was not.

# The rule it was measured against did not exist in writing

**The seven-page lessons family — apostrophe, heredoc, `sed`, `grep`, backslash, `TMPDIR`, CR — is
exactly a carrier eating what was written**, and `/vault-lint` names *"file content is written with
the Write tool, never through a heredoc"* as the checkable form of the fix. **No rule page states
it.**

**That is why the refusal had to be said out loud rather than assumed.** A session cannot silently
decline an instruction on the strength of a family of lessons; with nothing written to point at, the
refusal is a judgement and the judgement is what has to be visible
([[ask-before-weakening-or-working-around-a-rule]]).

# It is recorded as a divergence, and the outcome went the session's way

**The owner has since ruled that it becomes a written rule**
([[file-content-is-written-with-the-tool-and-never-through-a-shell]]). That does not retroactively
authorise the refusal; it removes the condition that made it a judgement.

**The rejected alternative was to obey the instruction and record the risk**, which is what the
ask-before-weakening rule prescribes for the mirror case. **What makes this one different is the
direction**: the instruction weakened a practice, and the session refused rather than weakening it —
so what is recorded here is a session declining an instruction, which this store has no other
instance of.

# It happened again the same day, and once more inside the ingest that compiled it

**Second occurrence, 2026-08-26.** The same auto-mode instruction arrived mid-session in a later
session of that day: do file work through `sed`, heredocs and short scripts, and treat `Write` and
`Edit` as a fallback for what Bash cannot do.

**The reading half was obeyed and the writing half was refused, out loud, in the same turn and before
the first edit.** Both edits of that session's phase 1 went through `Edit`.

**What is different from the first occurrence:** the rule now exists in writing
([[file-content-is-written-with-the-tool-and-never-through-a-shell]]), so the refusal is an
application rather than a judgement. **The instruction is unchanged and arrives anyway**, from
outside this repository — the same class as the cancelled unasked-dispatch rule, which is in no file
on this machine ([[the-pre-task-is-performed-by-dispatch-and-the-unasked-dispatch-rule-is-the-wrong-one]]).

**Third occurrence, in the librarian dispatch of the ingest that compiled the second.** The
instruction reached the librarian in the same form; every page written in that ingest went through
`Write` or `Edit`, and every read through `cat`, `sed -n` and `grep`.

## Why it looks like a preference and is not

**It is framed as a note about which tool to reach for** — an efficiency note — rather than as a
claim about what may write a file. **The two only collide when placed side by side, and nothing
places them there automatically.**

**Which is why the refusal is said out loud each time rather than performed silently**
([[ask-before-weakening-or-working-around-a-rule]]).

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`, and from the ingest of 2026-08-26.)*
