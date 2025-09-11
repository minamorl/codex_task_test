from __future__ import annotations

from fibonacci import fib_fast_doubling, fib_iterative, fib_memoized, fib_recursive

_iterative_mean: float | None = None


def test_benchmark_recursive(benchmark) -> None:
    benchmark(lambda: fib_recursive(20))


def test_benchmark_iterative(benchmark) -> None:
    global _iterative_mean
    benchmark(lambda: fib_iterative(10_000))
    _iterative_mean = benchmark.stats["mean"]


def test_benchmark_fast_doubling(benchmark) -> None:
    assert _iterative_mean is not None
    benchmark(lambda: fib_fast_doubling(10_000))
    fast_mean = benchmark.stats["mean"]
    assert fast_mean < _iterative_mean


def test_benchmark_memoized(benchmark) -> None:
    benchmark(lambda: fib_memoized(10_000))
