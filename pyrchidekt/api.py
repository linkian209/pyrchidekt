"""
This is the api querying that will return decks based on ID
"""
from .deck import Deck
import requests

ARCHIDEKT_API_BASE = "https://www.archidekt.com/api/"
DECK_SEARCH_ENDPOINT = ARCHIDEKT_API_BASE + "decks/{}/"

def getDeckById(id: int) -> Deck:
    """Retrieves a deck by id from Archidekt

    This queries the Archidekt API to retrieve the deck, returning the object representing the deck.

    Args:
        id: `int` The ID of the deck

    Returns:
        The `Deck` object. 

    Raises:
        RuntimeError: In either the case that the deck doesn't exist or it can't be retrieved for some reason
    """
    response = requests.get(DECK_SEARCH_ENDPOINT.format(id))
    match response.status_code:
        case 200:
            return Deck.fromJson(response.json())
        case 404:
            raise RuntimeError(f"{id} is either not a valid deck or it's private")
        case _:
            raise RuntimeError(f"Unknown error trying to retrieve deck {id}")