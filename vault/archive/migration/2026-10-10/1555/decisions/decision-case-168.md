---
type: decision
case: "168"
status: archived
update: ["[[rule-brief]]", "[[insight-librarian-frame-omits-required-reads]]"]
origin: raw/2026-09-15/1448/ledger.md#case-168
sprint: migration
created: 2026-09-15
tags: [harness, workflow, librarian]
---

## Context

`insight-librarian-frame-omits-required-reads` is the pattern "the frame of the librarian names the reads one by one, and the list is shorter than the judgments"; Case 143 closed it as `actioned`: the four reasons of the frame are one clause per judgment, nine runs without a recurrence. The librarian of session Q reopened it with a third lesson, `lesson-brief-next-section-has-no-source`: the Render of `rule-brief` gives a source to four of the five sections of the brief, and none to "What the next session does first". The librarian then copies the section from the previous brief and strikes nothing off: the reading of `estimate-brief-written` (124.1) stood in the section through three briefs after it passed. The brief of this session was built the same way — from the "Not done" of the handoff and the state after the run — but the rule does not ask for it. The Insight stands first in the Deferred list, severity 1.

## Problem

Accept the librarian's clustering — a section without a source is the same gap of the frame — and close the Insight with the fix; or reject it and leave the lesson on its own. And what the section is for: the owner wants a section that names the Estimates left to read.

## Given

`rule-brief` (`built`, `render` → `.claude/agents/librarian-guppi.md`, `estimates: [estimate-brief-written]`, `passed` on 124.1): in the Render "Where things stand" is sourced from the "What actually got done" of the handoff, which holds "what is not done", and the counts of the yaml; Deferred, Flags and Readings at the close have their sources; "What the next session does first" has none.
**＋** "Readings at the close" already lists the `pending` and `failed` Estimates by slug; the Spec of the session carries one `- [ ] read …` line per reading with the place and the way.
**＋** `insight-librarian-frame-omits-required-reads`: `open`, `severity` 1, `addressed_by: decision-case-143`, three children — two in the archive, `lesson-brief-next-section-has-no-source` `clustered`; History: reopened 2026-09-15.
**＋** `generate`: an `update` of an Insight with `status: actioned` goes as any update; the cascade archives the `clustered` children and recounts `severity`.
**＋** The model of 143: `set: {status: actioned, addressed_by: decision-case-143}`.
**－** `rule-skill-hi` assembles the Frontier from the whole brief — unchanged; the other rules that name a read are unchanged.

## Criterion

- [[estimate-brief-written]] § case 168

## History

- 2026-09-15 created · raw/2026-09-15/1448/ledger.md#case-168
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
