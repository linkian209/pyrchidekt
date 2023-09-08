"""
Edition Wrapper
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Any


@dataclass
class Edition:
    code: str
    name: str
    date: date
    type: str
    mtgo_code: Any

    @staticmethod
    def fromJson(data: dict) -> Edition:
        return Edition(
            data['editioncode'],
            data['editionname'],
            date.fromisoformat(data['editiondate']),
            data['editiontype'],
            data['mtgoCode']
        )