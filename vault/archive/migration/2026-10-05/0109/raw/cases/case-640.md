## Case 640 — A file under `.claude/rules/` keeps the text of Decision pages out of the searches of the main agent, `ask-guppi` and `case-guppi`

> **context:**
> `ask-guppi` may not search `vault/wiki/decisions/` except for two named reasons, and both reasons open one Decision page by its path. Its frame does not say how to leave that folder out of a Grep over all of `vault/wiki/`. At the `/pre-spec` of session 2245, call 16 of agent `a390781c7f1241c18` ran a Grep over `vault/wiki` with the glob `!decisions/**`, and the Grep printed lines of Decision pages. The reading of `estimate-ask-searches-at-prespec` at the `/hi` of session 0109 failed on that call. The cause is the way the Grep tool reads a glob. A glob that holds a slash counts from the working directory, which is the repository root, and not from the folder being searched. So `!decisions/**` skips only a `decisions/` folder at the root, and there is none.
>
> I tested this with Greps of `^type: decision` over `vault/wiki/`:
> - With the glob `!decisions/**`, the Grep printed 1080 files.
> - With `!**/decisions/**`, it printed 1 file, `rule-decisions-schema.md`, which is not a Decision page.
> - With `!vault/wiki/decisions/**`, it printed the same 1 file.
> - With `*.md !**/decisions/**`, it printed the same 1 file, so the exclusion also works next to a second filter.
>
> The Glob tool has no field for an exclusion. It prints paths only.
>
> The person first chose to name the glob that works in the frame of `ask-guppi`. They then chose to put the rule in one file under `.claude/rules/`, so that it holds for more than one agent, `case-guppi` included. Claude Code loads the files of `.claude/rules/` into context the way it loads `CLAUDE.md`. The folder does not exist yet: a Glob `.claude/rules/**` printed nothing. The file binds every Grep over `vault/wiki/` or a folder that holds it. It also says that the text of a Decision page is read only by a Read of its path, for a reason the frame of the agent names. A Glob stays free, because it shows no text. No frame lets the main agent read a Decision page, so a question on why something was decided goes to `ask-guppi`, whose frame allows that read.
>
> The `/pre-spec` findings on the ratified Case raised two questions, and the person answered both.
>
> First, where the rule lives. `rule-page-read` records that a file in `.claude/rules/` was weighed for its own rule and not taken, because it is text the agent may follow, and whether it loads inside a subagent is not documented. `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction` says the same of a rules file scoped by `paths:`. It ends: a rule every writer must follow goes where it loads for sure, which is `CLAUDE.md`, the agent's definition or the skill. The new file has no `paths:`, so it does not depend on a matching read. Whether it loads in a subagent is still unknown. The person chose to keep `.claude/rules/` as a trial. The first reading of `estimate-search-leaves-out-decisions-in-every-agent` shows whether the file stands in the context of `ask-guppi` and `case-guppi`. If it does not, a later Case moves the text to `CLAUDE.md`. The sentence of `rule-page-read` stands. It records a choice made for that rule, and its fact about subagents is what this reading tests. The lesson is of another session and gets no mark.
>
> Second, whether the rule binds the librarian. The frame of the librarian, the render of `rule-documentation`, says no read is forbidden to it. A read its job does not need, the text of a Decision page included, gets a line under Flags of the brief and is not a fault. The frame also has it run `git diff` on the files the scripts of the run wrote. The person chose to leave the librarian outside the rule. The file binds the main agent, `ask-guppi` and `case-guppi`, and says the librarian follows its own frame. So that frame and `estimate-documentation-completes` stand, and the new Estimate does not read the librarian.
>
> The pages. `rule-search-leaves-out-decisions` is new, a render Leaf under `rule-harness`. Like `CLAUDE.md`, it governs a file the agent reads when it acts, and the governed-files hook and `render --check` refuse drift in that file. `guppi/render.py` and `guppi/guard.py` read any `governs` path, and `write_all` creates the missing folder, so no code changes. The Purpose of `rule-harness` counts nine rules that run in no pipeline. A tenth child makes that count false, so the Purpose is updated. The `children` field is filled by the scripts from `ref`. A Glob `vault/**/*search-leaves-out-decisions*` printed nothing, so both new slugs are free. The Estimate slug adds `-in-every-agent` to the name shown in the round, to follow the slug form of `case-schema.md`. Both creates carry a `ref`, so the vault query of `ask-guppi` was not run.
>
> What the Case does with the Estimates:
> - `estimate-ask-searches-at-prespec` keeps its Criterion. Its last line already promises that no Grep or Read of `ask-guppi` reaches `vault/wiki/decisions/` outside the two reasons. Only its `method` is set anew, to name the render by this Case.
> - The new Estimate checks the main agent, `ask-guppi` and `case-guppi`, and whether the file loads.
> - `estimate-harness-pipeline` keeps its Criterion. Its line on the rules in no pipeline lists rules the Purpose of `rule-harness` names, and it already leaves out the settings file of guppi that the Purpose names. So it reads as rules the Purpose must hold, not as the whole list. After the update the Purpose still names each rule of that line, and the line stays true.
>
> The frame I read, by these searches:
> - A Grep of `` (Grep|grep|search)[^.]{0,80}`vault/wiki/` `` over `vault/wiki/rules/` printed `rule-case-build.md` and `rule-ask.md`. Over `.claude/` it printed `.claude/agents/case-guppi.md` and `.claude/agents/ask-guppi.md`. These are the rules that set what an agent does at a Grep over the wiki. Each forbids searching the Decision pages and allows only reads by path. The new file agrees with them and gives the means, so they stand.
> - A Grep of `decisions/` over `vault/wiki/rules/` printed `rule-case-build.md`, `rule-ask.md`, `rule-documentation.md`, `rule-decisions-schema.md` and `rule-vault-layout.md`. Over `.claude/` it printed `.claude/agents/librarian-guppi.md`, `.claude/agents/case-guppi.md` and `.claude/agents/ask-guppi.md`. Here is why each stands:
>   - The librarian is outside the rule, for the reason above.
>   - `rule-decisions-schema` governs the `schema.yaml` of the folder, and `rule-vault-layout` lists the folder. Neither speaks of a search.
> - A Grep of `decisions?/|Decision page` over `vault/wiki/estimates/` printed 16 files. Here is how they are placed:
>   - `estimate-ask-searches-at-prespec` enters the Case.
>   - `estimate-case-build-checks-the-finished-case` already promises that `case-guppi` searches the live pages with the Decision pages left out, so its Criterion stands.
>   - `estimate-documentation-completes` stands, because the librarian is outside the rule.
>   - `estimate-sprint-close-archives-the-decisions` is read by a script against the folder, as its Result records, and the file binds no script.
>   - The rest speak of the scripts that write, move, lint or rename Decision pages, not of an agent's search.
> - A Grep of `\.claude/rules` over `vault/wiki/`, with `!**/decisions/**`, printed `rule-page-read.md`, placed above.
> - A Grep of `every subagent|system prompt` over `vault/wiki/`, with `!**/decisions/**`, printed 8 files:
>   - `glossary.md`, `entity-glossary.md`, `rule-claude-md.md`, `rule-internal-context.md`, `rule-one-judgment-one-implementation.md`, `estimate-claude-md-rendered.md` and `estimate-one-judgment-one-implementation-followed.md` say that `CLAUDE.md` is the system prompt, which every session and every subagent loads. The How it works of `rule-claude-md` says the file holds what each agent needs and no more. These stay true. `CLAUDE.md` is still the system prompt and gains nothing. The new file is a second loaded text beside it, and `CLAUDE.md` does not claim to be the only one.
>   - `lesson-subagents-parallel-on-one-tree-red-mid-flight.md` speaks of tests run while subagents edit, not of what they load.
>
> Case 638 changes the confirmation paragraph of `rule-ask`, and this Case does not touch it. Case 639, built again in the same batch, lets the first answer of `ask-guppi` end its list of what was not checked with a line for each rule binding the agent that a search broke, the file of this Case included. This Case does not change `rule-ask`.
>
> Not done:
> - No hook refuses a Grep without the exclusion, and no `deny` permission locks the folder. If the next reading fails, those are the next step.
> - The frames of `ask-guppi`, `case-guppi` and the librarian are not changed.
> - The failed reading line of `estimate-ask-searches-at-prespec` is the main agent's, and this Case writes none.

> **problem:**
> A Grep of `ask-guppi` meant to leave out the Decision pages printed them, because the glob was written from the searched folder and the Grep tool reads it from the repository root. No text tells any agent which glob works, and the frame of each agent states the ban in its own words. The question is where one rule for the agents stands, which agents it binds, what it binds, and how it is checked.

> **recommend:**
> - **How the frame keeps Decision pages out of a search**
>   - Recommended: (a) name the glob that works: one sentence in `rule-ask` saying that a Grep or Glob over `vault/wiki/` or a wider folder leaves out Decision pages with `!**/decisions/**`, and that a glob written from the searched folder does not.
>   - Answer: (a). The person also asked whether this could be done through `.claude/rules/`, so that it holds for every agent, `case-guppi` included.
> - **Whether the frame of `case-guppi` gets the same sentence**
>   - Recommended: (b) both frames, one sub-case each.
>   - Answer: not answered; replaced by **Where the rule on Decision pages lives**.
> - **How the fix is checked**
>   - Recommended: (a) a new check on the new rule: at the `/hi` of a later session, the transcripts of the main agent, `ask-guppi`, `case-guppi` and the librarian are read to see that the file stands in each subagent's context and that no Grep or Glob over `vault/wiki/` or a wider folder printed a line of a Decision page. `estimate-ask-searches-at-prespec` keeps its check, and its method names the render by this Case.
>   - Answer: (a).
> - **Where the rule on Decision pages lives**
>   - Recommended: (b) one file in `.claude/rules/`, rendered from a new Rule page, loaded by every agent. The frames keep their own reasons for opening a Decision page.
>   - Answer: (b), to try it.
> - **What the file in `.claude/rules/` forbids**
>   - Recommended: (a) every search leaves them out: every Grep or Glob over `vault/wiki/` or a wider folder leaves out Decision pages with `!**/decisions/**`; a glob written from the searched folder does not; a Decision page is opened only by its path, where the agent's frame allows it; this binds the main agent too.
>   - Answer: (a).
> - **What the file says about Glob**
>   - Recommended: (a) the rule binds Grep, and Glob stays free: every Grep over `vault/wiki/` or a wider folder carries `!**/decisions/**`, alone or next to another filter; the text of a Decision page is read only by a Read of its path where the frame allows; a Glob may print a path of a Decision page; the new check looks at Grep and Read only.
>   - Answer: (a).
> - **Change**
>   - Asked: on the pre-spec findings that `rule-page-read` and `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction` doubt that a file of `.claude/rules/` loads in a subagent, the main agent asked where the rule lives: (a) in `CLAUDE.md`, or (b) `.claude/rules/` kept as a trial. It recommended (a). The person chose (b).
>   - Taken: the file stays under `.claude/rules/`. `given` names `rule-page-read` and the lesson. `context` says why the Case tries again: the first reading of the new Estimate shows whether the file loads in a subagent, and if not, a later Case moves the text to `CLAUDE.md`.
> - **Change**
>   - Asked: on the pre-spec finding that the rule clashes with the librarian's frame and `estimate-documentation-completes`, the main agent asked whether the rule binds the librarian: (a) the librarian is outside it, or (b) it is bound and its frame and that Estimate change. It recommended (a). The person chose (a).
>   - Taken: the file binds the main agent, `ask-guppi` and `case-guppi`, and says the librarian follows its own frame. The librarian leaves `when` and the new Estimate. The `－` line on the librarian's `git` command is replaced by one that leaves its calls out of the promise, and its frame and `estimate-documentation-completes` stand.

> **given:**
> `rule-search-leaves-out-decisions` and `.claude/rules/search-leaves-out-decisions.md`: the new rule and its render. It names the glob `!**/decisions/**` for a Grep over `vault/wiki/` and keeps out `vault/wiki/decisions/`.
> **＋** `estimate-search-leaves-out-decisions-in-every-agent`: the new check of that rule.
> **＋** `rule-harness` and `estimate-harness-pipeline`: the parent MOC, whose Purpose counts the rules in no pipeline, and the Estimate that lists them. The Criterion is unchanged.
> **＋** `estimate-ask-searches-at-prespec`: its `method` is set anew; its Criterion stands.
> **＋** `rule-ask` and `.claude/agents/ask-guppi.md`, with `rule-case-build` and `.claude/agents/case-guppi.md`: the frames that name the reasons to open a Decision page. Unchanged.
> **＋** `rule-documentation`, `.claude/agents/librarian-guppi.md` and `estimate-documentation-completes`: the frame of the librarian and its check, outside the rule. Unchanged.
> **＋** `rule-page-read` and `lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction`: they doubt that a file of `.claude/rules/` loads in a subagent. Unchanged.
> **＋** `rule-claude-md` and `entity-glossary`: they call `CLAUDE.md` the system prompt of every session and subagent. Unchanged.
> **＋** `vault/raw/2026-10-05/0109/cases/case-639.md`: it lets the first answer of `ask-guppi` name a search rule it broke.

> **when:**
> A session starts after `uv run guppi render` has written `.claude/rules/search-leaves-out-decisions.md` from `rule-search-leaves-out-decisions`, and the main agent, `ask-guppi` or `case-guppi` calls Grep, Glob or Read.

> **then:**
> `.claude/rules/search-leaves-out-decisions.md` stands in the context of the main agent, of `ask-guppi` and of `case-guppi`.
> **＋** Each Grep whose path is `vault/wiki/` or a folder that holds it carries `!**/decisions/**` in its glob, alone or after another filter, and prints no line of a page under `vault/wiki/decisions/`.
> **＋** The text of a Decision page reaches one of these agents only by a Read of its path, for a reason of `.claude/agents/ask-guppi.md` in `ask-guppi` and `case-guppi`, and for no reason in the main agent.
> **－** A Glob that prints the path of a Decision page breaks nothing: it shows no text of the page.
> **－** The calls of the librarian are outside this promise: it follows `.claude/agents/librarian-guppi.md`.

> **tasks:**
> - [ ] create `rule-search-leaves-out-decisions`
>   - ref: `rule-harness`
>   - kind: `Leaf`
>   - purpose: `Prevents the text of a Decision page from entering the context of the main agent, ask-guppi or case-guppi through a search of the vault`
>   - enforcement: `render`
>   - governs: `.claude/rules/search-leaves-out-decisions.md`
>   - render_mode: `full`
>   - tags: `[harness, workflow, session]`
>   - sections.Purpose:
>     ```
>     Prevents the text of a Decision page from entering the context of the main agent, `ask-guppi` or `case-guppi` through a search of the vault. A Decision page states a Case at its moment, and the folder holds a page per Case, so a search over the whole wiki that does not leave them out fills the context with them. The frames of `ask-guppi` and `case-guppi` forbid the search, but none named a glob that works, and the one an agent wrote did not: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from the folder it searches, so `!decisions/**` over `vault/wiki/` left nothing out (case 640). The librarian follows its own frame, which flags such a read rather than forbids it. The rule stands in one file under `.claude/rules/`, which Claude Code loads into context with no `paths:` to scope it. Whether such a file loads inside a subagent was not documented when [[rule-page-read]] weighed one ([[lesson-harness-a-paths-rule-misses-a-new-file-and-a-compaction]]); this rule tries it, its Estimate reads whether it loads, and if it does not, a later Case moves the text to `CLAUDE.md`.
>     ```
>   - sections.Render:
>     ```
>     <!-- rule-search-leaves-out-decisions -->
>     # The text of Decision pages stays out of every search
>
>     This file binds the main agent, `ask-guppi` and `case-guppi` (case 640). The librarian follows `.claude/agents/librarian-guppi.md`, and this file does not bind it.
>
>     - Every Grep whose `path` is `vault/wiki/` or a folder that holds it, the repository root included, carries `!**/decisions/**` in its `glob`: alone, or after another filter with a space between them, as in `*.md !**/decisions/**`.
>     - A glob written from the searched folder, such as `!decisions/**`, does not leave the folder out: the Grep tool reads a glob that holds a slash from the working directory, the repository root, and not from its `path`.
>     - The text of a Decision page under `vault/wiki/decisions/` is read only by a Read of its path, and only for a reason the frame of the agent names.
>     - A Glob may print the path of a Decision page: a path is no text of the page.
>     <!-- /rule-search-leaves-out-decisions -->
>     ```
> - [ ] create `estimate-search-leaves-out-decisions-in-every-agent`
>   - ref: `rule-search-leaves-out-decisions`
>   - kind: `QA`
>   - purpose: `Whether the main agent, ask-guppi and case-guppi load .claude/rules/search-leaves-out-decisions.md, each of their Greps over vault/wiki/ or a folder that holds it leaves out the Decision pages with !**/decisions/**, and the text of a Decision page reaches them only by a Read of its path for a reason their frame names`
>   - method: `by hand at the /hi of a later session: the transcripts of the main agent and of each ask-guppi and case-guppi of a session after the render of .claude/rules/search-leaves-out-decisions.md by case 640, whether the file stands in each context and each Grep, Glob and Read call, read against the Criterion, recorded in the estimate line`
>   - tags: `[harness, workflow, session]`
> - [ ] update `rule-harness`
>   - old: `Nine more belong here and run in no pipeline:`
>   - new: `Ten more belong here and run in no pipeline:`
>   - old: `the hook that shows the size of the context, and the hooks that read a page of the vault without its History (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1).`
>   - new: `` the hook that shows the size of the context, the hooks that read a page of the vault without its History, and the file under `.claude/rules/` that keeps the text of Decision pages out of a search (cases 59.6, 59.8, 127, 145.1, 304, 315, 392.3, 420.1, 476.1, 640). ``
>   - change: `a tenth rule outside the pipeline: the file under .claude/rules/ that keeps Decision pages out of a search (case 640)`
> - [ ] update `estimate-ask-searches-at-prespec`
>   - set:
>     ```
>     method: 'by hand at the /hi of a later session: the Grep, Glob and Read calls of ask-guppi at a /pre-spec after the render of .claude/agents/ask-guppi.md by case 633.2 and of .claude/rules/search-leaves-out-decisions.md by case 640, read in its agent transcript against the Criterion, recorded in the estimate line'
>     ```
>   - change: `the method names the render of .claude/rules/search-leaves-out-decisions.md by case 640; the Criterion stands`
> - [ ] `uv run guppi render`: `.claude/rules/search-leaves-out-decisions.md`
> - [ ] read `estimate-search-leaves-out-decisions-in-every-agent`

> **ratification:**
> ```
> - decision[case 640][create][rule-search-leaves-out-decisions]{ref:rule-harness}{tags:harness,workflow,session}
> - decision[case 640][create][estimate-search-leaves-out-decisions-in-every-agent]{ref:rule-search-leaves-out-decisions}{tags:harness,workflow,session}
> - decision[case 640][update][rule-harness]{ref:rule-harness}
> - decision[case 640][update][estimate-ask-searches-at-prespec]{ref:rule-ask}
> ```
