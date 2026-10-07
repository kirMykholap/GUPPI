---
type: decision
case: "711"
status: current
children: ["[[decision-case-711.1]]", "[[decision-case-711.2]]", "[[decision-case-711.3]]", "[[decision-case-711.4]]"]
origin: raw/2026-10-07/0636/ledger.md#case-711
sprint: migration
created: 2026-10-07
tags: [hooks, harness, workflow, session, librarian]
---

## Problem

A pair is signed against the page as it stands, not as the earlier Cases of the session leave it, and nothing makes `case-guppi` read the sentence around a match or the new text of another Case in the same sentence. The fault is found at `/pre-spec`, after the person approved the Case.

## Recommend

- **Should the check of a Case file apply the other Cases' pairs first?**
  - Recommended: (a) apply the other Cases' pairs first and those of the file last, by `check_pairs`, so an old text that then misses or matches twice goes back to `case-guppi`.
  - Answer: agreed, (a).
- **What happens when two Cases change the same sentence?**
  - Recommended: (a) a note sent back once, naming the other Case, the page and the start of the sentence; a sentence runs to a full stop followed by a space and a capital letter, or to the end of its paragraph.
  - Answer: agreed, (a).
- **Should my own instructions repeat the rule on reading the whole sentence?**
  - Recommended: (c) a script checks the read: a pair whose sentence came back whole from no read of the page file in the record of `case-guppi` goes back to it; a search result does not count.
  - Answer: agreed, (c), after the person asked whether the check could be made by a script.
- **One promise or three?**
  - Recommended: (a) three sub-cases, each with a new Estimate read by `tests/test_casecheck.py`.
  - Answer: agreed, (a).
- **Does the read check cover a word swapped across the vault too?**
  - Recommended: (a) both `replace` and `reword`, every match.
  - Answer: agreed, (a).
- **What counts as a read when my old words stand in another Case's new text?**
  - Recommended: (a) a read of the other Case's file whose output holds that Case's new text.
  - Answer: agreed, (a).
- **What happens to the item's page once these checks are approved?**
  - Recommended: (a) the same Case sets it `actioned`, its decision named as the one that acted on it.
  - Answer: agreed, (a).
- **Change**
  - Asked: the findings of `/pre-spec`. Name the tag check of Case 703.1 as a second exception where the Purpose of `rule-case-check` says the checks of a Case are those of pre-spec and of the Spec hook. Write `addressed_by` as a quoted wikilink, as `rule-insights-schema` sets it, unless the check of the Case file refuses a link to a decision of this session. Let `case-guppi` read the case file of a Case that the check of its file names in a finding or a note, by an update of `rule-case-build` (the person agreed, option (a)). Name `estimate-prespec-catches-an-indent-added-twice` and say why it stands. Confirm or fix the notes on the `then` lines that 711.3 shares with 711.2.
  - Taken: 711.3 names the tag check in its new wording, and its `given` names `case-703.md`. `addressed_by` stays bare, since the check refused the quoted wikilink, and the `context` gives the refusal. The new Case 711.4 updates `rule-case-build` and replaces the Criterion of `estimate-case-build-checks-the-finished-case`. The `context` names the indent Estimate and says why it stands. The shared `then` lines stay, and the `context` says why. The finding of 711.3 also names the file of the other Case.

## History

- 2026-10-07 created · raw/2026-10-07/0636/ledger.md#case-711
