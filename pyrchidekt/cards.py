"""
Card Classes. There are three: one for the archidekt wrapping, one containing artist and set info, and the one
that contains all of the actual card info.
"""
from __future__ import annotations
from .edition import Edition
from .formats import LegalFormat
from .mana import ManaProduction
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class OracleCard:
    """Actual Card Representation

    This class is the inner most layer of the onion containing the actual card information. This information
    likely comes from Scryfall.

    Attributes:
        id: `int` The ID of the card

        cmc: `int` The converted mana cost as an integer

        color_identity: `List[str]` The color identity represented as a list of strings.

        colors: `List[str]` Colors of the card as a list of strings

        faces: `List` A list of the faces of the card. (for dual sided cards)

        layout: `str` The layout of the card

        legalities: `Dict[LegalFormat, bool]` The formats in which the card is legal to play. This is a dictionary 
        with an Enum representation of all formats and a boolean if it is legal in that format.
        
        mana_cost: `str` The raw mana cost string. Uses special characters to represent the colors for example: 
        "1{U}" is 1 generic and 1 blue mana
        
        mana_production: `ManaProduction` The mana this card produces.
        
        name: `str` The name of the card

        power: `str` The power of the card as a string. This is because some powers are not integers (i.e. "*")

        salt: `str` The salt rating of the card (how salty do people feel when playing against it)

        sub_types: `List[str]` The sub types of a card (ex. ["Goblin", "Lord"])

        super_types: `List[str]` The super types of a card

        text: `str` The text printed on the card

        tokens: `List[str]` A list of IDs of tokens this card creates

        toughness: `str`  Toughness of a creature as a string. This is because some toughnesses are not 
        integers

        types: `List[str]` Types of the card (ex: ["Enchantment", "Creature"])

        loyalty: `str` How many loyalty counters a planeswalker comes with

        default_category: `str` The default category a card would go in if it is not already in one
    """
    id: int = field(default=-1)
    cmc: int = field(default=-1)
    color_identity: List[str] = field(default=list)
    colors: List[str] = field(default=list)
    faces: List = field(default=list)
    layout: str = field(default="")
    legalities: Dict[LegalFormat, bool] = field(default=dict)
    mana_cost: str = field(default="")
    mana_production: ManaProduction = field(default=ManaProduction)
    name: str = field(default="")
    power: str = field(default="")
    salt: float = field(default=-1.0)
    sub_types: List[str] = field(default=list)
    super_types: List[str] = field(default=list)
    text: str = field(default="")
    tokens: List[str] = field(default=list)
    toughness: str = field(default="")
    types: List[str] = field(default=list)
    loyalty: str = field(default="")
    default_category: str = field(default="")

    @staticmethod
    def fromJson(data: dict) -> OracleCard:
        """Returns an `OracleCard` from a dictionary.

        This takes in a formatted dictionary and returns an Object. An example of this is the following:
        ```json
        {
            "id": 35949,
            "cmc": 4,
            "colorIdentity": [
                "White",
                "Blue"
            ],
            "colors": [
                "White",
                "Blue"
            ],
            "faces": [],
            "layout": "normal",
            "legalities": {
                "alchemy": "legal",
                "legacy": "legal",
                "oldschool": "not_legal",
                "modern": "legal",
                "vintage": "legal",
                "oathbreaker": "legal",
                "1v1": "legal",
                "historicbrawl": "legal",
                "premodern": "not_legal",
                "historic": "legal",
                "commander": "legal",
                "paupercommander": "not_legal",
                "gladiator": "legal",
                "explorer": "legal",
                "brawl": "legal",
                "penny": "not_legal",
                "pioneer": "legal",
                "duel": "legal",
                "pauper": "not_legal",
                "standard": "legal",
                "future": "legal",
                "predh": "not_legal"
            },
            "manaCost": "{2}{W}{U}",
            "manaProduction": {
                "W": null,
                "U": null,
                "B": null,
                "R": null,
                "G": null,
                "C": null
            },
            "name": "Hylda of the Icy Crown",
            "power": "3",
            "salt": null,
            "subTypes": [
                "Human",
                "Warlock"
            ],
            "superTypes": [
                "Legendary"
            ],
            "text": "Whenever you tap an untapped creature an opponent controls, you may pay {1}. When you do, choose one —\n• Create a 4/4 white and blue Elemental creature token.\n• Put a +1/+1 counter on each creature you control.\n• Scry 2, then draw a card.",
            "tokens": [
                "36804"
            ],
            "toughness": "4",
            "types": [
                "Creature"
            ],
            "loyalty": null,
            "defaultCategory": null
        }
        ```

        Arguments:
            data: `dict` Formatted dictionary containing the data for the card

        Returns:
            The `OracleCard` object created from the data.
        """
        return OracleCard(
            id=data["id"],
            cmc=data["cmc"],
            color_identity=data["colorIdentity"],
            colors=data["colors"],
            faces=data["faces"],
            layout=data["layout"],
            legalities={LegalFormat.fromString(x): data["legalities"][x] for x in data["legalities"]},
            mana_cost=data["manaCost"],
            mana_production=ManaProduction.fromJson(data["manaProduction"]),
            name=data["name"],
            power=data["power"],
            salt=data["salt"],
            sub_types=data["subTypes"],
            super_types=data["superTypes"],
            text=data["text"],
            tokens=data["tokens"],
            toughness=data["toughness"],
            types=data["types"],
            loyalty=data["loyalty"],
            default_category=data["defaultCategory"]
        )


@dataclass
class Card:
    """The inner card representation
    
    This class represents the inner layer from the Archidekt wrapper, containing meta information not 
    relevant to actually playing the game.

    Attributes:
        id: `int` The ID of the card

        artist: `str` The artist of the card

        tcg_product_id: `int` The ID of the card on TCG Player
        
        ck_foil_id: `int` The ID of the foil card on Card Kingdon

        ck_normal_id: `int` The ID of the card on Card Kingdom

        cm_ed: `str` The full name of the set

        collector_number: `int` The collector number

        multiverse_id: `int` The multiverse ID

        mtgo_foil_id: `int` The ID of the foil on MTGO

        mtgo_normal_id: `int` The ID of the card on MTGO

        uid: `str` A UUID for the card on Scryfall

        display_name: `Any` A display name for the card
        
        edition: `Edition` The edition information of the card

        flavor: `str` The flavor text of the card

        games: `List` A list of the games

        options: `List[str]` Options for the card

        oracle_card: `OracleCard` The actual gameplay relevant info on the card

        owned: `int` How many copies are owned by the creator of the deck

        prices: `Dict[str, float]` A list of market prices by vender for the card at the time of querying

        rarity: `str` Rarity of the card
    """
    id: int
    artist: str
    tcg_product_id: int
    ck_foil_id: int
    ck_normal_id: int
    cm_ed: str
    collector_number: int
    multiverse_id: int
    mtgo_foil_id: int
    mtgo_normal_id: int
    uid: str
    display_name: Any
    edition: Edition
    flavor: str
    games: List
    options: List[str]
    oracle_card: OracleCard
    owned: int
    prices: Dict[str, float]
    rarity: str

    @staticmethod
    def fromJson(data: dict) -> Card:
        """Returns a `Card` from a dictionary
        
        Used in `Deck` creation, this method returns a `Card` from a JSON serialized object. An example of 
        this is as follows:
        ```json
        {
            "id": 122970,
            "artist": "Ekaterina Burmak",
            "tcgProductId": 512193,
            "ckFoilId": 282308,
            "ckNormalId": 281587,
            "cmEd": "wilds of eldraine",
            "collectorNumber": "206",
            "multiverseid": 0,
            "mtgoFoilId": 0,
            "mtgoNormalId": 0,
            "uid": "ae9231fd-053d-4b84-a7a8-86063465bc49",
            "displayName": null,
            "edition": {
                "editioncode": "woe",
                "editionname": "Wilds of Eldraine",
                "editiondate": "2023-09-08",
                "editiontype": "expansion",
                "mtgoCode": "woe"
            },
            "flavor": "",
            "games": [],
            "options": [
                "Normal",
                "Foil"
            ],
            "oracleCard": {...},
            "owned": 0,
            "prices": {
                "ck": 0.99,
                "ckfoil": 2.49,
                "cm": 0.0,
                "cmfoil": 0.0,
                "mtgo": 0.0,
                "mtgofoil": 0.0,
                "tcg": 1.04,
                "tcgfoil": 4.45
            },
            "rarity": "mythic"
        }
        ```

        Arguments:
            data: `dict` A formated dictionary

        Returns:
            The `Card` object represented by the dictionary
        """
        return Card(
            id=data["id"],
            artist=data["artist"],
            tcg_product_id=data["tcgProductId"],
            ck_foil_id=data["ckFoilId"],
            ck_normal_id=data["ckNormalId"],
            collector_number=data["collectorNumber"],
            cm_ed=data["cmEd"],
            multiverse_id=data["multiverseid"],
            mtgo_foil_id=data["mtgoFoilId"],
            mtgo_normal_id=data["mtgoNormalId"],
            uid=data["uid"],
            display_name=data["displayName"],
            edition=Edition.fromJson(data["edition"]),
            flavor=data["flavor"],
            games=data["games"],
            options=data["options"],
            oracle_card=OracleCard.fromJson(data["oracleCard"]),
            owned=data["owned"],
            prices=data["prices"],
            rarity=data["rarity"]
        )


@dataclass
class ArchidektCard:
    """The Archidekt Wrapper for a card
    
    This class is the outer most wrapper around a card, containing information relevant for Archidekt's front end.
    This wraps around the two inner layers as this instance is created every time a version of the card is added 
    into a deck.

    Attributes:
        id: `int` ID of the card

        card: `Card` The inner Card object

        categories: `List[str]` Categories the card is sorted within

        companion: `bool` Companion Flag. Indicates if the card is a Companion

        flipped_default: `bool` Should this card be displayed flipped by default

        label: `str` The label attached to the card

        label_color: `str` The color of the label

        modifier: `str` A modifier on the card

        quantity: `int` Quantity of this card in the deck

        custom_cmc: `Any` A custom CMC for the card

        removed_categories: `Any` Categories removed from the card

        created_at: `datetime` When this instance was created/added into the deck

        updated_at: `datetime` When this instance was last updated

        deleted_at: `datetime | None` When this instance was deleted from the deck
    """
    id: int
    card: Card
    categories: List[str]
    companion: bool
    flipped_default: bool
    label: str
    label_color: str
    modifier: str
    quantity: int
    custom_cmc: Any
    removed_categories: Any
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    @staticmethod
    def fromJson(data: dict) -> ArchidektCard:
        """Returns an `ArchidektCard` from a dictionary
        
        Used in `Deck` creation, this takes in a JSON deserialized dictionary and returns the `ArchidektCard`
        it represents. An example of this is as follows:
        ```json
        {
            "id": 1462788365,
            "categories": [
                "Commander"
            ],
            "companion": false,
            "flippedDefault": false,
            "label": "Have,#37d67a",
            "modifier": "Normal",
            "quantity": 1,
            "customCmc": null,
            "removedCategories": null,
            "createdAt": "2023-08-23T22:32:18.118305Z",
            "updatedAt": "2023-09-03T16:27:36.290285Z",
            "deletedAt": null,
            "card": {...}
        }
        ```

        Arguments:
            data: `dict` The dictionary containing the data

        Returns:
            The `ArchidektCard` represented by this data
        """
        label = ""
        label_color = ""

        if data["label"]:
            split_label = data["label"].split(",")
            if len(split_label) != 2:
                if len(split_label) == 1:
                    if "#" in split_label[0]:
                        label_color = split_label[0]
                    else:
                        label = split_label[0]
            else:
                label = split_label[0]
                label_color = split_label[1]

        return ArchidektCard(
            id=data["id"],
            card=Card.fromJson(data["card"]),
            categories=data["categories"],
            companion=data["companion"],
            flipped_default=data["flippedDefault"],
            label=label,
            label_color=label_color,
            modifier=data["modifier"],
            quantity=data["quantity"],
            custom_cmc=data["customCmc"],
            removed_categories=data["removedCategories"],
            created_at=datetime.fromisoformat(data["createdAt"]),
            updated_at=datetime.fromisoformat(data["updatedAt"]),
            deleted_at=datetime.fromisoformat(data["deletedAt"]) if data["deletedAt"] else None
        )