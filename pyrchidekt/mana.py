"""
Mana Production wrapper
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ManaProduction:
    white: int
    blue: int
    black: int
    red: int
    green: int
    colorless: int

    @staticmethod
    def fromJson(data: dict) -> ManaProduction:
        return ManaProduction(
            data["W"],
            data["U"],
            data["B"],
            data["R"],
            data["G"],
            data["C"]
        )
