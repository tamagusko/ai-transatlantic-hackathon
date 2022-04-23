# (c) Tiago Tamagusko 2022
"""
Plots the graph for the routes created.

Usage:
    create_route(G, best_route)
    plot_graph_route(G, route, weight)

Example:
    # create the graph with the OSMnx library (location = 'Coimbra', radius = 3000, transport_mode= 'drive')
    G = create_graph('Coimbra', 3000, 'drive')
    # add speed to the graph
    G = ox.add_edge_speeds(G)
    # add travel time to the graph
    G = ox.add_edge_travel_times(G)

    # best route from genetic algorithm (genAlgorithmBestRoute): result = 1293 [9, 0, 2, 3, 6, 1, 7, 5, 4, 8]
    best_route = [9, 0, 2, 3, 6, 1, 7, 5, 4, 8]
    plot_graph_route(G, create_route(G, best_route), 'travel_time')
"""
from __future__ import annotations

import osmnx as ox
import pandas as pd
from createGraph import create_graph
from shortestRoute import shortest_route

ox.config(use_cache=True, log_console=True)


# create a route based in a list of nodes
def create_route(G, best_route):
    """ Creates a route based in a list of nodes.
    Args:
        G: Graph (networkx)
        best_route: list of nodes to create the route (from genAlgorithmBestRoute.py)
       """
    df = pd.read_csv('./data/processed/clientCoordinates.csv', sep=';')
    latitudes = df['latitude'].to_list()
    longitudes = df['longitude'].to_list()
    route = []
    for i in range(len(best_route) - 1):
        route.append(
            shortest_route(
                G,
                latitudes[best_route[i]],
                longitudes[best_route[i]],
                latitudes[best_route[i + 1]],
                longitudes[best_route[i + 1]],
            ),
        )
    return route


def plot_graph_route(G, route, weight):
    """ Plots the graph and the shortest route.
    Args:
        G: Graph (networkx)
        route: list of routes to plot
    """
    return ox.plot_graph_routes(G, route, route_linewidth=6, node_size=0, bgcolor='k')


# test
G = create_graph('Coimbra', 3000, 'drive')
# add speed to the graph
G = ox.add_edge_speeds(G)
# add travel time to the graph
G = ox.add_edge_travel_times(G)

# best route from genetic algorithm (genAlgorithmBestRoute): result = 1293 [9, 0, 2, 3, 6, 1, 7, 5, 4, 8]
best_route = [9, 0, 2, 3, 6, 1, 7, 5, 4, 8]
plot_graph_route(G, create_route(G, best_route), 'travel_time')
