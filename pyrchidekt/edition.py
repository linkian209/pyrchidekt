"""
Edition Wrapper
"""
from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import Any


@dataclass
class Edition:
    """Small wrapper around Archidekt Edition
    
    This class is a small wrapper around the edition/set information for a card

    Attributes:
        code: `str` The code for the set
        
        name: `str` The name of the set

        date: `date` Date the set was released

        type: `str` Type of set

        mtgo_code: `Any` Code for the set on MTGO
    """
    code: str
    name: str
    date: date
    type: str
    mtgo_code: Any

    @staticmethod
    def fromJson(data: dict) -> Edition:
        """Returns an Edition object from a `dict`
        
        Creates an edition object from a JSON deserialized `dict`. An example of this is the following:
        ```json
        {
            "editioncode": "woe",
            "editionname": "Wilds of Eldraine",
            "editiondate": "2023-09-08",
            "editiontype": "expansion",
            "mtgoCode": "woe"
        }
        ```
        
        Arguments:
            data: `dict` The dictionary formatted to create an `Edition`

        Returns:
            The `Edition` object
        """
        return Edition(
            data['editioncode'],
            data['editionname'],
            date.fromisoformat(data['editiondate']),
            data['editiontype'],
            data['mtgoCode']
        )