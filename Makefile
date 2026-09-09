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
# `lint` (the vault) and `test` (the harness's own suite) arrive with Slice 2, when the code
# they run exists.

SHELL := /usr/bin/sh
.DEFAULT_GOAL := help
.PHONY: help style

help: ## list these targets
	@awk 'BEGIN{FS=":.*## "} /^[a-z-]+:.*## /{printf "  %-7s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

style: ## ruff over the Python in this repository; must be clean before every commit
	@uv run ruff check . < /dev/null
	@uv run ruff format --check . < /dev/null
