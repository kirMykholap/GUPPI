---
type: decision
case: "640"
status: archived
create: ["[[rule-search-leaves-out-decisions]]", "[[estimate-search-leaves-out-decisions-in-every-agent]]"]
update: ["[[rule-harness]]", "[[estimate-ask-searches-at-prespec]]"]
origin: raw/2026-10-05/0109/ledger.md#case-640
sprint: migration
created: 2026-10-05
tags: [harness, workflow, session]
---

## Problem

A Grep of `ask-guppi` meant to leave out the Decision pages printed them, because the glob was written from the searched folder and the Grep tool reads it from the repository root. No text tells any agent which glob works, and the frame of each agent states the ban in its own words. The question is where one rule for the agents stands, which agents it binds, what it binds, and how it is checked.

## Recommend

- **How the frame keeps Decision pages out of a search**
  - Recommended: (a) name the glob that works: one sentence in `rule-ask` saying that a Grep or Glob over `vault/wiki/` or a wider folder leaves out Decision pages with `!**/decisions/**`, and that a glob written from the searched folder does not.
  - Answer: (a). The person also asked whether this could be done through `.claude/rules/`, so that it holds for every agent, `case-guppi` included.
- **Whether the frame of `case-guppi` gets the same sentence**
  - Recommended: (b) both frames, one sub-case each.
  - Answer: not answered; replaced by **Where the rule on Decision pages lives**.
- **How the fix is checked**
  - Recommended: (a) a new check on the new rule: at the `/hi` of a later session, the transcripts of the main agent, `ask-guppi`, `case-guppi` and the librarian are read to see that the file stands in each subagent's context and that no Grep or Glob over `vault/wiki/` or a wider folder printed a line of a Decision page. `estimate-ask-searches-at-prespec` keeps its check, and its method names the render by this Case.
  - Answer: (a).
- **Where the rule on Decision pages lives**
  - Recommended: (b) one file in `.claude/rules/`, rendered from a new Rule page, loaded by every agent. The frames keep their own reasons for opening a Decision page.
  - Answer: (b), to try it.
- **What the file in `.claude/rules/` forbids**
  - Recommended: (a) every search leaves them out: every Grep or Glob over `vault/wiki/` or a wider folder leaves out Decision pages with `!**/decisions/**`; a glob written from the searched folder does not; a Decision page is opened only by its path, where the agent's frame allows it; this binds the main agent too.
  - Answer: (a).
- **What the file says about Glob**
  - Recommended: (a) the rule binds Grep, and Glob stays free: every Grep over `vault/wiki/` or a wider folder carries `!**/decisions/**`, alone or next to another filter; the text of a Decision page is read only by a Read of its path where the frame allows; a Glob may print a path of a Decision page; the new check looks at Grep and Read only.
  - Answer: (a).
- **Change**
  - Asked: on the pre-spec findings that `rule-page-read` and `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction` doubt that a file of `.claude/rules/` loads in a subagent, the main agent asked where the rule lives: (a) in `CLAUDE.md`, or (b) `.claude/rules/` kept as a trial. It recommended (a). The person chose (b).
  - Taken: the file stays under `.claude/rules/`. `given` names `rule-page-read` and the lesson. `context` says why the Case tries again: the first reading of the new Estimate shows whether the file loads in a subagent, and if not, a later Case moves the text to `CLAUDE.md`.
- **Change**
  - Asked: on the pre-spec finding that the rule clashes with the librarian's frame and `estimate-documentation-completes`, the main agent asked whether the rule binds the librarian: (a) the librarian is outside it, or (b) it is bound and its frame and that Estimate change. It recommended (a). The person chose (a).
  - Taken: the file binds the main agent, `ask-guppi` and `case-guppi`, and says the librarian follows its own frame. The librarian leaves `when` and the new Estimate. The `－` line on the librarian's `git` command is replaced by one that leaves its calls out of the promise, and its frame and `estimate-documentation-completes` stand.

## History

- 2026-10-05 created · raw/2026-10-05/0109/ledger.md#case-640
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
