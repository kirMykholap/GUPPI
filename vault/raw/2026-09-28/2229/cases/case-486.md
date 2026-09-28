## Case 486 — The Retro skeleton closes its code block on its own line

> **context:**
> The Retro skill ends with a sample of the report in a code block. In Markdown a code block closes only on a line that holds the closing backticks and nothing else. Here the next sentence, "When the person approves, commit … then call `/handoff`", stands on that same line after the backticks. So the block never closes, and the commit-and-handoff step reads as part of the sample. The break is in the Render of `rule-retro` (page line 73) and in `.claude/skills/retro/SKILL.md` (line 47), which is rendered from it. It came from the third `replace` pair of case 483. That pair's `new` ended on the closing fence as a YAML `|-` value, and the text after its anchor, in the same paragraph, joined that line. The librarian's run of 2026-09-28 found it, and the brief flags it.
> The person chose to fix the text only, in its ratified order, with no new Estimate. The fix is one `replace` pair. Its anchor "``` When the person approves, commit (" occurs once in the Render section. Its `new` closes the fence on its own line, then leaves a blank line before the sentence, whose words stay as they are. No reader changes and no code changes. The page and the skill file change together at the librarian's run: `generate` writes the page, then `guppi render` writes the file. The hook refuses a hand edit of the file, so the Retro of this session still reads the old line. This Case creates no page, so no vault query was run.
> The frame holds no contradiction. `estimate-retro-red-in-the-baseline-is-not-charged` quotes the commit condition, but its words and meaning stay the same. `estimate-retro-report-holds-each-fact-once` stays `pending` from case 483, and its reading by hand at the first `/retro` after the render looks at the report. `estimate-retro-loads` and `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` speak of readings and red checks. No Criterion speaks of the layout of the skill, so no Estimate is touched.
> Not done here: a guard that catches such a break before the librarian's run. That is the Frontier item C6, which the person raised. There, a `/pre-spec` check of the simulated pairs and a run of `materialize` and `generate` in Work Mode can be weighed together.

> **problem:**
> The closing fence of the report skeleton in `rule-retro` and in its rendered skill carries the next sentence on its line. The code block does not close, so the last step of Retro, the commit and the handoff, reads as part of the sample report.

> **recommend:**
> Replace the joined line with the fence alone on its line, a blank line, and the sentence unchanged after it. This keeps the order and the words that case 483 ratified. Moving the commit sentence before the skeleton was rejected, because it changes the ratified order for no gain.

> **given:**
> `rule-retro` — its Render: the closing fence of the report skeleton and the sentence after it
> **＋** `.claude/skills/retro/SKILL.md` — the skill rendered from `rule-retro`

> **when:**
> The agent loads `.claude/skills/retro/SKILL.md` at `/retro` and reads the form of the report.

> **then:**
> The skeleton of the report is a code block that closes on a line that holds the fence alone.
> **＋** The sentence on the commit and the handoff stands after the block as its own paragraph, with its words unchanged.
> **－** The text of the skeleton and of that sentence does not change.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: ```` ``` When the person approves, commit ( ````
>   - new:
>     ````
>     ```
>
>     When the person approves, commit (
>     ````
>   - change: `the closing fence of the report skeleton stands alone on its line, and the commit sentence follows as its own paragraph (case 486)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`

> **ratification:**
> ```
> - decision[case 486][update][rule-retro]{ref:rule-retro}
> ```
