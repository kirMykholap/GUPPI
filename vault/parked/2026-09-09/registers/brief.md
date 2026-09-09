# Brief — 2026-09-07
generated-at: 283c8ac
ingested: 2026-08-31-the-families-become-rules.md

**This brief is hand-written by the session, on the owner's decision, and no ingest produced it.**
The last ingest was the one named above; every ingest before this date is in `log.md`. The
librarian did not run and is not to be dispatched until the owner says so.

## What this repository is

The harness around Claude Code sessions and the Obsidian vault they compile into: hooks that
fire around a session, skills for its rituals, agents that read and write the vault, and the
scripts that check the vault against its own schema. It was split out of the `job hunt ai`
repository on 2026-09-07 with the whole history; that repository keeps the job-hunting product
on its `main`, tagged `vault-v1` at the split.

**How the harness works, whole, is on one page: [[harness-map]]** (`job_hunt_ai_vault/harness-map.md`).
Read it before anything else. It was written from the files, not from the wiki, on the day of the
split, and it is the baseline the owner's new plan is compared against.

## What the owner decided on 2026-09-07, and why

- **The frontier of 18 items carried from 2026-08-31 is cancelled.** «я хочу отменить весь
  фронтир». None of it is worked; it is input to the migration that follows.
- **The value here is the harness and the vault, not the product.** «большую ценность для меня
  сейчас несёт именно та часть, которая про харнесс и работу с Вики». The product left.
- **`entities`, `rules` and `lessons` stay live. `decisions` and `concepts` are parked.** His
  ground: the working harness is described in entities and rules; decisions govern nothing, they
  are records we read, and reading 218 of them into every `/pre-task` is what opened a session at
  about 200,000 tokens. Most of them are stale in his reading. Lessons were the session's addition
  and he accepted it: all 31 are about the harness, and they are the traps that cost hours.
- **The gate and every harness selftest are switched off for now** — by nobody running them, not
  by editing anything. `make gate`, `make smoke`, `make suite` still exist and will be red on
  broken links until the new system says what a link is.
- **`CLAUDE.md` is not rewritten and no hook is unregistered.** «переписывать Claude.md и
  отключать хуки - плохая идея». `settings.json` is exactly as it was.
- **The rituals are ignored and the librarian is not dispatched.** `/pre-task`, `/retro`,
  `/handoff`, `/ingest` — none of them ran for the split, on his explicit permission: «Ритуал мы
  игнорируем, библиотекаря не запускаем. Даю на это полное разрешение». The hooks that ask for
  them are advisory and will keep asking; that is expected.
- **The next session compares his new plan against the map and adopts it piece by piece**, on a
  clean context. The plan lives outside this repository until he brings it.

## What is where

**Live, under `wiki/`** — 162 pages: entities 44, rules 35, lessons 31, proposals 52. Proposals are
untouched; what happens to them is for the new plan.

**Parked, under `parked/`** — 369 pages, set aside and not retired: `parked/decisions/` (218),
`parked/concepts/` (147), `parked/entities/` (3, about the product), `parked/rules/` (1, about
the product's source layers). Their `_schema.yaml` files moved with them. `parked/` is outside
`wiki/` because the scripts, the catalogue and `/pre-task` read `wiki/` alone; Obsidian and `grep`
still see everything. It is not `archive/`: that folder holds pages that were retired, and these
were not.

**Left as they were** — `archive/` (the retired pages and the compiled journals), `raw/` (the
owner's notes of 2026-08-13 on the second brain, and an empty `handoffs/`), `docs/`,
`.superpowers/`, and the five registers.

## Do not read these to learn the state

- **`sprint.md`** — 1,973 lines. S3 is nominally open, but its whole frontier was cancelled and
  the file describes the state before the split. Nothing in it is current work.
- **`log.md`** — the librarian's actions up to 2026-08-31. History, not state.
- **`index.md`, `tags.md`, `authority.md`** — they still list the parked pages as if they were in
  `wiki/`. `bash scripts/vault-authority.sh --check` will report the drift; that is the parking,
  not a defect to repair before the new plan says what these registers become.

## Known false, and left so on purpose

- **The first paragraph of `CLAUDE.md` describes the job-hunting product**, which is no longer
  here. It is rendered from the rule page `the-map-in-claude-md-is-the-vault-its-librarian-and-the-sprint`
  and is corrected there, through `bash scripts/vault-inject.sh`, when the gate comes back. Not by
  hand: an edited region reads as drift the moment the gate runs.
- **Every `[[wikilink]]` into a parked page is broken from `wiki/`'s point of view.** Rule 4 of the
  gate will name all of them. That is the parking, counted.
- **`docs/who-reads-the-vault.md`, `docs/vault-cleanup-*.md`** describe the cleanup of 2026-08-30
  and 2026-08-31 as it stood then, including families whose decisions are now parked.

## What the next session does

1. Read [[harness-map]].
2. Take the owner's plan when he brings it, and compare it against the map, one mechanism at a
   time: keep, remove, rework.
3. Build the new system piece by piece, each piece admitted when a session has actually needed it.
   The harness reached 14 hooks and 20 scripts by admitting one per incident; that is the shape
   to avoid.

## Readings at the split, each from its own invocation

- `git log --oneline -1` in this repository: the commit that carries this brief; the split is
  the commits above `afb1b91`.
- `find job_hunt_ai_vault/wiki -name '*.md' | wc -l` → 162.
- `bash scripts/vault-catalogue.sh | wc -c` → 32,957, against 115,326 before the parking and
  201,927 before the cleanup of 2026-08-30 began.
- `make style` → clean over `scripts/`.
- `make gate` — **not run**, expected red on links into `parked/`.

## One platform trap met at the split

**A clone of this repository on Windows needs `git config core.longpaths true` before checkout
finishes.** The longest tracked path is 240 characters under the repository root, and the first
clone stopped with `Filename too long` on a coverage sidecar under `archive/2026-08-26/`. The
source repository already carried the setting; a fresh clone does not inherit it.
