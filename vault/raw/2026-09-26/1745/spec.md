<!-- approved 22:28:06 · session 71cd373f -->

# Spec — session 1745, 2026-09-26

## Case 439 — /hi: ratify after the fact the allowed-tools of its `!` commands

> **context:**
> `/hi` runs six `!` substitutions before the first turn of the agent, and their output is in the context with no read calls. Since client 2.1.282 in VS Code, the server-side classifier of auto mode checks each substitution. It gives no verdict for a substitution the person typed. The full reason was printed once, in session 1b191eaf: "the request that produced this action did not ask for one". So `/hi` failed at every run, and a fresh `/login` did not help. Commit 54509ed was made with the owner's consent but with no Case. It added an `allowed-tools` line with the six commands to the frontmatter of the Render of `rule-skill-hi`, and one sentence on the cause to `## How it works`. `uv run guppi render` rewrote `.claude/skills/hi/SKILL.md`. `render --check` exited 0, pytest passed, the lint output did not change, and after that `/hi` in this session ran whole. The change has no History line and no Decision.
> An `update` that has only `change` applies: `ITEM_KEYS["update"]` of `guppi/materialize.py` holds `change`, and `guppi/generate.py`, which imports it, writes the History line `updated: <change>` with a link to `decision-case-439`. A `replace` pair would fail here, because its `old` is no longer on the page. `sections` would rewrite whole sections for one line.
> The other pages and why they stay as they are:
> - The Pattern of `insight-hi-skill-substitution-checked-by-a-model-call` names a lapsed login as the cause. Its Proposal says "not an allow entry for the command", and the new cause refutes both. But that Proposal was rejected by Case 246. An Insight changes only by an `update` that actions or rejects it, and this Case makes none, so it stays as it is. The new cause goes into a lesson line in the ratification, and the librarian of the next run links it to this Insight.
> - `rule-permissions` allows only the working files of the session in `.claude/settings.json`. The change does not touch its list. The `allowed-tools` of the skill holds only while `/hi` runs, and only the person opens `/hi` (`disable-model-invocation: true`). Two of the six commands write files — `git pull --ff-only` the working tree, `uv run guppi render --sync` the governed files — and the owner allowed them for `/hi`; the `SessionStart` hook runs the same `render --sync` with no permission check. The Criterion of `estimate-permissions` speaks only of the `allow` list in `settings.json`.
> - The Criterion of `estimate-hi-no-read-calls` promises the context after `/hi` with no read calls. The change brings this behaviour back but does not change the promise. The Criterion of `estimate-hi-writes-frontier` speaks of the Frontier. No Estimate is touched.
> - The Case has no `create`, so no vault query is needed.

> **problem:**
> The change of `rule-skill-hi` and its Render already stand in the vault and in `.claude/skills/hi/SKILL.md`, but no Decision signed them. The question: ratify them after the fact as they stand, so that the History of the page gets a line with a link to the Decision.

> **given:**
> `rule-skill-hi` — the rule whose Render frontmatter and `## How it works` carry the change
> **＋** `.claude/skills/hi/SKILL.md` — the skill file rendered from `rule-skill-hi`
> **＋** `rule-permissions` — the rule of the allow list in `.claude/settings.json`

> **when:**
> The person types `/hi` in Claude Code 2.1.282 or later.
> **＋** A reader opens `rule-skill-hi`.

> **then:**
> The six `!` commands of `.claude/skills/hi/SKILL.md` — `git pull --ff-only`, `uv run guppi render --sync`, `git branch --show-current`, `git status --short`, `gh issue list`, `uv run guppi tail` — match the `allowed-tools` line of its frontmatter, run with no classifier verdict, and their output is in the context before the first turn.
> **＋** `## How it works` of `rule-skill-hi` says why: the server-side classifier gives no verdict for a `!` substitution the person types, and a matching rule needs no classifier.
> **－** The allow list of `.claude/settings.json`, rendered from `rule-permissions`, gets no entry for these commands.

```then
update:
- slug: rule-skill-hi
  change: the allowed-tools line of the Render frontmatter allows the six ! commands of /hi; the server-side classifier of client 2.1.282 gives no verdict for a substitution the person types (commit 54509ed)
```

```tasks
- [ ] update `rule-skill-hi`
- [x] `uv run guppi render --check` exits 0: `.claude/skills/hi/SKILL.md` equals the Render
```

## Case 440 — remove the keys of the shape before case 189: `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule or an entity

> **context:**
> Case 72 brought in the key `contract: same|changed`. On the flag `changed`, the script `materialize` found the Estimate of the rule by itself. It appended a `### case N` block to its Criterion and set it `pending`. `estimate_slug` corrected the slug of the Estimate the script derived, when it matched a live page. `estimate_kind` gave the derived Estimate its `kind`. `method` on a `create` of a Leaf rule was the signal to derive an Estimate. Case 189 removed all derivation: an Estimate has its own line and its own item, and its Criterion is the `when` and `then` of the Case. Case 194.1 left the old keys with no effect, so that old Specs lift with no `unknown`.
>
> Today nothing reads these keys. On a `create` of a rule or an entity, `materialize` drops them silently through `IGNORED_KEYS`, and `item_keys` lets them pass. On a `create` of an Estimate, `estimate_kind` and `estimate_slug` are removed. On an `update` they are not in the closed list `ITEM_KEYS`, and pre-spec gives a finding (case 436.2). They carry no function that does not exist elsewhere. A search of `vault/raw/` found no item line with these keys, and `materialize` reads only `raw/`. The pass of case 194.1 protects nothing any more.
>
> The Case takes all four keys. `method` goes only as a key of a rule or an entity: `case-schema.md` already says that a `create` of a rule or an entity carries none. On an Estimate, `method` is a field of the schema, and it stays. The keys `criterion` and `context` on a `create` of an Estimate and the nested `estimate` are not in the Case. They are other shapes (cases 193, 194.1), and a separate question. The line `contract: changed` in the unmigrated Criterion of `estimate-render-harness-reproduces` is the text of a past Case. It stays until that page is recut (case 202). The words "no `contract` line" in `estimate-case-protocol-case-form` speak of a `tasks` line, not of an item key, and they stay too.
>
> What changes after the removal. On a `create` of a rule or an entity these keys become `unknown` in `materialize`. The Spec hook refuses them. Pre-spec gives a finding. All three go by one `item_keys`. The Criteria of `estimate-prespec-checks-the-form-of-an-item` and `estimate-spec-write-copies-the-ratified-case` speak of this in general terms, and they stay. So `rule-prespec`, deferred by Case 438, is not touched. For a category whose schema the same session changes (case 308.2), such a key now reaches `fields`, like any foreign key. Today `IGNORED_KEYS` removes it there too. The Criterion of `estimate-materialize-lifts-unfiltered-on-a-schema-change` ("every key into `fields`") agrees with this and stays.
>
> Two Estimates of `rule-materialize` become false. `estimate-materialize-lifts-a-create-by-the-schema` lists these keys among the own keys of a `create`. The `－` line of `estimate-materialize-assembles` says they do not reach `unknown`. These are two promises, so two sub-cases. The Render of `rule-case-protocol` names the keys in two sentences, and that is the third sub-case. It changes no promise: the Estimates of `rule-case-protocol` speak of the loading of the file and of the form of a Case, not of item keys. No vault query is needed: the Case creates nothing.

> **problem:**
> The keys `contract`, `estimate_slug`, `estimate_kind` and `method` on a rule or an entity are left from the shape before case 189. Today nothing reads them, but the code, the docstrings, the tests and the pages name them and let them pass silently. Decide how to remove them whole: from the judgment `item_keys`, from the lift of `materialize`, from the Estimates that promise their pass, and from the Render of `case-schema.md`.

### Case 440.1 — a foreign key of a `create`: the old keys are no own keys any more

> **given:**
> `estimate-materialize-lifts-a-create-by-the-schema` — the promise on the lift of a `create` by the schema
> **＋** `guppi/materialize.py` — `IGNORED_KEYS`, `accepted_keys`, `item_keys`, `_lift_item` and the module docstring
> **＋** `guppi/prespec.py` — the docstrings of the module and of `check_form`
> **＋** `tests/test_materialize.py` — the tests of the lift by the schema and of `item_keys`
> **＋** `tests/test_prespec.py` — the test of the keys of the shape before case 189
> **＋** `tests/test_gate.py` — its plan fixture
> **＋** `vault/wiki/<category>/schema.yaml` — the fields of a category
> **＋** `rule-<category>-schema` — the rule of a category's schema

> **when:**
> `uv run guppi materialize` lifts a `create` or `defer` item whose category has its `vault/wiki/<category>/schema.yaml` on disk, in a unit that neither creates nor updates `rule-<category>-schema`.

> **then:**
> Only the keys the category's `schema.yaml` names as fields reach `fields` of the entry; `ref` goes to the entry, `sections` to its own key.
> **＋** A key that is no field of the schema and none of the item's own keys — `slug`, `ref`, `sections`, `file`, `estimate`, `parent_create`, `parent_tags` — is named under `unknown` on the entry, printed by `--show`, never written to the page, and the entry applies.
> **＋** The `type` and `purpose` of a `defer` are its own keys and reach `fields` whatever the category of its target; a `defer` without `purpose` is `incomplete: [purpose]`.

```then
update:
- slug: estimate-materialize-lifts-a-create-by-the-schema
  set:
    status: pending
  change: the Criterion replaced whole — the keys of the shape before case 189 are no own keys of a create (case 440.1)
```

```tasks
- [ ] update `estimate-materialize-lifts-a-create-by-the-schema`: the Criterion replaced whole
- [x] `guppi/materialize.py`: remove `IGNORED_KEYS`, its skip in `_lift_item` and in `accepted_keys` with the parameter `estimate`, the pops of `estimate_kind` and `estimate_slug` on an Estimate `create`, and the sentence on these keys in the module docstring
- [x] `guppi/prespec.py`: remove the sentence on the keys of the shape before case 189 from the module docstring and from the docstring of `check_form`
- [x] `tests/test_materialize.py`: `test_the_keys_of_the_old_shape_stay_ignored_and_never_unknown` becomes a test that `contract` and `method` on a rule's `create` are named under `unknown`; `test_item_keys_answers_for_each_kind_as_the_lift_does` asserts `method` and `contract` are not keys of a rule's `create`
- [x] `tests/test_prespec.py`: `test_the_keys_of_the_old_shape_are_not_read` becomes a test that `contract` on an `update` and `estimate_slug` on a rule's `create` are each the finding `key <key> is not a key of this item`
- [x] `tests/test_gate.py`: remove `contract: same` from `PLAN`
- [x] `uv run pytest tests/test_materialize.py tests/test_prespec.py tests/test_gate.py`
- [ ] read `estimate-materialize-lifts-a-create-by-the-schema`
```

### Case 440.2 — the yaml assembly: the `－` line on the old keys goes

> **given:**
> `estimate-materialize-assembles` — the promise on the entries of `materialize.yaml`
> **＋** `rule-materialize` — no Estimate is derived from a flag
> **＋** `guppi/materialize.py` — the lift of the entries
> **＋** `tests/test_materialize.py` — the fixtures of Cases 11 to 15 and their tests

> **when:**
> `uv run guppi materialize` lifts the record lines of a unit's `ledger.md` against the `then` blocks of its `spec.md`.

> **then:**
> `materialize.yaml` holds one entry per record line, in ledger order: `case`, `kind`, `category` from the slug prefix, `slug`, `ref`, `source`, `supersedes`, `tags`, `addresses`, `origin`, `line`, `text`, `decision`; from the `then` item found by its slug — `fields`, `sections`, `replace`, `reword`, `change`, `rename`, `impact`; what the block lacks is `incomplete`, never invented.
> **＋** `reword` is carried as a list of `{old, new}` pairs; a mapping or a scalar under it is `incomplete: [reword]`.
> **＋** An Estimate has its own line and its own entry, the `ref` of the line the Estimate itself; the entry of its `create` keeps `kind`, `purpose`, `method` and `tags` as fields.
> **＋** One decision record per Case: `decision`, `case_text`, `targets`; a sub-case reads a missing `context`, `problem`, `recommend` and `given` from its parent, never `when`.
> **＋** An `estimate` line whose slug has a `create` in the same unit is folded into it; one for a page of an earlier unit is an `estimate` entry of its own.
> **＋** The `new_tags` of any Case reach the yaml once each; an existing `materialize.yaml` is extended with the lines it does not hold, never rewritten.
> **＋** A line the grammar does not parse goes under `unparsed`, and the run goes on.
> **－** No entry of an Estimate is derived from a key of the item of a rule or an entity: an Estimate comes only from its own line.

```then
update:
- slug: estimate-materialize-assembles
  set:
    status: pending
  change: the Criterion replaced whole — the line on the keys of the shape before case 189 gives way to the line that no Estimate is derived from a key (case 440.2)
```

```tasks
- [ ] update `estimate-materialize-assembles`: the Criterion replaced whole
- [x] `tests/test_materialize.py`: the fixtures of Cases 12 to 14 lose `contract`, `estimate_slug` and `method` on their `update` items; `test_a_create_with_the_old_method_key_yields_no_estimate_and_keeps_the_key_off` and `test_an_update_with_the_old_contract_keys_yields_one_entry_without_them` assert the keys of Cases 11 and 15 under `unknown` and no Estimate entry derived
- [x] `uv run pytest tests/test_materialize.py`
- [ ] read `estimate-materialize-assembles`
```

### Case 440.3 — `case-schema.md` no longer names the old keys

> **given:**
> `rule-case-protocol` — its Render says what an item of a `then` block carries
> **＋** `vault/wiki/case-schema.md` — the Render of `rule-case-protocol`

> **when:**
> Someone reads `vault/wiki/case-schema.md`.

> **then:**
> The page says what a `create` and an `update` carry and names no key of the shape before case 189.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: A `create` of a rule or an entity carries no `method`, `estimate_kind` or `estimate_slug`; nothing is derived from it. A rule with several promises
    new: A rule with several promises
  - old: case 258.1); it carries no `contract`.
    new: case 258.1).
  change: the Render names no key of the shape before case 189 (case 440.3)
```

```tasks
- [ ] update `rule-case-protocol`: the Render drops the two sentences on the keys of the shape before case 189
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
```

## Case 441 — case-guppi writes the Case in English, and the Spec is written from that answer, spec.md included

> **context:**
> Today `case-guppi` builds a Case with its name, `context`, `problem` and `recommend` in Russian and its `given`, `when`, `then` and `tasks` in English. The main agent shows the answer unchanged. On `Stop`, `uv run guppi casecheck` compares the whole showing, heading and prose included, line by line with the answer stored in `<plan>.checked.json`. After the reply that carries the ledger lines, the `Stop` hook of `rule-spec-write` writes the stored answer into the plan file and into `<plan>.ratified.md`. Before the approval the agent translates the name, `context` and `problem` in the plan by hand. The `/pre-spec` check refuses a Cyrillic letter there, and a prose-only change is shown as a `DIFF` with no ratification (cases 373, 387). At `ExitPlanMode`, `guppi spec` appends the plan once to `raw/<hi date>/<hi HHMM>/spec.md`.
>
> This goes wrong in three places. First, a hand-made translation does not last. The hook writes from the store, so a Case rebuilt after its translation puts Russian prose back into the plan. The deferred decision on `rule-prespec` (case 438) describes this: a pre-spec finding in the body of a Case goes to its `case-guppi` and a new ratification, prose is fixed in the plan as a `DIFF`, and the translation is the last step. Second, a Case ratified after the approval reaches only the plan and its copy, never `spec.md`, and the scripts read `spec.md`. In session 1337, the sections of Cases 434 and 436.4 there were replaced by hand from the plan, with the person's consent. Third, a Case superseded in its own session must leave the Spec. The hook only replaces or inserts sections, so today the agent removes the Case by hand, and `/pre-spec` reports one still in the plan (case 299.2).
>
> The person chose this scheme:
> - `case-guppi` writes the whole Case in English.
> - The main agent translates the name, `context`, `problem` and `recommend` into Russian for the chat and shows the rest as the answer holds it.
> - The main agent writes a short-form defer in English in the chat.
> - The `Stop` comparison reads only `given`, `when`, `then`, `tasks` and `ratification`.
> - The Spec hook writes the English answer into the plan, into its copy and, once it stands, into `spec.md`. There it replaces the sections of a Case or places a new one, and keeps the ticks of unchanged task lines.
> - The Spec hook removes a Case that a `{supersedes:case N}` line of the reply supersedes.
> - The translation step and the prose `DIFF` go.
> - A changed ratified Case, in its prose or its body, goes to its `case-guppi`, is shown again whole and is ratified again. The hook writes only a stored answer after a reply with the Case's lines, so a hand edit of the plan would be overwritten.
> - The Cyrillic check of `/pre-spec` stays as a safety net.
>
> State of the pages. `rule-case-build` and its Render say the main agent shows the answer unchanged. `rule-case-check` compares the whole showing. `vault/wiki/case-schema.md`, the Render of `rule-case-protocol`, says the prose is Russian in the chat and translated in the Spec. It keeps a reduced re-showing of a ratified Case and the prose `DIFF`, and it leaves the removal of a superseded Case to the agent. `rule-prespec` tells the agent to translate before the run and to fix a wrong fact in the plan as prose. `rule-spec-write` states its purpose as "the words the person signed" and skips a Case whose last mention is a `DIFF`. `rule-spec-capture` names the agent as the writer of `## Deferred` in `spec.md`, which has been out of date since the hook took over the defer. Its Estimate `estimate-spec-capture-appends` keeps that writer in its Criterion. `rule-prespec` carries `deferred_by` case 438; sub-case 441.4 takes it up and supersedes it. Case 440.3 of this session also changes `rule-case-protocol`, and its anchors differ from the ones used here.
>
> The vault's answer. The two `create` items are Estimates with a `ref`. Their slugs, `estimate-spec-write-reaches-the-approved-spec` and `estimate-spec-write-removes-a-superseded-case`, are free: a Glob over `vault/` finds neither.
>
> Findings in the frame, and why each stands:
> - Without the prose `DIFF`, the `DIFF` skip of the Spec hook has no use left. It would also silently skip a re-ratification whose last mention is a code diff naming the Case. Sub-cases 441.8 and 441.9 remove it and the lines of the two Estimates that name it.
> - The `DIFF` exception of the `Stop` comparison stays in 441.3. A fence tagged `DIFF` is never the showing of a Case, and a diff of code or of a page that quotes a Case must not be compared.
> - `estimate-prespec-catches-a-superseded-case` stays true. A superseded Case still in the plan remains a finding, now a net behind the removal by the hook.
> - `estimate-case-protocol-defers-in-one-reply` stays true. It says nothing of the language, and the agent still writes nothing of the defer into a file.
> - The `## Language` section of `CLAUDE.md` (`rule-language`) and `estimate-language-followed` say that the name, `context` and `problem` "are translated into English in the Spec before its approval". The result still holds; only the step is gone. The person keeps them as they are, and the smallest wording, if they are ever changed, is "are Russian in the chat and English in the Spec".
> - The Purpose of `rule-spec-reconcile` gives the Russian prose of the ratified copy as its reason. The `when` of `estimate-spec-reconcile-shows-a-changed-case`, "the agent edits the plan file", no longer happens. Both stand because the page is deferred by case 423, whose question of a guard on the agent's edits of the plan the person has not decided.
> - `insight-case-show-built-case-retyped-by-hand` is not actioned. The main agent still writes the showing out, and the retyped lines it records stay compared parts.
> - `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-protocol-case-form`, `estimate-case-protocol-loaded`, `estimate-case-protocol-acknowledging-reply`, `estimate-spec-write-writes-a-defer` and `estimate-spec-capture-offers-the-fork` speak of nothing this Case changes.

> **problem:**
> The prose of a Case is written in Russian and translated by hand in the plan, and a later write from the stored answer undoes that translation. A Case ratified after the approval never reaches `spec.md`. A superseded Case leaves the Spec only by hand. Decide how the rules that build, show, check, pre-spec and write a Case take up the person's scheme, so that no hand edit of the plan or of `spec.md` is needed.

### Case 441.1 — case-guppi answers with the whole Case in English

> **given:**
> `rule-case-build` — the rule of `case-guppi`; its Purpose and its Render
> **＋** `estimate-case-build-writes-the-case` — the promise of the answer of `case-guppi`
> **＋** `.claude/agents/case-guppi.md` — the agent file rendered from `rule-case-build`
> **＋** `vault/wiki/case-schema.md` — the form and the language of the answer
> **＋** `.claude/agents/ask-guppi.md` — the vault query `case-guppi` runs itself
> **＋** `.claude/settings.json` — the hooks registered on each event

> **when:**
> The main agent dispatches `case-guppi` with a Case id, a Frontier item and its source, and the person's words on it; or sends it the person's question or change by `SendMessage`.

> **then:**
> `case-guppi` reads `vault/wiki/case-schema.md` whole before it writes the Case.
> **＋** Before a `create` without a `ref`, it runs the vault query of `.claude/agents/ask-guppi.md` itself, and the `context` of the Case gives the answer.
> **＋** It reads each page and file the `given` of the Case names, the Criterion of each Estimate such a page lists, and, for a Case that adds or changes a hook, the hooks on the same event in `.claude/settings.json`.
> **＋** Each contradiction it finds is fixed in the Case, or the `context` says why it stands.
> **＋** Its answer is the Case whole in English — the name, `context`, `problem` and `recommend` too — in the chat form of `vault/wiki/case-schema.md`, from the heading to the fence of `ratification`, and nothing else; asked again, it answers with the Case whole again, in English.
> **＋** An answer that needs a choice the person has not made is that question alone, with no Case heading.
> **＋** It runs on `model: opus` with `effort: medium` and the tools Read, Grep and Glob.
> **－** It writes no file and no ledger line.

```then
update:
- slug: rule-case-build
  replace:
  - old: the main agent shows it unchanged ([[rule-case-protocol]]), and the hooks of `rule-case-check` check it before the showing and compare the showing with it.
    new: the main agent shows it with its name, `context`, `problem` and `recommend` translated into Russian and the rest unchanged ([[rule-case-protocol]]), and the hooks of `rule-case-check` check it before the showing and compare the showing with it in all but that prose (case 441).
  - old: You build one Case of Plan Mode. The main agent shows your answer to the person unchanged, and the person ratifies it.
    new: You build one Case of Plan Mode. Write it whole in English — its name, `context`, `problem` and `recommend` too — since the Spec is written from your answer; the main agent shows it to the person with that prose translated into Russian and the rest unchanged, and the person ratifies it.
  change: case-guppi writes the whole Case in English; the main agent translates its prose for the chat (case 441.1)
- slug: estimate-case-build-writes-the-case
  set:
    status: pending
  change: the Criterion replaced whole — the answer is the whole Case in English (case 441.1)
```

```tasks
- [ ] update `rule-case-build`
- [ ] update `estimate-case-build-writes-the-case`
- [ ] `uv run guppi render`: `.claude/agents/case-guppi.md`
- [ ] read `estimate-case-build-writes-the-case`
```

### Case 441.2 — the main agent translates the prose for the chat; a changed Case goes back to case-guppi and is shown whole

> **given:**
> `rule-case-protocol` — its Render says how a Case is shown, changed and written
> **＋** `estimate-case-protocol-shows-the-built-case` — the promise of the showing of a built Case
> **＋** `vault/wiki/case-schema.md` — the Render of `rule-case-protocol`
> **＋** `rule-spec-write` — the hook that writes a Case from its stored answer
> **＋** `rule-spec-reconcile` — the comparison of an edited plan with its ratified copy

> **when:**
> The main agent takes up a Frontier item that needs a Case, the person answers a shown Case with a question or a change, or a ratified Case changes and is shown again, in Plan Mode or in Work Mode.

> **then:**
> The main agent dispatches `case-guppi` with the Case id, the Frontier item and its source, and the person's words on it, in the prompt of the call; nothing of the Case stands in the chat before the answer.
> **＋** A question or a change of the person on a shown Case goes to the same `case-guppi` by `SendMessage`.
> **＋** The main agent shows the Case of the answer whole, at its first showing and at every showing again — its name, `context`, `problem` and `recommend` translated into Russian, its `given`, `when`, `then`, `tasks` and `ratification` as the answer holds them — and that is the Case the person answers; its own text stands after one horizontal rule.
> **＋** A showing that the `Stop` comparison of `uv run guppi casecheck` refuses is followed, before the person answers, by a reply that shows the answer whole, translated the same way.
> **＋** A ratified Case that changes — in its prose or in its body — changes through its `case-guppi`, and its new answer is shown and ratified again; the main agent edits no Case in the plan file.
> **＋** An answer that holds no Case heading is a question the main agent puts to the person, and no Case is shown.
> **＋** The plan file stands with its title line before the first dispatch of the session.
> **＋** The main agent dispatches `ask-guppi` once, at pre-spec, and neither `ask-guppi` nor `frame-guppi` before a showing.
> **－** A deferred decision in the short form is written by the main agent in English in the chat, with no dispatch.

```then
update:
- slug: rule-case-protocol
  replace:
  - old: 'A ratified Case is, in Plan Mode, changed in the plan file first, and `rule-spec-reconcile` compares it with the ratified copy: when its `given`, `when`, `then`, `then` block or `tasks` changed, it is shown again — `context` and `problem` if they changed, always `given`, `when`, `then`, `tasks` and `ratification`, and no `recommend` (cases 62, 163); until it is ratified again, nothing of the change is acted on. When only its name, `context` or `problem` changed, the reply shows the change as a `DIFF` of the edit and asks for no ratification; the translation of the name, `context` and `problem` before the approval is no change and is not shown (cases 373, 387.3). In Work Mode a changed Case is shown again whole.'
    new: A ratified Case changes through its `case-guppi`, in its prose as in its body; the agent does not edit a Case in the plan file, and `rule-spec-reconcile` names an edit of the plan that changes what the scripts apply. Its new answer is shown again whole, in Plan Mode as in Work Mode, and ratified again, since the hook of `rule-spec-write` writes a Case only from its stored answer after a reply that carries its lines; until then nothing of the change is acted on (cases 438, 441).
  - old: 'Russian in the chat with the owner for the name of a Case, its `context`, `problem` and `recommend`, and the agent''s own text; `given`, `when`, `then` and `tasks` — lines and sub-points — are English in the chat already, the words the vault will hold (case 387.1). English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the name, `context` and `problem` are translated in the Spec before its approval, slugs, field names and ledger lines unchanged (cases 123, 387.1).'
    new: '`case-guppi` writes the whole Case in English (case 441). Russian in the chat with the owner for the name of a Case it built, its `context`, `problem` and `recommend` — the main agent translates them from the answer — and the agent''s own text; `given`, `when`, `then`, `tasks` — lines and sub-points — and `ratification` stand in the chat as the answer holds them, the words the vault will hold (cases 387.1, 441). The main agent writes a short-form Case in English in the chat, and the hook writes it as shown (case 441). English, in the manner of ASD-STE100 Simplified Technical English, in everything that lands in the vault: the Spec is written from the English answer and the English short form, slugs, field names and ledger lines unchanged (cases 123, 387.1, 441).'
  - old: The agent shows the Case of the answer whole and unchanged, its own text after one horizontal rule; a showing that the `Stop` comparison of `rule-case-check` refuses as different from the answer is followed, before the person answers, by a reply that shows the answer whole and unchanged;
    new: The agent shows the Case of the answer whole, at every showing, its name, `context`, `problem` and `recommend` translated into Russian and the rest unchanged, its own text after one horizontal rule; a showing that the `Stop` comparison of `rule-case-check` refuses as different from the answer is followed, before the person answers, by a reply that shows the answer whole, translated the same way;
  change: the main agent translates the prose of the English answer for the chat and writes a short-form Case in English; a ratified Case changes only through its case-guppi and is shown again whole; the prose DIFF and the translation before the approval go (case 441.2)
- slug: estimate-case-protocol-shows-the-built-case
  set:
    status: pending
  change: the Criterion replaced whole — the prose translated for the chat, every showing whole, a changed Case through its case-guppi, the short form in English (case 441.2)
```

```tasks
- [ ] update `rule-case-protocol`
- [ ] update `estimate-case-protocol-shows-the-built-case`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-case-protocol-shows-the-built-case`
```

### Case 441.3 — the Stop comparison reads only given, when, then, tasks and ratification

> **given:**
> `rule-case-check` — the rule of the check of an answer and of the comparison of a showing
> **＋** `estimate-case-check-shows-only-the-checked-case` — the promise of the comparison on `Stop`
> **＋** `guppi/casecheck.py` — `against_store`, `shown_text` and the module docstring
> **＋** `guppi/ratified.py` — the Spec hook, which imports `against_store`
> **＋** `tests/test_casecheck.py` — the tests of the comparison
> **＋** `<plan>.checked.json` — the store of the answers of `case-guppi`

> **when:**
> `Stop` fires after a reply of the main agent that shows a Case under `## Case N —` or `### Case N.M —` with at least one of its sections.

> **then:**
> `uv run guppi casecheck` compares each such Case with the Case of the same id in `<plan>.checked.json` in its `given`, `when`, `then`, `tasks` and `ratification`, line by line once line ends and trailing spaces are the same.
> **＋** The name of its heading, its `context`, `problem` and `recommend` are not compared: a showing that differs from the answer only in them passes.
> **＋** A Case the store does not hold, a Case that differs in a compared section, or a Case stored with findings exits 2, the reason and the findings on stderr.
> **＋** A parent shown with its sub-cases is compared part by part, as the store holds each.
> **＋** The Spec hook `guppi/ratified.py` judges a showing by the same comparison, imported.
> **－** A heading with no section, as in the acknowledging reply, a fence tagged `DIFF`, and a deferred decision in the short form — `context`, `problem` and a fence tagged `then` with `defer` items, no `given` and no `when` — are not compared.
> **－** On the re-fire (`stop_hook_active`) it exits 0.

```then
update:
- slug: rule-case-check
  set:
    purpose: Prevents a Case from being shown to the person in a form the checks of pre-spec refuse, or with other given, when, then, tasks or ratification than the ones that passed them
  replace:
  - old: or in other words than the ones that passed them. Until case 419
    new: or with other `given`, `when`, `then`, `tasks` or `ratification` than the ones that passed them; its prose the main agent translates for the chat (case 441). Until case 419
  - old: Each Case the reply shows under its heading with at least one of its sections is compared with the Case of the same id in `<plan>.checked.json`, line by line once line ends and trailing spaces are the same; a parent shown with its sub-cases is compared part by part.
    new: Each Case the reply shows under its heading with at least one of its sections is compared with the Case of the same id in `<plan>.checked.json` in its `given`, `when`, `then`, `tasks` and `ratification`, line by line once line ends and trailing spaces are the same; the name of its heading, its `context`, `problem` and `recommend`, which the main agent translates, are not compared (case 441); a parent shown with its sub-cases is compared part by part.
  change: the Stop comparison reads only given, when, then, tasks and ratification (case 441.3)
- slug: estimate-case-check-shows-only-the-checked-case
  set:
    status: pending
  change: the Criterion replaced whole — the prose is not compared (case 441.3)
```

```tasks
- [ ] update `rule-case-check`
- [ ] update `estimate-case-check-shows-only-the-checked-case`
- [x] `guppi/casecheck.py`: `against_store` compares the quoted `given`, `when`, `then`, `tasks` and `ratification` of the showing and of the stored text, the heading name and the prose left out; the module docstring says it
- [x] `tests/test_casecheck.py`: a showing whose heading name, `context`, `problem` and `recommend` differ from the answer passes; one that differs in `given`, `then`, a task sub-point or a `ratification` line is refused; a compared section present in one and missing in the other is refused
- [x] `uv run pytest tests/test_casecheck.py tests/test_ratified.py`
- [ ] read `estimate-case-check-shows-only-the-checked-case`
```

### Case 441.4 — pre-spec translates nothing and sends a finding in a Case to its case-guppi

> **given:**
> `rule-prespec` — the Render of the skill pre-spec; deferred by case 438
> **＋** `estimate-prespec-reconciles` — the promise of the run of pre-spec
> **＋** `/pre-spec` — the skill rendered from `rule-prespec` into `.claude/skills/pre-spec/SKILL.md`
> **＋** `rule-spec-write` — the hook that writes the new answer of a Case into the plan

> **when:**
> The person invokes `/pre-spec`, or the agent calls the skill, before the Spec is approved.

> **then:**
> The agent runs `guppi prespec --check` on the plan file with `--session <id>`, the eight-character id of the `hi:` line, and reads the first line of the output before the exit code — "no hi recorded for session …; nothing checked" means the wrong value; nothing is translated before the run.
> **＋** A finding in a Case — in its prose or in its body, a wrong fact of its `context` included — goes to the `case-guppi` of that Case by `SendMessage`; its new answer is shown and ratified again, and the hook of `rule-spec-write` writes it into the plan; the agent does not edit the text of a Case in the plan file.
> **＋** A finding in the Frontier or in a ledger line is fixed there, and the command runs again until it prints no finding.
> **＋** `ask-guppi` is dispatched once with the absolute path of the plan file and the instruction to read every Case outside `## Deferred` — `context`, `when`, `then`, the `then` block — and, for an `update` of a rule or an entity, the page's `estimates`; of a Case under `## Deferred` it reads only the slugs of its `defer` items.
> **＋** Three questions: which decisions contradict a page of the vault, a rule of the vault, or each other; whether an Estimate the Case does not name speaks of the thing the Case changes; which fact of a `context` — a page's status, a count, a case number, a claim that no page holds a thing — the vault does not bear out.
> **＋** The agent answers the findings with one report before any Case is shown again: each finding numbered, with the fix it proposes or why it is already known, and the decisions it needs from the person; then the changed Cases are shown again in one reply.
> **＋** `guppi gate` writes the stamped `prespec` line on the Skill call; then Plan Mode exits again.
> **－** The agent writes no list of the decisions: the plan is the list.
> **－** The body of a deferred decision is not read; a Case that changes a page another Case of the plan defers is still a finding.

```then
update:
- slug: rule-prespec
  replace:
  - old: 'and for every name, `context` or `problem` still holding a Cyrillic letter: translate them before you run it (case 387.4).'
    new: and for every name, `context` or `problem` still holding a Cyrillic letter — `case-guppi` writes English, and such a Case goes back to it (cases 387.4, 441).
  - old: A wrong fact of a `context` is fixed in the plan as a change of prose.
    new: A wrong fact of a `context` goes to the `case-guppi` of that Case like any other finding in a Case.
  - old: Fix the plan, the frontier or the line for each finding, then run it again until it prints no finding.
    new: A finding in a Case — its prose or its body — goes to the `case-guppi` of that Case by `SendMessage`, and its new answer is shown and ratified again, the hook of `rule-spec-write` writing it into the plan; do not edit the text of a Case in the plan. Fix the frontier or the line for any other finding, then run it again until it prints no finding (cases 438, 441).
  change: nothing is translated before the run; a finding in a Case goes to its case-guppi and a new ratification (case 441.4, supersedes 438)
- slug: estimate-prespec-reconciles
  set:
    status: pending
  change: the Criterion replaced whole — no translation before the run, a finding in a Case to its case-guppi (case 441.4)
```

```tasks
- [ ] update `rule-prespec`
- [ ] update `estimate-prespec-reconciles`
- [ ] `uv run guppi render`: `.claude/skills/pre-spec/SKILL.md`
- [ ] read `estimate-prespec-reconciles`
```

### Case 441.5 — the check of the plan against its ratified copy runs with no translation before it

> **given:**
> `estimate-prespec-checks-the-ratified-copy` — the promise of the comparison with the ratified copy and of the Cyrillic finding
> **＋** `rule-prespec` — the rule of the check
> **＋** `/pre-spec` — the skill rendered from `rule-prespec`
> **＋** `<plan>.ratified.md` — the ratified copy beside the plan file

> **when:**
> `guppi prespec --check <plan>` runs at `/pre-spec` and reads the plan and its ratified copy `<plan>.ratified.md`.

> **then:**
> A Case of the plan whose ids, `given`, `when`, `then`, `then` block or `tasks` differ from its section in the ratified copy: one finding naming the Case and the parts.
> **＋** A Case of the plan with no section in the copy, and a section of the copy with no Case in the plan: one finding each.
> **＋** A name, `context` or `problem` that holds a Cyrillic letter: one finding.
> **－** The section of a Case a `{supersedes:case N}` of the session's window names is no finding: that Case left the plan (case 299.1).
> **－** The section of a parent with sub-cases in the copy, every one of them named by such a line, is no finding: the parent left the plan with them.
> **－** A Case under `## Deferred` is not compared.

```then
update:
- slug: estimate-prespec-checks-the-ratified-copy
  set:
    status: pending
  change: the Criterion replaced whole — the run follows no translation; the Cyrillic finding stays (case 441.5)
```

```tasks
- [ ] update `estimate-prespec-checks-the-ratified-copy`
- [ ] read `estimate-prespec-checks-the-ratified-copy`
```

### Case 441.6 — the Spec hook writes a Case ratified after the approval into spec.md

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case
> **＋** `estimate-spec-write-reaches-the-approved-spec` — the promise of the write into `spec.md`
> **＋** `rule-spec-capture` — the rule that names the writers of `spec.md`
> **＋** `rule-case-protocol` — its Render says where the Spec hook writes
> **＋** `guppi/ratified.py` — the `Stop` hook `uv run guppi ratified`
> **＋** `guppi/spec.py` — its docstring names the writers of `spec.md`
> **＋** `tests/test_ratified.py` — the tests of the hook
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the approved Spec of the session

> **when:**
> The `Stop` hook `uv run guppi ratified` has written a ratified Case N from its stored answer into the plan file, after a reply whose `LEDGER` block holds the decision lines of Case N, and `raw/<hi date>/<hi HHMM>/spec.md` stands.

> **then:**
> The hook writes the same stored answer of Case N into `spec.md`: the heading, `context`, `problem`, `given`, `when` and `then`, the block tagged `then` and the block tagged `tasks`.
> **＋** Every section of Case N that stands in `spec.md` is replaced; a Case with no section there is placed after the last section of its family, or before the `## Deferred` of the last approved document, or at the end.
> **＋** A task line whose text stood in a replaced section keeps the box it had there.
> **＋** The `context` and `problem` of a sub-case's parent, written into `spec.md` and into the plan file, come from the parent's stored answer, never from the reply.
> **－** Nothing written into `spec.md` is translated or refused for its language.
> **－** A refusal that writes nothing of Case N into the plan file writes nothing of it into `spec.md`.
> **－** On the re-fire (`stop_hook_active`) nothing is written: exit 0.

```then
create:
- slug: estimate-spec-write-reaches-the-approved-spec
  ref: rule-spec-write
  kind: QA
  purpose: A Case ratified after the approval reaches spec.md from its stored answer, every section of it replaced or the Case placed, the ticks of its unchanged task lines kept
  method: uv run pytest tests/test_ratified.py -k approved_spec; by hand, the first Case ratified in Work Mode after the change
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-spec-write
  replace:
  - old: the section of Case N is replaced when it stands, appended otherwise.
    new: 'the section of Case N is replaced when it stands, appended otherwise. Once `spec.md` in the session''s folder stands, the hook writes the same stored answer into it too: every section of Case N there replaced, or the Case placed after its family, before the `## Deferred` of the last approved document, or at the end; a task line whose text stood in a replaced section keeps its box; the `context` and `problem` of a sub-case''s parent come from the parent''s stored answer, never from the reply (case 441).'
  change: once spec.md stands, a Case ratified after the approval is written into it too, its ticks kept (case 441.6)
- slug: rule-spec-capture
  replace:
  - old: 'The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped; Work Mode, which ticks the boxes of the `tasks` blocks and nothing else; and the agent, who appends the short-form Cases under `## Deferred` at the close of Plan Mode and at Retro, before their ledger lines.'
    new: 'The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped; the `Stop` hook of `rule-spec-write`, which, once the file stands, writes each Case ratified after the approval — its sections replaced, or placed — removes a superseded Case, and writes a defer-only Case at Retro under `## Deferred` (cases 421.1, 441); and Work Mode, which ticks the boxes of the `tasks` blocks.'
  change: 'the writers of spec.md: the Stop hook of rule-spec-write writes a Case ratified after the approval, removes a superseded one and writes a defer at Retro (case 441.6)'
- slug: rule-case-protocol
  replace:
  - old: into the plan file and into the ratified copy `<plan>.ratified.md` beside it, outside the repository; the agent creates the plan file
    new: into the plan file and into the ratified copy `<plan>.ratified.md` beside it, outside the repository, and, once `raw/<date>/<hi HHMM>/spec.md` stands, into it too, the ticks of its unchanged task lines kept (case 441); the agent creates the plan file
  change: the Spec hook writes into spec.md once it stands (case 441.6)
```

```tasks
- [ ] update `rule-spec-write`
- [ ] create `estimate-spec-write-reaches-the-approved-spec`
- [ ] update `rule-spec-capture`
- [ ] update `rule-case-protocol`
- [x] `guppi/ratified.py`: after `write_case` of Case N, when `spec.md` of the session folder stands, write the stored answer there — every section of Case N replaced, a new Case placed before the `## Deferred` of the last approved document — the boxes of task lines whose text stood in a replaced section kept; a parent's `context` and `problem` taken from its stored answer only; the module docstring says it
- [x] `guppi/spec.py`: the sentence on the writers in the module docstring says what `rule-spec-capture` says
- [x] `tests/test_ratified.py`: tests named `approved_spec` — a section replaced from the stored answer; two sections of Case N both replaced; a new Case placed; a ticked task line kept ticked and a changed one unticked; a refused showing writing nothing into `spec.md`; no `spec.md`, nothing written there; a parent's prose taken from the store when the reply shows it translated
- [x] `uv run pytest tests/test_ratified.py tests/test_spec.py`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-spec-write-reaches-the-approved-spec`
```

### Case 441.7 — the Spec hook removes a superseded Case

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes and removes the sections of the Spec
> **＋** `estimate-spec-write-removes-a-superseded-case` — the promise of the removal
> **＋** `rule-case-protocol` — its Render says a superseded Case leaves the Spec
> **＋** `guppi/ratified.py` — the `Stop` hook `uv run guppi ratified`
> **＋** `tests/test_ratified.py` — the tests of the hook
> **＋** `<plan>.ratified.md` — the ratified copy beside the plan file
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the approved Spec of the session

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds a decision line carrying `{supersedes:case N}`, and it has written the Case of that line in the same run.

> **then:**
> The hook removes the section of Case N — its heading, its sections, its `then` and `tasks` blocks, and the sections of its sub-cases — from the plan file and from `<plan>.ratified.md`.
> **＋** Once `raw/<hi date>/<hi HHMM>/spec.md` stands, it removes every section of Case N and of its sub-cases from it too.
> **＋** A `{supersedes:case N.M}` removes the section of that sub-case alone; its parent and its other sub-cases stay.
> **＋** A section of Case N under `## Deferred` is removed the same way.
> **－** A Case N that none of these files holds — a Case of an earlier session, a defer taken up — is no refusal, and nothing is removed.
> **－** A line whose own Case the hook refused or did not write removes nothing.
> **－** On the re-fire (`stop_hook_active`) nothing is removed: exit 0.

```then
create:
- slug: estimate-spec-write-removes-a-superseded-case
  ref: rule-spec-write
  kind: QA
  purpose: A Case superseded by a decision line of the reply leaves the plan file, the ratified copy and spec.md, with its sub-cases
  method: uv run pytest tests/test_ratified.py -k superseded; by hand, the first supersedes of a Case of the same session after the change
  tags:
  - hooks
  - harness
  - workflow
update:
- slug: rule-spec-write
  replace:
  - old: and nothing of the Case is written (case 436.3).
    new: and nothing of the Case is written (case 436.3). After the writes, a decision line of the reply that carries `{supersedes:case N}`, its own Case written in this run, removes the section of Case N — with its sub-cases, or `### Case N.M` alone when the line names a sub-case — from the plan file, the ratified copy and, once it stands, `spec.md` in the session's folder, under `## Deferred` too; a Case N none of them holds is no refusal (case 441).
  change: the Stop hook removes a Case superseded by a line of the reply from the plan, its copy and spec.md (case 441.7)
- slug: rule-case-protocol
  replace:
  - old: A Case superseded in its own session, before the Spec is approved, leaves the Spec — no heading, no section, no `then` or `tasks` block — and the superseding Case is written whole;
    new: 'A Case superseded in its own session leaves the Spec — no heading, no section, no `then` or `tasks` block: the `Stop` hook of `rule-spec-write` removes it from the plan file, the ratified copy and, once it stands, `raw/<date>/<hi HHMM>/spec.md` (case 441) — and the superseding Case is written whole;'
  change: the Stop hook removes a superseded Case from the Spec (case 441.7)
```

```tasks
- [ ] update `rule-spec-write`
- [ ] create `estimate-spec-write-removes-a-superseded-case`
- [ ] update `rule-case-protocol`
- [x] `guppi/ratified.py`: after the writes of `stop`, for each decision line of the reply whose Case was written in this run, remove the sections its `{supersedes:case N}` names from the plan, the ratified copy and `spec.md` when it stands; the module docstring says it
- [x] `tests/test_ratified.py`: tests named `superseded` — a Case and its sub-cases removed from the plan, the copy and `spec.md`; a sub-case removed alone; a section under `## Deferred` removed; a Case no file holds is no refusal; a refused Case removes nothing
- [x] `uv run pytest tests/test_ratified.py tests/test_prespec.py`
- [ ] `uv run guppi render`: `vault/wiki/case-schema.md`
- [ ] read `estimate-spec-write-removes-a-superseded-case`
```

### Case 441.8 — the Spec hook copies the stored answer; a DIFF no longer skips a Case

> **given:**
> `rule-spec-write` — the rule of the `Stop` hook that writes a ratified Case; its purpose and its Purpose
> **＋** `estimate-spec-write-copies-the-ratified-case` — the promise of the write into the plan and its copy
> **＋** `guppi/ratified.py` — `find_showing`, `names_in_diff` and the module docstring
> **＋** `guppi/casecheck.py` — the one comparison `against_store`
> **＋** `guppi/materialize.py` — `item_keys`, the one judgment of the keys of an item
> **＋** `guppi/generate.py` — applies the items by the same keys
> **＋** `tests/test_ratified.py` — the tests of the write

> **when:**
> The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds `- decision[case N]` lines of a kind other than `defer`; it reads the session's transcript for the last earlier reply that shows `## Case N —` whole, and `<plan>.checked.json` beside the plan file for the answer of `case-guppi` stored under Case N.

> **then:**
> The hook writes the stored answer of Case N into the plan file `plan_path` finds, the section of Case N replaced when it stands, appended otherwise: the heading, `context`, `problem`, `given`, `when` and `then` as the answer holds them; a block tagged `then` built from the sub-points of `tasks`; a block tagged `tasks` of the task lines without their sub-points; `recommend` and `ratification` are not written.
> **＋** It writes the same text the same way into the ratified copy `<plan>.ratified.md` beside the plan file.
> **＋** A last showing of Case N that differs from the stored answer — by the one comparison `uv run guppi casecheck` makes on `Stop`, imported from `guppi/casecheck.py` — a store with no Case N, or a Case N stored with findings: exit 2 with the reason on stderr, and nothing of Case N is written.
> **＋** A task line opening with `create`, `update`, `delete` or `defer` and the slug in its first code span is an item of the `then` block; its sub-points are its keys — `old` and `new` in pairs under `replace`, `reword old` and `reword new` under `reword`, `set`, `change`, `rename`, `sections.<Name>`, the fields of a `create` — each value one code span, padded by one space on each side when the value holds a backtick, or a fenced block under the sub-point.
> **＋** A sub-point that reads into no key `item_keys` of `guppi/materialize.py` gives the kind and the category of its item — the one judgment `guppi/materialize.py` lifts by and `guppi/generate.py` applies by — is refused: exit 2 with `` `<key>`: not a key of <kind> <slug> `` on stderr, and nothing of the Case is written.
> **＋** A value that holds a backtick in an outer span not padded on both sides is refused: exit 2 with `` `<key>`: a value holding a backtick takes its outer span padded by one space `` on stderr, and nothing of the Case is written.
> **＋** No plan file in the event log, no showing of Case N whole, or a sub-point it cannot read: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
> **－** A `create` or a `defer` of a category with no schema file, or of one whose schema rule a decision line of the session or of the reply creates or updates, is not judged by its keys (case 308.2).

```then
update:
- slug: rule-spec-write
  set:
    purpose: Prevents a ratified Case from entering the Spec in other words than the answer of case-guppi whose given, when, then, tasks and ratification the person signed
  replace:
  - old: Prevents a ratified Case from entering the Spec in other words than the ones the person signed.
    new: Prevents a ratified Case from entering the Spec in other words than the answer of `case-guppi` whose `given`, `when`, `then`, `tasks` and `ratification` the person signed.
  - old: Now `given`, `when`, `then` and `tasks` are English in the chat, and a hook copies them.
    new: Now `case-guppi` writes the whole Case in English, and a hook copies its stored answer (cases 437, 441).
  - old: A last showing that is a `DIFF` block writes nothing. After the write
    new: After the write
  change: the hook copies the stored English answer; a DIFF no longer skips a Case (case 441.8)
- slug: estimate-spec-write-copies-the-ratified-case
  set:
    status: pending
    purpose: The ratified Case enters the plan file and its ratified copy in the words of the stored answer of case-guppi, the then block built from the sub-points
  change: the Criterion replaced whole — the DIFF skip goes (case 441.8)
```

```tasks
- [ ] update `rule-spec-write`
- [ ] update `estimate-spec-write-copies-the-ratified-case`
- [x] `guppi/ratified.py`: `find_showing` returns the last message that shows the Case whole, a `DIFF` fence no longer read; `names_in_diff` and `DIFF_TAG` removed; the module docstring says it
- [x] `tests/test_ratified.py`: the test of a last `DIFF` showing becomes a test that a later `DIFF` fence naming Case N does not stop its write
- [x] `uv run pytest tests/test_ratified.py -k write`
- [ ] read `estimate-spec-write-copies-the-ratified-case`
```

### Case 441.9 — the check after the write names no DIFF

> **given:**
> `estimate-spec-write-checks-the-written-case` — the promise of the check after the write
> **＋** `rule-spec-write` — the rule of the `Stop` hook
> **＋** `guppi/prespec.py` — the checks of `prespec --check`, imported by the hook
> **＋** `raw/<hi date>/<hi HHMM>/frontier.md` — the Frontier, which the check does not read

> **when:**
> The `Stop` hook `uv run guppi ratified` has written Case N into the plan file and its ratified copy after a reply whose `LEDGER` block holds the decision lines of Case N.

> **then:**
> The hook runs the checks of `prespec --check`, imported from `guppi/prespec.py`, on each Case it wrote in this run and its sub-cases, with the decision lines of the reply added to those of the session's ledger, each line once.
> **＋** The `replace` and `reword` pairs of every Case of the plan are applied in entry order, and only an anchor of a Case written in this run that misses or hits more than once is a finding.
> **＋** On a finding: exit 2, the findings on stderr after `ratified:`, each naming its Case; the written Case stays in the plan and in its ratified copy.
> **＋** A finding of a Case not written in this run is not reported.
> **－** On the re-fire (`stop_hook_active`) nothing is checked: exit 0.
> **－** A Case not written in this run, and a defer-only Case, which the hook writes under `## Deferred`, are not checked.
> **－** The Frontier `raw/<hi date>/<hi HHMM>/frontier.md` is not read.
> **－** The plan is not compared with its ratified copy, and a name, `context` or `problem` that holds a Cyrillic letter is no finding.
> **－** A ledger line of the window that does not parse is no finding of this check.

```then
update:
- slug: estimate-spec-write-checks-the-written-case
  set:
    status: pending
  change: the Criterion replaced whole — a DIFF showing is no longer named (case 441.9)
```

```tasks
- [ ] update `estimate-spec-write-checks-the-written-case`
- [x] `uv run pytest tests/test_ratified.py -k checks_the_written`
- [ ] read `estimate-spec-write-checks-the-written-case`
```

### Case 441.10 — the append at the approval leaves what the Stop hook wrote

> **given:**
> `estimate-spec-capture-appends` — the promise of the append at `ExitPlanMode`
> **＋** `rule-spec-capture` — the rule of the hook `guppi spec`
> **＋** `rule-spec-write` — the `Stop` hook that also writes `spec.md`
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the approved Spec of the session

> **when:**
> `ExitPlanMode` is approved, and `uv run guppi spec` runs on its `PostToolUse` with the plan in `tool_response.plan`.

> **then:**
> In a session with a `hi`, the plan is appended to `raw/<hi date>/<hi HHMM>/spec.md` — a `---` separator when the file has content, the stamp `<!-- approved HH:MM:SS · session xxxxxxxx -->` and the plan text — once, even when the hook runs twice.
> **＋** A second approval of the same session appends under `---` and its stamp.
> **＋** The hook changes nothing that stands in the file: earlier documents, the sections the `Stop` hook of `rule-spec-write` wrote and a `## Deferred` section stay as they are, and `uv run guppi materialize` reads their Cases.
> **－** Without a `hi` the hook exits 2 naming the session, and the file is untouched.
> **－** The payload of another tool writes nothing: exit 0.

```then
update:
- slug: estimate-spec-capture-appends
  set:
    status: pending
    method: pytest in tests/test_spec.py with piped payloads against a temp vault; by hand, the next approval of a session after the change
  change: the Criterion replaced whole — the Stop hook of rule-spec-write, not the agent, writes the sections the append leaves (case 441.10)
```

```tasks
- [ ] update `estimate-spec-capture-appends`
- [x] `uv run pytest tests/test_spec.py`
- [ ] read `estimate-spec-capture-appends`
```

## Deferred

## Case 442 — the agent can forget the mark `addressed_by` or `addresses` on a lesson line

> **context:**
> A lesson line in the ledger must carry the mark `{addressed_by:case N}` when it is written after the Case of this session that closed its cause. When the lesson is written before the Case, the decision line of that Case carries the mark `{addresses:…}` (case 379). Today nothing makes the agent set the mark: the ledger hook writes the line without it. In session 1337 the line `lesson-hooks-subagentstop-fires-before-and-after-the-handback` stayed with no mark, although Case 434 closed its cause. The librarian then does not link the lesson to the decision, and the lesson stays `new`.

> **problem:**
> No check finds a lesson line with no mark when a Case of the same session closed its cause. How to catch such a missing mark? The decision is deferred.

```then
defer:
  - slug: rule-ledger-write
    type: rule
    purpose: A lesson line whose cause a Case of the same session closed carries addressed_by or the decision line carries addresses; nothing catches a missing mark
```
