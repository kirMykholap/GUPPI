---
type: rule
kind: Leaf
purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round of case-guppi from reaching the main agent with a question out of the form of the grill-me template, a round of case-guppi or a Case from being shown after a text of the main agent's own with no word to the agent at the person's next message, and a summary of case-guppi from reaching the main agent without the id and the name of the Case it built
status: built
enforcement: hook
implementation_ref: [guppi/casecheck.py, tests/test_casecheck.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-case-check-sends-back-a-faulty-case]]", "[[estimate-case-check-shows-only-the-checked-case]]", "[[estimate-case-check-requires-a-backlog-item-decided-on-its-page]]", "[[estimate-case-check-notes-a-criterion-line-not-carried]]", "[[estimate-case-check-notes-a-then-line-shared-by-siblings]]", "[[estimate-case-check-refuses-a-letter-outside-the-script]]", "[[estimate-case-check-requires-each-question-of-the-rounds]]", "[[estimate-case-check-refuses-a-problem-in-a-sub-case]]", "[[estimate-case-check-exits-2-on-an-error]]", "[[estimate-case-check-refuses-text-before-a-round]]", "[[estimate-case-check-sends-back-a-faulty-round]]", "[[estimate-case-check-sends-back-a-ratified-case-in-another-shape]]", "[[estimate-case-check-sends-back-a-case-number-held-by-another-agent]]", "[[estimate-case-check-refuses-text-outside-the-list]]", "[[estimate-case-check-sends-back-a-clash-with-another-case]]", "[[estimate-case-check-refuses-a-changed-case-file]]", "[[estimate-case-check-sends-back-a-summary-without-the-case-name]]", "[[estimate-case-check-sends-back-a-ratified-case-without-a-target]]", "[[estimate-case-check-judges-a-showing-after-a-refusal]]"]
origin: raw/2026-09-25/1228/ledger.md#case-419.3
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow, session]
---

## Purpose

Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other `given`, `when`, `then`, `tasks` or `ratification` than the ones that passed them, while fewer than three refusals of that Case stand since the person's last message, a round of `case-guppi` from reaching the main agent with a question out of the form of the template of `.claude/skills/grill-me/SKILL.md` (case 601.1), a round of `case-guppi` from being shown after a text of the main agent's own written after the round came back with no word to the agent: the `Stop` run lets the showing through, and the run on `UserPromptSubmit` tells the agent of it at the person's next message, so that the round is not shown twice (cases 562, 699.1), and a Case from being shown with a text of the main agent's own outside the list under its heading and its `ratification` or written after the summary of `case-guppi` came back with no word to the agent, told in the same way at the person's next message, so that the Case is not shown twice, while a Case whose file was not sent or whose showing differs from the stored text is still refused (cases 611, 699.2), each judged only by what follows the last refusal of the check in the turn (case 692), and a summary of `case-guppi` from reaching the main agent without the id and the name of the Case it built (case 662.3); the Case reaches the person in the file `case-guppi` writes, which the hook checks whole when the agent stops and stores, and a file that differs from its stored text is not shown or written into the Spec (cases 452.1, 645.2). The check of the file of a Case compares its Cases with the other Cases of the session, ratified or not, a dropped Case whose file is empty aside (case 701.7), by the judgment the check after ratification runs, so a Case that writes what another Case writes goes back to `case-guppi` before the person first sees it (case 629.1). Until case 419 no script read a Case before its ratification: the hook of `rule-spec-write` checks it only after the person signed, and a fault of the form was found by the person or at pre-spec ([[insight-case-form-chat-form-read-by-no-script]]). The checks of a Case are the ones of pre-spec and of the Spec hook, imported, not copied ([[rule-one-judgment-one-implementation]]), and every check of a round knows a round by one test and its title line by one pattern (case 601.1); the text of the story sections — `context`, `problem` and `recommend` — is not among them, only their presence, their order, the script of the name, `context` and `problem` of a Case, by the language finding of pre-spec, and the title of each item of `recommend` against the questions of the rounds (case 544.3): the person judges the text (cases 449, 537). The `Stop` run judges every reply whether `stop_hook_active` is set or not, since Claude Code keeps the flag set from a refusal of any `Stop` hook until the person's next message, and guards its own loop by its refusals in the transcript since that message: a reason of one Case is given at most three times, and a showing still wrong after that passes with a line on stderr, the Spec hook comparing it at ratification (case 688.1).

## History

- 2026-09-25 created · [[decision-case-419.3]]
- 2026-09-25 estimate estimate-case-check-sends-back-a-faulty-case added · [[decision-case-419.3]]
- 2026-09-25 updated: the Stop hook compares the shown Case with the checked one (case 419.4) · [[decision-case-419.4]]
- 2026-09-25 estimate estimate-case-check-shows-only-the-checked-case added · [[decision-case-419.4]]
- 2026-09-26 updated: the check reads the newest output of the subagent that holds a Case, a handback or a text, else last_assistant_message; the loop guard is the store, not stop_hook_active · [[decision-case-434]]
- 2026-09-26 updated: the categories whose schema rule the session changes come from the ratification fences and the session's window (case 436.4) · [[decision-case-436.4]]
- 2026-09-26 updated: the Stop comparison reads only given, when, then, tasks and ratification (case 441.3) · [[decision-case-441.3]]
- 2026-09-27 updated: pre-spec compares the plan with no ratified copy (case 445.2) · [[decision-case-445.2]]
- 2026-09-27 updated: the Purpose says the person judges the text of the story sections, while the check requires them and their order (case 449) · [[decision-case-449]]
- 2026-09-27 updated: the check writes the file of a Case that passed, from the text it stores, and stores the time of the store (case 452.1) · [[decision-case-452.1]]
- 2026-09-27 updated: the Stop comparison covers the sections a reply shows, the prose is not translated, and a shown Case needs a sending of its file in the same turn (case 452.2) · [[decision-case-452.2]]
- 2026-09-27 updated: the answer of case-guppi is checked against the open backlog lines of the Frontier (case 467.2) · [[decision-case-467.2]]
- 2026-09-27 estimate estimate-case-check-requires-a-backlog-item-decided-on-its-page added · [[decision-case-467.2]]
- 2026-09-28 updated: a line of a Criterion replaced whole that the new Criterion does not carry is a note, sent back to case-guppi once and kept in the store (case 472.1) · [[decision-case-472.1]]
- 2026-09-28 estimate estimate-case-check-notes-a-criterion-line-not-carried added · [[decision-case-472.1]]
- 2026-09-28 updated: two then lines of sibling sub-cases that share most of their words are a note (case 472.2) · [[decision-case-472.2]]
- 2026-09-28 estimate estimate-case-check-notes-a-then-line-shared-by-siblings added · [[decision-case-472.2]]
- 2026-09-30 updated: the check of each answer of case-guppi runs the language finding of pre-spec as a finding (case 537) · [[decision-case-537]]
- 2026-09-30 estimate estimate-case-check-refuses-a-letter-outside-the-script added · [[decision-case-537]]
- 2026-09-30 updated: the check of each answer of case-guppi requires the title of each question of its rounds in a recommend of the Case (case 544.3) · [[decision-case-544.3]]
- 2026-09-30 estimate estimate-case-check-requires-each-question-of-the-rounds added · [[decision-case-544.3]]
- 2026-09-30 updated: a sub-case that carries problem is a finding of the check of the answer (case 544.4) · [[decision-case-544.4]]
- 2026-09-30 estimate estimate-case-check-refuses-a-problem-in-a-sub-case added · [[decision-case-544.4]]
- 2026-09-30 updated: the Stop run exits 2 on its own error after the payload is read; the --subagent run keeps exit 0 (case 555.1) · [[decision-case-555.1]]
- 2026-09-30 estimate estimate-case-check-exits-2-on-an-error added · [[decision-case-555.1]]
- 2026-10-01 updated: the Stop check reads one ratification under the heading of a top-level Case as the showing of each sub-case it names (case 561.10) · [[decision-case-561.10]]
- 2026-10-01 updated: the Stop run refuses a reply that shows a round of case-guppi after a text of the main agent's own; after pre-spec only the first line of the reply is judged (case 562) · [[decision-case-562]]
- 2026-10-01 estimate estimate-case-check-refuses-text-before-a-round added · [[decision-case-562]]
- 2026-10-01 updated: the reason for the exemption after /pre-spec: each answer of the loop comes back in a turn of its own, and rule-prespec sets the text written there (case 581.2) · [[decision-case-581.2]]
- 2026-10-01 updated: the module docstring of guppi/casecheck.py says a Stop refusal is a user record marked isMeta, which the turn of the reply skips; a test checks a sending before a refusal (case 584) · [[decision-case-584]]
- 2026-10-02 updated: How it works removed by hand, a one-off, its facts in the docstring of guppi/casecheck.py; the language finding on an answer accepts a Latin letter in a code span (case 589.2) · [[decision-case-589.2]]
- 2026-10-03 updated: the SubagentStop check sends back a round of case-guppi with a question out of the grill-me form, once per text; one test of a round serves every check of a round (case 601.1) · [[decision-case-601.1]]
- 2026-10-03 estimate estimate-case-check-sends-back-a-faulty-round added · [[decision-case-601.1]]
- 2026-10-03 estimate estimate-case-check-sends-back-a-ratified-case-in-another-shape added · [[decision-case-610.1]]
- 2026-10-03 estimate estimate-case-check-sends-back-a-case-number-held-by-another-agent added · [[decision-case-610.2]]
- 2026-10-03 updated: the Stop check refuses a showing of a Case with a text of the main agent's own outside the list under its heading and its ratification (case 611) · [[decision-case-611]]
- 2026-10-03 estimate estimate-case-check-refuses-text-outside-the-list added · [[decision-case-611]]
- 2026-10-04 updated: the check of an answer compares its Cases with the other Cases of the session, from the plan file and the store (case 629.1) · [[decision-case-629.1]]
- 2026-10-04 estimate estimate-case-check-sends-back-a-clash-with-another-case added · [[decision-case-629.1]]
- 2026-10-04 estimate estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent added · [[decision-case-629.3]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-05 updated: the check reads the file case-guppi wrote, whole, when the agent stops, and keeps the old path of the answer text until the writer is live (case 645.2) · [[decision-case-645.2]]
- 2026-10-05 estimate estimate-case-check-refuses-a-changed-case-file added · [[decision-case-645.4]]
- 2026-10-05 status: built → draft · cascade
- 2026-10-05 estimate estimate-case-check-judges-a-lone-sub-case-with-its-stored-parent archived · cleanup
- 2026-10-05 estimate estimate-case-check-sends-back-a-summary-without-the-case-name added · [[decision-case-662.3]]
- 2026-10-05 updated: the SubagentStop check sends back a summary whose Case line is missing or differs from the heading of the file (case 662.3) · [[decision-case-662.3]]
- 2026-10-05 estimate estimate-case-check-sends-back-a-ratified-case-without-a-target added · [[decision-case-671.1]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-06 updated: the Stop run judges every reply whatever stop_hook_active says, a reason of one Case given at most three times a stretch; purpose set anew (case 688.1) · [[decision-case-688.1]]
- 2026-10-06 estimate estimate-case-check-judges-a-showing-after-a-refusal added · [[decision-case-688.1]]
- 2026-10-07 updated: the check judges a text before a round or a Case only after the round or the summary came back and after its last refusal in the turn · [[decision-case-692.1]]
- 2026-10-07 updated: a layout fault of a shown round passes the Stop run and is told to the agent at the person's next message by casecheck --prompt (case 699.1) · [[decision-case-699.1]]
- 2026-10-07 updated: a layout fault of a shown Case passes the Stop run and is told to the agent at the person's next message; a file not sent or a showing that differs from the store is still refused (case 699.2) · [[decision-case-699.2]]
- 2026-10-07 updated: the check of a Case compares it with no dropped Case, whose file is empty (case 701.7) · [[decision-case-701.7]]
