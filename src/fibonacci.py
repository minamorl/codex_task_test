from __future__ import annotations


def fib_recursive(n: int) -> int:
    """Compute the nth Fibonacci number using recursion.

    Args:
        n: Non-negative integer

    Returns:
        nth Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """Compute the nth Fibonacci number using iteration.

    Args:
        n: Non-negative integer

    Returns:
        nth Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
