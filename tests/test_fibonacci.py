import pytest
from src.fibonacci import fib_recursive, fib_iterative


@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (10, 55),
])
def test_fib_recursive(n: int, expected: int) -> None:
    assert fib_recursive(n) == expected


@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (10, 55),
])
def test_fib_iterative(n: int, expected: int) -> None:
    assert fib_iterative(n) == expected


def test_negative_input() -> None:
    with pytest.raises(ValueError):
        fib_recursive(-1)
    with pytest.raises(ValueError):
        fib_iterative(-1)
