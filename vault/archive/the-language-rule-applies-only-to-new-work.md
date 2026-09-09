---
title: "English is the rule for new work only: what predates 2026-08-05 stays Russian and is not mass-translated"
type: decision
status: deprecated
authority: language-scope
basis: human
sprint: S0
decided: 2026-08-05
created: 2026-08-14
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "CLAUDE.md"]
tags: [process, testing]
superseded_by: [[english-is-the-rule-and-the-russian-past-is-deferred]]
---

# The language rule has a boundary, and the boundary is a date

> [!WARNING] DEPRECATED 2026-08-15
> **There is no boundary any more.** The owner withdrew the "new work only" clause on 2026-08-15 —
> he had added it because he did not want to deal with the rest at the time, and in that form it
> had gone stale. What predates 2026-08-05 is **deferred, not exempt**:
> [[english-is-the-rule-and-the-russian-past-is-deferred]], with the size measured on
> [[migrating-the-repository-to-english]]. **Nothing below changed in practice** — nothing is
> mass-translated, no test is renamed — and the two reasons against a translation pass are carried
> forward verbatim. Kept because "why did this repository once treat its own past as another
> language, and what ended that" is a real question, and because the `elsewhere:` reading in the
> last section is corrected on the successor rather than removed here.

**English for everything written into the repository** — code, identifiers, docstrings, comments,
test names, `docs/`, commit messages, plans, specs, and any brief or report handed to a subagent.
Russian only for chat with the owner and for what he sees while using the tool: the web page and
the CLI output are **product content, not documentation**
([[statuses-stay-english-identifiers]] for the one case that looks like an exception and is not).

**The rule applies to new work.** Everything written before **2026-08-05** is in Russian — *38
source files, 263 test names*, the plans and the specs.

- **Do not mass-translate it.**
- **Do not rename existing tests.**
- **When you substantially rewrite an existing docstring or comment for other reasons, write the
  new text in English.**

The migrated handoff carries the same rule in its own voice, as a note to the reader: *"sections
1–8 predate that rule and stay in Russian until something substantially rewrites them. Do not
mass-translate them."*

**Rejected, by implication and by repetition:** a translation pass. Renaming 263 tests produces a
diff nobody can review, breaks every reference in the older plans, and buys nothing a reader of
this codebase needs — the tests are read by the person who wrote them and by agents that do not
care which language a name is in.

## Why this page exists, and what it says about `elsewhere:` verdicts

**This rule had no page until 2026-08-14, and for one day it had no home at all.**

The migration of 2026-08-13 gave the unit carrying it the verdict
`elsewhere:CLAUDE.md — the language rule, and the ban on mass-translating what predates it`. That
was correct then. On 2026-08-14 `CLAUDE.md` was cut to a map and four rules
([[claude-md-is-a-map-and-four-rules]]), the paragraph went with the rest of the language section,
and **nothing anywhere held it** — the ingest that followed found it by reading every removed block
against the page that was supposed to carry it.

The general form is on [[the-verdict-is-the-write]]: an `elsewhere:` verdict is a claim about a
file **the vault does not own**, and nothing re-checks it when that file changes.
