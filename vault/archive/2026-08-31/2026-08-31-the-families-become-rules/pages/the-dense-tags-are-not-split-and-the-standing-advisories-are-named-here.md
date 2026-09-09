---
title: "The dense tags are not split corpus-wide, and every per-folder advisory that stands is named here"
type: decision
status: archived
authority: standing-tag-advisories
binding: prohibition
basis: human
sprint: S1
decided: 2026-08-16
created: 2026-08-16
sources: ["scripts/vault-check.sh", "tags.md", "sprint.md", ".claude/agents/vault-librarian.md"]
tags: [retrieval, vault, testing]
---

# Decided 2026-08-16: measure inside the folder, split nothing yet

**Rejected: splitting `vault`, `process` and `testing`.** That was the plan that went in, carrying
three days of evidence behind it ([[dynamic-tag-classification-by-a-skill]]), and **the per-folder
measurement refuted it before it was applied.** The disease is a tag inside a folder, not a tag.

The finding the corpus-wide number was hiding, measured at `2036d98`:

| tag | `decisions/` (47) | `concepts/` (32) | `lessons/` (19) | `entities/` (15) | `proposals/` (5) |
|---|---|---|---|---|---|
| `vault` | **19** | **11** | 9 | 8 | 4 |
| `process` | **18** | 4 | **12** | 8 | 1 |
| `testing` | 5 | 7 | **13** | 3 | 2 |

**`testing` is healthy where it was accused** — 5 of 47 in `decisions/` at `2036d98`, ten percent,
which is a tag doing exactly its job — and useless only in `lessons/`. `process` is 4 of 32 in
`concepts/`. Two of the three tags called useless are useless in **exactly one folder each**, and a
corpus-wide split would have damaged them everywhere else to fix that one place.

Why the number is ten and why it is per folder is the mechanism, not the decision:
[[the-folder-is-the-first-narrowing]]. In one line: ten is the reader's ceiling and does not move
when the corpus does, which is what this project requires of a threshold after an earlier alarm
named a size outright and that number turned out to be invented
([[the-growth-signal-is-the-brief]], [[an-unsourced-number-is-dropped-not-chosen]]).

## The five lines the check prints at `2036d98`, and what stands for each

`bash scripts/vault-check.sh | grep advisory` prints these five and nothing else. Each is named
here, which is what acceptance criterion 3 of S1 asks of a line that still prints.

| # | The line | What stands, and why |
|---|---|---|
| 1 | `vault` selects **19** pages in `decisions/` | Stands. The store writes most about itself, and a decision about the store is the commonest thing this vault records. The cut that pays is **shape versus loop** — categories, folders, filenames, statuses on one side; handoff → ingest → verdict → brief on the other — and `process` has already half-made it, since 25 of the 42 `vault` pages measured on 2026-08-15 also carried `process` ([[dynamic-tag-classification-by-a-skill]]). Re-tagging some thirty `decisions/` pages is the judgement half of a lint and the owner's call ([[lint-waits-for-an-open-sprint]]) |
| 2 | `vault` selects **11** pages in `concepts/` | Stands, and it is the **weakest** of the five: one page over the ceiling. The same cut would resolve it, and on its own it would not be worth a re-tagging pass |
| 3 | `process` selects **18** pages in `decisions/` | Stands. Its cheapest split, an `environment` tag, takes 3 pages out of `process` and pulls 2 in from elsewhere — **5 pages for one word**, and none of the three are decisions, so it does not touch this line at all. Nothing cheaper has been designed |
| 4 | `process` selects **12** pages in `lessons/` | Stands. `lessons/` is *us, working on the product*, which is what `process` is defined as — the two overlap by construction, and a split here is a question about whether the folder and the tag should say the same thing. Nobody has argued it yet |
| 5 | `testing` selects **13** pages in `lessons/` | Stands, and it is the **first candidate when the skill runs**. It is the one place `testing` classifies nothing, and the split that fits is *accounting* — coverage, verdicts, counts, units. The vault-versus-product cut was already considered on 2026-08-13 and refused on a ground that still holds: `vault-check.sh` fails a build for the same reason `pytest` does |

**One caveat covers rows 1, 3 and 5.** The strata those cuts are named from were measured over the
whole corpus on 2026-08-15, before density was measured per folder, and **none of them has been
re-measured inside its folder** — so "5 pages for one word" and "accounting is five pages" are
counts of a corpus-wide slice, not of the folder the line is about. Which pages a cut would
actually move is the first thing the skill has to establish, and it is the reason none of the five
is closed by asserting a cut here.

## Splitting is surgical when it happens

**The unit of a split is a tag inside a folder** — `testing` in `lessons/`, never `testing`. That
follows from the measurement above: a tag can be healthy in one folder and useless in another, and
one corpus-wide cut cannot express that.

**And it is done by the skill, not by hand.** [[dynamic-tag-classification-by-a-skill]] designs a
pass that brings **a proposal for the owner to look at** — split candidates with a suggested cut,
the old word kept as an alias, and a drift list. A cut made once by hand changes pages the cutter
never wrote and leaves nobody able to check what recall was lost; the two hand-splits this vault
has (`collection` at 17 of 29, `web` at 22 of 56) worked and are the reason we know what they cost.

## The cost, stated rather than glossed

**Five standing lines are more than the three that stood before.** This project has already decided
that an alarm which always fires stops being read — it is the argument that rejected baselining the
brief's growth threshold at 4× a first-brief baseline ([[the-growth-signal-is-the-brief]]), and the
argument that refused to run `/vault-lint` on no schedule ([[lint-waits-for-an-open-sprint]]). The
advisory prints and does not fail the run for exactly that reason, and this page does not pretend
the count improved.

What changed is that the lines are now **actionable and unambiguous**: each names a folder, so each
has a bounded re-tagging pass behind it, and the threshold is one number rather than the two that
`vault-check.sh` and `tags.md` carried between them until 2026-08-16.

**Whether criterion 3 of S1 is met is read off the run, by the owner.** This page names the five
lines; it does not declare the criterion closed, exactly as a sprint is closed by the owner and not
by the librarian ([[a-sprint-closes-on-its-goal]], [[the-librarian-writes-unattended]]).

*The writes of 2026-08-16 moved two of the five: `vault` in `decisions/` to **20** and in
`concepts/` to **12**, measured after this page and its two siblings were written and before the
commit that carries them — both moved because those pages are about the store and carry `vault`,
which is the mechanism [[dynamic-tag-classification-by-a-skill]] names. This page also took
`testing` in `decisions/` from 5 to **6 of 47**, so the ten percent quoted above is the reading at
`2036d98` and is thirteen after it; the tag is still four pages under the ceiling there. The
figures in the table are the state the decision was taken against.*

## The owner read criterion 3 off the run on 2026-08-16: closed in part, retired in part

**His words, and the split is his:** the criterion's **intent is met** — every printed advisory is
named by a `decisions/` page, which is this page — while **its own wording describes a check that no
longer exists.** It names "the three tag advisories — `process` 33, `vault` 31 and `testing` 24
pages, all over the split threshold", and that check was replaced on `2036d98` by a per-folder count
against ten. The pages and the threshold in the criterion are both gone.

So: **partly closed, and partly no longer relevant.**

**That change belongs in `sprint.md`'s "Changes to the goal", and it is not written there yet.**
`sprint.md` is the record of the sprint, this page is not, and the librarian neither closes a sprint
nor edits its criteria ([[a-sprint-closes-on-its-goal]], [[the-librarian-writes-unattended]]). The
entry is owed by whoever runs `/sprint` next, and it is raised in the brief rather than performed
here.

## Six lines print after the ingest of 2026-08-16, and the sixth is named here

Measured from the run and not predicted, immediately after this journal was compiled:

| the line | against `2036d98` |
|---|---|
| `vault` in `decisions/` — **30** | was 19 |
| `process` in `decisions/` — **24** | was 18 |
| `process` in `lessons/` — **16** | was 12 |
| `testing` in `lessons/` — **16** | was 13 |
| `vault` in `concepts/` — **15** | was 11 |
| **`vault` in `lessons/` — 14** | **was 9, and under the ceiling; this line is new** |

**The sixth line stands, on the same ground as rows 1 and 2 of the table above.** The store writes
most about itself, and the ingest of 2026-08-16 compiled a session that was *entirely* about the
store: five of its lessons are about how this vault is measured, written, rewritten and read, so
every one of them carries `vault` honestly. The cut that would resolve it is the same one — shape
against loop — and it is the same judgement call, deferred to the skill that brings a proposal
([[dynamic-tag-classification-by-a-skill]]).

**One tag choice was corrected rather than defended.** [[batches-stays-a-tag-of-its-own]] was first
written `[retrieval, vault, collection]`; the page is about the tag dictionary and not about
gathering vacancies, so `collection` was removed as wrong on its own terms. It also took
`collection` in `decisions/` from 11 back to 10 and stopped a seventh line printing — which is
recorded here rather than left unsaid, because a tag chosen to quiet an instrument is the failure
[[an-instrument-that-contains-its-own-answers-can-be-gamed]] names.

**This page's own title says five, and six print.** The title is now false, by the count that this
ingest itself moved, and it is a new instance of
[[a-title-names-what-is-counted-instead-of-counting-it]] — created by the librarian, on a page the
librarian wrote the day before. **It is not retitled here**: a title carries the claim, so changing
one is supersession and the owner's ([[the-audits-findings-are-owed-to-the-owner]], finding #1,
which now has a third page under it).

## Seven lines print after the ingest of 2026-08-17, and the seventh is named here

Measured from the run, immediately after the journal of the harness session was compiled:

| the line | after the 2026-08-16 ingest |
|---|---|
| `vault` in `decisions/` — **39** | was 30 |
| `process` in `decisions/` — **32** | was 24 |
| `process` in `lessons/` — **19** | was 16 |
| `testing` in `lessons/` — **19** | was 16 |
| `vault` in `lessons/` — **17** | was 14 |
| `vault` in `concepts/` — **16** | was 15 |
| **`vault` in `proposals/` — 11** | **was 4, and under the ceiling; this line is new** |

**The seventh stands on the same ground as every other `vault` line**, with one thing worth saying
about it: `proposals/` is the smallest folder in the wiki, so a tag on eleven of its pages is close
to a tag on all of them — the tag classifies nothing *there* while classifying perfectly elsewhere,
which is the per-folder disease this page was written about, in its purest form yet.

**A new tag was minted rather than a `vault` added**, and this is the first advisory line to be
held down deliberately: the harness pages of this ingest carry **`harness`** where `vault` would
have been honest but useless — the harness is the files that instruct an agent, and *who owns them
and how they go stale* is a subject, not a corner of the store. Ten pages carry it, counted from
the run. Without that choice the `decisions/` line would read higher still.

**That is one step from the failure named above** — a tag chosen to quiet an instrument
([[an-instrument-that-contains-its-own-answers-can-be-gamed]]) — so the ground has to be the tag's
own merit and it is stated in `tags.md` beside the definition: `harness` is not a synonym for
`process`, and the words a question about it would use (`обвязка`, `инжектор`, `размеченный
регион`, `governs`) reached nothing at all before it existed.

**The title now understates by two.** It said five, six printed after the previous ingest, seven
print now. Still not retitled, for the same reason
([[a-title-names-what-is-counted-instead-of-counting-it]]).

## Ten print after the ingest of 2026-08-17, and the title no longer counts them

**The title was corrected in place** that day, to name what is counted instead of counting it, and
that is not a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]). The paragraph
above is the old wording and is kept; the count in it is superseded by this one.

Measured on the run after the ingest of 2026-08-17: `vault` **42** in `decisions/`, `process`
**40** in `decisions/`, `process` **24** in `lessons/`, `testing` **24** in `lessons/`, `vault`
**22** in `lessons/`, `vault` **18** in `concepts/`, `harness` **11** in `decisions/`, `process`
**11** in `entities/`, `testing` **11** in `concepts/`, `vault` **11** in `proposals/`. **Ten lines
where seven printed before**, and the three new ones are new *folders* rather than new tags —
`harness` and `process` crossed the threshold in folders where they had not, and `testing` in
`concepts/`. That is the per-folder measurement doing what it was changed for: a tag can be healthy
in one folder and useless in another ([[the-folder-is-the-first-narrowing]]).

**The filename still carries the count**, and that is deliberate rather than overlooked: renaming a
file moves an address, so it needs the rewriter-and-detector pair before it is attempted
([[a-rewriter-must-be-paired-with-a-detector]]). The decision itself — split nothing yet — is
unchanged.

## The title is compliant and the filename is not — measured 2026-08-17

**The brief reported this page as *"still false in its title"* and that was wrong.** Measured at
`ed239f2`: `title:` already read *"The dense tags are not split corpus-wide, and every per-folder advisory
that stands is named here"* and carries no quantity, so **rule 10 is silent and correct**.

**What is stale is the filename** — `the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here` — and rule 10
deliberately does not read filenames: the filename is the address, and **this page carries 23 inbound
links**, the most of any page in the corpus.

**The owner then extended the rule to cover filenames** ([[the-title-rule-extends-to-filenames]]), so this
page is now the named worst offender of a rule that has no verdict yet and whose rename is blocked on the
rewriter-and-detector pair ([[a-rewriter-must-be-paired-with-a-detector]]).

**The advisory count on this page's own subject has moved again**: **ten tag advisories print at
`814472a`**, plus the region-coverage line. That is why the title says *every advisory that stands is named
here* rather than counting them ([[a-stated-count-drifts-from-the-list-it-heads]]).

## Read off again on 2026-08-18 by the owner: nothing is split, and the condition for revisiting is named

**owner: split nothing yet.** Fifteen tag advisory lines print, plus the region-coverage line. The
decision is unchanged and is re-recorded rather than assumed, because a decision that is never
re-stated becomes a habit.

**The condition he named for revisiting is about the channel, not the count:** *fifteen advisory
lines that never change teach a reader to skip advisories*, and advisories are the one channel the
check has for speaking quietly. **So the trigger is a reader who has stopped reading them**, not a
threshold — the moment an advisory line is the thing nobody looks at, the mechanism has failed
whatever the number says ([[an-advisory-prints-one-line-and-sorts-what-it-names]]).

**The sixteenth line is not a tag line.** Region coverage is a different instrument sharing the same
channel, and it is the line most likely to be lost in the noise
([[a-governed-file-with-no-region-is-an-advisory]],
[[the-region-coverage-figure-is-dated-where-it-stands]]).

## Read again on 2026-08-18, second session: still not split, and the run prints twenty

**Twenty advisories**, up from eighteen at the previous ingest: seventeen tag-density lines, the
region-coverage line, and the filename line that arrived this session
([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]) — which prints six
continuation lines that are deliberately not counted as advisories
([[the-filename-advisory-prints-one-name-per-line]]).

**Nothing was split and nothing was decided about splitting.** It goes to `/vault-lint` at the
sprint retrospective, which is where the decision above already put it
([[lint-waits-for-an-open-sprint]]).

## Closed 2026-08-19: the filename was renamed, and the line that counted it stopped printing

**Every claim above about this page's own name is finished.** *"The filename still carries the
count"*, *"it needs the rewriter-and-detector pair before it is attempted"* and *"whose rename is
blocked on the rewriter-and-detector pair"* were all closed by one change on 2026-08-19. **The pair
was never built**: the sweep was `git mv`, one `sed -f` over every reference in `wiki/`, `archive/`,
`index.md`, `tags.md` and `sprint.md`, and a verification pass, with `log.md` swept by hand because
rules 4 and 5 do not read it ([[a-page-rename-is-sed-and-verify]],
[[log-md-is-outside-the-link-set-the-check-reads]]).
The decision this page carries — split nothing yet — is untouched by any of it.

**One sentence above now says the opposite of what it was written to say, and it is corrected here
rather than rewritten.** *"What is stale is the filename — `…`"* names, in its code span, the name
this page carries **today**: the reference rewriter reached a slug that was quoted as an **example**
rather than used as an **address**, and there is nothing in a slug that tells the two apart. The
name it was written about is in git and in the journals under `raw/`, where a slug of that date is
correct. **It is one of two places the sweep over-reached** — the other illustrates the same rule
with a slug that no longer counts ([[the-filename-verdict-is-an-advisory-while-the-title-verdict-is-red]]),
and both are in `log.md`. The shape is worth keeping: a rewriter over addresses will always
over-reach into quotation, which is why a rename ends in a read rather than in a clean exit code.

**Measured on the run of 2026-08-19: nineteen advisories, down from twenty.** Eighteen tag-density
lines and the region-coverage line; the filename line prints nothing, which is the whole of the
decrease. `bash scripts/vault-check.sh | grep -c 'advisory:'` returns 19 and
`bash scripts/vault-check.sh | grep -c 'filename(s) count'` returns 0. **No split is decided or
undecided here** — the tag lines and their numbers are the owner's to read off, as every section
above records ([[lint-waits-for-an-open-sprint]]).

## The counter came close to steering a librarian's own choice, for the second time

**2026-08-19.** Choosing tags for a new page, the librarian noticed that one natural set would push
`schema` in `decisions/` past the ceiling and print a further advisory line. **It chose different tags
on the merits and said so in the log**, rather than choosing them to keep the counter down.

**That is the second instance of an advisory count coming close to steering the choice it is supposed
to measure.** The first is on the record from the same week: the `schema` tag split was proposed to
the owner as beating a density counter, and the measurement then showed there was no counter to beat —
`harness`, `process` and `vault` stand at 54, 60 and 78 in `decisions/` against a threshold of ten, so
an honest split prints an advisory immediately and a nineteenth line joins eighteen that already stand
unactioned ([[the-schema-tag-splits-into-db-schema-and-record-schema]],
[[a-claim-that-runs-ahead-of-its-measurement-is-corrected-in-the-same-session]]).

**This page already argues that an alarm which always fires stops being read.** The instances above
are the other cost of the same thing: an alarm that always fires becomes a number the measured party
starts managing. **Neither instance changed a page**, and both were reported rather than hidden, which
is the only reason either is visible at all.

## The `record-schema` advisory fell out of a session because it lived only in a brief — 2026-08-19

**The advisory this page exists to hold stood, and the sweep it names went missing.** The
`record-schema` line in `decisions/` was in the brief's *next* list, the session did other work, and
**nothing raised it** — no artefact recorded that it had been dropped, because the brief is regenerated
and carries no memory of what it asked for last time.

**It was surfaced at the retro and ratified as a deferral onto `sprint.md`**
([[the-record-schema-sweep-and-the-trim-candidates-go-onto-the-sprint]]).

**That is a third cost of an always-firing advisory, beside the two above.** An advisory that always
prints is not only unread and not only managed — **it is indistinguishable from an advisory that was
scheduled to be actioned and was not**, because both look the same in the next run's output.

## The channel split, 2026-08-20 — the lines still stand and they no longer print on a bare run

**owner: the tag-density advisories move behind `bash scripts/vault-check.sh --lint`.** A bare gate
run went from **twenty-one advisories to one**, and the one that survives is region coverage — the
only line that was ever about the run in front of you
([[the-tag-density-advisories-move-behind-lint]],
[[a-governed-file-with-no-region-is-an-advisory]]).

**Nothing on this page is split, and nothing on it is retracted.** The decision it carries — split
nothing yet — is untouched. What changed is the **channel**: the condition the owner named on
2026-08-18 for revisiting was *a reader who has stopped reading them*, and the repair chosen was to
stop showing them to a reader who is not auditing the corpus, rather than to reduce their number.

**The trim that did happen is on the merits and does not move a line**: `record-schema` in
`decisions/` goes sixteen to fourteen, **and the advisory still prints at fourteen**
([[record-schema-is-dropped-from-the-trim-candidates]]).

**One consumer had already made this separation by hand, locally and silently** — the journal gate
hook has been filtering `advisory` out of the gate's output at line 108
([[the-journal-gate-hook]]). Independent evidence for the change rather than an argument for it, and
the third cost of an always-firing advisory this page names is what it evidences: **the lines were
not being read.**

**The three costs this page records are now four.** Unread, managed, indistinguishable from
scheduled-and-skipped — and **routed around by a consumer who never told anybody.**

## The advisories are back on every session, and a verdict is now owed rather than optional — 2026-08-21

**`/ingest` runs `--lint` at every session end** ([[the-tag-density-advisories-run-at-every-ingest]]).
**So this page's own finding — that an always-firing advisory stops being read — now applies to
these lines again, by the owner's ruling and with that finding in front of him.**

**Measured 2026-08-21 by `bash scripts/vault-check.sh --lint`, over a corpus of 490 pages:**

| tag | pages in `decisions/` | threshold |
|---|---|---|
| `vault` | 124 of 193 | ten |
| `process` | 106 | ten |
| `harness` | 98 | ten |

**A tag carried by 64% of a folder classifies nothing.** The run prints 28 advisories in 11.6 s and
exits 0.

**This is a collapse rather than a drift.** The decision this page carries — split nothing yet — was
taken when the densest line was in the thirties; the folder has since grown past the point where the
tag can narrow anything, and the folder-first rule is doing all the narrowing on its own
([[the-folder-is-the-first-narrowing]]).

**The verdict is the owner's and is not taken here.** Split, merge, raise the threshold, or classify
after the fact by a skill — each is a judgement about the corpus
([[dynamic-tag-classification-by-a-skill]], [[the-librarian-writes-unattended]]). **What has changed
is that it will be asked every session until it is answered.**

*(Compiled from `raw/handoffs/2026-08-21-the-mechanisms-are-wired-and-a-pre-task-changes-the-work.md`.)*
