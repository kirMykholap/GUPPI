---
title: "A file read in part was overwritten whole, and what stood in the unread part cannot be recovered"
type: lesson
status: archived
authority: partial-read-overwrite
basis: human
sprint: S2
created: 2026-08-22
sources: ["archive/2026-08-22/2026-08-22-the-pre-task-becomes-an-agent-and-a-prohibition-is-ratified/handoffs/2026-08-22-the-pre-task-becomes-an-agent-and-a-prohibition-is-ratified.md"]
tags: [process, harness]
---

# The incident, 2026-08-22

**A file the session had read only in part was rewritten whole.** The owner had twice referred to a
note he had left in that file — *там есть заметка в плане*, *комментарий в плане* — and it may have
been destroyed by the write. **Whether it was is unknowable**: the unread part was never read, so
there is nothing to compare the new file against.

**The loss is silent in both directions.** A partial read leaves the writer believing it knows the
file, and a whole write leaves no trace of what it replaced unless the file is under version
control — this one was not, because the plan lives outside the repository.

# The owner's ruling: it becomes a lesson, and no guard is built

**owner selected: overwriting a partially-read file becomes a lesson in the corpus.** Chosen against
a `PreToolUse` guard that refuses a `Write` to a file that was read only in part, and against
recording nothing at all.

**The refused guard is the interesting rejection.** It is buildable — the harness already carries a
`PreToolUse` branch on `Edit|Write` and the state to hang it on
([[the-guard-branch-lives-inside-a-hook-that-already-runs]]) — and it was still refused. What that
leaves is a rule an agent keeps rather than a mechanism that enforces it, which this store knows the
weakness of ([[knowing-a-rule-is-not-a-mechanism]]).

# What it teaches, since nothing enforces it

**A `Read` with an offset or a limit is not a read of the file.** It is a read of a window, and the
tool returns it without saying what it did not show. **A whole-file `Write` after a windowed read is
a write of the window plus whatever the writer imagined around it.**

**The safe move is the narrow one**: edit the span, do not replace the file. An `Edit` that fails
because its anchor is not what the writer thought is a message; a `Write` that succeeds because
nothing checks is not.

**And a file the owner has touched is not the session's to rewrite.** The specific loss here was not
a line of the session's own work — it was a note from the other party, in the one artefact he was
being asked to approve.

# A property of the channel, which is the other half of the same loss

**The plan-rejection channel delivered his rejection without his note.** He wrote a comment on the
plan; the text never reached the session, in the rejection or anywhere else, and the retro could not
close the line because there was nothing to read.

**So a note left there is not something a session can read.** That is worth knowing before relying on
the channel, and it means the same content has to arrive in chat to arrive at all
([[a-question-asked-is-not-a-question-answered]]).
