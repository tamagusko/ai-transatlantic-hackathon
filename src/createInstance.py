# (c) Tiago Tamagusko 2022
# BUG return NEED TO FIX
from __future__ import annotations

import osmnx as ox
import pandas as pd
from createGraph import create_graph
from shortestPathLen import shortest_path_len
ox.config(use_cache=True, log_console=True)

# create the graph with the OSMnx library (location = 'Coimbra', radius = 3000, transport_mode= 'drive')
G = create_graph('Coimbra', 3000, 'drive')
# add speed to the graph
G = ox.add_edge_speeds(G)
# add travel time to the graph
G = ox.add_edge_travel_times(G)


def get_distance_matrix(df):
    """
    Returns the distance matrix between each client.
    Args:
        dataset: The dataset must have two columns, one for the clients and one for the address coordinates.
    """
    latitudes = df['latitude'].to_list()
    longitudes = df['longitude'].to_list()
    distance_matrix = []
    for i in range(len(df)):
        for j in range(len(df)):
            if i != j:
                distance_matrix.append(
                    shortest_path_len(
                        G, longitudes[i], latitudes[i], longitudes[j], latitudes[j],
                    ),
                )
    return distance_matrix


df = pd.read_csv('./data/processed/clientCoordinates.csv', sep=';')
print(get_distance_matrix(df))
