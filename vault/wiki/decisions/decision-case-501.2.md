---
type: decision
case: "501.2"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-writes-a-plain-round]]"]
supersedes: ["[[decision-case-495]]"]
origin: raw/2026-09-29/0137/ledger.md#case-501.2
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness]
---

## Context

When a choice is still open, `case-guppi` answers with a round of numbered questions. It builds the round on the template of the skill `grill-me`, which it loads through its `skills` field. The person's own `/grill-me` interviews use the same template. The template gives a question a title, a free body "including multiple choices", and a recommended answer. The instructions of `case-guppi` add one loose sentence: each question body tells what each option changes, "as a before and after". No script reads a round. In the rounds of session 2000, Case 482 Q2 and Q4 gave no before, and Case 483 Q3 and Q4 gave only "After:". `estimate-case-build-writes-a-plain-round` was read `failed` (L25 of `archive/migration/2026-09-28/2000/raw/ledger.md`). The rounds of this session came in mixed shapes. One of them put a list of costs under an option, a second label in all but name. Case 495 put the item off.
The person chose these things. The shape goes into the template of `grill-me`, so that `/grill-me` and `case-guppi` share one template. A question states today once, on a `**Now:**` line. Every question takes the shape, and a question on something new says "nothing exists yet". Each option starts on its own line as a bold list item, with one nested `**After:**` item under it and nothing else. There is no list of costs, no second item and no other label. A cost is a plain sentence inside the `After:` text or in the reasoning after the arrow. At pre-spec the person added two things. The shape is worded once, in the template, and the instructions of `case-guppi` only point to it. The language of the labels does not matter: in the chat the labels stand translated and count as the same labels, because the shape is what is read.
The vault's answer: every item is an `update` with a `ref`, so no vault query ran. `rule-case-build` carries `deferred_by: [[decision-case-495]]`, so its decision line in 501.2 carries `{supersedes:case 495}`, and the page leaves the backlog. What `case-guppi` found in the frame:
- The question line keeps its colon, `❓ **Qn** - **<title>**:`, because `rule-case-protocol` describes how the main agent shows a round by that line. The body starts on the next line.
- The shape is worded once as text, in the template of 501.1, and signed once as a promise, in `estimate-skill-grill-me-asks-in-rounds`, whose `when` already covers both `/grill-me` and a round of `case-guppi`. The new text of `rule-case-build` and `estimate-case-build-writes-a-plain-round` only point to it.
- `estimate-case-protocol-shows-the-built-case` promises that the main agent translates a round line by line, each question "its title, body and recommended answer translated in place, nothing merged, dropped or added". It stays true and is not touched. A label translated in place keeps its line and its list item, so the shape reaches the chat whole. The `－` line of 501.1 says that a translated label counts as the same label.
- The criterion of `estimate-case-build-writes-the-case` still holds true: a round is still "in the form of" the template.
- `rule-skill-wait-what` keeps its own sentence, "as a before and after", for a re-explained round. Pointing it to the template is item C3 and is not done here.
- Not done: the hook of `rule-case-check` still reads no round, so a question off the shape is found only at a reading.
- The two Estimates set `pending` are read in a later session (case 428.1).

The answer check noted that three lines of the old Criteria are not carried. Each is dropped on purpose:
- "On the person's `/grill-me`, each question is numbered, with a title, a body and a recommended answer" in `estimate-skill-grill-me-asks-in-rounds` becomes the two shape lines. The shape covers `/grill-me` and `case-guppi` alike.
- "The form of a round of `case-guppi` is not read here" in the same Estimate is no longer true: the shape of that form now lives in the template. It becomes a `－` line that leaves only the Context paragraph and the case numbers to the Estimates of `rule-case-build`.
- "Each question body says what each option changes, as a before and after." in `estimate-case-build-writes-a-plain-round` moves to `estimate-skill-grill-me-asks-in-rounds`. There it is worded as the shape, so the same promise is not signed twice in two wordings.

## Problem

A round of questions often does not say, for each option, what holds today and what holds after it, and its options run together in solid text. The template gives no shape, and the one sentence in the instructions of `case-guppi` is loose, so the before part gets dropped or merged and extra labels creep in.

## Given

`rule-case-build` — the rule of `case-guppi`; its Render points to the question shape of the template
**＋** `.claude/agents/case-guppi.md` — the file rendered from it
**＋** `estimate-case-build-writes-a-plain-round` — the promise of a plain round; its Criterion replaced whole
**＋** `.claude/skills/grill-me/SKILL.md` — the template that holds the shape
**＋** `estimate-skill-grill-me-asks-in-rounds` — the promise that reads the shape

## History

- 2026-09-29 created · raw/2026-09-29/0137/ledger.md#case-501.2
