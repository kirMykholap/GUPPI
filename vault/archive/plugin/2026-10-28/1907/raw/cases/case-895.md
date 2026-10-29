## Case 895 — A test shows whether a helper goes on after a compaction

> **context:**
> Each answer to a round, each change and each finding goes back to the same `case-guppi` by `SendMessage`, and the helper keeps all it has read and said, so its context only grows (`lesson-case-build-agent-context-grows-on-every-resume`, which put the helper of Case 819 at 701016 tokens). In this session the task notifications of the main transcript `~/.claude/projects/c--PROJECTS-GUPPI/20e2347c-c292-4d8a-bd74-e0eb896ad1c1.jsonl` give `subagent_tokens` 87839, 101506 and 139934 for the helper of Case 893, and 82569, 104531, 142770, 184241 and 184584 for the helper of Case 894. The put-off of this growth stands on `rule-orchestration` by Case 884, carried over from Case 876.
> The person chose a procedure for a later session: a hook sees that a helper is past 400 000 tokens and has it write an interim Case with what is still to do; a compaction then comes by size, and the same helper reads its file again and goes on. The person chose to test the idea first and to build it only if it works, so this Case adds one check and one Work task, and the put-off on `rule-orchestration` stays as it stands for the Case that builds the procedure. The test writes only in a folder under the temporary area of the session, outside the repository, so nothing in the vault or the code changes by it and the one rule of `ratification.md` is kept; `rule-work-mode` runs only the approved Spec, so the test needs this Case to stand in it.
> The test rests on behaviour of Claude Code read in its documentation. https://code.claude.com/docs/en/sub-agents says that subagents compact automatically as their own context fills, that `autoCompactWindow` in the frontmatter of one subagent sets its window from 100000 to 1000000 tokens and needs v2.1.296 or later, that a size set by `CLAUDE_CODE_AUTO_COMPACT_WINDOW` in the shell overrides the field, and that a subagent can be resumed after a restart by resuming the same session; the transcript of the helper of Case 894 records version 2.1.310. The same page says that `/compact` acts on the main conversation, and https://code.claude.com/docs/en/hooks gives `PreCompact` a block and no way to add instructions to an automatic compaction, whose `custom_instructions` is null, and gives `PostCompact` no decision control, so nothing but the size starts a compaction or shapes its summary. https://code.claude.com/docs/en/context-window says that after a compaction the system prompt still applies, skill bodies come back up to 5 000 tokens each, and Claude Code reads again up to five recent files, a file over 5 000 tokens coming back as a path only. https://code.claude.com/docs/en/headless says that `claude -p` loads the hooks and subagents of its working folder unless `--bare` is set, waits for background subagents before it exits, and continues a conversation with `--resume` and a session id. https://code.claude.com/docs/en/model-config says that `opus` resolves to Opus 5.5 and that a model with a native 1M window compacts at about 967K tokens, so a helper today compacts only near that size.
> No page of the documentation that was read says whether the transcript file of a subagent keeps its earlier lines after a compaction, or whether `SubagentStop` and `PostCompact` hooks run for a subagent after one; the checks of `rule-case-check` read the earlier rounds and reads of a helper from that file. A Grep for `"subtype":"compact_boundary"` over `~/.claude/projects/c--PROJECTS-GUPPI` with the glob `*.jsonl` printed one file, the main transcript `682b0e2f-5e90-435e-be2e-7ba7f97d2ad4.jsonl`, with the record on its line 190, after the earlier lines; it printed no subagent transcript. The new Estimate checks these facts. A Glob `vault/**/estimate-case-build-goes-on-after-a-compaction.md` printed nothing, so the slug is free. No Estimate of `rule-case-build` speaks of a compaction, and this Case changes no text of the rule, so none of them is touched.

> **problem:**
> The procedure the person chose for a full helper rests on facts about how a subagent compacts that the documentation does not settle. Building it before those facts are seen would likely need a second Case.

> **recommend:**
> - **How do we stop the memory of the helper from growing?**
>   - Recommended: (a) a new helper rebuilds a built Case; not (b), compaction by size, since whether the checks keep their records is not checked.
>   - Answer: in the person's own words, `case-guppi` should watch its own context: a hook like the one of the main session warns past a size, and the question is what happens next.
> - **What happens once the hook finds a helper past the limit?**
>   - Recommended: (a) a new helper takes over the Case.
>   - Answer: the person disagreed with that procedure: the helper should work on, and when the hook says its context is full, a procedure saves its work and passes it on. Replaced by the question how a full helper hands its work to a fresh one.
> - **At what size is a helper past the limit?**
>   - Recommended: (a) 200 000 tokens.
>   - Answer: (b), 400 000 tokens, as in the main session.
> - **How does a full helper hand its work to a fresh one?**
>   - Recommended: (a) a handover file, then a fresh helper.
>   - Answer: the person proposed to combine the hook and the compaction: the helper writes an interim Case and what is left to do, a compaction follows, and the same helper goes on. Replaced by the question whether the hook and compaction work together on the same helper.
> - **Should the hook and compaction work together on the same helper?**
>   - Recommended: (a) the hook asks for an interim Case, then compaction comes by size.
>   - Answer: test the idea first, and build it if it works.
> - **Where do the test and the build go?**
>   - Recommended: (b) only the test now, the build in a later session.
>   - Answer: agreed, (b).
> - **How is the test run?**
>   - Recommended: (a) the main agent runs it in a test folder, with no window.
>   - Answer: agreed, (a).
> - **When does the test run?**
>   - Recommended: (a) in the Work Mode of this session.
>   - Answer: agreed, (a).
> - **What carries the test into Work Mode?**
>   - Recommended: (a) a small Case: one new check on `rule-case-build`, met by the test.
>   - Answer: agreed, (a).

> **given:**
> `estimate-case-build-goes-on-after-a-compaction`: the new check of a helper that compacts.
> **＋** `rule-case-build`: the rule of the helper, the target of the check.
> **＋** `lesson-case-build-agent-context-grows-on-every-resume`: the growth the later procedure answers.
> **＋** `rule-work-mode`: it runs only the approved Spec.
> **＋** `vault/wiki/ratification.md`: the one rule, kept since the test writes outside the repository.
> **＋** a test folder under the temporary area of the session: the agent file of a test helper, its hook and its text files.
> **＋** `~/.claude/projects/`: the transcripts of the test session and of its helper.

> **when:**
> The main agent runs `claude -p` in a test folder outside the repository, whose agent file of a test helper sets `autoCompactWindow: 100000` and tells it to read its interim file again after a compaction, and whose hooks log each `SubagentStop` and `PostCompact` event.
> **＋** The first run starts the test helper, has it read text files and write its interim file; a second run with `--resume` sends it more files, past 100000 tokens; a third run with `--resume` asks it to go on.

> **then:**
> The transcript of the test helper under `~/.claude/projects/` holds a `compact_boundary` record after it passes 100000 tokens.
> **＋** That transcript file keeps the lines of the helper before the `compact_boundary` record.
> **＋** The log of the test folder holds a `SubagentStop` line after the compaction.
> **＋** After the compaction the test helper reads its interim file again and goes on from what it says.
> **－** The size of 100000 tokens binds the test helper alone, through its agent file, and no size is set in the shell of `claude -p`.
> **－** No file of the repository changes by the test.

> **tasks:**
> - [ ] create `estimate-case-build-goes-on-after-a-compaction`
>   - ref: `rule-case-build`
>   - kind: `QA`
>   - purpose: `Whether a subagent with its own autoCompactWindow compacts past that size, keeps its earlier lines in its transcript file, still fires SubagentStop after the compaction, and reads its interim file again and goes on, as the later procedure for a full case-guppi needs`
>   - method: `by hand, in the Work Mode of the session that creates it: the test of the Criterion run by claude -p in a folder under the temporary area of the session, and the transcript of the test helper and the log of the folder read against the Criterion, recorded in the estimate line`
>   - tags: `[harness, hooks, case-build]`
> - [ ] by hand in Work Mode: set up the test folder under the temporary area of the session (the agent file of the test helper with `autoCompactWindow: 100000`, a hook on `SubagentStop` and `PostCompact` that appends one line to a log, large text files), run `claude -p` there with `--permission-mode acceptEdits` and with `--resume` and the session id of the first run for the later runs, read the transcript of the test helper and the log, and record what the test found as a `knowledge` lesson line with the test as its source.
> - [ ] read `estimate-case-build-goes-on-after-a-compaction`

> **ratification:**
> ```
> - decision[case 895][create][estimate-case-build-goes-on-after-a-compaction]{ref:rule-case-build}{tags:harness,hooks,case-build}
> ```
