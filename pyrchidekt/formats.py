"""
Enum for deck formats
"""
from __future__ import annotations
from enum import Enum

class Format(Enum):
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

class LegalFormat(Enum):
    ALCHEMY = 1
    LEGACY = 2
    OLD_SCHOOL = 3
    MODERN = 4
    VINTAGE = 5
    OATHBREAKER = 6
    ONE_V_ONE = 7
    HISTORIC_BRAWL = 8
    PREMODERN = 9
    HISTORIC = 10
    COMMANDER = 11
    PAUPER_COMMANDER = 12
    GLADIATOR = 13
    EXPLORER = 14
    BRAWL = 15
    PENNY = 16
    PIONEER = 17
    DUEL = 18
    PAUPER = 19
    STANDARD = 20
    FUTURE = 21
    PREDH = 22

    @staticmethod
    def fromString(input: str) -> LegalFormat:
        match input:
            case "alchemy":
                return LegalFormat.ALCHEMY
            case "legacy":
                return LegalFormat.LEGACY
            case "oldschool":
                return LegalFormat.OLD_SCHOOL
            case "modern":
                return LegalFormat.MODERN
            case "vintage":
                return LegalFormat.VINTAGE
            case "oathbreaker":
                return LegalFormat.OATHBREAKER
            case "1v1":
                return LegalFormat.ONE_V_ONE
            case "historicbrawl":
                return LegalFormat.HISTORIC_BRAWL
            case "premodern":
                return LegalFormat.PREMODERN
            case "historic": 
                return LegalFormat.HISTORIC
            case "commander": 
                return LegalFormat.COMMANDER
            case "paupercommander":
                return LegalFormat.PAUPER_COMMANDER
            case "gladiator":
                return LegalFormat.GLADIATOR
            case "explorer":
                return LegalFormat.EXPLORER
            case "brawl":
                return LegalFormat.BRAWL
            case "penny":
                return LegalFormat.PENNY
            case "pioneer":
                return LegalFormat.PIONEER
            case "duel":
                return LegalFormat.DUEL
            case "pauper": 
                return LegalFormat.PAUPER
            case "standard": 
                return LegalFormat.STANDARD
            case "future": 
                return LegalFormat.FUTURE
            case "predh":
                return LegalFormat.PREDH
            case _:
                raise TypeError("Not a legal format")