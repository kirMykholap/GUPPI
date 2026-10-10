---
type: decision
case: "743"
status: archived
children: ["[[decision-case-743.1]]", "[[decision-case-743.2]]", "[[decision-case-743.3]]", "[[decision-case-743.4]]", "[[decision-case-743.5]]", "[[decision-case-743.9]]", "[[decision-case-743.6]]", "[[decision-case-743.7]]", "[[decision-case-743.8]]"]
origin: raw/2026-10-08/2352/ledger.md#case-743
sprint: migration
created: 2026-10-08
tags: [sprint, workflow, librarian, harness, hooks, ledger, session, render]
---

## Problem

The close of a sprint leaves `raw/` full and files late sessions under the wrong sprint. It leaves `sprint.md` naming a closed sprint, and it keeps old Backlog lines in `backlog.md` for good. Nothing sets what the opening of the next sprint asks. The steps of the closing session load in every session.

## Recommend

- **What leaves raw/ at the close**
  - Recommended: (b) the close sweeps every session whose ledger is fully turned into pages, whatever its day; the closing session, an unfinished session and a conserved Spec stay until they can leave.
  - Answer: agreed, (b).
- **Which sprint folder a late session goes to**
  - Recommended: (b) by the sprint the session's own yaml records, `sprint.md` as the fallback.
  - Answer: agreed, (b).
- **The old event logs**
  - Recommended: (b) the close moves the logs of the earlier dates into the archive, still outside git.
  - Answer: agreed, (b).
- **The Backlog of the closed sprint**
  - Recommended: (b) the opening Case lists each line of the old Backlog, and the person moves or drops each one.
  - Answer: not each line. The opening of a sprint says that the backlog has entries and asks the person whether to take any of them, without going through them all.
- **What the opening Case of the next sprint asks**
  - Recommended: (b) a fixed list: the sprint id, its goal in one sentence, its Definition of done as Estimates, the first milestone and its items, and each line of the old Backlog.
  - Answer: (b), with the backlog question changed to match the answer on the Backlog.
- **When a line of the old Backlog leaves backlog.md**
  - Recommended: (b) a line leaves once the live sprint page names its page or its text, or its page is finished.
  - Answer: agreed, (b).
- **Where the questions of the opening Case are written down**
  - Recommended: (a) in `orchestration.md`, beside the paragraph on the closing session.
  - Answer: in a separate skill, since `orchestration.md` is read in every session, and the close and the opening of a sprint are rare.
- **What the new skill holds**
  - Recommended: (b) one skill, for example `/sprint`, for the whole turn of a sprint; the paragraph on the closing session moves out of `orchestration.md`.
  - Answer: agreed on the content, but as two skills, `/sprint-close` and `/sprint-open`. The person asked whether `/sprint-close` runs in Plan Mode or after it and leads up to the librarian, and asked that `/sprint-open` load by itself at `/hi` when no sprint is active, read from a variable.
- **How the skill starts**
  - Recommended: (b) the main agent starts it at those two moments, and the person may type it too.
  - Answer: agreed, (b).
- **Where the active sprint is recorded**
  - Recommended: (a) a key `sprint` in `guppi.toml`, written by `guppi render` from the live sprint page.
  - Answer: agreed, (a); replaced by the question on where the active sprint is written.
- **How `/hi` starts `/sprint-open`**
  - Recommended: (a) `/hi` reads the key and starts the skill when it is missing.
  - Answer: (b), a hook on `/hi`.
- **When `/sprint-close` runs and how far it goes**
  - Recommended: (a) from `/hi` to the end of Work Mode; it reaches the librarian through the close line of the Spec.
  - Answer: agreed, (a). The person asked how the skill starts when the close item is picked on the Frontier, what happens to the other items, and asked that the opening of a sprint add the close item at once as the last item of its last milestone.
- **How the agent knows to start `/sprint-close`**
  - Recommended: (a) the opening Case writes the close line in a fixed form that names `/sprint-close`, and picking it starts the skill.
  - Answer: agreed, (a).
- **What happens to the rest of the Frontier**
  - Recommended: (a) the skill puts off every other Cases line at once; the Work and Ask lines stay open.
  - Answer: agreed, (a).
- **When the session has already ratified another Case**
  - Recommended: (a) the skill refuses and puts the close off for a session of its own.
  - Answer: agreed, (a).
- **Where the active sprint is written**
  - Recommended: (b) in `sprint.md`: after the close `guppi sprint` writes the heading of the closed sprint marked closed, and the hook on `/hi` reads it.
  - Answer: agreed, (b).
- **Change**
  - Asked: at `/pre-spec`, the person chose that the merge of `migration` into `main` moves into `/sprint-close`: the closing session gives the merge to the next session as a Work line, and `/sprint-open` stays as decided.
  - Taken: the closing Case of `/sprint-close` holds a task line for the merge, which Work Mode leaves unticked so that the brief gives it as Work to the session that opens the next sprint; the merge line leaves the Backlog of `entity-sprint-migration` (743.8).
- **Change**
  - Asked: at `/pre-spec`, the person chose that 743.9 also rewrites the `purpose` of `estimate-sprint-checks-the-file`, so that it covers both the render of the live page and the closed form.
  - Taken: the `set` of `estimate-sprint-checks-the-file` in 743.9 writes a new `purpose` that names both.

## History

- 2026-10-09 created · raw/2026-10-08/2352/ledger.md#case-743
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
