# (c) Tiago Tamagusko 2022
# BUG return NEED TO FIX
from __future__ import annotations

import time

import numpy as np
import osmnx as ox
import pandas as pd
from createGraph import create_graph
from shortestRoute import shortest_route_length
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
    distance_matrix = np.matrix(np.zeros((len(df), len(df))))
    for i in range(len(df)):
        for j in range(len(df)):
            time.sleep(1)
            distance_matrix[i, j](
                shortest_route_length(
                    G, longitudes[i], latitudes[i], longitudes[j], latitudes[j],
                ),
            )
    return distance_matrix


df = pd.read_csv('./data/processed/clientCoordinates.csv', sep=';')
# print(get_distance_matrix(df))
distance_matrix = np.matrix(np.zeros((len(df), len(df))))
distance_matrix[0, 1] = shortest_route_length(
    G, 40.2019077, -8.4132559, 40.2079321, 8.4241537,
)
# print(shortest_route_length(G, 40.2019077, -8.4132559, 40.2079321, 8.4241537))
print(df.head())
