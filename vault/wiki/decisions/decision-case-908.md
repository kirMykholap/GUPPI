---
type: decision
case: "908"
status: current
children: ["[[decision-case-908.1]]", "[[decision-case-908.2]]", "[[decision-case-908.3]]"]
origin: raw/2026-10-29/1930/ledger.md#case-908
sprint: plugin
created: 2026-10-29
tags: [harness, session, workflow]
---

## Problem

Two shipped checks hold a sentence that is false in a project that installed GUPPI: one names GUPPI's own transcripts folder, the other names Russian as the language of the chat, and a third check, of how a built Case is shown, names Russian too. The other four under the same defer wait, since a replaced Criterion would hold their rules `draft` for a long time.

## Recommend

- **Which checks this Case rewrites**
  - Recommended: (a) the six of the defer; the glossary check keeps its text, since this session's reading did not list it.
  - Answer: agreed, (a).
- **When the new texts come in**
  - Recommended: (b) now only `estimate-permissions`, read at the Retro of this session, and `estimate-orchestration-forwards-a-discussion-question`, whose rule is already `draft`; the other four keep their text under the defer.
  - Answer: agreed, (b).
- **When the discussion-question check is read**
  - Recommended: (a) the `method` names its event: by hand, after a question of the person to discuss an item.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the allow list holds one Read rule for all the paths under the transcripts folder, not one per path.
  - Taken: the first `then` line of Case 908.1 says a Read rule for the paths under it.
- **Change**
  - Asked: at `/pre-spec`, the Render on the page of `rule-orchestration` names the language by a placeholder; only the rendered file holds Russian.
  - Taken: the `context` states that fact.
- **Change**
  - Asked: at `/pre-spec`, the discussion-question check is read at the Retro of a session that holds such a question, from the tool calls of that session, since `/hi` reads no transcript of an earlier session.
  - Taken: Case 908.2 sets its `method` so.
- **Change**
  - Asked: at `/pre-spec`, `estimate-orchestration-shows-the-built-case` names Russian as the chat language too; add a sub-case that replaces its Criterion whole, with no change of status.
  - Taken: Case 908.3 replaces it with the chat language named by role.

## History

- 2026-10-29 created · raw/2026-10-29/1930/ledger.md#case-908
