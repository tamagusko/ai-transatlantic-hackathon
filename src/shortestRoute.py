# (c) Tiago Tamagusko 2022
"""
Find the shortest route based on two nodes (start and end).

Usage:
    shortest_route(G, start_node, end_node)

Example:
    # find the best route between two client1 and client2
    client1 = coordinates('Rua Larga 1, Coimbra, Portugal')
    client2 = coordinates('Rua do Brasil, 232, Coimbra, Portugal')
    route1 = shortest_route(G, client1, client2)
"""
from __future__ import annotations

import networkx as nx
import osmnx as ox
ox.config(use_cache=True, log_console=True)


def shortest_route(G, start_node, end_node):
    """ Find the shortest route based on two nodes (start and end).
    Args:
        G: Graph (networkx)
        start_node: origin node - format: (LAT, LONG)
        end_node: destination node - format: (LAT, LONG)

    More on: https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
    """
    start = ox.get_nearest_node(G, start_node)
    end = ox.get_nearest_node(G, end_node)
    weight = 'travel_time'
    return nx.shortest_path(G, start, end, weight)
