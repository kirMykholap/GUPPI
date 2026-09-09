---
title: "/lint has never run, because it is defined per sprint and no sprint has ever been opened"
type: decision
status: archived
superseded_by: [[vault-lint-runs-every-session-so-the-sweep-fires]]
authority: lint-cadence
binding: deferral
basis: inference
sprint: S0
decided: 2026-08-14
created: 2026-08-14
sources: ["archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md", ".claude/skills/vault-lint/SKILL.md", "raw/notes/2026-08-13-owners-note-second-brain-instructions.md", "raw/notes/2026-08-13-owners-note-second-brain-info.md"]
tags: [vault, process]
---

# The audit is scheduled against something that does not exist yet

`/vault-lint` is defined as a **retrospective activity, one per sprint**
([[one-librarian-behind-every-caller]]) — a cadence taken verbatim from the owner's instructions note,
«ручной запуск в конце спринта». **Two of the three checks that note listed for it were made
mechanical instead** and now run on every write: orphans, and the `status:` vocabulary
([[vault-scripts]]). **The third was never built at all** — reconciling the architecture in
`entities/` against the register in `decisions/` is in no skill and in no script
([[the-owners-instructions-note-and-what-was-built-from-it]]). **The owner's other note lists a
fourth check that nothing implements either** — *«отсутствие необходимых концептуальных страниц»*,
the conceptual pages the corpus is missing — and it is a different item from the reconciliation
above, so the two notes together ask for five checks of which three are built
([[the-owners-method-note-and-what-was-built-from-it]]). It is also the only one of the five that
no `grep` could answer: a page that ought to exist leaves no trace to search for. No sprint has
ever been opened
([[a-sprint-closes-on-its-goal]]), so **the thing that watches the health of the knowledge base has
never run on its own schedule** — not once, on a corpus that is now past eighty pages.

**The deferral stands rather than being repaired**, and the reason is that the two halves of a lint
have different costs:

- **the mechanical half costs seconds** — duplicate authorities, dead tags, split candidates,
  broken links. Most of it is already `vault-check.sh` on every write ([[vault-scripts]]);
- **the judgement half needs an open sprint to close against.** Merging two near-duplicate pages is
  supersession and the owner's call; re-tagging pages a session never touched is not an ingest's
  act. Findings with nowhere to be decided become a list nobody reads.

**Rejected: running it anyway, on no schedule.** That produces exactly the standing advisory this
project has already learned not to read — an alarm that fires every time and cannot be acted on.

## The consequence is an agenda that accrues, and it is now named

Recorded 2026-08-14, all of it in `log.md`:

- **three page pairs proposed for merging** (the journal's count; `log.md` heads the same list with
  "four pairs" and lists three — [[a-stated-count-drifts-from-the-list-it-heads]]);
- **two filenames that understate their pages**;
- **tags past the split threshold** `tags.md` sets. The journal reports two — `process` on 23
  pages of 81 and `testing` on 18 — and the ingest of 2026-08-14 made it **three of 95**:
  `process` 32, `vault` 31, `testing` 23. The pages written that day are about the vault and about
  how we work, so they landed on exactly the tags that were already too wide. **An ingest may not
  fix this**: re-tagging pages it never touched is the judgement half, and it is the owner's;
- **two recorded gaps**, as the journal names them: no page for the hooks, and none for the module
  map. The first has since been closed — [[session-hooks]] was written the same evening the gap was
  recorded, and this is the agenda going stale in the harmless direction. **The module map stands**:
  §3 of the old handoff is a single fenced block, so it never was a unit and never had a verdict
  ([[vault-scripts]]). `log.md` names two more of the same kind, the CLI and the data model.

**Opening a sprint is what unblocks all of it**, which makes this deferral one of the concrete
costs of having none.

**The premise expired the same day this page was written: S1 was opened on 2026-08-14**, and its
first acceptance criterion is a `/vault-lint` over the whole corpus with an outcome against every
finding. The title stayed true for a day — the audit had not run — but the reason it had not was
gone, and the agenda above became the agenda of an open sprint rather than of no sprint. Reported,
not closed: whether a sprint has met its goal is the owner's to say
([[a-sprint-closes-on-its-goal]]).

**And on 2026-08-15 it ran** — the first `/vault-lint` this corpus has ever had, over 108 pages in
`wiki/` and three in `archive/`, with its findings and their outcomes in `log.md`. **The title of
this page is now false**, and correcting a title is supersession rather than an edit
([[the-wiki-has-five-folders-and-tasks-is-not-one]] is the precedent, retired the same week for the
same reason). It is named here and left for the owner rather than done by the run that made it
false: this page is the record of *why* the audit was deferred, which is still the answer to "why
did a store go three days unaudited", and that reasoning does not expire with the deferral.

Of the agenda above, the 2026-08-15 run closed the counts and left the judgements: the three merge
candidates and the two understating filenames are supersessions and still stand; the three tag
advisories are acceptance criterion 3 of S1 and are the owner's; the module map, the CLI and the
data model are still uncompiled negative space.

**The retitle of this page is one of the six findings deferred to the owner** on 2026-08-15 —
[[the-audits-findings-are-owed-to-the-owner]], which carries all six with a reason each.

**And the negative space was sharpened into a finding.** The module map, the CLI and the data model
are not unfinished ingests: **they have no source in `raw/` to be compiled from.** All six sources
report `INGEST COMPLETE`, and that is compatible with the layout of `src/jobhunt/` being written
down nowhere — §3 of the old handoff is a single fenced block and fenced content produces no units
at all ([[vault-scripts]]). *The absence of a source is the finding, not the absence of a page*,
and no coverage run will ever report it. What would:
[[a-check-for-missing-conceptual-pages]].

The two checks this page names as never built now have pages of their own —
[[reconciling-entities-against-the-decision-register]] and
[[a-check-for-missing-conceptual-pages]] — so the designs stop living as clauses inside a
deferral.

---

**Two notes added 2026-08-16, neither of which changes what this page says.**

**Its title is false and its supersession is decided but not executed.** `/vault-lint` has run —
2026-08-15, over 108 pages ([[the-audits-findings-are-owed-to-the-owner]], finding #1). The
owner has decided the retitle and nobody has performed it; twelve inbound links wait to move with
it ([[structure-work-agreed-and-not-executed]]).

**It is also one of the two records found mis-filed on 2026-08-16**: typed `decision` while its
title asserts a *state*. The defect is in the schema rather than in the filing —
[[a-schema-per-type-says-what-a-record-asserts]].

---

**Third note, 2026-08-19: the title is still false, nothing can see that it is, and the price stated
above is wrong in kind.**

**No instrument can catch this one.** Rule 10 reads a title for a counting word; a title that asserts
a false *state* is invisible to it, and to every other verdict there is
([[the-no-quantity-rule-reads-the-title-and-the-filename-and-never-the-body]]). The falsehood has now
stood for three days on a page whose whole subject is auditing the store.

**And *"twelve inbound links wait to move with it"* is wrong about what a retitle costs.** A title is
corrected in place; the filename is the address, and correcting a title moves no address and strands
nothing ([[a-title-corrected-in-place-is-not-a-supersession]]). **The retitle is free.** What carries
a link cost is a *rename*, which is a different operation and was measured this week at ten seconds
for sixteen of them ([[a-page-rename-is-sed-and-verify]]).

**Left standing rather than executed**, because the owner decided the retitle and the wording is his;
what is corrected here is the belief that it was expensive.

# Retired 2026-08-30: the cadence changed and the reason this page gave dissolved

**Superseded by [[vault-lint-runs-every-session-so-the-sweep-fires]].** `/vault-lint` becomes a
per-session ritual, so the premise of this page — a per-sprint cadence against a sprint that had never
opened — no longer holds in either half.

**What made the change urgent is not the sprint at all.** The sweep in `scripts/vault-archive.sh` is
the **only** mechanism that shrinks `wiki/`, and it lives inside this ritual. On 2026-08-29 `/ingest`
ran twice and `/vault-lint` did not run once: the corpus went 556 to 568 pages and nothing was
retired.

**owner, 2026-08-29:** «sweep должен происходить каждый ingest. Почему сегодня не прошел? vault-lint
выглядит как то, что мы должны делать каждую сессию».

**This page carried `basis: inference` and the successor carries `basis: human`**, which is the
ranking that settles it without argument.

**The venue of the sweep does not move**
([[the-archive-mover-is-a-sweep-inside-the-archive-script-at-the-lint-stage]]) — only how often the
ritual holding it runs.

*(Corrected 2026-08-30 from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
