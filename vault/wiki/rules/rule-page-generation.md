---
type: rule
kind: Leaf
purpose: Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified
status: built
enforcement: check
implementation_ref: [guppi/generate.py, tests/test_generate.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-generate-writes]]", "[[estimate-generate-walks-dates]]", "[[estimate-generate-writes-the-decision-page]]", "[[estimate-generate-fails-alone]]", "[[estimate-generate-cascades]]", "[[estimate-generate-ticks-the-spec]]", "[[estimate-generate-renames]]", "[[estimate-generate-rewords]]", "[[estimate-generate-writes-rules-from-applies-to]]", "[[estimate-generate-replace-takes-the-leading-indent]]"]
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Purpose

Prevents a ratified decision from ending the session without a page, or a page from
carrying a field nobody ratified. The script is the only writer to `wiki/`. It lays
the content of `materialize.yaml` into schema fields and invents nothing: what it writes beyond that content is computed from the pages, the Specs and the ledgers of `raw/` by the steps this page names — the cascade, the ticks of the Spec, the links of a `rename`, the words of a `reword` (case 369); no section is derived from a ref field, no Estimate from a flag, and the Criterion of an
Estimate is replaced whole by the text its Case signed (cases 166.2, 194.1, 201.1). A
page is always created, even incomplete: red lint is an accurate signal of debt, a
decision with no page is the ledger and the vault disagreeing silently. A slug
collision is an error, never a rename — with one exception: a `create` whose slug is a
placeholder page, `status: draft` and no `kind`, fills that page (case 101.1). An `update` whose item carries `rename: <new slug>` moves the page to the new slug, the same category prefix, and rewrites every link and ref field to it in the live pages of `wiki/`, Decision pages included; a taken or foreign slug fails the entry (case 258.1). An `update` whose item carries `reword` — a list of `{old, new}` pairs — replaces each pair as a whole word in every section but History and Result, and in `purpose` and `method`, of every live page of `wiki/`, one History line per page touched; the page is the owner, and a `new` absent from its own text, or a pair with no hit, fails the entry; a slug goes through `rename`, not `reword` (case 274.1). One bad
entry never stops the run: it is marked `failed`, reported, and the rest apply (case 47). An entry whose Case, kind and slug match an entry of the same yaml that already applied is marked applied, changes no page and ticks no line of the Spec, so a Case approved again in its session, its lines written again with a mark added, changes each page once (cases 514, 522). The Decision page of a Case is written before its entries and carries the body of every defer (cases 52.4, 186.1), and `## Recommend`, the `recommend` of the Case; a Case with sub-cases gets a page of its own before theirs, with `## Problem`, `## Recommend` and `children` and never `## Context`, and the page of each sub-case carries `parent` and no `## Problem` (case 544.7); the page of a Case superseded in its own session and gone from the Spec — its record carries `superseded_by` and no `case_text` — has a two-line body naming the superseding Decision, and its status follows the mechanism as for any superseded page (case 299.4); a page that a later Case supersedes takes the pages of its `children` with it, at any depth: each that stands `current` becomes `superseded` and names the later Decision in `superseded_by`, an archived or superseded one is left as it is, and no `deferred_by` is cleared through them (case 660.3); a page that a later Case supersedes while it stands `archived` stays `archived` where it lies: it takes the later Decision into its `superseded_by`, with one History line, and the `deferred_by` the later Case clears is cleared as for any page (case 467.3), so `cleanup` does not bring it back (case 683); the cascade after all entries computes what is computed — `built`, the archive of a superseded decision, the severity of an Insight, the `rules` of an Entity from the `applies_to` of the live rules (case 305.3) — never by hand (case 104). The script moves no line of the sprint page: a milestone item leaves its milestone only by a Case (`rule-sprint`, case 539.1). Once an entry is applied, the script ticks its line in the Spec — a page entry the line `- [ ] <kind> `<slug>`` in the section of the entry's Case of the Spec beside the yaml; an `estimate` entry, a `create` with a folded reading, a `delete`, whose Estimate no reading will ever reach (case 463), or an `update` that sets an Estimate `passed` or `failed` by the person's decision, which no reading follows (case 672), every unticked `- [ ] read `<slug>`` line of every live Spec of `raw/` — one reading is of the page, whose Criterion is one, however many Cases and however many sessions touched it (cases 312, 326) — in the Spec beside the yaml first — skipping the section of a Case whose first decision entry stands after the reading, the `delete` or the `update` in the ledger, a Case ratified after it — and then in the `spec.md` of the other session folders of `raw/`, oldest first, skipping in every Spec the section of a Case whose entries the yaml beside it marks `superseded_by`, its work standing under the superseding Case — so the Spec's page lines and reading lines are closed by the one who did the work, and a line not found is no error (cases 226.1, 270.1, 280, 286). The mechanism — the shape of every entry and every History line — lives in the docstring of `guppi/generate.py`.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 estimate estimate-generate-writes added · raw/2026-09-10/ledger.md#case-32
- 2026-09-10 status: draft → built · cascade
- 2026-09-10 updated: without --date the script walks every raw/<date> with a yaml, applying what is not yet applied · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 estimate estimate-generate-walks-dates added · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: built → draft · cascade
- 2026-09-10 updated: an entry fails alone whatever the cause; log.md is appended per entry; History and log carry the run's date, created the yaml's · raw/2026-09-10/ledger.md#case-47
- 2026-09-10 estimate estimate-generate-rejects-shape-alone added · raw/2026-09-10/ledger.md#case-47
- 2026-09-10 estimate estimate-generate-logs-per-entry added · raw/2026-09-10/ledger.md#case-47
- 2026-09-10 estimate estimate-generate-dates-history-by-run added · raw/2026-09-10/ledger.md#case-47
- 2026-09-10 updated: a delete of something outside the vault (category unknown) applies with a stdout line; a delete of a missing page still fails · raw/2026-09-10/ledger.md#case-48
- 2026-09-10 estimate estimate-generate-passes-delete-outside-vault added · raw/2026-09-10/ledger.md#case-48
- 2026-09-11 updated: a decision page carries kind and target_slug lists and the sections Context, Problem, Given, When from case_text · [[decision-case-52.1]]
- 2026-09-11 updated: a defer with a page appends the decision slug to deferred_by; a placeholder is born with it; a supersedes removes the superseded decision from the list · [[decision-case-52.3]]
- 2026-09-11 updated: the decision page of a Case is written before its entries; History and log lines end with `· [[decision-case-N]]` when a decision exists, else the ledger pointer · [[decision-case-52.4]]
- 2026-09-11 status: draft → built · cascade
- 2026-09-11 updated: a lesson entry writes the lesson only; no paired Estimate · [[decision-case-53.1]]
- 2026-09-11 updated: an estimate entry always sets status, overwrites Result and appends History; no skip · [[decision-case-53.2]]
- 2026-09-11 updated: an entry that applies loses a failed mark left by an earlier run · [[decision-case-53.3]]
- 2026-09-11 status: built → draft · cascade
- 2026-09-11 estimate estimate-generate-rejects-shape-alone archived · cleanup
- 2026-09-11 estimate estimate-generate-logs-per-entry archived · cleanup
- 2026-09-11 estimate estimate-generate-dates-history-by-run archived · cleanup
- 2026-09-11 estimate estimate-generate-passes-delete-outside-vault archived · cleanup
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 updated: a decision page names its targets by kind — one list per kind present — instead of two lists aligned by position (case 59.4) · [[decision-case-59.4]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-12 updated: the derived Estimate page, the criterion block appended or removed, the decision page's Criterion links and no When (case 72.4) · [[decision-case-72.4]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-13 updated: a create over a placeholder fills it; any other existing page stays a collision (case 101.1) · [[decision-case-101.1]]
- 2026-09-13 updated: the walk covers the yaml of every session folder as well as the date-level yaml (case 103.3) · [[decision-case-103.3]]
- 2026-09-13 updated: a superseded decision is archived by the cascade (case 104.1) · [[decision-case-104.1]]
- 2026-09-13 updated: the clustered lessons of an actioned Insight are archived by the cascade (case 104.2) · [[decision-case-104.2]]
- 2026-09-13 updated: an open Insight with no live child is archived by the cascade; supersedes case 97 (case 104.3) · [[decision-case-104.3]]
- 2026-09-13 updated: an update reaches an archived page in the archive, so a restore and its fix are one entry (case 105.3) · [[decision-case-105.3]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-14 updated: the cascade reads a child's status in the archive too, so an archived child is not counted live (case 110) · [[decision-case-110]]
- 2026-09-14 updated: the cascade derives the ## Insight section of every clustered lesson from its insight field (case 114) · [[decision-case-114]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: a defer marks an Insight deferred_by like a Rule, and the Addressed by section of an Insight is derived from addressed_by (case 124.2) · [[decision-case-124.2]]
- 2026-09-14 updated: the literal decision-case-N of the History line of 2026-09-11 and of the Given of decision-case-112.1–112.6 quoted by hand, a one-off migration; entry 112.6 superseded (case 130.1) · [[decision-case-130.1]]
- 2026-09-14 updated: the History line of case 114, `updated: the`, completed by hand to name the derived ## Insight section — a one-off migration (case 131) · [[decision-case-131]]
- 2026-09-14 updated: an entry materialize failed is skipped, its failed mark kept (case 142.2) · [[decision-case-142.2]]
- 2026-09-14 updated: ref fields written as quoted wikilinks; read through the brackets; one migration over wiki/ and archive/ (case 148.1) · [[decision-case-148.1]]
- 2026-09-14 updated: an entry with superseded_by is skipped without a line; its Decision page still written (case 151) · [[decision-case-151]]
- 2026-09-15 updated: no derived section on any write; the Addressed by derivation of 124.2/164 removed; the migration over wiki/ and archive/; supersedes 164 (case 166.2) · [[decision-case-166.2]]
- 2026-09-15 updated: the cascade step of 114 removed: no ## Insight derived on lessons; supersedes 114 (case 166.3) · [[decision-case-166.3]]
- 2026-09-15 updated: the sentence of 164 on the librarian's create and the refusals, carried by 171 since 164 is superseded before it applies; supersedes 124.2 (case 171) · [[decision-case-171]]
- 2026-09-15 updated: block 148.1 restated without the body sections; supersedes 148.1 (case 172) · [[decision-case-172]]
- 2026-09-15 status: built → draft · cascade
- 2026-09-15 status: draft → built · cascade
- 2026-09-16 deferred · [[decision-case-182]]
- 2026-09-16 updated: a defer writes its purpose to the decision page under · [[decision-case-186.1]]
- 2026-09-16 defer by decision-case-182 superseded · [[decision-case-191]]
- 2026-09-16 deferred · [[decision-case-191]]
- 2026-09-16 updated: Purpose carries the text of the model; How it works dropped by hand, the mechanism in the docstring of guppi/generate.py (case 201.1) · [[decision-case-201.1]]
- 2026-09-16 estimate estimate-generate-writes-the-decision-page added · [[decision-case-201.2]]
- 2026-09-16 estimate estimate-generate-fails-alone added · [[decision-case-201.3]]
- 2026-09-16 estimate estimate-generate-cascades added · [[decision-case-201.4]]
- 2026-09-16 defer by decision-case-191 superseded · [[decision-case-203.2]]
- 2026-09-17 deferred · [[decision-case-217]]
- 2026-09-17 status: built → draft · cascade
- 2026-09-18 defer by decision-case-217 superseded · [[decision-case-226.1]]
- 2026-09-18 estimate estimate-generate-ticks-the-spec added · [[decision-case-226.1]]
- 2026-09-18 updated: generate ticks the page line of the Spec once the entry is applied (case 226.1) · [[decision-case-226.1]]
- 2026-09-18 status: draft → built · cascade
- 2026-09-20 updated: an update with rename moves the page and rewrites its links; a taken or foreign slug fails the entry (case 258.1) · [[decision-case-258.1]]
- 2026-09-20 estimate estimate-generate-renames added · [[decision-case-258.1]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 status: draft → built · cascade
- 2026-09-20 updated: generate ticks the read line of the Spec when it applies a reading, in this unit's Spec first and then in the other sessions of raw/ (case 270.1) · [[decision-case-270.1]]
- 2026-09-20 updated: reword on an update item — pairs replaced as whole words across the live pages, the owner check, failed on no hit (case 274.1) · [[decision-case-274.1]]
- 2026-09-20 estimate estimate-generate-rewords added · [[decision-case-274.1]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 updated: a reading does not tick the read line of a Case ratified after it in the same session (case 280) · [[decision-case-280]]
- 2026-09-21 updated: a reading does not tick the read line of a superseded Case, in any Spec of raw/ (case 286) · [[decision-case-286]]
- 2026-09-21 deferred · [[decision-case-298]]
- 2026-09-22 defer by decision-case-298 superseded · [[decision-case-299.2]]
- 2026-09-22 updated: the Decision page of a Case superseded in its own session has a two-line body naming the superseding Decision (case 299.4) · [[decision-case-299.4]]
- 2026-09-22 estimate estimate-generate-writes-rules-from-applies-to added · [[decision-case-305.3]]
- 2026-09-22 updated: the cascade writes rules on an Entity from the applies_to of the live rules (case 305.3) · [[decision-case-305.3]]
- 2026-09-22 status: draft → built · cascade
- 2026-09-22 updated: one reading ticks every read line of its slug in the first Spec that holds one (case 312) · [[decision-case-312]]
- 2026-09-22 status: built → draft · cascade
- 2026-09-23 updated: a reading ticks the lines of its slug in every live Spec of raw/, not in the first that holds one (case 326) · [[decision-case-326]]
- 2026-09-23 updated: the cascade counts the live Estimates alone — one standing archived is not counted (case 328) · [[decision-case-328]]
- 2026-09-23 updated: after the cascade, the move of a passed-over sprint item to the Backlog (case 354.1) · [[decision-case-354.1]]
- 2026-09-23 updated: the move drops a milestone it left with no line (case 354.2) · [[decision-case-354.2]]
- 2026-09-23 updated: the docstrings of guppi/generate.py name an entry with no category, not a Rule-class file (case 365) · [[decision-case-365]]
- 2026-09-23 updated: the script invents nothing; what it writes beyond the yaml is computed by the steps the page names (case 369) · [[decision-case-369]]
- 2026-09-23 estimate estimate-generate-writes-the-given added · [[decision-case-378.3]]
- 2026-09-24 status: draft → built · cascade
- 2026-09-25 status: built → draft · cascade
- 2026-09-25 status: draft → built · cascade
- 2026-09-27 deferred · [[decision-case-456]]
- 2026-09-27 defer by decision-case-456 superseded · [[decision-case-463]]
- 2026-09-27 updated: a delete ticks the read lines of its slug across the live Specs of raw/, with the skips of a reading (case 463) · [[decision-case-463]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 deferred · [[decision-case-469]]
- 2026-09-29 updated: an entry whose Case, kind and slug match an applied entry of the same yaml is marked applied and changes no page (case 514) · [[decision-case-514]]
- 2026-09-29 estimate estimate-generate-writes-the-given archived · cleanup
- 2026-09-29 updated: a repeat ticks no line of the Spec (case 522) · [[decision-case-522]]
- 2026-09-30 updated: the move of a passed-over sprint item and the drop of an emptied milestone removed, and with them the reading of the Frontiers (case 539.1) · [[decision-case-539.1]]
- 2026-09-30 updated: a replace old that opens with spaces or tabs takes the spaces and tabs before its first word on the page (case 543.3) · [[decision-case-543.3]]
- 2026-09-30 estimate estimate-generate-replace-takes-the-leading-indent added · [[decision-case-543.3]]
- 2026-09-30 updated: the Decision page carries Recommend; a Case with sub-cases gets its own page, linked to theirs by children and parent (case 544.7) · [[decision-case-544.7]]
- 2026-10-04 status: draft → built · cascade
- 2026-10-04 status: built → draft · cascade
- 2026-10-04 status: draft → built · cascade
- 2026-10-05 updated: a superseded Decision page takes the pages of its sub-cases with it (case 660.3) · [[decision-case-660.3]]
- 2026-10-05 status: built → draft · cascade
- 2026-10-05 status: draft → built · cascade
- 2026-10-05 updated: an update that sets an Estimate passed or failed by the person's decision ticks its read lines across the live Specs, with the skips of a reading (case 672) · [[decision-case-672]]
- 2026-10-06 defer by decision-case-469 superseded · [[decision-case-683]]
- 2026-10-06 updated: a supersede of a Decision already archived keeps it archived and only appends the superseding Case to its superseded_by, so cleanup does not bring it back (case 683) · [[decision-case-683]]
