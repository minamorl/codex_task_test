"""Command-line interface for Fibonacci toolkit."""
from __future__ import annotations

import argparse
import json
import sys
from typing import Callable

from .core import (
    fib_fast_doubling,
    fib_iterative,
    fib_memoized,
    fib_neg,
    fib_range,
    fib_recursive,
)

METHODS: dict[str, Callable[[int], int]] = {
    "recursive": fib_recursive,
    "iterative": fib_iterative,
    "fast": fib_fast_doubling,
    "memo": fib_memoized,
}


def main(argv: list[str] | None = None) -> int:
    """Entry point for the ``fib`` command."""
    parser = argparse.ArgumentParser(prog="fib")
    sub = parser.add_subparsers(dest="command", required=True)

    fib_p = sub.add_parser("fib", help="compute single Fibonacci number")
    fib_p.add_argument("n", type=int)
    fib_p.add_argument("--method", choices=METHODS.keys(), default="fast")
    fib_p.add_argument("--neg", action="store_true")
    fib_p.add_argument("--mod", type=int)

    range_p = sub.add_parser("fib-range", help="compute range of Fibonacci numbers")
    range_p.add_argument("start", type=int)
    range_p.add_argument("stop", type=int)
    range_p.add_argument("--method", choices=METHODS.keys(), default="fast")
    range_p.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)

    try:
        if args.command == "fib":
            n: int = args.n
            if n < 0 and not args.neg:
                raise ValueError("negative n requires --neg")
            func = fib_neg if args.neg else METHODS[args.method]
            result = func(n)
            if args.mod is not None:
                result %= args.mod
            print(result)
        else:
            result_list = fib_range(args.start, args.stop, method=args.method)
            if args.json:
                print(json.dumps(result_list))
            else:
                print(" ".join(str(x) for x in result_list))
        return 0
    except (ValueError, TypeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
