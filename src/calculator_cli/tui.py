from __future__ import annotations

from typing import Optional
from prompt_toolkit.formatted_text import FormattedText

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from rich.panel import Panel

from .core import CalculationError, evaluate_expression
from .history import History
from .themes import ThemeManager

HELP_TEXT = """Commands:
- :help          show this help
- :history       show recent calculations
- :clear         clear history
- :theme         cycle light/dark/bright_blue
- :quit / :exit  exit
Otherwise, type an expression (e.g., 1 + 2 * 3) and press Enter.
"""


class CalculatorTUI:
    def __init__(self, initial_theme: Optional[str] = None) -> None:
        self.theme = ThemeManager(name=initial_theme or "light")
        self.console = self.theme.build_console()
        self.history = History()
        self.session = PromptSession(completer=WordCompleter([
            ":help", ":history", ":clear", ":theme", ":quit", ":exit",
        ], ignore_case=True))
        self.bindings = self._build_bindings()

    def _build_bindings(self) -> KeyBindings:
        kb = KeyBindings()

        @kb.add("c-c")
        @kb.add("c-d")
        def _(event) -> None:  # noqa: ANN001
            event.app.exit()

        return kb

    def run(self) -> None:
        self.console.print(Panel("Rich + prompt_toolkit Calculator\nType :help for commands", style="meta"))
        while True:
            try:
                text = self.session.prompt(self._prompt_tokens, key_bindings=self.bindings, style=self._prompt_style)
            except (KeyboardInterrupt, EOFError):
                self.console.print("\nbye!", style="meta")
                break

            stripped = text.strip()
            if not stripped:
                continue
            if stripped in {":quit", ":exit"}:
                self.console.print("bye!", style="meta")
                break
            if stripped == ":help":
                self.console.print(Panel(HELP_TEXT, title="Help", style="meta"))
                continue
            if stripped == ":history":
                self._print_history()
                continue
            if stripped == ":clear":
                self.history.clear()
                self.console.print("history cleared", style="meta")
                continue
            if stripped == ":theme":
                self.theme.toggle()
                self.console = self.theme.build_console()
                self.console.print(f"theme switched to {self.theme.name}", style="meta")
                continue

            self._handle_expression(stripped)

    def _handle_expression(self, expr: str) -> None:
        try:
            result = evaluate_expression(expr)
        except CalculationError as exc:
            self.console.print(f"error: {exc}", style="error")
            return
        self.history.add(result)
        self.console.print(f"= {result.value}", style="result")

    def _print_history(self) -> None:
        if not self.history.entries:
            self.console.print("(empty)", style="meta")
            return
        lines = [f"{idx+1}. {entry.expression} = {entry.value}" for idx, entry in enumerate(self.history.entries)]
        self.console.print(Panel("\n".join(lines), title="History", style="meta"))

    @property
    def _prompt_style(self) -> Style:
        return Style.from_dict({"prompt": "ansicyan bold"})

    @property
    def _prompt_tokens(self) -> FormattedText:
        return FormattedText([("class:prompt", "calc> ")])


def run(initial_theme: Optional[str] = None) -> None:
    CalculatorTUI(initial_theme=initial_theme).run()
