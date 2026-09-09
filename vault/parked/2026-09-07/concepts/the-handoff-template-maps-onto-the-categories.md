---
title: "The handoff template and the mapping ingest files it by"
type: concept
status: current
authority: handoff-template
basis: code
sprint: S0
created: 2026-08-13
sources: [".claude/templates/handoff.md", "archive/handoffs/TEMPLATE.md", ".claude/skills/handoff/SKILL.md", "archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md"]
tags: [vault, process]
---

# The handoff template, rewritten 2026-08-17

`.claude/templates/handoff.md`, copied by `/handoff` to `raw/handoffs/<YYYY-MM-DD>-<slug>.md` at the
end of a session, after the retro ([[the-retro-step]]). Frontmatter: `session:`, `sprint:`, and
`commits:` — a range, so that the session's testimony can be held against git's evidence.

**The cut is by heading text, and the numbers are gone.** Every section carries a `→ ingest:` line
naming where it is filed, and `/ingest` reads those lines rather than carrying a copy of the mapping
([[the-mapping-is-documented-at-each-hop-and-copied-nowhere]]):

| Section | Where it goes |
|---|---|
| State | the brief only — **never compiled into the wiki** |
| Entities | `entities/` |
| Decisions | `decisions/` |
| How it is built | `concepts/` |
| Lessons | `lessons/` |
| Deferred | `decisions/` for the deferral — **and `proposals/` as well** where a design sits behind it. One item routinely becomes two pages |
| Feedback to the librarian | `log.md`, under the kind the entry names: `- miss:`, `- lint:` or `- measure:` |
| Anything else worth keeping | free-form; its units are `skip:` unless the librarian finds them a category, and **if it fills up repeatedly the template is missing a section** |
| Harness | `decisions/` for what was decided, `proposals/` for a design behind it, `elsewhere:<file>` for a bare work item naming the file to change |

**`State` is never compiled** because it is state, and state is a lie within a sprint: "task 5 is
next" is true for a day. It feeds the brief, which is regenerated, and dies with it —
[[journal-vault-brief-each-artefact-has-one-owner]].

**Entities → Decisions → How it is built → Lessons is also the order an answer is given in**: what
already exists, what was already decided, how it is built, what will bite you. One sequence to
remember rather than two — [[one-librarian-behind-every-caller]].

## What changed on 2026-08-17, and what did not

**The numbers are gone from the form and from the check.** `/ingest` used to say *section 7* in so
many words, and a number moved every time a section was inserted; six files held a copy of that
number and drifted ([[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]]). The rule that
enforces the set now reads it from the template and judges a journal only while it is uncompiled
([[a-journal-is-judged-only-while-it-is-uncompiled]]).

**The form left `raw/` and was archived, not deleted**: `archive/handoffs/TEMPLATE.md` still carries
the numbered version, and this page's own history below was written against it
([[claude-templates-directory]]).

**Everything else on this page still holds** — and that is why it was rewritten rather than retired:
twelve live pages cite it, most of them for claims that did not change. `State` is never compiled,
`raw/` is immutable, an empty section is a legal answer, and this file is the only channel from a
session to the librarian. **Only the numbering claim died.**

**`authority: handoff-template` stays here.** Nothing decided that it should move to
[[claude-templates-directory]], which describes the directory rather than the form, and nothing
decided that it should not — it is named in the journal of 2026-08-17 as an open question and is
recorded here as one.

## The rules that look like formalities and are not

- **An empty section is a legal answer — write "none" — but the section stays.** Nobody misses
  `Feedback to the librarian` on their own; it has to be asked. **This is a rule, not an
  exhortation**: rule 8 of `vault-check.sh` fails a journal carrying `session:` whose heading set
  differs from the template's ([[vault-scripts]]). Nothing else in this repository looks inside
  `raw/` at all, so a short handoff would otherwise lose a category in silence.
- **`raw/` is immutable.** A correction is a new line in a later handoff, never a rewrite of an
  earlier one ([[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]],
  [[raw-holds-testimony-and-artefacts-are-frozen]]).
- **`Feedback to the librarian` does not carry only misses.** It is the only channel a subagent's
  measured cost can reach `log.md` through ([[a-subagent-cannot-report-its-own-cost]]), so
  `- measure:` and `- lint:` lines travel here and are filed under their own kinds.

**A claim about this template asserted from prose rather than from the file was wrong three times in
one session** ([[a-claim-asserted-from-prose-rather-than-from-the-file]]). Read the template.

---

## What stood here until 2026-08-17, kept verbatim

*Nothing below is deleted, and the numbered mapping it describes was true of
`archive/handoffs/TEMPLATE.md` when it was written. It is superseded by the table above, and the
paragraph headed "The numbers are decided away" is the one that has now happened.*


# The handoff template

`archive/handoffs/TEMPLATE.md`, copied by `/handoff` to `raw/handoffs/<YYYY-MM-DD>-<slug>.md` at the
end of a session. Frontmatter: `session:`, `sprint:`, and `commits:` — a range, so that the
session's testimony can be held against git's evidence.

**The section numbers are load-bearing**, because ingest files by number:

| Section | Where it goes |
|---|---|
| 1. State | the brief only — **never compiled into the wiki** |
| 2. Entities | `entities/` |
| 3. Decisions | `decisions/` |
| 4. How it is built | `concepts/` |
| 5. Lessons | `lessons/` |
| 6. Deferred | `decisions/` — deferring is a decision, with a date and a rejected alternative — **and `proposals/` as well, where a design sits behind the deferral** |
| 7. Feedback to the librarian | `log.md`, under the kind the entry names: `- miss:`, `- lint:` or `- measure:` |
| 8. Anything else worth keeping | free-form; **if it fills up repeatedly the template is missing a section** |

§1 is never compiled because it is state, and state is a lie within a sprint: "task 5 is next" is
true for a day. It feeds the brief, which is regenerated, and dies with it —
[[journal-vault-brief-each-artefact-has-one-owner]].

**2 → 3 → 4 → 5 is also the order an answer is given in**: what already exists, what was already
decided, how it is built, what will bite you. One sequence to remember rather than two —
[[one-librarian-behind-every-caller]].

## Two rows the mapping got wrong, corrected 2026-08-15

**§6 is not one folder.** The fifth category arrived on 2026-08-15
([[proposals-are-a-folder-not-a-status]]) and it cuts across this table: a deferral is a decision
and stays in `decisions/`, while **the design it defers is a proposal**. One §6 item routinely
becomes two pages, and `/ingest` step 1b exists for exactly that. The ingest of this journal split
one item that way — three named designs that do not exist became three `proposals/` pages, while
the deferral of all six audit findings became one `decisions/` page
([[the-audits-findings-are-owed-to-the-owner]]). **An intention is filed in `proposals/`,
never in `decisions/` or `concepts/`.**

**§7 does not carry only misses.** It is the only channel a subagent's measured cost can reach
`log.md` through, because a subagent cannot see its own usage
([[a-subagent-cannot-report-its-own-cost]]) — so `- measure:` lines travel here, and so do
`- lint:` lines about the librarian itself. Of the seven items in §7 of the 2026-08-15 journal,
**four were `measure:` and three were `lint:`, and none was a `- miss:`.** Each is transferred
under its own kind and verbatim in substance, including the two that correct an earlier entry:
the correction stands *beside* the original, never inside it, which is the rule `raw/` itself lives
by.

## Two rules that look like formalities and are not

- **An empty section is a legal answer — write "none" — but the section stays.** Nobody misses
  section 7 on their own; it has to be asked. **This is a rule, not an
  exhortation**: since 2026-08-13 `vault-check.sh` fails when a journal carrying `session:` does
  not carry **the set 1–8** ([[vault-scripts]]). Nothing else in the repository looks
  inside `raw/` at all, so a six-section handoff would otherwise lose two categories in silence.

  *Two corrections here, both made 2026-08-15 by the first `/vault-lint`.* This bullet said the
  check fails on **fewer than eight numbered sections**; it does not, and never did — the rule
  reads the *set*, because dropping §7 and writing a second §6 also counts eight, and renumbering
  §7 to §3 counts eight as well. That was corrected in the script on the day the rule was written
  and is stated on [[vault-scripts]]; only this page kept the count wording. And the bullet used to
  cite [[active-tasks-stay-empty-until-a-tracker-exists]] for "the same reasoning keeps an empty
  section in the brief" — that page is **deprecated**, and its successor
  [[the-brief-has-no-active-tasks-section]] reverses exactly that: the brief's section was removed
  rather than kept empty, by the owner on 2026-08-14. The handoff's rule is unchanged; what is gone
  is the analogy, because the brief no longer keeps one.
- **`raw/` is immutable.** A correction is a new line in a later handoff, never a rewrite of an
  earlier one: what the session believed at the time is data, and the vault's own worst failure so
  far was reading an appended document as though its later text had replaced its earlier text
  ([[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]]).

**It is the only channel from a session to the librarian**, which did not watch that session
([[vault-librarian]]). Everything the vault will ever know about a day is what this file says —
which is why the template is strict rather than a suggestion, and why the units of a handoff are
counted mechanically at ingest ([[ingest-is-units-and-verdicts]]).

## The numbers are decided away, and this page is not yet superseded

**2026-08-16, the second session of that day:**
[[the-handoff-template-moves-out-of-raw-and-drops-its-numbers]] takes the template to
`.claude/templates/handoff.md`, **drops the numbers**, cuts by heading text instead, and adds a
ninth section, `Harness`, at the end. The reason is the coupling this page calls load-bearing:
`/ingest` naming *section 7* is exactly what made inserting a section a renumbering of everything
that referred to a number.

**Nothing has moved on disk.** `archive/handoffs/TEMPLATE.md` still carries the numbers, this ingest was
performed against the mapping above, and the retirement belongs to the session that performs the
change rather than to the one that recorded the intention — the shape
[[the-repository-claude-md-becomes-a-dispatch-table]] set. **The supersession is the owner's to
order**, and it is raised in the brief.

One row of the table above changes when it happens: §6 already routes to two folders, and
`Anything else worth keeping` gains a written default — its units are `skip:` unless the librarian
finds them a category.
