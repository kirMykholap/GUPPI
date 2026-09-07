---
name: vault-lint
description: Audit the vault for contradictions, orphans, broken links and tag drift. Run once per sprint, at the retrospective.
---

# Lint the vault

First run the mechanical checks. `$VAULT` is the top-level directory holding a `wiki/`; the scripts
find it themselves.

```bash
VAULT=$(ls -d */wiki 2>/dev/null | head -1 | sed 's|/wiki$||')
bash scripts/vault-check.sh --lint
for src in "$VAULT"/raw/*/*.md; do
  bash scripts/vault-coverage.sh "$src"
done
```

`--lint` is not decoration and this is the only caller that passes it. The tag-density advisories
print **only** under that flag: they are a statistic about the whole corpus, they can never fail a
run, and the decision they feed — split a tag or leave it — is made here, once a sprint, and
nowhere else. On every other run they printed twenty lines nobody could act on and buried the one
advisory that *was* about that run. The flag adds lines and never removes a check; the exit code is
identical either way, and a selftest case holds that.

So this is the run where the density lines get read. If you skip the flag you will not see them,
and the audit below will be missing its input rather than finding nothing wrong.

There is no exception in that loop any more. It used to skip `*/TEMPLATE.md`, because the handoff
template lived in `raw/` and is a form rather than a source; the template moved to
`.claude/templates/` on 2026-08-17 and `raw/` is an inbox now, so the exception guarded nothing and
would have gone on guarding nothing. **An exception written by filename outlives what it excepted**,
which is the same defect that was taken out of rule 8 of the check the same day. Note also that the
migrated 2026-08-12 document carries no frontmatter at all, so it cannot be filtered by a field
either - every file in `raw/` is a source and gets a coverage report.

The `VAULT=` line is not decoration: the loop is yours, not the scripts', and without it the
glob expands to `/raw/handoffs/*.md` and every coverage call reports "no such file" — which
reads exactly like nothing being wrong.

Everything they report is a defect in the vault, never in the check. Fix the pages. A raw document
with unverdicted units is an **unfinished ingest** — finish it before anything else in the audit,
because every later check is being run against an incomplete corpus.

## Count the vault's CRLF files

```bash
VAULT=$(ls -d */wiki 2>/dev/null | head -1 | sed 's|/wiki$||')
git ls-files "$VAULT" | while read -r f; do
  n=$(tr -dc '\r' < "$f" | wc -c)
  [ "$n" -gt 0 ] && printf '%6d CR  %s\n' "$n" "$f"
done
```

**The instrument is `tr -dc '\r' | wc -c`, and never `grep -c $'\r'`.** In the shell used here that
escape collapses to an **empty pattern**, an empty pattern matches every line, and `-c` counts
matching lines — so it returns the file's line count, always. It was used in this repository to
contradict a subagent's correct claim, reporting 232, 59 and 57 against three files of exactly 232,
59 and 57 lines, and it survived being read because a plausible non-zero number that happens to be a
true fact about the file passes a sanity check every time. A second session walked into it again
four days later.

**It prints nothing for about a minute** — 56 s over 682 files, measured 2026-08-26 — because it
spawns `tr` per file. That is a silent loop, not a hung one, and it runs once a sprint.

**What the number means.** `.gitattributes` pins `*.md text eol=lf`, so the committed blob is
already LF and only the **working copy** drifts. `git status` is silent about it, which is why
nothing else here would ever report it. Each printed line is one file that is CRLF on disk; how many
lines print is the count.

**No figure is written into this file.** Between 2026-08-22 and 2026-08-26 the recorded population
went eight, then five, then two, and three of those files renormalised themselves with nothing
deciding it and nothing observing it. A number in prose goes false without saying so; this step
exists so the number is taken rather than remembered.

## Drain the lessons queue — and this dispatch runs FIRST

**Before the audit, not after, and the order is forced rather than chosen.** This dispatch **writes**
`proposals/` pages, and an audit is scheduled after the last write of the thing it audits: a run
that audits and then writes has not audited what it shipped. See
`<vault>/wiki/decisions/the-audit-is-dispatched-after-the-writes.md`.

First take the queue, which is arithmetic and not judgement:

```bash
uv run python scripts/lessons-queue.py
uv run python scripts/lessons-queue.py --slugs
```

**Why this exists.** `lessons/` is a store nothing empties, and the queue is what nothing anywhere
cites — not a rule, not a proposal, **and not a decision**. That membership was widened by the owner
on 2026-08-26; the narrower definition this paragraph used to carry, and the figures it quoted with
it, described a population the script no longer measures. **The count is printed by the run above and
is deliberately not written here.**

Seven pages of the queue are one failure — a tool eating what was written — accumulated between 17
and 23 August, and there is no rule about it. **The same class fired five more times in the session
that built this step.**

**Why no existing mechanism finds it.** `--near` matches on WORDS, and those seven pages share none:
*apostrophe*, *heredoc*, *sed*, *grep*, *backslash*, *TMPDIR*, *CR*. The family is conceptual. It
shows in the register: **every lesson carries an `authority:` value of its own and not one family has
ever held two.** And the librarian cannot see it from where it normally stands — it writes a lesson at an
ingest, one at a time, inside the context of the session that produced it, where the seventh looks
exactly like the first. **It did not miss seven times; it stood seven times where the repetition is
invisible.** A fresh dispatch reading the whole queue with one question has no session context at
all, which is why the fix is the position and not the agent.

Dispatch `vault-librarian` (Agent tool, `subagent_type: "vault-librarian"`) with:

> Read every lesson in the queue above and group them into families — pages recording the same
> underlying failure, whatever words they use.
>
> 1. **The question is not "should this be a rule".** It is: **what form of fix would have prevented
>    all N of these?** The answer may be a rule, a gate verdict, a selftest case, a change of tool,
>    or nothing.
> 2. **A proposal must name a mechanical check.** Where no check can exist, write no proposal — the
>    lesson stays a lesson. *"Be careful with quoting"* is unverifiable and is not written;
>    *"file content is written with the Write tool, never through a heredoc"* is checkable and would
>    have prevented all seven.
> 3. **Name every member of a family, by slug.** Grouping is a judgement and a judgement can be
>    wrong; the owner must be able to see seven slugs and decide for himself whether they are one
>    thing. A proposal against a phantom family is the failure mode of this whole step.
> 4. **Run `bash scripts/vault-authority.sh --near <slug>` before writing any page**, and obey
>    `no-new-entity-where-an-existing-one-can-carry-the-claim`. This dispatch is the likeliest place
>    in the whole ritual to write a proposal that already exists.
> 5. **Report four numbers: read, families found, proposals written, rejected as singletons.** A run
>    that found nothing must be distinguishable from a run that did not happen — see
>    `an-instrument-that-fails-towards-nothing-to-do`. "Nothing found" without the counts is not a
>    result.
> 6. **No threshold is set for a family's size.** Report the size and, where the lessons record it,
>    what each occurrence cost. Whether a family of two is worth a rule is the owner's call and not
>    a number's.
>
> Append a `lint` entry to `log.md` naming the four numbers and each family you wrote a proposal for.

**The proposals reach the owner through the brief and he decides.** Writing one is not acting on it.

**And this step may propose changes to itself.** Its own misfires become lessons, and it reads
lessons. That is fine while the output is a proposal to the owner and never a self-edit — it is the
one place in this system where the loop closes on itself, which is why the limit is written here
rather than assumed.

## Then the sweep — after the lessons dispatch and before the audit

```bash
bash scripts/vault-archive.sh --dry-run --sweep <date> <session-slug>   # read the list first
bash scripts/vault-archive.sh --sweep <date> <session-slug>
```

**It walks `decisions/`, `lessons/`, `proposals/` and `rules/`, applies each folder's criterion,
writes `status: archived`, moves the page into `archive/<date>/<session>/pages/` and rewrites every
`sources:` citation of it.** `entities/` and `concepts/` have no criterion and are not walked.

**It runs here and not earlier, and the reason is the criterion rather than the audit.** The lessons
dispatch above writes `proposals/` pages, and a new proposal citing a lesson **changes what the
lessons criterion selects** — a sweep before it would archive a lesson the run was about to give a
citer. The audit-after-the-writes rule points the same way and is the weaker of the two arguments.

**The date and the session are arguments and are never derived**: a derived date is a date nobody
chose. **Read the dry run before the real one** — the first sweep of a corpus is a third of `wiki/`
moving at once, and nothing else in this system shows you that list.

**It continues past a page it may not move**, collects those refusals, prints them **before** it runs
the gate, appends one line to `log.md`, and exits non-zero when anything was refused or the gate is
red. A refusal is a page that is not ready to leave, not a failed run: read the list and decide.

## Then the audit

Dispatch `vault-librarian` (Agent tool, `subagent_type: "vault-librarian"`) with:

> Audit the vault. Report, do not fix, except where the fix is unambiguous.
>
> 1. **Contradictions the greps cannot see** — two pages that disagree in substance while
>    claiming different `authority` values, or none. Mark both with a
>    `> [!CAUTION] CONTRADICTION` block; do not choose a winner.
>    A page already carrying `> [!NOTE] CONTRADICTION — RESOLVED <date> BY THE OWNER` is
>    **settled and is not a finding.** That block quotes the caution it replaced, on purpose: a
>    resolved contradiction is still a thing that happened. Do not re-mark it and do not remove it.
> 2. **Stale `status: current`** — pages describing something the code no longer does. Check
>    against `src/` where the page's `basis` is `code`; a `code` page loses to the code itself.
> 3. **Pages missing** — subjects referenced repeatedly across pages with no page of their own.
>    **Name the folder each one belongs in before calling it a missing concept.** The wiki has
>    five, and the fifth is the trap: a subject that was *designed and never built* is a
>    `proposals/` page, not a `concepts/` one, and what separates them is whether the thing
>    exists. See `<vault>/wiki/decisions/proposals-are-a-folder-not-a-status.md`.
> 4. **Tag drift** — two tags whose definitions have converged (merge, one becomes the other's
>    alias), and tags whose definition no longer matches how they are used.
> 5. **Index drift** — does `index.md` still name the categories, the naming rule, the current
>    sprint and the hub pages, and nothing else? It is a map, and its failure mode is becoming a
>    catalogue one useful row at a time.
> 6. **The brief's growth** — read the `measure` entries in `log.md` and report the trend.
>
> Append the findings to `log.md` as a `lint` entry.
