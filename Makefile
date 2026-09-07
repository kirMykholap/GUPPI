# The single entry point for this repository's checks.
#
# WHY THIS FILE EXISTS. Running "the checks" was four commands typed by hand, and the fourth is the
# one somebody forgets. The names `gate`, `smoke` and `suite` were decided on 2026-08-26 and mean
# different things; this file is where each of them becomes exactly one command, which is the half
# of that decision the names alone do not buy.
#
# THE TARGET IS `style` AND NOT `lint`, DELIBERATELY. In this repository `lint` already means two
# things - `/vault-lint`, the per-sprint audit, and `bash scripts/vault-check.sh --lint`, the
# advisory channel. A third meaning is the collision the naming decision was written against, and
# the precedent it names is `retrospective`, which meant two rituals for three days and put two
# live contradictory answers in the vault about when `/ingest` runs.
#
# `smoke` DOES NOT USE PREREQUISITES, AND THAT IS THE POINT. `smoke: gate style` reads better and
# is wrong: make aborts a target when a prerequisite fails, so a red gate would hide whether the
# selftests pass. A run taken before handing work over has to report every verdict it has, not the
# first one it hits. So each step is invoked through `$(MAKE)` or directly, its failure is caught
# with `||`, and the accumulated code is what the target exits with.
#
# `scripts` JOINED THE CHECK HALF ON 2026-08-31 AND NOT THE FORMAT HALF, and the asymmetry is
# deliberate rather than an oversight. The folder had never been linted at all: two files written
# that day produced 21 findings no target could see, and the whole folder produced 10 more. Those
# are fixed and the check is clean. `ruff format --check scripts` would fail on SIX existing files,
# and reformatting scripts nobody was reviewing is a diff of its own - it belongs in a change where
# someone reads it, not smuggled into the target that made the check honest (owner, 2026-08-31,
# «Да, добавляем», put to him with the cost of the ten findings measured first).
#
# NO TARGET HERE WRITES. `style` runs `ruff format --check` rather than `ruff format`, and there is
# no target for `scripts/vault-inject.sh`, which edits tracked files. A target that reports and a
# target that mutates the working copy are different kinds of thing, and nothing in this project
# decides that a build target may perform the register write ritual.
#
# EVERY RECIPE CLOSES ITS OWN STANDARD INPUT, AND THAT IS A MEASUREMENT RATHER THAN TIDINESS.
# `powershell.exe -File scripts/hook-selftest.ps1` run from a make recipe with stdin inherited HANGS
# - measured 2026-08-26: killed at 100 s with zero CPU consumed, and a first attempt sat for
# forty-nine minutes before anyone looked. The same command with `< /dev/null` finishes in 43 s and
# reports `caught 169, missed 0`. The suite spawns about a hundred and seventy child processes it
# feeds through pipes, and an inherited console handle that never closes is what they wait on.
#
# THE RULE IS EVERY LINE AND NOT THE ONE THAT BIT, deliberately. No check in this file reads
# standard input, so closing it is correct everywhere, and one rule that always holds is worth more
# than an exemption list somebody has to keep true. A timeout would not have helped and is not the
# fix: an MSYS signal does not reach a native Windows process, which this repository has measured
# twice and paid for three times - `timeout 330` returned here having killed make and bash and left
# two powershells running.
#
# `exec < /dev/null` AT THE HEAD OF THE RECIPE DOES NOT WORK, AND IT WAS TRIED. It reads as the
# tidier form - one redirection for the whole block - and the run hung at the same step with it in
# place, twice, against three runs that finished with the redirection written on the command itself.
# Whatever `exec` does to this shell's own descriptor, it is not what the spawned process inherits.
# The per-command form is the one with a measurement behind it, so it is the one written here, and
# a later reader tempted to collapse it should collapse it and time the result.
#
# RECURSION IS NOT THE CAUSE, ALSO MEASURED. `hook-selftest.ps1` invoked from a recipe that had just
# run a sub-make finished in 42 s, exactly as one invoked with no recursion at all did. The
# jobserver was the first suspect and it was wrong.

# THE PRODUCT LEFT THIS REPOSITORY ON 2026-09-07. `src/` and `tests/` are gone with it, so `style`
# covers `scripts/` alone and there is no `test` target: the only suites here are the harness's own,
# and `smoke` runs them. The paragraph above about `ruff format --check` still holds for `scripts/`.

SHELL := /usr/bin/sh
.DEFAULT_GOAL := help
.PHONY: help gate smoke suite style

help: ## list these targets
	@awk 'BEGIN{FS=":.*## "} /^[a-z-]+:.*## /{printf "  %-7s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

gate: ## structural rules over the live vault corpus
	@bash scripts/vault-check.sh < /dev/null

style: ## ruff over the scripts, must be clean before every commit
	@uv run ruff check scripts < /dev/null

# The narrowed slice is named by the session and never inferred from a diff: a session that edited
# rule 15 and ran rule 11's case proves nothing, and nothing would catch that. With no ONLY= the
# floor still runs, which is a legal run rather than a degraded one.
smoke: ## fast check of the whole repository; ONLY=<pattern> adds a slice of the suite
	@fail=0; \
	echo "== gate";     $(MAKE) -s gate                                                     < /dev/null || fail=1; \
	echo "== style";    $(MAKE) -s style                                                    < /dev/null || fail=1; \
	echo "== hooks";    powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts/hook-selftest.ps1 < /dev/null || fail=1; \
	echo "== dialogue"; uv run python scripts/session-dialogue-selftest.py                  < /dev/null || fail=1; \
	echo "== measure";  uv run python scripts/vault-measure-selftest.py                     < /dev/null || fail=1; \
	if [ -n "$(ONLY)" ]; then \
	  echo "== suite slice: $(ONLY)"; \
	  bash scripts/vault-check-selftest.sh --only '$(ONLY)'                                 < /dev/null || fail=1; \
	fi; \
	if [ $$fail -eq 0 ]; then echo "SMOKE-EXIT: 0 (ok)"; else echo "SMOKE-EXIT: $$fail (FAILED)"; fi; \
	exit $$fail

# `smoke` is a subset of this by construction, so the whole selftest of the gate is what `suite`
# adds. It costs about an hour and runs at a sprint's close or in a rare case somebody names.
suite: ## the full sweep - smoke plus the gate's own selftest, about an hour
	@fail=0; \
	$(MAKE) -s smoke                                                                        < /dev/null || fail=1; \
	echo "== suite";    bash scripts/vault-check-selftest.sh                                < /dev/null || fail=1; \
	if [ $$fail -eq 0 ]; then echo "SUITE-EXIT: 0 (ok)"; else echo "SUITE-EXIT: $$fail (FAILED)"; fi; \
	exit $$fail
