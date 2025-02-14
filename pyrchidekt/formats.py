"""
Enum for deck formats
"""

from __future__ import annotations
from aenum import Enum


class Format(Enum):
    """Enumerated wrapper around the format code and legalities strings

    This class combines both the numeric format codes and string legality codes that Archidekt uses
    """
    _init_ = 'value string'
    STANDARD = 1, "standard"
    MODERN = 2, "modern"
    COMMANDER = 3, "commander"
    LEGACY = 4, "legacy"
    VINTAGE = 5, "vintage"
    PAUPER = 6, "pauper"
    CUSTOM = 7, None
    FRONTIER = 8, "oldschool"
    FUTURE_STANDARD = 9, "future"
    PENNY = 10, "penny"
    ONE_V_ONE_COMMANDER = 11, "1v1"
    DUEL_COMMANDER = 12, "duel"
    BRAWL = 13, "brawl"
    OATHBREAKER = 14, "oathbreaker"
    PIONEER = 15, "pioneer"
    HISTORIC = 16, "historic"
    PAUPER_COMMANDER = 17, "paupercommander"
    ALCHEMY = 18, "alchemy"
    EXPLORER = 19, "explorer"
    HISTORIC_BRAWL = 20, "historicbrawl"
    GLADIATOR = 21, "gladiator"
    PREMODERN = 22, "premodern"
    PREDH = 23, "predh"
    TIMELESS = 24, "timeless"
    CANADIAN_HIGHLANDER = 25, "canlander"

    def __str__(self: Format) -> str:
        return self.string 
    
    @classmethod
    def _missing_value_(cls, value):
        for member in cls:
            if member.string == value:
                return member
