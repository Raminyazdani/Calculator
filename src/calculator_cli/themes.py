from __future__ import annotations

from dataclasses import dataclass
from rich.console import Console
from rich.theme import Theme


THEMES = {
    "light": Theme({
        "prompt": "cyan",
        "result": "bold green",
        "error": "bold red",
        "meta": "dim",
    }),
    "dark": Theme({
        "prompt": "bright_cyan",
        "result": "bold bright_green",
        "error": "bold bright_red",
        "meta": "grey62",
    }),
    "bright_blue": Theme({
        "prompt": "bold bright_blue",
        "result": "bold blue",
        "error": "bright_blue",
        "meta": "blue",
    }),
}
THEME_ORDER = ["light", "dark", "bright_blue"]


@dataclass
class ThemeManager:
    name: str = "light"

    def __post_init__(self) -> None:
        if self.name not in THEMES:
            self.name = "light"

    def build_console(self) -> Console:
        return Console(theme=THEMES[self.name])

    def toggle(self) -> None:
        idx = THEME_ORDER.index(self.name)
        self.name = THEME_ORDER[(idx + 1) % len(THEME_ORDER)]
