<!-- approved 00:57:00 · session 3397fb1f -->

# Session 2333 — Plan Mode of 2026-11-26

## Case 1072 — The check of /retro on a red test is split into a text check and a CLI load

> **context:**
> When a skill opens, Claude Code first runs the `!` commands at its top, and one command that exits non-zero stops the whole skill. The page https://code.claude.com/docs/en/skills says "A failed command aborts the entire skill invocation, not just its own placeholder", and that with the default `bash` shell any non-zero exit code counts as a failure. Case 1003.4 put `--exit-zero` on the lines Tests and Style of the Render of `rule-retro`, and lines 7 and 9 of `.claude/skills/retro/SKILL.md` hold `guppi test --exit-zero` and `guppi style --exit-zero`. In `.guppi/guppi/commands.py`, `run` sets the status 1 on a red command or a missing key, and `exit_zero` prints `exit code: <status>` and returns 0 when the flag stands. `estimate-retro-loads-on-a-red-command` stays `pending`: Case 1007 put it off, its `## Problem` being that no Case set when or in which client the first load of `/retro` after the render is read. `lesson-vs-code-extension-hands-the-skill-preamble-to-the-agent` says the VS Code extension hands the `!` commands to the agent and does not run them when the skill loads, so a load there proves nothing, while the CLI runs them and refuses the skill on a non-zero exit. The brief of the librarian of session 1515 says the render left `.claude/skills/retro/SKILL.md` unchanged.
> The person chose the split. Case 1072.1 gives the Estimate a new `purpose`, `method` and Criterion that read the text of `.claude/skills/retro/SKILL.md` and run the `--exit-zero` tests of `.guppi/tests/test_commands.py`, and this session's Retro can take that reading. Case 1072.2 creates a one-off Estimate of `entity-sprint-plugin` with `once: true` that reads a load of `/retro` in the Claude Code CLI in its transcript. That follows the field `method` of `rule-estimates-schema` (case 1071.1): an Estimate whose target is not a sprint page reads no transcript, and the rule binds an Estimate that gets a new `method`. The old `method` read a transcript, so a new `method` on `rule-retro` could not keep that reading. The `method` of Case 1072.2 waits for its event by a part that opens with `by hand, after` and names the event before a colon, as `waits_for_an_event` of `.guppi/guppi/lint.py` judges it. It holds no `first ... after the render`, which `FIRST_AFTER` of the same module would report as the class `moment`. Its `transcript` part is allowed on a sprint page, as `reads_a_transcript` judges it.
> The output of the flag itself — the lines of the run, then `exit code: <n>`, then exit 0 — is promised by `estimate-guppi-config-runs-the-test-and-style-commands`, which stands `passed` and names `.claude/skills/retro/SKILL.md` in its `When`. So the new Criterion of Case 1072.1 does not sign that output again. It names the flag on the lines Tests and Style, the exit 0 of a red run that the text and the tests show, and the line Ledger. It says no word of the load, since its `method` cannot see whether Claude Code refuses the skill. The old Criterion is replaced whole. Its lines on the load move, by meaning, into the Criterion of Case 1072.2 alone: the trigger, the skill that loads whatever the commands find, and the lines that come back with their output and exit code. At `/pre-spec`, `ask-guppi` found that 1072.1 and 1072.2 signed the load twice, against "Nothing is signed twice" of `case-schema.md`, so the words of the load left 1072.1. It also found that the `when` of 1072.2 covered two paths, the agent's call and the typed `/retro`, while its `method` reads one load, against "the reading of a `then` that covers both takes both (case 173)". By the person's answer, the `when` of 1072.2 names only the agent's call of `/retro` on `PreToolUse Skill` at the end of `/work`, and the typed `/retro` is not read. The sentence of the `## Purpose` of `rule-retro` that says the tests and the style check run with `--exit-zero` so a red test does not stop the skill from loading stays true, so the rule gets no `update`. The other Estimates of `rule-retro` speak of something else: `estimate-retro-runs-on-to-the-handoff`, `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`, `estimate-retro-red-in-the-baseline-is-not-charged` and `estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case` by their `purpose`, and `estimate-retro-loads`, which has no `purpose`, by its Criterion, which speaks of the readings Retro takes. None speaks of the load on a red command, so none is touched. The update of Case 1072.1 carries `{supersedes:case 1007}` and names the page, so `generate` clears its defer. The brief of session 1515 reports `guppi test` exit 0 and `guppi check` exit 0, no line, under `## Readings at the close`. A Grep of `estimate-retro-loads-on-a-red-command` over `vault/wiki/` and `.claude/` printed four files: `vault/wiki/rules/rule-retro.md`, where the slug stands in its `estimates` field and History, and `vault/wiki/backlog.md`, `vault/wiki/brief.md` and `vault/wiki/log.md`, which a run writes. None of these goes false. `backlog.md` lists the page under Deferred, and the librarian's run writes that file again after the defer is retired. The check of this file also named `vault/raw/2026-11-26/2333/cases/case-1073.md`. I read the finished files of Cases 1073 and 1074 whole. Case 1073 sets `estimate-synthesis-keeps-actioned-by-the-mark` of `rule-synthesis` `passed` by the person's decision. It cites the paragraph of `rule-retro` on readings, which this Case leaves as it stands. Case 1074 adds new parts to `README.md` and creates an Estimate on `entity-guppi-repository`. Neither changes a page, file or moment that this Case changes, and no line of either goes false against this Case. Case 1074 says that Case 1075 changes `entity-sprint-plugin`. This Case changes no sentence of that page: its `create` with `ref: entity-sprint-plugin` only adds the new Estimate to the page's `estimates`, which `generate` writes. No prompt or check named Case 1075, so its file was not read. The Grep of `lesson\[error\]|\{addresses:` in this session's ledger printed nothing, so no mark is written.

> **problem:**
> The check that `/retro` loads on a red test waits for a load that names no client, while only a load in the Claude Code CLI can show it. The rule now also forbids a transcript reading in an Estimate of a rule page that gets a new `method`.

> **recommend:**
> - **How the check of /retro on a red test is taken**
>   - Recommended: (a) split: a text check on `rule-retro`, the lines Tests and Style of `.claude/skills/retro/SKILL.md` read and the `--exit-zero` tests of `.guppi/tests/test_commands.py` run; and a one-off check on `entity-sprint-plugin` that reads a load of `/retro` in the Claude Code CLI in its transcript, before the close of the sprint `plugin`.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: at `/pre-spec`, the words of the load leave Case 1072.1 so the load is signed once, in Case 1072.2. Asked of the person: how many load paths of `/retro` in the CLI Case 1072.2 checks, recommended (a), only the agent's call at the end of `/work`.
>   - Taken: the `when`, `then` and `purpose` of Case 1072.1 name only the flag, the exit 0 of a red run and the line Ledger. By the person's answer, agreed (a), the `when`, `purpose` and `method` of Case 1072.2 name only the agent's call of `/retro` at the end of `/work`, and the typed `/retro` is not read.

### Case 1072.1 — The lines Tests and Style of /retro run both commands with --exit-zero

> **given:**
> `estimate-retro-loads-on-a-red-command`: its `purpose`, `method` and Criterion are replaced, and its defer retired.
> **＋** `.claude/skills/retro/SKILL.md`: the file rendered from the Render of `rule-retro`, whose text the reading reads.
> **＋** `.guppi/tests/test_commands.py`: the `--exit-zero` tests that the reading runs.
> **＋** `uv run --project .guppi pytest .guppi/tests/test_commands.py -k exit_zero`: the command that runs those tests.
> **＋** `rule-estimates-schema`: an Estimate off a sprint page reads no transcript.

> **when:**
> `uv run --project .guppi guppi render` writes `.claude/skills/retro/SKILL.md` from the Render of `rule-retro`.
> **＋** `uv run --project .guppi pytest .guppi/tests/test_commands.py -k exit_zero` runs.

> **then:**
> The line Tests of `.claude/skills/retro/SKILL.md` runs `uv run --project .guppi guppi test --exit-zero`, and its line Style runs `uv run --project .guppi guppi style --exit-zero`.
> **＋** With that flag, a run of either command that finds a failing test or a style finding exits 0.
> **－** The line Ledger runs `uv run --project .guppi guppi tail` as before, with no flag.

```then
update:
- slug: estimate-retro-loads-on-a-red-command
  set:
    status: pending
    purpose: Whether the lines Tests and Style of /retro run guppi test and guppi style with --exit-zero, so that a run of either command that finds a failing test or a style finding exits 0, while its line Ledger runs guppi tail with no flag
    method: 'uv run --project .guppi pytest .guppi/tests/test_commands.py -k exit_zero; by hand, at the Retro of the session that sets this method: the lines Tests, Style and Ledger of .claude/skills/retro/SKILL.md read against the Criterion, recorded in the estimate line'
  change: 'taken up: the Criterion replaced whole, its reading moved to the text of the skill and the --exit-zero tests; the load in the CLI is read by a one-off Estimate of the sprint page; the defer of case 1007 retired'
```

```tasks
- [x] update `estimate-retro-loads-on-a-red-command`
- [x] read `estimate-retro-loads-on-a-red-command`
```

### Case 1072.2 — /retro loads in the Claude Code CLI

> **given:**
> `estimate-sprint-plugin-retro-loads-in-the-cli`: the new one-off check of a load of `/retro` in the CLI.
> **＋** `entity-sprint-plugin`: the live sprint page that the one-off check targets.
> **＋** `.claude/skills/retro/SKILL.md`: the skill whose load is read.
> **＋** `/work`: the skill of `.claude/skills/work/SKILL.md` that calls `/retro` at its end.
> **＋** `rule-estimates-schema`: a transcript reading stands on a one-off Estimate of the sprint page.

> **when:**
> In the Claude Code CLI, the agent calls `/retro` of `.claude/skills/retro/SKILL.md` on `PreToolUse Skill` at the end of `/work`.

> **then:**
> The skill loads, whatever `uv run --project .guppi guppi test` and `uv run --project .guppi guppi style` find.
> **＋** Its lines Tests and Style each come back with the output of its command and a last line `exit code: <n>`, and the agent takes each failing test and each style finding from them.

```then
create:
- slug: estimate-sprint-plugin-retro-loads-in-the-cli
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether /retro, called by the agent at the end of /work in the Claude Code CLI, loads whatever guppi test and guppi style find, its lines Tests and Style each ending with the line that names the exit code
  method: 'by hand, after a call of /retro by the agent at the end of /work in the Claude Code CLI: the transcript of that session under ~/.claude/projects/ read against the Criterion, the skill loaded and its lines Tests and Style each ending with the line exit code: <n>, recorded in the estimate line with the transcript named'
  once: true
  tags:
  - sprint
  - session
  - harness
```

```tasks
- [x] create `estimate-sprint-plugin-retro-loads-in-the-cli`
- [ ] read `estimate-sprint-plugin-retro-loads-in-the-cli`
```

## Case 1073 — The check of the mark at synthesis passes by the person's decision

> **context:**
> At synthesis the librarian hangs each new lesson on an Insight that shares its cause. When that Insight is already `actioned` and the lesson entry carries `addressed_by`, the mark that a Case of its own session closed its cause, `rule-synthesis` keeps the Insight `actioned` and moves `addressed_by` to the later of the two cases; an Insight born from such a lesson is set `actioned` right after its `create`; an unmarked lesson sets an `actioned` Insight `open`. `estimate-synthesis-keeps-actioned-by-the-mark` checks this, and its `method` waits for a librarian's run that puts a marked lesson under an `actioned` Insight. Its one reading, of 2026-09-27, exercised the branch of a later case alone and says that the not-later, born-Insight and unmarked branches were not exercised; case 920.3 replaced its Criterion and set it `pending` again, and case 1009 put it off at `/hi` of session 2035, since no Case of that session set when those branches are read. The brief of the librarian of session 1515 says that its run held no `lesson` entry. No code makes this judgment, so no test can run it: a Grep for `addressed_by` over `.guppi/` printed 69 hits in 12 files, and the hits of `.guppi/guppi/` that I read around their lines — `materialize.py`, `ledger.py`, `generate.py`, `lint.py`, `pages.py`, `prespec.py`, `sprint_close.py` — judge the mark of a lesson line, write it on a lesson entry, keep a Decision page that a live page names, or list the field; none compares the case of a lesson with the case of an Insight. The run the `method` waits for may not come before the close of the sprint `plugin`, which archives its `actioned` Insights, as the Purpose of `rule-synthesis` says (case 627.5).
> The person chose to set the Estimate `passed` by the person's decision, as `vault/wiki/case-schema.md` allows (case 669.16): its `update` sets `status` and `checked`, writes the Criterion back unchanged under `sections: Criterion`, and opens its `Result` with the date and the place of the decision, the last reading kept after it. `checked` is 2026-11-27, the date of the decision, as the schema sets it for a status the person's decision sets, though the session opened on 2026-11-26. The target `rule-synthesis` carries `core: true`, so `/pre-spec` judges the new `Result` by `outside` of `.guppi/guppi/pointers.py`, which I read whole: the place of the decision stands in a bracket of its own, and the decision ids of the old reading stand in code spans, which it puts aside as samples. The `update` carries `{supersedes:case 1009}` and names the page, so `generate` clears its `deferred_by` and the item leaves the backlog, as `case-schema.md` sets it for taking up a deferred decision (case 429). By the paragraph of `rule-retro` on readings, an Estimate whose `update` sets `passed` by the person's decision and writes its Criterion back unchanged is neither read nor set `failed`, so the Case has no `read` task. I read the `cascade` of `.guppi/guppi/generate.py`: a rule whose Estimates all stand `passed` turns `built`, and the other two Estimates of `rule-synthesis`, `estimate-synthesis-clusters` and `estimate-synthesis-reads-the-status-its-yaml-sets`, stand `passed`, so the rule turns `built` at the librarian's run. While it stands `draft` it does not stop `guppi ship`: `is_draft_core` of `.guppi/guppi/pages.py` accepts no page whose History holds a line that set it `built` and none of whose Estimates stands `failed`. The Criterion of `estimate-synthesis-reads-the-status-its-yaml-sets` speaks of a marked lesson too, but of an Insight that a decision entry of the same yaml sets `actioned`; the Case does not change the behaviour it checks, so that Estimate is left alone, and `estimate-synthesis-clusters` has no `purpose` and its Criterion speaks of no mark.
> A Grep for `synthesis-keeps-actioned` over `vault/wiki/` printed `backlog.md`, `brief.md`, `log.md`, `rules/rule-synthesis.md` and `estimates/estimate-clean-branch-ships-neutral-texts.md`. The line of `backlog.md` is the item of the defer that the Case takes up, and `brief.md` and `log.md` are not read. `rule-synthesis` names the page in its `estimates`, which stands. The hit in `estimate-clean-branch-ships-neutral-texts` is its `Result`, the record of a past reading of the clean version, and stands. A Grep for `synthesis-keeps|synthesis_keeps` over `.guppi/` and `.claude/` printed nothing, so no test reads this page by its name. A Grep of the session's ledger for `lesson\[error\]` and one for `\{addresses:` printed nothing, so the Case closes no lesson. I read the finished file of Case 1072 whole: it replaces the Criterion of `estimate-retro-loads-on-a-red-command` on `rule-retro` and creates `estimate-sprint-plugin-retro-loads-in-the-cli` on `entity-sprint-plugin`; it changes no page this Case changes, sets nothing at synthesis, and names this Case only as a file its check listed, so no line of either Case goes false and nothing changes here.

> **problem:**
> The check of the mark at synthesis has waited since its Criterion was last replaced for a librarian's run that may never come in this sprint, and three of its branches were never read. It needs a verdict that does not wait for that run.

> **recommend:**
> - **How the check gets its verdict**
>   - Recommended: (b) set `passed` by the person's decision, its Criterion written back unchanged, its result saying that the earlier run read one branch and that three branches were never exercised.
>   - Answer: agreed, (b).

> **given:**
> `estimate-synthesis-keeps-actioned-by-the-mark`: the check that the Case sets `passed` by the person's decision.
> **＋** `rule-synthesis`: the rule whose paragraph of the mark the check reads.
> **＋** `.claude/agents/librarian-guppi.md`: the librarian, which does the synthesis.
> **＋** `.guppi/guppi/generate.py`: the cascade, which archives the lessons of an `actioned` Insight.
> **＋** `vault/wiki/brief.md`: the brief, which reports the pair beside the synthesis.
> **＋** `decision-case-M`: the Decision that the `addressed_by` of the Insight names before the lesson joins it.

> **when:**
> The librarian, at synthesis, hangs a lesson whose entry carries `addressed_by: decision-case-N` on an existing Insight of the same pattern that stands `actioned` with `addressed_by: decision-case-M`.

> **then:**
> When case N is later than case M — compared number by number, `378.5` after `378.4` — the `update` carries `set: {addressed_by: decision-case-N}`, and `status` stays `actioned`.
> **＋** When case N is not later than M, the `update` carries no `addressed_by`: the field stays `decision-case-M`, and `status` stays `actioned`.
> **＋** Either way the `update` carries `children` plus the lesson; the lesson is `clustered`, the cascade archives it, and the brief reports the pair beside the synthesis.
> **＋** An Insight born from a marked lesson gets, right after its `create`, an `update` with `set: {status: actioned, addressed_by: decision-case-N}` (as set in case 302.2).
> **＋** A lesson with no `addressed_by` sets an `actioned` Insight `open` with `set: {status: open}`, and a new Insight is born `open`.
> **－** `addressed_by` never names two decisions.

```then
update:
- slug: estimate-synthesis-keeps-actioned-by-the-mark
  set:
    status: passed
    checked: 2026-11-27
  sections:
    Criterion: |-
      When:
      The librarian, at synthesis, hangs a lesson whose entry carries `addressed_by: decision-case-N` on an existing Insight of the same pattern that stands `actioned` with `addressed_by: decision-case-M`.

      Then:
      When case N is later than case M — compared number by number, `378.5` after `378.4` — the `update` carries `set: {addressed_by: decision-case-N}`, and `status` stays `actioned`.
      **＋** When case N is not later than M, the `update` carries no `addressed_by`: the field stays `decision-case-M`, and `status` stays `actioned`.
      **＋** Either way the `update` carries `children` plus the lesson; the lesson is `clustered`, the cascade archives it, and the brief reports the pair beside the synthesis.
      **＋** An Insight born from a marked lesson gets, right after its `create`, an `update` with `set: {status: actioned, addressed_by: decision-case-N}` (as set in case 302.2).
      **＋** A lesson with no `addressed_by` sets an `actioned` Insight `open` with `set: {status: open}`, and a new Insight is born `open`.
      **－** `addressed_by` never names two decisions.
    Result: |-
      2026-11-27, Plan Mode (the person's decision, case 1073): set passed without a new reading; the not-later, born-Insight and unmarked branches were never exercised, and a problem seen later in them comes back as a lesson.

      2026-09-27, raw/2026-09-27/1819/materialize.yaml, insight-case-show-built-case-retyped-by-hand, the archived lesson and vault/wiki/brief.md read by hand after 049458e; the lesson marked `decision-case-458` under an Insight actioned by `decision-case-452.4` gave an update with the lesson in children and addressed_by `decision-case-458`, no status, the Insight stays actioned, the lesson clustered and archived, the pair named in the Flags; the not-later, born-Insight and unmarked branches were not exercised
  change: set passed by the person's decision, its Criterion unchanged; the defer of decision-case-1009 taken up
```

```tasks
- [x] update `estimate-synthesis-keeps-actioned-by-the-mark`
```

## Case 1074 — The README explains its terms and shows the path of a decision

> **context:**
> `README.md` tells a newcomer what GUPPI is, why it exists, how a session goes, its main parts, how to install and use it, its status, how to contribute and its license. It explains none of the terms it uses, such as Case, Frontier, Spec or Estimate. It shows no example of a question the person answers, and nothing in it shows how a signed answer becomes a vault page and then a harness file. At the `/hi` of session 1336 the person confirmed the README as it stands and asked for more information in it, a diagram among it, in a Case of its own later. Case 1068 put that off on `entity-guppi-repository`, whose `code_ref` holds `README.md`, and its Problem reads that no Case of that session decides what information and which diagram `README.md` gains. This Case takes that defer up. Its update of `entity-guppi-repository` carries `{supersedes:case 1068}` and only a `change`, since no sentence of the page changes: its Purpose speaks of the rules of the repository, which this Case does not touch. The person chose the content: a section of key terms, a section on the path of one decision with a diagram of that path, and one short example question of a round. The diagram is a Mermaid block in the text of `README.md`. GitHub's page on creating diagrams (https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) says that diagram rendering is available in Markdown files, by a fenced code block with the `mermaid` language identifier. As a choice of form, the three new parts stay one Case with one Estimate, since one reading by the person judges them together. The person chose a new Estimate on `entity-guppi-repository` over a new Criterion for `estimate-sprint-plugin-readme-describes-the-project`. That Estimate targets the page of the sprint `plugin`, stands `passed` and is a done-when item of the sprint. Its Criterion stays true after this Case, since `then` removes no section that it names. The round offered the reading at the Retro of this session, and `/pre-spec` found that it cannot be taken there: the Render of `rule-retro` says that the reply that ends Retro asks the person nothing (case 569.1), and that a reading whose `method` names the person's word is a line of `## Ask the person` of `handoff.md` (case 531.1). So the `method` waits for the handoff of the session that writes the new parts, by a part that opens with `by hand, after` and names that event before a colon, which `waits_for_an_event` of `.guppi/guppi/lint.py` accepts, and the person answers at a `/hi` after it, as `estimate-sprint-plugin-readme-describes-the-project` was read. Until then `check_unread` of `.guppi/guppi/lint.py` gives the `pending` Estimate no finding, since `waits_for_a_later_moment` accepts that part. The `recommend` item of that question keeps the recommendation as it stood when the person answered it. Case 1075 of this session changes `entity-sprint-plugin`, and I read its finished file whole. It writes no note on the README wish, since this Case takes that wish up, and it changes no part of `README.md`. It moves the README line of the milestone The plugin to `## Closed`, worded as the person confirmed the README, and it leaves `estimate-sprint-plugin-readme-describes-the-project` as it stands. Nothing of this Case goes false against it. Of the four Estimates of `entity-guppi-repository`, no `purpose` speaks of the README: they check the remote on GitHub, the development project, the stops of the merge tasks and the MIT license. The page has no `core: true`. The cascade in `.guppi/guppi/generate.py` sets a page `draft` by its own Estimates, so the new `pending` Estimate sets this page `draft` until it is read. `is_draft_core` of `.guppi/guppi/pages.py` blocks the clean build only for a page with `core: true`, so this Case blocks no clean build. `README.md` does not ship in the clean version: `ROOT_FILES` of `.guppi/guppi/ship.py` lists `CLAUDE.md`, `.gitattributes` and `LICENSE` alone. A Grep for `README` over `.guppi/` printed hits only in `.guppi/tests/test_generate.py` and `.guppi/tests/test_ship.py`, both of another file named `README.md` (`.guppi/tests/README.md` and a cache file under a temporary folder), so no test and no code reads the root `README.md`. A Grep for `README` over `.claude/`, `.github/` and `plugin/` printed nothing. A Grep for `README` over `vault/wiki/` printed 7 files: `backlog.md`, `sprint.md`, `log.md`, `tags.md`, `entities/entity-sprint-plugin.md`, `entities/entity-guppi-repository.md` and `estimates/estimate-sprint-plugin-readme-describes-the-project.md`. The README line of `entity-sprint-plugin`, which Case 1075 moves from the milestone The plugin to `## Closed`, names the README on what the project is and its parts and use, and stays true. The new Estimate has a `ref`, so no vault query of `ask-guppi` ran for it. The tags `readme` and `github` stand in `tags.md`. The text follows `rule-language`: the README is in English.

> **problem:**
> `README.md` uses terms it never explains, shows no question the person answers, and does not show how a signed answer becomes an enforced rule. A newcomer cannot picture the work before installing GUPPI.

> **recommend:**
> - **What information the README gains**
>   - Recommended: (b) key terms and the path of a decision, plus one short example question of a round.
>   - Answer: agreed, (b).
> - **Which diagram the README holds**
>   - Recommended: (b) the path of one decision, from the person's answer to the rendered harness file.
>   - Answer: agreed, (b).
> - **How the diagram is drawn**
>   - Recommended: (a) a Mermaid block in the README text, which GitHub draws.
>   - Answer: agreed, (a).
> - **How the change is checked**
>   - Recommended: (a) a new Estimate on `entity-guppi-repository`, read by the person's answer at the Retro of this session.
>   - Answer: agreed, (a).

> **given:**
> `README.md`: the description of GUPPI on GitHub, which gains the new parts.
> **＋** `entity-guppi-repository`: the page of the repository, whose `code_ref` holds `README.md` and whose defer this Case takes up.
> **＋** `estimate-guppi-repository-readme-shows-the-path-of-a-decision`: the new check of the new parts of `README.md`.
> **＋** `rule-language`: the README is written in English.

> **when:**
> The person reads `README.md` at the root of the branch of the session whose Work Mode wrote its new parts.

> **then:**
> `README.md` has a section that explains the terms it uses: Case, Frontier, Spec, Estimate, ratify, vault page and librarian.
> **＋** A section says what one signed decision leaves: a line in the ledger of the session, a part of the Spec, a vault page after the librarian's run and, for a rule, the harness file rendered from it.
> **＋** That section holds a diagram of that path, from the person's answer to the harness file that the hooks enforce in the next session.
> **＋** The diagram stands in `README.md` as a fenced block tagged `mermaid`, which GitHub draws as a picture.
> **＋** A section shows one shortened question of a round: its title, what holds now, two options and the recommended answer.
> **＋** The person says that the new parts explain GUPPI to a newcomer.
> **－** No section that `README.md` holds today is removed.

```then
create:
- slug: estimate-guppi-repository-readme-shows-the-path-of-a-decision
  ref: entity-guppi-repository
  kind: QA
  purpose: Whether README.md explains the terms it uses, shows the path of one decision from the person's answer to the rendered harness file in a Mermaid diagram, and shows one short example question of a round, as the person confirms
  method: 'by hand, after the handoff of the session whose Work Mode writes the new parts of README.md: the person''s answer on README.md, read at the root of the branch of that session at a /hi after that handoff; the estimate line keeps the person''s answer'
  tags:
  - readme
  - github
update:
- slug: entity-guppi-repository
  change: README.md gains a section of key terms, the path of one decision with a Mermaid diagram of it, and one short example question of a round
```

```tasks
- [x] update `entity-guppi-repository`
- [x] create `estimate-guppi-repository-readme-shows-the-path-of-a-decision`
- [x] `README.md`: adds a section of key terms, a section on the path of one decision with its diagram in a block tagged `mermaid`, and a section with one shortened question of a round, and keeps each section it holds today.
- [ ] read `estimate-guppi-repository-readme-shows-the-path-of-a-decision`
```

## Case 1075 — The milestone The plugin keeps the merge and the close

> **context:**
> The sprint page `entity-sprint-plugin` is the plan of the sprint `plugin`. Its `## Milestones` hold the items of the work, and `guppi sprint` renders them into `vault/wiki/sprint.md`. An item whose part before ` — ` names no page is a note, which `rule-sprint` never ticks, so it keeps its milestone open until a Case removes it. The milestone The plugin holds four items: the clean version made into a Claude Code plugin, `rule-morph`, the README and the close line. Case 1021 put this milestone off because no Case said when the clean version is installed by hand, when the README is written, or when `plugin` closes. Case 1050 put it off because no Case said how the clean version becomes a plugin, how `rule-morph` is read in a new project, or when `plugin` closes. Most of that work is done. `estimate-sprint-plugin-installs-as-a-plugin` passed on 2026-11-04 in session 0358, and `estimate-sprint-plugin-readme-describes-the-project` passed on 2026-11-26 by the person's answer at `/hi` of session 1336. `rule-morph` and `rule-skill-setup` stand `built`, and both Estimates of `rule-morph` stand `passed`. So the line of `rule-morph` is now false where it says that the two pages stay `draft` until the readings in a new project. The one check of a new install that still waits is `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main`, a one-off Estimate of the sprint page, which this Case leaves as it stands.
> The person chose four things. The three finished items leave the milestone for `## Closed`, and the milestone keeps the close line. The merge line goes just before the close line, in the form that step 3 of `/sprint-open` of `rule-skill-sprint-open` sets for each new sprint where `.claude/skills/merge-main/SKILL.md` stands. That file stands here, and `/merge-main` builds no Case when the branch already holds `main` on GitHub. The person's wish for more in the README gets no note in this Case. Before the answer, the main agent told the person that Case 1074, built at the same time, takes that wish up in this session, and that the note then falls away. The person agreed to it, and chose in Case 1074 to add those parts to `README.md`. No moment is set for the close, and the person takes up the close line in a session of its own. The other option of the first question would have left the milestone with notes that `rule-sprint` never ticks, and its Purpose says that each milestone holds exactly the items whose closing closes it. The update names the page and carries `{supersedes:case 1021}` and `{supersedes:case 1050}`, so `generate` clears both defers and the item leaves `backlog.md`, as `case-schema.md` sets it for taking up a deferred decision (case 429).
> The promise is a state of the page that is checked once, so it takes a new one-off Estimate of the sprint page with `once: true`, read in the Spec at the Retro of this session. That is a choice of form. A Glob `vault/**/estimate-sprint-plugin-plugin-milestone*.md` printed nothing, so the slug is free. Of the Estimates of the page, `estimate-sprint-plugin-close-steps-run-from-the-line` quotes the close line in its `When`. The line stays word for word and stays the last item of the last milestone, and the merge line comes before the moment that this Estimate reads, so its Criterion stands. The `method` of `estimate-sprint-plugin-readme-describes-the-project` names the Work Mode that writes `README.md` under the milestone The plugin. That Estimate stands `passed`, and its `method` records a moment that has passed, so it stands. `estimate-sprint-plugin-done-counts-a-one-off-reading` reads the Purpose, which this Case leaves as it stands. The other Estimates of the page speak of other things by their `purpose`.
> A Grep `milestone The plugin|The plugin milestone|under the milestone The plugin` over `{vault/wiki,.claude,.guppi/guppi}/**` printed `entities/entity-sprint-plugin.md`, `estimates/estimate-sprint-plugin-installs-as-a-plugin.md`, `estimates/estimate-sprint-plugin-readme-describes-the-project.md` and `log.md`. The hits of the first two files are History lines, and the third is the `method` that stands as said above. A Grep `entity-sprint-plugin` over `{vault/wiki,.claude}/**` printed 29 files. I read each hit around its line outside the Estimates of the page, `log.md`, `brief.md` and `backlog.md`. Those hits stand in `entities/entity-sprint.md`, `rules/rule-guppi-config.md`, `rules/rule-morph.md`, `rules/rule-spec-box.md`, `estimates/estimate-case-build-reads-the-readers-of-a-new-files-folder.md`, `estimates/estimate-case-protocol-splits-a-transcript-reading.md`, `estimates/estimate-prespec-hook-reports-a-method-that-reads-a-transcript.md`, `estimates/estimate-spec-box-runs-a-conserved-spec.md`, `estimates/estimate-sprint-keeps-one-live-page.md` and `lessons/lesson-case-build-numbers-a-new-case-from-the-case-files-alone.md`. They name the `## Backlog` of the page, its place in `children`, a History line or a past result. None names its `## Milestones` or `## Closed`, so none goes false. I read `entities/entity-sprint.md` whole. Its Purpose says that the `## Milestones` of a sprint are its Slices in order, and that stays true. The note of the check also listed the Estimates of the page. Apart from the ones judged above, they speak of other things by their `purpose`. A Grep `entity-sprint-plugin|sprint-plugin` over `.guppi/` printed `guppi/lint.py`, `tests/test_lint.py` and `tests/test_prespec.py`. The hit in `lint.py` is a docstring example, the one in `test_lint.py` a `method` string, and `test_prespec.py` writes a page of that slug under `tmp_path`, so no test reads the live page. A Grep ``merge-main|/sprint-close`|the close of|the merge of`` over `.guppi/guppi/` printed lines in `backlog.py`, `generate.py`, `gitstate.py`, `ledger.py`, `materialize.py`, `pages.py`, `ship.py`, `sprint.py` and `sprint_close.py`, and none of them matches the text of a milestone item. Cases 1072 and 1073 of this session change other pages. Case 1072.2 adds an Estimate to the `estimates` of this page, a field this Case leaves alone. I read the finished file of Case 1074 whole. It adds to `README.md` a section of key terms, a section on the path of one decision with a Mermaid diagram, and one short example question of a round. It checks them by a new Estimate on `entity-guppi-repository`. It changes no line of `entity-sprint-plugin` and leaves `estimate-sprint-plugin-readme-describes-the-project` as it stands. So the README wish is met in this session, and neither Case needs a fix. The Grep of this session's ledger for `lesson\[error\]` and the one for `\{addresses:` printed nothing, so the Case closes no lesson.

> **problem:**
> The milestone The plugin still lists as open three items whose work is done, and one of its lines says that two pages stay unfinished, though both are built. Its two notes keep it open for good, both of its defers still stand, and it has no merge step before the close.

> **recommend:**
> - **What the Case changes on the milestone The plugin**
>   - Recommended: (a) the finished items move to Closed: the plugin that installs, the README and the setup leave the milestone for `## Closed`, the milestone keeps the close line, and both defers are retired.
>   - Answer: agreed, (a).
> - **A merge step before the close**
>   - Recommended: (a) the merge line goes just before the close line, in the form that `/sprint-open` sets.
>   - Answer: agreed, (a).
> - **Where your wish for more in the README goes**
>   - Recommended: (a) a note in the `## Backlog` of the sprint page.
>   - Answer: agreed, after the main agent said that Case 1074 takes the wish up in this session and that the note then falls away; Case 1074 adds it to `README.md`, so no note is written.
> - **When the sprint closes**
>   - Recommended: (a) no set moment: the person takes up the close line in a session of its own when the sprint is done.
>   - Answer: agreed, (a).

> **given:**
> `entity-sprint-plugin`: the live sprint page, whose milestone The plugin and `## Closed` change and whose two defers are retired.
> **＋** `estimate-sprint-plugin-plugin-milestone-holds-the-merge-and-the-close`: the new one-off check of the page.
> **＋** `rule-sprint`: a note is never ticked, and each milestone holds the items whose closing closes it.
> **＋** `rule-skill-sprint-open`: the form of the merge line and of the close line.
> **＋** `.claude/skills/merge-main/SKILL.md` and `.claude/skills/sprint-close/SKILL.md`: the skills that the merge line and the close line start.
> **＋** `estimate-sprint-plugin-close-steps-run-from-the-line`: the check that quotes the close line.
> **＋** `rule-morph`: the setup of a new project, whose line leaves the milestone.

> **when:**
> Someone reads the `## Milestones` and the `## Closed` of `entity-sprint-plugin` in the Spec, at the Retro of the session that ratified this Criterion.

> **then:**
> The milestone The plugin holds the line ``- the merge of `main` into `plugin` — `/merge-main`, a session of its own``, and after it the close line ``- the close of `plugin` — `/sprint-close`, a session of its own``, as its last item.
> **＋** The milestone holds no other item: the clean version made into a plugin, the line of `rule-morph` and the README have left it.
> **＋** `## Closed` holds, after the lines it held, a line for the clean version made into a plugin, one for the setup of a new project and one for the README.
> **－** The milestone The clean branch, the `## Backlog` and the Purpose of `entity-sprint-plugin` stay as they were.
> **－** The close line keeps the words that `estimate-sprint-plugin-close-steps-run-from-the-line` quotes.

```then
create:
- slug: estimate-sprint-plugin-plugin-milestone-holds-the-merge-and-the-close
  ref: entity-sprint-plugin
  kind: QA
  purpose: Whether the milestone The plugin of the sprint page holds the merge line and then the close line alone, and Closed holds the plugin that installs, the setup and the README; read once
  method: 'by hand, at the Retro of the session that sets this Criterion: the update of entity-sprint-plugin in the Spec read against the Criterion, recorded in the estimate line'
  once: true
  tags:
  - sprint
  - workflow
update:
- slug: entity-sprint-plugin
  replace:
  - old: |-
      - the clean version made into a Claude Code plugin
      - [[rule-morph]] — the setup Case that the first `/hi` after `/guppi:install` puts before the opening of the first sprint; the setup skill `/setup` of `rule-skill-setup`, its step in `/hi` and in `/sprint-open`, the key `setup_done` of `guppi.toml`, the pass of the ledger hook for the setup Case while no sprint is open and the clean version that ships `setup_done = false` are built by case 1017; what remains: the readings by hand of its two Estimates in a new project installed from a copy that `guppi ship --allow-draft` writes, until which `rule-morph` and `rule-skill-setup` stay `draft` and the workflow writes nothing to `prod`
      - the README on what the project is and what it is for and on its main parts and its use
    new: '- the merge of `main` into `plugin` — `/merge-main`, a session of its own'
  - old: '- The name of the main branch: a project whose main branch is not main sets its name at the setup, and the code and the skills read it (case 1070)'
    new: |-
      - The name of the main branch: a project whose main branch is not main sets its name at the setup, and the code and the skills read it (case 1070)
      - The clean version made into a Claude Code plugin: written into a local folder by `guppi ship --allow-draft`, it installs into an empty project, `/guppi:install` copies GUPPI there and `/hi` runs there (case 1075)
      - The setup of a new project: `rule-morph` and `rule-skill-setup` built, the setup Case at the first `/hi` after `/guppi:install` before the first sprint (case 1075)
      - The README on what the project is and what it is for and on its main parts and its use, as the person confirmed it (case 1075)
  change: 'taken up: the finished items of the milestone The plugin leave for Closed, the merge line stands before the close line; the defers of decision-case-1021 and decision-case-1050 retired'
```

```tasks
- [x] update `entity-sprint-plugin`
- [x] create `estimate-sprint-plugin-plugin-milestone-holds-the-merge-and-the-close`
- [x] `uv run --project .guppi guppi sprint`
- [x] read `estimate-sprint-plugin-plugin-milestone-holds-the-merge-and-the-close`
```
