"""
Card Classes. There are two, one for the archidekt wrapping and one that is just the card
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