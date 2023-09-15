# Pyrchidekt
Pyrchidekt is a Python library for interfacing with decks from the website [Archidekt](https://www.archidekt.com).

# Installation
```shell
pip install pyrchidekt
```

# Example
The following example shows how to use `pyrchidekt` to query a deck and iterate through all cards in each category.
```python
from pyrchidekt.api import getDeckById

deck = getDeckById(1)
for category in deck.categories:
    print(f"{category.name}")
    for card in category.cards:
        print(f"\t{card.quantity} {card.card.oracle_card.name}")
    print("")
```