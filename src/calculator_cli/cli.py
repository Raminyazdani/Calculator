from __future__ import annotations

import argparse
import sys

from rich.console import Console

from . import __version__
from .core import CalculationError, evaluate_expression
from .themes import ThemeManager
from .tui import run


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Rich + prompt_toolkit calculator")
    parser.add_argument("expr", nargs="?", help="evaluate a single expression and exit")
    parser.add_argument("--theme", choices=["light", "dark", "bright_blue"], help="set initial theme")
    parser.add_argument("--version", action="version", version=f"calculator-cli {__version__}")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    args = parse_args(argv)
    theme = ThemeManager(name=args.theme or "light")
    console = theme.build_console()

    if args.expr:
        try:
            result = evaluate_expression(args.expr)
        except CalculationError as exc:
            console.print(f"error: {exc}", style="error")
            return 1
        console.print(f"= {result.value}", style="result")
        return 0

    run(initial_theme=args.theme)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
