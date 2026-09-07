---
title: "A runbook that carries the nonce cannot be read by the thing being measured"
type: lesson
status: archived
authority: probe-instrument-contamination
basis: measurement
sprint: S2
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md"]
tags: [testing, harness, agents]
---

# The defect, found while running the probe it belongs to

`probe/RUNBOOK.md` states its own principle in one section — *"neither string is guessable, so 'I can
see it' cannot be confused with 'I inferred it'"* — and **defeats it two sections below**, by
prescribing that the subagent be told to *"report verbatim whether the string `PROBE-TEXT-4K7QX2` is
present in its context."*

**That brief puts the string in its context.** A subagent quoting it back has proven nothing, and the
probe's entire instrument is the unguessability of the nonce
([[an-instrument-that-contains-its-own-answers-can-be-gamed]]).

**What was run instead:** *read the target, then report any text that arrived with the read and is not
in the file* — naming no nonce, and leaving the subagent nothing to echo. It returned the rule file
verbatim ([[what-reaches-a-subagent-a-scoped-rule-does-and-an-html-comment-does-not]]).

# The same flaw reaches the main session, from the other direction

**Reading the runbook to learn how to run the probe hands the reader both nonces before the
measurement starts.** So the main session can never be its own clean instrument for the first probe,
and the hook log is the only honest observable there.

That is not a defect in the runbook's wording; it is a defect in **its existing as a document the
measurer reads.** A runbook is read by whoever runs the probe, and in a probe about what an agent has
in its context, the runner *is* the subject.

# The general shape

**An instrument's documentation is part of the subject's environment whenever the subject is a
reader.** Anything a human harness would keep in a sealed envelope — the expected answer, the control
value, the nonce — is delivered into the measurement by the ordinary act of preparing it.

**Two arrangements survive it, and the probe uses both:**

- **an observable outside the reader** — a hook writing a log file. The log cannot be contaminated by
  what the session read, because the session did not write it;
- **a brief that names nothing** — the subject is asked *what arrived that is not in the file*, never
  *did X arrive*. The nonce stays in the checker's hands.

**The rule to carry:** in an instrument for a reading agent, the answer key and the runbook are
separate artefacts, and the one that reaches the subject holds no answers
([[a-subagents-most-believable-sentence-is-the-one-to-measure]]).
