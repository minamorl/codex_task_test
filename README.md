# Fibonacci Toolkit

Minimal toolkit providing several Fibonacci implementations, a CLI, tests,
benchmarks and a self-checking CI gate.

## Quickstart
```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
make ci
python -u tools/ci_selfcheck.py
```
If every step succeeds the final line will be `CI_PASS`.

## CLI Examples
```bash
# Single number
fib fib 30 --method fast
fib fib -8 --neg --method fast

# Range output as JSON
fib fib-range 5 10 --json
```

## Self-Check Protocol
Running `python -u tools/ci_selfcheck.py` verifies installed dependencies and
executes linting, type checks and tests exactly as the CI pipeline.
Success is indicated by the final line:
```
CI_PASS
```
