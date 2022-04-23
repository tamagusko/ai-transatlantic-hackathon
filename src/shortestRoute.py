# (c) Tiago Tamagusko 2022
"""
shortest_route: Find the shortest route based on two nodes (start and end).
shortest_route_length: Find the shortest route length based on two nodes (start and end).

Usage:
    shortest_route(G, start_lat, start_long, end_lat, end_long)
    shortest_route_length(G, start_lat, start_long, end_lat, end_long)

Example:
    # find the best route between two client1 (40.2019077, -8.4132559) and client2 (40.2079321, 8.4241537)
    route = shortest_route(G, 40.2019077, -8.4132559, 40.2079321, 8.4241537)

    # find the length of best route between two client1 (40.2019077, -8.4132559) and client2 (40.2079321, 8.4241537)
    length = shortest_route_length(G, 40.2019077, -8.4132559, 40.2079321, 8.4241537)
"""
from __future__ import annotations

import networkx as nx
import osmnx as ox
ox.config(use_cache=True, log_console=True)


def shortest_route(G, start_lat, start_long, end_lat, end_long):
    """ Find the shortest route based on two nodes (start and end).
    Args:
        G: Graph (networkx)
        start_lat: latitude of origin node
        start_long: longitude of origin node
        end_lat: latitude of destination node
        end_long: longitude of destination node

    More on: https://osmnx.readthedocs.io/en/stable/osmnx.html and
    https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
    """
    start = ox.distance.nearest_nodes(G, start_long, start_lat)
    end = ox.distance.nearest_nodes(G, end_long, end_lat)
    weight = 'travel_time'
    return nx.shortest_path(G, start, end, weight)


def shortest_route_length(G, start_lat, start_long, end_lat, end_long):
    """ Find the length of the shortest route based on two nodes (start and end).
    Args:
        G: Graph (networkx)
        start_lat: latitude of origin node
        start_long: longitude of origin node
        end_lat: latitude of destination node
        end_long: longitude of destination node

    More on: https://osmnx.readthedocs.io/en/stable/osmnx.html and
    https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
    """
    start = ox.distance.nearest_nodes(G, start_long, start_lat)
    end = ox.distance.nearest_nodes(G, end_long, end_lat)
    weight = 'travel_time'
    return nx.shortest_path_length(G, start, end, weight)
