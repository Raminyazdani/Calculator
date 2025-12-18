from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .core import EvaluationResult


@dataclass
class History:
    entries: List[EvaluationResult] = field(default_factory=list)

    def add(self, result: EvaluationResult) -> None:
        self.entries.append(result)

    def last(self, n: int = 1) -> list[EvaluationResult]:
        return self.entries[-n:]

    def clear(self) -> None:
        self.entries.clear()

