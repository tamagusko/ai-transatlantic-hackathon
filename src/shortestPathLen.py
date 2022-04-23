# (c) Tiago Tamagusko 2022
"""
Find the shortest path lenght based on two nodes (start and end).

Usage:
    shortest_path_length(G, start_lat, start_long, end_lat, end_long)

Example:
    # find the best route between two client1 (40.2019077, -8.4132559) and client2 (40.2079321, 8.4241537)
    route1 = shortest_path_length(G, 40.2019077, -8.4132559, 40.2079321, 8.4241537)
"""
from __future__ import annotations

import networkx as nx
import osmnx as ox
ox.config(use_cache=True, log_console=True)


def shortest_path_len(G, start_lat, start_long, end_lat, end_long):
    """ Find the shortest route based on two nodes (start and end).
    Args:
        G: Graph (networkx)
        start_node: origin node - format: (LAT, LONG)
        end_node: destination node - format: (LAT, LONG)

    More on: https://osmnx.readthedocs.io/en/stable/osmnx.html
    """
    start = ox.distance.nearest_nodes(G, start_long, start_lat)
    end = ox.distance.nearest_nodes(G, end_long, end_lat)
    weight = 'travel_time'
    return nx.shortest_path_length(G, start, end, weight)
