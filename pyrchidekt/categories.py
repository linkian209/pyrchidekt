"""
Loose Wrapping around Archidekt Categories
"""
from __future__ import annotations
from .cards import ArchidektCard
from dataclasses import dataclass, field
from typing import List


@dataclass
class Category:
    """Loose wrapper around the Archidekt Category
    
    This is a category from Archidekt. This one has a lot of defaults and such because some cards don't have
    normal archidekt categories and we need to make some.

    Attributes:
        id: `int` The id of the category. 

        name: `str` The name of the category

        included_in_deck: `bool` The cards in this category are considered part of the deck

        included_in_price: `bool` The cards in this category should be included in the price of the deck

        is_premier: `bool` This is a premier category

        cards: `List[ArchidektCard]` The cards contained in this category
    """
    id: int = field(default=-1)
    name: str = field(default="")
    included_in_deck: bool = field(default=False)
    included_in_price: bool = field(default=False)
    is_premier: bool = field(default=False)
    cards: List[ArchidektCard] = field(default_factory=list)

    @staticmethod
    def fromJson(data: dict) -> Category:
        """Creates a category from a dict
        
        This method creates a Category from a JSON deserialized `dict`. An example format of this is as
        follows:
        ```json
        {
            "id": 45917676,
            "name": "Maybeboard",
            "includedInDeck": false,
            "includedInPrice": false,
            "isPremier": false
        }
        ```

        Arguments:
            data: `dict` The dictionary containing the data required to make a category

        Returns:
            A `Category` object made from the dictionary.
        """
        return Category(
            id=data["id"],
            name=data["name"],
            included_in_deck=data["includedInDeck"],
            included_in_price=data["includedInPrice"],
            is_premier=data["isPremier"]
        )