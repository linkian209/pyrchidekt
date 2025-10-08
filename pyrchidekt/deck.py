"""
Loose Wrapper around Archidekt's Deck object
"""

from __future__ import annotations
from .cards import ArchidektCard
from .categories import Category
from .formats import Format
from .owner import Owner
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional
from warnings import warn


@dataclass
class Deck:
    """The Deck object

    This is the main object from this module. It contains all the information about a deck.

    Attributes:
        id: `int` The deck id

        name: `str` Name of the deck

        created_at: `datetime` When the deck was created

        updated_at: `datetime` When the deck was last updated

        format: `Format` What format the deck is listed as in Archidekt

        description: `str` Description of the deck

        featured: `str` URL to the featured image of the deck

        custom_featured: `str` The custom featured URL

        game: `Any` The Game for the deck

        private: `bool` Is the deck private or not

        view_count: `int` The number of views the deck has gotten

        cards: `List[ArchidektCard]` The cards in the deck

        points: `int` The points for the deck

        user_input: `int` Amount of user input

        owner: `Owner` Owner of the deck

        categories: `List[Category]` The categories in the deck

        comment_root: `int` The ID of the comment at the head of the chain

        editors: `List[Any]` The list of other editors for the deck

        parent_folder: `int` The ID of the folder the deck is in

        bookmarked: `bool` Is the deck bookmarked?

        deck_tags: `List[str]` Tags for the deck

        card_package: `Any` The package for the deck.

        edh_bracket: `Optional[int]` The EDH bracket the deck is listed as in Archidekt

        unlisted: `bool` Is the deck unlisted or not

        theorycrafted: `bool` Is the deck theorycrafted or not

        playgroup_deck_url: `Optional[str]` The URL of Playgroup.gg the deck is associated with in Archidekt
    """

    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    format: Format
    description: str
    featured: str
    custom_featured: str
    game: Any
    private: bool
    view_count: int
    cards: List[ArchidektCard]
    points: int
    user_input: int
    owner: Owner
    categories: List[Category]
    comment_root: int
    editors: List[Any]
    parent_folder: int
    bookmarked: bool
    deck_tags: List[str]
    card_package: Any
    edh_bracket: Optional[int]
    unlisted: bool
    theorycrafted: bool
    playgroup_deck_url: Optional[str]

    @staticmethod
    def fromJson(data: dict) -> Deck:
        """Creates a `Deck` from a `dict`

        This method creates `Deck` from a JSON deserialized `dict`.

        An example of a deck is as follows:
        ```json
        {
            "id": 123456,
            "name": "Deck #2",
            "createdAt": "2023-08-23T22:31:39.567776Z",
            "updatedAt": "2023-09-04T02:22:43.394183Z",
            "deckFormat": 3,
            "edhBracket": 2,
            "game": 1,
            "description": "{\"ops\":[]}",
            "viewCount": 1000,
            "featured": "https://storage.googleapis.com/archidekt-card-images/woe/ae9231fd-053d-4b84-a7a8-86063465bc49_art_crop.jpg",
            "customFeatured": "",
            "private": false,
            "unlisted": false,
            "theorycrafted": false,
            "points": 0,
            "userInput": 0,
            "owner": {...},
            "commentRoot": 5223305,
            "editors": [],
            "parentFolder": 139452,
            "bookmarked": false,
            "categories": [...],
            "deckTags": [],
            "playgroupDeckUrl": null,
            "cardPackage": null,
            "cards": [...]
        }
        ```

        This method will loop through all the lists and create objects from them as well.

        Arguments:
            data: `dict` The deck data

        Returns:
            The `Deck` object
        """
        try:
            _format = Format(data["deckFormat"])
        except ValueError as e:
            warn(
                message=f"{e} -> skipping deck format\n"
                f"For new formats, please file an issue at "
                f"https://github.com/linkian209/pyrchidekt/issues",
                category=RuntimeWarning,
                stacklevel=2,
            )
            _format = None

        retval = Deck(
            id=data["id"],
            name=data["name"],
            created_at=datetime.fromisoformat(data["createdAt"]),
            updated_at=datetime.fromisoformat(data["updatedAt"]),
            format=_format,
            description=data["description"],
            featured=data["featured"],
            custom_featured=data["customFeatured"],
            game=data["game"],
            private=data["private"],
            view_count=data["viewCount"],
            cards=[ArchidektCard.fromJson(x) for x in data["cards"]],
            points=data["points"],
            user_input=data["userInput"],
            owner=Owner.fromJson(data["owner"]),
            categories=[Category.fromJson(x) for x in data["categories"]],
            comment_root=data["commentRoot"],
            editors=data["editors"],
            parent_folder=data["parentFolder"],
            bookmarked=data["bookmarked"],
            deck_tags=data["deckTags"],
            card_package=data["cardPackage"],
            edh_bracket=data["edhBracket"],
            unlisted=data["unlisted"],
            theorycrafted=data["theorycrafted"],
            playgroup_deck_url=data["playgroupDeckUrl"]
        )

        categories = {x.name: x for x in retval.categories}

        for card in retval.cards:
            added_to_categories = False
            if card.categories and len(card.categories):
                for category in card.categories:
                    deck_category = categories.get(category)
                    if deck_category is None:
                        deck_category = Category(name=category)
                        categories[deck_category.name] = deck_category
                        retval.categories.append(deck_category)
                    deck_category.cards.append(card)
                added_to_categories = True

            if not added_to_categories and card.card.oracle_card.default_category:
                deck_category = categories.get(card.card.oracle_card.default_category)
                if deck_category is None:
                    deck_category = Category(
                        name=card.card.oracle_card.default_category
                    )
                    categories[deck_category.name] = deck_category
                    retval.categories.append(deck_category)
                deck_category.cards.append(card)

        return retval
