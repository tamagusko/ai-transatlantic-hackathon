# (c) Tiago Tamagusko 2022
"""
API to Transforms an address into coordinates (lat and long).

Usage:
    coordinates(address)
    Return:
        (LATITUDE, LONGITUDE)

Example:
    # Returns the coordinates of the Reichstag (address: Platz der Republik 1, 11011 Berlin, Germany)
    coordinates('Platz der Republik 1, 11011 Berlin, Germany')
    Return:
        (52.5185918, 13.3766658)
"""
from __future__ import annotations

from geopy.geocoders import Nominatim


def coordinates(address: str):
    locator = Nominatim(user_agent='myGeocode', timeout=10)
    try:
        location = locator.geocode(address)
        return location.latitude, location.longitude
    except AttributeError:
        return None  # If the address is not found, return None


# print(coordinates('Rua Quinta da Portela, Coimbra, Portugal'))
