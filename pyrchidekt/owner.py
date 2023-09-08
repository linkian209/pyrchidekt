"""
Loose wrapping around deck owner. No PII other than a username and id.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Owner:
    id: int
    username: str
    avatar: str
    frame: Any
    ck_affiliate: str
    tcg_affiliate: str
    referrer_enum: Any

    @staticmethod
    def fromJson(data: dict) -> Owner:
        return Owner(
            id=data["id"],
            username=data["username"],
            avatar=data["avatar"],
            frame=data["frame"],
            ck_affiliate=data["ckAffiliate"],
            tcg_affiliate=data["tcgAffiliate"],
            referrer_enum=data["referrerEnum"]
        )