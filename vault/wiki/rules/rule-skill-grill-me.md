---
type: rule
kind: Leaf
purpose: Prevents an interview from acting on a plan before each of its decisions is put to the person and settled, and the skill that runs it from being a file no rule page governs
status: draft
enforcement: render
governs: .claude/skills/grill-me/SKILL.md
render_mode: full
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-skill-grill-me-asks-in-rounds]]"]
origin: raw/2026-09-26/2300/ledger.md#case-443.1
sprint: migration
created: 2026-09-26
tags: [harness, workflow]
---

## Purpose

Prevents an interview from acting on a plan before each of its decisions is put to the person and settled, and the skill that runs it from being a file no rule page governs. `/grill-me` asks in rounds: the frontier of a design tree, the questions whose prerequisites are settled, each with a recommended answer. It served the person's own interviews without a page until case 443.1. The same text serves `case-guppi`, which loads it through the `skills` field of its frontmatter ([[rule-case-build]]), so two of its sentences name no one agent: a fact is found by the agent itself, or by a sub-agent when the agent can dispatch one; the shared understanding is confirmed by the user's word unless the instructions that started the grill name another confirmation. The question template is an indented code block, the form it took when case 443.1 was written, before case 444 let a fenced value carry a shorter fence.

## Render

<!-- rule-skill-grill-me -->
---
name: grill-me
description: Grill the user relentlessly about a plan, decision, or idea. Use when the user wants to stress-test their thinking, or uses any 'grill' trigger phrases.
---

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Each question should be formatted like so:

    ❓ **Q1** - **<question title>**:

    **Now:** <what holds today, said once for the question; "nothing exists yet" when nothing does>
    <a sentence that introduces a quotation and names its source, when the question quotes one>:
    > <the quoted words, as the source holds them>

    **Options:**

    🔹 **(a) <option name>**
      - **After:** <what holds with this option>
        > <a quotation inside the item, indented four spaces as far as the text of the item>

    🔹 **(b) <option name>**
      - **After:** <what holds with this option>

    ➡️ <your recommended answer, and why>

The body of a question starts on the line after its title. The `**Now:**` line says once what holds today. The label `**Options:**` stands alone on the line before the first option. Each option starts on its own line, after a blank line, with the mark 🔹 and its name in bold, and under it stands one nested `**After:**` item: what holds with this option. No other line of a question starts with 🔹. An option has nothing else under it: no list of costs, no second item, no other label. A cost, when it matters, is a plain sentence inside the `**After:**` text or in the reasoning after `➡️`. Every question takes this shape, one on a new idea with nothing behind it too. In the language of the chat the labels may stand translated; the shape stays.

A list starts on a new line and never runs inside a sentence. Items marked by a number, a letter or a bullet, and a series of two or more clauses that name parallel things, stand one per line; a short series of words inside a sentence stays in it. In the `**Now:**` text a list stands under the sentence that introduces it. Under an `**After:**` item it stands nested one level deeper, inside that item. In the recommended answer it stands on the lines under `➡️`, which close the question.

A quotation — words taken from a page, a file or a reply to show what they say — stands as a blockquote on its own line, a fragment of a few words too; it never stands inside a sentence in quote marks. The sentence that introduces it stands on the line before it and names its source, and the quoted words stand as the source holds them. In the `**Now:**` text the blockquote stands under the sentence that introduces it. Under an `**After:**` item it stands inside that item, indented four spaces as far as the text of the item, so that it renders there and is no second item. In the recommended answer it stands on the lines under `➡️`.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), find it yourself, or dispatch a sub-agent when you can dispatch one; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the shared understanding is confirmed: by the user's word, unless the instructions that started the grill name another confirmation.
<!-- /rule-skill-grill-me -->

## History

- 2026-09-27 created · [[decision-case-443.1]]
- 2026-09-27 estimate estimate-skill-grill-me-asks-in-rounds added · [[decision-case-443.1]]
- 2026-09-28 status: draft → built · cascade
- 2026-09-29 updated: every question of a round takes one shape: a Now line once, each option on its own line with one After item under it and nothing else (case 501.1) · [[decision-case-501.1]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-09-29 updated: the options of a question stand under an Options label, each marked with 🔹; every list stands one item per line (case 511.1) · [[decision-case-511.1]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 updated: a quotation in a round stands as a blockquote on its own line, inside an After item indented to its text (case 524.1) · [[decision-case-524.1]]
- 2026-09-30 updated: the Options label of the question template stands at the indent of the other lines (case 543.2) · [[decision-case-543.2]]
- 2026-09-30 status: draft → built · cascade
- 2026-10-02 status: built → draft · cascade
