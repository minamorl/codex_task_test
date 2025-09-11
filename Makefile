.PHONY: setup lint typecheck test bench all

setup:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

lint:
	. .venv/bin/activate && ruff check src tests

typecheck:
	. .venv/bin/activate && mypy src

test:
	. .venv/bin/activate && PYTHONPATH=src pytest -q

bench:
	. .venv/bin/activate && mkdir -p out && PYTHONPATH=src pytest -q tests/test_bench.py --benchmark-only --benchmark-json out/bench.json

all: lint typecheck test
