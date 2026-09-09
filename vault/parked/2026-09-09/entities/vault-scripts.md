---
title: "The scripts that hold the vault, and the one that proves the others still check anything"
type: entity
status: current
authority: vault-scripts
basis: code
sprint: S0
created: 2026-08-13
sources: ["scripts/vault-check.sh", "scripts/vault-units.sh", "scripts/vault-coverage.sh", "scripts/vault-catalogue.sh", "scripts/vault-check-selftest.sh", "archive/2026-08-13/2026-08-13-second-brain-phase-1/handoffs/2026-08-13-second-brain-phase-1.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "archive/2026-08-19/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell/handoffs/2026-08-19-the-gate-checked-itself-against-a-decoy-and-the-guard-objection-fell.md", "archive/2026-08-23/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md"]
tags: [vault, testing]
---

# The five scripts

All five are plain bash over the files. Nothing here needs a database, a model, or the network.
*(This page said "four" until 2026-08-15, when `vault-catalogue.sh` was added.)*

| Script | The question it answers |
|---|---|
| `scripts/vault-check.sh` | is the store structurally sound? **18 failing conditions**, one line per violation, 2–3 s — *the count is history from 2026-08-26; `--rules` prints the register* |
| `scripts/vault-units.sh` | what are the claims in this document? one line per unit |
| `scripts/vault-coverage.sh` | has every claim in this document been accounted for? **0.7 s**, down from 22 |
| `scripts/vault-catalogue.sh` | what pages are there at all? writes `catalogue.md` from the frontmatter of every page |
| `scripts/vault-check-selftest.sh` | do those rules still catch what they were written for? **58 cases**, measured 2026-08-15, ~2 min — **61 later the same day**, with `wiki/proposals/` |

## `vault-check.sh` — what fails the run is printed, not listed here

**The enumeration that stood here is no longer the live description, 2026-08-26**, on the owner's
ruling. It stands below under a dated history heading of its own, and it is replaced by a register
the script prints:

```
bash scripts/vault-check.sh --rules
```

**A printed register cannot drift and this list always had**
([[a-printed-register-cannot-drift-and-a-maintained-one-always-has]],
[[the-vault-scripts-page-stays-a-hub-and-the-gate-and-its-suite-get-subject-pages]]). The list is
not deleted, because a page in this store loses no text; it stops being the live description.

## The eighteen-condition list, moved here from the live description — 2026-08-26

**Nothing below is edited.** It is the enumeration as it stood, with its own corrections, kept for
the history it carries and superseded as a description by `--rules`, which printed **16 headings**
on 2026-08-26.

Re-derived from the script on 2026-08-13; it said **8** until then, which was true several commits
earlier. The whole file was rewritten the same day and went from **71 s to 3 s**, by reading
frontmatter instead of whole files and making one pass instead of one grep per field per page.

1. a required directory is missing — `raw/handoffs`, the four `wiki/` folders, `archive/`; **five `wiki/` folders since 2026-08-15**, when `proposals/` was added ([[proposals-are-a-folder-not-a-status]]) — and rule 2 needed no change at all, because `want` is the folder name minus its trailing `s`;
2. a register is missing — `CLAUDE.md`, `index.md`, `tags.md`, `log.md`;
3. a page lacks one of the six required frontmatter fields;
4. `type:` disagrees with the folder the page sits in;
5. a `decisions/` page carries no `decided:` date;
6. `status:` is something other than `current` or `deprecated`;
7. a `deprecated` page is still in `wiki/` instead of `archive/`;
8. the frontmatter block is never closed by a second `---`;
9. a page has two `tags:` lines;
10. a page carries fewer than 2 or more than 4 tags;
11. a path in `sources:` does not exist;
12. two `current` pages claim the same `authority`;
13. a `[[wikilink]]` resolves to nothing — or to an **empty** file, which once satisfied it;
14. a page is an orphan, linked from nowhere in `wiki/`, `archive/`, `index.md`, `tags.md` or
    `sprint.md`;
15. the **repository's** `CLAUDE.md` names a page that does not exist;
16. a tag is used on a page and is not defined in `tags.md`;
17. a journal in `raw/handoffs/` carrying `session:` does not carry **the set 1–8** of the
    template's numbered sections. An empty section is a legal answer — the word "none" — but a
    dropped one is knowledge that was never asked for, and **§7 is the only channel through which a
    miss against the librarian is ever reported**
    ([[the-handoff-template-maps-onto-the-categories]]). Nothing else in this repository looks
    inside `raw/` at all, so a six-section handoff would pass every other rule here and lose two
    categories in silence.

    **It is the set, not the count, and it strips fences** — both corrected the day the rule was
    written. Eight occurrences is not eight sections: dropping §7 and writing a second §6 counts
    eight, and so does renumbering §7 to §3. And a `## 7.` quoted inside an example block is not a
    section; every other link rule in this script had stripped fences since the day a `<script>`
    comment satisfied an id search, and this one was added without it — **the third time in this
    one file** ([[an-example-inside-a-code-block-satisfies-a-search]]);
18. **`catalogue.md` is not what `scripts/vault-catalogue.sh` produces** — added 2026-08-15 in
    `b58ec48`. Rule 9 fails in two ways with two messages, absent and stale, and both are the one
    question: is that file the generator's output. It is compared by **regenerating and diffing,
    never by mtime** — a checkout rewrites mtimes and the first staleness check in this project
    fired on every clone for exactly that. What is *not* done here is the load-bearing half:
    `catalogue.md` is absent from the register list rules 4 and 5 read for links and must stay
    absent, because it links to every page and would leave the orphan rule running, passing and
    proving nothing ([[the-catalogue-is-generated-not-maintained]]).

Two more conditions **print without failing**, deliberately: a registered tag used on no page, and
a tag on more than 20 pages. Both are conditions the vault grows into rather than breaks into, and
neither has a fix that is correct to apply on the spot — re-tagging pages this session never
touched is a `/lint` job and the owner's call. An alarm that fires every run and cannot be acted
on is one you learn not to read.

**The second of those two was re-measured on 2026-08-16 and the sentence above is the old rule.**
It is still two advisories and they still print without failing; what changed is what is counted.
**A tag is now measured inside a single folder of `wiki/`, and the advisory prints above ten** —
one line per tag per folder, naming the folder. `archive/` is not measured, because nothing is
answered from it. Neither half of that is new: **ten is the ceiling already written into the
librarian's own definition** — stop and report a miss above about ten pages opened for one question
— so it is a property of the reader and does not move when the corpus does, which is what this
project requires of a threshold ([[the-growth-signal-is-the-brief]]); and **per folder** because
`decisions/` grows monotonically while `lessons/` grows only when something burns us, so one
absolute count over both tracks the project's age instead of the tag's power to classify. The floor
falls out for free — a folder of ten pages or fewer can never produce a slice over ten — and so
does a fact one corpus-wide number cannot state: a tag can be healthy in one folder and useless in
another ([[the-folder-is-the-first-narrowing]]). **Five lines print at `2036d98`**, and each is
named by a decision: [[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]].

**It cost no second pass.** The seventh section already collected every tag of every page; the
change derives the folder from the page's own path in that same pass and counts per
`(folder, tag)` pair instead of per tag. **`archive/` never matches the pattern**, so it is
excluded by construction rather than by a rule — which is the cheap kind of exclusion, since there
is nothing to keep in step later.

Three properties of it are load-bearing rather than incidental:

- **only the frontmatter block counts.** Read line-wise, a fenced `yaml` example carrying the six
  field names satisfies the required-fields rule on a page with no frontmatter at all, and an
  `authority:` line inside such an example forges a duplicate against a real page — whose obvious
  "fix" is to change the real page;
- **both YAML spellings of a list are read**, inline and block. Obsidian's own property editor
  emits the block form, and while only the inline form was parsed a page written in Obsidian
  contributed no tags at all: its unregistered tags went unreported and the 2-to-4 rule never
  fired, because a page with no entries never reaches the count;
- **one `awk` pass over the whole corpus**, not one `grep` per field per page — that was some 700
  processes for 75 pages. A check the librarian is told to run after *every* write has to stay
  cheap enough that it is actually run.

**Run it after every write.**

## `vault-units.sh` — the denominator, and what it cannot see

A unit is one claim: a heading, a table row, a bullet, a numbered item, a bold or bulleted line
inside a blockquote, or the **opening line of a paragraph**. It was narrower until 2026-08-13 —
only paragraphs and bullets opening in **bold** — and that narrowness reproduced the exact failure
the script exists to prevent: sections written in plain prose contributed nothing but their
headings while coverage reported 100%.

Two document shapes are answered explicitly: a file with **no blank lines at all** (every line not
matched by a stronger rule becomes a unit, because "a line after a blank one" finds nothing there),
and an **unclosed fence** (a warning on stderr and exit 3, because a complete-looking accounting of
a truncated document is worse than no accounting).

**A third of the same family was open until 2026-08-15**, and it is the one the script's own
documentation did not list. A paragraph is counted when it opens *after a blank line*, and the
heading rule set `blank = 0` — so **text written flush against its heading, with no blank line
between, was invisible to the denominator**. The fix is one word: `blank = 1` on the heading rule.
**It was priced before it was applied**, which is the part worth copying: **+2 units across all six
sources**, both inside the owner's instructions note — line 4, already verdicted by hand, and line
55, which was not — so the whole cost of closing it was one line of `awk` and one verdict, and no
closed source went red. Found on the first document not written from this project's own template,
which is what a limitation of this kind waits for.

**A line under a bullet is deliberately still not a unit.** It is that bullet's continuation, not a
separate claim, and treating it as one would inflate the denominator with fragments nobody can
verdict.

**Fenced content produces no units at all.** The reader toggles on every line that opens or
closes a fence and skips everything between, so a fenced block needs no verdict, gets none, and
`INGEST COMPLETE` says nothing whatever about it. This is not hypothetical: **§3 of the old
handoff — the module map, the one place the layout of `src/jobhunt/` was written down — is a
single fenced block.** It was never a unit, never had a verdict, and the vault has no page for it.
Read the denominator as *claims outside code fences*, and where a source's substance lives inside
one, that is a subject to compile by hand or to record as known negative space.

## `vault-coverage.sh` — the tally

Two modes, chosen by whether the sidecar `<source>.coverage.tsv` exists. **Verdict mode** lists
units carrying no verdict and verdicts that are not verdicts, and prints `INGEST COMPLETE` only
when both lists are empty; **evidence mode** is a first pass that greps distinctive tokens from
each unit against the wiki to help build the sidecar, and exits 1 always, because a first pass must
not read as a verdict to anything checking the exit code.

A verdict is `page:<name>` (the page must exist and be non-empty), `journal`, `elsewhere:<where>`
or `skip:<reason>` — there is no fifth option. The existence rule is the **weak half** of what
`page:` means; the strong half — that the page received the claim — is
[[the-verdict-is-the-write]] and no script reaches it. Names come first and free prose after ` — `; the
prose is kept, because a verdict that explains itself is worth more than a tidy one. **`journal`
is the one verdict that takes nothing after it**: it is matched exactly, and prose appended to it
is not a verdict at all.

**That grammar was undocumented until 2026-08-13 and was discovered by breaking it**, twice in one
direction. A third tab field turns twenty words of prose into page names; and the rule that reads
the names was tightened — to catch a name after a comma-space — into one that rejected the free
prose this file's own header promises. **The tightening was worse than the defect it fixed**: it
turned one real annotation into eleven `BAD VERDICT` lines and made the ingest gate red on data
committed six commits earlier, with no legal fix available. The rule that stuck reads names up to
an em dash, which is how every verdict in this vault already wrote its prose.

## The `sources:` rule checks that a path exists, never that it still holds the claim

Rule 11 is satisfied by a file being present. It says nothing about whether that file still says
what the citing page says it says — and that gap has been met at scale: **24 pages cited
`docs/HANDOFF.md`, which since `d30b317` is a 27-line pointer.** They were repointed to the
verbatim copy in `raw/`, where the claims actually are.

It is the same blind spot as a verdict naming a page that does not contain the claim: mechanical
provenance, no fidelity. See [[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]],
and [[fidelity-to-a-source-and-fidelity-to-the-tree]] for why the two directions of fidelity are
different properties with one instrument between them.

**Rule 4 has the mirror-image blind spot, found by the first audit.** A `[[wikilink]]` must
resolve to a non-empty file — and a page in `archive/` is one, so a `current` page may rest its
argument on a `deprecated` one and the gate stays green:
[[a-live-page-can-argue-from-a-deprecated-one]].

**Headings are excluded from the denominator.** That is why the tool prints *332 of 332* on the old
handoff while `vault-units.sh` emits 362 lines for the same file: the 30 headings carry verdicts
too, and the arbiter does not count them.

**Neither script checks fidelity**, and coverage says so in its own header: a page whose content a
later slice replaced passes both modes, identifiers and all
([[a-long-source-contradicts-itself-and-the-first-hit-is-the-old-one]] is the instance).

## `vault-catalogue.sh` — the one file whose contents are nobody's to choose

Added 2026-08-15 in `b58ec48`. It reads the frontmatter of every page in `wiki/` and `archive/` and
prints one table row each — name, title, `status`, `sprint`, tags — grouped by category, with the
counts produced by the same run that produces the rows, so a stated count cannot drift from the
list it heads ([[a-stated-count-drifts-from-the-list-it-heads]]). `--write` puts it in
`catalogue.md`; without the flag it prints, which is how rule 9 compares.

**Run it after any write under `wiki/` or `archive/`, before `vault-check.sh`** — the gate is red
while the catalogue is older than the corpus.

Three details are the same ones the other scripts learned the hard way: the vault is discovered by
"the top-level directory containing a `wiki/`" in the identical idiom ([[the-vault-directory]]);
every path is `-print0`/`xargs -0` because the vault's name has contained a space; and all of a
section's pages go through **one** `awk`, because one process per file turned the selftest's ~45
regenerations into four thousand processes. **The whole run is 1.0 s over 108 pages, measured
2026-08-15**; the first version, at one `awk` per file, cost the selftest minutes. A `|` inside a title is replaced with `&#124;`, which
would otherwise end the markdown cell it sits in.

Why it exists at all, and why it must never join the link register:
[[the-catalogue-is-generated-not-maintained]].

## `vault-check-selftest.sh` — what "verified by removal" actually means

This vault's most repeated phrase has a mechanical meaning, and this script is it. Every rule is
broken **on purpose** in a throwaway copy of the vault, one at a time, and the check must name that
defect and exit with the right code. **58 cases, 0 missed, measured 2026-08-15 at `b58ec48`**, and **61 of 61, 0 missed, re-measured later the same day** with the three cases the fifth category brought — a proposal in its own folder, one mistyped as a decision, and the folder removed. **Wall-clock 201 s, measured 2026-08-15**, of which about **43 s is the catalogue regeneration rule 9 added** — 43 wrapper cases at 1.0 s each, measured rather than apportioned ([[a-rule-over-every-page-makes-every-test-fragile]]). One `awk` per run instead of one per wrapper would return roughly 30 s of it, and that optimisation is deferred ([[the-audits-findings-are-owed-to-the-owner]]) —
this line read 55 at `42f7a56` and 54 on 2026-08-13; the CRLF sidecar was the case added between
those two, and the catalogue brought the last three. **The one that matters most is the orphan
case**: it plants a page nothing links to, regenerates the catalogue *so that the catalogue does
link to it*, and still expects the orphan reported. That is what holds `catalogue.md` out of the
link register for good, rather than a comment asking the next author not to add it. Several of them are over
`vault-coverage.sh` rather than `vault-check.sh`, because a verdict grammar that accepts anything
is not an accounting.

- the vault is never touched: everything happens under `mktemp -d`, and citations that point
  outside the vault are recreated as empty placeholders, because the rule under test asks whether a
  citation *resolves*, not what it contains;
- **a mutation that changes nothing is reported as a failure**, not as a pass — `diff -rq` against
  the pristine copy runs before the check does, and **the subject pages are picked by what the
  cases need rather than by sort order**. Both exist because reshaping the corpus made **three
  cases go quiet while staying green**: a `sed` that matches nothing leaves a tree that is clean by
  construction, and all three were cases asserting that *nothing happens*
  ([[a-test-green-under-any-implementation]]). A case that tests nothing is the failure this whole
  family is about;
- there are negative cases too: mutations after which the check must stay **green**, and cases
  where one output line must appear while another must not — a legitimate edit once produced two
  violations from one cause;
- `SCRIPTS=/some/dir bash scripts/vault-check-selftest.sh` runs the suite against a candidate copy
  of the scripts, so a rule can be changed and tested before it is installed.

The rule it enforces on us: **if you think a rule is wrong, change it in the selftest first.** And
the reason the whole thing exists is [[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]] —
a check never observed failing is not known to check anything.

## What they will not do

They will not depend on the vault's directory name — see [[the-vault-directory]] — and every path
inside them is quoted, because an unquoted `$(find ...)` word-split a directory name containing a
space and the check printed `ok` having read nothing.

**There is a fifth self-test and it is not bash**: `scripts/hook-selftest.ps1`, **29 of 29,
measured 2026-08-14** — this page said 25 until then, [[session-hooks]] said 29 and `log.md` says
31, which is three numbers for one script inside one store
([[a-stated-count-drifts-from-the-list-it-heads]]) — over the two hooks — those are PowerShell for a reason the shell scripts do not share, and it is on
[[session-hooks]].

## What the scripts gained on 2026-08-17

**`vault-check.sh` gained rule 10 and rewrote rule 8**, and the counts above moved with them.

- **Rule 10 — a title carries no measurable quantity.** It fails a page whose title holds a digit or
  a number word and which carries no `quantity:` line. It **asks and does not judge**, because no
  lexical predicate separates a count that belongs to the page from one that belongs to the world
  ([[the-title-check-asks-and-does-not-judge]]). Four exemptions, each because it is not a count: a
  code span, an ISO date, a digit glued to a letter, and the word *one*.
- **Rule 8 — the journal section set — was rewritten twice over.** It reads the set from
  `.claude/templates/handoff.md` instead of counting numbered sections; it judges a journal **only
  while no `.coverage.tsv` sidecar sits beside it** ([[a-journal-is-judged-only-while-it-is-uncompiled]]);
  it tells a journal from a form by a property rather than by a filename
  ([[a-journal-is-told-from-a-form-by-a-property-not-a-filename]]); and it stopped printing
  `unexpected [none]` when nothing was unexpected
  ([[a-placeholder-that-collides-with-real-data]]). **The numbered wording in the list above is the
  old rule** and is kept as history: the set it names, 1–8, no longer exists.

**`vault-check-selftest.sh` caught 71, missed 0** on 2026-08-17 — up from 61 at the start of that
session. Two of its cases had been quiet for some time and were repaired the same day: they cleared
the subject's inbound links from a **copied** list of registers while the check reads a longer one
([[a-copied-list-drifts-and-a-sweep-cannot]]).

**`vault-coverage.sh` reports seven of seven sources `INGEST COMPLETE`**, measured after
`.claude/skills/vault-lint/SKILL.md` stopped skipping `*/TEMPLATE.md` in its coverage loop. **This
script never mentioned the template**: the claim that it did was asserted from prose
([[a-claim-asserted-from-prose-rather-than-from-the-file]]).

**A hook now runs `vault-check.sh` unasked**, when a journal is written into `raw/handoffs/` —
[[the-journal-gate-hook]]. The scripts are no longer only what an agent remembers to run.

## The numbering in this section is this page's own, and it is not the script's

*(Recorded 2026-08-17.)* The list of **18 failing conditions** above is an enumeration written on
this page and it has never matched `vault-check.sh`'s own rule numbers. The script has rules 1–8
plus 5b, then 10, 11 and 12; **9 is retired and dead**
([[a-retired-rule-number-is-never-reused]]). Every other page in this corpus cites the **script's**
numbering, and that is the one to use.

Nothing above is removed, because each numbered item is still a true statement about something the
check fails on. Read them as a list of conditions, not as rule numbers. The mismatch was found at a
`/pre-task`, where the next rule's number had to be established before anything could be written.

## What the scripts gained on 2026-08-17, in the second session of that day

**There are six scripts now**, and the vault gained a rendering step. The write ritual is
**inject, then check** — there is no catalogue step any more.

| Script | What changed |
|---|---|
| `scripts/vault-inject.sh` | **appeared.** The renderer |
| `scripts/vault-check.sh` | rules 11 and 12 added, rule 9 retired, rule 1 grew the sixth folder, the frontmatter pass learned `governs:` |
| `scripts/vault-catalogue.sh` | survives and **only prints**; `--write` exits 2 |
| `scripts/vault-check-selftest.sh` | **97 caught, 0 missed**, up from 71 at the start of the session |

**`scripts/vault-inject.sh` — the renderer.** Two modes: it writes, or `--check` prints every
disagreement and writes nothing. It is a script, not an agent and not a hook. What travels from a
rule page is the `<!-- text -->` slice, not the page
([[what-travels-from-a-rule-page-is-a-marked-slice]]), and a deprecated rule renders nothing
([[a-deprecated-rule-does-not-render]]). On 2026-08-17 it reported agreement over **zero rules**,
which is agreement over nothing and says so in those words.

**Rule 11 — marked regions in the harness.** The governed set is swept, never listed: both
`CLAUDE.md` files and every `*.md` under `.claude/`
([[the-governed-set-is-swept-and-markdown-by-property]]). It goes red for markup that is broken and
prints one advisory line for a governed file carrying none
([[a-region-is-a-paired-comment-named-for-a-rule]],
[[a-governed-file-with-no-region-is-an-advisory]],
[[an-advisory-prints-one-line-and-sorts-what-it-names]]). Its coverage denominator is walked off
`ARGV` so that an empty governed file cannot fall out of it
([[a-denominator-is-walked-off-the-input-list]]). **It stood at `0 of 13` on the day it was built**,
and that advisory does not fail the run.

**Rule 12 — a region agrees with its page.** It asks by running `vault-inject.sh --check`, never by
a second implementation of the comparison ([[a-check-asks-by-running-the-writer-it-checks]]).

**Rule 9 is retired and `catalogue.md` is deleted** ([[the-page-list-is-a-query-not-a-generated-file]]).
The selftest's `regen_catalogue` wrapper went with it, and so did the **43 seconds of the suite's
201** that the wrapper cost. The two citations of [[the-catalogue-is-generated-not-maintained]]
higher up this page describe the mechanism as it stood until 2026-08-17 and are left standing as
history.

**The selftest count, broken down as it was measured:** +18 for regions and rules, +10 for the
injector, −2 for the retired catalogue cases, +1 for the generator — 71 to 97, 0 missed.

**Two failures met while building it**, both cheap and both recorded: an apostrophe inside an awk
comment ended the shell quote ([[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]]), and
`empty_vault` held its own copy of the layout and went red when `wiki/rules/` arrived
([[a-copied-list-drifts-and-a-sweep-cannot]]). The mechanism itself was hand-probed on nine failure
paths before the suite was pointed at it ([[hand-probe-a-new-mechanism-before-running-the-suite]]).

## What the scripts gained on 2026-08-17, in the third session of that day

**No script appeared or left. Two changed, and one of them got slower by a factor of two and a half.**

| Script | What changed |
|---|---|
| `scripts/vault-check.sh` | **gained** the address verdict, inside rule 11; **lost** the `governs:` destination-uniqueness verdict beside rule 3; keeps a `rulegoverns` table of slug-to-destination pairs that the frontmatter pass now **retains instead of discarding** |
| `scripts/vault-check-selftest.sh` | **99 caught, 0 missed**, up from 97 — one case removed with the rule it tested, one added in its place, so the count is *level* rather than unmoved. Its sandbox now materialises every destination a current rule governs |
| `scripts/vault-inject.sh` | unchanged, and now the reason the check costs `4.9 s`: rule 12 runs it, and it is **`1.98 s` of that** |

**The `rulegoverns` table is the load-bearing change.** The frontmatter pass had been reading `governs:`
and throwing it away once its own verdicts were done; keeping it is what makes the address verdict a
join between two tables the check already builds, rather than a second sweep
([[the-address-verdict-joins-an-existing-rule-instead-of-becoming-its-own]]).

**The uniqueness verdict was removed by the owner, not weakened by a session**
([[governs-uniqueness-is-removed-and-the-pair-carries-it]]). Its selftest case was **flipped from red to
green** rather than deleted: two rules on one file with two regions is now asserted legal.

**The sandbox's fixture defect is worth reading as a class.** It created placeholders for `sources:`
paths only, never for the destination a rule names in `governs:` — so the **first real rule page would
have reddened the pristine copy before a single case ran**. Fixed by sweeping the regions out of the rule
pages and copying the real destination **whole**, so the region it carries arrives with it. Found by a
`/pre-task` reading the code, not by the suite ([[a-fixture-must-materialise-what-the-subject-reads]]).

**The selftest now costs 8m04s.** That is measured, its cause is measured, and it scales with the number
of rule pages rather than with the corpus
([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]). **The `4.9 s` figure for
`bash scripts/vault-check.sh` contradicts the `~2 s` printed in the repository's `CLAUDE.md`**, and that
block is not the librarian's to edit ([[the-command-list-moves-into-a-makefile]]).

**Region coverage stands at `1 of 13`** and the advisory names the twelve files that carry none
([[a-governed-file-with-no-region-is-an-advisory]]). Eleven advisory lines print in total and the run
exits 0.

## What the scripts gained on 2026-08-18

**No script appeared or left. Three changed, and `vault-inject.sh` changed materially four times in
one session.**

| Script | What changed |
|---|---|
| `scripts/vault-inject.sh` | walks `wiki/*/*.md` pre-filtered by `grep -l '^governs:'`; takes the marker's type word from the page's folder; **refuses a slice carrying a wikilink**; carries a fenced block through instead of deleting it; compares with a sentinel so the tail is visible; writes one blank line after the slice, **inside** the region |
| `scripts/vault-check.sh` | the six type words are swept off `wiki/` as `singular:plural` pairs and passed into both awks, replacing the inline `sub(/s$/)`; the marker scanner's net widened from the literal `rule` to any word; the region address is `folder/slug` and the pair table is keyed the same; one new frontmatter verdict; the `folder == "rules"` gate now covers **two of its three branches** |
| `scripts/vault-check-selftest.sh` | **107 caught, 0 missed**, up from 99. Sandbox destination sweep follows the injector's glob; `empty_vault()` strips regions by the marker's *form* rather than by the word `rule`; eight new cases; three fixtures rewritten to the new agreeing shape; **`run_render` is new** |

**`run_render` is the only helper in that suite that asserts on the bytes a writer produced** rather
than on what the check said. That distinction is the point: every other case reads a verdict, and a
writer can be wrong in a way no verdict mentions
([[a-check-asks-by-running-the-writer-it-checks]]).

**Four changes to the injector, each with its own page:** the wider walk and the moved red
([[a-slice-with-no-governs-is-red-and-the-inert-field-is-gone]]); the fence
([[a-fenced-block-inside-a-slice-survives-into-the-destination]]); the comparison that could not see
a trailing newline ([[a-command-substitution-strips-the-newline-a-gate-compares]]); and the
separator ([[the-injector-writes-the-separator-inside-the-region]],
[[the-rendered-form-is-defined-once-and-read-by-the-writer-and-the-comparison]]).

**The wider walk is free, and the cost model on record was wrong about what to count.** Measured
2026-08-18, three runs each: `vault-inject.sh --check` **1837 ms** over every folder against
**1898 ms** over `wiki/rules/` alone, and `vault-check.sh` **5258 ms** against **5168 ms**. The
pre-filter costs **113 ms**; the real cost is **processes per page**, at about 40 ms per spawn on
this platform ([[measure-before-optimising-and-count-processes-not-pages]]).

**Selftest wall clock was not timed this session**, so the 8m04s figure stands unrevised rather than
restated ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

**One warning the check carries and the injector does not**: the *no apostrophes in an awk comment*
guard. The separator change edited the one program without it
([[an-apostrophe-in-an-awk-comment-ends-the-shell-quote]]).

## What the scripts gained on 2026-08-19

**No script appeared or left. Two changed, and both changed because the key set became a thing the
gate reads rather than a thing it carries.**

| Script | What changed |
|---|---|
| `scripts/vault-check.sh` | rule 2 lost its hardcoded six required fields and now reads `wiki/<folder>/_schema.yaml`, with **three new verdicts** — an undeclared key, a folder with no schema, a schema parsing to no required keys ([[the-per-folder-frontmatter-schema]]). Rule 10 lost the `answered` short-circuit, the reader that set it and the tail of its note offering the field, and its word list gained `second`…`twentieth`; the comment was rewritten rather than patched. `ruleclaim` widened to any page carrying `authority:` beside `governs:` ([[the-ruleclaim-branch-widens-to-any-page-carrying-authority-and-governs]]) |
| `scripts/vault-check-selftest.sh` | **120 caught, 0 missed**, up from 112. Two cases inverted, eight added, one corrected because a message it greps moved; four fixtures gained `sprint:`; `empty_vault()` now mirrors the `_schema.yaml` files off the pristine copy |

**The row above this one said `107 caught` and was one ingest behind.** The reading of 2026-08-18 was
**112**, recorded in that day's journal and in the brief generated from it, and this table was not
extended by that ingest. The row is left as it was written and corrected here, per the rule for a
figure this store has already renumbered too often
([[the-region-coverage-figure-is-dated-where-it-stands]],
[[a-title-corrected-in-place-is-not-a-supersession]]). **A table appended to once per session is
exactly the shape that silently misses one**, and this is the instance.

**Every one of the new cases was proved against the pre-change scripts before it was trusted**:
five new cases and one changed message, of which **exactly six are missed by the old check and
nothing else** ([[a-case-that-passes-before-the-change-tests-nothing]]). The sixth is the changed
`ruleclaim` message, which no reasoning had flagged as testable
([[a-cosmetic-change-is-load-bearing-when-a-test-greps-the-output]]).

**The nine cases the tightening broke were the suite's own fixtures**, not the check
([[the-fixture-corpus-goes-red-before-the-rule-it-was-never-written-for]]). `empty_vault()` is now
the **third** thing in that one function which has to be swept off the pristine copy rather than
listed; a fourth will make that function the thing to read before adding anything to the vault's
layout.

**A verdict here cannot be proved in a sandbox.** `vault-check.sh` resolves its vault relative to
itself, so every new verdict this session was proved by planting an offending page in the real tree
and reverting in the same command
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

**The run as it stands, 2026-08-19**: `vault-check.sh` exits 0 with **19 advisories** — eighteen tag
density and one region coverage — zero `note` lines, and **the filename advisory prints nothing for
the first time** ([[the-filename-advisory-prints-one-name-per-line]]).
`vault-inject.sh` reports 0 rewritten and 0 problems.

## What the scripts gained in the second session of 2026-08-19

**No script appeared or left. One changed, and it changed because it had stopped being a fixture of this
corpus.**

| Script | What changed |
|---|---|
| `scripts/vault-check-selftest.sh` | 149 insertions, 82 deletions. Its sandbox **mirrors the repository** rather than copying the vault to `vault_copy` ([[the-selftest-sandbox-is-a-mirror-rather-than-a-renamed-copy]]); the `governs:` sweep runs **before** the `sources:` placeholder loop ([[a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first]]); and a new case runner, **`run_found`**, grades a case on whether discovery landed on a real vault instead of on a whole-run green |

**The row above this one recorded `120 caught, 0 missed`, and that reading was already dead when it was
written.** The same ingest that recorded it compiled the page whose `sources:` cite
`job_hunt_ai_vault/wiki/decisions/_schema.yaml` — and those citations are what the placeholder loop then
materialised into a decoy vault. **Measured on the tree that existed the next session: `caught 24, missed
96`**, reproduced with the six schemas reverted to their committed state, so the `basis` promotion is not
implicated ([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

**The readings in order, all 2026-08-19:** `24/96` baseline; **`86/34`** with the loop ordering fixed;
**`119/1`** with the sandbox mirroring the repository. **The last one is the case `the vault is renamed`,
which is a corpus finding rather than a suite defect**
([[the-corpus-names-the-vault-directory-and-a-rename-is-a-rewrite]],
[[the-renamed-vault-case-is-graded-on-the-question-it-asks]]) — and it is why *"the fix moved it from 24
to 86"* was published as **the** cause and was not one
([[the-first-published-diagnosis-can-be-a-real-defect-and-still-not-the-cause]]).

**`run_found` was proved able to fail before its score was believed**
([[a-case-that-passes-before-the-change-tests-nothing]]): the mutation was replaced with one that moves
the vault to depth 3, past discovery's `-maxdepth 2`; the case reported MISSED with the other 119
unchanged; and the plant was reverted in the same command
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

**The suite's exit code is its score and always was.** Its last line is `[ "$fail" -eq 0 ]`, and with one
case planted broken it returns **1**. A session claimed otherwise three times in one hour, every time
through a pipeline ([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]],
[[a-claim-labelled-measured-came-from-an-instrument-reporting-its-own-exit-code]]).

**Wall clock, measured this session: roughly five minutes on an idle machine.** It copies **401 files**
per case — the copy is ~0.25 s and the diff ~0.14 s, and **the gate is the rest**
([[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

**The run as it stands:** `vault-check.sh` exits 0 with **20 advisories** — nineteen tag density and one
region coverage — and zero `note` lines; `vault-inject.sh` reports 0 rewritten and 0 problems.

# What the three scripts gained on 2026-08-19, and the timing on the record is a lower bound

**`scripts/vault-inject.sh`** gained a `render:` branch, the `whole` writer, `paths_of()`,
`marked_by()`, and deletion by marker with two ways of finding an orphan
([[the-whole-mode-owns-a-file-end-to-end]], [[deletion-keys-on-the-marker-and-nothing-else]]).

**`scripts/vault-check.sh`** gained the value enumeration
([[a-fields-legal-values-live-beside-its-legal-keys]]), a coverage rule reading *region or whole
generation* ([[the-criterion-on-governed-files-is-reworded-to-admit-full-generation]]), explicit
recognition of the generated marker
([[a-generated-files-marker-escaped-a-red-verdict-by-an-accident-of-spelling]]), and `\r` stripping
in the value loader — but not in the two beside it
([[no-cr-reaches-awk-on-this-host-and-the-container-is-where-it-bites]]).

**`scripts/vault-check-selftest.sh`** had **nine SIGPIPE-prone conditions rewritten** and cases
added; **`scripts/hook-selftest.ps1`** gained cases for the guard branch and for comment stripping.

| Reading | Value, 2026-08-19 into 2026-08-20 |
|---|---|
| `bash scripts/vault-check.sh` | exit 0, **21 advisories**, 0 notes |
| `bash scripts/vault-inject.sh --check` | clean |
| `powershell scripts/hook-selftest.ps1` | **54 caught, 0 missed**, exit 0, from 40 at the session's start |
| `bash scripts/vault-check-selftest.sh` | **130 caught, 0 missed**, measured after the AST move |

**The wall clock above is a figure to stop quoting.** This page records *"roughly five minutes on an
idle machine"*; a run on 2026-08-19 **exceeded a 600-second timeout** and finished in the
background. That is a lower bound rather than a reading — nothing timed it end to end — but it is
already double the figure in circulation, and each case copies the whole tree, so the cost grows
with the corpus ([[the-selftest-cost-scales-with-the-rule-pages-it-renders]],
[[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]). **Worth timing
properly before the number is quoted again**, and it is owed as a `measure:` line.

**And the suite's fully-green reading came with a correction to what a miss was.** It reported
`caught 124, missed 0` after the value cases and `caught 130, missed 0` after the deletion cases.
The last figure on the record was `caught 119, missed 1`, the miss being *the vault is renamed* —
which now passes; and *the generator lists a new page* was **never a real miss** but the SIGPIPE
flake ([[a-quiet-grep-at-the-end-of-a-pipe-reports-a-match-as-a-failure]]).

## Two scripts joined it on 2026-08-20, and one grew a flag

- **`scripts/vault-archive.sh`** — the first tool here that moves a path and rewrites its citations
  ([[vault-archive-sh]]). Usage:
  `bash scripts/vault-archive.sh [--dry-run] <date> <session> <kind> <file>...`. It runs the gate
  itself afterwards and exits on that code.
- **`scripts/vault-check.sh --lint`** — the tag-density advisories moved behind a flag, and
  `/vault-lint` is the only caller that passes it. A bare run went from twenty-one advisories to one
  ([[the-tag-density-advisories-move-behind-lint]]). **An unknown argument exits 2**
  ([[the-gate-exits-on-a-usage-error-with-a-code-of-its-own]]).
- **`scripts/vault-check-selftest.sh` runs its cases concurrently**, `JOBS` defaulting to 8:
  **1093 s to 368 s**, byte-identical output
  ([[the-selftest-was-serial-because-every-case-wrote-into-one-directory]],
  [[no-verdict-lives-in-a-variable-in-a-parallel-suite]]).

**The wall-clock figure this page carried for the selftest is superseded by a real end-to-end
reading** ([[the-gates-cost-grows-with-the-corpus-and-rule-pages-are-the-minor-term]]): the gate
itself is **8512 ms** on a 379-page corpus, and the suite is 130 of those.

## The selftest readings on 2026-08-20, second session

- **`scripts/vault-check-selftest.sh` — `caught 135, missed 0`**, from 133. Two cases and one
  fixture variant added, both about `render:` on a `concepts/` page: one for an absent field, one
  for a value outside the schema's list. **The absent-field case was run against the unchanged
  injector first and read `MISSED`** — `134 caught, 1 missed`, the miss being that case and nothing
  else ([[a-case-that-passes-before-the-change-tests-nothing]],
  [[an-absent-render-is-red-on-a-page-that-renders]]). **The wall clock was not re-measured**; the
  suite's parallel form was timed at 368 s the day before and nothing in these cases changes its
  shape.
- **`scripts/hook-selftest.ps1` — `caught 70, missed 0`**, unchanged. **Three assertions were
  hardened** to pin the literal `` `bash scripts/vault-check.sh` `` rather than the words announcing
  it, and no case was added
  ([[a-selftest-case-can-pin-the-announcement-while-the-thing-it-announces-is-broken]]). **A suite
  whose count did not move can still have got stronger**, and one of its cases is a known hazard on
  a red tree ([[the-green-gate-selftest-case-is-deferred-and-the-fixture-repair-cannot-reach-it]]).
- **`scripts/vault-inject.sh` no longer defaults `render:`.** Absence is a verdict of its own, and
  `""` is spelled out as its own case arm ([[an-absent-render-is-red-on-a-page-that-renders]]).

## What moved on 2026-08-20, third session

- **`scripts/record-pre-task.ps1` — appeared, and it is not a vault script.** It is what `/pre-task`
  runs to record itself, in PowerShell for the reason every hook here is
  ([[the-ritual-records-itself-rather-than-being-detected]], [[the-pre-task-ledger]]). **It lives
  under `scripts/` rather than `.claude/hooks/` deliberately**: it is a command a session runs, and
  under `.claude/hooks/` the registration check would find it owing neither an entry nor a
  dot-source ([[the-plan-check-hook]]).
- **`scripts/vault-inject.sh` requires `paths:` only under `.claude/rules/`.** The requirement keys
  on the destination rather than on the mode, because a rule delivered by a hook message has no file
  to match ([[paths-is-required-where-it-is-read-and-nowhere-else]]). **The condition was first
  written as one glob that matched none of the destinations it guards**, and a selftest case turned
  over on the next run ([[a-refusal-written-as-one-glob-can-match-none-of-the-paths-it-guards]]).
- **`scripts/vault-check-selftest.sh` — `caught 136, missed 0`**, from 135: the pair of cases the
  `paths:` condition needs, one per side, less the one they replaced. **It was also edited while
  bash was executing it**, and the run collapsed with missing result files that read as a suite
  defect ([[a-shell-script-was-edited-while-bash-was-executing-it]]).
- **`scripts/hook-selftest.ps1` — `caught 94, missed 0`**, from 70, for the plan hook and the write
  net. **A suite can print the same green for code that never executed**: a missing dot-source went
  quiet rather than failing, and the only signal was the count that did not move
  ([[a-fixture-must-materialise-what-the-subject-reads]], [[the-pre-task-state-library]]).

## What the scripts gained on 2026-08-21

- **`scripts/vault-authority.sh` — appeared.** It answers the question the admission rule is decided
  by: does this claim already have a page ([[no-new-entity-where-an-existing-one-can-carry-the-claim]],
  [[authority-becomes-the-index-and-is-required-outside-rules]]). Subcommands: `--list`, `--near`,
  `--group`, `--check`, `--orphans`, `--binding`, `--trace`; with no argument, `--list`. It walks the
  corpus **once**, frontmatter only, and every subcommand reads that one pass — which is what makes a
  sweep over the whole store the wide half of the reading rule rather than a cost.
  **`--trace <page>` is the reverse of the coverage sidecar**, which already recorded source line →
  page and had no way back; it is nearly free because the trail already existed
  ([[the-sidecar-is-the-single-definition-of-compiled]]).
- **`scripts/vault-catalogue.sh` prints `authority` per row** — **558 lines and 109,053 bytes** over
  the whole corpus in one command, from 536 lines before. It is the instrument the ten-page ceiling
  was always written against: the ceiling is about *opening* a page and never about searching for one
  ([[the-folder-is-the-first-narrowing]]).
- **`scripts/vault-check.sh` gained rule 13**, which asks whether a page carries an `authority:`
  nothing can look up — and asks it **by running `vault-authority.sh --orphans`** rather than by
  re-deriving the condition ([[a-check-asks-by-running-the-writer-it-checks]]).
- **The suite refuses to run at all if either delegating tool is empty.** A rule that delegates by
  running a script is silenced by a zero-byte stub: measured 2026-08-21, an empty
  `scripts/vault-authority.sh` made rule 13 print **not one line**, and every case written for it
  would have passed having tested nothing
  ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]],
  [[a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first]]).
- **`scripts/vault-check-selftest.sh` — `caught 141, missed 0`**, from 136. The run of readings was
  **136 → 132/9 → 133/8 → 141/0 → 140/1 → 141/0**, and the check was never wrong in any of them: the
  first two are the fixtures the new required fields reddened, and the fifth is a case whose subject a
  ruling had abolished ([[the-fixture-corpus-goes-red-before-the-rule-it-was-never-written-for]],
  [[a-rule-over-every-page-makes-every-test-fragile]]).
- **`empty_vault` sweeps the vault's top-level markdown** instead of listing the registers by hand.
  The list had drifted twice before and drifted a third time when `authority.md` joined rule 1's
  existence check ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).
- **`scripts/hook-selftest.ps1` — `caught 108, missed 0`**, from 107.

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

# The writer and the gate learned that `governs:` may name more than one file — 2026-08-21

**`scripts/vault-inject.sh` gained `governs_targets()`**, a parser that accepts a bare path and an
inline list and refuses anything else. Its walk now feeds the main loop one `page<TAB>destination`
pair per line instead of one page, and the loop body is untouched
([[the-governs-list-is-expanded-at-the-walk-and-the-address-verdict-asks-membership]]).

**`scripts/vault-check.sh` gained `govsplit()`** in the frontmatter pass, written from the same
rules so the two readers cannot disagree about spelling. The `governs|` fact is emitted once per
destination and rule 11's address comparison asks membership rather than equality.

**`scripts/hook-selftest.ps1` gained the register of which hook refuses and which speaks**, as cases
rather than prose ([[a-refusal-is-possible-on-pretooluse-alone-and-the-register-is-a-test]]).

**Readings at the end of that session, each exit code read from its own invocation**
([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]):

- **`scripts/vault-check-selftest.sh` — `caught 147, missed 0`**, from 144, and **the count moved by
  exactly the three cases added**. All three exist to reach a branch the whole corpus cannot
  ([[a-green-gate-can-be-no-evidence-about-the-branch-just-changed]]).
- **`scripts/hook-selftest.ps1` — `caught 114, missed 0`**, from 110, moved by exactly the four cases
  added. **Two of the four printed `MISSED` on their first run for real defects in the case code**,
  so both directions were observed on the real tree
  ([[a-tree-broken-for-a-real-reason-is-a-better-fixture-than-a-planted-offender]]).
- **`bash scripts/vault-check.sh` exits 0** with the one standing advisory, `a region or whole
  generation covers 4 of 15`; **`bash scripts/vault-inject.sh` reports 0 rewritten, 0 generated,
  0 removed, 0 problems.**

**None of it is committed.** The six files stood modified in the working tree at HEAD `340ccb0` when
the journal was written and still did at the ingest that compiled it.

*(Compiled from `raw/handoffs/2026-08-21-a-rule-the-owner-never-gave-is-struck-and-governs-learns-a-list.md`.)*

# Three scripts changed on 2026-08-22

- **`scripts/vault-archive.sh` — a fifth `kind`, `pages`**, and the first that does not come from
  `raw/`. Its `sources:` rewrite had nothing to do on its first cargo, because no page cited the
  retired page in `sources:` — **checked by hand before the move rather than trusted**, which is what
  separates a correct zero from an instrument failing towards *nothing to do*
  ([[vault-archive-sh]], [[an-instrument-that-fails-towards-nothing-to-do]]).
- **`scripts/vault-authority.sh` — the argument dispatch became a loop over the argumentless modes**,
  with the exit code the worst of those run rather than the last. The operand-taking modes keep single
  dispatch and refuse anything after them. **It used to drop every flag after the first without a
  word** ([[an-instrument-that-answers-half-a-question-in-the-voice-of-a-whole-one]]).
- **`scripts/vault-check.sh` — rule 14 and the `blockgoverns` verdict.** Rule 14 names every
  owner-attributed block carrying no Cyrillic, behind `--lint`, reading UTF-8 lead bytes rather than a
  character class ([[the-quote-is-cyrillic-rule-stands-as-an-advisory-and-stays-out-of-the-core]]).
  The verdict joins the existing frontmatter verdicts rather than taking a rule number
  ([[governs-takes-a-bare-path-or-an-inline-list-and-the-block-form-is-red]],
  [[a-retired-rule-number-is-never-reused]]).

**Readings at the end of that session, each exit code read from its own invocation**:
`vault-check.sh` 0 with one standing advisory at `a region or whole generation covers 6 of 15`;
`vault-check-selftest.sh` **`caught 158, missed 0`** from 147, eleven cases added;
`hook-selftest.ps1` **`caught 123, missed 0`** from 114, nine cases added; `vault-inject.sh` 0 and
idempotent, a second run rewriting no region; `vault-authority.sh --check --binding` 0 on both halves
**after the repair above**.

**The selftest figure was taken against the exact tree that was committed**, after two earlier runs
had measured trees that had since moved
([[a-figure-measured-before-the-tree-moved-is-not-a-measurement-of-this-tree]]).

**And `caught 158` is a number two cases larger than it looks.** The same session found two cases that
had run, passed and never been counted, so the suite it started from was reporting a total that was
short ([[no-verdict-lives-in-a-variable-in-a-parallel-suite]]).

# Four scripts changed on 2026-08-23, and one verdict was written and removed the same day

- **`scripts/vault-check.sh` no longer holds the legal `status` values.** They were a hardcoded
  pair in the `awk` pass with the pair restated in the message beside it; both are gone, and the
  six `wiki/*/_schema.yaml` files carry the list instead — five `[current, deprecated]`,
  `proposals/` carrying `implemented` as a third
  ([[implemented-joins-the-legal-status-values-and-the-status-block-enters-every-schema]],
  [[the-legal-value-list-lives-in-each-folders-schema]]).
- **The gate gained a verdict named `realised` and lost it within about an hour.** It reddened
  `status: implemented` inside `wiki/`. **It is not in the tree**, and what was wrong was the
  reading rather than the mechanism: the mark opens a state and had been read as an address
  ([[a-mark-that-opens-a-state-is-not-a-mark-that-names-a-place]]).
- **`scripts/vault-inject.sh` stopped reading an unknown status as not-current.** Its test was
  positive — `current` or else — so every other word fell into the retired branch and **a rule page
  carrying one silently stopped rendering**. It now refuses a status it does not know. The same
  shape has caught this store before, where `render:` is read only after a page without `governs:`
  has been skipped ([[the-injector-reads-render-only-after-it-has-skipped-a-page-without-governs]]).
- **`scripts/vault-archive.sh` gained a seventh refusal**, scoped to `kind = pages`
  ([[vault-archive-sh]]).
- **`scripts/vault-check-selftest.sh` had a case repaired.** `a status the schema lacks` grepped
  the gate for a message the same day's change had deleted
  ([[a-local-proof-that-a-new-verdict-fires-is-not-a-regression-run-of-the-old-ones]]).

**Readings at the end of that session, each exit code read from its own invocation**
([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]):

| command | reading |
|---|---|
| `bash scripts/vault-check.sh` | exit 0, one standing advisory: `a region or whole generation covers 7 of 15 harness markdown files` |
| `bash scripts/vault-inject.sh` | `0 region(s) rewritten, 0 file(s) generated, 0 removed, 0 problem(s)` |
| `bash scripts/vault-authority.sh --check --binding` | exit 0; 515 slugs; 182 prohibition, 23 deferral, 10 divergence |
| `bash scripts/vault-check-selftest.sh` | `caught 158, missed 0`, exit 0 — **run five times that day, reading `caught 157, missed 1` in the middle three** |
| `pwsh scripts/hook-selftest.ps1` | **not run**, in a session that changed three scripts |

**The corpus stood at 530 pages under `wiki/` and 40 under `archive/`.**

**Nothing was committed.** All of it stood unstaged at `b17fe90`, the commit the session began at —
21 changed paths, and the same 21 were still unstaged when this was compiled.

*(Compiled from `raw/handoffs/2026-08-23-the-archive-becomes-history-and-three-refusals-land.md`.)*

# Four scripts changed again in the second session of 2026-08-23, and the field they were changed for now exists

- **`scripts/vault-check.sh` gained a verdict on the *target* of `decided_by:`.** It resolves the
  wikilink, reads the target's `type:`, and reddens anything that is not a `decisions/` page. The
  message names the type it found ([[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]]).
- **It gained a `--lint` counter of the shortfall**, over `wiki/proposals/` and `wiki/rules/` alone
  — the population criterion 3 narrowed to earlier the same day. Read at this ingest, every page it
  names is a `proposals/` page, because `wiki/rules/` is full.
- **No second existence check was written, and that was decided rather than skipped.** Measured
  first: a `decided_by:` target that resolves to nothing already prints `broken wikilink`, because a
  wikilink in frontmatter is swept exactly like one in the body; a target that exists and is an
  `entity` printed nothing and the gate exited 0. **Only the second case was new**, so only the
  second got a verdict. A second existence check would be a second reader of a fact rule 5 already
  reads, and two readers of one fact drift.
- **The link sweep now excludes the four RAW archive kinds** — `handoffs`, `plans`, `specs`, `notes`
  — from the set whose outbound links must resolve, while leaving them resolvable as targets. This
  is the repair that unblocked the archive step of the previous ingest
  ([[what-an-archived-page-asserts-is-frozen-and-how-it-is-found-is-live]]).
- **`scripts/vault-archive.sh` gained a second precondition and had a real bug repaired.** The
  precondition refuses to release a proposal carrying `status: refused` without `decided_by:`; the
  bug was `--include` placed after `--`, which made it an operand and ran the `pages` precondition
  with no file filter at all ([[vault-archive-sh]],
  [[an-option-after-a-double-dash-is-an-operand-and-the-search-runs-unfiltered]]).
- **`scripts/vault-check-selftest.sh` gained ten cases and a runner that reads the injector's own
  exit and message**, which no helper there did before. **One of its helpers now hardcodes a real
  page slug and forty-three cases stand on it**, which is a coupling nothing points at from the
  page's end ([[a-fixture-helper-that-hardcodes-a-page-slug-couples-every-case-built-on-it]]).
- **The six `wiki/*/_schema.yaml` gained `Links:`; two of them gained `decided_by:`.**

**Readings at the end of that session, as the journal records them, each exit code read from its own
invocation** ([[an-exit-code-read-through-a-pipe-belongs-to-the-last-stage]]):

| command | reading |
|---|---|
| `bash scripts/vault-check-selftest.sh` | `caught 168, missed 0`, exit 0 |
| `pwsh scripts/hook-selftest.ps1` | `caught 123, missed 0`, exit 0, 58 s — **it had not been run against the four changed scripts at all** until then |
| `bash scripts/vault-inject.sh` | 0 rewritten, 0 generated, 0 removed, 0 problems |
| `bash scripts/vault-check.sh` | exit 0, one standing advisory at `7 of 15` |
| `bash scripts/vault-check.sh --lint` | exit 0 |
| `bash scripts/vault-authority.sh --check --binding` | exit 0 |

**`uv run pytest`, `ruff` and the browser walk were not run and are not owed**: no Python changed and
the product has not moved since 2026-08-12.

**Measured at the ingest that compiled this section:** `wiki/` holds 546 pages, `wiki/rules/` holds
sixteen and every one of them carries `decided_by:`. The schema comment stating the promotion
happened *once all fifteen rule pages carried it* is a statement about the moment of the promotion,
and the sixteenth page — the style rule — landed after it.

*(Compiled from `raw/handoffs/2026-08-23-the-cause-of-a-page-becomes-a-field-and-the-style-rule-lands.md`.)*

# An arithmetic script joins them — 2026-08-24

| Script | The question it answers |
|---|---|
| `scripts/lessons-queue.py` | which lessons are cited by **neither a rule nor a proposal**? Python, stdlib only, run through `uv` |

**Measured on the day it landed: 94 of 140 `lessons/` pages** — 21 cited by a rule, 36 by a
proposal, 46 in the union.

**It does not group them, deliberately.** Grouping lessons into families is the judgement the
`/vault-lint` collector dispatch exists to supply, and a script that guessed at it would hand the
agent an answer instead of a worklist
([[the-librarian-is-blind-to-a-recurring-family-from-where-it-stands]]).

**It is the first Python among these**, which is why `*.py` was pinned to LF the same day
([[the-python-class-is-pinned-to-lf-before-it-cost-anything-in-this-repository]]).

*(Two further Python scripts landed that day — `scripts/session-dialogue.py` and its selftest — and
they are harness scripts rather than vault scripts: they read the transcript store, not this store
([[the-session-dialogue-extract]]).)*

# Four scripts changed in the second session of 2026-08-24, and two of them learned to print a register

**`scripts/vault-check.sh` gained `--rules`**, a second flag that prints the rule register swept from
the script's own `^# [0-9]` headings and exits 0 without reaching the vault. It is a **mode** and not
a filter — it runs no check, never prints `VAULT-CHECK: ok`, and always exits 0 — which is why it
stands outside the prohibition on hiding a verdict behind a flag
([[the-rules-flag-is-a-mode-rather-than-a-filter-and-stands-outside-the-flag-prohibition]]). The
usage-error message now names both legal arguments. The reading of 2026-08-24: **15 heading(s)**.

**Rule 5c reads `binding:` off the `decided_by:` target in the same `awk` pass that already read its
`type:`**, and carries the narrowed `idea` verdict
([[a-verdict-reads-every-field-it-needs-in-the-pass-that-already-opened-the-page]],
[[the-idea-and-decided-by-verdict-is-built-narrowed-to-a-non-deferral-cause]]).

**Rule 13 makes one invocation of `vault-authority.sh --orphans --check` where it made two**, and the
`grep '^VAULT-AUTHORITY:'` that used to filter the first of them is gone — **it discarded every line
without that prefix, so half of the rule swallowed what the other half would have reported.** A pair
taken in a quiet window: 1.54 → 1.30 s, an effect below the day's noise at gate level.

**`scripts/vault-check-selftest.sh` gained `--list`, `--only <pattern>`, and an argument contract**
where it had none: an unknown argument exits 2. `--list` **sweeps the file** rather than walking the
dispatchers, so it sees the cases written inline that no dispatcher owns
([[the-case-list-is-swept-from-the-file-because-some-cases-have-no-dispatcher]]). `wanted()` takes
the case number even when the case is skipped, so a filtered run does not renumber the report
([[a-filter-sits-at-the-top-of-a-dispatcher-and-still-takes-the-case-number]]). New in it:
`run_arg_case`, `plant_idea_pair`, and five cases.

**`scripts/vault-inject.sh` lost five process spawns per page.** `status:` and `render:` are read in
one `awk` pass instead of one `awk` and a `sed | head | sed`; `governs_targets()` lost the
`sed | head -1 |` in front of its `awk` and gained an anchored match with `exit`. **The parser's
four rules were not retyped**
([[measure-before-optimising-and-count-processes-not-pages]]).

**Readings of 2026-08-24, each from its own invocation:** the suite `caught 173, missed 0`, exit 0;
`--list` prints the same figure and **agreed with the run exactly**; the gate exits 0 with one
standing advisory; `--lint` exits 0; the injector reports nothing rewritten and no problems.

**The suite's wall clock that day is not comparable with the previous one and must not be quoted as
a regression** ([[a-control-nothing-touched-separates-a-change-from-the-machine]]).

## The list of the gate's failing conditions on this page is a drifted third copy, and deleting it is owed work

**The owner reads the gate and its suite as two entities and asked for a page each.** The plan he
approved is: run `bash scripts/vault-authority.sh --near` first, then read the family **by hand**,
then split, then **delete** the numbered list of failing conditions above — a drifted copy is
repaired by deleting it, not by correcting it
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**Not done at the ingest of 2026-08-24, and named rather than half-done.** What the reconnaissance
returned, so the next attempt starts from the split: `--near vault-scripts` answers that the slug is
already in the family **the gate**, which holds ten slugs; the suite has a family of its own,
**the selftest of the vault's own scripts**, holding thirteen — **and no entity page.** So the
register already carries the division this page does not.

# Three counts on this page are stale, corrected 2026-08-25 rather than deleted

**Read off `authority.md` on 2026-08-25: the gate's family holds 15 slugs and the family for the
selftest of the vault's own scripts holds 15.** This page says ten and thirteen, and the register's
own note on the second family says thirteen. **Three stale copies of two lists.**

**The numbers above stay where they are, dated to the days they were taken**
([[the-region-coverage-figure-is-dated-where-it-stands]],
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]). The owner's ruling is that the
subject descriptions move to two new pages and the history stays here, so the copies go when the split
happens rather than in passing
([[the-vault-scripts-page-stays-a-hub-and-the-gate-and-its-suite-get-subject-pages]]).

**And the split moves no address.** 79 pages under `wiki/` link to `[[vault-scripts]]`, 107
occurrences, and the ruling keeps this filename and this slug exactly as they are.

# Two scripts joined them and the gate gained a rule — 2026-08-26

**`scripts/vault-measure.py`** — the writer of the vault's `measure` regions and the only thing that
writes a gauge's number, with three modes and five refusals
([[vault-measure-py]]). **`scripts/vault-measure-selftest.py`** — 59 cases in its own throwaway
vault, including one that proves `--check` executes nothing.

**Rule 15 of `scripts/vault-check.sh`** asks its question by running `vault-measure.py --check`,
reads the lines and never the exit code, and notes a missing file
([[the-gate-delegates-by-running-the-writer-it-checks-and-reads-lines-not-exit-codes]]). **The
number is 15 and not 14 even though 14 is due for retirement**, because a retired rule number is
never reused ([[a-retired-rule-number-is-never-reused]]).

**The suite's sandbox copy list gains `vault-measure.py`**, the first Python script on it, and the
coupling is total: an uncopied script reddens all 27 clean cases at once
([[a-gate-rule-that-runs-a-script-is-coupled-to-the-suites-sandbox-copy-list]]).

**Readings taken 2026-08-26, each from its own invocation**: `vault-check-selftest.sh` **caught 178,
missed 0**, exit 0, wall clock not taken; `vault-check.sh` exit 0, `--lint` exit 0, `--rules`
**16 headings**; `vault-measure.py --check` exit 0 over **0 regions**;
`vault-measure-selftest.py` **caught 59, missed 0**; `session-dialogue-selftest.py` **caught 52,
missed 0**, from 32; `hook-selftest.ps1` **caught 148, missed 0**, from 144.

**The gate itself reads about 20.2 s on this machine against the 15.3 s recorded above** — machine
drift, measured with rule 15 removed as well
([[a-control-nothing-touched-separates-a-change-from-the-machine]]).

**`scripts/vault-check.sh` was corrupted and repaired the same day.** A helper round-tripped it
through Python's text mode and destroyed three literal CR bytes inside three awk regexes; `bash -n`
passes on the corrupted file ([[a-file-round-tripped-through-pythons-text-mode-loses-a-literal-carriage-return]]).

**`powershell -NoProfile -File` is the command that runs the PowerShell suites on this machine.**
There is no `pwsh` here — Windows PowerShell 5.1 is the only shell present, and every row above
naming `pwsh` is shorthand for the longer form.

# Two scripts changed on 2026-08-26, in the second session of that day

## `scripts/vault-check.sh` — rule 15's interpreter probe hung the gate and was repaired

**The probe chose the first candidate that *existed* rather than the first that *worked*.** On this
machine `python3` resolves to the Microsoft Store stub, which neither answers nor exits, so the gate
never returned — read as slow, then as contended, then as starved, for an hour
([[python3-on-this-machine-is-the-microsoft-store-stub]],
[[a-trace-answered-in-ninety-seconds-what-an-hour-of-process-archaeology-did-not]]).

**A candidate resolving under `WindowsApps` is now skipped *without being run*.** The guard is a path
test and not a timeout, because a timeout cannot bound a process it cannot signal
([[an-msys-signal-does-not-reach-a-native-windows-process]],
[[an-interpreter-probe-must-choose-what-works-rather-than-what-exists]]).

**Readings after the repair: 21.5 s, exit 0, `VAULT-CHECK: ok` on a 682-file corpus**, and 20.45 s
after the last edit of that session. The recorded cost of rule 15 alone on this machine was 20.2 s,
so 21.5 s is the norm rather than a remainder. `bash -n scripts/vault-check.sh` clean. **The order of
candidates is unchanged and behaviour on a machine without the stub is identical.**

**The repair has no selftest case**, and the suite that would carry it now runs once a sprint
([[a-defect-one-day-old-outlived-the-selftest-that-shipped-with-it]],
[[the-suite-stops-running-every-session]]).

## `scripts/lessons-queue.py` — it reads three folders and reports two populations

**It scans `decisions/` as a citer as well**, and prints **`CITED`** — the loop's end state — beside
**`LANDED`**, which counts a `rules/` page or a proposal carrying `status: implemented`
([[the-lessons-queue-counter-prints-cited-and-landed-apart]]).

**Measured 2026-08-26 after the edit:** lessons 165; cited by rule 22, by proposal 55, by decision
120; `CITED` 128, `LANDED` 27, **queue 37 against 100 before**. No lesson was touched.

**Its printed block now carries its own blind spot in prose**: it never scans `archive/`, so an
implemented proposal moving out drops `LANDED` and raises the queue with nothing having gone
backwards.

**Its docstring title and the collector's brief still describe the population it no longer
measures**, and rewriting them is an S3 line.

## Four selftests, and only one of them is expensive

`vault-check-selftest.sh` builds one sandbox root and one pristine copy of the corpus, then gives
**each** of its ~178 cases its own working copy of that baseline and runs the gate inside it, through
a worker pool. **The other three copy no corpus per case** — which is why 148 hook cases cost 2m17s
and 178 gate cases cost an hour. **The difference is structural rather than a matter of case count**,
and it is what the smoke runner's composition is built on
([[the-smoke-runner-is-built-first-thing-next-session]]).

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md` and `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*

# What changed on 2026-08-28

**`scripts/vault-check.sh` changed in one verdict.** The `retired` verdict now fires on
`status: archived` as well as on `deprecated`, and carries the value it found in its detail field, so
one message names whichever mark it met and sends the reader to the right repair
([[a-status-value-is-either-an-address-or-a-stage-and-the-gate-treats-them-oppositely]]).

**`scripts/vault-check-selftest.sh` gained three cases and one fixture planter** — `archived` in
`wiki/lessons/` red, `processed` in `wiki/entities/` red through `badvalue`, and `processed` in
`wiki/decisions/` producing no verdict at all, which is the case that asserts silence.

**And its `--only` flag is a substring glob rather than a regular expression**, so a narrow run that
selects nothing prints `caught 1, missed 0 - FILTERED` and reads as a pass
([[a-narrow-suite-run-that-matches-no-case-still-prints-a-catch]]).

**Nothing was taken out of service.**

# What changed on 2026-08-29, and four scripts moved

**`scripts/vault-archive.sh` gained `--sweep`**, and it is the largest change of the day. It is kept
on that script's own page rather than here ([[vault-archive-sh]]).

**`scripts/vault-check.sh` gained the deprecated-link advisory**, behind `--lint`: one line per
retired page that a live `wiki/` page still links to. First reading after the sweep — **43 dead
targets, 3 of them named in a `decided_by:` field**. A bare gate run is unchanged at **23.6 s** and
`--lint` costs **28.6 s**, so the advisory itself is about **five seconds**
([[the-deprecated-link-advisory-prints-one-line-per-dead-target]],
[[a-link-pass-that-keeps-the-filename-beside-the-link-is-linear]]).

**It keys on the literal value `deprecated`, never on "the target's status"** — a phrasing about the
status in general would have grown from 43 lines to hundreds the day the sweep ran, because about 240
pages in `archive/` now carry `status: archived`
([[the-deprecated-link-advisory-keys-on-the-literal-value-and-not-on-the-targets-status]]).

**And it lost a defect.** Two advisories — the quote advisory and the `decided_by:` shortfall —
printed the word `advisory:` on their continuation lines, so `grep -c 'advisory:'`, which the brief
reports as the count of advisories, read **54 where the true count is 30**
([[an-advisory-word-on-a-continuation-line-inflates-the-count-the-brief-reports]]).

**`scripts/vault-check-selftest.sh` gained five things**: sections in `--list`, section matching in
`--only`, an exit-2 refusal for a selection that matches nothing, a `BASELINE` record kind, and the
count case its own header has promised since 2026-08-24. Its three source sweeps became functions,
because they now have two callers.

- **An unmatched `--only` substring refuses with exit 2 before the sandbox is built**, which is what
  stops a typo reading as a pass.
- **`--only` matches a section name as well as a case name**, and the section is derived from where
  the case sits rather than from a second list
  ([[a-suite-section-is-derived-from-where-a-case-sits]]).
- **The baseline copy left the `pass` tally.** Taking it out shifts every published suite count in
  this corpus by one — `caught 133, 141, 148, 156` and `194` across at least six pages. The change is
  corpus-wide and silent, and it does not mean any of those readings was wrong when it was taken.
- **`--list` had overcounted its inline cases by one since it was built**, because the comment
  explaining the sweep quotes the literal the sweep looks for
  ([[a-comment-quoting-the-literal-a-sweep-looks-for-is-counted-by-that-sweep]]). It reports **181**
  cases where it reported 182.
- **The count case fired for the first time and agrees at 194.**

**Whole and unfiltered, the suite reads `caught 194, missed 0, exit 0` in 29m12s** on 2026-08-29,
against 34m08s at 178 cases on 2026-08-24. Sixteen more cases and five fewer minutes, after the sweep
took `wiki/` from 762 pages to 523. It is **not** a controlled experiment — three readings on three
days under different machine load — but it is the only evidence there is that archiving moved the term
that grows.

**`scripts/vault-authority.sh --check` changed what "stale" means.** A register row is stale only when
**no page in `wiki/` or `archive/`** carries the slug; the other direction still asks about `wiki/`
alone ([[a-register-row-is-stale-only-when-no-page-anywhere-carries-the-slug]]). It agreed with the
tree at **507 slugs** after the sweep.

**`scripts/hook-selftest.ps1` grew from 194 cases at 55 s to 3m15s**, and **the journal gives its new
case count three different ways** — `caught 217` in its checks list, `caught 210` in one `measure:`
line and `204` in another. The three are copied here as they stand rather than reconciled: `raw/` is
immutable, the run is not repeatable from the vault, and the figure a reader needs is the wall clock,
which all three agree on. Ten cases came from the `--only` contract and six from the feedback hook's
new ritual half; almost the whole wall clock is the one `--only` case that lets a suite run proceed
and therefore pays for a sandbox copy and two gate runs
([[the-only-cases-live-in-the-hook-suite-and-the-expensive-pair-is-kept]]).

**Nothing was taken out of service.**

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# Gauge: an ingest's cost tracks tool calls, not file sizes — 2026-08-29

**Across the five recorded `/ingest` runs carrying both figures, tokens per tool call sit between 1,552
and 2,170 — a factor of 1.4 — while the totals span a factor of 1.8 and the call counts a factor of
2.4.**

**What it means:** the spend is the accumulated context re-sent at every tool call, rather than any
single large read. **What it does not mean:** that the relation is linear — **two of the five points
invert**, and nobody can quote a net.

**That is the argument for moving reading into an isolated context**, and it is also why the rewiring's
benefit cannot be quoted: the reading agents' cost is measurable and the librarian's saving is not
([[the-ingest-rewired-so-the-librarian-dispatches-and-returns-once]],
[[the-verdict-and-the-pen-are-held-by-different-parties]]).

**One earlier attempt to net the two was wrong in a way worth naming**: it summed an isolated
subagent's budget into the librarian's and never subtracted what the librarian would stop reading. The
three figures were each recorded verbatim; **the addition was the error**
([[a-subagent-cannot-report-its-own-cost]]).

## `log.md` against the other registers, read the same day

**`log.md` is 972,717 bytes over 10,464 lines and is 69% of the registers by size** — `tags.md`
168,935, `sprint.md` 136,330, `authority.md` 89,193, `index.md` 33,578. **Split at the S3 boundary:
503,239 bytes before 2026-08-23 and 469,478 after**, over seven days; one day's section alone is 33,038.

**A sprint-close rotation halves the file and a per-session one would leave 33–67k.** It does **not**
mean either saves tokens, which depends on how much of it is read — and nothing measures that
([[log-md-is-filled-mechanically-and-rotates-when-the-sprint-closes]]).

# `scripts/vault-check.sh` gained rules 16 and 17 on 2026-08-30

**Rule 16 judges body sections and dated frontmatter keys per folder**, reading both from that
folder's `_schema.yaml` — `sections:`, `lifecycle_from:` and `required_from:`. It **compares the set,
never the sequence**, and reads `# ` rather than `## ` because that is what `wiki/` writes: 900
first-level headings against 395 second-level ones in `decisions/` alone. **The `sections()` helper
gained a heading level as an argument**, so rule 8 goes on reading `## ` for journals — one helper,
two callers, no second list.

**Rule 17 is the handshake**, scoped to targets in `proposals/` and `rules/` because `decided_by:` is
legal nowhere else ([[a-decision-declares-its-target-and-the-handshake-closes-it]]).

**The `retired` verdict learned a third mark, `repealed`, with a message of its own** — because naming
the wrong one sends a reader to write a `superseded_by:` that the archiver would refuse.

**Cost and state, each from its own invocation on 2026-08-30**: the gate at **exit 0, 21.3 s**,
against 19.4 s before the two new rules, with the region advisory unchanged at `11 of 17`.
`vault-check-selftest.sh` at **caught 204, missed 0**, against 194 at its last whole reading — ten
cases added that day, seven for the lifecycle in the gate and three for the archiver's repeal
preconditions. `hook-selftest.ps1` at **caught 218, missed 0**, up from 217. `make style` clean at 88
files.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`, extended 2026-08-30.)*

# The catalogue stops printing the archive — 2026-08-30, later the same day

**`bash scripts/vault-catalogue.sh` printed 201,927 bytes over 975 lines and now prints 131,604.**
The `## archive` section was **70,323** of them, about 17,500 tokens, **paid on every dispatch and
discarded by instruction** — `.claude/agents/pre-task.md:116` told its reader to throw it away.

**Removing it brings the script into agreement with what two files already claimed about it.**
`index.md:9` and `job_hunt_ai_vault/CLAUDE.md:45` both say it prints the same list as `pages.base`,
and `pages.base` filters `wiki/` and holds no archive at all. **The script was the one that
disagreed.**

**It prints the six live folders and nothing else.** Whether the script survives at all is now an
open question the owner raised and nobody answered: if `/pre-task` phase 1 goes when `decisions/`
empties, the catalogue goes with it, and nothing decides that
([[the-prohibition-families-become-rule-pages-served-by-a-hook]]).

# The apostrophe hazard came back, an hour before the overflow — 2026-08-30

**A comment containing an apostrophe inside the awk program closed its single-quoted shell string and
broke the gate with a syntax error.** One apostrophe ends the quote and the next backtick becomes a
command substitution. **Loud, and fixed in minutes** — unlike the overflow that came out of the same
comment block an hour later.

**This is the fourth recorded instance of that hazard in this repository** and the first since the
page recording the previous three left for `archive/` — it sits at
`archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/pages/an-apostrophe-in-an-awk-comment-ends-the-shell-quote.md`
and its own closing line is that *"a defence that has failed three times while its own page was in
front of the party failing it is not a defence"*. **The warning is now written into the file itself**,
beside the quotes, which is where the party about to fail it is looking.

**Both faults came from one comment block, an hour apart, and both are removed by the same repair**:
the program leaves the shell string for `awk -f`, ratified and deferred
([[the-awk-program-moves-into-a-file-of-its-own]], [[the-gate-can-stop-checking-and-go-on-exiting-zero]]).

# The readings after all of it, each from its own invocation on `2be376b`

**`bash scripts/vault-check.sh` — exit 0 and an empty stderr**, which is now a case in the suite
rather than an observation. **`bash scripts/vault-check-selftest.sh` — caught 212, missed 0**, against
204 at the last whole reading. **`powershell -NoProfile -File scripts/hook-selftest.ps1` — caught 224,
missed 0**, against 218, and it must be given `< /dev/null` if it is not run in the foreground
([[backgrounding-a-task-that-reads-standard-input-is-what-hangs-it]]). **`make style` clean at 88
files. `make smoke` SMOKE-EXIT: 0** in the foreground. `make test` was not run and no Python changed.

**An intermediate reading of `caught 210, missed 2` is kept rather than dropped**: both failures were
this session's own regressions in other cases' fixtures, both were repaired and verified by name, and
the whole suite was then re-run — because `--only` is not a reading of the set
([[a-narrow-suite-run-that-matches-no-case-still-prints-a-catch]]).

**Both regressions are worth naming because neither was visible from reading the assertions.** One
case had pinned its fixture to the end of `wiki/decisions/_schema.yaml` and stopped testing its
subject the moment a block was added below it
([[a-fixture-pinned-to-the-end-of-a-file-expires-when-a-block-is-appended-below-it]]); the other broke
because a section was made obligatory without grepping the suite for the fixtures carrying the value
it was scoped to ([[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]]).
**The suite is the only reader that would have caught either, and it caught them by accident** — one
reported the wrong reason and was called a miss only because the message did not match.

# Two generators joined the folder, and the folder joined a target — 2026-08-31

**`scripts/build-families-table.py` is new.** It regenerates `docs/vault-cleanup-families.md` in English
from `job_hunt_ai_vault/authority.md`, the frontmatter of every live page, and the hand-written verdicts
in `docs/vault-cleanup-verdicts.md`, **which it reads rather than overwrites**. The generator it
replaces existed only in another session's temp directory, was in no commit, and destroyed any verdict
written by hand — so the table was unregenerable the moment somebody filled a column in.

**`scripts/build-family-rules.py` is new.** It drafts one `wiki/rules/` page per vault-facing family and
**refuses outright to write a title carrying a measurable quantity**, which is the no-quantity rule
enforced at the point of authorship rather than by the gate afterwards. It must be run **inside** the
librarian's dispatch, because both orders of the family-rule act redden the gate
([[the-family-rules-are-drafted-by-a-generator-inside-the-librarians-dispatch]]).

**The whole folder is linted now.** `make style` widened to `ruff check src tests scripts`, and the ten
findings it had never been able to see were fixed first
([[scripts-joins-make-style-and-only-the-check-half]]).

**`scripts/session-dialogue-selftest.py` and `scripts/vault-measure-selftest.py` still report
`caught 52` and `caught 59`, `missed 0`** after those repairs.

## The catalogue's archive blind spot has a consequence now, and it did not before

**The section above records `vault-catalogue.sh` dropping `archive/` on 2026-08-30.** On that day it
cost nothing worth naming. **On 2026-08-31 it costs 129 decisions.** They moved into
`archive/2026-08-31/2026-08-31-the-families-become-rules/pages/`, so `/pre-task` phase 1 cannot see
them, and the obliges-and-rejected half of each sits one wikilink deeper than any instruction sends a
reader — a family rule's clause is a title.

**The consequence is that `/pre-task` starts answering with claims rather than with what a decision
obliges**, and it belongs to the `/pre-task` rework rather than to the catalogue
([[pre-task-reads-too-much-and-the-rework-belongs-to-vault-ask]]).

## A reading of `--sweep` that no page had

**`bash scripts/vault-archive.sh --sweep` selects about 57 of 293 discharged prohibitions**, because its
`decisions/` arm takes slugs named in some page's `decided_by:` and a rule page names exactly one. The
129 were moved by named batches after a `--dry-run`, which collects refusals and moves nothing
([[a-selector-written-for-one-discharge-shape-cannot-see-a-new-one]]).

*(Extended 2026-08-30 from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`, and again at the ingest of `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
