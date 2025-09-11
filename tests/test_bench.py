from __future__ import annotations

from fibonacci import fib_fast_doubling, fib_recursive


def test_benchmark_recursive(benchmark) -> None:
    benchmark(lambda: fib_recursive(20))


def test_benchmark_fast_doubling(benchmark) -> None:
    benchmark(lambda: fib_fast_doubling(10_000))
