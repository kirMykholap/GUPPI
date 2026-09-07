---
session: 2026-08-24
sprint: S3
commits: none
---

# Handoff — 2026-08-24

**Nothing was committed.** The session began at `efa0aa8` and still stands there; every change
below is unstaged in the working tree. The owner did not ask for a commit and none was made.

## State

**Done.** The feedback catcher reads the form the rendered rule actually shows and files one entry
per line instead of one per fence. `scripts/vault-check.sh` gained `--rules`, a register swept from
its own headings. `scripts/vault-check-selftest.sh` gained `--list` and `--only <pattern>` and an
argument contract. `scripts/vault-inject.sh` lost five process spawns per page. Rule 13 of the gate
runs `vault-authority.sh` once instead of twice. `decided_by:` is filled across `wiki/proposals/`.
The narrowed `idea`/`decided_by:` verdict is built. The ratification sweep of the 27
owner-attributed blocks is done.

**Not done.** The flag that would skip rules 12 and 13 — it meets a live prohibition and the owner
deferred the conversation. The full per-rule narrowing. The entity split for the gate and its suite.
The six decision pages that six proposals need. The `measure:` section: its shape is decided, its
grammar is not.

**In flight.** Nothing.

**Next step.** `/ingest`, which owes the six missing decision pages.

**Checks, each exit code read from its own invocation:**

| command | reading |
|---|---|
| `pwsh scripts/hook-selftest.ps1` | `caught 141, missed 0`, exit 0 — from 138 at the session's start |
| `bash scripts/vault-check-selftest.sh` | `caught 173, missed 0`, exit 0, **37m44s** at 704 vault files and 577 pages under `wiki/` |
| `bash scripts/vault-check-selftest.sh --list` | 173 case(s) — 157 dispatched, 16 written inline; **it agrees with the run exactly** |
| `bash scripts/vault-check.sh` | exit 0, one standing advisory at `a region or whole generation covers 8 of 15` |
| `bash scripts/vault-check.sh --lint` | exit 0; **7 pages in `proposals/` and `rules/` carry no `decided_by:`, down from 33** |
| `bash scripts/vault-inject.sh` | 0 rewritten, 0 generated, 0 removed, 0 problems |
| `bash scripts/vault-check.sh --rules` | 15 heading(s), swept from the script, exit 0 |

**`uv run pytest`, `ruff check`, `ruff format --check` and the browser walk were not run and are not
owed:** no Python under `src/` changed and the product has not moved since 2026-08-12. The one Python
file this session touched is `scripts/session-dialogue.py`, and it was run rather than edited.

**The 37m44s is not comparable with the 34m08s on the record** and must not be quoted as a
regression. Two things differ: the corpus grew from 562 to 577 pages, and the machine measurably
slowed. The control is `scripts/vault-authority.sh`, which nothing touched all session and which
went from 1.18–1.38 s to 1.52–1.98 s; the gate on identical code went from 15.02/15.39/15.42 s to
21.21/21.46/24.87 s. **The only defensible claim about what the work bought is the paired gate
reading: 17.2 → 15.3 s, minus 11%**, three runs each, taken back to back in a quiet window.

## Entities

**`scripts/vault-check.sh` — changed.** A second flag, `--rules`, which prints the rule register
swept from the script's own `^# [0-9]` headings and exits 0 without reaching the vault. The
usage-error message now names both legal arguments. Rule 5c reads `binding:` off the
`decided_by:` target in the same awk pass that already read its `type:`, and carries the narrowed
`idea` verdict. Rule 13 makes one invocation of `vault-authority.sh --orphans --check` where it made
two, and the `grep '^VAULT-AUTHORITY:'` that used to filter the first of them is gone — it discarded
every line without the prefix, so half of that rule swallowed what the other half would have
reported.

**`scripts/vault-check-selftest.sh` — changed.** `--list`, `--only <pattern>`, and an argument
contract where it had none: an unknown argument exits 2. `--list` sweeps the file rather than
walking the dispatchers, so it sees the sixteen cases written inline that no dispatcher owns.
`wanted()` takes the case number even when the case is skipped, so a filtered run does not renumber
the report. New: `run_arg_case`, `plant_idea_pair`, and five cases.

**`scripts/vault-inject.sh` — changed.** `status:` and `render:` are read in one awk pass instead of
one awk and a `sed | head | sed`; `governs_targets()` lost the `sed | head -1 |` in front of its awk
and gained an anchored match with `exit`. **The parser's four rules were not retyped** — only the
plumbing in front of them moved, because this function is already the second of three readers of
`governs:` in the repository.

**`.claude/hooks/catch-the-feedback.ps1` — changed.** `$OPENS` decides what opens a record; a record
starts at column zero, optionally behind a list dash, and nowhere else. `Split-Records` turns one
fence into one entry per kind line. The old regex `^\s*([A-Za-z-]+)\s*:` could not pass a leading
dash, and the leading dash is exactly what the rule renders in `CLAUDE.md`.

**`job_hunt_ai_vault/wiki/proposals/_schema.yaml` — changed by the session, not the librarian**,
under the clause that what the gate reads as its own input is the session's to write. The comment
holding the objection to the `idea`/`decided_by:` pair is left exactly as it stood and its answer is
appended beneath it.

**`wiki/proposals/` — 27 of 34 pages now carry `decided_by:`, and one page carries `status: idea`.**
That value was minted on 2026-08-23 and this is the first page in the corpus ever to hold it.

## Decisions

**owner:** «Берем пункт 1 и оставляем пункт 2 до получения измерений. Подписываюсь.»

The suite gets a narrowed fast mode for the loop and **one** full end-to-end run at the end. Rejected:
paying the incidental-coverage price permanently, which is what the live proposal names as the cost
of its second step. The owner's own contribution is the shape that removes it — the full run at the
end restores what the narrowing loses, so the price becomes *you find out later* rather than *you
never find out*. The proposal page does not contemplate that answer and now owes it.

**owner:** «Мне нравится идея делать небольшой прогон для быстрой проверки, а уже в конце - запускать
полный прогон. То есть если прогон ломает какое-то правило - проверяем его, копим такие прогоны и уже
потом заупскаем один полный сквозной. Это хорошее решение, принимается.»

**owner:** «пробуем удешевить injector вместо флага. Если не получится - вернемся к обсуждению снятия
запрета правилом.»

The flag that would have skipped rules 12 and 13 meets
[[the-tag-density-advisories-move-behind-lint]], `binding: prohibition` — *the exit code is identical
with and without the flag*, *nobody can later move a verdict behind the same argument*. Those two
rules print `note`, which sets `fail=1`, so such a flag moves the exit code by construction. Rejected:
lifting the prohibition today. What obliges: the injector work took 1.9 s of a 17.2 s gate; the flag
is worth 5.1 s of 15.3 s, and the conversation about lifting the prohibition is the next session's.

**The session ruled that `--rules` is a mode rather than a filter and therefore outside that
prohibition**, and the owner confirmed the reading and ordered it written as a decision page rather
than left in a script comment: `--rules` runs no check, never prints `VAULT-CHECK: ok`, always exits
0, and so has no run from which to hide anything. Rejected: treating any second flag on the gate as
the forbidden shape.

**owner:** «Строим, но сужаем: правило краснеет, только если decided_by: ведёт на решение, которое не
deferral.»

The `idea`/`decided_by:` verdict is built narrowed. Rejected: both unnarrowed readings, because a
deferral is a decision here and the corpus holds twenty-four of them — a half-thought that was
deferred would be forbidden from being an `idea` at all, which is the objection
`wiki/proposals/_schema.yaml` has carried in the session's own words since the value was minted.
Rejected outright: the third reading, that a proposal which is not an `idea` must carry the field,
which [[decided-by-is-legal-in-proposals-and-rules-and-required-in-rules]] already forbids. **It fires
on nothing in this corpus by construction** and is a guard against a page written tomorrow.

**owner:** «Отправлять в архив должен скрипт на этапе lint. Он проходит по всем записям, проверяет
поля и двигает куда нужно. Если такого механизма еще нет - записывай, будем строить.»

And, on where it lives: it is a sweep inside `scripts/vault-archive.sh` rather than a new script, so
that it inherits that script's refusals rather than acquiring its own opinion about when a move is
allowed. Rejected: a second mover. The full condition list and its behaviour on a refusal are their
own session.

**owner:** «я уже отвечал на этот вопрос. Beads переносится на Sprint 4»

**owner:** «показывай полный список и контекст. Я хочу понимать к чему именно относился decision
перед тем как согласиться или нет»

**owner:** «я ратифицирую все эти блоки. Утверждения верны по сути.»

**This is ONE ratification of a list of 27, not 26 signatures.** Writing it as 26 separate owner
utterances would reproduce the exact defect the sweep exists to remove. One block was rejected:

**owner:** «Мне не нравится пункт 6: он устарел, так как там число и какой статус сейчас - мы не
знаем.»

That is `the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count.md:42`, which
instructs the reader to report *the twelve unmarked files are unchanged*. **The successor carries no
number at all** — the count of unmarked files is a gauge, and gauges do not live inside instructions.
Today's reading, `8 of 15` with seven unmarked and all seven named by the advisory, stands beside it
as a dated line. Rejected: a successor saying "seven", which would go stale on the same two-week
clock that produced 12, 13, 8 and 7.

**owner:** «Некоторые из них продублированы - это мы разбрем позже, когда подготовим и протестируем
механизм»

**owner:** «мы отступили от решения, но уже как есть»

**DIVERGENCE: the ratification sweep ran inside a build session**, against
[[the-ratification-sweep-waits-for-a-session-of-its-own]], which rejects *"doing it today, at the end
of a session that had already spent itself. Blocks read consecutively are read carelessly by the
tenth."* Why it looked unnecessary: the owner routed the sweep to the retro himself, to fill a
34-minute run, and it then happened earlier still, in ordinary conversation. **The outcome is
recorded with it**: of 27 blocks shown, the owner rejected exactly the one with a drifted number in
it. **And the decision is therefore changed rather than merely broken** — a sweep may run inside a
session **when the list is assembled in advance and shown whole**, which is the condition that made
it work. That change is the owner's, taken at the retro.

**DIVERGENCE: the session dispatched an agent where its own instructions forbid dispatching one
unasked.** `/pre-task` may be performed only by dispatching the `pre-task` agent; the session's
instructions forbid calling agents the owner did not ask for. The two rules contradict. The session
did not resolve it silently — it put the contradiction to the owner, who authorised the dispatch:

**owner:** «да, запускаем.»

**The contradiction stands for the next session.**

**Not a divergence, and listed so a later reader does not mistake it for one:** the session edited
`wiki/proposals/_schema.yaml` while a `PreToolUse:Edit` hook warned about the vault's single writer.
[[what-the-gate-reads-as-its-own-input-is-the-sessions-to-write]] puts that file in the session's
hands and says no divergence is recorded. The owner stated the division wider than the question:

**owner:** «Библиотекарь отвечает за документы, сессия правит harness, хуки, скрипты, код и прочее.»

**owner:** «оставить как есть»

`migrating-the-repository-to-english.md` names its cause twice — once in `sources:`, the old idiom,
and once in `decided_by:`, the field built to replace it. Both sentences are true; deleting a true
line for tidiness erases provenance, and the page is the one place a reader can see the two idioms
side by side. Rejected: removing the `sources:` entry.

**owner:** «интересно. Оставим как интересный кейс, можно составить lesson.»

About `the-system-naming-which-hooks-block`, whose `decided_by:` points at a page that is
`deprecated` and lives in `archive/`. Rule 5c permits an archived target explicitly.

**owner, on how a measurement lives:** the split is by the **role of the number and not by the
folder**. *Testimony* is evidence for a claim, lives with that claim in any folder, and never
mutates — the claim was made against that number. *A gauge* answers "how much now", has one true
value at a time, mutates, and lands on an entity page as a consequence of what it is rather than as
a restriction on where measures may go. **A gauge that can be printed is never written by hand**,
which is the principle `--rules` and `--list` were built on the same day.

**owner selected: a marked section rather than a frontmatter field** —
`<!-- measure -->` … `<!-- /measure -->`, legal in any folder, required nowhere, with **no**
frontmatter flag beside it. Chosen against a field, which cannot hold the prose a measurement needs
— a number, its conditions, its date and its subject — and which is what the gate reads for verdicts.
Chosen against a flag-plus-section pair, which restates what a sweep can already see. **It is a
second customer of an existing mechanic**: the `<!-- text -->` slice on rule pages is already a
machine-read region inside a body, with the injector reading it and rules 11 and 12 checking both
ends. The grammar and the build are their own session.

**owner selected: `measure: [slug] text`** — the destination in brackets straight after the kind,
with a page slug, `gauge:<slug>` or `none` as its legal values. Chosen against a trailing arrow,
where the anchor is the last occurrence of a character that also appears inside numbers, and against
a word between the kind and the colon, which would break the regex the hook's kind parser uses and
which this session had just repaired. **Not one of this session's forty-odd `measure:` lines named a
destination.**

**A gauge is checked for uniqueness** by the same shape as two `current` pages sharing an
`authority:`. **The check itself waits**: the corpus holds almost no gauges, and a rule with no
subjects is a rule nobody can test.

**owner:** «1) оставляем decided_by: пустым. Принимается»

Six pages of `wiki/proposals/` keep no `decided_by:` — five where the owner deferred something and
no `decisions/` page was ever compiled from the ruling, plus
`the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate`. The field is optional in that folder, so
an absent field is legal; **`status: idea` would have been false**, because it asserts nobody ruled.
Rejected: marking them `idea` to close the count.

**The session overrode the librarian on one page and told the owner in the same turn.**
`the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate` was reported as `idea`; the owner ordered
its second step on 2026-08-24 and this session executed it, so *a half-thought nobody ruled on* is
false. It joined the leave-empty group. Confirmed: **owner:** «согласен».

**owner:** «поле пишем, размещение не трогаем, расхождение записываем отдельно.»

About `a-style-rule-for-the-prose-a-session-writes`, which carries `status: implemented` and sits in
`wiki/proposals/` while [[an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim]]
says such a page moves. Rejected: moving it here.

## How it is built

**A record in the feedback file opens at column zero and nowhere else.** The catcher's old parser
matched `^\s*([A-Za-z-]+)\s*:`, and `\s*` passes whitespace but not a dash — while `[A-Za-z-]+`
swallows the dash as the kind and then finds no colon, so the whole block fell through to
`unknown:`. The leading dash is what the rule renders into `CLAUDE.md`, so **two renderings of one
rule disagreed and the hook understood only the one nobody follows**. The repair anchors the opener
at column zero with an optional list dash, and drops the leading `\s*` deliberately: indentation is
what separates a continuation from a record, and a `miss:` is obliged to say where it surfaced — a
sentence that lands on the next line and may itself open with a word and a colon.

**A printed register cannot drift and a maintained one always has.** `--rules` sweeps the script's
own headings; `--list` sweeps the suite's own file. The case that proves a register is *derived* is a
mutation — remove a heading in the sandbox and require the row to vanish — because counting the
output against the same headings the feature reads is green under any implementation, including a
list typed in by hand. **Neither proves the register is complete**: a rule the gate can emit with no
heading is invisible to both, and nothing reports it.

**`--list` sweeps rather than walks, because sixteen cases have no dispatcher.** Walking the
dispatchers and printing instead of running is the obvious implementation and it cannot see the
cases written inline in the archive, catalogue and units sections, which reach `report` directly. It
would understate the suite by sixteen while reading as complete.

**A filter must sit at the top of a dispatcher and not at the verdict**, because the expensive part —
a 704-file tree copy and a full gate run — happens between them. And it must take the case number
anyway: results are numbered as they are dispatched so that two runs of a green suite are
byte-identical, and a filter that stopped the counter would renumber everything after it.

**The gate is one shared awk pass plus two delegated scripts, and the shared pass is two thirds of
it.** Measured on a quiet machine: 15.3 s total, of which rule 12 is 3.57 s, rule 13 is 1.5 s, and
the gate's own passes over 577 pages are 10.2 s. **This is why narrowing to one rule buys far less
than the arithmetic suggests** — rules 1 through 10 ride the same pass and cannot be skipped
individually.

**A verdict that needs a second field off a page it has already opened reads it in the same pass.**
Rule 5c resolves the `decided_by:` wikilink, finds the target and reads its `type:`; `binding:` comes
off that same awk. The citing page's `status:` is not re-read either — the frontmatter pass already
holds every page's status and emits `ideapage|` for the ones that matter. A second loop over the same
links would be a second reader of one fact.

**A fixture must own both ends of what it asserts.** `plant_idea_pair` plants the decision beside the
proposal instead of pointing at a real decision in the corpus, whose `binding:` a librarian may
legitimately change tomorrow. It also registers both slugs in `authority.md`, which no other planter
in that file has ever had to do.

## Lessons

**A grep pattern that requires a dot after a rule number cannot see a heading that names two rules.**
The plan asserted rules 4 and 5 carried no `# N.` heading. They share one: `scripts/vault-check.sh:565`,
`# 4 and 5. Links resolve, and no page is an orphan.` There are fifteen headings, not fourteen, and
the script explains the sharing on the next line — two questions over one set built once, which cost
71 seconds at 75 pages when asked per page.

**A subtotal read as a total.** The plan called the suite "136 cases". 136 is the sum of the five
dispatchers the session happened to enumerate; six more dispatchers and sixteen inline cases were
never counted. The true figure was 168 and matched the last recorded reading, which the session had
in front of it.

**A `/pre-task` killed five factual claims of an approved plan, and the fifth was a page that does
not exist.** The plan cited a corpus page about a variable leaking between sections; there is none.
It also placed `a-verdict-pairing-the-idea-status-with-a-named-decision` in `decisions/` when it lives
in `proposals/`. **Its two counts: the shortlist named 32 pages and 21 were opened in full.** Cost:
186,629 tokens, 63 tool uses, 11m52s — a fourth point beside 230,882/14m58s, 225,195/16m and
182,599/13m40s. Four points, not a rate.

**A projection published as a number, wrong by a factor of three.** The plan promised about eleven
minutes off the suite from cheapening the injector. The paired measurement gives 1.9 s off a 17.2 s
gate — three to four minutes. Both figures the projection rested on had been taken on a contended
machine. The session spent the day arguing that a number must be printed rather than maintained, and
put a maintained number with no instrument behind it into the plan it wrote that same hour.

**Measuring a copy of a script placed somewhere else measures nothing.** `scripts/vault-inject.sh`
does `cd "$(dirname "$0")/.."` and resolves `governs:` against the working directory, so a copy in a
scratch directory found no destination and finished in 0.8 s — an instrument failing towards
*nothing to do*, which reads exactly like success. Setting `VAULT=` does not repair it; the copy has
to sit beside the original.

**A control that nothing touched is what separates a change from the machine.**
`scripts/vault-authority.sh` was not edited all session and drifted from 1.18–1.38 s to 1.52–1.98 s,
while the gate on identical code went from 15.02/15.39/15.42 s to 21.21/21.46/24.87 s — about 40%.
Without that control the 37m44s suite run would have been published as a regression caused by the
session's own work.

**The suite's wall clock is not a usable instrument for a change of this size on this machine.** One
point costs 38 minutes, the machine drifts by a third inside one session, and the effect being
looked for is 1.9 s. The instrument that works is the gate, at three readings a minute, with a
control beside it.

**Process spawn costs about 19 ms here, not the 40 ms written into `scripts/vault-inject.sh` in
2026-08-18.** Eighty spawns were removed and returned 1.55 s in the first reading. The old figure is
in a comment that reasons from it.

**A whole-file grep for a field name is satisfied by that name in prose.** The librarian's "does this
page already carry `decided_by:`" guard hit the phrase in the body of
`links-is-filled-by-a-script-from-the-bodys-wikilinks.md:84` and aborted the write at page 18 of 26.
The same class as [[an-example-inside-a-code-block-satisfies-a-search]], one level down. Repaired by
narrowing the guard to the frontmatter block.

**A case that passes before the change is proved by removing the guard, not by running it green.**
Two cases this session were green before their mechanisms existed: the continuation guard in the
feedback catcher and the `deferral` exemption in the new verdict. Making the parser eager turned the
first over — an indented `note:` was torn into its own record and filed as `unknown:`. Making the
exemption match nothing turned the second over. Neither would have been worth anything without that
step.

**An assertion anchored at end-of-line fails against platform newlines.** A case read `MISSED`
against a mechanism that was already correct, because `(?m)$` sits after the `\r` in a CRLF file.

**No fixture in `scripts/vault-check-selftest.sh` had ever met rule 13.** Every planter there plants
a page carrying `governs:`, or a concept where `authority:` and `governs:` are forbidden together —
so none had ever needed an `authority:` slug registered in `authority.md`, and the register is
compared against the tree in **both** directions. The first version of `plant_idea_pair` reddened the
tree for a reason the case was not about.

**Eight of fourteen lines signed `the owner said it` carried the session's English paraphrase rather
than his words** — on the very day the ratification sweep against exactly that defect was completed.
His words were in the transcript the whole time and the extract recovered all eight in a minute. The
mark channel learned to name the *shape* of a decision on 2026-08-24 and was never obliged to carry
the *words*, and the gap between those two obligations is the eight lines.

**The session recorded no feedback marks for the whole of the retro, in which it took about twenty
decisions.** The cause is diagnosable rather than forgetfulness: step 5 of `/retro` builds its
ratification list *from the marks*, and the session read that as the retro replacing the mark
channel. It reads them; it does not replace them. **The owner is watching for a repeat rather than
fixing it now.**

**The session's own report of its retro was wrong by one** — 21 lines claimed answered where 20 were,
because the owner had answered wider than one question and left its fork open. A count stated in a
report about a ritual was not checked against the ritual's own list.

**`--list | head -1` prints `sed: couldn't flush stdout: Permission denied`.** That is a closed pipe,
not a defect — the same class as [[a-quiet-grep-at-the-end-of-a-pipe-reports-a-match-as-a-failure]].

**Two librarian dispatches, measured:** reading the back-fill cost 218,397 tokens, 74 tool uses,
18m32s; writing it cost 246,874 tokens, 22 tool uses, 6m54s.

## Deferred

**The flag that skips rules 12 and 13**, and with it the conversation about lifting
[[the-tag-density-advisories-move-behind-lint]]. Consequence: 5.1 s of a 15.3 s gate stays on the
table, about a third, and the next session meets the prohibition with the same question.

**The full per-rule narrowing** — the second step of
[[the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate]]. Consequence: none pressing; the
measurement now exists and says the ceiling is far below the naive arithmetic, because rules 1
through 10 share one pass.

**Separate entity pages for the gate and for its suite.** The owner asked for them and the work is
the librarian's: `--near` first, then the family read **by hand** because `--near` matches on words
and has already returned *in no group* about a page that exists, then the split, then **deletion** of
the eighteen-condition list on `vault-scripts.md`. Consequence: nine scripts stay on one page under
one `authority:`, and a third drifted copy of the gate's numbering stays live.

**The `measure:` section's grammar and its build.** The shape is decided; the grammar has to be
checked against the numbers already written across the corpus, which is reading. Consequence: every
`measure:` line written between now and then names a destination but has nowhere structured to land.

**The uniqueness check for a gauge.** Consequence: none today — the corpus holds almost no gauges.

**"The librarian prints each criterion's decider output into the brief."** Named at this session's
start with «можем обсудить» and not discussed. Consequence: the *Sprint* section of the brief keeps
being written by hand, for a third session.

**The five rules of `wiki/rules/` that still owe a mechanical instrument**, and the first run of the
lessons collector. Both the owner's, at the session's start:

**owner:** «5) пропускаем, откладываем на следующую сессию» … «7) переносим на следующую сессию»

**Beads → Sprint 4.**

**owner:** «я уже отвечал на этот вопрос. Beads переносится на Sprint 4»

**The duplicated owner blocks — 7/26 and 20/24 of the shown list.**

**owner:** «Некоторые из них продублированы - это мы разбрем позже, когда подготовим и протестируем
механизм»

**Six decision pages that do not exist**, which is why six proposals keep no `decided_by:`. Four of
the six are one session: `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`
carries seven items under `Deferred` and exactly one decision page was ever compiled from it.
**Writing them is compiling a journal, so the next ingest owes them** — and the six empty fields then
close without a second pass over the pages. The slugs whose causes are missing:
`a-machine-readable-format-for-the-registers`, `a-rule-usage-axis-for-vault-lint`,
`lessons-become-a-queue-drained-into-proposals`, `the-obsidian-cli-as-a-reading-surface-for-this-store`,
`the-reading-funnel-is-delivered-as-a-procedure`, and
`the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate`.

**owner:** «написать их»

**Left fragile, and none of it is scoped work yet:** `--only` has a floor of about two minutes,
because the sixteen inline cases run their bodies even when their verdicts are discarded; the rule
register proves it is derived and never that it is complete; `plant_idea_pair` writes into
`authority.md`, which no other planter touches; and **the gate's own passes are two thirds of its
cost and nothing this session touched them.**

## Feedback to the librarian

Drained whole from `.superpowers/sdd/vault-feedback.md`. **Nine of the blocks below were filed under
`unknown:` by the catcher before it was repaired**, each carrying its real kinds inside its own body;
they are copied here exactly as filed, and the librarian files each line under the kind declared
inside it rather than under `unknown`.

- miss: the rendered rule in `CLAUDE.md:63-83` claims its own example is safe for the wrong reason.
  The text says *"A `VAULT-FEEDBACK` fence nested inside another fence is an example and is ignored,
  so the block above files nothing"* — but **the block above is NOT nested**: lines 70 and 76 are the
  only fences in the region, with no outer fence. It files nothing only because it sits in a file
  rather than in a message. **The trap: a session that quotes that region back into a reply files
  four spurious entries**, because the catcher reads a top-level `VAULT-FEEDBACK` fence exactly as it
  is written there. The fix is to make the example genuinely nested in a four-backtick fence, which
  makes it self-demonstrating and safe to quote. Found in this session's review of its own ingest.
- lint: the owner's ruling that an interrupted session needs no journal of its own — «зачем тебе
  журнал прерванной сессии? Мы уже все обсудили и нашли. Значит эта сессия покроет все потери» —
  took verdict `journal` at the ingest of 2026-08-24 and did not reach `wiki/`. **Defensible**: the
  paragraph is about how that particular journal was assembled. **But it is also a reusable ruling on
  how a skipped ritual is repaired** — the session that read the lost one carries it, marked as
  carried — and that class will recur. `raw/` is immutable and the sidecar is written, so this is a
  note for a later ingest rather than a correction.
    (kind not declared by this file - filed as written)
- unknown: - miss: brief 2026-08-24 утверждает "Beads, still never put back to you" — владелец говорит, что уже отвечал на этот вопрос. Ответа нет нигде в корпусе; всплыло на старте сессии
  - decision: Beads переносится на Sprint 4 — the owner said it
  - decision: back-fill decided_by: в wiki/proposals/ и verdict idea/decided_by: берутся в план текущей сессии — the owner said it, in that order
  - decision: критерий 1 (инструменты пяти правил) и первый запуск lessons collector откладываются на следующую сессию — the owner said it
  - decision: ratification sweep делается только с показом полного списка и контекста каждого блока до согласия — the owner said it
- unknown: - decision: suite получает быстрый суженный режим для цикла и один полный сквозной прогон в конце; полный прогон восстанавливает попутное покрытие, которое сужение теряет — the owner said it, against paying the coverage price permanently
  - miss: страница proposal the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate называет потерю попутного покрытия ценой второго шага и не рассматривает финальный полный прогон как способ её вернуть
  - measure: gate 22.7 s real / 9.1 user / 15.3 sys; из них vault-inject.sh --check 7.9 s и vault-authority.sh --check 1.6 s. Машина не была подтверждённо idle — это измерение того же класса, что и отвергнутые вчера, и годится для сравнения долей внутри одного прогона, но не для before/after
  - measure: 136 диспатчей в suite (92 run_case, 30 run_clean, 10 run_case_absent, 3 run_render, 1 run_found), 704 файла в копии на кейс, JOBS=8; 136 × 22.7 s ≈ 51 мин последовательно против 34m8s измеренных, то есть ускорение от параллели ≈1.5× на восьми ядрах
- unknown: - decision: пункт 1 (gate получает способ не запускать правила 12 и 13) берётся в план; пункт 2 (сужение до одного правила) не берётся, пока нет измерения — the session understood it, pending the owner's confirmation
  - miss: 136 кейсов suite не записаны нигде, кроме кода scripts/vault-check-selftest.sh; увидеть список можно только прочитав скрипт или заплатив 34-минутный прогон
  - miss: wiki/entities/vault-scripts.md держит девять скриптов на одной странице с authority: vault-scripts, включая gate и его suite, которые владелец читает как две разные сущности
  - measure: у правил 4 и 5 в scripts/vault-check.sh нет заголовков вида "# N."; заголовки есть у 1, 2, 3, 5b, 5c, 6, 7, 8, 9, 10, 11, 12, 13, 14. Реестр правил нельзя смести с кода, пока эти два не размечены
  - measure: gate — это один общий проход awk, на котором сидят правила 1-10, плюс два отделяемых запуска скриптов (12 и 13). Из 22.7 с: 9.5 с отделяемы, 13.2 с общие. Потолок сужения до одного правила поэтому много ниже наивной арифметики
  - harness: владелец отметил, что разделение объяснения на "что такое gate" и "что такое suite" до сравнения вариантов сделало ответ понятным
- unknown: - decision: пункт 1 берётся, пункт 2 (сужение до одного правила) откладывается до измерения — the owner said it: «Берем пункт 1 и оставляем пункт 2 до получения измерений. Подписываюсь.»
  - decision: список 136 кейсов и реестр правил печатаются командами и не переносятся на страницу entity; страница называет команды — the session understood it, on the ground that catalogue.md was deleted and rule 9 retired for exactly this shape
  - decision: сужение gate объявляется на границе секции, а не на кейсе, и section() сбрасывает его, чтобы оно не протекало в соседнюю секцию — the session understood it
  - miss: --near матчит по словам; brief 2026-08-24 записал, что он вернул "in no group" про существующую страницу. Для разделения vault-scripts.md одного --near недостаточно, семейство нужно читать руками
- unknown: - miss: ритуал требует /pre-task между планом и одобрением и запрещает выполнять его иначе, чем диспатчем агента pre-task; инструкции сессии запрещают вызывать агентов без просьбы владельца. Два правила противоречат друг другу, и разрешить это может только владелец
  - harness: hook на PreToolUse:Write сработал на первой записи сессии и назвал пропущенный ритуал до того, как что-либо было построено — это тот случай, ради которого он написан
- unknown: - measure: из 27 owner-attributed блоков без кириллицы ровно 1 заявляет себя дословной английской цитатой (в кавычках); остальные 26 - английские предложения без кавычек, подписанные owner:. Все 23 страницы несут basis: human
  - measure: один блок продублирован дословно на двух страницах - "a question once asked is closed by the owner and by nobody else" на the-maps-region-replaces-the-prose-it-duplicated.md:35 и a-question-asked-is-not-a-question-answered.md:22. Проверок 26, не 27
  - miss: transcript'ы покрывают 2026-08-03..08-24, кроме 2026-08-15; ни один из 27 блоков не датирован этим днём, но корпус нигде не записывает, за какие дни запись существует
- unknown: - measure: /pre-task на этом плане - 186 629 токенов, 63 обращения, 11м52с. Четвёртая точка рядом с 230 882/14м58с, 225 195/16м и 182 599/13м40с. Четыре точки, не ставка
  - miss: план утверждал, что у правил 4 и 5 нет заголовков; заголовок есть, общий на два правила, scripts/vault-check.sh:565. Заголовков 15, не 14
  - miss: план называл 168-кейсовый suite "136 кейсов" - это сумма пяти перечисленных функций, а не suite; ещё шесть диспатчеров и ~16 ручных кейсов не были посчитаны
  - miss: план сослался на несуществующую страницу корпуса про переменную, протекающую из секции в секцию
  - miss: план указал wiki/decisions/a-verdict-pairing-the-idea-status-with-a-named-decision.md; страница лежит в wiki/proposals/
  - measure: предварительный фильтр injector'а - 0.17 с на 577 страниц; весь --check - 5.7 с на 16 отобранных страницах, то есть ~350 мс на страницу при цене порождения процесса ~40 мс на этой платформе
  - decision: A5 в нынешнем виде упирается в the-tag-density-advisories-move-behind-lint (binding: prohibition), запрещающую уводить verdict за флаг; вопрос вынесен владельцу, сессия его не решает
- unknown: - decision: 26 из 27 owner-attributed блоков ратифицированы одним решением по показанному списку - the owner said it: «я ратифицирую все эти блоки. Утверждения верны по сути.» Это ОДНА ратификация списка, не 26 подписей; записывать её как 26 отдельных высказываний запрещено, это воспроизводит дефект, ради которого sweep затевался
  - decision: блок the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count.md:42 не ратифицирован - the owner said it: «он устарел, так как там число и какой статус сейчас - мы не знаем»
  - decision: дубликаты 7/26 и 20/24 разбираются позже, когда механизм подготовлен и протестирован - the owner said it
  - measure: region coverage сегодня 8 из 15, неразмеченных семь, и все семь названы в advisory; блок 6 предписывает сообщать «двенадцать»
  - miss: the-ratification-sweep-waits-for-a-session-of-its-own отвергает разбор блоков внутри истратившей себя сессии; sweep прошёл именно так. DIVERGENCE. Записать вместе с исходом: из 27 показанных владелец отклонил ровно тот, в который вшито разошедшееся число
- unknown: - decision: удешевляем injector вместо флага; если не выйдет - возвращаемся к разговору о снятии prohibition отдельным правилом - the owner said it
  - decision: работа по D завершена, sweep прошёл внутри build-сессии, отступление принято как есть - the owner said it: «мы отступили от решения, но уже как есть»
  - miss: a-verdict-pairing-the-idea-status-with-a-named-decision.md утверждает, что два прочтения пары «краснят разные страницы»; построить страницу, на которой они расходятся, не удалось - оба срабатывают на пересечении и различаются только текстом сообщения
  - measure: в корпусе 24 решения с binding: deferral. Полумысль, отложенная решением, получит decided_by: при back-fill, и любое из двух прочтений запретит ей быть idea - конфликт проявится ровно после back-fill, а не сейчас
- miss: девять блоков этой сессии записаны в vault-feedback.md как "unknown:" - строки 75, 80, 84, 90, 94, 96, 99, 106, 111, около сорока строк. Вид каждой строки читается внутри записи, но механически потерян; librarian при /ingest должен разложить их по видам, объявленным внутри, а не по "unknown"
- decision: verdict пары строится в суженном виде - краснеет только если decided_by: ведёт на решение, у которого binding: не deferral; отложенная полумысль остаётся idea - the owner said it
- measure: регулярка хука проверена на четырёх формах строки: "miss: text" матчится, "- miss: text", "- `miss`: text" и "`miss:` text" не матчатся
- measure: hook-selftest.ps1 caught 141, missed 0, exit 0 после правки catcher'а; было 138 до сессии, +3 новых кейса
- measure: vault-check-selftest.sh --list печатает 171 кейс - 155 диспатченных, 16 инлайновых; реальный прогон печатал 168 до добавления трёх кейсов, значит --list и прогон сходятся
- measure: --only "the register" отработал за 2м24с против 34 минут полного прогона, 167 кейсов пропущено
- decision: --list сметает имена из собственного файла и не запускает ничего; альтернатива - обход диспатчеров с печатью вместо запуска - не видит 16 инлайновых кейсов и занизила бы suite на шестнадцать, читаясь как полный список - the session understood it
- decision: --rules это режим, а не фильтр, и потому не подпадает под prohibition о флагах: он не выполняет ни одной проверки, не печатает VAULT-CHECK: ok и всегда выходит 0 - the session understood it, and the distinction is written into the script beside the two flags
- miss: инлайновый кейс, отброшенный --only, уже выполнил своё тело; теряется вердикт, а не цена. Перенос проверки раньше требует перестройки пятнадцати рабочих кейсов archive-секции
- measure: injector 6.19/6.26/6.34 до и 3.45-3.71 после (пять подряд), gate 17.31/17.04/17.33 до и 15.42/15.02/15.39 после. Тихая машина, пары сняты подряд. Injector -43%, gate -1.9 с или 11%
- measure: сегодняшний разбор gate 15.3 с - правило 12 (injector) 3.57 с / 23%, правило 13 (authority --orphans 0.55 + --check 0.99) 1.5 с / 10%, собственные проходы awk по 577 страницам 10.2 с / 67%
- measure: прежняя оценка "9.5 с из 22.7, 42%" снята на занятой машине и отменяется; флаг стоит 5.1 с из 15.3, то есть 33%
- miss: план обещал около 11 минут с suite от удешевления injector'а; фактически 3-4 минуты. Расчёт стоял на двух цифрах, снятых на занятой машине
- miss: измерение копии скрипта, запущенной из другого каталога, не измеряет ничего - vault-inject.sh делает cd в свой родительский каталог и резолвит governs: от рабочего каталога, поэтому копия в scratchpad отработала за 0.8 с, не найдя ни одного назначения. Копию надо класть рядом с оригиналом
- measure: цена порождения процесса на этой машине ~19 мс, а не 40 мс, записанных в комментариях vault-inject.sh 2026-08-18: убрано 5 спавнов на страницу на 16 страницах, то есть 80, и это дало 1.55 с в первом замере
- decision: --only имеет пол около 2 минут - сборка песочницы плюс тела 16 инлайновых кейсов, которые выполняются даже когда отброшены - the session understood it, measured at 2m24s for 8 cases and 2m59s for 11
- miss: ни один планировщик страниц в vault-check-selftest.sh не сажает страницу с authority:, поэтому ни один не встречался с правилом 13. Первая версия фикстуры покраснела: слуг в дереве, но не в authority.md, а реестр сверяется в обе стороны
- measure: правило 13 сведено к одному запуску vault-authority.sh --orphans --check; пара, снятая в тихом окне, 1.54 -> 1.30 с. Эффект на уровне gate ниже сегодняшнего шума и не измерен
- measure: контроль на замедление машины - vault-authority.sh не менялся вовсе и ушёл с 1.18-1.38 на 1.52-1.98 с, gate с 15.0-15.4 на 17.1-22.2. Сдвиг средовой, не от правок
- decision: вердикт пары вешается на цикл правила 5c, а не заводит правило 15: 5c уже резолвит decided_by:, находит целевую страницу и читает её type:, и binding: читается тем же проходом. Второй цикл по тем же ссылкам был бы вторым читателем одного факта - the session understood it
- miss: комментарий в wiki/proposals/_schema.yaml держит возражение против пары idea/decided_by как открытый вопрос, который обязана решить строящая сессия; сужение владельца от 2026-08-24 отвечает ровно на него, и комментарий теперь описывает решённое
- measure: диспатч librarian на чтение back-fill - 218 397 токенов, 74 обращения, 18м32с. Пятая точка рядом с 186 629/11м52с, 230 882/14м58с, 225 195/16м и 182 599/13м40с
- measure: из 33 страниц wiki/proposals/ без decided_by: 26 имеют найденную причину, 2 - чистые idea, 5 - решение принято владельцем и никогда не скомпилировано в страницу decisions/. Из 26 целей 16 несут binding: deferral, 10 - prohibition; одна цель deprecated и лежит в archive/
- miss: пять отложений владельца не имеют страницы в decisions/, и четыре из пяти из одной сессии - в журнале 2026-08-21 семь §Deferred пунктов, скомпилирована одна страница решения. Proposal'ы написаны, решения за ними нет
- measure: вердикт пары после back-fill не может сработать ни на одной странице: он требует одновременно status: idea и decided_by:, а метод ставит idea ровно там, где решения нет. Это сторож на будущее, а не уборка, и столбец binding: сегодня ни на что не влияет
- miss: wiki/proposals/a-style-rule-for-the-prose-a-session-writes.md несёт status: implemented и лежит в wiki/proposals/, тогда как an-implemented-proposal-moves-to-archive-and-the-successor-carries-its-claim и proposals/_schema.yaml говорят, что такая страница уходит в archive/
- decision: страницу, чей status требует переезда, отправляет в archive/ скрипт на этапе lint - он проходит по всем записям, проверяет поля и двигает куда нужно; сессия и librarian такие переезды руками не делают - the owner said it
- miss: такого механизма нет. scripts/vault-archive.sh двигает только то, что названо ему аргументом, и ничего не ищет; .claude/skills/vault-lint/SKILL.md читает stale status: current глазами и ничего не двигает. Найденный сегодня случай - a-style-rule-for-the-prose-a-session-writes несёт status: implemented и лежит в wiki/proposals/
- decision: decided_by:, указывающий на deprecated страницу в archive/, сохраняется как есть и становится кандидатом на lesson - the owner said it: «интересно. Оставим как интересный кейс, можно составить lesson»
- decision: the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate не получает status: idea вопреки отчёту librarian - владелец приказал её второй шаг 2026-08-24 и эта сессия его исполнила, значит "полумысль, на которую никто не давал решения" ложно; страница уходит в группу "поле пустое" - the session understood it, and the owner was told in the same turn
- measure: диспатч librarian на запись - 246 874 токена, 22 обращения, 6м54с. Проверено мной на дереве: gate exit 0, --lint 33 -> 7, поле на 27 из 34 страниц proposals/, ровно одна страница со status: idea, diff 28 файлов 131 вставка 1 удаление
- miss: проверка "несёт ли страница уже это поле", грепающая весь файл, срывается на имени поля, встреченном в прозе тела - запись прервалась на 18-й странице из 26 из-за фразы в links-is-filled-by-a-script-from-the-bodys-wikilinks.md:84. Тот же класс, что an-example-inside-a-code-block-satisfies-a-search, этажом ниже
- miss: hook на PreToolUse:Edit предупреждает о единственном писателе wiki/ при правке wiki/*/_schema.yaml, тогда как what-the-gate-reads-as-its-own-input-is-the-sessions-to-write прямо выносит эти файлы в зону сессии. Сеть хука шире правила
- miss: job_hunt_ai_vault/CLAUDE.md всё ещё обязывает регенерировать catalogue.md после любой записи под wiki/; файл удалён и заменён на pages.base, правило 9 gate на пенсии
- miss: migrating-the-repository-to-english.md называет свою причину дважды - строкой в sources: и полем decided_by:, - то есть ровно тем способом, который decided-by-is-a-field-of-its-own-and-not-a-line-in-sources отверг. Сообщено и не исправлено
- measure: status: idea впервые в истории корпуса стоит на странице - telling-an-unfilled-retro-from-a-written-one. Значение отчеканено 2026-08-23 и до сегодня не использовалось
- measure: полный прогон vault-check-selftest.sh - caught 173, missed 0, exit 0, 37м44с при 704 файлах в vault и 577 страницах под wiki/. С прежними 34м08с при 562 страницах не сопоставимо
- measure: --list напечатал 173 кейса, реальный прогон поймал 173. Инвариант "список не разошёлся с кодом" сошёлся точно с первого раза
- measure: дрейф среды пойман на неизменном коде gate - 15.02/15.39/15.42 с в тихом окне против 21.21/21.46/24.87 с через час, то есть +40%. Контроль того же дрейфа на vault-authority.sh, которого не касались: 1.18-1.38 -> 1.52-1.98
- decision: единственное защитимое утверждение о результате A - парное измерение gate 17.2 -> 15.3 с, минус 11%, снятое подряд в тихом окне. Wall clock полного прогона в этой сессии измеряет состояние машины - the session understood it
- miss: wall clock полного прогона suite - негодный инструмент для правок такого размера на этой машине: одна точка стоит 38 минут, машина дрейфует на треть внутри сессии, а эффект правки составил 1.9 с. Инструмент, дающий три точки за минуту, - это gate, плюс контрольный скрипт, которого не касались, чтобы поймать дрейф среды
- miss: SIGPIPE от `--list | head -1` печатает "sed: couldn't flush stdout: Permission denied" - это закрытая труба, а не дефект; тот же класс, что a-quiet-grep-at-the-end-of-a-pipe-reports-a-match-as-a-failure
- miss: за весь retro сессия не записала ни одной марки, хотя приняла в нём около двадцати решений - самую плотную их часть за сессию. Причина: шаг 5 скилла retro строит ratification-список ИЗ марок, и сессия прочла это как "retro собирает решения вместо марок". Retro марки читает, а не заменяет; сессия, переставшая отмечать в retro, обнуляет измерение "сколько нашли марки против сколько нашли чтением" для следующей сессии
- miss: сессия отчиталась о 21 отвеченной линии, а отвечены 20 - на Q2 владелец ответил шире вопроса и конкретную развилку не закрыл. Счёт, названный в отчёте о ритуале, был неверен на единицу
- decision: толкование, что --rules это режим, а не фильтр, и потому не подпадает под the-tag-density-advisories-move-behind-lint, признано верным и должно быть записано страницей решения, а не комментарием в скрипте - the owner said it: «согласен»
- decision: отказ писать вид с backticks подтверждён - the owner said it: «Если ты утверждаешь что все работает - окей»
- decision: отдельные entity для gate и suite передаются librarian вместе с планом сессии - сначала --near и чтение семейства руками, потом разделение, потом удаление разошедшегося списка из 18 условий на vault-scripts.md - the owner said it: «полностью согласен. Передать библиотекарю необходимость такой страницы и твой план»
- decision: пункт "librarian печатает вывод decider каждого критерия в brief" переносится на следующую сессию - the owner said it
- decision: правка wiki/*/_schema.yaml сессией законна, divergence не записывается; разделение труда шире вопроса - librarian отвечает за документы, сессия правит harness, хуки, скрипты и код - the owner said it: «Библиотекарь отвечает за документы, сессия правит harness, хуки, скрипты, код и прочее»
- decision: the-suite-gets-a-scanner-exclusion-before-a-narrowed-gate не получает status: idea; поправка сессии подтверждена - the owner said it: «согласен»
- decision: перемещатель в archive/ - это не новый скрипт, а обход внутри vault-archive.sh, который проверяет вики по условиям и двигает найденное; полный список условий и поведение на отказе - отдельная сессия - the owner said it
- decision: шесть недостающих страниц решений пишет ближайший /ingest, а не отдельный диспатч сессии - the owner said it: «согласен»
- decision: три дефекта harness входят в спринт по одной строке - хук PreToolUse:Edit исключается для _schema.yaml, CLAUDE.md vault'а обновляется от устаревшего обязательства про catalogue.md, session-dialogue.py получает три состояния меню - the owner said it
- decision: measure делится по роли числа, а не по папке - свидетельство живёт там же, где утверждение, в любой папке и не мутирует никогда; датчик отвечает на "сколько сейчас", мутирует, и то, что он оказывается на entity, - следствие того, что он такое - the owner said it
- decision: measure получает размеченный раздел <!-- measure --> … <!-- /measure -->, разрешённый в любой папке и необязательный везде; свойства в frontmatter не заводим - the owner said it: «Раздел... Принимается»
- decision: грамматика раздела measure и его постройка выносятся в отдельную сессию, а решение о форме записывается proposal'ом сегодня - the owner said it
- decision: строка measure обязана называть назначение, в скобках сразу после вида - measure: [slug] текст; легальные значения - слуг страницы, gauge:slug или none - the owner said it: «б. Принимаю твою рекомендацию»
- decision: датчик проверяется на единственность той же фигурой, что две current страницы с одним authority:; сама проверка откладывается, пока датчиков в корпусе почти нет - the owner said it
- decision: migrating-the-repository-to-english.md оставляет обе строки - sources: и decided_by:; обе истинны, а удаление правдивой строки ради чистоты стирает провенанс - the owner said it: «оставить как есть»
- miss: восемь из четырнадцати строк, подписанных "the owner said it", несли английский пересказ сессии вместо слов владельца - тот самый дефект, ради которого затевался ratification sweep, воспроизведённый в канале марок в тот же день, когда sweep прошёл. Слова существовали в transcript'е всё это время и были восстановлены извлечением за минуту
- decision: пропуск марок внутри retro не чинится сейчас - владелец смотрит, повторится ли он, и решает по повторению - the owner said it: «я посмотрю повторится это или нет. Если повторится - будем решать что делать»

## Anything else worth keeping

**The extract of this session's own dialogue was read before anything was recalled from memory**, as
`/retro` step 0 requires: 19 owner turns, 74 session replies, 2 menus — **both interrupted and
neither answered** — 21 feedback marks, 184,152 bytes. Of the retro's 26 open lines, **14 came from
the feedback marks and 7 were found by reading the extract**, with 5 more surfacing inside the retro
itself. The previous measured ratio was 4 from marks against 11 found by reading. The marks missed a
third here where they missed two thirds then.

**Both of this session's menus were interrupted and neither produced a ruling.** The owner answered
in prose immediately after each, at length, with conditions and counter-questions attached — the
shape a menu has no room for. No ruling this session arrived through an option label.

**Reading the two mechanisms apart before comparing the options is what unblocked the whole suite
conversation.** The owner had twice asked for the same two options «чуть проще»; what blocked him was
that the gate and its selftest were being discussed as one subject, and their names share a word.
Once split he did not merely follow the comparison — he improved it, proposing the
fast-run-plus-one-full-run shape that removed the only objection the live proposal records against
the option he then chose:

**owner:** «Очень хорошо, что ты обьяснил отдельно про gate и про suite. Не знаю какая именно
инструкция это дала, но стало лучше.»

**`--list` and the real run agreed at 173 on the first attempt**, which is the anti-drift case
working on the day it was written.

**The session contradicted itself in three places, and they are recorded rather than tidied.** It
argued all day that a number must be printed rather than maintained and then wrote a maintained
projection into the plan. It flagged the sweep-inside-a-build-session departure before it happened
and then let it happen two turns earlier without naming it again. And it refused to land the verdict
before the back-fill finished on an ordering it had itself shown could not bite — obedience to the
stated order was right, the reasoning published for it was not the reasoning that applied.

## Harness

- harness: catch-the-feedback.ps1:136 не разбирает строку с ведущим "- ", а именно такую форму показывает отрендеренное правило в CLAUDE.md:70-76; шаблон в vault-feedback.md:17-19 показывает форму без дефиса. Два рендера одного правила расходятся, хук понимает только второй. Чинить: regex '^\s*-?\s*([A-Za-z-]+)\s*:', без backticks - обе формы с backticks проверены и не матчатся
- harness: catch-the-feedback.ps1 пишет ОДИН вид на один fence (строки 135-149: один $kind с первой строки на весь блок), а CLAUDE.md показывает четыре вида в одном блоке. Чинить: одна запись на строку, начинающуюся с вида; строки с отступом - продолжение предыдущей
- harness: раздел "The four kinds a session writes" в .superpowers/sdd/vault-feedback.md обязан описать единый стандарт записи - одна строка одна запись, "- вид: текст", продолжение с отступом в два пробела, backticks только в прозе шапки - и новый обязательный элемент назначения у measure
- harness: hook-selftest.ps1 получает кейс на то, что запись не может содержать вид внутри тела другой записи - сегодня девять таких блоков прошли молча
- harness: марка decision: должна нести слова владельца дословно в тот же момент, когда пишется, а не только называть форму. Форму она называть научилась 2026-08-24, слова - нет, и разрыв между этими двумя обязательствами и есть восемь строк выше
