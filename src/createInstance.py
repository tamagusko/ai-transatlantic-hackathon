from __future__ import annotations

import osmnx as ox
import pandas as pd
from coordinates import coordinates
from createGraph import create_graph
from plotRoute import plot_graph_route
from shortestRoute import shortest_route
ox.config(use_cache=True, log_console=True)

# create the graph with the OSMnx library (location = 'Coimbra', radius = 3000, transport_mode= 'drive')
G = create_graph('Coimbra', 3000, 'drive')
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)


def get_distance_matrix(df):
    """
    Returns the distance matrix between each client.
    Args:
        dataset: The dataset must have two columns, one for the clients and one for the address coordinates.
    """
    distance_matrix = []
    for i in range(len(df)):
        for j in range(len(df)):
            if i != j:
                distance_matrix.append(
                    shortest_route(
                        G, df.iloc[i]['coordinates'], df.iloc[j]['coordinates'],
                    ),
                )
    return distance_matrix


df = pd.read_csv(
    './data/processed/clientAddressCoordinates.csv',
    sep=';', encoding='utf-8',
)
# print(get_distance_matrix(df))
