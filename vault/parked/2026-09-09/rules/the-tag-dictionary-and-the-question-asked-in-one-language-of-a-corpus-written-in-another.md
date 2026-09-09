---
title: "The tag dictionary, and the question asked in one language of a corpus written in another"
type: rule
status: current
authority: alias-purpose
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[batches-stays-a-tag-of-its-own]]
tags: [process, retrieval, vault]
---

# The tag dictionary, and the question asked in one language of a corpus written in another

What a tag is for, when one is split or kept, and how a question asked in Russian reaches a page written in English. Answers "what do I call this, and in which language".

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A migration's warning is developer output and is written in English, and the migrations already applied are not translated ([[a-migrations-warning-is-developer-output-and-stays-in-english]])
- English technical terms are not transliterated into Cyrillic in Russian chat ([[english-terms-are-not-transliterated-into-cyrillic]])
- The English rule is forward-only and the unit of translation is the file ([[the-english-rule-is-forward-only-and-the-unit-is-the-file]])
- The `schema` tag splits into `db-schema` and `record-schema`, and the bare word stays an alias on each ([[the-schema-tag-splits-into-db-schema-and-record-schema]])
- The dense tags are not split corpus-wide, and every per-folder advisory that stands is named here ([[the-dense-tags-are-not-split-and-the-standing-advisories-are-named-here]])
- The pages about what this project does not own get one shared tag, and stay in the folders they are in ([[the-pages-about-what-this-project-does-not-own-get-one-shared-tag]])
- The plan the owner reads in order to approve it is written in Russian, and `plans` leaves the English list ([[the-plan-the-owner-reads-to-approve-it-is-written-in-russian]])
- The translation of `test_migrations.py` stands with its Cyrillic fixture data and stderr substrings ([[the-migration-test-translation-stands-with-its-remaining-cyrillic]])
- `batches` stays a tag of its own: the merge into `collection` was proposed and refused the same day ([[batches-stays-a-tag-of-its-own]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *the tag dictionary and the two languages* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is not the script's pick.** The script takes the `authority:` of the earliest-decided member, which here is `batches-tag` — a decision about one tag staying separate, and a page that leaves for `archive/`. The slug carried instead is `alias-purpose`, which
[[aliases-carry-the-question-across-languages]] carries and keeps: that concept is the family's own question — how a question in one language reaches a page in the other — so the hook has a live page to match on. `decided_by:` still names a member decision, which is what this folder requires and what the slug is not obliged to agree with.
