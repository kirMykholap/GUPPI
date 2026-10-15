---
type: rule
kind: Leaf
purpose: Prevents a ratified line from existing only in a chat reply, or landing in a session no /hi opened
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/ledger.py, .guppi/guppi/materialize.py, .guppi/guppi/gate.py, .guppi/guppi/casecheck.py, .guppi/guppi/tags.py, .guppi/tests/test_ledger.py, .guppi/tests/test_gate.py, .claude/settings.json]
parent: "[[rule-session-start]]"
estimates: ["[[estimate-ledger-write-lifts]]", "[[estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session]]", "[[estimate-ledger-write-refuses-a-lesson-without-its-prefix]]", "[[estimate-ledger-write-refuses-a-mark-with-no-decision-line]]", "[[estimate-ledger-write-refuses-a-line-it-cannot-read]]", "[[estimate-ledger-write-exits-2-on-an-error]]", "[[estimate-ledger-write-names-the-kind-of-a-user-record]]", "[[estimate-ledger-write-asks-for-the-mark-of-a-lesson]]", "[[estimate-ledger-write-reminds-of-the-mark-on-a-decision-line]]", "[[estimate-ledger-write-holds-a-decision-line-off-the-stored-case]]", "[[estimate-ledger-write-refuses-a-line-that-is-no-record]]", "[[estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag]]"]
origin: raw/2026-09-09/ledger.md#case-10
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, ledger]
core: true
---

## Purpose

Prevents a ratified line from existing only in a chat reply, or landing in a session no
`/hi` opened. The instruction to write `- decision[...]`, `- estimate[...]` and
`- lesson[...]` lines lives in `ratification.md` and `orchestration.md`, the Renders of `rule-ratification` and `rule-orchestration` that `/hi` loads (cases 273, 595), so a session without `/hi` produces none — and would produce them in *any* session
if the instruction stood in `CLAUDE.md` again, including one with no sprint, no branch context and no brief. Without this hook's check the
ledger would silently gain a session that was never a working session, and the librarian
would materialize pages from it the next day. It also refuses, while no live page `vault/wiki/entities/entity-sprint-<id>.md` stands, every decision line of the session but a `defer`, until the session's ledger or the same reply holds a `create` decision line of an `entity-sprint-` slug, with one stderr line that names the opening of the next sprint, so that the session after the close of a sprint opens the next sprint first, as `rule-sprint-close` sets it (case 628.3). It refuses a fresh `create` decision line of a page `entity-sprint-<id>` when `has_page` of `.guppi/guppi/materialize.py` finds that page live or archived, with one stderr line that names the id and asks for another, and such a refused line opens no sprint (case 788.1). It holds a decision line other than a `defer` that is not a line of the `ratification` of the Case `case-guppi` stored for it, a `{addresses:<slug>}` mark set aside, and tells the agent once a stretch to copy it again from the summary of `case-guppi`; the line never lands while it differs, since `generate` takes the ref and the tags of a page from it (case 688.7). It holds once a lesson line with no `{addressed_by:case N}` written after a decision line of the session, and asks the agent whether a Case of the session closed its cause: the line written again with the mark, or unchanged, is written (case 682.1). It writes the decision lines of a reply that follow a lesson of the session no mark links to a Case, and then reminds the agent once a stretch: the Case that fixed the cause writes one of its decision lines again with `{addresses:<lesson slug>}` (case 685.1). It refuses aloud a line of a `LEDGER` block that is no record — a non-blank line that does not open with `- decision[`, `- estimate[` or `- lesson[`, which it skipped without a word before — so a record with a broken opening is not lost unseen (case 695.1). It refuses a fresh lesson line whose `{tags:...}` holds a tag that no row of `vault/wiki/tags.md` holds and that no tag line of a Case of the session declares, a decision line of that Case standing in the session's ledger or in the same `Stop`, read by `.guppi/guppi/tags.py`, the reading the check of `rule-case-check` shares, so that an unlisted tag reaches no page through a lesson; a `{newtag:<tag>|<meaning>|<aliases>}` block of the line itself, or of a lesson line of the session's ledger or of the same `Stop`, declares the tag too, read by `parse_line` of `.guppi/guppi/materialize.py`, when the tag stands in the `{tags:...}` of its line and its meaning and aliases are not empty, so that a lesson brings its new tag with its meaning and aliases at any phase; its stderr line asks for a tag of `tags.md` or for that block; with no `tags.md` no tag is judged (as set in case 703.2, and in case 827.1).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-10
- 2026-09-09 updated: records are the lines of a LEDGER block, not bare lines · raw/2026-09-09/ledger.md#case-15.1
- 2026-09-09 updated: each written line carries the time of writing · raw/2026-09-09/ledger.md#case-15.3
- 2026-09-09 updated: compact and resume of the same session keep the hi window open · raw/2026-09-09/ledger.md#case-14
- 2026-09-10 status: draft → built · cascade
- 2026-09-10 deferred · raw/2026-09-10/ledger.md#case-51
- 2026-09-11 deferred_by decision-case-51 set · [[decision-case-52.3]]
- 2026-09-11 defer by decision-case-51 superseded · [[decision-case-55.1]]
- 2026-09-11 updated: the hi window spans the dates of the session: the event logs back to its start are joined · [[decision-case-55.1]]
- 2026-09-11 updated: the hi window spans the dates of the session; every LEDGER block of the session's transcript is read at each Stop, the last reply as fallback · [[decision-case-55.2]]
- 2026-09-13 updated: the lines go to the session folder raw/<hi date>/<hi HHMM>/ledger.md; the dedupe reads every ledger under raw/ (case 103.1) · [[decision-case-103.1]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-13 status: draft → built · cascade
- 2026-09-14 updated: the window is the session's own stamped hi after its first start; a foreign start no longer closes it (case 111.3) · [[decision-case-111.3]]
- 2026-09-14 deferred · [[decision-case-117]]
- 2026-09-14 updated: an unstamped hi keeps its window by the old rule while no stamped hi exists (case 111.6) · [[decision-case-111.6]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 defer by decision-case-117 superseded · [[decision-case-122]]
- 2026-09-14 updated: guppi gate refuses a Skill call while a then item of the session's Spec or plan file has no decision line in the ledger; the text before a tool call is never kept (case 122) · [[decision-case-122]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: the fallback of 111.6 — an unstamped hi bound by position — removed; a hi of the session's stamp is the one way to open the window (case 136.3) · [[decision-case-136.3]]
- 2026-09-15 updated: the Spec check of 122 names the second entry of the gate, the typed command (case 169.1) · [[decision-case-169.1]]
- 2026-09-15 updated: the refusal on an unwritten ledger line quoted with both advices, the agent's and the person's (case 174) · [[decision-case-174]]
- 2026-09-16 updated: the pass on "no source found" of 122 narrowed — a /retro with no source and no ledger line is refused by rule-retro-commit (case 180) · [[decision-case-184]]
- 2026-09-18 updated: the text before a tool call is kept in the transcript and read at the next Stop; the gate's advice says so (case 224.1) · [[decision-case-224.1]]
- 2026-09-20 updated: the ledger instruction lives in the Case schema loaded by /hi, not in CLAUDE.md (case 277.2) · [[decision-case-277.2]]
- 2026-09-25 updated: the hook refuses a reading of an Estimate that a decision line of the session creates or updates (case 428.1) · [[decision-case-428.1]]
- 2026-09-25 estimate estimate-ledger-write-refuses-a-reading-of-a-change-of-the-session added · [[decision-case-428.1]]
- 2026-09-25 status: built → draft · cascade
- 2026-09-26 deferred · [[decision-case-442]]
- 2026-09-26 status: draft → built · cascade
- 2026-09-27 estimate estimate-ledger-write-refuses-a-lesson-without-its-prefix added · [[decision-case-460.5]]
- 2026-09-27 updated: the ledger hook refuses a lesson line whose slug lacks lesson- (case 460.5) · [[decision-case-460.5]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 status: draft → built · cascade
- 2026-09-29 updated: the ledger hook refuses a lesson line whose {addressed_by:case N} has no decision line of Case N before it (case 497.1) · [[decision-case-497.1]]
- 2026-09-29 estimate estimate-ledger-write-refuses-a-mark-with-no-decision-line added · [[decision-case-497.1]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-09-30 updated: the hook refuses a line that parse_line cannot read (case 552.2) · [[decision-case-552.2]]
- 2026-09-30 estimate estimate-ledger-write-refuses-a-line-it-cannot-read added · [[decision-case-552.2]]
- 2026-09-30 updated: the hook exits 2 on its own error after the payload is read, and 0 on an error while it reads the payload (case 552.4) · [[decision-case-552.4]]
- 2026-09-30 estimate estimate-ledger-write-exits-2-on-an-error added · [[decision-case-552.4]]
- 2026-09-30 status: built → draft · cascade
- 2026-09-30 status: draft → built · cascade
- 2026-10-01 updated: the hook writes whatever stop_hook_active says; each refused line is told once a stretch, and no hi and its own error once a stretch, judged by its own refusals in the transcript (case 577.3) · [[decision-case-577.3]]
- 2026-10-01 updated: an error of the hook comes back at the first Stop of each stretch; an error while it reads the payload exits 0, since the hook cannot tell its own refusal then (case 577.4) · [[decision-case-577.4]]
- 2026-10-01 status: built → draft · cascade
- 2026-10-02 estimate estimate-ledger-write-names-the-kind-of-a-user-record added · [[decision-case-592]]
- 2026-10-02 updated: ## How it works left the Leaf, its mechanism in the docstring of guppi/ledger.py; the person's message and a returned answer are named by one function of guppi/ledger.py, which the case check and the token counter import (case 592) · [[decision-case-592]]
- 2026-10-02 updated: the instruction to write the ledger lines lives in ratification.md and orchestration.md (case 595.17) · [[decision-case-595.17]]
- 2026-10-03 status: draft → built · cascade
- 2026-10-04 updated: refuses the decision lines of a session with no live sprint page until it creates one (case 628.3) · [[decision-case-628.3]]
- 2026-10-05 updated: the hook refuses a reading of an Estimate that a decision line of the session creates or updates only before the mark retro of the session (case 670.1) · [[decision-case-670.1]]
- 2026-10-05 status: built → draft · cascade
- 2026-10-05 status: draft → built · cascade
- 2026-10-06 defer by decision-case-442 superseded · [[decision-case-682.1]]
- 2026-10-06 updated: the hook holds once a lesson line with no addressed_by mark written after a decision line of the session, and asks for the mark (case 682.1) · [[decision-case-682.1]]
- 2026-10-06 estimate estimate-ledger-write-asks-for-the-mark-of-a-lesson added · [[decision-case-682.1]]
- 2026-10-06 updated: the hook writes the decision lines after an unmarked lesson and reminds the agent of the addresses mark (case 685.1) · [[decision-case-685.1]]
- 2026-10-06 estimate estimate-ledger-write-reminds-of-the-mark-on-a-decision-line added · [[decision-case-685.1]]
- 2026-10-06 updated: the hook holds a decision line that is not a line of the stored ratification of its Case, every time it differs (case 688.7) · [[decision-case-688.7]]
- 2026-10-06 estimate estimate-ledger-write-holds-a-decision-line-off-the-stored-case added · [[decision-case-688.7]]
- 2026-10-07 updated: the hook refuses aloud a non-blank line of a LEDGER block that is no record line · [[decision-case-695.1]]
- 2026-10-07 estimate estimate-ledger-write-refuses-a-line-that-is-no-record added · [[decision-case-695.1]]
- 2026-10-07 estimate estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag added · [[decision-case-703.2]]
- 2026-10-07 updated: the ledger hook refuses a lesson line with a tag that tags.md does not hold and no ratified Case of the session declares (case 703.2) · [[decision-case-703.2]]
- 2026-10-13 updated: refuses the create of a sprint page whose id a live or archived sprint page already holds (case 788.1) · [[decision-case-788.1]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the slug of rule-sprint-close stands outside the bracket of its pointer · [[decision-case-809]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 updated: a newtag block of a lesson line declares a new tag for the ledger hook (case 827.1) · [[decision-case-827.1]]
