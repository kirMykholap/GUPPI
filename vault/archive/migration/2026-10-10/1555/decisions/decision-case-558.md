---
type: decision
case: "558"
status: archived
children: ["[[decision-case-558.1]]", "[[decision-case-558.2]]", "[[decision-case-558.3]]"]
origin: raw/2026-09-30/2042/ledger.md#case-558
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, librarian, render, ledger]
---

## Problem

The librarian's frame bans reads by a closed list, and its Estimate fails on any read outside it. The list keeps missing reads that the job needs, mostly for the brief, so the Estimate has failed five times in a row, each time on a read its work needed, and each fix only widened the list until the next run. The question was whether the promise gets softer, what the bans protect, and how a read that the frame did not foresee becomes feedback instead of a failure.

## Recommend

- **How strict the promise on reads stays**
  Recommended: (a) check only the bans; the list of reads stays in the frame as a guide.
  Answer: not answered; the person asked first why the librarian's reads are banned, and the later question on what a read outside the list does to `estimate-documentation-completes` replaced it.
- **Which of the four reads of the last run become allowed**
  Recommended: (a) all four; the ban covers the content of a page, not its name.
  Answer: not answered; the later question on what the ban on Decision pages and the archive covers replaced it.
- **Where the brief gets the facts that sent the librarian outside its list**
  Recommended: (a) a script prints the facts the brief needs.
  Answer: (b) the frame allows the reads the job needs: the librarian decides itself what it needs; if it is seen to spend too many tokens, the question is taken up again.
- **What a read outside the list does to `estimate-documentation-completes`**
  Recommended: (a) a read outside the list is a finding, not a failure; the Estimate fails only on a ban.
  Answer: (a), agreed; the next round widened it, so that no read fails once the librarian records it.
- **What the ban on Decision pages and the archive covers**
  Recommended: (a) the ban covers the text of a page, not its name.
  Answer: (a), with a correction: the Estimate does not fail when pages are read, since such a read is a finding that the librarian must record; the librarian's instructions speak of no hard ban, and ask it to say so when it needs a read of its own; this is the librarian's feedback on its frame.
- **How a read beyond the frame's list reaches the next session**
  Recommended: (a) the librarian writes each such read into Next session, `Cases`, of its brief.
  Answer: not a Case; it is closer to a flag or a lesson.
- **Where the librarian records a read outside its inputs**
  Recommended: (a) a line under Flags of the brief.
  Answer: (a), agreed.
- **Change**
  Asked: fix the findings of the second pre-spec run: the Purpose of `rule-materialize` says the ledger is not needed at all while the frame needs one read of it; the frame says the job does not need a search of the archive while it names the Glob by slug and a listing of the archive; the context misstates the state of Case 557.2 and the count of the lines not carried.
  Taken: the `purpose` and the Purpose of `rule-materialize` say the ledger beyond its one read and the Spec beyond its unticked lines; the frame says the job does not need a search of the text of the pages under `vault/archive/`; the context names the rebuilt 557.2 and counts five removed bans among the six lines not carried.

## History

- 2026-09-30 created · raw/2026-09-30/2042/ledger.md#case-558
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
