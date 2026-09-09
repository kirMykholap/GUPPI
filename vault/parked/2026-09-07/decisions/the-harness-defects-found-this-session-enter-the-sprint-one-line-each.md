---
title: "The harness defects found this session enter the sprint, one line each"
type: decision
status: current
authority: harness-defect-scheduling
binding: deferral
basis: human
sprint: S3
decided: 2026-08-24
created: 2026-08-24
sources: ["archive/2026-08-24/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause/handoffs/2026-08-24-the-suite-learns-to-list-itself-and-every-proposal-names-its-cause.md", "sprint.md"]
tags: [harness, process, vault]
---

# The ruling, 2026-08-24

**Three defects found this session go onto the sprint as work rather than being fixed in place**, on
the owner's decision:

- **the `PreToolUse:Edit` hook is excepted for `wiki/*/_schema.yaml`** — it warns about the vault's
  single writer over files a decision puts in the session's hands, so its net is wider than the rule
  ([[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]]);
- **the vault's own `CLAUDE.md` loses its obligation to regenerate `catalogue.md`** — the file was
  deleted, `pages.base` replaced it, and the gate rule that checked it is retired
  ([[pages-base]], [[the-catalogue-is-generated-not-maintained]]);
- **`scripts/session-dialogue.py` gets three menu states** rather than two.

**Rejected: fixing them inside the session that found them.** Each touches a file an agent reads,
and the session was already changing four scripts and a hook.

# What it obliges

**They are named on `sprint.md` and are the next session's**, one line each, with no design attached
to any of them.

# Amendment, 2026-08-25 — the menu-state defect is four states, and one of the three was already done

**Written now and dated today, on the owner's instruction** — «5) мы пишем сейчас. текущей датой».
The text above is not rewritten ([[the-region-coverage-figure-is-dated-where-it-stands]]).

**`scripts/session-dialogue.py` gets four menu states, not three.**

> **owner:** «состояний меню. Делаем 4, как требует код»

**The widening was approved rather than assumed.** A scope ratified as three and built as four is a
widening, and widening asks ([[narrowing-a-scope-notifies-and-widening-it-asks]]).

**Read off the code: the counter increments `answers` only inside its `tool_result` branch**, so a
menu the owner interrupts and answers in prose is indistinguishable from one whose answer was lost.
The states are separated by whether a `tool_result` exists, whether a later turn exists, and whose it
is. **The one that will dominate is him answering in prose rather than selecting**, which is his
documented preference ([[a-list-the-owner-must-confirm-is-prose-in-chat-and-not-a-rendered-menu]]) —
so the defect line as written both undercounted the states and named the wrong dominant case.

**And the second defect was already done when this page was written.** `job_hunt_ai_vault/CLAUDE.md`
no longer obliges regenerating a `catalogue.md` and states the opposite; live mentions survive only in
`.superpowers/sdd/` transcripts and one design spec under `docs/`. `sprint.md` carried it as work for
a day longer, and that line is struck there rather than corrected
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]], [[pages-base]]).

**The first defect is decided and not built**
([[the-schema-files-leave-the-one-writer-note-by-a-flag-of-their-own]]).
