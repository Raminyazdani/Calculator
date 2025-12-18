import sys
from pathlib import Path

# Ensure the src/ directory is on sys.path so tests can import calculator_cli
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if SRC not in sys.path:
    sys.path.append(str(SRC))

