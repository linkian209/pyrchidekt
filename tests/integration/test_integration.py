from pyrchidekt.api import getDeckById
import pytest


class TestIntegration:
    def testGoodFetch(self):
        assert(getDeckById(5220997))

    def testUnknownDeckThrowsException(self):
        with pytest.raises(RuntimeError):
            getDeckById(-1)