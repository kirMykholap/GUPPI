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

SHELL := /usr/bin/sh
.DEFAULT_GOAL := help
.PHONY: help style test lint test-session-start test-plan-mode test-documentation test-harness test-end-of-work

help: ## list these targets
	@awk 'BEGIN{FS=":.*## "} /^[a-z-]+:.*## /{printf "  %-7s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

style: ## ruff over the Python in this repository; must be clean before every commit
	@uv run ruff check . < /dev/null
	@uv run ruff format --check . < /dev/null

test: ## pytest over the harness's own suite
	@uv run pytest -q < /dev/null

lint: ## the vault: the rendered harness matches its pages, pages pass the checks
	@uv run guppi render --check < /dev/null
	@uv run guppi lint < /dev/null

test-session-start: ## the pipeline over rule-session-start's children
	@uv run pytest -q tests/test_event.py tests/test_ledger.py < /dev/null

test-plan-mode: ## the pipeline over rule-plan-mode's children
	@uv run pytest -q tests/test_spec.py tests/test_pretask.py < /dev/null

test-documentation: ## the pipeline over rule-documentation's scripts
	@uv run pytest -q tests/test_materialize.py tests/test_generate.py tests/test_cleanup.py < /dev/null

test-harness: ## the pipeline over rule-harness's children
	@uv run pytest -q tests/test_render.py tests/test_lint.py < /dev/null

test-end-of-work: ## the pipeline over rule-end-of-work's children
	@uv run pytest -q tests/test_gate.py < /dev/null
