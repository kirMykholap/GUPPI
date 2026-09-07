---
title: "A menu resolves to a state, and pressing stop counts as an answer"
type: concept
status: current
authority: menu-state-set
basis: code
sprint: S3
created: 2026-08-26
sources: ["archive/2026-08-26/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself/handoffs/2026-08-26-the-harness-half-is-built-and-the-owner-rules-how-the-vault-empties-itself.md", "scripts/session-dialogue.py"]
tags: [harness, process, retrieval]
---

# The four states, and the two questions that produce them

**`resolve_menus` in `scripts/session-dialogue.py` reads two things about a menu**: whether a
`tool_result` exists for it, and whether a later turn exists and whose it is. Those two questions
give four outcomes, not two:

| state | how it is recognised |
|---|---|
| answered by selection | a `tool_result` exists |
| answered in prose after an interrupt | no `tool_result`, and his turn follows |
| still open | no `tool_result`, and nothing follows |
| lost | no `tool_result`, and the session's own turn follows |

**An interrupt marker counts as his turn.** Pressing stop is an answer to the menu — a menu the
owner cut off has been decided, and counting it as unanswered would file a real ruling as a
question nobody replied to.

**`system` entries are stepped over.** A background-task notification arriving between the menu and
the answer is neither party speaking, and reading it as a turn moves an answered menu into `lost`.

# The population this correction ranges over is one

**Measured 2026-08-26 across 40 transcripts: 193 menus — 192 answered by selection, 1 answered in
prose after an interrupt, 0 still open, 0 lost.** The four-state defect fired **once** across every
transcript on disk.

**That does not make the split wrong; it makes it small.** The one case is a real ruling that the
three-state reading would have filed as unanswered, and the cost of the distinction is a function
and four counters. It is written here so that the next reader of the counters knows the shape of
the population before drawing a rate from it ([[agent-round-trip-cost]] is the standing example of
a figure that had to be fenced the same way).

# The same session found the opposite case, and it has no instrument

**Its own extract: 6 owner turns, 65 session replies, zero menus asked.** Every ruling of
2026-08-26 arrived in prose. `/retro` carries a line about a session whose every ruling arrived
through a menu; the mirror case has no line and nothing counts it
([[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]]).
