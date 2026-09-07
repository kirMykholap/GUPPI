---
session: 2026-08-19
sprint: S2
commits: a1b89d9..bd7cb1f
---

# Handoff — 2026-08-19

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

Session opened 2026-08-18 23:31 and ran across midnight. Correction notes on retitles carry
2026-08-18; everything from the rename sweep onward carries 2026-08-19, on the convention the
owner ruled — **the date of a note is the date the text became false, not the date of the
session**.

## State

**Done — the whole of the `quantity:` ruling, in the order it was recorded as a dependency.**

1. **Corpus.** 28 pages edited, 27 retitled. 24 carried `quantity:`; four more carried an ordinal
   and were repaired ahead of the predicate. `quantity:` went 24 → 0 across `wiki/` and `archive/`.
2. **Filenames.** 16 renames — the 13 the advisory printed plus 3 ordinal slugs the check could not
   yet see. `git mv`, one `sed -f`, and `log.md` by hand.
3. **Schema.** `quantity:` removed from `job_hunt_ai_vault/CLAUDE.md`, and its section rewritten as
   *Titles and filenames*, because the field is gone and its absence is what has to be documented.
4. **Check.** Rule 10 no longer reads the field; the word list gained `second`…`twentieth`.

**Also done, from the retro:** a `_schema.yaml` per `wiki/` folder with the gate reading it; the
`schema` tag split into `db-schema` and `record-schema`; `ruleclaim` widened; two boundaries closed
as boundaries rather than debts.

**In flight: nothing.** Working tree clean but for `pages.base` (the owner's Obsidian view state)
and `probe/instructions-loaded.log` (untracked measurement artefact, grows on every path match).

**Next step: probe 4.** It needs `/compact` and then an edit attempt on `probe/probe-target.md`
without reading it first. Sequenced last on purpose — see *Deferred*.

**Checks.** `vault-check.sh` exit 0, **19 advisories** (18 tag density + 1 region coverage), zero
`note` lines, and **the filename advisory prints nothing** for the first time. `vault-inject.sh`
0 rewritten / 0 problems. **Selftest 120 caught, 0 missed**, up from 112 — and verified against the
pre-change scripts, where exactly six are missed and nothing else. `pytest` and `ruff` were not run
and correctly so: no product code was touched.

## Entities

**Appeared — `wiki/<folder>/_schema.yaml`, six of them.** Each names the frontmatter keys a page in
that folder must and may carry. `vault-check.sh` reads them; nothing restates the list. Their header
carries the principle they were built on: **they encode what is decided, not what is observed.**

**Appeared — the per-folder schema's three verdicts** in `vault-check.sh`: an undeclared key is red,
a folder with no schema is red, a schema parsing to zero required keys is red.

**Changed — `scripts/vault-check.sh`.** Rule 10 lost the `answered` short-circuit, the reader that
set it, and the tail of its note message offering the field. Rule 2 lost its hardcoded six required
fields. `ruleclaim` widened. Rule 10's comment was rewritten rather than patched.

**Changed — `scripts/vault-check-selftest.sh`.** Two cases inverted, eight added, one corrected
because a message it greps moved. Four fixtures gained `sprint:`. `empty_vault` now mirrors the
schema files off the pristine copy.

**Changed — `job_hunt_ai_vault/CLAUDE.md`.** The `### quantity` section became *Titles and
filenames*, and later gained both boundaries. Hand-edited by the session; see *Decisions*.

**Changed — the `schema` tag, taken out of service.** Split into `db-schema` (6 pages) and
`record-schema` (10 in `wiki/`, 3 in `archive/`). The bare word survives as an alias on both.

**Appeared — `probe/instructions-loaded.log`**, written by the `InstructionsLoaded` hook. It is the
uncontaminated instrument for probe 1.

## Decisions

- **`quantity:` is executed out of existence, in the recorded order.** Corpus, filenames, schema,
  check. Rejected: tightening first, which would have reddened 24 pages in one run.
- **owner: ordinals join rule 10's word list — `second` through `twentieth`.** Shown a measurement
  arguing against `second` (three titles carry it, three of three mean *another*), he ruled it in
  anyway, preferring a predicate with no exemptions to remember over one that is right more often.
  **Rejected: exempting `second` on the measured evidence.** `first` stays out, mirroring the
  measured exemption for `one` — 13 pages, every one a position or a pronoun.
- **owner: the gate learns the set of legal frontmatter keys, from a yaml per folder.** Rejected:
  a targeted verdict per prose-only rule. One general mechanism closed three holes, one of which
  nobody had listed. Rejected also: a key list inside the check, because two lists of one set drift
  and this project has lost two selftest cases to exactly that.
- **owner: the schema files encode what is decided.** `basis` is carried by 321 of 321 pages and is
  optional there, because a field carried by everything is not thereby required — that reasoning is
  how `quantity:` entered the store.
- **owner: `ruleclaim` widens to any page carrying `authority:` beside `governs:`.** The comment
  keeping it narrow said the vault ruled on nothing here; the vault had since ruled, so the ruling
  was wider than the gate enforcing it.
- **owner: rule 10 reads the title and the filename and never the body — a boundary, not a debt.**
  Rejected: a sprint line and a proposal page listing the counting headings. Measured: **201 counting
  headings across 128 of 308 pages**, so the list would need extending by every page written after.
- **owner: a title's length is unbounded and no check measures it.** Rejected: a length advisory.
  Naming what is counted costs characters and a limit would charge that back to correct prose.
- **owner: the `schema` tag splits, and both halves are renamed.** Rejected: leaving the general word
  on the database half, because the drift happened *against* an explicit database-only definition —
  a prose defence already tested once and failed.
- **owner: the correction note's date is the date the text became false**, not the date of the
  session. This is why one session produced notes dated 2026-08-18 and 2026-08-19.
- **owner: the schema file is the session's to hand-edit, with the divergence recorded.**
- **DIVERGENCE — the session hand-edited `job_hunt_ai_vault/CLAUDE.md` twice.** The rule is that the
  librarian writes the vault. What the rule said: one writer. What was done: the session removed the
  `quantity:` example and its section, then added both boundaries. Why it looked unnecessary: **no
  decision names who may write the schema file** — the one-writer rule closed only the registers, and
  the last hand-edit of this same file is already on the record as a divergence for the same reason.
  **The clause is still owed.** Authorised by the owner in the retro rather than assumed.
- **A licence was cited and was not needed.** A brief invoked the clause letting a session edit a
  register during a rename. The librarian established that `index.md`, `sprint.md` and `log.md` are
  its to write outright, so there was no divergence to record. Named so it is not inherited as
  precedent.

## How it is built

- **A declaration silences the one instrument that would have caught it drifting.** Two of the 24
  `quantity:` declarations were false while they stood — one page declared a third member would make
  it wrong rather than stale, over a body that had gained a third member on that same page. Neither
  was found by anything mechanical, and neither could be. This is the mechanism behind the
  withdrawal, and it is stronger than the tidiness argument made at the time.
- **With no appeal, a word in the predicate is a promise.** While a page could declare itself, a word
  only had to be *usually* a count — a false positive cost a line of frontmatter. Now it is paid for
  by rewriting correct prose. `second` is the known, deliberate exception.
- **A rename is `git mv`, one `sed -f`, and a verification pass.** Sixteen of them moved **148**
  inbound wikilinks inside the set rules 4 and 5 read, and **14** more in `log.md`, which is outside
  it. The rewriter-and-detector pair the renames were said to be blocked on was never built and was
  never needed.
- **`sed` cannot tell an address from a quotation.** The sweep rewrote two slugs that pages were
  quoting as *examples* of counting names, and one sentence came to say the opposite of what it was
  written to say. Nothing in a slug distinguishes the two uses.
- **A path-scoped rule under `.claude/rules/` reaches the main session and a subagent alike**, and
  HTML comments in it are stripped before the model sees them. Measured; see *Anything else*.
- **The check resolves its vault relative to itself**, so a sandbox copy is unreachable and a new
  verdict can only be proved by planting an offending page in the real tree and reverting in the same
  command. Every verdict added this session was proved that way.

## Lessons

- **The tightening broke nine of the suite's own cases, and only the suite found it.** The gate was
  verified four ways against the real tree and every new verdict was made to fire. What broke was the
  *fixtures*: they predate the requirement and carry no `sprint:`, so every page the suite plants
  went red and nine cases expecting green failed. **This session's own subject arriving from the
  blind side** — "corpus before check" was applied to `wiki/` and forgotten for the fixture corpus.
  Verified not pre-existing by running the same suite against the pre-change scripts.
- **`grep -c $'\r'` does not count CRLF lines — it returns the file's total line count.** The escape
  collapses to an empty pattern. It reported 232, 59 and 57 against three files of exactly 232, 59
  and 57 lines, and was used to contradict a subagent's correct claim. Caught only because the wrong
  number agreed with a real quantity. The honest instrument is `tr -dc '\r' | wc -c`.
- **The LF pin protects the repository and not the working copy, and `git status` cannot tell you.**
  One `raw/` handoff is CRLF in all 337 of its lines on disk while its blob is clean LF, and git
  reports it unmodified because `text eol=lf` normalises on the way in. This is the inverse of the
  recorded lesson where `git status` *overstated* a diff.
- **A runbook that carries the nonce cannot be read by the thing being measured.** The probe's own
  brief for probe 2 prescribed telling the subagent the string it was supposed to confirm — which
  puts it in its context and defeats the runbook's own principle. Reading the runbook at all hands
  the main session both nonces before the measurement starts.
- **A message a test greps is load-bearing twice over.** Changing `ruleclaim`'s wording broke an
  existing case; changing the filename advisory's heading did not, and the difference was only
  knowable by grepping. Both were caught before the commit, one by grep and one by the suite.

- **The session contradicted itself four times and corrected each in the same session.** Each is a
  measurement arriving after a claim, which is the pattern worth keeping rather than the individual
  slips. **(a)** "Probe 2 unblocked the `.claude/rules/` move" — probe 2 is named the blocker in the
  runbook and passed, but probe 4's own stated consequence gates the move as well; the first
  statement was narrower than the truth. **(b)** The tag split was sold to the owner on a counter
  that does not exist — the neighbouring tags in that folder stand at 54, 60 and 78 against a
  threshold of ten, and an honest split prints an advisory immediately; the owner had already agreed
  on trust when the measurement arrived, and it was corrected to him before anything was executed.
  **(c)** A corpus maximum of 145 characters was quoted against a 175 measured differently — 145
  counted the title's quotation marks, and the comparable reading is 143. **(d)** The per-folder
  schema was priced at "one verdict, one selftest case" when the owner agreed to it, and it is S2's
  first acceptance criterion; re-priced in two readings before any code was written.
- **Running the suite against the pre-change scripts is what made every new case evidence.** Five new
  cases and one changed message: against the old check, exactly six missed and nothing else. The
  sixth was the message change itself, which no reasoning had flagged as testable. A case that passes
  before the change tests nothing.
- **Two independent instruments agreed on all sixteen inbound-link counts, and the second saw what
  the first could not.** Mine counted `[[wikilinks]]`; the librarian's also counted bare slug
  mentions and found **28 bare against 14 linked in `log.md`**. A rewriter matching only the linked
  form would have left two thirds dangling with a green gate.

## Deferred

- **Probe 4 and the `.claude/rules/` move.** Probe 4 needs `/compact`, which is sequenced **after**
  `/ingest`: the journal is the only thing the next session inherits, and compaction before it risks
  the journal to buy a measurement about a proposed refactor. **Consequence of not doing it:** the
  probe directory stands, and the AST-rule move stays blocked — probe 2 passed, but probe 4's own
  stated consequence gates the move as well.
- **The wide reading of the per-type schema** — what a record of each type asserts and what expires
  it, as a fixture the selftest runs. This is S2 criterion 1 and only the field half was built.
  **owner: the wide half is a conversation about each type, not a task**, and running it at the end
  of a long session would run it badly.
- **`record-schema` needs a sweep**, at `/vault-lint`, of at least seven `decisions/` pages and three
  elsewhere that are about the record schema and carry no such tag. **Its boundary is what the
  `_schema.yaml` files are about to settle**, which is why it waits. Three trim candidates go on the
  same list.
- **`basis` is on 321 of 321 pages and declared core by nothing.** Either it belongs in the core and
  the decision page should say so, or it is genuinely optional and every page carries it out of
  habit. One line either way; the schemas leave it optional until then.
- **What `archive/` is has never been decided.** Rule 6 and rule 10 both read `wiki/` only, and the
  two cases pull opposite ways — an undefined tag in `archive/` is a real defect, a counting title
  there is arguably the rule working. `raw/` has a page saying it is frozen testimony; `archive/`
  does not.
- **`lint-waits-for-an-open-sprint` says "/lint has never run", which is false**, and no instrument
  can see it because the falsehood is not a count. Its stated price of twelve inbound links is also
  wrong in kind: a retitle moves no address.
- **`*.yaml` is not pinned in `.gitattributes`** and the six schema files will convert to CRLF on the
  next checkout. **Measured: the parse is CR-clean on this host and the gate stays correct**, so by
  this project's rule — a class is pinned after it costs something — it is not pinned. The
  measurement is what makes the first failure answerable rather than a fresh investigation.

## Feedback to the librarian

No `could-not-close:` lines: every question the retro opened carries an
`answered:` or a `deferred:` with a destination.

- measure: **the sidecar line-ending warning fired again, on the very next ingest.** Committing today's ingest printed *"LF will be replaced by CRLF the next time Git touches it"* for `2026-08-18-the-filename-half-lands-and-the-escape-hatch-falls.coverage.tsv` — the same unpinned `*.tsv` class the previous session recorded, now with a second occurrence rather than one. Still no cost: `vault-coverage.sh` read the sidecar and reported `94 of 94 units, INGEST COMPLETE`, exit 0, with the file already written LF and about to be converted. So [[a-file-class-is-pinned-after-it-costs-something]] still says do not pin it — but the class now converts on every single ingest by construction, which is a different fact from "three files have been converted", and it means the first failure will arrive on a sidecar nobody is watching.

---

- miss: **the selftest figure in `wiki/entities/vault-scripts.md` is one ingest behind.** Its latest
  row still reads *"107 caught, 0 missed, up from 99"*, while the journal of 2026-08-18 and the
  brief generated from it both say **112 caught, 0 missed, up from 107**. The page is the one a
  pre-task reads to price a selftest change, so the stale row understates what two retired cases
  cost. The row exists and was simply not extended by the last ingest — a table that is appended to
  per session is exactly the shape that silently misses one.

- lint: **`sprint.md` and `index.md` disagree on how many filenames carry a count.** `sprint.md`
  says *"11 filenames of 259"* and calls the eleven renames "the first customer of the
  rewriter-and-detector pair"; `index.md` corrects the same figure to thirteen and retires the
  rewriter as overpriced. Measured today with rule 10's own predicate over `wiki/`: **thirteen**.
  Both registers are yours; the older of the two is the one a reader hits first from the sprint
  brief. `sprint.md` line 93 also still reads *"one file of thirteen carries a region"* where the
  denominator has moved to fourteen.

- process: **the probe's own brief for probe 2 names the nonce, which contaminates the observable it
  is reading.** `probe/RUNBOOK.md` prescribes telling the subagent to "report verbatim whether the
  string `PROBE-TEXT-4K7QX2` is present in its context" — but that brief *puts the string in its
  context*, so a subagent quoting it has proven nothing, and the runbook's own principle ("neither
  string is guessable, so 'I can see it' cannot be confused with 'I inferred it'") is defeated by
  the instruction two sections below it. Ran instead: read the target, then report any text that
  arrived with the read and is not in the file — naming no nonce. The same flaw hit probe 1 from the
  other direction: reading `RUNBOOK.md` to learn how to run the probe hands the reader both nonces
  before the measurement starts, so the main session can never be its own clean instrument for
  probe 1 and the hook log is the only honest one. **A runbook that carries the nonce cannot be read
  by the thing being measured** — the general shape is worth a page.

- process: **`grep -c $'\r'` does not count CRLF lines — it returns the file's total line count.** The
  escape collapses to an empty pattern, which matches every line, so the number that comes back is
  large, plausible, and always exactly `wc -l`. Used it to check whether a subagent's edits had
  introduced CRLF; it reported 232, 59 and 57 against three files of 232, 59 and 57 lines, and the
  agreement of the wrong number with a real quantity is the only thing that gave it away. The honest
  instrument is `tr -dc '\r' | wc -c`, which reports the byte count and cannot be confused with a
  line count. Measured after the correction: zero CR bytes, blob and worktree alike. This is
  [[a-measurement-agreeing-with-no-expectation-needs-a-second-instrument]] arriving in a new place —
  the figure agreed with nothing and a second instrument killed it — and line endings are a class
  this project has already been bitten by twice, so the command that lies about them is worth naming.

- miss: **two of the twenty-four `quantity:` declarations were already false while they stood, and
  the field is what hid it.** `concepts/fidelity-to-a-source-and-fidelity-to-the-tree` declared *"a
  third would make the page wrong rather than stale"* — and a third arrived: the section *"A third
  kind, proved on 2026-08-17: fidelity of a move"* was added to that very page while the
  declaration sat in its frontmatter, so the title read "two different properties" over a body
  describing three. `concepts/three-artefacts-three-owners` declared *"the artefacts counted are
  named in the title itself"*, and the page names a fourth artefact with a fourth owner in its own
  body. **Both were caught only because a human-scale reader was retitling them**, and the check
  cannot catch it by construction: a declaration silences the verdict permanently, so the one
  instrument that would notice the drift is the one the field switches off. This is the concrete
  cost of [[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]] — not
  that the escape hatch was untidy, but that it converted a self-correcting check into a claim
  nobody re-read. Worth a page: **a declaration that silences a check must expire or be re-derived,
  because the thing it silences is the thing that would have found it wrong.**

- process: **the LF pin protects the repository and not the working copy, and `git status` cannot
  tell you.** `job_hunt_ai_vault/raw/handoffs/2026-08-17-a-rule-is-written-once-and-rendered.md` is
  **CRLF in all 337 of its lines on disk** while its committed blob is clean LF — and `git status`
  reports it unmodified, because `text eol=lf` normalises on the way in and the file therefore
  compares equal. The pin's own stated reason is the opposite of what it delivered here: *"it
  changes nothing about the repository and everything about the WORKING copy, which is what scripts
  that edit these files actually read"* ([[markdown-is-pinned-to-lf]]). A tool that writes a file
  after checkout leaves CRLF on disk, and nothing reports it. This is the inverse of
  [[line-endings-make-git-status-overstate-what-changed]] — there the command overstated a diff,
  here it is silent while every line ending differs — and the two belong beside each other, because
  a reader who has learned the first will trust `git status` in exactly the case where it says
  nothing. Detected only because a rename sweep made me measure CR bytes across the whole vault;
  `tr -dc '\r' < file | wc -c` is the instrument, and one file of 374 carries it.

- lint: **the schema's own frontmatter example carries `authority:` beside `governs:`** — the exact
  combination [[authority-beside-governs-is-forbidden-on-any-page]] forbids. It is a field
  catalogue rather than a real page, and its comments do say the exclusion out loud ("Optional, and
  forbidden on a rule"; "rules only, and required") — but the block is fenced as a copyable
  frontmatter example and its `type:` is `concept`, so a page copied from it lands outside the
  `ruleclaim` branch, which fires only on `type: rule`. **The alarm about the ruling being wider
  than its gate now has a concrete instance, and it is the schema.** Found while editing that file
  for the `quantity:` removal; deliberately not repaired, because it belongs to the owed
  verdict-plus-selftest-case and not to this clean-up.

- process: **the check reads no field whitelist, so nothing stops `quantity:` from coming back.**
  Measured while tightening rule 10: `vault-check.sh` has no verdict over the *set* of frontmatter
  keys — rule 2 asks what named fields answer for, and an unrecognised key is invisible to every
  rule there is. The field is now rejected in the schema, in `index.md` and in rule 10's own
  comment, and by nothing mechanical. A returning `quantity:` would be inert, since no verdict
  reads it — but "the rule holds in prose and nothing stops an agent from breaking it" is the exact
  shape of the standing alarm about `authority:` beside `governs:`, and this is a second instance
  of it in the same file. Worth deciding once, for both: **either a frontmatter key set the gate
  knows, or an explicit acceptance that field rules are advisory.** Not built — a verdict is the
  owner's to authorise, and this one has no urgency because the field is dead rather than dangerous.

- miss: **three sources disagreed on which frontmatter fields are required, and `basis` is in none
  of them.** `vault-check.sh` required six — `title type status created sources tags`. The decision
  page [[the-frontmatter-core-is-fixed-and-updated-joins-it]] declares a core of **seven**, adding
  `sprint`. And `basis` is carried by **321 of 321** pages, is named on that same page as *"the only
  field conflict resolution rests on"*, and is declared core by neither. The per-folder schemas
  built today encode the decided seven and leave `basis` optional, because a field carried by every
  page is not thereby required — that reasoning is exactly how `quantity:` entered the store. But
  the omission looks like an oversight rather than a decision: **either `basis` belongs in the core
  and the page should say so, or it is genuinely optional and 321 pages carry it out of habit.**
  The owner's call, and it is one line either way. Recorded rather than assumed, and the schema
  files can be changed in the same minute the ruling lands.

- lint: **`archive/` is outside the reach of several rules, and whether that is design or omission
  has never been decided.** Rule 6 reads tags from `wiki/` only, so an archived page carrying a tag
  `tags.md` does not define passes silently — found today when the `schema` split would have left
  three archived pages holding a word that no longer exists, and only caught because the librarian
  went looking. Rule 10 reads titles from `wiki/` only, so four archived pages carry a count today:
  `a-region-is-checked-against-its-rules-governs` (*fifth*), `the-wiki-has-no-tasks-folder`
  (*four*), and two more in their slugs. **The two cases pull opposite ways.** An undefined tag in
  `archive/` is a real defect: the dictionary and the corpus are supposed to describe each other,
  and a page nobody can reach through the tag is exactly what the density rule is about. A counting
  title in `archive/` is arguably correct — `the-wiki-has-five-folders-and-tasks-is-not-one` is
  archived *because* the count went stale, which is the rule working. So the question is not "widen
  the page set" but **what `archive/` is**: frozen testimony like `raw/`
  ([[raw-holds-testimony-and-artefacts-are-frozen]]), or live retired content that the retrieval
  rules still govern. `raw/` has a page saying which it is; `archive/` does not, and the two rules
  above are behaving as if the answer were already known and are disagreeing about it.

- process: **correction to the `quantity:`-can-return line above — it closed itself the same
  session.** That entry said the field was rejected in the schema and in prose and by nothing
  mechanical. The per-folder `_schema.yaml` gate built hours later rejects it as a key no schema
  declares, so the field can no longer be written onto a page at all: measured, a page carrying
  `quantity:` now reddens with *"frontmatter key 'quantity' is in neither the required nor the
  optional list"*. **Half of the standing `authority:`-beside-`governs:` alarm closed the same
  way** — that verdict was widened tonight and now fires on any page carrying both. Left the
  original line standing rather than deleting it, because the pair is the useful record: a general
  gate over the key set retired two specific prose-only rules that had each been queued for their
  own verdict, and the next "this rule has no mechanism" finding is worth checking against the
  general gate before a verdict is written for it.

## Anything else worth keeping

**Three of the four probes are answered, and the answers are in `probe/RUNBOOK.md`.**

- **1 — does the mechanism work at all: PASS.** Both instruments agree. The hook log took a line
  naming `"load_reason":"path_glob_match"` and the trigger file, and the rule's text arrived in the
  session's context attached to the tool result.
- **2 — does it reach a subagent: PASS, and the move proceeds as designed.** A subagent given a brief
  naming no nonce and no rules file made one tool call, opened nothing else, and returned the whole
  rule file verbatim, reporting that it had not opened it.
- **3 — are HTML comments stripped: STRIPPED, so a generated-file banner is free.** On disk the rule
  file's line 6 is an HTML comment; in what reached either reader, the frontmatter and the comment
  are both absent. This matches what the corpus already measured on `CLAUDE.md` region markers.
- **4 — compaction: not run.** Needs `/compact`.

**The `auto mode` instruction is delivered to subagents too.** It reached one whose brief required
the Read tool and told it to prefer Bash; it followed the brief and reported the conflict rather
than resolving it silently. Worth knowing before a brief depends on which tool a subagent reaches
for.

**A tag choice was made with a counter in view, and reported rather than hidden.** Choosing tags for
a new page, the librarian noticed one natural set would push `schema` in `decisions/` past the
threshold and print a twentieth advisory, chose different tags on the merits, and said so. That is
the second instance of an advisory count coming close to steering a librarian's own choice.

## Harness

- **The `authority:`-beside-`governs:` alarm is discharged**, and half of the "rules that live only
  in prose" class with it. The general key-set gate retired two specific verdicts that had each been
  queued. **The next "this rule has no mechanism" finding is worth checking against the general gate
  before a verdict is written for it.**
- **`probe/RUNBOOK.md` gained its answers and two corrections to its own method.** Delete the probe
  directory, `.claude/rules/_probe-paths.md`, the hook and the settings block once probe 4 is
  recorded.
- **`empty_vault` in the selftest now mirrors the `_schema.yaml` files off the pristine copy** — the
  third thing in that one function that has to be swept rather than listed. A fourth will make it the
  thing to read before adding anything to the vault's layout.
- **The `_schema.yaml` parser is guarded against a schema that yields nothing, and not against one
  that yields a wrong set.** A key misspelled in the yaml would reject every page carrying the
  correct spelling — loud, not silent, but a confusing morning.
- **`vault-scripts.md` records the selftest at 107; it is 120.** The table is appended per session
  and silently missed one.
