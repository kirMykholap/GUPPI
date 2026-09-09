---
title: "A cut to the repository's `CLAUDE.md` can lose an assertion but cannot strand a page"
type: concept
status: current
authority: claude-md-reachability
basis: code
sprint: S1
created: 2026-08-16
sources: ["archive/2026-08-16/2026-08-16-the-structure-questioned/handoffs/2026-08-16-the-structure-questioned.md", "scripts/vault-check.sh", "CLAUDE.md"]
tags: [vault, process]
---

# Three facts from the code, and what they bound

1. **Rule 5b of `vault-check.sh` validates every `[[wikilink]]` in the repository's `CLAUDE.md`**,
   and it has a selftest case ([[vault-scripts]]).
2. **`claude-md-scope` removed every wikilink from that file**
   ([[claude-md-is-a-map-and-four-rules]]), so the rule currently guards nothing.
3. **Those links deliberately do not count towards reachability.** A page reached only from
   `CLAUDE.md` is already an orphan and already fails the orphan rule.

Together they bound the damage precisely: **deleting a paragraph from `CLAUDE.md` cannot strand a
page.** Nothing can hang off that file alone.

## What a cut can lose is an assertion no page carries

That is the residue, and **it is what every observed staleness here has been.** The two successive
shrinks of the file each dropped exactly one statement no page held, and both times a human found
it by reading the removed text beside the page that was meant to carry it — which is acceptance
criterion 4 of S1, and why [[the-paragraph-was-deleted-on-purpose]] reframed the question as *what
tells a loss from a deletion*.

## The failure has a shape, and the shape is that no rule reads a `CLAUDE.md`

Four instances are now on record, and the last two arrived on 2026-08-16:

| # | The stale claim | How it was found |
|---|---|---|
| 1–2 | the two shrinks, one lost statement each | a human reading the removed text |
| 3 | the vault's `CLAUDE.md` describes `archive/` as holding the handoffs of closed sprints; they never move there | `log.md`, during an ingest |
| 4 | the vault's `CLAUDE.md` schema still lists four types, while the same file documents `proposals/` in three other places | reading it to look up what a `title:` asserts |
| 5 | the repository's `CLAUDE.md` named `.claude/agents/vault-librarian.md` after the owner moved the file, and was false within the hour | reading, again — nothing reported it |

**A `CLAUDE.md` is not a wiki page.** No rule reads one, no check compares it against the decisions
it contradicts, and every instance above was found by a human's eye. That is the same gap as S1
criterion 4, and the proposed answer — *it may point and may not assert* — is
[[claude-md-may-point-and-may-not-assert]], with the owner's own direction for the repository's
file in [[the-repository-claude-md-becomes-a-dispatch-table]].

Instance 4 is the vault's own schema and is **not fixed by this page**: the librarian does not
write the store's rulebook, and the correction is logged as a miss instead.

## Instances 6 and 7, 2026-08-16 — and one of them is not a `CLAUDE.md` at all

| # | The stale claim | How it was found |
|---|---|---|
| 6 | `.claude/skills/ingest/SKILL.md` line 9 says *"one source at a time — never batch several handoffs"*, while [[ingest-is-batched-at-the-retrospective]], decided the same day, says the opposite. The skill's last commit, `f7f654e`, predates the decision | reading the skill beside the decision while measuring how `/ingest` would have to change |
| 7 | the vault's own `CLAUDE.md` documents the contradiction check as `rg "^authority:" wiki -o \| sort \| uniq -d`, which never compares slugs — [[a-command-that-is-false-only-in-its-documentation-fails-nothing]] | reading it to explain the field to the owner |

**Instance 6 widens the class beyond this page's title.** It is the first divergence found between a
**skill** and a **decision** rather than inside a `CLAUDE.md`, and the general statement is
therefore *no rule reads any harness file against the vault* —
[[no-rule-reads-a-harness-file]], which carries the running total.

*(The prose above the first table says "Four instances are now on record" and the table beneath it
already listed five rows. That was found on 2026-08-16 and reported as a miss; it is the same
failure the corpus names as [[a-stated-count-drifts-from-the-list-it-heads]]. The count is left
where it stands and **re-derived from the tables** instead: five rows there, two here.)*

**The answer is now designed rather than only proposed:**
[[the-harness-is-compiled-not-maintained]] makes the harness a build product, and
[[marked-regions-and-the-prose-outside-them]] is the part aimed at the residue this page names —
hand-written prose asserting something no page carries. **A gate over it guarantees agreement and
not truth** ([[a-gate-guarantees-agreement-never-truth]]).

## Row 6 now cites an archived page — annotated 2026-08-17

[[ingest-is-batched-at-the-retrospective]] is `deprecated` and lives in `archive/` since
2026-08-17; its successor is [[ingest-runs-after-handoff-at-the-end-of-a-session]]. **The row is
left as written** — it records a divergence that was real when it was found — but the claim it rests
on has narrowed: the skill's *"one source at a time"* is right about **compilation** and was only
ever wrong about **dispatch**.

The link resolves, so nothing failed, which is precisely
[[a-live-page-can-argue-from-a-deprecated-one]] — this time caused by a supersession rather than
found in one.

## Rows 8 and 9, found 2026-08-17 while deleting the block that carried them

The register stood at seven. **Both new rows come out of the same block — `## Where things are` in the
repository's `CLAUDE.md`** — and both were found by reading it against the tree in order to justify
deleting it ([[where-things-are-is-deleted-now-and-generated-later]]).

| # | The stale claim | How it was found |
|---|---|---|
| 8 | `.claude/` is listed as `skills/`, `agents/`, `hooks/`, `settings.json` — **`templates/` omitted**, though the forms moved there the previous day | reading the block beside `ls .claude/` before deleting it |
| 9 | the same block closes *"its directory name is the owner's to change and nothing may depend on it"*, which **contradicts [[governs-is-a-path-from-the-repository-root]]** — decided the day before, and it fixes the vault's directory name inside `governs:` | the same reading |

**Row 9 is the sharper of the two**, and it is a new species for this register: not a claim that went
stale, but a claim that was **contradicted by a decision taken elsewhere in the same store**, one day
apart, with nothing comparing the two ([[no-rule-reads-a-harness-file]]).

**Two other defects of the same block were already recorded** — the tooling list two scripts behind, and
the vault line omitting `wiki/rules/`, `pages.base` and `archive/` — so the block carried four at
deletion.

**The repair was deletion, and the answer this page has been waiting for is half-built.** The rules of
that file now render from pages and reddening is mechanical for them
([[wiki-rules-holds-the-rules-of-the-repository-claude-md]]); **the prose outside every region is still
allowed and unchecked**, which is where all nine of these rows lived
([[marked-regions-and-the-prose-outside-them]], [[the-repository-claude-md-after-the-rules-left-it]]).
