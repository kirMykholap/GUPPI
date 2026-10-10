---
type: decision
case: "302.2"
status: archived
update: ["[[rule-synthesis]]", "[[estimate-synthesis-keeps-actioned-by-the-mark]]", insights-schema]
origin: raw/2026-09-21/1853/ledger.md#case-302.2
sprint: migration
created: 2026-09-21
tags: [harness, workflow, librarian]
---

## Context

The lesson L3 of session 1315 was written, and in the same session 296 closed its cause: the line of 296 carries `{addresses:…}`, `materialize` puts `addressed_by: decision-case-296` on the lesson's entry (284.3). The librarian, at synthesis, finds a second lesson with the same cause (0958) and by the rule creates an Insight `open`, severity 2. The synthesis rule knows the mark in one case only — the lesson falls under an Insight that already exists and is `actioned`: it stays `actioned`, `addressed_by` moves to the decision (284.4, `estimate-synthesis-keeps-actioned-by-the-mark`, `pending`, no date). The case "an Insight is born from a marked lesson" is not in the rule — so it is born `open`, goes to the brief's Deferred, to the Frontier and into a Case, although the decision that closed the pattern is named on the lesson's entry. No change of mechanism is needed: `generate` sets every new Insight `open` (`INITIAL_STATUS`), and the librarian already appends the `update` of each lesson — one more `update` of the new Insight in the same yaml, `set: {status: actioned, addressed_by}`, applies right after the `create`; the cascade archives the `clustered` children. The Proposal of the Insight — a check in pre-spec and a flag of the librarian — is read no further: the pattern is closed by 296, the Case schema (294), `estimates/schema.md` and §7 (297) name the form, the readings W1–W4 of this session confirmed it. The pages: the Insight `open`, both lessons `clustered`; `rule-synthesis` `draft` (its Render a partial of `.claude/agents/librarian-guppi.md`); of its two Estimates the Case touches `estimate-synthesis-keeps-actioned-by-the-mark`, not `estimate-synthesis-clusters`; `insights/schema.md` a Rule-class file, by hand, the `status` row; §8 of the index and the glossary do not contradict and are not touched.

## Problem

Close the Insight as solved by 296, and close the gap by which every cause cured in its own session costs a Case of the next one.

## History

- 2026-09-22 created · raw/2026-09-21/1853/ledger.md#case-302.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
