"""
Loose Wrapping around Archidekt Categories
"""
from __future__ import annotations
from .cards import ArchidektCard
from dataclasses import dataclass, field
from typing import List


@dataclass
class Category:
    id: int = field(default=-1)
    name: str = field(default="")
    included_in_deck: bool = field(default=False)
    included_in_price: bool = field(default=False)
    is_premier: bool = field(default=False)
    cards: List[ArchidektCard] = field(default_factory=list)

    @staticmethod
    def fromJson(data: dict) -> Category:
        return Category(
            id=data["id"],
            name=data["name"],
            included_in_deck=data["includedInDeck"],
            included_in_price=data["includedInPrice"],
            is_premier=data["isPremier"]
        )