---
type: rule
kind: Leaf
purpose: Prevents a ratified decision from ending the session without a page, or a page from carrying a field nobody ratified
status: built
enforcement: check
implementation_ref: [guppi/generate.py, tests/test_generate.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-generate-writes]]", "[[estimate-generate-walks-dates]]", "[[estimate-generate-writes-the-decision-page]]", "[[estimate-generate-fails-alone]]", "[[estimate-generate-cascades]]", "[[estimate-generate-ticks-the-spec]]"]
origin: raw/2026-09-10/ledger.md#case-32
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Purpose

Prevents a ratified decision from ending the session without a page, or a page from
carrying a field nobody ratified. The script is the only writer to `wiki/`. It lays
the content of `materialize.yaml` into schema fields and writes nothing else: no
section is derived from a ref field, no Estimate from a flag, and the Criterion of an
Estimate is replaced whole by the text its Case signed (cases 166.2, 194.1, 201.1). A
page is always created, even incomplete: red lint is an accurate signal of debt, a
decision with no page is the ledger and the vault disagreeing silently. A slug
collision is an error, never a rename — with one exception: a `create` whose slug is a
placeholder page, `status: draft` and no `kind`, fills that page (case 101.1). One bad
entry never stops the run: it is marked `failed`, reported, and the rest apply (case
47). The Decision page of a Case is written before its entries and carries the body of
every defer (cases 52.4, 186.1); the cascade after all entries computes what is
computed — `built`, the archive of a superseded decision, the severity of an Insight —
never by hand (case 104). Once an entry is applied, the script ticks its line in the Spec beside the yaml — `- [ ] <kind> `<slug>`` in the section of the entry's Case — so the Spec's page lines are closed by the one who did the work, and a line not found is no error (case 226.1). The mechanism — the shape of every entry and every History line — lives in the docstring of `guppi/generate.py`.

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
