from __future__ import annotations

import osmnx as ox
from coordinates import coordinates
from createGraph import create_graph
from plotRoute import plot_graph_route
from shortestRoute import shortest_route
ox.config(use_cache=True, log_console=True)

# this list will be created by the optimization function based on client list
G = create_graph('Coimbra', 3000, 'drive')
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)
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


plot_graph_route(G, route, 'travel_time')
