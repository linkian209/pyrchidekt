from __future__ import annotations
from pyrchidekt.deck import Deck
import json
import pytest


@pytest.fixture
def data() -> dict:
    with open("tests/unit/resources/deck.json", "r") as f:
        return json.load(f)    

class TestArchidekt:
    def testDeckGetsMade(self, data: dict):
        assert(Deck.fromJson(data))