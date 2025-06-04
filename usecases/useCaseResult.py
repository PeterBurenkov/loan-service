from __future__ import annotations
from dataclasses import dataclass


@dataclass
class UseCaseResult:
    success: bool
    message: str
    data: dict | None = None
