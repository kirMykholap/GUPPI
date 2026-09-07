---
title: "The librarian cannot see a recurring family from where the ingest stands"
type: concept
status: current
authority: librarian-repetition-blindness
basis: inference
sprint: S3
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read/handoffs/2026-08-24-the-feedback-line-is-spoken-and-the-floor-under-a-session-is-read.md", ".claude/skills/vault-lint/SKILL.md", "scripts/lessons-queue.py"]
tags: [vault, agents, process]
---

# The position, not the agent

**At an ingest the librarian writes one lesson at a time, inside the context of the session that
produced it, where the seventh instance looks exactly like the first.** It has no view of the six
before it, because nothing in that dispatch asks for one.

**It did not miss seven times; it stood seven times where the repetition is invisible.** The shell
quoting family reached seven pages that way, and the wrong repair would be to instruct the same
agent to try harder ([[knowing-a-rule-is-not-a-mechanism]]).

# The fix is a different dispatch, and the numbers say why a grep is not one

**`wiki/lessons/` holds 140 pages, 500,661 bytes, about 125k tokens whole**, median page 2.8 KB —
readable in one dispatch that carries no session context. **94 of the 140 are cited by neither a
rule nor a proposal**: 21 by a rule, 36 by a proposal, 46 in the union.

**And the existing lookup cannot find a family here.** There are **140 distinct `authority:` values
over 140 pages: not one family has ever held two lessons.** `bash scripts/vault-authority.sh --near`
matches on words, and the seven pages of the shell-quoting family share none
([[an-authority-register-on-the-model-of-the-tag-dictionary]]).

# Where it runs

**`/vault-lint` was already an agent dispatcher**, so the collector is a second brief to the same
`vault-librarian` and no second writer appears ([[one-librarian-behind-every-caller]],
[[parallel-librarians-break-the-one-writer-property]]).

**It runs before the audit dispatch**, because the audit is scheduled after the last write of what
it audits and this one writes `proposals/` ([[the-audit-is-dispatched-after-the-writes]]).

**Its worklist is arithmetic**: `uv run python scripts/lessons-queue.py` prints the lessons cited by
neither a rule nor a proposal and **does not group them**, because grouping is the judgement the
dispatch exists to supply ([[vault-scripts]]).

# No threshold was set, deliberately

> **owner: порог не назначаем, смотрим за работой агента и вносим правки если понадобится. Он сам
> себя может улучшать через lessons**

**How many witnesses make a family is left to the agent and watched rather than legislated**, and
the correction path he names is the corpus itself. *(Turn 38 of 2026-08-24, verified against the
extract rather than recalled — the first time this ritual could check an attribution against the
words ([[the-session-dialogue-extract]]).)*

# It has never been run

**Built 2026-08-24, executed never.** The first run is a session of its own, on the owner's
decision, and until then this page describes a mechanism rather than a practice.
