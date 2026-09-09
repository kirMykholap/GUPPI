---
session: 2026-08-16
sprint: S1
commits: 86823e3..0329407
---

# Handoff — 2026-08-16

## 1. State

**Done, four commits.** `5e864f1` pinned markdown to LF and identified the cause of the
`git status` overstatement. `94483b1` taught `/vault-lint` the fifth category and the resolved
contradiction shape. `2036d98` replaced the corpus-wide tag advisory with a per-folder one and put
the folder first in the librarian's narrowing procedure. `0329407` carries the librarian's writes
for S1 criterion 3 — three pages created, five updated.

**Not done.** The supersession of [[lint-waits-for-an-open-sprint]] (decided, not executed); the
rewrite of `index.md`; the mechanism for S1 criterion 4. All three are in §6.

**Next step.** `/ingest`, then the S1 closure decisions still open: the second retitle, `index.md`,
and whether criterion 4 gets a mechanism or a written refusal.

**Checks.** `pytest` and `ruff` were **not run, and correctly so** — nothing under `src/` or
`tests/` was touched all session. `bash scripts/vault-check.sh` exits 0 with five density
advisories, which are the subject rather than a failure. `bash scripts/vault-check-selftest.sh`
caught 62 of 62, missed 0. All seven sources in `raw/` report `INGEST COMPLETE`. No browser walk —
there was no product change to walk.

**Tree, uncommitted at the time of writing.** Two changes, neither of them this session's work: the
owner moved `.claude/agents/vault-librarian.md` to `.claude/agents/vault-libranian/AGENT.md` — note
the typo in the directory name; the agent still resolves because `name:` in its frontmatter is
correct — and an editor reformatted the table alignment in `wiki/entities/vault-feedback-file.md`
with no change of content.

## 2. Entities

- **`.gitattributes`** gained a second rule, `*.md text eol=lf`. It had pinned only `*.sh`.
- **The vault-librarian agent file** moved, by the owner, to
  `.claude/agents/vault-libranian/AGENT.md`. Its content is unchanged apart from `color: purple`
  and this session's edit to the narrowing procedure. The repository's `CLAUDE.md` line 103 named
  the old path and was false for about an hour; **it and every citation in `wiki/` were rewritten
  before this journal was finished** — see the miss in §7 for what the gate did and did not catch.
- **`.claude/skills/vault-lint/SKILL.md`** changed: item 3 now asks which folder a missing page
  belongs in before calling it a missing concept, and item 1 knows that a resolved contradiction is
  not a finding.
- **`scripts/vault-check.sh`** changed shape in its seventh section — see §4.
- **An editor is reformatting vault pages.** Markdown table alignment was rewritten in
  `wiki/entities/vault-feedback-file.md` by something other than this session. It produces diff
  noise and will keep producing it.

## 3. Decisions

**Markdown is pinned to LF, not CRLF, and the rule was not widened.** `eol=lf` because `*.sh` is
already LF, the index was already LF everywhere, and the vault's tooling is `awk` and `bash` on the
host and in the container alike. Rejected: widening to `*.py` and `*.html`, because `tests/` holds
parser fixtures and their bytes are not changing in a commit about line endings. Obliges: the
`.gitattributes` file itself is still unpinned and warns on its own commit.

**Tag density is measured inside a folder, against ten.** Rejected: the corpus-wide count at `>20`,
because folders grow at different rates for different reasons — decisions grow monotonically and are
never pruned, lessons only when something burns us — so an absolute count over the whole corpus
tracks the project's age rather than a tag's power to classify. Ten is not a new number: it is the
reading ceiling already written into the librarian, a property of the reader that does not move when
the corpus does. Obliges: the floor comes free, `archive/` is not measured, and five slices now
print where three did.

**The three tags are not split corpus-wide.** That was the plan that went in with three days of
evidence behind it, and the per-folder measurement refuted it before it was applied: `testing` is 5
of 47 in `decisions/` and 13 of 19 in `lessons/`. Rejected: splitting a tag everywhere to fix one
folder. Obliges: the unit of a split is a tag inside a folder, and it is done by the skill that
brings a proposal rather than by a hand cut nobody can check for lost recall.

**`batches` stays as it is.** Proposed and refused the same day; the four reasons are in §7.

**A title carries no measurable quantity — absolute, no exceptions.** Not "seven AST tests", not
"one librarian with four callers", not "two moments". The technique that removes them: **name what
is being counted instead of counting it** — "staleness is checked before the brief is written and
again before it is read" rather than "two staleness checks". Rejected twice on the way: a version
allowing counts bound to a date, and a version allowing design invariants like *one* finaliser. The
owner refused both, and the rule is unconditional. Obliges: eight titles are out of compliance, and
**three of the eight will be broken by S2 on purpose** — the folder count, the count of rules in
`CLAUDE.md`, and the script count.

**The title's form follows the record's type.** An `entity` is a noun phrase — "the wiki as docs
storage" — and there the label *is* the answer. A `decision` or a `lesson` states its claim, because
the search surface is filenames and a label there makes the result stop answering. This is one of
the fields the per-type schema will define.

**`index.md` and the vault's `CLAUDE.md` get separate roles.** `CLAUDE.md` is for whoever **writes**
a page — the schema, the fields, supersession, contradictions. `index.md` is for whoever **reads** —
hub pages, and nothing else. Measured duplication to remove: the categories table (in both,
near-verbatim), the naming rule (in both), and the current sprint (in `index.md`, while `sprint.md`
declares itself the only place it lives). Cross-links between the two stay; copies do not.

**The repository's `CLAUDE.md` becomes a dispatch table.** "Need to know what is decided → call this
skill. Need to start a slice → call this agent." Rejected: reversing `claude-md-scope` to re-admit
wikilinks — the owner does not want them, and a pointer at a skill is checkable exactly as a pointer
at a page is, because the skill either exists in `.claude/skills/` or does not. Obliges: the four
rules move out into the `rules` type, and "where things are" is either dropped or generated, because
it is the block that has already gone stale.

**`rules` becomes a type in the wiki**, and a script later injects each rule into the zone of the
project it governs, the way Claude's own per-directory mechanism works. S2.

**Ingest changes cadence.** `/handoff` every session; `/ingest` batched at the retrospective over
all journals since the last one. The reason is measured: a dispatch costs 15–30 minutes and the
fixed cost dominates, so three journals in one dispatch cost about one. Obliges: uncompiled sources
accumulate — visibly, because `vault-coverage.sh` reports per source.

**The first measurement to keep is whether the vault is used.** Per session: how many times it was
asked, and how many of those answers changed what the session did. Chosen over coverage or readiness
scales because it needs no scale that does not exist, and because it is the number that decides
whether the store is a tool or ballast.

**S1 criterion 3 is closed in part and retired in part.** Its intent is met — every printed advisory
is named by a `decisions/` page — while its own wording describes a check that no longer exists. The
owner calls it partly closed and partly no longer relevant, and the change belongs in `sprint.md`'s
"Changes to the goal".

## 4. How it is built

**The `git status` overstatement is a stale stat cache, not a line ending.** The index caches each
entry's **size**. Rewriting a file into the other line-ending form leaves the blob identical, so
`git add --renormalize` never restats the entry and the cached size stays at the old form's:
`git ls-files --debug` reported `size: 2496` against a 2455-byte file whose worktree and index
hashes were both `26800c3a`. `git status` then reports it modified for as long as the cache stands.
Reading `git status` twice never helped, because a second read cannot fix a stale cache.
`git add -A` restats and settles it.

**`git checkout-index -f` does not overwrite an existing file** whose normalised content already
matches the index. The file must be removed first. Forcing a working tree to match its attributes is
therefore delete-then-checkout, not a checkout with a flag.

**The advisory derives the folder from the page's path** inside the same pass that already collects
every tag, counts per `(folder, tag)` pair, and prints over ten. `archive/` never matches the
pattern, so it is excluded by construction rather than by a rule.

**Narrowing had a step that the search never used.** The librarian's procedure ran three greps and
all three over `wiki/` whole; the five folders classified pages and no search touched them.
`/pre-task` had been doing folder-first alone the entire time. The caveat that keeps it honest: a
guessed folder is a silent miss, so a question that does not name its kind still searches the whole
wiki.

**Nothing can hang off the repository's `CLAUDE.md` alone.** Rule 5b validates its wikilinks, and
those links deliberately do **not** count towards reachability — a page reached only from
`CLAUDE.md` is already an orphan and already fails. So deleting a paragraph from it cannot strand a
page. What it can lose is an assertion that no page carries, which is what all the observed
staleness has been.

## 5. Lessons

**A plan carrying three days of evidence was refuted by one measurement taken a different way.** The
plan was to split `vault`, `process` and `testing`. Measuring the same tags per folder showed
`testing` at 5 of 47 in `decisions/` — ten percent, a tag doing its job — and useless only in
`lessons/`. The corpus-wide number could not express "healthy here, useless there", and the remedy
it implied would have damaged the tag everywhere to fix one place. The evidence was not wrong; the
instrument was too coarse to see what it was evidence of.

**The session proposed cutting the only working example of the mechanism it was defending.** The
`batches` merge looked right under "make the dictionary smaller" and was proposed in the same
session that replaced that frame with "does the tag narrow inside a folder". Under the new frame
`batches` is a refinement of `collection` — 18 pages narrowed to 5 — which is exactly what the new
rule is built on. A proposal made under one frame must be re-checked when the frame changes, and
nothing prompts that; it was caught only because the owner asked why.

**The rule against numbers in titles had to be applied to the session's own rewrites twice before it
held.** Both attempts to demonstrate it left counts in — "one definition", "two moments" — and the
owner caught both. A rule with exceptions is a rule nobody can apply, and the exceptions were being
added by the same turn that was explaining the rule.

**The unreadable mass in this repository is not the vault.** Measured: `wiki/` is 121 pages and
7,701 lines, averaging 63 lines a page, with nine pages over a hundred. `docs/superpowers/` is 15
documents and **19,959 lines**, the largest plan being **4,864 lines** — seventy-seven wiki pages in
one file. The complaint that an agent writes documents too large to read, which therefore have to be
trusted, points at the plans, and this whole session was spent restructuring the thin half.

## 6. Deferred

| Not doing now | Consequence |
|---|---|
| Superseding [[lint-waits-for-an-open-sprint]] — **decided**, not executed | a `current` page keeps a title falsified in 2026-08-15, and twelve inbound links wait to be moved with it |
| The second retitle, [[two-staleness-checks-at-two-times]] | undecided by the owner; its **filename** is false too, so the cost is higher than the first |
| Rewriting `index.md` down to hubs | the map keeps three copies of what `CLAUDE.md` and `sprint.md` own; audit finding #3 stays open |
| The mechanism for S1 criterion 4 | a `CLAUDE.md` claim can still go stale unnoticed; four instances so far, the newest created this session by a file move |
| Alias-to-page in the dictionary | written as a proposal and not taken; the mechanism that inflates the big tags keeps working |
| `tasks/` | the owner's call, and he does not want to hold that much structure yet |
| The product's own shape — module map, CLI, data model | `entities/` holds fifteen pages, **none of them about the application**; they have no source in `raw/` to be compiled from |
| Moving `raw/` into a dated `archive/` | wanted, and blocked on a path rewriter: **115 of 124 pages cite `raw/` in `sources:`**. Cheaper shape agreed — the ingest that compiles a source moves it and fixes the citations it has just written, leaving one migration pass for the existing 115 |
| Structure inside `raw/` — `plans/`, `specs/`, `notes/` | agreed as nearly free, and still not done |
| `/vault-ask` as a mask rather than a dispatch | the fork is context pollution against tokens and wall-clock, and it is not obvious either way |
| Pinning `.gitattributes` itself | it warns on its own commit; outside the scope of the finding it belongs to |

## 7. Feedback to the librarian

- miss: [[line-endings-make-git-status-overstate-what-changed]] prices the `.gitattributes` fix as
  "one commit that rewrites 59 files and nothing else". Measured at `86823e3` before doing it: all
  161 tracked `.md` are already `i/lf` in the index, so the commit changes exactly one file. The
  52/59 split is the **working copy only** and never reached a blob. Surfaced doing finding #4.
- miss: the same page says the cause of the overstatement "remains unidentified". It is
  identified. The index caches each entry's stat **size**; when a tool rewrites a file into the
  other line-ending form the blob is unchanged, so `git add --renormalize` never restats the
  entry and the cached size stays at the old form's. `git ls-files --debug` showed `size: 2496`
  against a 2455-byte file whose worktree and index hashes were both `26800c3a`. `git status` and
  `git update-index --refresh` then report it modified forever - the "read it twice" ritual never
  helped, because a second read cannot fix a stale cache. `git add -A` restats and settles it.
- miss: `git checkout-index -f` does **not** overwrite an existing file whose normalised content
  already matches the index - `-f` is not enough, the file must be removed first. Cost twenty
  minutes of believing the refresh had run when the working copy was untouched.
- measure: line endings in the working copy at `86823e3`, by extension, CR-containing/pure-LF:
  `md` 97/64, `py` 89/8, `sh` 5/1, `html` 16/0. The split is repo-wide and not a property of
  markdown; five vault scripts sat at `w/crlf` under `attr/text eol=lf` and git said nothing.
  `docker-entrypoint.sh` was `w/lf` and the container was never at risk.
- lint: **the split advisory changed shape on 2026-08-16 and four pages now state the old rule.**
  `vault-check.sh` no longer counts a tag over the whole corpus at `>20`; it counts a tag inside a
  folder against **ten**, the ceiling already written into the librarian ("more than about ten
  pages for one question"). Stale as of that commit: `tags.md` line 10 ("more than ~15-20 pages"),
  [[aliases-carry-the-question-across-languages]] line 65, [[vault-scripts]] line 73, and
  [[dynamic-tag-classification-by-a-skill]] in three places, including the "two numbers for one
  rule" paragraph - which is now one number and wants rewriting rather than deleting.
  *(Discharged inside this session, by the dispatch that produced `0329407`; kept here because the
  transfer into `log.md` is what records that it was owed.)*
- lint: **`batches` stays as it is - the merge was proposed on 2026-08-16 and refused the same day
  by the owner, and the reason it was proposed turned out to be void.** It was a merge candidate
  only under the old frame, where the measure was the dictionary's size and `batches` "selects
  nothing new" as a strict subset of `collection` (verified at `94483b1`: all five of its pages
  carry both). Under the rule adopted the same day the measure is whether a tag narrows inside a
  folder against ten, and `batches` is 3 in `decisions/` and 2 in `concepts/` - nowhere near it.
  Four reasons against, each checkable: (1) `tags.md` records that `collection` was narrowed on
  2026-08-13 at 17 of 29 pages and **bookkeeping is the piece that went out to `batches`**, so the
  merge reverses a recorded split that worked; (2) the dictionary's own merge rule is "two tags
  with near-identical definitions" and these two are not - the act of gathering versus the run's
  bookkeeping - so it was never a candidate by the written rule, only by a subset test invented in
  chat; (3) a strict subset is a refinement, which is the narrowing the new rule is built on -
  `collection` selects 18, `batches` 5 inside them; (4) it would perform the very mechanism that
  inflated `vault`, moving `финализатор` and `parse_batches` onto a tag that selects 18 pages
  instead of 5. Mechanical cost also higher than stated: four of the five pages carry exactly
  `[batches, collection]` and would need a new second tag chosen by hand, three of them in
  `decisions/` where two advisories already fire.
- lint: **two pages owed for S1 criterion 3.** A `decisions/` page naming the five advisory lines
  the new check prints and saying which stand and why - the criterion is met by every printed line
  being named, not by silence. And a `proposals/` page for **alias-to-page in the dictionary**:
  designed on 2026-08-16, not taken, because folder-first narrowing shrinks the problem it solved
  and because a dictionary of pointers drifts into the catalogue `index.md` refuses to be.
  *(Both were written in the same session, by the dispatch that produced `0329407`.)*
- measure: tag density per folder at `94483b1`, the five slices over the ceiling of ten -
  `vault` 19 of 47 in `decisions/` and 11 of 32 in `concepts/`; `process` 18 of 47 in `decisions/`
  and 12 of 19 in `lessons/`; `testing` 13 of 19 in `lessons/`. What the corpus-wide number hid:
  **`testing` is healthy where it was accused** - 5 of 47 in `decisions/`, 10% - and useless only
  in `lessons/`. `process` is 4 of 32 in `concepts/`. The disease is per folder, not per tag.
- miss: **the vault's own `CLAUDE.md` schema does not list the fifth type.** Line 56 still reads
  `type: concept  # decision | concept | entity | lesson - must match the folder`, while the same
  file documents `proposals/` in three other places - the folder table, the boundary with
  `decisions/`, and the rule that a proposal is never a record of something that exists. The
  category was added "in a single pass across five places" and this is a sixth the pass did not
  reach. `vault-check.sh` rule 2 would catch a mistyped page, so the damage is a schema that
  disagrees with the check and with its own file, not a broken store. Surfaced looking up what the
  schema says a `title:` asserts, which it does not say either.
  **This is the third claim living only in a `CLAUDE.md` to go stale with nothing noticing** - the
  `archive/` description was the second and is already in `log.md`. Three instances is a shape, and
  it is the same shape as S1 criterion 4: a `CLAUDE.md` is not a wiki page, no rule reads it, and
  no check compares it against the decisions it contradicts.
- miss: **a fourth instance, created during this session and by a file move.** The repository's
  `CLAUDE.md` line 103 names `.claude/agents/vault-librarian.md`. The owner moved that file to
  `.claude/agents/vault-libranian/AGENT.md` mid-session, and the line became false within the hour.
  Nothing reported it; it was found by reading. Note that the directory name is misspelled and the
  agent resolves only because `name:` in its frontmatter is right.
- miss: **the move broke the gate, and this is the answer to the owner's question about whether a
  script can fix paths after a move.** Moving the agent file left eight files in the vault and three
  outside it naming `.claude/agents/vault-librarian.md`. `vault-check.sh` went red **immediately**
  and named three of them - the three carrying the path in `sources:`. It said nothing about the
  other five, which mention it in prose, nor about the repository's `CLAUDE.md` and two plans under
  `docs/`. So: the detector is complete for citations and blind everywhere else, which is the same
  boundary as every other check here. A rewriter does not have to be perfect where a detector is
  complete; it has to be paired with one, and this move had no rewriter at all.
  *(The directory name was misspelled `vault-libranian` and was corrected during this session.
  The owner then authorised a mechanical path rewrite: six pages in `wiki/` and the repository's
  `CLAUDE.md` now name `.claude/agents/vault-librarian/AGENT.md`. `raw/` was left alone, and the
  two plans under `docs/` were left naming the old path because they are testimony about their own
  date. The gate is green again.)*
- lint: **the owner's model of a skill and a subagent, stated 2026-08-16 and worth a page.** A
  **skill is a role mask** the agent puts on for a specific piece of work, with isolated context; a
  **subagent is an extra body** - called for parallel work, or for a chain of masks worn one after
  another, which makes a subagent essentially a workflow described in advance. The consequence is
  immediate and costly: `/vault-ask` **dispatches** the librarian today, paying 15-30 minutes for a
  search that under this model is a mask the main agent could wear. The counter-argument is already
  recorded - `/pre-task` says the reading must happen outside the main context or it settles there
  permanently. So the trade is **context pollution against tokens and wall-clock**, not cheap
  against expensive, and it is a fork rather than an obvious win.
- lint: **two records are mis-filed because the schema is universal, found 2026-08-16.**
  [[lint-waits-for-an-open-sprint]] is typed `decision` while its title asserts a **state** ("has
  never run"), and [[app-restart-required]] is typed `entity` while its
  `authority: restart-to-see-changes` is an **obligation**. Both are the same defect: nothing in the
  schema says *what a record of each type asserts, and what expires it*. The owner's fix is a schema
  or template per type. The trap to design around: a template nothing tests becomes the next stale
  `CLAUDE.md`, so each template must be a real page the selftest runs through `vault-check.sh`.
- lint: **a mechanism for `CLAUDE.md`, proposed 2026-08-16: it may point and may not assert.**
  Three facts from the code: rule 5b already validates every `[[wikilink]]` in the repository's
  `CLAUDE.md` and has a selftest case; `claude-md-scope` removed every wikilink from that file, so
  the check currently guards nothing; and those links deliberately do not count towards
  reachability, so **nothing can hang off `CLAUDE.md` alone** and a deleted paragraph can never
  strand a page. What it can lose is an assertion no page carries - which is what all three
  staleness failures were. Checkable approximation: every normative paragraph carries at least one
  link into the vault. *(The owner declined the wikilink half: he wants that file pointing at skills
  and agents instead, and a named skill is checkable the same way a named page is.)*
- lint: **an editor is reformatting vault pages.** Markdown table alignment in
  [[vault-feedback-file]] was rewritten by something other than the session or the librarian -
  content byte-identical, padding changed. It produces diff noise on pages nobody edited, which is
  the same class of false alarm as the line-ending churn, and is worth knowing before it is mistaken
  for a librarian write.
- measure: **the vault changed what the session did five times on 2026-08-16, out of five lookups**
  - [[the-growth-signal-is-the-brief]] and [[an-unsourced-number-is-dropped-not-chosen]] stopped a
  threshold being invented; `tags.md`'s record that `collection` was split killed the `batches`
  merge; [[the-librarian-writes-unattended]] stopped a direct write to `tags.md`; the brief's hook
  about fragile selftests shaped how the rule was added. **Four of the five were about the vault's
  own machinery**, and the one about the subject came from the owner, not from the corpus. This is
  the measurement the owner chose to start with: lookups per session, and how many changed a
  decision.
- measure: **the librarian dispatch of this session cost 115,165 subagent tokens, 46 tool uses and
  13 minutes 22 seconds**, and produced three pages, five updates, a `log.md` entry and a
  regenerated catalogue. It is the fifth measured writing dispatch and sits inside the 14-29 minute
  band already recorded.
- measure: **`wiki/` is 121 pages and 7,701 lines, averaging 63 lines a page, nine of them over a
  hundred; `docs/superpowers/` is 15 documents and 19,959 lines, the largest 4,864.** Measured
  2026-08-16 while answering why the store feels bulky. The store is the thin half of this
  repository, by a factor of two and a half.

## 8. Anything else worth keeping

**The owner named the problem the whole structure exists to solve, and it is worth quoting rather
than paraphrasing:** an agent writes large documents with no structure, they cannot realistically be
read, so they are trusted; details inside them are wrong; the agent goes and builds the wrong thing;
and the correction cycle repeats. The measurement in §5 says where that lands — the plans, not the
vault.

**This project already invented the answer and applied it in exactly one place.** `sprint.md` gives
every acceptance criterion **the command that decides it**, so the owner does not read to verify — he
runs something. No plan or spec under `docs/superpowers/` has anything of the kind. A plan step that
cannot be verified by running something is a step that has to be trusted, and that is the whole
mechanism of the complaint above.

**Three of the eight titles that break the new naming rule will be broken by S2 by design** — the
folder count, the count of rules in `CLAUDE.md`, and the count of scripts. Whoever executes S2
should expect to rename them as part of that work rather than discover them afterwards.
