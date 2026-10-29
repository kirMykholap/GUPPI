---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/ratified.py, .guppi/guppi/ledger.py, .guppi/guppi/casecheck.py, .guppi/tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-reconcile-refuses-an-edit-of-the-plan]]", "[[estimate-spec-reconcile-refuses-a-case-file-another-agent-holds]]"]
origin: raw/2026-09-23/1859/ledger.md#case-387.3
sprint: migration
created: 2026-09-23
tags: [hooks, harness, workflow, session]
core: true
---

## Purpose

Prevents a ratified Case from changing in what the scripts apply without the person seeing it whole and ratifying it again. The hooks alone write the Cases into the plan (since case 441): the `Stop` hook of `rule-spec-write` writes the text of the file of `case-guppi` that `rule-case-check` stored, and a Case changes only through its `case-guppi` and a new ratification. The agent writes only the title line that creates the plan, and a hook refuses any other edit of it, and any edit of the file of a built Case that the person is sent, before it lands, unless `case-guppi` makes it and no other agent holds the number of that Case (cases 453, 645.3, 650.1; a comparison with a ratified copy stood here from case 387.3 to case 445.1).

## History

- 2026-09-24 created · [[decision-case-387.3]]
- 2026-09-24 estimate estimate-spec-reconcile-shows-a-changed-case added · [[decision-case-387.3]]
- 2026-09-24 status: draft → built · cascade
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 deferred · [[decision-case-412]]
- 2026-09-25 defer by decision-case-412 superseded · [[decision-case-414.1]]
- 2026-09-25 deferred · [[decision-case-416]]
- 2026-09-25 defer by decision-case-416 superseded · [[decision-case-419.2]]
- 2026-09-25 deferred · [[decision-case-423]]
- 2026-09-27 defer by decision-case-423 superseded · [[decision-case-445.1]]
- 2026-09-27 updated: the guard refuses the agent's edits of the plan and its store, the title line that creates the plan excepted; the comparison with the ratified copy goes (case 445.1) · [[decision-case-445.1]]
- 2026-09-27 ref `estimate-spec-reconcile-shows-a-changed-case` → `estimate-spec-reconcile-refuses-an-edit-of-the-plan` · [[decision-case-445.1]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 updated: the guard also refuses the agent's edit of a file under the cases/ folder of a session folder, judged by one function of guppi/casecheck.py (case 453) · [[decision-case-453]]
- 2026-09-27 status: draft → built · cascade
- 2026-10-05 updated: the guard lets case-guppi alone write under cases/, and refuses case-guppi anywhere else (case 645.3) · [[decision-case-645.3]]
- 2026-10-05 status: built → draft · cascade
- 2026-10-05 estimate estimate-spec-reconcile-refuses-a-case-file-another-agent-holds added · [[decision-case-650.1]]
- 2026-10-05 updated: the first write of case-guppi on the file of a Case holds its number in the store, and a write of another case-guppi on that file is refused with a free number (case 650.1) · [[decision-case-650.1]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the history of the guard stands in the brackets of its pointers · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-26 updated: the old comparison stands in the bracket of its cases · [[decision-case-881.14]]
- 2026-10-28 updated: the guard writes the file of case-guppi itself and stops the call, so no permission prompt comes in Plan Mode (case 894.1) · [[decision-case-894.1]]
- 2026-10-29 updated: the hook writes any file of case-guppi under cases/, its working note included (case 896.2) · [[decision-case-896.2]]
- 2026-10-29 updated: How it works removed by hand, a one-off, its facts in the docstring of .guppi/guppi/ratified.py; the clause on the old path of rule-case-check dropped · [[decision-case-904.1]]
