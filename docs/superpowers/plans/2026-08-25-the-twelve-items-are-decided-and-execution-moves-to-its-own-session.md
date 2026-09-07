# The twelve items are decided, and execution moves to a session of its own

> **For agentic workers:** this plan overrides the `writing-plans` default of subagent-driven
> execution. This project writes its code in the main session — see `CLAUDE.md`, «How a slice is
> executed». Librarian dispatches are the exception, because `wiki/` has exactly one writer.

**Written 2026-08-25. Nothing here was built that day.** The owner set twelve items, all twelve were
worked to a decision, `/pre-task` checked the resulting plan against the tree and killed one item of
it, and he moved execution out on the grounds of size. This document is the executable half; the
reasons are in the vault.

**Read the vault before starting.** Every design below rests on a ruling compiled from the journal of
2026-08-25. Where this document and a `wiki/` page disagree, the page is newer.

---

## A. Three harness defects

### A1 — except the per-folder schemas from the one-writer note

`.claude/hooks/ask-the-vault.ps1` sets `$inWiki` at :166 for any path under the vault's `wiki/` or
`archive/`. That flag is read in **two** further places: :210 prints the one-writer note, and :277
excludes the vault from the pre-task net.

**Do not narrow `$inWiki`.** Narrowing it would take the schema files out of the pre-task exclusion as
well, against the decision that every vault path class is excluded from that net. Add a **separate
flag consumed only by the :210 branch**.

The schemas are the session's to write by the decision of 2026-08-19, so the note is false there.

**Case in `scripts/hook-selftest.ps1`, asserting on output rather than exit code** — the hook exits 0
either way. The note fires today and must not after; that discrimination is the proof.

**One page needs a dated note.** The page holding that the one-writer note's scope is untouched says
narrowing it would reverse the direction the owner chose. The 2026-08-19 clause is the ground for
doing it anyway, and the page is `current` and says the opposite direction. Write the note; do not
leave it silent.

### A2 — record, build nothing

The obligation to regenerate a deleted `catalogue.md` is already gone from the vault's own
instructions, which now state the opposite. `sprint.md` still carries it as work. **The librarian
strikes the line rather than correcting it**, on the rule that a drifting list is repaired by deletion.

### A3 — four menu states, not three

`scripts/session-dialogue.py:253` increments `answers` only inside the `tool_result` branch, so a menu
the owner interrupts and answers in prose counts as an answer lost — and answering in prose is his
documented preference.

**Four states:** answered by selection; interrupted and answered in prose; still open; genuinely lost.
They are separated by whether a `tool_result` exists, whether a later turn exists, and whose it is.

**This widens a ratified scope** — the sprint and the decision page both say *three*. The owner
approved the widening on 2026-08-25 and **the decision page takes an amendment note dated that day.**

Cases in `scripts/session-dialogue-selftest.py`.

## B. The `the owner said it` mark repair

The verbatim obligation already exists in `.superpowers/sdd/vault-feedback.md` and is absent from the
rule text rendered into `CLAUDE.md`. Four renderings of one instruction; the injector writes three.

### B1 — the obligation reaches `CLAUDE.md` through the rule that already carries it

The rule page holding that a block attributed to the owner is written in his own Russian **already
carries the claim in its `<!-- text -->` slice** and governs the handoff and ingest skills.
`CLAUDE.md` is not among its destinations, and that is the hole.

**Add `CLAUDE.md` to that page's `governs:` list.** Do not write the same claim into a second rule —
two rule pages asserting one claim is what the admission rule and the whole reason regions exist both
forbid. The inline list form is legal; the YAML block form is red.

**Add the context requirement to the same slice**: a quotation carries the context it was given in,
not the sentence alone.

### B2 — CANCELLED

A fourth `governs:` address pointing at `.superpowers/sdd/vault-feedback.md` is forbidden by name. The
file is git-ignored and `/handoff` empties it every session, so the injector reports a destination
carrying no region and exits 1, which reddens rule 12 and locks out the only writer who could clear
it. A previous `/pre-task` killed this same proposal and a `lessons/` page records it.

### B3 — the catcher marks an unquoted attribution, and its blind spot is written down

`.claude/hooks/catch-the-feedback.ps1:187-189` already files an undeclared kind **with a note** rather
than dropping it. Follow that shape for a `decision:` record containing `the owner said it` and no
Cyrillic byte (208–211). A note, never a refusal — the alphabet verdict is ruled advisory.

**Write the blind spot down rather than implying the channel is closed.** The byte test catches an
English paraphrase and cannot catch a Russian one: `log.md` holds 32 records carrying
`the owner said it`, of which 15 carry no guillemet quotation and all 15 are Cyrillic. The real
discriminator is the absent quotation, not the alphabet.

Case in `scripts/hook-selftest.ps1`, proved by removing the guard.

### B4 — mark fifteen records, do not rewrite them

- **The population is 15, not 8.** The eight are the marks in the feedback file on 2026-08-24; in
  `log.md` there are fifteen. Hand the librarian a measured list.
- **`log.md` is never rewritten, at all.** Append **one new record naming the fifteen**, not a clause
  on each existing line.
- **The note is dated 2026-08-24**, the day the text became false.
- **The wording is that the owner chose not to restore the words** — option three of three — never
  that recovery is impossible. A `basis: measurement` lesson says an extract recovered all eight in a
  minute, and that page takes a dated note of its own.

## C. The sweep of 27 owner-attributed blocks, and the rule that finds them is retired after it

27 blocks across 23 pages: 25 in `decisions/`, 1 in `lessons/`, 1 in `rules/`. All 27 were read; none
is a genuine English quotation from the owner.

**The order is forced.** Cancelling the rule removes the instrument that produces the list, so:

### C1 — freeze the list first

Write the 23 pages and the claim each block carries into the ratification page, **by page and claim,
never by line number** — the same edit moves every line.

**Say on the page why this is not the copy that drifts.** A prohibition holds that the list is read
from the run and never from a page, because a figure written there would drift. This writes pages and
claims, no numbers and no line numbers. Thread it out loud or the next `/pre-task` reads a breach.

### C2 — rewrite the 27

The blockquote goes, the `owner:` signature goes, the attribution of the decision stays as prose, and
each rewritten block cites the ratification page. **`basis: human` stays on all 23 pages.**

**Write on the page that this answers carried sprint item 12**: a paraphrase surviving ratification is
not demoted to `basis: inference`; it stops being a quotation instead. That item has been open since
2026-08-22 and gets its answer nowhere else.

The duplicate — one claim byte-identical on two pages — loses its signature in both copies. Merging
them stays deferred.

The block in the language rule page sits outside its slice, so `CLAUDE.md` does not change.

### C3 — then retire the alphabet rule

**Owner, 2026-08-25: the Cyrillic test is overturned.** Cyrillic does not mean the words are his — 15
Cyrillic records carry no quotation and the byte test flags none of them; and a genuine English
quotation from him exists, which is why the verdict was advisory in the first place.

**This is a supersession of a prohibition page**, not an edit. What carries the weight instead is the
ratification step in `/retro`, which puts every attributed line to him before it can become a page.

**Its selftest cases are deleted with it, not repaired.** One case grades by requiring the advisory
heading to appear, and it appears only because the corpus holds the 27; the parity cases pinning the
flag go too.

**Acceptance changes with it:** 27 rewritten against 27 frozen, counted. Not an empty advisory.

### C4 — say what the sweep does not cover

The page the sprint names as heading the sweep is already ratified in the owner's own Russian, dated
2026-08-22, and says so in a section of its own. `sprint.md` still lists it as pending. **Strike that
line**; it is a stale register entry, not work.

## D. The entity split for the gate and its suite

`wiki/entities/vault-scripts.md` **keeps its filename and its `authority:` slug** — 79 pages and 107
occurrences under `wiki/` link to it and no address moves.

**The owner's order:** `vault-authority.sh --near` (done 2026-08-24) → **read the family by hand** →
split → delete the list.

- The page stays the **hub**: what the scripts are together, the write ritual, the shared pass, what
  they will not do, **and every dated history section**.
- Two new pages take the subject description **without history**: the gate (`vault-check.sh`) and the
  suite (`vault-check-selftest.sh`). Both need **new** `authority:` slugs.
- **Do not restate mechanism.** Two `concepts/` pages already hold the gate's cost decomposition and
  the suite's mutation-test shape.
- **Sections move whole, never split.** Cutting a paragraph that covers two scripts rewrites a
  sentence a source asserted.
- **The eighteen-condition list is deleted**, not moved. "Nothing is ever deleted" is about pages.
- The prose counts *ten* and *thirteen* are deleted: both families hold 15. A third stale copy sits in
  the register's own note; it is dated, so it stands where it is.
- **The two gauges already routed land here**, each on its own page — the pages-owing-a-move gauge on
  the archive script's entity page, region coverage on the new gate page. **D runs before E's gauge
  writes.**

## E. The `measure` mechanism

### E1 — `scripts/vault-measure.py`, three modes, and no number is ever typed

- **write**: `--page <slug> --role gauge --subject <slug> --command <command>`, or
  `--role testimony --value <text> --conditions <text>`.
  **A gauge takes no `--value`.** The line carries the subject, the command and the date.
- **`--refresh`**: walks every `measure` region, **runs each gauge's command and writes the number
  beside it.** The librarian runs it at the end of an ingest. A command must print exactly the line
  wanted.
- **`--check`**: shape only, **executes nothing.** The gate runs this one.

**This is what keeps the live prohibition intact**: a gauge that can be printed is never written by
hand, and here no hand writes it. **The prohibition page takes a dated note naming the mechanism**, or
a later `/pre-task` reads a contradiction.

Refusals, exit 2: slug not found; slug in two folders; a gauge with no `--command` or no `--subject`;
a testimony with no `--conditions`; a gauge subject already carried by another `current` page.
Testimony appends and is never replaced; a gauge is replaced by subject.

**Name the deferral the fifth refusal touches.** A decision defers the gauge-uniqueness **verdict over
the corpus** and rejects building it beside the decision. What is built here is a **writer's refusal**,
which is a different thing — say so, or this builds the rejected alternative under another name. **That
deferral page takes a note**, on the owner's ruling of 2026-08-25.

**Exit codes: name the fork.** 2 is a usage error in the gate, the catalogue, the coverage and the
authority scripts, while the archive script uses 2 for refusals as well. This follows the archive
precedent, so **E2 parses lines and not the code** — the shape rules 12 and 13 already use.

### E2 — a gate rule that asks by running `--check`

With a `missing file` note, so a deleted script reddens the gate rather than silently disabling the
check. The shape of rules 12 and 13.

**The real cost is not 1.5 seconds.** The suite runs the gate about 171 times against a 34m8s total,
so this adds roughly **four minutes** to a run the owner asked to shrink.

**Before the full run**, confirm the new `missing file:` note cannot fire inside the renamed-vault
case's sandbox: its grader greps for exactly `missing (directory|file):`.

### E3 — rule 11 recognises the marker explicitly

Declare a `measure` marker out of scope rather than letting it escape the malformed verdict by an
accident of spelling. The precedent is the generated-file marker recognised in the same rule for the
same reason.

**Say out loud that rule 11 walks the harness sweep alone.** A measure region inside a `wiki/` page —
where every region will live — is not checked by it at all. Only E2 reaches those.

### E4 — a rule page obliging the script

`governs:` names `.claude/agents/vault-librarian.md`, `job_hunt_ai_vault/CLAUDE.md` and
`.claude/skills/ingest/SKILL.md`. The instruction to run the gate after a write lives in three
hand-maintained copies today; do not add a fourth.

**The vault's own `CLAUDE.md` gains its first region** — no rule page governs it, and it is one of the
seven files in acceptance criterion 4's shortfall. **Region coverage goes from 8 of 15 to 9 of 15.**
Report the number; reading the criterion is the owner's.

**Before the 38-minute run**, check the prediction that the first rule governing a file inside the
vault reddens the renamed-vault case. A 2026-08-19 regrading probably defused it and two `current`
pages disagree: `bash scripts/vault-check-selftest.sh --only "the vault is renamed"`, two minutes.
Either way, that page takes a dated note.

### E5 — the destination bracket widens, by supersession

The page listing the legal destination values is a prohibition, and widening the list **changes its
claim**: successor with `supersedes:`, old page `deprecated` with `superseded_by:`, moved to
`archive/`. New form: `[gauge:<page>/<subject>]` for a gauge, one name for testimony.

### E6 — cases for every refusal, each proved by removing the guard

## F. The first lessons-collector run

**A reading dispatch that writes nothing.** It reads the queue — 157 lessons, 106 cited by neither a
rule nor a proposal as of 2026-08-25 — plus `rules/` and `proposals/`, so it does not propose what is
already covered, and runs the `--near` lookup before every candidate. **It returns families and
proposal drafts as its result.**

`.claude/skills/vault-lint/SKILL.md` is rewritten: :47 and :99 currently tell the dispatch to write
`proposals/` and append a `lint` entry.

- **The old ordering argument goes with it.** The skill puts this dispatch first *because it writes*.
  Once it writes nothing, that ground is gone; do not leave it standing.
- **It does not write a line into the brief.** The brief is derived and never a source. The librarian
  writes the **pages**, and the brief carries them by generation. The `lint` entry with its four
  numbers stays in `log.md`, or a run that found nothing stops being distinguishable from a run that
  did not happen.
- **The queue is not cut into batches.** The seventh lesson looks like the first from anywhere that
  cannot see all seven.

The librarian writes the pages afterwards. **The owner decides**; writing a proposal is not acting on
it.

## G. The librarian's channel to the session

Born in the retro of 2026-08-25, on the owner's ruling that the current mechanism looks wrong.

**The librarian stops writing into `.superpowers/sdd/vault-feedback.md`.** That file is a channel for a
party that cannot write files — a session in plan mode — and the librarian can. Its findings go to
`log.md`, which the vault already defines as the librarian's actions and the misses reported against
it.

**What is addressed to the session reaches the brief by generation**, surfaced from `log.md` by
whatever writes `brief.md`. The librarian never hand-writes a derived file.

**Why this is not cosmetic:** `/handoff` runs before `/ingest`, so anything the ingest writes into that
file is drained by the *next* session's handoff and filed under the wrong session. On 2026-08-25 the
file held 115 records and roughly a third belonged to the previous session's ingest.

---

## Order

1. **F is dispatched first** — it only reads, and the tree is untouched. 30–45 minutes in the
   background.
2. **While it runs: A and E.** These are session files, not `wiki/`; no overlap with the dispatch.
3. **Cheap checks before expensive ones:** `--only "owner block"` and `--only "the vault is renamed"`,
   two minutes each, **before** the 38-minute run.
4. **Librarian writes, serially** — `wiki/` has one writer. First dispatch **C + B**, second **D**.
   **D precedes E's gauge writes.**
5. **F's result** goes to the librarian last.
6. **G** with the other harness work.
7. **`vault-measure.py --refresh`** at the very end, after every write.

## Deferred, with reasons

- **The flag that skips rules 12 and 13, and the prohibition behind it** — the owner could not decide
  on 2026-08-25 and said so. Both forms are recorded with their cost: a mode that issues no verdict
  leaves the prohibition untouched; a flag requires overturning it by supersession. **This is the third
  deferral**, and by the rule agreed that day it must now name the sprint it happens in or be refused.
- **The `closed_by:` register for rule closures** — 1.5–2 hours. The design is complete: a field in
  `wiki/rules/` with two spellings, `case:<name>` verified against the suite's own `--list` and a
  `[[wikilink]]` verified as a current decision page; declared optional, back-filled across all
  sixteen pages, then promoted to required, with the promotion as the acceptance test.
- **The archive sweep** — designed. First run measured: two pages, both `implemented`, both pass the
  precondition, so it moves both and refuses nothing. Refusals are reported by the sweep with a
  non-zero exit and counts; the gate stays silent about placement.
- **The librarian printing each criterion's decider output into the brief** — deferred by the owner, a
  fourth time. The unnamed obstacle is now measured: two of four criteria are decided by a 38-minute
  suite.
- **The two unbuilt clauses of acceptance criterion 4** — a rule reading the content of `index.md`, and
  rule 5b covering a second kind of target. Rule 5b is vacuous today: the repository `CLAUDE.md` holds
  zero `[[wikilinks]]`, so it can never print, while naming four skills nothing verifies.
- **The suite's 37m44s reading and the forty-per-cent machine drift** — untouched by the owner's
  ruling, set for a later session.
- **Two homeless repairs from the retro**: deciding a reversible fork instead of presenting it is about
  *when* a session asks and the register holds no family for that question; and the session shape — one
  item carried through discussion, decision, build and verification rather than twelve carried to
  discussion — belongs to the sprint.

## Verification

Each exit code read from its own invocation.

```
bash scripts/vault-check-selftest.sh --only "owner block"           # 2 min, BEFORE anything
bash scripts/vault-check-selftest.sh --only "the vault is renamed"  # 2 min, BEFORE anything
bash scripts/vault-inject.sh                                        # 0/0/0/0
bash scripts/vault-check.sh                                         # exit 0
bash scripts/vault-check.sh --lint                                  # exit 0
uv run python scripts/vault-measure.py --check                      # exit 0
pwsh scripts/hook-selftest.ps1                                      # caught N, missed 0
uv run python scripts/session-dialogue-selftest.py                  # caught N, missed 0
bash scripts/vault-check-selftest.sh                                # ~38 min, once, at the end
```

**Acceptance in substance:** 27 rewritten blocks counted against 27 frozen on the ratification page;
`vault-measure.py` refusing on each of its five conditions, every refusal proved by removing the
guard; and `--refresh` writing a number that was not in the line before it ran.

`ruff` is not run: `src` and `tests` are untouched, and the project command does not cover `scripts/`.
