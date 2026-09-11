from __future__ import annotations
from pyrchidekt.cards import OracleCard
from pyrchidekt.categories import Category
from pyrchidekt.edition import Edition
from pyrchidekt.mana import ManaProduction
from pyrchidekt.owner import Owner
from pyrchidekt.deck import Deck
import json
import pytest


@pytest.fixture
def data() -> dict:
    with open("tests/unit/resources/deck.json", "r") as f:
        return json.load(f)


class TestArchidekt:
    def testDeckGetsMade(self, data: dict):
        assert Deck.fromJson(data)


class TestOracleId:
    # Scryfall oracle ids, verified against api.scryfall.com/cards/named
    HYLDA_ORACLE_ID = "1733c71b-fd28-48dd-8a3d-41afd4b22f0e"
    SMOTHERING_TITHE_ORACLE_ID = "153376c9-dffd-458c-8ce3-a4c8269bc4e9"

    def testOracleCardExposesUid(self, data: dict):
        deck = Deck.fromJson(data)
        oracle_cards = {c.card.oracle_card.name: c.card.oracle_card for c in deck.cards}
        assert oracle_cards["Hylda of the Icy Crown"].uid == self.HYLDA_ORACLE_ID
        assert oracle_cards["Smothering Tithe"].uid == self.SMOTHERING_TITHE_ORACLE_ID

    def testOracleCardUidDefaultsWhenAbsent(self, data: dict):
        payload = dict(data["cards"][0]["card"]["oracleCard"])
        del payload["uid"]
        assert OracleCard.fromJson(payload).uid == ""

    def testCardUidIsThePrintingNotTheOracleId(self, data: dict):
        deck = Deck.fromJson(data)
        for archidekt_card in deck.cards:
            card = archidekt_card.card
            assert card.uid != card.oracle_card.uid


class TestDefaultConstruction:
    def testContainerDefaultsAreEmptyContainers(self):
        card = OracleCard()
        assert card.color_identity == []
        assert card.colors == []
        assert card.faces == []
        assert card.sub_types == []
        assert card.super_types == []
        assert card.tokens == []
        assert card.types == []
        assert card.legalities == {}

    def testContainerDefaultsAreIterable(self):
        assert list(OracleCard().types) == []

    def testContainerDefaultsAreNotShared(self):
        first, second = OracleCard(), OracleCard()
        first.types.append("Creature")
        assert second.types == []

    def testManaProductionDefaultIsAnInstance(self):
        assert OracleCard().mana_production == ManaProduction(0, 0, 0, 0, 0, 0)


class TestHashability:
    def testEveryClassInTheGraphIsHashable(self, data: dict):
        deck = Deck.fromJson(data)
        archidekt_card = deck.cards[0]
        for obj in (
            deck,
            deck.owner,
            deck.categories[0],
            archidekt_card,
            archidekt_card.card,
            archidekt_card.card.edition,
            archidekt_card.card.oracle_card,
            archidekt_card.card.oracle_card.mana_production,
        ):
            assert isinstance(hash(obj), int)

    def testObjectsWorkInSetsAndAsDictKeys(self, data: dict):
        deck = Deck.fromJson(data)
        assert len({c.card.oracle_card for c in deck.cards}) == len(deck.cards)
        assert {deck: "metadata"}[deck] == "metadata"

    def testEqualObjectsHashEqualAcrossIndependentParses(self, data: dict):
        first, second = Deck.fromJson(data), Deck.fromJson(data)
        assert first == second
        assert hash(first) == hash(second)
        assert len({first, second}) == 1

    def testValueEqualityIsPreserved(self, data: dict):
        first, second = Deck.fromJson(data), Deck.fromJson(data)
        assert first is not second
        assert first == second

    def testInstancesRemainMutable(self, data: dict):
        deck = Deck.fromJson(data)
        deck.name = "Renamed"
        assert deck.name == "Renamed"

    def testDistinctTypesSharingAKeyDoNotCollide(self):
        assert hash(Category(id=1)) != hash(Owner(1, "", "", None, "", "", None))

    def testHashesAreDiscriminatedByType(self):
        """Mixing the type into the hash stops unrelated classes sharing a key from colliding."""
        assert hash(Category(id=1)) != hash((1,))
        assert hash(OracleCard(id=7, name="Sol Ring")) != hash((7, "Sol Ring"))
        assert hash(ManaProduction(1, 0, 0, 0, 0, 0)) != hash((1, 0, 0, 0, 0, 0))

    def testOracleCardHashesOnItsScryfallOracleId(self):
        uid = "1733c71b-fd28-48dd-8a3d-41afd4b22f0e"
        assert hash(OracleCard(id=1, uid=uid)) == hash(OracleCard(id=2, uid=uid))

    def testOracleCardWithoutUidFallsBackToIdAndName(self):
        assert hash(OracleCard(id=7, name="Sol Ring")) == hash(
            OracleCard(id=7, name="Sol Ring")
        )
        assert hash(OracleCard(id=7, name="Sol Ring")) != hash(
            OracleCard(id=7, name="Mana Crypt")
        )

    def testEditionHashesOnItsSetCode(self, data: dict):
        edition = Deck.fromJson(data).cards[0].card.edition
        assert hash(edition) == hash(
            Edition(edition.code, "different", edition.date, "different", None)
        )

    def testManaProductionHashesOnItsValues(self):
        assert hash(ManaProduction(1, 0, 0, 0, 0, 0)) == hash(
            ManaProduction(1, 0, 0, 0, 0, 0)
        )
        assert hash(ManaProduction(1, 0, 0, 0, 0, 0)) != hash(
            ManaProduction(0, 1, 0, 0, 0, 0)
        )

    def testDeckHashIsStableWhileVolatileFieldsChange(self, data: dict):
        """`view_count` moves on every fetch, so equality and hashing diverge for decks."""
        first, second = Deck.fromJson(data), Deck.fromJson(data)
        second.view_count += 1
        assert hash(first) == hash(second)
        assert first != second
        assert len({first, second}) == 2
