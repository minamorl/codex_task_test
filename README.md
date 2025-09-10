# Fibonacci Toolkit

A minimal Fibonacci toolkit showcasing multiple implementations, tests, benchmarks, and a CLI.

## Installation
```bash
pip install -e .
```

## CLI Usage
```bash
# Single Fibonacci number
python -m fibonacci.cli fib 30 --method fast
python -m fibonacci.cli fib -30 --neg --method fast

# Range of numbers
python -m fibonacci.cli fib-range 5 10 --json
```

## Development
```bash
make setup
make lint
make typecheck
make test
make bench
```

## Complexity
- Recursive: exponential
- Iterative: O(n)
- Fast doubling: O(log n)
