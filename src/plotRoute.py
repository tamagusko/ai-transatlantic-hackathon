# (c) Tiago Tamagusko 2022
"""
Plots the graph for the routes created.

Usage:
    plot_graph_route(G, route, weight)

Example:
    # create the graph with the OSMnx library (location = 'Coimbra', radius = 3000, transport_mode= 'drive')
    G = create_graph('Coimbra', 3000, 'drive')
    # add speed to the graph
    G = ox.add_edge_speeds(G)
    # add travel time to the graph
    G = ox.add_edge_travel_times(G)
    route1 = shortest_route(G, 40.2019077, -8.4132559, 40.2079321, 8.4241537)
    route2 = shortest_route(G, 40.2079321, 8.4241537, 40.21136145, -8.409485431339796)
    route = route1, route2
    plot_graph_route(G, route, 'travel_time')
"""
from __future__ import annotations

import osmnx as ox
# from coordinates import coordinates  # uncomment if you want a example
# from shortestRoute import shortest_route  # uncomment if you want a example
# from createGraph import create_graph  # uncomment if you want a example

ox.config(use_cache=True, log_console=True)


def plot_graph_route(G, route, weight):
    """ Plots the graph and the shortest route.
    Args:
        G: Graph (networkx)
        route: list of routes to plot
    """
    return ox.plot_graph_routes(G, route, route_linewidth=6, node_size=0, bgcolor='k')
