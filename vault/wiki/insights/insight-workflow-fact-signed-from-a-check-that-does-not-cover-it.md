---
type: insight
pattern: "A fact is signed — in a Case, in a reading, in a ledger line — on a check narrower than the claim: the command that ran answered one question and the sentence it supports makes a wider one, while the wider check was one more command away."
status: actioned
children: ["[[lesson-fact-asserted-from-a-partial-check]]", "[[lesson-ledger-estimate-line-carried-a-count-not-read]]", "[[lesson-case-context-claim-wider-than-its-search]]", "[[lesson-case-context-bookkeeping-written-from-memory]]"]
severity: 0
addressed_by: "[[decision-case-388]]"
origin: raw/2026-09-22/2046/ledger.md#L21
sprint: migration
created: 2026-09-22
tags: [workflow, ledger, session, tests]
---

## Pattern

Two lessons where the check that was made is narrower than the claim it was used to sign.

`lesson-ledger-estimate-line-carried-a-count-not-read`: the reading line of
`estimate-prespec-checks-the-plan` said "72 green in the file" after one combined pytest run
over three files; the per-file number was never printed and was split from memory.
`pytest tests/test_prespec.py` alone gives 52.

`lesson-fact-asserted-from-a-partial-check`: Case 348 was ratified on the claim that every
ledger line stands in `materialize.yaml`; what had been checked was that `line`, `text` and
`origin` exist on the entries the agent looked at. `vault/raw/2026-09-22/0014/materialize.yaml`
holds entries for lines 1–51, 58 and 60 of a 64-line ledger, with `unparsed` empty.

In both, the question put to the tool was about a sample or about a shape, and the sentence
signed was about a whole — a file's count, every line of a ledger.

## Proposal

A suggestion, not a decision.

A claim that enters a Case, a reading or a ledger line names the command its output rests on,
and is no wider than that output: a per-file count comes from a run of that file alone, a
combined run gives a combined number and nothing else.

A claim about a whole set — every line of a ledger, every entry of a yaml — is checked by a
count on both sides, not by the shape of the entries read. Where that check is a command, it
belongs in the Case's `tasks` as a reading; where it is not, the claim is written as what was
actually seen.

Neither half is decided here.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#L21
- 2026-09-23 updated: actioned by rule-agent-writing — a claim no wider than its check (case 359) · [[decision-case-359]]
- 2026-09-23 updated: synthesis: lesson-case-context-claim-wider-than-its-search added, the claim of a Case's context covered the whole vault while its grep covered a few phrases; reopened from actioned · raw/2026-09-23/1126/ledger.md#L42
- 2026-09-23 deferred · [[decision-case-380]]
- 2026-09-23 updated: synthesis: lesson-case-context-bookkeeping-written-from-memory added, the bookkeeping facts of a Case's context written from memory and none checked when the sentence was written · raw/2026-09-23/1355/ledger.md#L35
- 2026-09-24 defer by decision-case-380 superseded · [[decision-case-388]]
- 2026-09-24 updated: actioned: a fact of a context is checked by ask-guppi at pre-spec; the text rule of rule-agent-writing stays (case 388) · [[decision-case-388]]
