# (c) Tiago Tamagusko 2022
"""
Transforms an address into coordinates (lat and long).

Usage:
    $ coordinates('address')

Example:
    # Returns the coordinates of the Reichstag (address: Platz der Republik 1, 11011 Berlin, Germany)
    $ coordinates('Platz der Republik 1, 11011 Berlin, Germany')
    return: (52.5185918, 13.3766658)
"""
from __future__ import annotations

from geopy.geocoders import Nominatim


def coordinates(address: str):
    locator = Nominatim(user_agent='myGeocoder')
    location = locator.geocode(address)
    return location.latitude, location.longitude
