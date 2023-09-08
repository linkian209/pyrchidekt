"""
Loose Wrapper around Archidekt's Deck object
"""
from __future__ import annotations
from .cards import ArchidektCard, Card
from .categories import Category
from .formats import Format
from .owner import Owner
from dataclasses import dataclass
from datetime import datetime
from typing import Any, List

@dataclass
class Deck:
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

    @staticmethod
    def fromJson(data: dict) -> Deck:
        retval = Deck(
            id=data["id"],
            name=data["name"],
            created_at=datetime.fromisoformat(data["createdAt"]),
            updated_at=datetime.fromisoformat(data["updatedAt"]),
            format=Format(data["deckFormat"]),
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
            card_package=data["cardPackage"]
        )

        categories = {x.name: x for x in retval.categories}

        for card in retval.cards:
            added_to_categories = False
            if len(card.categories):
                for category in card.categories:
                    deck_category = categories.get(category)
                    if(deck_category is None):
                        deck_category = Category(name=category)
                        categories[deck_category.name] = deck_category
                        retval.categories.append(deck_category)
                    deck_category.cards.append(card)
                added_to_categories = True

            if not added_to_categories and card.card.oracle_card.default_category:
                deck_category = categories.get(card.card.oracle_card.default_category)
                if(deck_category is None):
                    deck_category = Category(name=card.card.oracle_card.default_category)
                    categories[deck_category.name] = deck_category
                    retval.categories.append(deck_category)
                deck_category.cards.append(card)
        
        return retval
