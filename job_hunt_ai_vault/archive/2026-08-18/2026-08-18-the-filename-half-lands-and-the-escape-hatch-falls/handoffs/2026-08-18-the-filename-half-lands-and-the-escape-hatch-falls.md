---
session: 2026-08-18
sprint: S2
commits: e4065d4..c521a10
---

# Handoff — 2026-08-18

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

Second session of 2026-08-18. The brief it opened on was generated at `ce58eb9`; HEAD was already
`e4065d4`, the ingest commit that landed after the brief was written. That is not drift — it is the
ordering the ritual produces — but it is why the range below starts where it does.

## State

**Done.**

- **The definition of *retrospective* renders into `CLAUDE.md`** (`46b7c76`). Eleventh region, second
  non-rule renderer after the map. The move is verbatim: the diff of `CLAUDE.md` is three insertions
  and no deletions — the two markers and the separator — and the slice was cut out of the file with
  `sed` rather than retyped, both sides hashing the same.
- **Rule 10 reads the filename with the predicate it reads the title with** (`2772439`), as an
  advisory where the title half is red. Six standing offenders, each a page whose title had already
  been repaired. Format corrected to one name per line at `c521a10`.
- **The probe that measures conditional delivery is laid** (`f552abd`) and is inert until Claude
  Code restarts. `probe/RUNBOOK.md` carries the four probes and what each outcome decides.
- **A `/grill-me` on the `.claude/rules/` move**, run to an empty frontier. Designed, not built; the
  decisions are below.

**Not done.** The move itself. The four probe measurements — they need a restart, deliberately.
The `quantity:` removal the owner ruled tonight, which is the next session's first work.

**In flight: nothing. Tree clean at `c521a10`.**

**Next step, and the order is a dependency rather than a preference:** clean the corpus of
`quantity:` first, then rename the counting filenames, then tighten rule 10. Tightening the check
first reddens 24 pages at once, because they are silent today only because the field answers for
them.

**Checks.** Selftest **caught 112, missed 0**, up from 107 — and re-run after the format change,
because a case greps that output. `vault-check.sh` exits 0 with **20 advisories**, both new ones
this session's own. `vault-inject.sh --check` unchanged, reporting agreement. **`pytest` and `ruff`
were not run and correctly so** — no product code was touched.

→ ingest: `journal` — never compiled. State is a lie within a sprint; it feeds the brief and dies with it.

## Entities

**Appeared.**

- `wiki/concepts/a-retrospective-is-a-sessions-end-not-a-sprints-ritual.md` — the definition, written
  by the librarian, `governs: CLAUDE.md`, carrying no `authority:`. The slug and title were the
  session's choice; the corpus has no titling rule for `concepts/`.
- **The eleventh region in `CLAUDE.md`**, and the first whose source paragraph already stood in the
  destination — so the prose was deleted after the render was verified, which is the ratified order.
- **The filename half of rule 10** — one predicate over a second string, inside rule 10 rather than
  as a rule of its own.
- **`.claude/rules/`** — the directory now exists, holding one temporary probe file. It is the
  fourteenth governed markdown file and nobody listed it anywhere.
- **`.claude/hooks/instructions-loaded.ps1`** and an `InstructionsLoaded` block in
  `.claude/settings.json`.
- **`probe/`** — a throwaway directory with a runbook and a target, committed on the owner's
  instruction that it be archived rather than deleted when spent.

**Taken out of service.**

- **`quantity:`** — the frontmatter field. Rejected by the owner tonight; see Decisions. It still
  stands on 24 pages and still silences seven filenames until the corpus is cleaned.

→ ingest: `entities/`

## Decisions

**The definition renders as a `concepts/` page, and the move is verbatim.** Rejected: rewording
while moving, because a change nobody decided would be invisible in the diff of a move; rejected:
deleting the paragraph instead of rendering it, because then no page owns the question. Obliges: the
page is the only place that text is corrected.

**The filename half is an advisory where the title half is red.** owner. Rejected: red, priced out
loud — `vault-check.sh` would exit 1 on every run until the renames landed, and a gate that is
always red is not a gate; rejected: renaming the six on the spot, which widens into the half that
was blocked. What the owner asked of it — "a twelfth name is never minted silently" — a printed line
delivers in full, because a new page is renamed in the minute it is written.

**owner: the rule is unconditional. No digits in a title, none in a filename. The `quantity:` field
is rejected, and this question is closed permanently. The librarian checks everything standing in
the rule's way and rewrites it; then the librarian renames the files.**

Rejected alternative, named: give the field a decision page and keep it. Refused because the owner
had already ruled the rule unconditional twice, `basis: human`, and had refused two specific
exception classes on the way — counts bound to a date, and design invariants — both of which are
alive in `quantity:` values today. What it obliges, in order: a decision page; 24 pages stripped and
retitled; the counting filenames renamed with their links rewritten and the `log.md` hole closed;
`### quantity` removed from the store's schema; only then `answered` removed from rule 10 and the
two selftest cases that test the escape hatch retired.

**A `quantity:` line answered for both the title and the filename** — taken by the session on
2026-08-18 and **superseded the same day** by the ruling above. Recorded because the check shipped
with it and seven filenames are exempt on it right now.

**owner: the advisory prints one name per line; every line carries the `VAULT-CHECK:` prefix; no
continuation line carries the word `advisory:`.** The prefix keeps the output greppable line by
line. Withholding the second word keeps `grep -c 'advisory:'` counting advisories rather than names
— the brief reports that number, and six continuations would have turned twenty into twenty-five
overnight with nothing having changed.

**owner: `authority:` beside `governs:` on a non-rule page is forbidden.** Both non-rule renderers
have done without it, and leaving it unruled costs a question every time.

**owner: the register instruction joins the language rule's slice.** It is about how to write, and
the language rule is the only place that is read.

**owner: Core is a decision, not a summary.** `CLAUDE.md` carries what bootstraps the asking — the
rules you need *before* you can reach the vault — plus what is irreversible if missed. It sorts all
nine rules without a remainder, and it is why the JavaScript rule can leave while the test-database
rule stays.

**owner: the AST move goes ahead to prove the mechanism, not to save context.** Measured this
session: the eleven regions are 3637 bytes, roughly 850 tokens, and the AST rule itself is about 45.
"Better to test it on one rule than on ten later." The word *economy* is to stay out of the decision
page.

**A file in `.claude/rules/` is generated whole, not region-carrying.** The destination would be
frontmatter plus rule text with nothing hand-written around it, and a region protects an insert into
a file that has its own life. This is the `whole` delivery mode, designed earlier and still unbuilt.
Its check is free: regenerate and compare, which is how rule 12 already asks its question.

**`paths:` lives on the vault page and the injector syncs it into the destination.** owner. This is
what `render:` lacked when it was refused — a writer and a reader. Obliges: writer **and** checker,
because a one-way sync means a hand edit in the destination is never noticed. Frontmatter is not a
region and the marker mechanism cannot reach it, which is a second argument for generating whole.

**Generation, rewriting and deletion belong to a script, not to an agent.** owner: "then we
guarantee our system works rather than hoping." Not a new script — a mode inside `vault-inject.sh`,
because a third command is a third place to forget it. **Deletion is guarded: the script deletes
only files carrying its own generated-marker.** That marker is simultaneously the human's warning
not to hand-edit and the script's permission to remove — a file without it is never touched,
whatever the vault thinks of it.

**owner: hand-writing is forbidden only in `.claude/rules/` files backed by a vault page.** A file
with no page is legitimate, not garbage — which is exactly why deletion must key on the marker
rather than on the absence of a page.

**`paths:` is written with the widest true pattern.** The cost is asymmetric: over-matching costs a
little context, under-matching costs a rule that does not arrive.

**No frequency cache for `CLAUDE.md`.** owner: collect the statistics, consider adoption when it
makes sense. Rejected now because a rule sitting in `CLAUDE.md` is never asked about, so the counter
starves whatever it caches and the cache oscillates; because frequency evicts exactly the rules
whose failure is rare and catastrophic; and because it would make `CLAUDE.md` non-deterministic,
different in two clones of the same repository.

**Removing the JavaScript rule from `CLAUDE.md` is agreed and not yet done.** owner: the system is
"about to write something → ask the vault", and `/pre-task` enumerates constraints rather than
answering a topic, so a rule nobody knows exists is still surfaced. The session argued the opposite
and conceded. It still needs its own dated page under `conditional-delivery-gate`, because ceasing
unconditional delivery is a change of guarantee.

**Divergences, three, each a decision with a rejected alternative of "obey the rule".**

- **A vault miss was found and not written to `vault-feedback.md` in the turn it appeared.** It was
  reported to the owner in chat and filed hours later at the retro, marked late in the file itself.
  It looked unnecessary because it had just been said out loud — which is the exact failure the rule
  names, since chat does not survive the session.
- **An approved shape was replaced without telling the owner.** He chose the filename verdict from a
  multi-line preview and received a single comma-run, because the house style won silently.
  `narrowing-a-scope-notifies-and-widening-it-asks` makes a replacement a question; neither a
  question nor a notification happened. Confessed at the retro unprompted and corrected at `c521a10`.
- **The filename half was built leaning on `quantity:`,** with `OWED TO THE OWNER` written beside it
  and the lean taken anyway. That the field had no authority at all was not knowable until the
  retro, but the lean is on the record and is why the check must not be tightened first.

→ ingest: `decisions/`

## How it is built

**A path-scoped rule triggers on a read, and editing an existing file implies one.** The vendor
documentation says only "reads" and is silent on Edit, Write and Bash. But the Edit tool's own
contract requires the file to have been read in the session, and Write requires it for an existing
file — so *touching* an existing file does trigger the rule, which is the owner's reading and it is
correct. What genuinely does not trigger: **creating a new file**, and **a Bash command**. That is
precisely why the JavaScript rule and the test-database rule fail the movability criterion, and why
of nine rules exactly one is path-scopable.

**After `/compact` a scoped rule is not re-injected**; it returns only on a fresh matching read.
Whether that matters reduces to one measurable thing: whether Edit demands a re-read after
compaction. Probe 4.

**Whether a scoped rule reaches a subagent is documented nowhere.** Both halves are documented
separately — a subagent receives project rules; scoped rules load on a read — and no line joins
them. Every task here is reviewed by a subagent, so this is the blocker, and it is probe 2.

**`InstructionsLoaded` is a real harness hook event, not a name someone invented.** It carries
matchers by load reason, `path_glob_match` among them, and its exit code is ignored — observation
only, it cannot block a load. The corpus had the name and nothing else.

**`.claude/rules/*.md` joins rule 11's governed set the moment it lands** — demonstrated live this
session, not argued: the coverage advisory moved from `1 of 13` to `1 of 14` when the probe file
appeared, and nobody edited a list. The sweep is by property.

**`log.md` is outside the link set rules 4 and 5 read.** The set is `wiki/`, `archive/`, `index.md`,
`tags.md`, `sprint.md`. Demonstrated in a throwaway worktree: a deliberately incomplete rename left
**13 dangling `[[wikilinks]]` in `log.md` and the gate exited 0 saying nothing**. `raw/` is outside
it too and correctly so — a journal naming an old slug is history recording what was true then.

**A page rename is sed-and-verify, and the "blocked" framing is overpriced.** All six standing
renames, done in an isolated worktree: **10.1 seconds wall clock including a full gate run**, 51
files, and the gate came back at exactly the baseline. The detector is complete for the link set —
a half-done rename prints a broken wikilink and an orphan. The "23 inbound links" figure on the
proposal page does not reproduce at any commit checked, and **no `proposals/` page designs the
rewriter the renames are said to be waiting on.**

**`note()` sets `fail=1` and the script ends `exit "$fail"`; an advisory is a bare `echo`.** That is
the whole of the red-versus-advisory choice, and it was read in the file rather than taken on trust.

**`run_clean` cannot test an advisory exemption.** It asserts exit 0 and an `ok` line, and an
advisory changes neither — a broken exemption would print its slug and still pass. Every non-firing
case for the filename half is `run_case_absent` instead, with the reason written beside them.

**Rule 10's `answered` flag returns before the slug is evaluated**, so a `quantity:` line silences
both halves. Seven filenames are exempt on it today.

→ ingest: `concepts/`

## Lessons

**A field admitted around the admission procedure outlives the rule it softens.** `quantity:` was
introduced 2026-08-17 inside the same commit that wrote rule 10, filed in that session's journal
under *Entities → Appeared* rather than under Decisions. No `owner:` line anywhere touches it; no
`decisions/` page carries an `authority:` for it; there is no `decided:` date. On that same day the
owner **refused** a different new field under a written admission procedure, with the reason that a
field nobody writes and nobody reads becomes a per-page invention. The rule it softened had been
ruled unconditional twice, and the two exception classes he refused on the way are alive in
`quantity:` values today. It took a retrospective a day later, and the owner's own suspicion, to
find it. **The instrument that would have shown it was installed by its own author** — rule 10's
comment says the declarations outnumbering the retitles is the signal — and nobody read it: 24
declarations against 23 retitles, and 5 against 5 since the rule became checkable.

**The turn that explains a rule adds exceptions to it — and it recurred.** That lesson was written
2026-08-16 about the session that first stated the rule. The exception came back the next day in a
weaker form: two carve-outs with stated boundaries were refused, and an unbounded one in free text,
judged by nobody, replaced them.

**A page that says "measured" can carry a figure nobody measured.** Two on the same page this
session: `tests/unit/*boundary*.py` recorded as "six files, measured" covers one of the three files
that actually import the AST helper, and the "23 inbound links" price does not reproduce anywhere.
Both fell to one `ls` and one `grep`.

**Chat is not a channel that survives the session.** The miss above was said out loud to the owner
and therefore felt captured, and was filed hours late. The rule requiring the line in the same turn
exists for exactly this feeling.

**A replaced shape reads as no replacement when only the shape moved.** The owner chose a verdict
from a preview and got a different rendering, because the content was identical. That is how a
substitution passes for none.

**Run the new case against the old code, and say honestly which cases prove nothing.** Of five new
selftest cases, one discriminates — it reported MISSED against the old check, which is the only
reason the mechanism is known to be new. The other four assert absence and pass against the old code
too. A suite claiming five new cases prove a new mechanism would be wrong about four of them.

**Re-run the suite after a change that looks cosmetic.** The advisory's format is load-bearing for a
case that greps the output. It survived — measured, on a day that had already found a "measured"
figure nobody measured.

**Deriving what the vault already holds costs a round.** The criterion separating movable rules from
unmovable ones was worked out from scratch and reported as a finding, while the corpus had it
written and measured, on a page an agent had already been dispatched to read.

→ ingest: `lessons/`

## Deferred

**The `.claude/rules/` move itself** — designed to an empty frontier, not built. Consequence: the
`whole` delivery mode stays unbuilt and the AST rule stays unconditional, which costs nothing but
context. A design sits behind this and belongs in `proposals/`.

**The four probe measurements** — laid and inert until a restart. Consequence if never run:
`.claude/rules/_probe-paths.md` sits in the governed set indefinitely and the coverage advisory
keeps reading 14 instead of 13.

**Removing the JavaScript rule from `CLAUDE.md`** — agreed, needs its own dated page.

**Statistics on which rules get asked for** — collection approved, adoption not. The open design
point, recorded so it is not derived again: **what counts as "asked"**, given that a rule already in
`CLAUDE.md` is never asked about.

**Core described as its own record** — owner: "what will always be in `CLAUDE.md`" should be written
down separately. Not discussed in detail.

**What a sprint is and how it is worked with** — owner deferred it explicitly.

**Splitting the dense tags** — untouched; advisories now 20. → `/vault-lint` at the sprint
retrospective.

**Eight files carrying `1 of 13`** — untouched, and staler than yesterday while the probe is laid.

**Which mechanism preserves the paragraph break at a region boundary** — the alarm as posed is
answered (no break is missing), but separator-versus-collapse cannot be told from this file, because
every region also carries a blank line outside it. Deciding it needs a region with text flush
against it, and none exists.

**The `log.md` hole** — outside rules 4 and 5' link set, demonstrated. Part of the rename work now.

→ ingest: `decisions/` for the deferral, **and `proposals/` as well** where a design sits behind it. One item routinely becomes two pages.

## Feedback to the librarian

- measure: **the coverage sidecar is an unpinned file class that a script parses, and it has already been converted.** Noticed 2026-08-18 at the close of the ingest, from git's own warning on commit: *"LF will be replaced by CRLF the next time Git touches it"*. `.gitattributes` pins `*.sh`, `*.md`, `*.ps1` and `*.json` and says nothing about `*.tsv`, so `core.autocrlf` owns the sidecars. **Three already carry CR in the working copy** — 362, 41 and 55 bytes — and `scripts/vault-coverage.sh` strips `\r` nowhere. Measured rather than assumed: converting a copy of today's sidecar to CRLF and running coverage against it still reports `97 of 97 units carry a verdict, INGEST COMPLETE`, and the oldest CR-carrying sidecar passes too. **So it has cost nothing yet, and [[a-file-class-is-pinned-after-it-costs-something]] says that is exactly when not to pin it.** Recorded so the decision, when it comes, is made on this observation instead of on the next surprise. What would change it: any verdict word failing validation because of a trailing CR — the script advertises that it reports "verdicts that are not verdicts", and whether that test is CR-tolerant by design or by accident is not established.

- miss: **`moving-a-rule-into-claude-rules-with-a-paths-scope` states a measured glob that does not cover what it claims.** Surfaced 2026-08-18 during the `/grill-me` fact-finding for the move itself, when the librarian quoted the page's table verbatim and I ran `ls` against it. The page records `paths: ["tests/unit/*boundary*.py"]` as **"six files, measured"**. Six files do match. But the set the AST rule exists to protect is the files importing `_ast_boundary`, and there are **three** of them: `test_network_boundary.py`, `test_normalize_boundaries.py`, `test_parser_boundaries.py`. The glob matches **one of the three** — the two spelled in the plural fall outside it, because the pattern demands `boundar-y` and they carry `boundar-ies`. `tests/unit/*boundar*.py` matches all eight boundary tests. So the one migration that passes the page's own safety criterion would have silently failed to load for two thirds of its subjects, which is precisely the failure the criterion exists to prevent, reproduced inside it. The figure is stated without the plural spelling having been considered. **Filed late, and that is itself the finding**: the rule says the line is written in the turn the miss appears, and I carried it in chat to the retro instead — the exact failure the file's own header describes.

- lint: **`index.md`'s Naming section carries two stale claims.** It says *"Only the title half is checked"* — the filename half was built this session at `2772439` — and repeats *"at least four filenames carry a count today and the worst carries 23 inbound links"*, where thirteen carry one, six print in the advisory, and the 23 does not reproduce at any commit.

- lint: **`index.md` still says the definition of *retrospective* "waits on an owner decision about whether a non-rule record may render at all".** Settled 2026-08-18; the page rendered this session at `46b7c76`.

- process: **a line written into `vault-feedback.md` during `/ingest` waits a whole session.** `/handoff` drains the file before `/ingest` writes to it, so the sidecar `measure:` entry above sat there untouched from the previous session's close until this one's retro opened the file.

→ ingest: `elsewhere:log.md`, filed under the kind each line names — `- miss:`, `- lint:` or `- measure:`.

## Anything else worth keeping

**Measuring a subagent's report instead of believing it paid twice in one session.** Before the
librarian returned on rule 10, the same detector was run independently against filenames: 13 firing,
7 answered, 6 real. The librarian came back with the identical split, derived separately. The habit
also caught the glob defect and dissolved the "23 inbound links" price.

**The probe is committed rather than left in the working tree, on the owner's instruction that it be
archived when spent rather than deleted.** `f552abd` is that archive.

**`/pre-task` surfaced constraints three times that could not have been queried by name** — eight
`decisions/` pages in the first answer alone. That is the evidence that settled the JavaScript-rule
argument, and it came from the session's own transcript.

→ ingest: free-form. Its units are `skip:` unless a category is found for them.

## Harness

**Remove `quantity:` from rule 10 — both halves — and retire the two selftest cases that test the
escape hatch** (`title_declared`, `filename_declared`). File: `scripts/vault-check.sh`,
`scripts/vault-check-selftest.sh`. **Only after the corpus is clean**, or the gate reddens on 24
pages at once.

**Remove the `### quantity` section from the store's schema.** File: `job_hunt_ai_vault/CLAUDE.md`.

**Close the `log.md` hole** — either add it to the link set rules 4 and 5 read, or grep the old slug
to zero as a step of every rename. File: `scripts/vault-check.sh`.

**Run the four probes and then clear the probe** — `probe/`, `.claude/rules/_probe-paths.md`,
`.claude/hooks/instructions-loaded.ps1`, and the `InstructionsLoaded` block in
`.claude/settings.json`. The runbook is `probe/RUNBOOK.md`.

**Build the `whole` delivery mode inside `vault-inject.sh`** — generate a governed file entire,
including its frontmatter and its generated-marker; check by regenerating and comparing; delete only
what carries the marker. File: `scripts/vault-inject.sh`, and a verdict in `scripts/vault-check.sh`
for a marked file whose page is gone.

**Sync `paths:` from the vault page into the destination's frontmatter, and check it.** A writer
without a checker makes the sync one-way and silent.

**Correct the glob on the proposal page** to `tests/unit/*boundar*.py`, or wider — the decision this
session is that `paths:` takes the widest true pattern.

→ ingest: `decisions/` for what was decided, `proposals/` for a design behind it, `elsewhere:<file>` for a bare work item that names the file to change.
