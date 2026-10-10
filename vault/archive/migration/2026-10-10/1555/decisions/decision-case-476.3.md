---
type: decision
case: "476.3"
status: archived
update: ["[[rule-prespec]]", "[[estimate-language-spec-prose-in-english]]"]
origin: raw/2026-09-28/1318/ledger.md#case-476.3
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Context

`rule-language` keeps the repository in English and the chat with the owner in Russian. The rule is text. Its Render stands in `CLAUDE.md`, and the words English and Russian are also written into four more rendered texts: `case-schema.md`, `case-guppi.md`, `ask-guppi.md` and the `pre-spec` skill. The pre-spec finding `ratified.untranslated` looks for Cyrillic. A project with another pair of languages would have to rewrite each of these. `estimate-language-followed` also promises that the agent's own text in the chat is Russian. The reply that acknowledged Case 471 was English, and the Estimate failed, as it had failed on 2026-09-26. `insight-session-reply-language-follows-the-english-text-read` (`open`, severity 2) found that no guard reads the language of a reply.
The person decided in four rounds. There is no check and no reminder on the reply: a slip in the chat costs one request to rewrite it and lands nothing in the vault. So the chat leaves the promise of the Estimate, and that decision answers the Insight. The two languages become settings, `documentation_lang` and `chat_lang`. They are set in the `## Render` of a new Rule, `rule-guppi-config`, which is rendered into `guppi.toml`, guppi's one settings file. A Render may hold `{{documentation_lang}}` or `{{chat_lang}}`. The render reads the codes from the `## Render` of `rule-guppi-config` and puts the name of the language into the output file. It does not read `guppi.toml`, because that file is itself an output of the render. The page keeps the placeholder, so a changed code reaches every text at the next render. The checks read `guppi.toml`: the pre-spec finding takes the script of `documentation_lang` from it through the same module, `guppi/config.py`.
The vault's answer: no page describes a settings file of guppi. `rule-settings` governs Claude Code's `.claude/settings.json`, which is another file. `rule-morph` holds the questions asked at install and the category set as data. It is deferred by case 239 and stays untouched here, because naming it would take up its defer. The install questions and the category set stay with it. Both `create` lines carry a `ref`, and a Glob of `vault/**/` finds no page for `rule-guppi-config` or `estimate-guppi-config-fills-the-languages`.
The frame. The Purpose of `rule-harness` counts the pages that belong to it and run in no pipeline, with the list of their cases. 476.1 adds the new page and case 476.1 to that sentence. `rule-render-harness` is a Leaf that still carries `## How it works`, and the Rule schema says the section leaves at its next touch (cases 193, 200.2). `generate` replaces a section but cannot remove one. So 476.1 removes the section as a one-off migration and moves its text into the docstring of `guppi/render.py`, where the schema puts the mechanism of a Leaf. The docstring already holds most of that text. It gains the sentence of case 139.1, the librarian's commit of case 89.2, and the placeholders.
The Criterion of `estimate-render-harness-reproduces` says that the diff of each file equals the text of its page's Render; with a placeholder, the file holds the Render with the names put in. Its block of case 139.1 also says that the How it works of the page gains a sentence, and that sentence now stands in the docstring. That Estimate is still in the shape before case 193 and waits for a later recut in Slice 3g. Its lines stand until then, and the new Estimate states the fill.
`estimate-orchestration-shows-the-built-case`, `estimate-case-build-writes-the-case`, `estimate-ask-finds` and `estimate-spec-write-checks-the-written-case` name English or Russian as this project's values. With `en` and `ru` they stay true, so none is touched. The Purpose sections that say English stay for the same reason.
Four lines of the old Criterion of `estimate-language-followed` read the chat, and the new Criterion drops them by the person's decision: the Russian of the agent's text, the ledger lines as they stand in the chat, the short form in the chat, and transliteration. A short form written in another language would still fail the line on the Spec, because the hook writes it there as shown. Every other line is carried, with `documentation_lang` in place of English. The Criterion of `estimate-language-spec-prose-in-english` keeps each of its lines, with a letter outside the script of `documentation_lang` in place of a Cyrillic letter and `guppi.toml` read in its `when`.
The render code lands at once and the pages land at the librarian's run: a render with no placeholder needs no `rule-guppi-config` (476.1). The pre-spec finding reads `guppi.toml`, which exists only after the librarian's render. Before that the finding only goes red and loses nothing, so it keeps no old form.
Not done: transliteration of English terms into Cyrillic (the failure of 2026-09-26) is not checked. The language of the chat has no guard. The install questions stay with `rule-morph`. The aliases of `tags.md` and `glossary.md` stay Russian data. The slug `estimate-language-spec-prose-in-english` stays as it is. The other Leafs that still carry `## How it works` are not touched.

## Problem

The language pair is written by hand into several rendered texts and one check, so another pair means rewriting each of them. `estimate-language-followed` also promises the language of the agent's replies in the chat. Only the agent guards that, so a slip the person fixes with one request fails a rule whose output in the repository was right.

## Given

`guppi/config.py` — the script of a language, and the read of `guppi.toml`
**＋** `guppi/ratified.py` — `untranslated`, the judgment of the finding
**＋** `guppi/prespec.py` — `check_untranslated`, the text of the finding
**＋** `tests/test_prespec.py` — the tests of the finding
**＋** `guppi.toml` — the language of the repository, as the checks read it
**＋** `rule-prespec` and `.claude/skills/pre-spec/SKILL.md` — its Render names the finding
**＋** `estimate-language-spec-prose-in-english` — its Criterion replaced whole

## History

- 2026-09-28 created · raw/2026-09-28/1318/ledger.md#case-476.3
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
