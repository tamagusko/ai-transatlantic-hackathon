# (c) Tiago Tamagusko 2022
"""
Create an instance for the distances between clients.
Returns an n x n matrix with n = number of clients.

Usage:
    get_distance_matrix(df)
Example:
    # Creates a matrix for the distances between clients.
    df = pd.read_csv('./data/processed/clientCoordinates.csv', sep=';')
    get_distance_matrix(df)
"""
from __future__ import annotations

import numpy as np
import osmnx as ox
from createGraph import create_graph
from shortestRoute import shortest_route_length
# import pandas as pd  # uncomment in test
ox.config(use_cache=True, log_console=True)

# create the graph with the OSMnx library (location = 'Coimbra', radius = 3000, transport_mode= 'drive')
G = create_graph('Coimbra', 3000, 'drive')
# add speed to the graph
G = ox.add_edge_speeds(G)
# add travel time to the graph
G = ox.add_edge_travel_times(G)


def get_distance_matrix(df):
    """
    Returns the distance matrix between each client using the latitude and longitude.
    Args:
        df: The dataset must have two columns latitude and longitude.
    """
    latitudes = df['latitude'].to_list()
    longitudes = df['longitude'].to_list()
    distance_matrix = np.matrix(np.zeros((len(latitudes), len(longitudes))))
    for i in range(len(df)):
        for j in range(len(df)):
            distance_matrix[i, j] = int(
                shortest_route_length(
                    G, latitudes[i], longitudes[i], latitudes[j], longitudes[j],
                ),
            )
    return distance_matrix

# test
# df = pd.read_csv('./data/processed/clientCoordinates.csv', sep=';')
# print(get_distance_matrix(df))
