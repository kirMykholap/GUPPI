---
title: "A loss measured between different quantities is not a loss, and the first report of one was wrong"
type: lesson
status: archived
authority: mismatched-quantity-comparison
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [testing, process, harness]
---

# What was reported and what was true

**Reported:** the guard's delivery drops 248 characters when HTML comments are stripped, and that
may be content loss.

**What was compared:** the hook's **whole JSON output** against the `additionalContext` **alone**.
Different quantities. The difference between them is the JSON envelope, which was never rule text.

**Measured properly:** **971 bytes on disk against 940 delivered**, and a line-by-line diff showing
**exactly one line missing — the comment itself.** `<!--` is present in the source and absent from
what is delivered.

# Why the wrong reading was believable

**The number was real, the subtraction was correct, and the direction was right** — comments were
being stripped, and something did get smaller. Everything about the report was true except what the
two numbers were measurements *of*.

**That is the property that makes this family hard**: the instrument answers a different question
and the answer is well-formed ([[the-evidence-was-not-wrong-the-instrument-was-too-coarse]],
[[grep-with-an-escaped-cr-returns-a-line-count-and-not-a-cr-count]],
[[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]).

# What settled it, and it is the cheap move

**A line-by-line diff, not a byte count.** A count says *something changed*; a diff says *what*. The
diff took one command and turned an open question about content loss into a closed one with a name:
one line, and it is the comment.

**The rule:** before a difference between two numbers is reported as a loss, say what each number
counts. If the two sentences are not the same sentence with a different date, the difference is not
a loss ([[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

# What it was load-bearing for

**The *generated, do not edit* banner was ruled free on the strength of comments being stripped**
([[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]). Had the guard delivered
comments verbatim, the banner would have been spent on every edit of every governed file — the
banner's whole cost argument, quietly reversed by the mechanism built to serve it.
