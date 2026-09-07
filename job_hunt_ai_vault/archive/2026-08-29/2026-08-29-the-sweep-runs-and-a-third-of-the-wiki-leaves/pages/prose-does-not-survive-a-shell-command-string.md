---
title: "Prose does not survive a shell command string, and the transport is the fault rather than the heredoc"
type: lesson
status: archived
authority: prose-transport
basis: measurement
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md"]
tags: [process, agents, harness]
---

# It fired twice in one session, seconds apart

**Once losing the heredoc that carried the retro file**, and once **executing a markdown code span as a
command** — `bash: line 9: span: command not found`, in the very command written to investigate the first
failure.

## The diagnosis, and it is a diagnosis rather than a guess

**Eight heredoc constructs were written to files and parsed. All eight parse cleanly.** Apostrophes,
backticks, em dashes, arrows, HTML comments, backslashes, and bodies of two hundred lines. **So heredoc
syntax is not the fault.**

**The fault is the transport.** The command reaches `bash` wrapped in quotes, and prose carrying backticks
or apostrophes is then either executed as command substitution or breaks the wrapping. The heredoc is
innocent; the layer that hands the whole command to the shell as one string is not.

**The first explanation offered was *"it stumbled over quotes"*, and that is the part worth keeping.** It
was a guess presented as a diagnosis, in a project whose standing question is *how would you check that*
([[the-owners-question-was-how-would-you-check-that]]). The measurement that replaced it took minutes and
changed the remedy completely: a guess about quoting would have produced more escaping, which cannot help.

## The remedy, and why it is not a script

**A script does not help, because the script is invoked by the same command.** Wrapping the write in
`scripts/write-prose.sh "<the prose>"` moves the prose into an argument, which is the thing that breaks.

So:

- **Prose is written with the file-writing tool**, never through a shell command;
- **a generator reads its input from a file**, never from an argument.

## Where it belongs, and the sibling already on the record

**This is a rule-page candidate by the admission test** — imperative, and no test can hold it
([[the-harness-is-compiled-not-maintained]]). It has not been written as one.

Its sibling is [[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]]: same layer, same cause, one
character. **Two instances of one failure in one repository, and the second was met while writing the first
down** — which is the pattern this store treats as evidence that a rule belongs in the harness rather than
in a reader's memory ([[no-rule-reads-a-harness-file]]).
