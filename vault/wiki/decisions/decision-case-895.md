---
type: decision
case: "895"
status: current
create: ["[[estimate-case-build-goes-on-after-a-compaction]]"]
origin: raw/2026-10-28/1907/ledger.md#case-895
sprint: plugin
created: 2026-10-28
tags: [harness, hooks, case-build]
---

## Problem

The procedure the person chose for a full helper rests on facts about how a subagent compacts that the documentation does not settle. Building it before those facts are seen would likely need a second Case.

## Recommend

- **How do we stop the memory of the helper from growing?**
  - Recommended: (a) a new helper rebuilds a built Case; not (b), compaction by size, since whether the checks keep their records is not checked.
  - Answer: in the person's own words, `case-guppi` should watch its own context: a hook like the one of the main session warns past a size, and the question is what happens next.
- **What happens once the hook finds a helper past the limit?**
  - Recommended: (a) a new helper takes over the Case.
  - Answer: the person disagreed with that procedure: the helper should work on, and when the hook says its context is full, a procedure saves its work and passes it on. Replaced by the question how a full helper hands its work to a fresh one.
- **At what size is a helper past the limit?**
  - Recommended: (a) 200 000 tokens.
  - Answer: (b), 400 000 tokens, as in the main session.
- **How does a full helper hand its work to a fresh one?**
  - Recommended: (a) a handover file, then a fresh helper.
  - Answer: the person proposed to combine the hook and the compaction: the helper writes an interim Case and what is left to do, a compaction follows, and the same helper goes on. Replaced by the question whether the hook and compaction work together on the same helper.
- **Should the hook and compaction work together on the same helper?**
  - Recommended: (a) the hook asks for an interim Case, then compaction comes by size.
  - Answer: test the idea first, and build it if it works.
- **Where do the test and the build go?**
  - Recommended: (b) only the test now, the build in a later session.
  - Answer: agreed, (b).
- **How is the test run?**
  - Recommended: (a) the main agent runs it in a test folder, with no window.
  - Answer: agreed, (a).
- **When does the test run?**
  - Recommended: (a) in the Work Mode of this session.
  - Answer: agreed, (a).
- **What carries the test into Work Mode?**
  - Recommended: (a) a small Case: one new check on `rule-case-build`, met by the test.
  - Answer: agreed, (a).

## History

- 2026-10-28 created · raw/2026-10-28/1907/ledger.md#case-895
