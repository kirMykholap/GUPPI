---
type: decision
case: "693"
status: archived
update: ["[[rule-permissions]]", "[[estimate-permissions]]", "[[rule-morph]]"]
origin: raw/2026-10-06/1448/ledger.md#case-693
sprint: migration
created: 2026-10-06
tags: [harness, session]
---

## Problem

A search whose path is the saved transcripts folder itself still makes the client ask for permission, though the allow list was meant to let every search there run without a prompt.

## Recommend

- **Which search asked for permission**
  - Recommended: (a) the records folder if the prompt named the `.claude\projects` path, otherwise (c), treat the records folder as the cause.
  - Answer: (a), the records folder.
- **How a search of the records folder stops asking**
  - Recommended: (a) a second read rule for the folder itself, beside the present one.
  - Answer: agreed, (a); with the note that these allow rules name the person's own folders and system, so another install of guppi would need its own.
- **The allow rule on another person's machine**
  - Recommended: (a) the rule for this machine now; `context` and the Purpose of `rule-permissions` say that another install needs its own folder name, which waits for `rule-morph`.
  - Answer: agreed, (a).
- **How the fix is checked**
  - Recommended: (a) replace the Criterion of `estimate-permissions` so it names the folder itself and everything inside it, checked by the person's word in Work Mode of this session after the render.
  - Answer: agreed, (a).
- **Change**
  - Asked: at pre-spec, the live probe of `estimate-permissions` cannot run in Work Mode of this session, since a rendered file changes at the librarian's render after the session; the person chose that the probe runs in a session after the librarian's render, the Estimate staying `pending` until then.
  - Taken: the `method` of `estimate-permissions` names a session after the librarian's render and the person's word there.
- **Change**
  - Asked: at pre-spec, the `purpose` of `rule-morph` names only the category set, not the questions of the install; the person chose that this Case widens it to the name of the transcripts folder in the allow list.
  - Taken: an `update` of `rule-morph` widens its `purpose` and its Purpose, and the new text of `rule-permissions` says that its initiation at install sets the folder name.

## History

- 2026-10-07 created · raw/2026-10-06/1448/ledger.md#case-693
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
