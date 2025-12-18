# Calculator (TUI)

Python 3.10 terminal calculator with history, light/dark themes, and a Rich + prompt_toolkit interface. Ships as a CLI, documented for GitHub Pages, and developed with narrated step-by-step commits.

## Features
- Basic arithmetic with safe expression evaluation
- Command history view and replay
- Light/dark theme toggle for the UI output
- Help/commands inside the TUI; CLI entrypoint for quick runs
- Docs site (GitHub Pages) with usage and roadmap

## Stack
- Python 3.10
- prompt_toolkit for the prompt loop and keybindings
- Rich for styled output and theming

## Setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .             # install the package so `python -m calculator_cli.cli` works
```

## Run
```powershell
python -m calculator_cli.cli               # launch TUI (after pip install -e .)
python -m calculator_cli.cli "1+2*3"      # one-off expression
python -m calculator_cli.cli --theme dark  # start with dark theme
python -m calculator_cli.cli --theme bright_blue  # start with bright blue theme
python -m calculator_cli.cli --version     # show version
```

## Tests
```powershell
pytest
```

## Docs
- Docs: see `docs/index.md` (deployed via GitHub Pages).

## License
- MIT (see `LICENSE.md`).

## Changelog
- See `CHANGELOG.md` (current: 0.1.0 initial release).

## Roadmap / TODO
- [x] Core: safe expression parser + arithmetic engine
- [x] History: in-memory store with optional persistence
- [x] TUI: prompt_toolkit loop with Rich-rendered panels
- [x] Themes: light/dark palettes and toggle command
- [x] CLI: command help, exit, history navigation, errors
- [x] Tests: unit tests for core + interaction mocks for TUI
- [x] Docs: usage guide, GitHub Pages workflow
- [x] Polish: packaging metadata, release notes

## Commit Plan (narrated)
1. Scaffold project, dependencies, and TODOs.
2. Implement core evaluator with tests.
3. Wire TUI shell (history + theme toggle) to core.
4. Polish CLI UX, error handling, and packaging metadata.
5. Add docs and GitHub Pages publishing.

## GitHub Pages (docs plan)
- Publish static docs from `docs/` via Pages workflow.
- Include quickstart, feature tour, and commands list.
