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
    COMMANDER_EDH = 3
    LEGACY = 4
    VINTAGE = 5
    PAUPER = 6
    CUSTOM = 7
    FRONTIER = 8
    FUTURE_STANDARD = 9
    PENNY_DREADFUL = 10
    ONE_V_ONE_COMMANDER = 11
    DUAL_COMMANDER = 12
    BRAWL = 13
    OATHBREAKER = 14
    PIONEER = 15
    HISTORIC = 16
    PAUPER_EDH = 17
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
    ALCHEMY = "alchemy"
    LEGACY = "legacy"
    OLD_SCHOOL = "oldschool"
    MODERN = "modern"
    VINTAGE = "vintage"
    OATHBREAKER = "oathbreaker"
    ONE_V_ONE = "1v1"
    HISTORIC_BRAWL = "historicbrawl"
    PREMODERN = "premodern"
    HISTORIC = "historic"
    COMMANDER = "commander"
    PAUPER_COMMANDER = "paupercommander"
    GLADIATOR = "gladiator"
    EXPLORER = "explorer"
    BRAWL = "brawl"
    PENNY = "penny"
    PIONEER = "pioneer"
    DUEL = "duel"
    PAUPER = "pauper"
    STANDARD = "standard"
    FUTURE = "future"
    PREDH = "predh"
    TIMELESS = "timeless"
    CANADIAN_HIGHLANDER = "canlander"
