---
title: "The governed denominator may grow for reasons other than a skill being added, and the criterion that every governed file carries a region does not move because of it"
type: decision
status: deprecated
authority: coverage-denominator-reading
superseded_by: "[[the-region-coverage-instruction-carries-no-count-and-reports-the-unmarked-files-as-unchanged]]"
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-18
created: 2026-08-18
sources: ["archive/2026-08-18/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind/handoffs/2026-08-18-the-marker-carries-its-type-and-the-gate-was-blind.md", "sprint.md"]
tags: [harness, vault, process]
---

# Decided by the owner on 2026-08-18: yes, and it is reported one way only

**The governed set is swept, never listed** — both `CLAUDE.md` files and every `*.md` under
`.claude/` ([[the-governed-set-is-swept-and-markdown-by-property]]). So the denominator of the
region-coverage advisory grows whenever a governed markdown file appears, and that is not only a
skill being added: `.claude/rules/` landing would add files by construction
([[moving-a-rule-into-claude-rules-with-a-paths-scope]]).

**S2's criterion 6 does not move because of it.** The criterion asks *does every governed file carry
a marked region*, and the owner has read it on the files twice
([[a-sprint-closes-on-its-goal]]).

*(The title read "The governed denominator may grow for reasons other than a skill being added, and
criterion 6 does not move because of it" until 2026-08-18, and the sentence above is where the
number is now resolved. **6 was never a count**: it is the identifier of one of S2's acceptance
criteria in `sprint.md`, and a seventh criterion would not make this page stale. That reasoning
stood in a `quantity:` line until the field was rejected and the rule made unconditional over
titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), which withdrew the only way
a page had to declare itself exempt — **a number that is genuinely an address still leaves the
title**. A code span around the number was rejected as a dodge for exactly this shape, because this
corpus writes such numbers in plain prose, so the title names the criterion by what it requires
instead ([[a-title-names-what-is-counted-instead-of-counting-it]]). Not a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

## How the number is reported, and how it is not

> **owner: report it as *the twelve unmarked files are unchanged*, never as *coverage improved*.**

**He has twice read that criterion as a file count**, and a fraction whose denominator moved reads
as progress in the numerator when nothing was marked up. The unmarked files are the quantity the
criterion is about; the fraction is the instrument's phrasing, not the criterion's.

## What this does not authorise

**It is not a licence to patch the figure wherever it appears.** Seven `current` pages plus
`index.md` carry `1 of 13` or `0 of 13`, and the repair for a drifting copy is to date it or delete
it, never to correct seven copies into a new number
([[the-region-coverage-figure-is-dated-where-it-stands]],
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# The numerator moved without a file gaining a region, which this page did not anticipate — 2026-08-20

**The reading is `a region or whole generation covers 2 of 15`.** The numerator went from one to two
**because the criterion was reworded, not because any file gained a region**
([[the-criterion-on-governed-files-is-reworded-to-admit-full-generation]]).

**Proved both ways in the real tree**: the generated marker stripped gives `1 of 15`, restored gives
`2 of 15` ([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

**So this page's rule needs its mirror stated.** It says a moved *denominator* must not be reported
as progress. **A moved numerator is the same failure from the other side**: the files that carried no
region that morning still carry none — thirteen of them — and coverage did not improve.

**The owner's phrasing extends without amendment**: report it as *the thirteen unmarked files are
unchanged*, never as *coverage improved*. What is new is only that the sentence now has to survive a
numerator that moved for a reason unrelated to markup.

**And this page still does not authorise patching the figure wherever it appears**
([[the-region-coverage-figure-is-dated-where-it-stands]]).

# The denominator grew again, this time by a file the vault itself generated — 2026-08-20, third ingest

**The reading is `a region or whole generation covers 3 of 15`**, read from
`bash scripts/vault-check.sh`. The file that arrived is `.claude/hooks/messages/pre-task.md`,
generated whole from [[a-pre-task-runs-between-the-plan-and-its-approval]], and it is marked from
the moment it exists — **so the numerator and the denominator moved together, by construction**.

**This is the growth this page predicted, from a new direction.** It named `.claude/rules/` landing
as growth *by construction*; a rule delivered by a hook message adds a governed file the same way,
and neither growth says anything about the twelve files that carry no region.

**The required phrasing, and it is the owner's:** *the unmarked files are unchanged* — never
*coverage improved*.

**The count of them is where the corpus and the journal disagree, and it is left as a disagreement.**
The advisory names **twelve** unmarked files at this ingest, and the journal's `Harness` section
says to report *the thirteen unmarked files are unchanged*. The section above this one records
`2 of 15` where the journal of the same day records `2 of 14`. **The reading is the command, not any
of these sentences** ([[the-region-coverage-figure-is-dated-where-it-stands]]) — and no verdict on
criterion 6 is read off here, which is the owner's ([[a-sprint-closes-on-its-goal]]).

# The denominator also **falls**, and this page was written for growth only — reported 2026-08-20

**It fell by one and rose by one for unrelated reasons, and the record skips the trip.** The corpus
carries `2 of 15` from the second session of 2026-08-20; that session's own first gate run measured
`2 of 14`. The drop has a cause already on the record — `vault-archive.sh` moved the probe
scaffolding out of the working set ([[vault-archive-sh]],
[[the-probe-scaffolding-is-archived-whole-into-specs]]) — and the rise is the generated pre-task
message arriving ([[a-pre-task-runs-between-the-plan-and-its-approval]]).

**A reader comparing `2 of 15` with `3 of 15` sees a numerator moving inside a stable denominator,
which is not what happened.** That is the same misreading this page exists to prevent, met from the
direction it does not cover: it is written *for growth*, and says the number is reported as *the
unmarked files are unchanged* rather than as *coverage improved*.

**The required phrasing is unaffected and neither figure is patched.** Both readings are dated where
they stand ([[the-region-coverage-figure-is-dated-where-it-stands]]). What is added here is that
**the denominator moves in both directions**, so the sentence to reach for is about the files that
carry no region and never about the fraction.

# The denominator moved in both directions and came back to where it was — 2026-08-22

**The reading is `a region or whole generation covers 7 of 15`**, from `bash scripts/vault-check.sh`,
against `6 of 15` the same morning.

**The unmarked files are unchanged, and there is one fewer of them: eight, not nine.** That is the
required phrasing and it is the owner's; **never *coverage improved***. No file that carried no
region gained one.

**The denominator went down and up in the same session and landed where it started.**
`.claude/skills/pre-task/SKILL.md` was deleted and left the governed set;
`.claude/agents/pre-task.md` was created and joined it
([[the-pre-task-becomes-an-agent-and-the-ritual-is-enforced]],
[[the-governed-set-is-swept-and-markdown-by-property]]). **A reader comparing `6 of 15` with
`7 of 15` sees a numerator moving inside a stable denominator, and that is not what happened** —
which is the misreading the section above this one exists to prevent, met a second time and this
time on a round trip rather than a one-way move.

**The numerator moved for the same reason it did on 2026-08-20**: the arriving file is marked from
the moment it exists, so numerator and denominator move together by construction, and the departing
file took an unmarked slot with it. **Neither movement says anything about the eight files that
carry no region.**

**Nothing is patched anywhere.** `index.md` carries `5 of 15`, `vault-scripts` carries `6 of 15` and
`vault-librarian` carries `4 of 15`; each is a reading of its own day and stands
([[the-region-coverage-figure-is-dated-where-it-stands]],
[[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

**And no verdict is read off this.** Whether the criterion is met is the owner's
([[a-sprint-closes-on-its-goal]]).

# Superseded 2026-08-24, on the owner's rejection of the instruction below

> **owner:** «Мне не нравится пункт 6: он устарел, так как там число и какой статус сейчас - мы не
> знаем.»

**The block under *How the number is reported* was shown to him in the ratification sweep of
2026-08-24 and it is the one block of the list he rejected.** What he rejected is the number inside
the instruction, not the instruction: reporting it as *the unmarked files are unchanged* stands, and
the successor states it with no count at all
([[the-region-coverage-instruction-carries-no-count-and-reports-the-unmarked-files-as-unchanged]]).

**Everything on this page stays readable for the question it now answers**, which is *why did we
stop writing the count into the rule* — a page whose own body records the count going from twelve to
thirteen to eight is the evidence for the change.
