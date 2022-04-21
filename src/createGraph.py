# (c) Tiago Tamagusko 2022
"""
Creates a networkx graph using OSMnx.

Usage:
    create_graph(location, dist, transport_mode)
Example:
    # Creates a graph from the coordinates of two addresses in Coimbra
    G = create_graph("Coimbra", 3000, "drive")
"""
from __future__ import annotations

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, LineString

import matplotlib.pyplot as plt
import plotly_express as px

import networkx as nx
import osmnx as ox

from coordinates import coordinates
ox.config(use_cache=True, log_console=True)


def create_graph(location, dist, transport_mode):
    """ Creates a networkx graph using OSMnx.
    Args:
        location: the location of the central node to build the graph
        dist: distance from the central node to the other nodes to be represented (meters).
        transport_mode: the mode of transport ("all_private", "all", "bike", "drive", "drive_service", "walk")
    Returns:
        the networkx graph

    # More on: https://osmnx.readthedocs.io/en/stable/osmnx.html and https://arxiv.org/pdf/1611.01890.pdf
    """
    return ox.graph_from_address(location, dist=dist, network_type=transport_mode)
