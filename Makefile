# The single entry point for this repository's checks. `make help` lists them.
#
# Every recipe closes its own standard input. A PowerShell child spawned from a make recipe
# with stdin inherited hangs (measured 2026-08-26, forty-nine minutes once); no check here
# reads stdin, so closing it is correct everywhere, and one rule that always holds beats an
# exemption list somebody has to keep true.
#
# No target here writes to the working tree. A target that reports and a target that mutates
# are different kinds of thing.
#
# `test` arrived with Slice 1; `lint` and the per-MOC test pipelines with Slice 2, three more
# with Slice 3. `lint` only checks: the writers are `uv run guppi render`,
# `guppi generate` and `guppi cleanup`.
#
# Every recipe runs under a POSIX sh. On Windows, make started from PowerShell finds no
# `/usr/bin/sh` and would fall back to cmd.exe, where `< /dev/null` names no file; so it takes
# the sh of Git for Windows by its path, with its `usr/bin` first on PATH, and stops before any
# recipe when there is none (case 457).

SHELL := /usr/bin/sh
ifeq ($(OS),Windows_NT)
space := $(subst ,, )
# A `?` stands for a space: make's path functions split words on spaces.
POSIX_DIRS := C:/Program?Files/Git/usr/bin C:/Program?Files?(x86)/Git/usr/bin \
  $(subst $(space),?,$(subst \,/,$(LOCALAPPDATA)))/Programs/Git/usr/bin
POSIX_BIN := $(subst ?,$(space),$(firstword $(foreach d,$(POSIX_DIRS),$(if $(wildcard $(d)/sh.exe),$(d)))))
ifeq ($(POSIX_BIN),)
$(error no POSIX sh: sh.exe is in none of $(subst ?,$(space),$(POSIX_DIRS)); install Git for Windows)
endif
SHELL := $(POSIX_BIN)/sh.exe
export PATH := $(POSIX_BIN);$(PATH)
endif
.DEFAULT_GOAL := help
.PHONY: help style test lint test-session-start test-plan-mode test-documentation test-harness test-end-of-work

help: ## list these targets
	@awk 'BEGIN{FS=":.*## "} /^[a-z-]+:.*## /{printf "  %-7s %s\n", $$1, $$2}' $(MAKEFILE_LIST) < /dev/null

style: ## ruff over the Python in this repository; must be clean before every commit
	@uv run ruff check . < /dev/null
	@uv run ruff format --check . < /dev/null

test: ## pytest over the harness's own suite
	@uv run pytest -q < /dev/null

lint: ## the vault: the rendered harness, the sprint file, the backlog and the glossary match their sources, pages pass the checks; every step runs, red if any is (case 587)
	@status=0; \
	uv run guppi render --check < /dev/null || status=1; \
	uv run guppi sprint --check < /dev/null || status=1; \
	uv run guppi backlog --check < /dev/null || status=1; \
	uv run guppi glossary --check < /dev/null || status=1; \
	uv run guppi lint < /dev/null || status=1; \
	exit $$status

test-session-start: ## the pipeline over rule-session-start's children
	@uv run pytest -q tests/test_event.py tests/test_ledger.py < /dev/null

test-plan-mode: ## the pipeline over rule-plan-mode's children
	@uv run pytest -q tests/test_spec.py tests/test_prespec.py < /dev/null

test-documentation: ## the pipeline over rule-documentation's scripts
	@uv run pytest -q tests/test_materialize.py tests/test_generate.py tests/test_cleanup.py < /dev/null

test-harness: ## the pipeline over rule-harness's children
	@uv run pytest -q tests/test_render.py tests/test_lint.py < /dev/null

test-end-of-work: ## the pipeline over rule-end-of-work's children
	@uv run pytest -q tests/test_gate.py < /dev/null
