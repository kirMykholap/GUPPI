---
title: "The acceptance questions the vault must answer, and the run of 2026-08-14 that was the first honest one"
type: entity
status: current
authority: acceptance-instrument
basis: measurement
sprint: S0
created: 2026-08-14
sources: ["docs/superpowers/plans/2026-08-13-acceptance-questions.md", "archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md"]
tags: [vault, retrieval, testing]
---

# The instrument, and what it has actually shown

`docs/superpowers/plans/2026-08-13-acceptance-questions.md` holds five questions and, **written in
advance, the answers they should produce**. It is the only check this store has on *fidelity* —
whether a compiled page still says what its source said — because coverage cannot reach that
([[ingest-is-units-and-verdicts]]).

## The run of 2026-08-14: five questions, five PASS

Q1–Q4 were dispatched as **four parallel `vault-librarian` agents**; Q5 was the owner's own
question and went through `/vault-ask`.

| | Question | What it showed |
|---|---|---|
| Q1 | the batch finaliser | every expected element, plus the bonus that the startup sweep closes only `started_by='web'` batches; drew the `load_state` consequence unprompted, and read the *no test guards this rule* gap off the page — **a gap the first run had found as negative space and which had since been compiled into it** ([[batch-lifecycle]]) |
| Q2 | agent round-trip cost | the number, its provenance, and the boundary that makes the answer complete: 5–35 minutes describes *implementer* trips ([[agent-round-trip-cost]]). Also produced the six-hours finding |
| Q3 | JavaScript, asked in Russian | the narrowed rule, the honest reason, and the owed AST test ([[javascript-policy]]) |
| Q4 | a React rewrite, asked in Russian | the island rule and its single condition, **and the required negative space**: no decision about a wholesale rewrite exists, and making one would have to *supersede* [[the-stack-stays-htmx]] rather than sit beside it, because `authority: frontend-stack` is already claimed |
| Q5 | "what pages were planned in this project?" | two pages plus the shell were the entire planned set; the resume editor and the AI interview are named only as examples of the island condition, not as a backlog; [[collection-features-deferred]] records a prediction that did not come true. Negative space: **no roadmap page exists at all** |

Q1 is the loop closing on a single item, visible end to end: negative space found by one run,
compiled into the page, and read back off it by the next.

## Why this run counts and the earlier ones did not

**The harness injects `CLAUDE.md` into a subagent as it stood at the *parent session's* start**
([[claude-code-config-loading]]), so every earlier run silently had the long file's explanations
sitting beside the corpus, and could not distinguish "the vault answered" from "the rule file did".
This run was made in a session that began **after** the file was cut, and four agents reported the
file they were holding independently — two by counting a transcription, two by matching heading
order and sampled phrases; all four found the 210-line post-`d30b317` version.

**That instrument expires with the session.** The next session's agents will hold the 110-line
file, so this particular confound is gone — but the general form remains: a test of what a document
supplies must run in a session that started after the document changed.

## Two things about it that are not fixed

- **It can be gamed by its own subject.** The file contains the expected answers, so an agent that
  greps for *"batch finaliser"* can hit it and produce a flawless run having read nothing of the
  vault. Every dispatch on 2026-08-14 carried an explicit prohibition and every agent reported
  compliance — **an instruction, not a mechanism**:
  [[an-instrument-that-contains-its-own-answers-can-be-gamed]];
- **the results are not in the file.** They exist in the journal of 2026-08-14 only. The file still
  shows Q5 as `_Open_` and carries no record of the run — including the confound removal, which is
  the whole reason the run mattered. **The designed instrument disagrees with the record**, and
  reconciling them is owed to whoever next opens it.
