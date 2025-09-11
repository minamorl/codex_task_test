from hypothesis import given, settings
from hypothesis import strategies as st

from fibonacci import fib_fast_doubling, fib_neg

hp_settings = settings(deadline=None, max_examples=100)


@given(st.integers(min_value=1, max_value=20_000), st.integers(min_value=1, max_value=20_000))
@hp_settings
def test_addition_formula(m: int, n: int) -> None:
    lhs = fib_fast_doubling(m + n)
    rhs = (
        fib_fast_doubling(m - 1) * fib_fast_doubling(n)
        + fib_fast_doubling(m) * fib_fast_doubling(n + 1)
    )
    assert lhs == rhs


@given(st.integers(min_value=0, max_value=20_000))
@hp_settings
def test_doubling_even(k: int) -> None:
    lhs = fib_fast_doubling(2 * k)
    rhs = fib_fast_doubling(k) * (2 * fib_fast_doubling(k + 1) - fib_fast_doubling(k))
    assert lhs == rhs


@given(st.integers(min_value=0, max_value=20_000))
@hp_settings
def test_doubling_odd(k: int) -> None:
    lhs = fib_fast_doubling(2 * k + 1)
    rhs = fib_fast_doubling(k + 1) ** 2 + fib_fast_doubling(k) ** 2
    assert lhs == rhs


@given(st.integers(min_value=2, max_value=20_000))
@hp_settings
def test_monotonicity(n: int) -> None:
    assert fib_fast_doubling(n + 1) > fib_fast_doubling(n)


@given(st.integers(min_value=1, max_value=20_000))
@hp_settings
def test_negafib_property(n: int) -> None:
    assert fib_neg(-n) == ((-1) ** (n + 1)) * fib_fast_doubling(n)
