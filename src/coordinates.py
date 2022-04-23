# (c) Tiago Tamagusko 2022
"""
Transforms an address into coordinates.

Usage:
    coordinates(address)
    Return:
        (LATITUDE, LONGITUDE)

    latitude(address)
    Return:
        LATITUDE

    longitude(address)
    Return:
        LONGITUDE

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


def latitude(address: str):
    return coordinates(address)[0]


def longitude(address: str):
    return coordinates(address)[1]
