---
type: decision
case: "668"
status: current
create: ["[[estimate-synthesis-reads-the-status-its-yaml-sets]]"]
update: ["[[rule-synthesis]]", "[[entity-glossary]]"]
supersedes: ["[[decision-case-663]]"]
origin: raw/2026-10-05/1616/ledger.md#case-668
sprint: migration
created: 2026-10-05
tags: [harness, workflow, librarian, session]
---

## Problem

The rule of synthesis does not say whether an Insight that a decision entry of the lesson's own `materialize.yaml` sets `actioned` counts as `actioned` for a lesson that joins it. As a result, a lesson with no mark can join such an Insight with no reopening and go to the archive, as if a decision had closed its cause.

## Recommend

- **Which status the librarian reads when a lesson joins an Insight**
  - Recommended: (a) the status after the run's decisions: an Insight counts as `actioned` when it stands so on disk or when a decision entry of the same run sets it so; an unmarked lesson reopens it, a marked one keeps it `actioned`, and the brief reports the reopening.
  - Answer: agreed, (a).
- **The Insight this already happened to**
  - Recommended: (a) leave the Insight `actioned` and the lesson archived; the Case says why in its `context`.
  - Answer: agreed, (a).
- **The glossary row on the status of an Insight**
  - Recommended: (a) the row names the mark, and says that an Insight a decision of the same run sets `actioned` counts as `actioned`; the glossary file is rebuilt.
  - Answer: agreed, (a).
- **How the change is checked**
  - Recommended: (a) a new Estimate, `estimate-synthesis-reads-the-status-the-run-sets`, read by hand after the first run in which a lesson joins an Insight a decision of the same run sets `actioned`; `estimate-synthesis-keeps-actioned-by-the-mark` stands with its result.
  - Answer: agreed, (a).
- **Change**
  - Asked: at /pre-spec, whether the scope is the lesson's own yaml, that is its own session, or every yaml of the librarian run; the person chose the lesson's own yaml.
  - Taken: every text of the Case says a decision entry of the same `materialize.yaml`, the lesson's own session: the name, `problem`, the glossary row, the new Estimate, renamed `estimate-synthesis-reads-the-status-its-yaml-sets`, and its `purpose`; its `method` names the kind of run, not the first one.

## History

- 2026-10-05 created · raw/2026-10-05/1616/ledger.md#case-668
