---
type: decision
case: "921"
status: current
update: ["[[rule-skill-hi]]", "[[estimate-hi-takes-its-readings]]"]
origin: raw/2026-10-30/0304/ledger.md#case-921
sprint: plugin
created: 2026-10-30
tags: [session, harness, workflow]
---

## Problem

An Ask question at `/hi` that asks the person to judge a text names no place where the text stands and quotes none of it, so the person's answer and the reading line written on it can rest on another text than the one the Estimate means.

## Recommend

- **What should `/hi` say beside an Ask question that asks the person to judge a text?**
  - Recommended: (a) name the place, and quote the text when it is in a file; for a text shown only in the chat of an earlier session, name that session by its date and start time and the reply, and say that the agent cannot open that chat; the reading line names the same place.
  - Answer: agreed, (a).
- **Which page sets this: `/hi` alone, or also the writers of the Ask question?**
  - Recommended: (a) `/hi` alone; only `rule-skill-hi` changes.
  - Answer: agreed, (a).
- **How is the change checked?**
  - Recommended: (a) replace the Criterion of `estimate-hi-takes-its-readings`, its `purpose` with it; its `method` stands.
  - Answer: agreed, (a).
- **Do the words in `orchestration.md` on the form of an Ask question change too?**
  - Recommended: (a) leave them and their two Estimates as they are; `context` says why they stand.
  - Answer: agreed, (a).
- **Change**
  - Asked: on a finding of `/pre-spec`, the person agreed that when the question names no path, `/hi` looks for the text by a Grep or a Glob over the files of the repository, such as the brief, the handoff of the session and the page of the Estimate, never a saved chat; when it finds the text it names the path and the section and quotes it, and when it does not, it takes the text as one shown only in a chat; the Render and the Criterion name alike the step that opens the file.
  - Taken: the new Render and `then` say that the step that puts the `A` lines searches for the text and opens the file it finds; the `－` line on the pages opened names both steps and no saved chat; the `purpose` names the search.

## History

- 2026-10-30 created · raw/2026-10-30/0304/ledger.md#case-921
