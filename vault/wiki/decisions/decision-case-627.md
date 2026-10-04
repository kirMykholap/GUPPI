---
type: decision
case: "627"
status: current
children: ["[[decision-case-627.1]]", "[[decision-case-627.2]]", "[[decision-case-627.3]]", "[[decision-case-627.4]]", "[[decision-case-627.5]]"]
origin: raw/2026-10-04/1439/ledger.md#case-627
sprint: migration
created: 2026-10-04
tags: [sprint, workflow, harness, render, schema, librarian]
---

## Problem

Nothing does the close of a sprint, and its four Estimates cannot be read: they wait for a close that waits for every reading, the sprint page's own included. The question is what this Case builds, what condition lets the close go ahead, and how its checks get read.

## Recommend

- **What does this Case build, and what does it leave to the Case on where the close runs?**
  - Recommended: (a) the tool here, the place there: one command, `guppi sprint-close`, marks the pages `archived` for `guppi cleanup`, with a preview that changes nothing; this Case changes the texts the moves make false; the next Case sets who calls it, when, and how the next sprint opens.
  - Answer: (a).
- **How do the four Estimates of the close get a moment when they can be read?**
  - Recommended: (a) a pytest test over a made-up vault and the preview over the live vault, read in this session, each Criterion replaced to name the command.
  - Answer: (b): each method gains the pytest test, the When and Then stay, and the reading by hand waits for a real close.
- **What does this Case do with the three Estimates of migration itself?**
  - Recommended: (a) leave them to the close; the preview lists them; the deferred decision on `entity-sprint-migration` stays open.
  - Answer: (a). The person added that if every Estimate had to pass at the close, the sprint could never close, since its own Estimates wait for the real close. So the close must be allowed with Estimates not passed, and this can change later. The mechanism is settled now, and the close itself runs later.
- **What must be true before the close moves any page?**
  - Recommended: (a) settled, not passed: each Estimate of the sprint page that has not passed is read now or archived unread with the sprint page, never carried; the text of `rule-sprint-close` and the When of the four Estimates change; their Then stays.
  - Answer: agreed.
- **How do your choices on pending Estimates reach the command?**
  - Recommended: (a) by slug on the command line, `--carry <slug>` and `--archive-unread <slug>`; an Estimate read now is read before the run; the run refuses while a listed Estimate has neither passed nor been named.
  - Answer: agreed.
- **What happens to a check of the synthesis that says an actioned Insight stays live for good?**
  - Recommended: (a) replace the Criterion of `estimate-synthesis-clusters` whole, so that an actioned Insight stays live until the close of its sprint; read again at the next librarian run with at least two lesson entries.
  - Answer: agreed.
- **Can an Estimate of the sprint page be carried into the next sprint?**
  - Recommended: (a) add the exception to the Then of `estimate-sprint-close-settles-unread-estimates`: an Estimate the sprint page lists is read now or archived unread.
  - Answer: agreed.
- **Change**
  - Asked: both changes. Read the four Estimates over the preview of the command on the live vault, beside a pytest test over a made-up vault, so that they are read in Work Mode and need not be carried at the close of migration. Close the gap of a reading that comes out `failed`: such an Estimate counts as settled, carried by `--carry`, or archived with the sprint page when the sprint page lists it, its status kept in the record of the close.
  - Taken: the When of each of the four names the run with `--apply` over the made-up vault of `tests/test_sprint_close.py` or the preview over the live vault. Each Then keeps its lines and gains one line on what the preview shows. Each method is a pytest test and a reading by hand of the preview of migration. The ledger hook refuses a reading of an Estimate that its own session updates (case 428.1), so the four are read in a later session, with no real close needed, not in this Work Mode. The Then of 627.4 gains the line on a failed reading. The rule's Purpose says that an Estimate of the sprint page that stands `failed` goes with the sprint page with no choice by name. The tests of `-k settle` gain the failed case.
- **Change**
  - Asked: in 627.1 only, the last sentence of the Purpose of `rule-sprint-close` points to the section `## How it works` that Case 628.1 writes on the same page, in place of saying that where the close runs and how the next sprint opens are not decided.
  - Taken: the last sentence of the Purpose now reads that these are set in `## How it works` of this page (case 628.1). The `given` of 627.1 names the case file of Case 628.
- **Does the change to the sprint page also close the question put off on it?**
  - Recommended: (a) close the question with this update: the decision line of this Case on `entity-sprint-migration` carries the mark that closes the deferred decision, which the settling step, the readings in groups and the four Estimates read without a real close answer; Case 628 carries the same mark; this Case changes only its own milestone line.
  - Answer: agreed.

## History

- 2026-10-04 created · raw/2026-10-04/1439/ledger.md#case-627
