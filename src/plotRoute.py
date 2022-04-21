# (c) Tiago Tamagusko 2022
"""
Plots the graph and the shortest route.

Usage:
    plot_graph_route(G, start, end, weight)

Example:
    G = create_graph('Coimbra', 3000, 'drive')
    # impute missing edge speeds and add travel times
    G = ox.add_edge_speeds(G)
    G = ox.add_edge_travel_times(G)
    end = coordinates('Rua do Brasil, 232, Coimbra, Portugal')
    start = coordinates('Rua Larga 1, Coimbra, Portugal')

    plot_graph_route(G, start, end, 'travel_time')
"""
from __future__ import annotations

import networkx as nx
import osmnx as ox
# from coordinates import coordinates  # uncomment if use address
# from createGraph import create_graph  # uncomment to use
ox.config(use_cache=True, log_console=True)


def plot_graph_route(G, start, end, weight):
    """ Plots the graph and the shortest route.
    Args:
        G: Graph (networkx)
        start: the starting point of the route (lat and long). i.e. '52.5185918, 13.3766658'
        end : the end point of the route (lat and long). i.e. '52.5185918, 13.3766658'
        weight: the weight of the edges ('length', 'travel_time')
        Returns:
            the graph plotted
    """
    start_node = ox.get_nearest_node(G, start)
    end_node = ox.get_nearest_node(G, end)
    # https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
    # default method='dijkstra'
    route = nx.shortest_path(G, start_node, end_node, weight='travel_time')
    return ox.plot_graph_route(G, route, route_linewidth=6, node_size=0, bgcolor='k')
