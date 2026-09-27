---
type: decision
case: "446"
status: current
update: ["[[rule-language]]", "[[estimate-language-followed]]"]
origin: raw/2026-09-26/2300/ledger.md#case-446
sprint: migration
created: 2026-09-26
tags: [harness, render, workflow]
---

## Context

The `## Language` section of `CLAUDE.md` is the Render of `rule-language`. It says that the name of a Case, its `context`, `problem` and `recommend` "are Russian in the chat and are translated into English in the Spec before its approval". The Criterion of `estimate-language-followed` repeats the step: "The name, `context` and `problem` are translated into English in the Spec before its approval."
Since Case 441 this step does not exist. `case-guppi` answers in English. The main agent translates the prose into Russian only for the chat. The hook of `rule-spec-write` writes the stored English answer into the Spec. So nobody translates anything into English before approval.
Case 441 also made the main agent write a short-form defer in English in the chat, and the hook writes it as shown. This makes a second part of the same sentence false. The Render and the Criterion both say that the name, `context` and `problem` of every Case are Russian in the chat, but a short-form Case is English there.
The Criterion has one more fault: it says `recommend` enters the Spec, and it does not. The Decision pages of Case 441 record that the person kept the sentence then because the result still held. They also name the smallest wording: "are Russian in the chat and English in the Spec".
The vault's answer: this Case creates no page, so there was no slug to ask about. Among the live pages and the files of the repository, the sentence stands in three places only: `CLAUDE.md`, the Render of `rule-language` and the Criterion of `estimate-language-followed`. Decision pages are not counted in that search. No code tests the sentence. The sentence also stands in records under `raw/` and `archive/`: the Spec and `materialize.yaml` of session 1745, the Spec and `materialize.yaml` of the archived session 1859 of 2026-09-23, and the Frontier of this session. Those files keep it as records, and this Case does not change them.
`case-guppi` read the frame and found three things that stay as they are. The `## Language` section of `vault/wiki/case-schema.md` already states the English answer and the English short form, so it stays true and does not change. The `Purpose` of `rule-language` and its `purpose` field also stay true. `estimate-claude-md-rendered` only promises that the file equals the Render and is loaded, so this Case does not touch it (case 378.5).
`estimate-language-followed` stands `failed` from session 1745. This Case replaces its Criterion whole and sets it `pending`. After that, the ledger hook refuses a reading of it in this session (case 428.1). So Frontier line W32 cannot close by a reading this session.

## Problem

The Render of `rule-language`, which is `CLAUDE.md`, and the Criterion of `estimate-language-followed` describe a step that is gone: an English translation of the prose of a Case before approval. They also say that a short-form Case is Russian in the chat, but it is English there. A session reads a false rule on its first turn, and a reading of the Estimate checks a step nobody takes.

## Given

`rule-language` — its Render is the `## Language` section of `CLAUDE.md`
**＋** `CLAUDE.md` — the `## Language` section, rendered from `rule-language`
**＋** `estimate-language-followed` — the Estimate of `rule-language`
**＋** `raw/<date>/<hi HHMM>/spec.md` — the Spec of a session
**＋** `vault/wiki/case-schema.md` — its `## Language` section and the short form constrain the wording

## History

- 2026-09-27 created · raw/2026-09-26/2300/ledger.md#case-446
