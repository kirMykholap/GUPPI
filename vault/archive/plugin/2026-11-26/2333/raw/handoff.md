# Handoff — 2026-11-26, items of the backlog

## Notes from memory

- The person's "1-5. Берём 4,5 одним батчем" was read as items 4 and 5 alone; the person meant items 1 to 3 as well, and said so after Cases 1072 and 1073 were ratified, so items 1 to 3 came as a second batch. In the second batch the person kept the item `rule-ratification` as it stands (the list of plain sprints leaves `caseid.py` after the close of `plugin`), so its Case 1076 was dropped and holds no decision line.
- Case 1075 asked where the person's wish for more in the README goes; the main agent said that Case 1074 takes the wish up in this session, and the person agreed, so Case 1075 writes no Backlog note for it.
- Case 1074 keeps its `recommend` item "How the change is checked" with the words "at the Retro of this session", as the person answered it; its `method` and `context` were moved at `/pre-spec` to the person's answer at a `/hi` after this handoff.
- At `/hi`, the brief of session 1515 said that the event of `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` stood in session 1515; its transcript shows two acknowledging replies after `/pre-spec` (lines 1219 and 1277), both ending with the Frontier and sent on by the hook, neither waiting for the person's word, so the reading was not taken.

## Direct instructions to the librarian

- Check first the update of `entity-sprint-plugin` under Case 1075: its first `replace` takes three lines of the milestone The plugin whole, and its second adds three lines to `## Closed`; the line of Case 1070 in `## Closed` must stay before them.
- `{supersedes:case 1007}`, `{supersedes:case 1009}`, `{supersedes:case 1068}`, `{supersedes:case 1021}` and `{supersedes:case 1050}` each retire a defer: `estimate-retro-loads-on-a-red-command`, `estimate-synthesis-keeps-actioned-by-the-mark`, `entity-guppi-repository` and `entity-sprint-plugin` leave `backlog.md`, which goes from 8 items to 4 (`rule-ratification` and the three plain lines stay).
- Case 1073 sets `estimate-synthesis-keeps-actioned-by-the-mark` `passed` by the person's decision with `checked: 2026-11-27`; with its two other Estimates `passed`, the cascade should set `rule-synthesis` `built`.
- Cases 1072, 1073 and 1074 were ratified twice, after `/pre-spec`, with the same decision lines; the ledger holds each line once.

## What actually got done

- Cases ratified: 1072 (1072.1, 1072.2), 1073, 1074 and 1075.
- Code and files changed: `README.md` gains the sections Key terms, The path of one decision (with a Mermaid diagram) and What a question looks like; no section it held was removed. No code or test changed.
- `uv run --project .guppi guppi test`: 2034 passed, 6 skipped, 2 deselected; `uv run --project .guppi guppi style`: all checks passed, 109 files already formatted.
- Readings: ledger lines 1 and 2 at `/hi` (`estimate-guppi-config-fills-the-main-branch`, `estimate-orchestration-dispatches-case-guppi-at-a-level`, both `passed`); at Retro, `estimate-retro-loads-on-a-red-command` and `estimate-sprint-plugin-plugin-milestone-holds-the-merge-and-the-close`, both `passed`. No lesson.

## Debt

- No box of the Spec is debt.
- 10 boxes wait for the librarian: the 7 page lines of Cases 1072 to 1075, the `read` lines of the two Estimates read at Retro, and the `guppi sprint` line of Case 1075. The `read` lines of `estimate-sprint-plugin-retro-loads-in-the-cli` and `estimate-guppi-repository-readme-shows-the-path-of-a-decision` wait for their event and for the person.
- `estimate-sprint-plugin-retro-loads-in-the-cli` — waits for its event: a call of `/retro` by the agent at the end of `/work` in the Claude Code CLI. This session ran in the VS Code extension, which handed the commands of the skill to the agent, so the event did not come.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — waits for an acknowledging reply after `/pre-spec` that waits for the person's word; this session had none.

## Observations

- frontierguard refused two Edits of `frontier.md` that closed the box and wrote the closer of the line of C6 in two changes; the line was then closed in one edit of the whole line, as the guard asks.
- `guppi prespec --check` printed, after the findings were fixed, five `note:` lines on Case 1072: four lines of the old Criterion of `estimate-retro-loads-on-a-red-command` not carried, which moved by meaning into 1072.2, and one `then` line of 1072.2 sharing most of its words with 1072.1; `ask-guppi` confirmed that the two promises differ.

## For the next session

- The sprint item C1, `rule-clean-branch` (the clean branch), put off again at the close of Plan Mode.

## Ask the person

- `estimate-guppi-repository-readme-shows-the-path-of-a-decision` — needs the person — at a `/hi` after this handoff: do the new sections of `README.md` (Key terms, The path of one decision with its Mermaid diagram, What a question looks like) explain GUPPI to a newcomer?
