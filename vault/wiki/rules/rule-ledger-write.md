---
type: rule
kind: Leaf
purpose: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
status: built
enforcement: hook
implementation_ref: [guppi/ledger.py, guppi/materialize.py, guppi/gate.py, guppi/casecheck.py, guppi/tags.py, tests/test_ledger.py, tests/test_gate.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, hooks, harness, ledger]
core: true
---

## Purpose

Prevents a ratified line from existing only in a chat reply, or landing in a session no
`/hi` opened. The instruction to write `- decision[...]`, `- estimate[...]` and
`- lesson[...]` lines lives in `ratification.md` and `orchestration.md`, the Renders of `rule-ratification` and `rule-orchestration` that `/hi` loads, so a session without `/hi` produces none — and would produce them in *any* session
if the instruction stood in `CLAUDE.md` again, including one with no sprint, no branch context and no brief. Without this hook's check the
ledger would silently gain a session that was never a working session, and the librarian
would materialize pages from it the next day. It also refuses, while no live page `vault/wiki/entities/entity-sprint-<id>.md` stands, every decision line of the session but a `defer`, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug, with one stderr line that names the opening of the next sprint, so that the session after the close of a sprint opens the next sprint first, as `rule-sprint-close` sets it. It refuses a fresh `create` decision line of a page `entity-sprint-<id>` when `has_page` of `guppi/materialize.py` finds that page live or archived, with one stderr line that names the id and asks for another, and such a refused line opens no sprint. It holds a decision line other than a `defer` that is not a line of the `ratification` of the Case `case-guppi` stored for it, a `{addresses:<slug>}` mark set aside, and tells the agent once a stretch to copy it again from the summary of `case-guppi`; the line never lands while it differs, since `generate` takes the ref and the tags of a page from it. It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session, and asks the agent whether a Case of the session closed its cause: the line written again with the mark, or unchanged, is written. It writes the decision lines of a reply that follow a lesson of the session no mark links to a Case, and then reminds the agent once a stretch: the Case that fixed the cause writes one of its decision lines again with `{addresses:<lesson slug>}`. It refuses aloud a line of a `LEDGER` block that is no record — a non-blank line that does not open with `- decision[`, `- estimate[` or `- lesson[`, which it skipped without a word before — so a record with a broken opening is not lost unseen. It refuses a fresh lesson line whose `{tags:...}` holds a tag that no row of `vault/wiki/tags.md` holds and that no tag line of a Case of the session declares, a decision line of that Case standing in the session's ledger or in the same `Stop`, read by `guppi/tags.py`, the reading the check of `rule-case-check` shares, so that an unlisted tag reaches no page through a lesson; from `/work` to the end of Retro, where no Case is ratified, its stderr line asks for a tag of `tags.md` and for the new tag as a line of the handoff to a later session; with no `tags.md` no tag is judged.

## History

- 2026-10-14 shipped with GUPPI
