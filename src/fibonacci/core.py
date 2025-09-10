"""Core Fibonacci implementations."""
from __future__ import annotations

from functools import lru_cache
from typing import Callable


def _ensure_int(n: int) -> None:
    if not isinstance(n, int):
        raise TypeError("n must be an int")


def fib_recursive(n: int) -> int:
    """Compute the n-th Fibonacci number recursively.

    Parameters
    ----------
    n: int
        Index (n >= 0).
    """
    _ensure_int(n)
    if n < 0:
        raise ValueError("n must be non-negative")
    import sys
    sys.setrecursionlimit(max(3000, n + 50))
    if n in (0, 1):
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """Compute the n-th Fibonacci number using iteration."""
    _ensure_int(n)
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_fast_doubling(n: int) -> int:
    """Compute the n-th Fibonacci number using fast-doubling.

    Runs in O(log n) time.
    """
    _ensure_int(n)
    if n < 0:
        raise ValueError("n must be non-negative")

    def _fib(k: int) -> tuple[int, int]:
        if k == 0:
            return (0, 1)
        a, b = _fib(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k % 2 == 0:
            return (c, d)
        return (d, c + d)

    return _fib(n)[0]


@lru_cache(maxsize=None)
def _fib_pair(n: int) -> tuple[int, int]:
    if n == 0:
        return (0, 1)
    a, b = _fib_pair(n // 2)
    c = a * (2 * b - a)
    d = a * a + b * b
    if n % 2 == 0:
        return (c, d)
    return (d, c + d)


def fib_memoized(n: int) -> int:
    """Compute the n-th Fibonacci number using memoization."""
    _ensure_int(n)
    if n < 0:
        raise ValueError("n must be non-negative")
    return _fib_pair(n)[0]

def fib_neg(n: int) -> int:
    """Compute Fibonacci numbers for negative indices.

    For n >= 0, behaves like :func:`fib_fast_doubling`.
    For n < 0, uses F(-n) = (-1)^(n+1) F(n).
    """
    _ensure_int(n)
    if n >= 0:
        return fib_fast_doubling(n)
    k = -n
    result = fib_fast_doubling(k)
    return -result if k % 2 == 0 else result


_METHODS: dict[str, Callable[[int], int]] = {
    "recursive": fib_recursive,
    "iterative": fib_iterative,
    "fast": fib_fast_doubling,
    "memo": fib_memoized,
}


def fib_range(start: int, stop: int, method: str = "fast") -> list[int]:
    """Return Fibonacci numbers for the inclusive range [start, stop]."""
    _ensure_int(start)
    _ensure_int(stop)
    if start < 0 or stop < 0 or start > stop:
        raise ValueError("invalid range")
    func = _METHODS.get(method)
    if func is None:
        raise ValueError("unknown method")
    return [func(i) for i in range(start, stop + 1)]
