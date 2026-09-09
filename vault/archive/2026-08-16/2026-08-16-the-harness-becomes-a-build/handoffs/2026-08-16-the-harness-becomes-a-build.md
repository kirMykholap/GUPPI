---
session: 2026-08-16
sprint: S1
commits: none
---

# Handoff — 2026-08-16

## 1. State

**A design session end to end. No code, no commits, nothing under `src/` or `tests/` touched.**
It ran past midnight into 2026-08-17; both dates belong to one session and the artefacts are filed
under the day it began.

**Done.** The harness has a design: it stops being maintained and becomes a build. Every record type
has a settled field schema. `raw/` has a settled meaning and artefacts have a home. All of it is in
`docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md`, which is **the substance of this
session** — this journal records what was decided and why; the spec carries the shape.

**Not done.** Nothing is built. Three items block construction: the handoff template's final form is
designed but not written to disk, the `asserts:` predicate set is not agreed, and the marked regions
are designed but no file carries one.

**Checks.** `pytest` and `ruff` were not run, correctly: `src/` and `tests/` were not touched.
`vault-check.sh` was not run either — nothing was written under `wiki/`. The only writes were two
untracked files and three lines into a git-ignored draft.

**Next step.** Agree the `asserts:` predicate set, then write the template to
`.claude/templates/handoff.md`, then mark up the first two files.

## 2. Entities

**Appeared, both untracked at the time of writing:**

- `docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md` — the design, four parts.
- `.claude/skills/grill-me/SKILL.md` — **added by the owner mid-session.** It interviews in rounds:
  a design tree, a frontier of questions whose prerequisites are settled, each asked with a
  recommended answer, and facts gathered by the interviewer rather than asked of the user. It drove
  the whole second half of this session.

**Changed:** `.superpowers/sdd/vault-feedback.md` — three entries, all misses, all in section 7.

**Designed and not existing:** `wiki/rules/`, `archive/<date>/`, `.claude/templates/handoff.md`,
`harness-build`, `harness-gate`, the `authority` register, the staleness detector.

## 3. Decisions

**The harness is compiled, not maintained.** A rule is written once as a page; the harness file is
its output. Rejected: the librarian maintaining `CLAUDE.md` and hooks — it never deletes text, and a
harness file must shrink, so the invariant that makes unattended writing reviewable is exactly what
makes it unfit to keep one. Rejected too: leaving the harness outside anyone's zone, which is the
status quo that produced every recorded staleness.

**No symlinks.** Measured rather than argued: `core.symlinks=false` in this repo, and `ln -s`
produces a copy on this machine. A committed symlink would check out as a text file holding a path,
so `CLAUDE.md` would contain one line and no instructions. It would also hard-code the vault's
directory name, which nothing may do.

**A harness change is recorded the moment it is decided**, as a marked line in `vault-feedback.md`,
and cut out at ingest on a section boundary. Rejected: an agent classifying prose as harness-related
at ingest — a classifier detects presence and cannot detect absence, so a missed rule would be
unbounded and silent.

**The librarian keeps its monopoly on `wiki/`** and writes both the decision page and the rule page.
The steward is scripts that run after it, not a second agent. Rejected: a parallel steward — two
unattended writers already lost a write on 2026-08-14, and a lost update leaves no trace in
`git diff`. Sequencing costs nothing, because the steward's half is a script.

**`/ingest` runs after `/handoff`, at the end of a session.** This corrects the wording of
`ingest-is-batched-at-the-retrospective`, and it exposed a real ambiguity: **"retrospective" names
two different rituals** — the one at the end of every session and the one at the end of every
sprint. The owner's decision is to **rename the end-of-session skill** so the word stops meaning two
things. Batching survives as the shape of a single dispatch: one dispatch, sources compiled one at a
time inside it, because the measurement the cadence rests on only holds for one dispatch.

**`raw/` holds testimony, not artefacts.** A journal is testimony; a spec and a plan are artefacts —
an instruction that was executed. Measured: the journal of 2026-08-16 is 75 units and cost a 15–29
minute dispatch; a spec is 175–289 units and a plan 354–525, and `docs/superpowers/` holds 16 644
lines of plans against 2 488 across all six journals. Roughly ten times the present ingest workload,
every unit owing a verdict. The mechanical proof is S1's own criterion 2: a spec placed in `raw/`
breaks *every source reports `INGEST COMPLETE`* by construction.

**`archive/<date>/`, dated by session, holds everything that left the working set that day** — the
journal, its sidecar, the specs and plans, **and the pages retired that day**. `raw/` becomes an
inbox that is empty between sessions, which is the owner's stated want: the uncompiled set visible
by looking rather than by running a script over every file. Rejected: a separate `sessions/` folder,
which would keep `archive/` single-meaning at the cost of the one date-ordered entry point.

**The sixteen artefacts under `docs/superpowers/` migrate**, in the same wave as the 115 pages
citing `raw/`. Rejected: leaving them, which preserves a mutable location thirteen pages depend on.

**The core is eight fields** — `title`, `type`, `status`, `created`, `sources`, `tags`, `sprint`,
and the new `updated`. The test for admitting one is in §4.

**`decided` stays** on decisions: only 8 pages of 58 carry the date in their H1, so for fifty it is
the sole carrier, and batching widens the gap between deciding and writing. Rejected: dropping it,
which would make every decision of a sprint look taken on the day of its retrospective.

**`supersedes` stays and gains a symmetry rule** — the schema demands the link in both directions,
explains why, and nothing checks it, so `A supersedes B` with `B` silent passes today.

**`proposals` is left as it stands, with a mark to revisit.** The defect is recorded, not fixed: two
statuses, three states, so `deprecated` cannot distinguish *built* from *refused* — the question the
category was created to answer.

**`entities` will describe the application** — one page per package, written when that area is
worked, with no coverage numbers. Sequenced **after** `asserts:` and the staleness detector exist,
because without them it is a second "Where things are" and rots on schedule.

**The handoff template moves to `.claude/templates/handoff.md`, loses its numbers, and gains a
`Harness` section last.** Both skills point at it rather than carry a copy. The owner's corrections
are a **marked token in place**, not a section of their own — a marker written by a human is
authorship rather than classification, and it keeps the correction beside the claim it corrects.

**A paragraph becomes a rule page if it is imperative and not enforced by a test.** Where a test
holds the rule, the test is the rule.

**One page, `harness-layout`, says what lives where**, and carries the file list in `asserts:`, so a
harness file nobody described turns the gate red.

## 4. How it is built

**The field test, refined by the data.** A field earns its place if **(a) something reads it and
fails without it, or (b) it independently restates a fact the tree already asserts, so a
disagreement catches a writer's error.** (b) is a checksum, not duplication: `type` and `status`
agree with their folder on every page of the corpus and always have — the checksum has never fired,
which is not the same as being idle.

**Four delivery modes, and the division is forced by the destination's physical shape**, not chosen
as a taxonomy. `region` — the file is hand-written and only a piece comes from the page. `whole` —
the file has no hand-written part at all, and **JSON cannot carry a marker because it has no comment
syntax**. `zone` — the destination does not exist yet and the injector creates `<dir>/CLAUDE.md`,
which is how a rule reaches a reader *before* the work rather than by search. `none` — there is no
text destination; only the page's `asserts:` reach the tree. Remove any one and some file becomes
undeliverable.

**Two mechanisms, two different failures.** A marked region keeps the harness **saying** what the
vault holds. `asserts:` keeps the tree **being** what the rule claims. The first catches the ingest
skill contradicting the cadence decision; the second catches "four types where five folders exist",
and a path that a file move made false.

**`asserts:` is a closed set with a flat, line-oriented syntax.** Closed because the pages are
written unattended, and an arbitrary shell predicate would let the store execute what an agent
wrote. Flat because there is no YAML parser available: PyYAML is absent, the stdlib has none, and
the existing scripts parse frontmatter line-wise in awk. An unknown predicate name is itself a
failure, which is what makes the set closed in fact rather than in wording.

**The staleness detector, whose inputs already exist.** For each page, compare `updated` (else
`created`) against the last commit of every source that is a live file of the tree; a newer source
means the page is **suspect**. One `git log --name-only` pass dates everything at once. Coverage is
**91 pages of 142**; the other 51 cite only the immutable `raw/` and are invisible to it, although a
page compiled from a journal can go stale against the code exactly as any other can. This is the
instrument for the gap the vault already named and measured — *fidelity to the tree: checked by
nothing*, with six pages measured on 2026-08-15 as describing what the repository no longer does.

**`updated` is stamped by a script from the diff and carries no weight it cannot hold.** It means
bytes moved, not that anyone re-read the sources, so it must not clear a suspicion — a typo fix
would clear it silently, in the dangerous direction. The suspicion is a **finding, and a finding
carries an outcome**, which is how every other finding here is closed. Two mechanics: the stamper
compares content **excluding its own line**, or it re-triggers on itself; and the write ritual
becomes **stamp → catalogue → check**, because stamping modifies files.

**`authority` needs a register, on the model of `tags.md`.** The librarian's own definition never
mentions the field — the only party that fills it is nowhere instructed how to choose a value, and
there is no register to look in. **133 unique slugs on 133 pages is the predicted result of having
nothing to consult**, and it turns the field from a preventer of duplicates into a detector that
fires only when someone reuses a formulation, which is when they had already noticed the overlap.
With a register the field becomes rare rather than universal, and the check moves to write time.

**`basis` gets an enumeration check.** It is the only field conflict resolution rests on — a page on
`human` outranks one on `inference`, which is what will let the owner's marked corrections outrank
agent testimony — and today `basis: banana` passes.

**Marked regions: form and failures.** A paired HTML comment named for the rule's slug, alone on its
line at column zero, no nesting and no overlap. **A marker inside a fenced block does not count** —
the check's existing fence-stripping pass is reused, and its two recorded scars are exactly this
error. Four verdicts: a region with no page, a `render: region` rule with no region, and two rules
into one region are all red; text outside regions is allowed and unchecked.

**Three layers over the prose that stays outside regions**, because that last verdict is the real
hole: the regions themselves; a grep for imperative words outside them as a cheap approximation —
which is the check already proposed in the vault, and **103 hits across ten files**, a list one can
work through rather than a fog; and the semantic pass of `/vault-lint` once per sprint. Plus a
coverage number per file in the gate's output, which turns an invisible hole into a number that
shrinks as markup proceeds.

## 5. Lessons

**The gate guarantees agreement, never truth — and it was demonstrated live.** A rule text drafted
in this session said `/ingest` runs at the retrospective; it was wrong, and the owner caught it by
reading. A wrong rule renders into the harness flawlessly. Nothing in this design defends against an
error of content; only reading does. This belongs written beside the design, because otherwise the
mechanism reads as stronger than it is.

**Three divergences were found in one session, all by reading two files side by side**, which brings
the running total to seven and confirms the shape: no rule reads a `CLAUDE.md`, and no rule compares
a skill against a decision. They are in section 7.

**A field with no register produces unique values by default.** `authority` was designed as a
uniqueness declaration and behaves as a per-page invention, because the mechanism was copied from
tags without the machinery that makes tags work: a dictionary, an obligation to consult it, and an
obligation to record the rejected word. Any future field claiming uniqueness needs its register in
the same breath.

**`rg -o` without a capture group silently disarms a duplicate check.** The vault's own schema
documents `rg "^authority:" wiki -o | sort | uniq -d`; it prints the literal field name once per
match, so it reports a duplicate whenever two pages carry the field and never compares values. The
script implements it correctly, so **only the documentation was false — which is the worst case**:
nothing fails, and the reader who follows the documentation learns nothing.

**Measurement settled two questions that argument could not.** Symlinks died on `core.symlinks=false`
and an `ln -s` that produced a copy, not on preference. Ingesting specs and plans died on 75 units
against 525, not on taste. Both had plausible arguments on either side until a number arrived.

**Interviewing in rounds worked, and its discipline is the transferable part**: ask only the
questions whose prerequisites are settled, give a recommended answer with every one, and go find the
facts rather than asking for them. Four turns of this session changed a recommendation because a
fact came back different from the guess.

## 6. Deferred

**The `asserts:` predicate set** — four sketched; the full set and the rule for growing it are not
agreed. Cost of waiting: nothing downstream can be written, including the entity pages about the
application.

**The `authority` register** — agreed in principle, undesigned: where it lives, who writes it,
whether it is generated, what the librarian owes before minting one. Cost: the field goes on
behaving as a per-page invention.

**Mechanising the title rule** — eight titles carry a measurable quantity and nothing checks it.
S2's criterion 2, open since the rule was written.

**A home for ideas** — S2's second blocking question, untouched. An idea is pre-design and
`proposals/` holds designs.

**The gates at session start** — parked by the owner as not a priority; routing stays manual.

**Naming the steward** — trivial and open.

**The markup itself** — which regions exist in which files. Gradual, starting with
`.claude/skills/ingest/SKILL.md` and the repository's `CLAUDE.md`, both of which have recorded
divergences already.

## 7. Feedback to the librarian

- `miss:` `claude-md-can-lose-an-assertion-but-cannot-strand-a-page` — the prose says "Four
  instances are now on record" while the table beneath it lists five rows (1–2, 3, 4, 5). The page's
  own stated count drifts from the list it heads, which is the shape it links to. Surfaced while
  reading it for the `CLAUDE.md`-staleness discussion.
- `miss:` **harness against vault, a live contradiction.** `.claude/skills/ingest/SKILL.md` line 9
  says *"One source at a time — never batch several handoffs"*, while
  `decisions/ingest-is-batched-at-the-retrospective.md`, decided 2026-08-16, says ingest runs once
  over every journal since the last. The skill's last commit, `f7f654e`, predates the decision.
  Sixth recorded instance of a harness file asserting something false, and **the first found between
  a skill and a decision rather than inside a `CLAUDE.md`**. Surfaced while measuring how `/ingest`
  would have to change.
- `miss:` **the vault's `CLAUDE.md` documents a broken check.** Under `### authority` it gives
  `rg "^authority:" wiki -o | sort | uniq -d` as the way to find contradictions. With `-o` and no
  capture group that prints the literal `authority:` once per match, so it reports one spurious
  duplicate whenever two or more pages carry the field — 133 of 142 on the current tree — and never
  compares the slugs. The correct form needs a capture: `rg '^authority: *(.*)' -o -r '$1'`.
  `vault-check.sh` rule 3 implements it correctly, from frontmatter and `current` pages only, so the
  mechanism works and only its documentation is false. Seventh recorded instance. Surfaced while
  trying to explain the field to the owner.

## 8. Anything else worth keeping

**Two of the four questions blocking S2 are answered by this design.** `rules` is a sixth folder in
`wiki/`, and the move of `raw/` into a dated archive is designed whole. The two that remain are the
home for ideas, and whether product work interleaves.

**S1's tail may now be met.** Criterion 4 asked for *a check that fires, or a written decision that
there will be none*. A check is now designed, and the criterion's own words ask for "a working
answer" rather than a built mechanism. That reading is the owner's to confirm.

**The agreed order of work is 1 → 3 → 2:** the handoff template first, because ingest, the
end-of-session ritual and the harness section all depend on it; then the marked-region rules; then
the `asserts:` predicates. The first is complete; the second is complete but for the predicate set.

**Telling the spec-writing skill where to write is the first real use of the mechanism** — a line in
`vault-feedback.md`, a rule page, `governs:` on the skill file, a rendered region, the gate. Work
that was queued anyway, not an exercise.

**`grill-me` is untracked** (`.claude/skills/grill-me/`), as is the spec. Neither was committed.
