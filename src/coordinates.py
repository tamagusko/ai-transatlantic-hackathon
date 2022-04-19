# (c) Tiago Tamagusko 2022
"""
API to Transforms an address into coordinates (lat and long).

Usage:
    HOST/coordinates?address='ADDRESS'
    Return:
        0: latitude
        1: longitude

Example:
    # Returns the coordinates of the Reichstag (address: Platz der Republik 1, 11011 Berlin, Germany)
    $ https://mvptransatlanticai.herokuapp.com/coordinates?address='Platz der Republik 1, 11011 Berlin, Germany'
    return:
        0: 52.5185918
        1: 13.3766658
"""
from __future__ import annotations

from fastapi import APIRouter
from geopy.geocoders import Nominatim

router = APIRouter()


@router.get('/coordinates')
async def coordinates(address: str):
    locator = Nominatim(user_agent='myGeocoder')
    try:
        location = locator.geocode(address)
        return location.latitude, location.longitude
    except AttributeError:
        return None  # If the address is not found, return None
