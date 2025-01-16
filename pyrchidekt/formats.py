"""
Enum for deck formats
"""
from __future__ import annotations
from enum import IntEnum, StrEnum

class Format(IntEnum):
    """Enumerated wrapper around the format code
    
    This class is a wrapper around the deck format codes Archidekt uses
    """
    STANDARD = 1
    MODERN = 2
    COMMANDER = 3
    LEGACY = 4
    VINTAGE = 5
    PAUPER = 6
    CUSTOM = 7
    FRONTIER = 8
    FUTURE_STANDARD = 9
    PENNY = 10
    ONE_V_ONE_COMMANDER = 11
    DUEL_COMMANDER = 12
    BRAWL = 13
    OATHBREAKER = 14
    PIONEER = 15
    HISTORIC = 16
    PAUPER_COMMANDER = 17
    ALCHEMY = 18
    EXPLORER = 19
    HISTORIC_BRAWL = 20
    GLADIATOR = 21
    PREMODERN = 22
    PREDH = 23
    TIMELESS = 24
    CANADIAN_HIGHLANDER = 25

class LegalFormat(StrEnum):
    """Enumerated wrapper around the legalities strings

    This class is a wrapper around the card legalities format strings Archidekt uses
    """
    STANDARD = "standard"
    MODERN = "modern"
    COMMANDER = "commander"
    LEGACY = "legacy"
    VINTAGE = "vintage"
    PAUPER = "pauper"
    FRONTIER = "oldschool"
    FUTURE_STANDARD = "future"
    PENNY = "penny"
    ONE_V_ONE_COMMANDER = "1v1"
    DUEL_COMMANDER = "duel"
    BRAWL = "brawl"
    OATHBREAKER = "oathbreaker"
    PIONEER = "pioneer"
    HISTORIC = "historic"
    PAUPER_COMMANDER = "paupercommander"
    ALCHEMY = "alchemy"
    EXPLORER = "explorer"
    HISTORIC_BRAWL = "historicbrawl"
    GLADIATOR = "gladiator"
    PREMODERN = "premodern"
    PREDH = "predh"
    TIMELESS = "timeless"
    CANADIAN_HIGHLANDER = "canlander"
