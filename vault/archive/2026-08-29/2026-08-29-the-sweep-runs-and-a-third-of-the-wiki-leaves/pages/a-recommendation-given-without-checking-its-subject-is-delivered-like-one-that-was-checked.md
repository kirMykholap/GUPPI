---
title: "A recommendation given without checking its subject is delivered exactly like one that was checked"
type: lesson
status: archived
authority: unchecked-recommendation
basis: measurement
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md"]
tags: [process, agents, retrieval]
---

# The incident, 2026-08-26

**Twenty-four recommendations were put to the owner in one sweep. Two of them were rubbish, and
nothing in how they were delivered said so.**

- **Build a `binding:` column into `scripts/vault-catalogue.sh`** — a script no skill and no agent
  calls. Zero mentions in `.claude/`, measured after his one-line question
  ([[the-catalogue-gains-no-binding-column-and-the-question-is-withdrawn]]).
- **Delete a VS Code setting that does not exist.** The extension has fifteen documented settings and
  none of them inserts text into a system prompt; two of them were glued together into a third
  ([[the-vs-code-extension-reads-its-starting-mode-from-user-settings]]).

**Both were stated with the same confidence as the twenty-two that survived.** The first fell to a
question, the second to a documentation lookup — neither cost more than a minute, and neither had
been spent.

# The lesson is about the delivery, not about being wrong

**Confidence is not a signal here, because it is uniform.** A recommendation whose subject was read
and one whose subject was assumed arrive in the same voice, in the same list, at the same length.
**The reader has no way to sort them** and pays the checking cost for all of them or for none.

**The same shape found two rubbish items on the ten-item carried list**, and both were found by
opening the pages rather than by reading the list: one item had been true on 2026-08-21 and stopped
being true when a rule region landed; the other named a page that had been closed three days earlier.

# What follows

**Check the subject of a recommendation before making it, or say that you have not.** The cost of the
check is a grep; the cost of not making it is the owner's time and a decision taken on a false
premise ([[the-owners-question-was-how-would-you-check-that]]).

**The narrow cousin of this failure is a hand-typed number or date**, which nothing reads and which
arrives with the same authority as one that was measured
([[a-date-typed-into-a-docstring-is-a-measurement-and-goes-wrong-silently]]).

# It happened twice more on 2026-08-27, and both were delivered as checked

**A claim that `wiki/entities/vault-archive-sh.md:69` carries a live "built and wired to nothing".**
The sentence is past tense, under a heading naming the caller the script gained on 2026-08-21, and is
correct as written. The recommendation to repair it was issued without opening its subject
([[vault-archive-sh]]).

**And a count of the `*(Compiled from …)*` signature taken with a looser pattern than the literal**,
reported as 100 files / 89 under `wiki/` / 128 occurrences against the true 96 / 88 / 118. The grep
matched `Compiled from` without the opening bracket and caught prose *about* the signature
([[a-figure-measured-over-one-folder-was-reported-as-a-reading-of-the-corpus]]).

**Both were the session's own findings about the corpus, and both were corrected by the session
itself in a later turn.** The lesson is unchanged and the instances are added because the class is
recurrent rather than historical.
