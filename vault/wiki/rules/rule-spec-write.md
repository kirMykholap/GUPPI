---
type: rule
kind: Leaf
purpose: Prevents a ratified Case from entering the Spec in other words than the Case case-guppi wrote into its file, whose given, when, then, tasks and ratification the person signed and the check of rule-case-check stored
status: draft
enforcement: hook
implementation_ref: [.guppi/guppi/ratified.py, .guppi/tests/test_ratified.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-write-copies-the-ratified-case]]", "[[estimate-spec-write-checks-the-written-case]]", "[[estimate-spec-write-writes-a-defer]]", "[[estimate-spec-write-reaches-the-approved-spec]]", "[[estimate-spec-write-removes-a-superseded-case]]", "[[estimate-spec-write-exits-2-on-an-error]]", "[[estimate-spec-write-answers-a-refusal]]", "[[estimate-spec-write-refuses-a-changed-case-file]]", "[[estimate-spec-write-tells-each-reason-once]]", "[[estimate-spec-write-reads-a-new-tag]]", "[[estimate-spec-write-copies-a-built-defer-only-case]]", "[[estimate-spec-write-writes-the-map]]", "[[estimate-spec-write-shows-the-map-in-the-plan-view]]", "[[estimate-spec-write-rebuilds-the-maps-of-the-spec]]", "[[estimate-spec-write-map-follows-the-ticks-of-the-scripts]]"]
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [hooks, harness, workflow, session]
core: true
---

## Purpose

Prevents a ratified Case from entering the Spec in other words than the Case `case-guppi` wrote into its file, whose `given`, `when`, `then`, `tasks` and `ratification` the person signed and the check of `rule-case-check` stored. `case-guppi` writes the whole Case in the documentation language, and a hook copies its stored answer. The hook writes each Case not into the plan file, which the person approves at the exit of Plan Mode, but into the Cases file `<plan stem>.cases.md` beside it, outside the repository, so that the plan file holds its title line and the map alone; in the texts of the harness the plan is the plan file with its Cases file, and each reader of the Cases of the plan reads the plan file and then its Cases file, by `plan_cases_text` of `.guppi/guppi/ledger.py`, or, where it holds the plan text already, by `with_cases` of the same module, which `plan_cases_text` calls. The same hook opens the plan file, under its title line, with a map of the Cases of the plan, rebuilt at each run that writes, places or removes a Case: a table of the top-level Cases with their stops and their checks, a Mermaid diagram of the Cases in order, and one entry per Case and sub-case whose lines take their words from the Case, with a box before each task line, ticked as the line with the same text in the same Case of `spec.md` is ticked once that file stands, and a sign after the box of each open stop and each open check; each box stands indented under the entry of its Case, so no line of the map starts with a box at its first character or with a Case heading and none is `## Deferred`, no reader of the Cases sees it and a Case placed in `spec.md` after the approval goes before the `## Deferred` of its document, never into the map, and `uv run --project .guppi guppi ratified --map <file> --session <stamp>` prints the map of the Cases of a file and of the Cases file beside it. The map at the head of each approved document of `spec.md` that holds one is rebuilt in the same way from the Cases of that document: at each run of this hook that writes, places or removes a Case or a defer there; after each edit of the file by the agent, by the hook `uv run --project .guppi guppi ratified --boxes` that runs after the edit and that rebuilds the map of the plan file too when the file is the `spec.md` of the session; and at each tick of the scripts of the librarian's run; a document with no map gets none, and the line that opens each map of spec.md says that each box copies the box of its task line below and is no task of its own, while the line that opens the map of the plan file names its Cases file, where those task lines stand.

## History

- 2026-11-28 shipped with GUPPI
