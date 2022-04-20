# (c) Tiago Tamagusko 2022
"""
API to Transforms an address into coordinates (lat and long).

Usage:
    HOST/coordinates?address='ADDRESS'
    Return:
        latitude: LATITUDE
        longitude: LONGITUDE

Example:
    # Returns the coordinates of the Reichstag (address: Platz der Republik 1, 11011 Berlin, Germany)
    https://mvptransatlanticai.herokuapp.com/coordinates?address='Platz der Republik 1, 11011 Berlin, Germany'
    return:
        latitude: 52.5185918
        longitude: 13.3766658
"""
from __future__ import annotations

from fastapi import APIRouter
from geopy.geocoders import Nominatim

router = APIRouter()


@router.get('/coordinates')
async def coordinates(address: str):
    locator = Nominatim(user_agent='mvptransatlanticai', timeout=10)
    try:
        location = locator.geocode(address)
        return {'latitude': '{}'.format(location.latitude), 'longitude': '{}'.format(location.longitude)}
    except AttributeError:
        return None  # If the address is not found, return None
