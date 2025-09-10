from typing import Callable

import pytest

from fibonacci import (
    fib_fast_doubling,
    fib_iterative,
    fib_memoized,
    fib_neg,
    fib_recursive,
)

CASES = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (10, 55),
    (20, 6765),
    (30, 832040),
]


@pytest.mark.parametrize("n, expected", CASES)
def test_values(n: int, expected: int) -> None:
    assert fib_recursive(n) == expected
    assert fib_iterative(n) == expected
    assert fib_fast_doubling(n) == expected
    assert fib_memoized(n) == expected


def test_cross_method_consistency() -> None:
    for n in range(31):
        results = {
            fib_recursive(n),
            fib_iterative(n),
            fib_fast_doubling(n),
            fib_memoized(n),
        }
        assert len(results) == 1


@pytest.mark.parametrize("n", range(1, 31))
def test_negafib_identity(n: int) -> None:
    assert fib_neg(-n) == ((-1) ** (n + 1)) * fib_fast_doubling(n)


@pytest.mark.parametrize("func", [
    fib_recursive,
    fib_iterative,
    fib_fast_doubling,
    fib_memoized,
])
def test_negative_input_error(func: Callable[[int], int]) -> None:
    with pytest.raises(ValueError):
        func(-1)


@pytest.mark.parametrize("func", [
    fib_recursive,
    fib_iterative,
    fib_fast_doubling,
    fib_memoized,
    fib_neg,
])
def test_type_error(func: Callable[[int], int]) -> None:
    with pytest.raises(TypeError):
        func(1.5)  # type: ignore[arg-type]
