## Case 470 — `estimate-skill-grill-me-asks-in-rounds` is read on a round of `case-guppi` too

> **context:**
> `.claude/skills/grill-me/SKILL.md` is the text of `rule-skill-grill-me`. It reaches an agent in two ways: the person types `/grill-me`, or `case-guppi` loads it through `skills: [grill-me]` and asks the rounds of Plan Mode with it. The `When` of `estimate-skill-grill-me-asks-in-rounds` names only the person's typed command. So no round of `case-guppi` counts toward a reading. The handoff of session 2050 counts 14 such rounds in that session. The person seldom types `/grill-me`, so the reading may never come and `rule-skill-grill-me` stays in `draft`.
> In the round, the person chose to widen the trigger to both paths. For `case-guppi`, the instructions that started the grill name the confirmation: the showing of the Case and its ratification (`rule-case-build`). The line on confirmation therefore holds as written. The `－` line on dispatching a sub-agent stays true on both paths.
> At pre-spec, `ask-guppi` found that the new `When` would sign the form of a round of `case-guppi` twice. `estimate-case-build-writes-the-case` already signs "a round of questions in the form of `.claude/skills/grill-me/SKILL.md`", so one bad round would fail two Estimates. The person agreed to this fix: the form line reads only the person's `/grill-me`. On a round of `case-guppi`, this Estimate reads the frontier rule, finding facts and the confirmation, and a `－` line leaves the form to `estimate-case-build-writes-the-case`. That Estimate's Criterion is not touched.
> This Case does not fix the two rounds that broke the frontier rule, in 465 and in the fourth round of 467. That fix is a separate promise on `rule-case-build`. Under this Case, a round that breaks the rule again counts as a `failed` reading of this Estimate. The Context of case 466 says this Estimate does not change. It stands in the Spec of session 2050 and on the live pages `decision-case-466.1` and `decision-case-466.2`. A Decision page records what held when it was written, so that sentence does not become false. The Purpose of `rule-skill-grill-me` still holds. The Case has no `create`, so no vault query ran.

> **problem:**
> The promise of the grill-me skill can be read only on a command the person seldom types. The path where the skill is actually used, the rounds of `case-guppi`, gives no reading. The Estimate may stay `pending`, and its rule `draft`, with no end.

> **recommend:**
> Replace the Criterion of `estimate-skill-grill-me-asks-in-rounds` whole. The `When` names both the person's `/grill-me` and a round of `case-guppi`. The form of a question is read only on the person's `/grill-me`, because `estimate-case-build-writes-the-case` already signs the form of a round of `case-guppi`. The `method` becomes a round read on either path. This reads the promise of the skill where the skill is used, and nothing is signed twice. The rejected option was to narrow the Estimate to `render --check` alone, because that drops the frontier rule from every Estimate, and the frontier rule is the rule the two rounds broke.

> **given:**
> `estimate-skill-grill-me-asks-in-rounds` — the promise of the skill, its Criterion replaced whole and its method changed
> **＋** `rule-skill-grill-me` — the rule the Estimate reads, unchanged
> **＋** `.claude/skills/grill-me/SKILL.md` — the skill text both paths load
> **＋** `.claude/agents/case-guppi.md` — the agent that loads the skill by its `skills` field and names the confirmation of its rounds
> **＋** `estimate-case-build-writes-the-case` — the promise of the form of a round of `case-guppi`, unchanged

> **when:**
> The person types `/grill-me` on `UserPromptSubmit`, or `case-guppi` answers with a round of questions, with `.claude/skills/grill-me/SKILL.md` loaded by `skills: [grill-me]` in `.claude/agents/case-guppi.md`, after `uv run guppi render` wrote `.claude/skills/grill-me/SKILL.md` from `rule-skill-grill-me`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/grill-me/SKILL.md` equals the Render of `rule-skill-grill-me`.
> **＋** The agent asks in rounds: each round holds every question whose prerequisites are settled, and the agent waits for the answers before the next round.
> **＋** On the person's `/grill-me`, each question is numbered, with a title, a body and a recommended answer.
> **＋** A fact the agent can look up it finds itself, or by a sub-agent when it can dispatch one; the person is asked only for decisions.
> **＋** The agent acts on the grill only after the shared understanding is confirmed, by the person's word unless the instructions that started the grill name another confirmation.
> **－** The form of a round of `case-guppi` is not read here: it is the promise of `estimate-case-build-writes-the-case`.
> **－** No sentence of `.claude/skills/grill-me/SKILL.md` requires the agent to dispatch a sub-agent.

> **tasks:**
> - [ ] update `estimate-skill-grill-me-asks-in-rounds`
>   - set: `{status: pending, method: "uv run guppi render --check; by hand, one round read in the chat in a session after the render, of the person's /grill-me or of case-guppi"}`
>   - change: `the Criterion replaced whole — a round of case-guppi reads the frontier rule, finding facts and the confirmation; the form of its questions stays with estimate-case-build-writes-the-case (case 470)`
> - [ ] read `estimate-skill-grill-me-asks-in-rounds` — `uv run guppi render --check`; by hand, one round of the person's `/grill-me` or of `case-guppi` in a session after this one

> **ratification:**
> ```
> - decision[case 470][update][estimate-skill-grill-me-asks-in-rounds]{ref:estimate-skill-grill-me-asks-in-rounds}
> ```
