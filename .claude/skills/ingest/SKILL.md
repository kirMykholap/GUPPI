---
name: ingest
description: Compile the handoffs no ingest has compiled into the vault and regenerate the brief. Run at the end of a session, after /handoff. Use when a session is finishing, after writing the journal, or when asked to update the knowledge base.
---

# Ingest

Dispatch the `vault-librarian` agent (Agent tool, `subagent_type: "vault-librarian"`) with the
instruction below, then **review what it did** — see "After the librarian returns".

**One source at a time, inside one dispatch — and the two halves of that sentence are not the same
claim.** Compiling two journals as one blurred document loses the ability to guide what is
emphasised, and it is where an auto-maintained wiki starts to rot; that is why sources are read one
at a time. **Dispatching twice is a different matter**: a librarian round trip costs 15-30 minutes
whatever it is given, so the fixed cost is paid per dispatch and not per source. This line used to
read *"never batch several handoffs"* full stop, which was right about compilation and wrong about
dispatch, and it read as a flat contradiction against a decision for three days. Ingest runs after
`/handoff`, at the end of every session, so in practice there is one source anyway.

The vault is the top-level directory holding a `wiki/` — `$VAULT` below. Never hard-code its name;
the owner renames it, because it is what Obsidian displays.

**The source is chosen by the sidecar, never by the date in a filename.** A handoff is compiled when
`<name>.coverage.tsv` sits beside it — that file is written by the ingest that gave every unit a
verdict, so its absence is what *not yet compiled* means, and it is a file-existence test that no
ordering can break. This rule used to read *the newest file by the date in its name*, and **a date
prefix orders sessions only while there is one a day**: on 2026-08-17 two journals of one day sorted
by their slug rather than by time and the `SessionStart` hook fired on a journal that had been
ingested hours before. Three journals now carry 2026-08-20, so the old rule had nothing left to
break the tie. **Two other readers already use this test** — that hook, and rule 8 of
`scripts/vault-check.sh`, which judges a journal only while no sidecar sits beside it — so after
this change all three answer *is this compiled?* the same way. It also **removes the need for the
collision check** that [[the-closing-ritual-produces-what-the-journal-cannot-hold]] points `/handoff`
at: the collision is minted when `/handoff` picks a filename, and a reader that never orders by
filename cannot be misled by one.

**Scoped to `raw/handoffs/`, never to `raw/`.** `raw/plans/` and `raw/specs/` hold artefacts that
are frozen and cited rather than compiled — they will never earn a sidecar, and a predicate widened
to `raw/` would report them as uncompiled forever.

Instruction to pass:

> Ingest the handoffs in `$VAULT/raw/handoffs/` matching `2*.md` that have **no `<name>.coverage.tsv`
> beside them** — not the newest by name, and never by mtime, which any checkout rewrites. Where
> more than one is uncompiled, take them in the order of the date in their names, oldest first, one
> source at a time inside this one dispatch. Where every handoff has a sidecar, say so and ingest
> nothing rather than picking one. Follow `$VAULT/CLAUDE.md`.
>
> 1. **Split the source into units and give every unit a verdict.** Run
>    `bash scripts/vault-units.sh <source>`; it emits one line per claim — a heading, a table
>    row, a bullet, a numbered item, or the line a paragraph opens on. Bold has nothing to do
>    with it: the rule was once bold-only and that hid two whole sections of the first journal
>    it was run on. Write a verdict for each into the sidecar, which is the source's name with
>    `.md` replaced by `.coverage.tsv` — `2026-08-13-x.md` gets `2026-08-13-x.coverage.tsv`,
>    and a sidecar under any other name is not read. One line per unit, `LINE<TAB>VERDICT`,
>    one of exactly four:
>
>    | verdict | meaning |
>    |---|---|
>    | `page:<name>` | compiled into that wiki page. Several: `page:a,b,c` — one claim may be split across pages, and saying so is how a reader of the sidecar finds all of it |
>    | `journal` | session state, not knowledge. Stays in `raw/`, never enters the wiki |
>    | `elsewhere:<where>` | belongs to `CLAUDE.md`, the code, the task tracker, or the librarian's own `log.md` — which is where `Feedback to the librarian` goes |
>    | `skip:<reason>` | deliberately not compiled, and why |
>
>    **There is no fifth option.** A unit with no verdict is an unfinished ingest, and
>    `bash scripts/vault-coverage.sh <source>` is what says so.
>
>    A unit inside a section you have declared `journal` wholesale still gets read: the first
>    widening of the unit rule found two claims hidden inside such a section, one of them
>    knowledge. **The section's verdict is a default, never a licence to skip its contents.**
>
> 1b. **`wiki/proposals/` is a category like the other four** (added 2026-08-15): what was
>    raised or designed and never built. A unit that describes an intention is filed there,
>    never in `decisions/` or `concepts/` — an intention compiled as a record of something
>    built passes every check in this project and still lies, which has now happened twice.
>    The decision to defer keeps its own page in `decisions/`; the proposal carries the design.
> 2. For a handoff written from our own template the mapping is already known, and **you read it
>    from `.claude/templates/handoff.md` rather than from this skill.** Every section there carries
>    a `→ ingest:` line naming where it is filed; the verdicts follow those lines. This skill
>    deliberately holds no copy of the mapping: it held one for three days as *section 7*, and a
>    number moved every time a section was inserted. **The cut is by heading text now** — a
>    renamed heading changes where knowledge lands, which is why rule 8 of `vault-check.sh`
>    compares a journal's headings against that same file and why nothing here restates them.
>
>    `Anything else worth keeping` is the one section with no folder: file what fits, and say so
>    in the log when nothing does — a catch-all that fills up repeatedly means the template is
>    missing a section. **For any document not written from the template there is no shortcut at
>    all, and step 1 is the whole method.**
> 2b. **Dispatch your readers before you write anything, and dispatch them yourself.** You hold
>    `Agent` for this. Send `decisions-agent` the decisions this handoff carries and `lessons-agent`
>    the lessons it carries; they run in parallel, because neither writes and neither depends on the
>    other. Wait for both, then write what they found. **You return once** — a ritual that dispatches
>    you twice is the arrangement this replaced.
>
>    **They read and you write, and that division does not move.** Their verdicts are findings to act
>    on, never edits already made. Read `contradicts` rows especially: the gate compares two `current`
>    pages only under the *same* `authority:` and is blind to a disagreement under different slugs,
>    which is the one class nothing mechanical will ever find.
>
>    **Look a candidate up with the command the rule names**, `bash scripts/vault-authority.sh --near
>    <candidate-slug>`, and not with a second route of your own. A rule you cannot look anything up
>    for is an exhortation, and two routes to one question is how a corpus starts disagreeing with
>    itself.
>
>    **Known and not worked around:** a reading dispatch that grades something is supposed to run
>    after the last write to what it grades, and here you write into the corpus the decisions agent
>    just judged. Its verdicts are taken against the corpus as it stood when it read. Say so in
>    `log.md` if a verdict and your own write disagree, rather than quietly preferring one.
> 3. Where a new page replaces an old one, retire the old one per the schema — `deprecated`,
>    `superseded_by:`, move to `archive/`. Never delete text.
> 3b. **You do not set `status: processed`, and you no longer set any mark when you write
>    `decided_by:`.** Write the pointer and stop there. `scripts/vault-archive.sh` decides on its
>    own whether a decision is discharged, and it writes `status: archived` as it moves the page —
>    one pass, one writer, one mark.
>
>    **This reverses the instruction that stood here until 2026-08-30**, which had you set
>    `processed` in the same act as `decided_by:`. That arrangement existed because setting the
>    mark was a *judgement* and moving the page was *mechanics*, and the two were kept apart so an
>    error of judgement was not immediately irreversible. The judgement is gone: a decision now
>    declares its own target, and whether that target received it is a comparison a script makes.
>    With nothing left to judge, a second step buys nothing — and `processed` and `archived` are two
>    values of one field, so in a single pass the first would be written and overwritten in the same
>    act and no reader could ever see it (owner, 2026-08-30: «archived выглядит честнее, чем
>    processed»).
>
>    **What the mark used to distinguish is now read off the tree**: a decision whose target names
>    it back in `decided_by:` was discharged, and one that left because the proposal listing it was
>    refused did not. Both end as `archived`, and the difference is derived rather than stored.
> 4. Where two `current` pages end up claiming the same `authority`, mark **both** with a
>    `> [!CAUTION] CONTRADICTION` block and raise it in the brief. Do not choose.
> 5. Update `index.md` only if a category, the naming rule, the current sprint or a hub page
>    changed. `index.md` is a map, not a catalogue — it must not grow when pages are added.
> 6. Update `tags.md`: new tags with definitions, and rejected candidate words as aliases.
> 7. Append to `log.md`, under today's `## YYYY-MM-DD` heading and one line per entry: an
>    `- ingest:` line (what was read, created, updated, deprecated, and why), an `- miss:` line
>    per item in the handoff's `Feedback to the librarian`, and an `- measure: brief=<bytes>` line
>    for the brief you generate in step 9.
>
>    That section also carries `measure:`, `decision:` and `harness:` lines, not only misses — transfer those under
>    their own kind rather than filing everything as a miss. **A `measure:` line reporting an
>    agent's token cost can only arrive this way**: a subagent cannot see its own usage, the
>    harness reports it to the main session, and the main session may not write `log.md`. Copy the
>    figure as observed, with whatever the session said about what the number does and does not
>    mean; do not convert it to money or restate it as a rate.
>
>    **`decision:` is a session kind as of 2026-08-24 and it names its own shape** — *the owner
>    said it*, *the owner selected it*, or *the session understood it*. **File that shape as it
>    stands and never promote one to the next.** A session's understanding written in as his word
>    is the failure that put a rule he had never given on a page for three days
>    ([[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).
>
>    **`lint:` and `process:` stopped being SESSION kinds the same day** and stay yours in
>    `log.md`, where you wrote 339 of its 704 lines. A journal from before that date carries them
>    and they transfer unchanged: `raw/` is immutable and what a session believed at the time is
>    data.
> 8. **Before the brief, compare the journal against the tree.** Run `git log --oneline` for the
>    handoff's `commits:` range and `git status --short`. A journal is written at the end of a
>    session and read at the start of the next one, and work can land in between — the first real
>    ingest met a `State` that said "in flight: nothing" while three tasks sat uncommitted on disk.
>    **Never edit the journal**: `raw/` is immutable and what the session believed is data. Put the
>    measured state in the brief beside what `State` claims, and say which is which.
> 9. **Stamp and regenerate `$VAULT/brief.md` — the last thing written, and written from what is now in
>    the vault rather than from what you remember reading.** See below.
> 10. Run `bash scripts/vault-inject.sh` — a rule page edited and not rendered leaves the gate
>    red, and rule 12 asks by running this — then
>    `bash scripts/vault-check.sh` and `bash scripts/vault-coverage.sh <source>`, and fix
>    anything either reports. **The ingest is not finished while a unit lacks a verdict**, and
>    coverage exits non-zero both when a verdict is missing and when it has no sidecar to read
>    at all — a report of "0 of 33 evidenced" is not a pass.
> 11. **Run the corpus-state checks, which no ritual was calling.** About 25 s together, measured
>    2026-08-21:
>
>    ```bash
>    bash scripts/vault-check.sh --lint
>    for src in "$VAULT"/raw/*/*.md; do bash scripts/vault-coverage.sh "$src"; done
>    ```
>
>    `--lint` adds the tag-density advisories, which until 2026-08-21 printed only under
>    `/vault-lint` — a ritual defined per sprint that had therefore never run against this corpus.
>    **The owner's ruling of that date puts them back on a per-session run.** The reason recorded
>    against it stands and is not refuted: an always-firing advisory stops being read. What changed
>    is that the figures became a finding rather than background — `vault` selects 124 of 193 pages
>    in `decisions/` — and a finding nobody sees is worse than one they tire of. If they ever fall
>    silent, this call costs 11 s and prints nothing.
>
>    **The coverage loop is a different instrument and is not contested**: it reads every source in
>    `raw/`, not just the one compiled here, so it reports an ingest left unfinished on an earlier
>    day. On the day it was wired it found `15 verdicts are not verdicts` in the 2026-08-12 journal.
>
>    Neither call can fail this step. Report what they print; the judgements they feed - split a
>    tag, or leave it - are the owner's, made at `/vault-lint`.
> 12. **Archive the source, and this is the last thing the ingest does.**
>
>    ```bash
>    bash scripts/vault-archive.sh <date> <session-slug> handoffs <the source you just compiled>
>    ```
>
>    **It goes after step 10 and not before it**, because step 10 runs `vault-coverage.sh` against
>    the source path and this moves that path. The script does the move and the `^sources:` rewrite
>    as ONE run and then runs the gate itself: between the two the tree is red, and a filesystem
>    cannot make the pair atomic.
>
>    **Only the source this ingest compiled.** The 20 journals that accumulated before this step
>    existed stay where they are - sweeping them is 480 `sources:` lines in one commit and is its own
>    piece of work, deliberately not folded in here (owner, 2026-08-21).
>
>    **What this buys beyond an emptier `raw/`**: the uningested-journal alarm in
>    `.claude/hooks/session-brief.ps1` reads sidecar absence in `raw/handoffs/`, and once compiled
>    journals leave, a non-empty `raw/handoffs/` comes to mean *work that was never compiled* rather
>    than *history that piled up*.

### The two qualities, which are not the same check

**Coverage** — nothing was dropped. Mechanical, and 100% is required. It works only because the
*denominator* is produced by a script: if the same party both listed the units and accounted for
them, a forgotten section would simply never appear on the list. That is precisely how the `State`
section of the old handoff was lost on the first pass.

**Fidelity** — what was compiled says what the source said. **No script can check this.** The
Critical found in task 2 would have passed coverage without a murmur: the page existed, its
identifiers matched, and its content was six months out of date.

One kind of infidelity does have a mechanical half, and this is the rule that names it:

<!-- rule: a-block-attributed-to-the-owner-is-written-in-his-own-russian -->
The owner's words enter a journal verbatim and in Russian. Where a session understood rather than
heard, it writes its own understanding in its own voice and does not sign it `owner:`.

<!-- /rule: a-block-attributed-to-the-owner-is-written-in-his-own-russian -->

**Compiling a paraphrase into a quote block is the failure this rule exists for**, and it is not
hypothetical: a rule the owner never gave was rendered here as his words, stamped `basis: human`,
and decided three things over three days before he saw it. `bash scripts/vault-check.sh --lint`
names every block under `wiki/` that carries no Cyrillic. It is an advisory rather than red,
because a genuine English quotation from him exists as a case.

Fidelity is checked two ways, both cheap: **sampling** — the sidecar records the source line, so
ten random units opened side by side with their pages take ten minutes and give a real verdict on
whether the system lies — and the **acceptance questions**, whose answers are known in advance.
A review agent is for large migrations only.

Run coverage every time. Sample on every ingest. Pay for an agent when a whole document moves.

## The brief

`$VAULT/brief.md` is derived and is **never a source**. If it is wrong, fix the vault or this
skill — never the brief. A hand-edited brief that survives a session is immediate divergence.

Shape:

```markdown
# Brief — <date of the ingest that produced it>
generated-at: <the short commit id of HEAD when you write it>
ingested: <the file name of the journal this brief was built from>

## Alarms
<only if there is one: a contradiction raised, a missing handoff for the previous session,
 or the brief has outgrown its threshold. Otherwise omit the section entirely.>

## Sprint
<read from `$VAULT/sprint.md`, which is the record; do not restate it from memory. If that file
 does not exist yet, say "no sprint record exists yet" — do not invent one.>
Goal: <text> — or "no sprint declared; open one before starting work".
Acceptance criteria: <list>.
Progress: <closed / open, as the handoff reported it>.

## State
Done / not done / in flight / next step, from the `State` section of the newest handoff.

## What must not be broken
<three to six lines, each linking to the page that explains it. Not the explanations themselves.>

## From the librarian
<only if there is one. What the librarian recorded in `log.md` during THIS ingest that is
 addressed to the session rather than to the corpus: a question it could not answer itself, a
 request, a finding it wants acted on. Read from `log.md`, never remembered, and never carried
 through `.superpowers/sdd/vault-feedback.md` — see below. Omit the section entirely when the
 ingest raised nothing.>

## Hooks for this work
<"if you touch X, ask the vault about Y" — one line per foreseeable subject, from what the
 sprint's state suggests is next.>
```

**`From the librarian` is why the librarian never writes `.superpowers/sdd/vault-feedback.md`**
(owner, 2026-08-25). That file is a channel for a party that cannot write files — a session in plan
mode — and the librarian can. Writing there also files the line under the wrong session: `/handoff`
runs before `/ingest`, so the next session's handoff drains it. Measured the day of the ruling: 115
records in the file, roughly a third written by the previous session's ingest after that session's
handoff had already emptied it.

**Nothing instructed the librarian to write that file — it was practice, and this is where the
prohibition now lives**, beside the section that replaces it. The rule about who empties a feedback
line is untouched: a session's own lines are still drained by its own `/handoff`.

**And this section is generated like every other one.** The brief is derived and is never a source,
so the line is written into `log.md` first and surfaced here — never hand-written into `brief.md`.

**Neither line is decoration.** `ingested:` names the last journal compiled, and the `SessionStart`
hook asks exactly one thing of it: that the file it names still **exists**. A brief naming a journal
that is not there was built from something that has since moved, or from nothing. **The hook does
not compare it against the newest journal** — a session that wrote its journal and never ran this
skill is caught by sidecar absence instead, for the reason under *The source is chosen by the
sidecar* above. This paragraph claimed the comparison was *by name* from 2026-08-17, when the hook
was repaired, until 2026-08-20, when the skill was; **the copy is what went false, and nothing
checks a copy.** No rule page governs this file, so a change to the hook does not reach these words.
The durable repair is a `wiki/rules/` page rendering a region here, and it is designed nowhere.

**`ingested:` stays a bare filename, and from 2026-08-21 the hook resolves it in two places** —
`raw/handoffs/`, and `archive/*/*/handoffs/`. Step 12 archives the journal this ingest compiled, so
`raw/handoffs/<name>` stops existing the moment the ingest finishes and a check that looked only
there would have fired on **every** session start: the alarm class this file has already removed
twice. **Rejected: writing the destination path into this line at step 9** — that is a line
asserting a path three steps before the step that creates it, and it would have gone false whenever
the archive failed while the brief still read as if it had not. A filename is an identity and
survives the move; where the file lives is a question for whoever is looking for it.

`generated-at:` is provenance a reader can check without git — the hook does **not** compare it,
because a brief is generated and then committed, so it is one commit behind by construction and
comparing it would warn every time. Staleness is asked of git history instead: commits landing
after the one that carries the brief. Nothing here is ever compared by mtime — a `git checkout`
rewrites those, and a clone rewrites them in an order that made the first version of that check
fire on every single clone.

**If the previous session left no handoff**, say so in the first line of Alarms — meaning a
session that wrote no journal at all. A document that was migrated into `raw/` is a source, not a
session's testimony, and does not answer for the session it names.

A silently inherited old brief is the worst available outcome.

Keep the brief short. It is read at the start of every session, and its size is the growth signal
that tells the owner a sprint has stopped being one goal.

## After the librarian returns

**This is the review that replaced asking permission, and it is yours, not the librarian's.** Every
step above is performed by the party being reviewed; the guard hook cannot help, because a
`PreToolUse` payload does not say who is writing. Git is the only real enforcement this design has.

```bash
git diff --stat -- <the vault>
git diff -- <the vault>/wiki
tail -20 <the vault>/log.md
bash scripts/vault-check.sh
bash scripts/vault-coverage.sh <source>
```

Git says **what** changed and the log says **why**. A disagreement between them is itself a finding:
a page rewritten that the log does not mention, or a `- ingest:` line claiming work the diff does
not show. Read it before committing.

Then **sample for fidelity**, because coverage cannot: open ten of the sidecar's `page:` verdicts
beside the source lines they name, and check that the page says what the source said. The first
time this was done it caught a page whose title carried a number no tool had ever produced — the
page guarding the migration gate.

**To regenerate the brief alone** — if it was deleted or hand-edited — dispatch the librarian with
step 9 only. It does not need to redo any verdict work.

## Then commit, and the ingest is not finished until you have

**The commit is the session's and never the librarian's.** Every step inside the block above is
performed by the party being reviewed, so a librarian that committed its own work would be
countersigning its own testimony. This is the same sentence as the review itself: it belongs to
the caller.

**The diff is read before the commit, not after it.** The `git diff` and the fidelity sample above
are the whole of what replaced asking permission, and the owner reads that diff. A step that
commits as soon as the sample is taken removes the one reader this arrangement has, which is the
opposite of what a commit here is for.

```bash
git add -- <the vault>
git commit          # English, like every message in this repository
git status --short  # empty, or say what is left and why
```

The message says what was compiled: how many pages were written and extended, what was retired and
on what ground, and what the gate, `authority.md` and coverage read afterwards.

**Nothing of the session stays uncommitted past this point** — not the ingest's pages and not the
work the journal describes. On 2026-08-29 a sweep of 239 pages, three hook changes and the ingest
that compiled them all sat in a working copy until the next day; that journal recorded
`commits: none` as a finding about itself, and the next session opened by cleaning up rather than
by working. `git status --short` printing nothing is the check, and it is cheap.

<!-- This step is an imperative held by no test and typed into a harness file rather than rendered
     from a wiki/rules/ page. It owes such a page - or a page saying why it cannot have one - under
     every-rule-in-wiki-rules-owes-a-mechanical-instrument. Owner-decided 2026-08-30. -->

