# Calculator TUI

Python terminal calculator with Rich + prompt_toolkit. Supports one-off expression evaluation, interactive history, and light/dark themes.

## Quickstart
- Create venv & install:
  - Windows: `python -m venv .venv && ./.venv/Scripts/Activate.ps1 && pip install -r requirements.txt`
  - macOS/Linux: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
- Interactive TUI: `python -m calculator_cli.cli`
- One-off expression: `python -m calculator_cli.cli "1+2*3"`
- Start with dark theme: `python -m calculator_cli.cli --theme dark`
- Show version: `python -m calculator_cli.cli --version`

## Commands (inside TUI)
- `:help` — show help
- `:history` — list calculations for this session
- `:clear` — clear history
- `:theme` — toggle light/dark theme
- `:quit` / `:exit` — exit

## Examples
- `2 + 2 * 3`
- `(5 - 3) ** 2`
- `10 // 3`

## Notes
- Division by zero and invalid syntax are reported as errors.
- History is in-memory for the current session.

## Project
- Code and README are in the repository root.
- GitHub Pages publishes this `docs/` folder.
