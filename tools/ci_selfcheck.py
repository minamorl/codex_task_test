#!/usr/bin/env python3
"""Local CI self-check script."""
from __future__ import annotations

import importlib
import json
import os
import pathlib
import subprocess
import sys
from typing import Dict

ROOT = pathlib.Path(__file__).resolve().parents[1]
REQ_FILE = ROOT / "requirements.txt"


def verify_requirements() -> None:
    """Import all packages listed in requirements.txt."""
    for line in REQ_FILE.read_text().splitlines():
        pkg = line.strip()
        if not pkg or pkg.startswith("#"):
            continue
        module = pkg.split("==")[0].split("[")[0].replace("-", "_")
        importlib.import_module(module)


def run_cmd(cmd: list[str]) -> int:
    """Run a subprocess command and return its return code."""
    env = dict(os.environ)
    if cmd[0] == "pytest":
        env["PYTHONPATH"] = "src"
    result = subprocess.run(cmd, env=env)
    return result.returncode


def main() -> int:
    verify_requirements()
    summary: Dict[str, str] = {}
    commands = {
        "lint": ["ruff", "check", "src", "tests"],
        "typecheck": ["mypy", "src"],
        "tests": ["pytest", "-q"],
    }
    overall_ok = True
    for key, cmd in commands.items():
        code = run_cmd(cmd)
        summary[key] = "ok" if code == 0 else "fail"
        overall_ok &= code == 0
    print(json.dumps(summary))
    if overall_ok:
        print("CI_PASS")
        return 0
    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
