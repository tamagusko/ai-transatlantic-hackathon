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

import osmnx as ox
ox.config(use_cache=True, log_console=True)


def plot_graph_route(G, route, weight):
    """ Plots the graph and the shortest route.
    Args:
        G: Graph (networkx)
        route: list of routes to plot (format of route: shortest_route(G, start_node, end_node))
    """
    return ox.plot_graph_routes(G, route, route_linewidth=6, node_size=0, bgcolor='k')
