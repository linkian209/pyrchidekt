"""
Mana Production wrapper
"""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ManaProduction:
    """Mana Production Wrapping
    
    This class wraps the mana production of a card
    
    Attributes:
        white: `int` The amount of white mana created

        blue: `int` The amount of blue mana created

        black: `int` The amount of black mana created

        red: `int` The amount of red mana created

        green: `int` The amount of green mana created

        colorless: `int` The amount of colorless mana created
    """
    white: int
    blue: int
    black: int
    red: int
    green: int
    colorless: int

    @staticmethod
    def fromJson(data: dict) -> ManaProduction:
        """Cretes a ManaProduction from a `dict`
        
        This method trakes a JSON deserialized objet and creates an object from it. An example of this is as
        follows:
        ```json
        {
            "W": 1,
            "U": 1,
            "B": null,
            "R": null,
            "G": null,
            "C": null
        }
        ```

        Arguments:
            data: `dict` The data dictionary

        Returns:   
            The `ManaProduction` object
        """
        return ManaProduction(
            data["W"],
            data["U"],
            data["B"],
            data["R"],
            data["G"],
            data["C"]
        )
