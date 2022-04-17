# (c) Tiago Tamagusko 2022
# source :https://towardsdatascience.com/driving-distance-between-two-or-more-places-in-python-89779d691def
# documentation: http://project-osrm.org/docs/v5.5.1/api/#route-service
"""
Calculates the route between two addresses using OSRM API

Usage:
    $ route(origin, destination)

Example:
    # Returns the route between the Reichstag (address: Platz der Republik 1, 11011 Berlin, Germany)
    # and the Hauptbahnhof (address: Hauptbahnhof, 10117 Berlin, Germany)
    $ route('Platz der Republik 1, 11011 Berlin, Germany', 'Hauptbahnhof, 10117 Berlin, Germany')
"""
from __future__ import annotations

import requests
from coordinates import coordinates
# import json


def route(origin: str, dest: str):
    orig_lat, orig_long = coordinates(origin)
    dest_lat, dest_long = coordinates(dest)
    result = requests.get(
        f'http://router.project-osrm.org/route/v1/car/{orig_long},{orig_lat};{dest_long},{dest_lat}?overview=false''',
    )
    return result


# test:
# origin = 'Platz der Republik 1, 11011 Berlin, Germany'
# destination = 'Hauptbahnhof, 10117 Berlin, Germany'
# routes = json.loads(route(origin, destination).content)
# print(routes.get("routes")[0])
