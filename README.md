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

# Developing
It is encouraged to use virtual environments to develop `pyrchidekt`. To start developing, install the requirements:
```shell
pip install -r requirements/dev.txt
```

# Testing
Testing will be run on PRs and before deploys for new releases. For local testing, see below.

## Setup
You must additionally install the testing dependencies:
```shell
pip install -r requirements/test.txt
```
All tests can be run as follows:
```shell
coverage run -m pytest tests
```
With reporting then checked using:
```shell 
coverage report
```
There are two types of tests: unit and integration. 

## Unit Tests
Unit tests ensure that the basic data `dict` conversion works correctly from how the inferred API works. These are run as follows:
```shell
coverage run -m pytest tests/unit
```
These tests should be run often when changing the dataclasses

## Integration Tests
Integration tests ensure that `pyrchidekt` works with the current API of Archidekt. They are run as follows:
```shell
coverage run -m pytest tests/integration
```
These tests can be run less frequently. So long as Archidekt doesn't change their API data structures, these will pass.