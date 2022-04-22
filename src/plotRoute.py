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
from coordinates import coordinates
from createGraph import create_graph
ox.config(use_cache=True, log_console=True)


def shortest_route(G, start_node, end_node):
    # https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
    start = ox.get_nearest_node(G, start_node)
    end = ox.get_nearest_node(G, end_node)
    weight = 'travel_time'
    return nx.shortest_path(G, start, end, weight)


def plot_graph_route(G, route, weight):
    """ Plots the graph and the shortest route.
    Args:
        G: Graph (networkx)
        route: list of routes to plot (format of route: shortest_route(G, start_node, end_node))
    """

    return ox.plot_graph_routes(G, route, route_linewidth=6, node_size=0, bgcolor='k')


# test
G = create_graph('Coimbra', 3000, 'drive')
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)
# this list will be created by the optimization function based on client list
client1 = coordinates('Rua do Brasil, 232, Coimbra, Portugal')
client2 = coordinates('Rua Larga 1, Coimbra, Portugal')
client3 = coordinates('Avenida da Guarda Inglesa, Coimbra, Portugal')
client4 = coordinates('Avenida Fernão de Magalhães, 627, Coimbra, Portugal')
client5 = coordinates('Rua Camilo Pessanha,Coimbra, Portugal')
route1 = shortest_route(G, client1, client2)
route2 = shortest_route(G, client2, client3)
route3 = shortest_route(G, client3, client4)
route4 = shortest_route(G, client4, client5)
route = route1, route2, route3, route4

# plot results
plot_graph_route(G, route, 'travel_time')
