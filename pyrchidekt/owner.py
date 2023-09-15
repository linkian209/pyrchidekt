"""
Loose wrapping around deck owner. No PII other than a username and id.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class Owner:
    """Owner Wrapper
    
    This is a loose wrapping around the owner of a deck.

    Attributes:
        id: `int` The owners's ID

        username: `str` The owner's username

        avatar: `str` The URL of their avatar

        frame: `Any` The frame for the owner

        ck_affiliate: `str` The owner`s CardKingdom Affiliate link

        tcg_affiliate: `str` The owner`s TCG Player Affiliate link

        referrer_enum: `Any` The referrer enumeration
    """
    id: int
    username: str
    avatar: str
    frame: Any
    ck_affiliate: str
    tcg_affiliate: str
    referrer_enum: Any

    @staticmethod
    def fromJson(data: dict) -> Owner:
        """Creates an `Owner` from a dict
        
        This method creates an `Owner` object from a JSON deserialized `dict`. An example of this is is as
        follows:
        ```json
        {
            "id": 12345,
            "username": "User #1",
            "avatar": "https://storage.googleapis.com/topdekt-user/avatars/default/avatar_colorless.svg",
            "frame": null,
            "ckAffiliate": "",
            "tcgAffiliate": "",
            "referrerEnum": null
        }
        ```

        Arguments:
            data: `dict` The JSON deserialized data

        Returns:
            The `Owner` object
        """
        return Owner(
            id=data["id"],
            username=data["username"],
            avatar=data["avatar"],
            frame=data["frame"],
            ck_affiliate=data["ckAffiliate"],
            tcg_affiliate=data["tcgAffiliate"],
            referrer_enum=data["referrerEnum"]
        )