---
session: 2026-08-17
sprint: S2
commits: ed239f2..814472a
---

# Handoff — 2026-08-17

Anywhere below, a line beginning **owner:** is the owner's own testimony. It outranks the line
it stands beside, and whatever page it reaches earns `basis: human`.

## State

**Done.** The fifth verdict of the marked-region rules is built and proved: a region whose slug
names a current rule that governs a different file is red, written into rule 11 rather than into
the injector. The `governs:` destination-uniqueness verdict was removed by the owner. Every rule of
the repository's `CLAUDE.md` — nine of them now — lives in `wiki/rules/` and is rendered by
`scripts/vault-inject.sh`. The `## Where things are` block is deleted. Two places still asserting
the removed uniqueness are corrected. `pages.base` is committed as the owner's own view.

**Not done, and none of it blocking anything committed:** the mechanism change (`governs:` read as
a field rather than a folder, the marker becoming `<!-- [type]: slug -->`, a verdict for a marker
whose type disagrees with its page, a verdict for a slice with no `governs:`); the fenced-block
defect in the injector; `make`; the map; the project description as a record; the questions
document; the rule forbidding a hand-edit inside a region; the catalogue's `governs` column.

**In flight: nothing. The tree is clean at `814472a`.**

**Next step**, in dependency order: the mechanism change, then the records that only need a page
and a region behind it.

**Checks.** `scripts/vault-check-selftest.sh` — **99 caught, 0 missed**, baseline clean, wall clock
**8m04s**. `bash scripts/vault-check.sh` — green, eleven advisories, region coverage `1 of 13`.
`bash scripts/vault-inject.sh --check` — every rule agrees with the region it governs. `pytest`,
`ruff check` and `ruff format` were **not run, and correctly**: the product has not moved since
2026-08-12 by decision, and nothing in this session touched `src/` or `tests/`. No browser walk,
for the same reason.

## Entities

- **`wiki/rules/`** — from zero pages to nine, in two batches of four and five. Every one of them
  governs `CLAUDE.md`.
- **`scripts/vault-check.sh`** — gained the address verdict inside rule 11; lost the
  destination-uniqueness verdict beside rule 3; keeps a `rulegoverns` table of slug-to-destination
  pairs that the frontmatter pass now retains instead of discarding.
- **`scripts/vault-check-selftest.sh`** — its sandbox now materialises every destination a current
  rule governs, sweeping them out of the rule pages and copying the real file whole. Three cases
  were repaired for cause and one was flipped from red to green.
- **The repository's `CLAUDE.md`** — restructured: two sections merged into one, one section
  deleted, nine marked regions, and a heading that no longer states a count.
- **`job_hunt_ai_vault/pages.base`** — unchanged in kind, changed in standing: it stops being a
  review item.
- **`docs/HANDOFF.md`** — untouched, but its status is now measured rather than assumed: the file
  exists, 29 lines, a pointer, and the project simply no longer routes through it.

## Decisions

**owner:** *the `governs:` destination-uniqueness rule is removed.* It forbade two current rules
from governing one file. Rejected alternative: keep it and stop the migration, since all four rules
of `CLAUDE.md` share that destination. The rule was stricter than the schema it guarded — the schema
says a rule names the one destination **its** text goes to, and says nothing about a destination
taking one rule — and its stated argument, *a renderer that has to pick*, was false: the injector
keys on the pair of file and slug, measured at four rules into one file, four regions, no problems.
Obliges: uniqueness now lives on the pair, held by rule 11 (one slug marking two regions in one
file) and by the fifth verdict (a region in a file its rule does not govern).

**owner:** *"the file stops carrying assertions" means no **unsourced** assertions.* The
dispatch-table decision was taken on 2026-08-16, before a renderer existed, so its two options were
a hand-written assertion or a pointer; the third did not exist. A rendered assertion has a page
behind it, is corrected in one place, and reddens the gate when it drifts. Obliges: a factual record
may render into `CLAUDE.md`, and the project description stays in the file.

**owner:** *`## Where things are` is deleted now; a generator comes later.* The second half of
*dropped or generated*, taken as dropped-first. Rejected: correcting the block, which is what the
drifting-list decision exists to refuse.

**owner:** *`governs:` becomes a property of any page rather than a mark of one folder.* Rejected: a
seventh folder (the folder set was closed the day before, and its admission test rejects a
description that goes stale on its own), and putting the description in `rules/` (which would empty
the admission test that folder stands on). Not built.

**owner:** *the marker becomes `<!-- [type]: slug -->`, with the script substituting the record's
type.* His argument: once a non-rule can render, the word `rule` in the marker is a lie. The session
first objected that this puts a mutable field into an address, then withdrew the objection: the type
is the folder, pages do not move between folders, and the marker becomes a **complete** address into
the vault, which removes the cross-folder lookup that the field-driven design would otherwise need.
Two conditions attached: the word is validated against the closed six-type set rather than matched
as any word, and a marker whose type disagrees with its page gets its own verdict. Not built.

**owner:** *the command list moves into a `Makefile`, not a shell dispatcher.* The session
recommended `scripts/do.sh` because `make` is not installed in this environment and needs none; he
overruled it, and the session agrees the argument was weak — five minutes of setup against a
convention every agent already knows. Obliges: pipelines belong there too, `make check` rather than
four commands remembered in order.

**owner:** *the sprint belongs in the map* of the repository's `CLAUDE.md`, beside the vault and its
librarian. The admission test agreed for the map: an entry earns its place if a session that does
not know it does the work **wrong**, not merely slowly.

**owner:** *rule 10 extends to filenames.* Two pieces of work follow and they are not the same size:
a verdict in the check, which is small, and the renames, which are blocked on the rewriter-and-
detector pair because a filename is what every wikilink resolves to.

**owner:** *stop watching `pages.base`.* It stays tracked — removing it would leave another checkout
without the view the vault documents — but a session commits it without discussion.

**owner:** *S2 criterion 6 is NOT MET*, unchanged, read on the files rather than on the mechanism.

**owner:** *rule 4 — how a slice is executed — migrates first*, chosen on the admission test as the
only one of the four that no test can ever hold.

**Session decisions, taken without asking and reviewed at the retro:** the fifth verdict is a
verdict inside rule 11 rather than a numbered rule 13, because it is the fifth of a set whose other
four live there; the `## Language` section is one rule page rather than two, on the injector's own
criterion that a rule ships one piece of text or it is two rules; rules leave the numbered list for
unnumbered blocks, because a marker stands alone at column zero and an ordinal shipped into the wiki
would drift as the remaining rules migrated.

## How it is built

**The mechanism has two directions and needs both.** The injector walks pages to files: it takes
each current rule page, reads `governs:`, opens **only** that destination, and compares byte for
byte. The check walks files to pages: it sweeps both `CLAUDE.md`s and every markdown under
`.claude/`, finds the regions, and asks whether each is well formed, has a page behind it, and sits
at the right address. Neither sees what the other sees: the injector never opens a file no
`governs:` names, and the check never notices a rule that has no region anywhere.

**What the fifth verdict uniquely catches is the leftover, not the wrong file.** A rule governing A
whose region sits only in B was already red: the injector opens A, finds no region, and rule 12
reports it. The case that survives every other verdict is the region present in A **and also** in B
— rule 11 keys its duplicate check per file, and the injector never opens B. A selftest case built
from the proposal as written would have passed with the new code reverted.

**A marker is an address.** With the type in it, it is a complete one — `<!-- entity: some-slug -->`
resolves to exactly one path — which is why the owner's design removes a lookup rather than adding a
copy.

**The injector strips fenced blocks on both sides**, so a code block inside a `<!-- text -->` slice
is silently dropped and the injector still reports success. Proved on an isolated copy: a slice of
three lines rendered as one, `1 region(s) rewritten, 0 problem(s)`. The stripping exists so that a
documented example of a marker is not read as a marker; it should gate marker **recognition** and
not content **copying**.

**A page outside `wiki/rules/` carrying `governs:` is silently inert** — the injector globs one
folder, and every `governs:` branch in the check is gated on `folder == "rules"`. The field is
neither rendered nor refused.

**The selftest's cost is now a function of the number of rule pages.** 89 cases, each running a full
check at 4.9 s, of which `vault-inject.sh --check` is 1.98 s because rule 12 asks by running the
injector and the injector spawns two `awk` processes per page. Nine pages today; about fifteen
seconds of suite per rule after this.

## Lessons

- **A proposal can be wrong about the hole it describes.** The page behind the fifth verdict named
  the wrong file to touch, stated the defect in a form that is already caught, and `sprint.md`
  repeated the misattribution. A `/pre-task` found all of it before a line was written, and one of
  those findings is what stopped a selftest case that would have passed for the wrong reason.
- **A test built from a specification can pass without the code it tests.** The fix was to build the
  case from the mechanism rather than from the prose: region in the right file **and** a copy in
  another, which nothing else reports.
- **A suite's fixture must materialise what the subject reads, not what an earlier rule read.** The
  sandbox created placeholders for `sources:` paths only, so the first real rule page would have
  reddened the pristine copy before a single case ran.
- **Prose does not survive a shell command string.** It broke twice in one session — once losing the
  heredoc carrying the retro file, once executing a markdown code span as a command. Eight heredoc
  constructs were then written to files and parsed cleanly, which is how the syntax was cleared and
  the transport blamed. The first explanation, *"it stumbled over quotes"*, was a guess presented as
  a diagnosis, and that is the part worth keeping.
- **A ritual that runs unannounced is indistinguishable from improvisation.** The owner could not
  tell `/retro` had been invoked. It had been; nothing was said out loud, and nothing showed its
  steps. A ritual nobody can see running is one nobody can tell was skipped.
- **A stated count over a list drifts, and the repair is to stop stating it.** The heading `Four
  rules that cannot wait for a question` was about to head nine.

## Deferred

- **The mechanism change** — field-driven injection, `[type]:` markers, the two new verdicts. Design
  is agreed in full; not building it leaves the project description, the *retrospective* definition
  and the map with nowhere to live.
- **The fenced-block defect** — until it is fixed, the by-hand `rg` recipe cannot become a rule and
  stands as unsourced prose in a section that is otherwise rendered.
- **`make`, the map, and a generated `Where things are` are one unbuilt mechanism** — a generator
  that fills a marked region from the tree rather than from a page. Building it once serves three
  things; not building it leaves the `## Commands` block drifting, and it already has: it claims
  `vault-check.sh` takes ~2 s and the measured figure is 4.9 s.
- **The rule forbidding a hand-edit inside a region.** Nothing anywhere says it. The mechanism is
  currently protected by two people remembering it.
- **The questions document for an empty repository** — `proposals/`, `status: idea`, growing by one
  line each time a question cannot be closed without the owner. Four such today.
- **The catalogue's `governs` column.** The Obsidian half exists as a named view; the agent half,
  five lines, does not — so the reader who most needs *which rules render into this file* is the one
  who cannot get it.
- **The detector for `current` pages citing archived ones.** Deferred by the owner twice this
  session; the standing brief alarm carries it.
- **The filename renames** under the extended rule 10 — blocked on the rewriter-and-detector pair;
  the worst offender carries 23 inbound links.
- **The selftest's cost.** One `awk` pass over all rule pages instead of two processes each.
- **The repository `CLAUDE.md`'s first sentence**, which now says the file *is a map and a handful of
  rules*: the map was deleted and nine rules render. Deliberately not patched, because patching it
  would have been another sentence of unsourced prose from the same author.

## Feedback to the librarian

- miss: the brief's third alarm says `the-three-tags-are-not-split-and-five-advisories-stand` is "still false in its title". Measured at `ed239f2`: its `title:` was already corrected to "The dense tags are not split corpus-wide, and every per-folder advisory that stands is named here" and carries no quantity, so rule 10 is silent and correct. What is stale is the **filename**, which rule 10 deliberately does not cover (the filename is the address; 23 inbound references). Surfaced when the owner asked why the rule had fired again — it had not.
- miss: `wiki/proposals/a-region-is-checked-against-its-rules-governs.md` lists **Touches** as `scripts/vault-inject.sh` and `scripts/vault-check-selftest.sh`, omitting `vault-check.sh` — where its own *What it would take* paragraph puts the join. The injector iterates rule pages and looks only inside each `governs:` destination; it holds no table of regions found elsewhere, and giving it one would put a second copy of the swept governed set in the tree. Surfaced at implementation, from the code, before writing a line.
- miss: `sprint.md` and `what-the-harness-build-waits-on` both call it *"the fifth verdict of rule 12"*, but rule 12 by design contains no logic of its own — it asks by running the injector. The verdict is about a region's **address**, which only the sweeping check sees, so it lands in rule 11. Surfaced in the same pre-task.
- miss: the same proposal states the hole as *"a region carrying a rule's slug in a different governed file"*. Measured against the code: the pure wrong-file case is **already red today** — `region_of` returns `ERR carries no region for it` and rule 12 fails, naming the absence in the right file rather than the stray in the wrong one. What the fifth verdict uniquely catches is the **leftover duplicate**: the region present in the right file *and also* in another governed file, where rule 11 passes (its `dupslug` key is per file) and rule 12 never looks. A selftest case built from the proposal as written would have passed without the new code.
- process: no page records how a proposal's own defect is corrected before the proposal is built. The three lines above are all corrections to one unbuilt page that retires the day the work lands.
- process: the selftest sandbox materialised only the paths named in `sources:`, never the one a rule names in `governs:` — so the first real rule page would have turned the pristine copy red before a single case ran, taking every `run_clean` and every expected exit code with it. Fixed by sweeping the destinations out of the current rule pages and copying the real file **whole**, so the region it carries arrives with it. Found by the pre-task reading the code, not by the suite.
- process: the first migration coupled three existing cases, exactly as the suite's own comment predicts (*"the question to ask when adding one is which cases are now coupled"*). `inject_vault_relative` needed a path that does not resolve at the repository root and `CLAUDE.md` now does, so it moved to `index.md`. The coverage case asserted `cover 1 of`, a number that moves with every migration, so it now asserts that the file it marked stopped being listed as unmarked. `empty_vault` left a governed file carrying a region whose page it had just deleted, so it sweeps the regions out too. Measured after: **99 caught, 0 missed**, up from 97.
- process: rule 4 left the numbered list in `CLAUDE.md` and became a marked block. A marker must stand alone at column zero, which breaks a list item, and shipping the ordinal inside the rule page would put a number in the wiki that drifts as the other three migrate. The heading still reads *Four rules* and is still true: three numbered, one marked.
- miss: `vault-check.sh` forbade two current rules from governing one destination, and the schema it guards says no such thing — it says a rule names the one destination **its** text is injected into. The check was stricter than its own text, which is the shape of [[the-hook-was-stricter-than-the-rule-it-enforced]] happening a second time. It surfaced on the mechanism's first real use, blocking the migration of the four rules that share `CLAUDE.md`. **Removed by the owner, 2026-08-17.** Its stated argument — a renderer that has to pick — was false: the injector keys on the pair of file and slug, measured at four rules into one file, four regions, `0 problem(s)`. What it looked like it protected is held by rule 11 (one slug, two regions in one file) and by the fifth verdict (a region in a file its rule does not govern).
- lint: the librarian marked that contradiction live in five places before the owner resolved it in the same turn — `> [!CAUTION]` blocks on `a-deprecated-rule-does-not-render` and `rules-becomes-a-type-of-its-own`, a dated note on the verdict table of `marked-regions-and-the-prose-outside-them`, a caution on each of the three new rule pages, and an `- alarm:` in `log.md`. All of it is now stale and needs retiring against the decision. It is the librarian's write, not the session's.
- measure: the four rules of the repository's `CLAUDE.md` are rendered from `wiki/rules/`, proved unchanged word for word against `ed239f2` by diffing the rendered regions against the pre-migration list items. Selftest **99 caught, 0 missed**; one case removed with the rule it tested and one added in its place, so the count is level rather than unmoved.
- process: **owner, 2026-08-17: "the file stops carrying assertions" means no UNSOURCED assertions.** A rendered assertion has a page behind it, is corrected in one place and reddens the gate when it drifts — the disease [[the-repository-claude-md-becomes-a-dispatch-table]] was written against is cured rather than renamed. That decision was taken on 2026-08-16, before a renderer existed, so its two options were hand-written assertion or pointer; the third did not exist yet. The project description therefore stays in `CLAUDE.md` as a rendered record.
- process: **owner, 2026-08-17: `## Where things are` is DELETED now, and a generator comes later** — the second half of *dropped or generated*, chosen as dropped-first. Measured against `e478c19` the block carries four defects: `scripts/` is two scripts behind (recorded), `.claude/` omits `templates/` (**not recorded until now**), the vault line omits `wiki/rules/`, `pages.base` and `archive/` and its closing clause contradicts [[governs-is-a-path-from-the-repository-root]], which fixed the vault directory name a day ago (**not recorded until now**), and `docs/HANDOFF.md` names a file that exists but that the project no longer routes through. The two unrecorded ones are new instances for the register on [[claude-md-can-lose-an-assertion-but-cannot-strand-a-page]], which stood at seven.
- miss: a non-rule page carrying `governs:` is **silently inert** — `vault-inject.sh` globs `wiki/rules/*.md` only, and every `governs:` branch in `vault-check.sh` is gated on `folder == "rules"`. So the field is neither rendered nor refused outside that folder, which is this project's most-repeated failure shape: a green that examined nothing. Whatever is decided about widening it, that silence has to become either a rendering or a refusal.
- measure: **the selftest now takes 8m04s** (user 2m31, sys 3m00), against the 201 seconds recorded before rule 9 was retired and the ~158 that left. Measured cause, not guessed: 89 cases × 4.9 s per full check = 436 s, plus the tree copy per case. Of those 4.9 s, `vault-inject.sh --check` is **1.98 s** — about 40% — and it scales linearly with the number of rule pages, because rule 12 asks by running the injector and the injector spawns two `awk` processes per page. Nine rule pages today; **each further migrated rule adds roughly fifteen seconds to the suite**, so marking up the remaining twelve governed files takes it past fifteen minutes. The fix, when it is wanted, is one pass over all pages instead of two processes each.
- lint: two claims of the removed uniqueness outlive it and are the session's to correct, not the librarian's: `job_hunt_ai_vault/CLAUDE.md` still documents `governs:` as *"required, and unique across current rules"*, and `scripts/vault-check.sh` still carries a comment arguing the uniqueness where no verdict prints any more. **Both corrected in this session at `ba998a0`** — they are harness files rather than the librarian's, so they were the session's to fix. Kept here as the record of a class, not as an open item.
- process: **owner, 2026-08-17: the command list moves into a `Makefile`, not into a shell dispatcher.** I recommended `scripts/do.sh` because `make` is not installed in this environment (Git Bash ships none) and the dispatcher needs no install; he overruled it, and correctly — my argument was five minutes of setup against a convention every agent already knows without being told. The value is pipelines: one `make check` instead of four commands remembered in the right order. Evidence for moving it at all, measured today: `## Commands` says `vault-check.sh` takes *~2 s* and it now takes **4.9 s**, a list drifting from reality inside the same session that changed it.
- process: **owner, 2026-08-17: the sprint belongs in the map** of the repository's `CLAUDE.md`, as an entity beside the vault and its librarian. The admission test we agreed for the map: an entry earns its place if a session that does not know it does the work **wrong**, not merely slowly — not knowing where `src/` is costs ten seconds of `ls`; not knowing the vault exists costs every reason the session produced. By that test the vault, its librarian and the sprint are in; the locations of tests, sources and hooks are out.
- process: the command map, the generated `Where things are`, and `make help` are **one unbuilt mechanism** — a generator that fills a marked region from the tree rather than from a vault page. Building it once serves three things, and it is what the owner's *dropped now, generated later* is waiting on.
- process: **owner's verdict, 2026-08-17: S2 criterion 6 is NOT MET**, unchanged. Region coverage moved `0 of 13` → `1 of 13` and nine rules render, but the criterion asks about **files**, and one file of thirteen carries a region. This is the second time he has read that criterion on the files rather than on the mechanism being built — the first was on the day it was written.
- process: **owner, 2026-08-17: rule 10 extends to FILENAMES.** A title carrying a measurable quantity is already caught; a filename carrying one is not, and the check reads only `title:` by design — the reasoning written into it is that the filename is the address, so renaming moves something and retitling does not. He decided the rule covers both. **Two pieces of work follow and they are not the same:** a verdict in the check, which is small; and the renames themselves, which are blocked on the rewriter-and-detector pair, because the worst offender has 23 inbound links and a filename is what every `[[wikilink]]` resolves to. At least four filenames carry a count today, and some of those counts are invariants that ask for no rename.
- process: **owner, 2026-08-17: stop watching `pages.base`.** He edits it often through Obsidian, and its diff is not a review item. It stays tracked in git — removing it would leave any other checkout without the view the vault documents — but a session commits it without discussion and never treats a change to it as something to explain.
- process: **the owner could not tell that `/retro` had run.** The skill WAS invoked and its body loaded; what was missing is the announcement and the visible steps. The instruction is explicit — say which skill is being used and for what, then follow its checklist out loud — and skipping that makes a ritual indistinguishable from improvisation **from the only side that matters**, which is his. A ritual nobody can see running is a ritual nobody can tell was skipped.
- process: **file content must never travel inside a shell command string, and this cost two failures in one session.** Diagnosed rather than guessed: eight heredoc constructs were written to files and parsed — apostrophes, backticks, em dashes, arrows, HTML comments, backslashes, 200-line bodies — and **all eight parse cleanly**, so heredoc syntax is not the fault. The fault is the transport: the command reaches bash wrapped in quotes, and prose carrying backticks or apostrophes is then either executed as command substitution or breaks the wrapping. It fired once on the retro file and once, seconds later, in the very command written to investigate it — `bash: line 9: span: command not found`, a code span in prose executed as a command. The remedy is not a script, because the script is invoked by the same command: **prose is written with the file-writing tool, and a generator reads its input from a file rather than from an argument.** This is a rule-page candidate by the admission test, and it has a sibling already on the record: [[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]].

## Anything else worth keeping

- **The librarian refused to resolve a contradiction it found**, marked both halves, named the
  choice as the owner's, and the owner resolved it in the same turn. The one-writer design did
  exactly what it was built for, on the first occasion that tested it. It then went back and
  annotated six pages that were still claiming the question open, rather than let the corpus argue
  with itself.
- **Hand-probing before the suite.** Four states measured in seconds against an eight-minute run,
  and the same habit found the fenced-block defect, which no existing test would have caught because
  no rule ships a code block yet.
- **A verification that the migration changed no words.** The rendered regions were diffed against
  the list items they replaced, and every non-marker line of the previous file was checked for
  presence: only the deleted section, two headings and the counting phrase are gone.

## Harness

- Build the mechanism change: `vault-inject.sh` reads `governs:` as a field; `vault-check.sh` accepts
  `<!-- [type]: slug -->` against the closed type set; a verdict for a marker whose type disagrees
  with its page; a verdict for a `<!-- text -->` slice on a page with no `governs:`; selftest cases
  for each.
- Fix the injector's fence handling so a code block inside a slice travels: gate marker recognition
  on the fence, not content copying. Two selftest cases — a slice carrying a fence renders it, and a
  marker inside a fence inside a slice does not close it.
- Add a `Makefile` with the project's pipelines and point `## Commands` at it.
- Write the map into the repository's `CLAUDE.md`: the vault and its librarian, the sprint, the
  routes. Its admission test is agreed.
- Write the rule that forbids hand-editing text inside a marked region.
- Add a `governs` column to `scripts/vault-catalogue.sh`.
- Add a verdict for a filename carrying a measurable quantity, under the extended rule 10.
- Reduce the injector to one `awk` pass over all rule pages.
- `elsewhere:job_hunt_ai_vault/sprint.md` — criterion 5 still says *"none has, and the first
  migration is next session's work"*, which stopped being true at `e81a6e4`.
