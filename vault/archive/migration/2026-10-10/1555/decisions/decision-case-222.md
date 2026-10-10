---
type: decision
case: "222"
status: archived
update: ["[[insight-ledger-hi-tied-to-its-session-by-position]]", "[[insight-ledger-hi-tied-to-its-session-by-position]]"]
supersedes: ["[[decision-case-205]]", "[[decision-case-192]]"]
origin: raw/2026-09-16/2238/ledger.md#case-222
sprint: migration
created: 2026-09-16
tags: [harness, hooks, ledger]
---

## Context

`ask-guppi` read the Spec against the vault at pre-task and found seven places that contradict a rule or the code: the refusal of 211.2 would hit three entries of this same yaml without `set.method` (209.5, 209.6, 211.1); 209 promised a position among `children` that `generate` does not give; 209.2 promised a `make lint` exit 0 unreachable while the sprint page's own Estimates stand unread; a line of 213.3's Criterion said the hook does not change beside 213.2 which changes it; 213.4 set the Insight `actioned` and left its `deferred_by` of 192 and 205, which the brief would keep listing; 211.3 counted `unmigrated` 37 where the run gives 34; 210 edited pages by hand where `index.md` §1 says the scripts are the only writers to `wiki/`, with a History line ending in no pointer. Each is amended in place in the Spec above. 213.1 and 221 replace the Criterion of `estimate-prespec-checks-the-plan` twice in one plan; the later text contains the earlier and applies last — known, not changed.

## Problem

The `deferred_by` of the Insight is cleared only by a `supersedes` of the deferring Case, one Case per line; 213.4's line carries none.

## History

- 2026-09-17 created · raw/2026-09-16/2238/ledger.md#case-222
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
