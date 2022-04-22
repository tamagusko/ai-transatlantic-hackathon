# Output result formats to guide the development team


With the modules developed so far, with the addresses of the clients we can calculate the coordinates (coordenadas.py).

With these coordinates, we generate a graph with the shortest distance (based on travel time) between customers. However, we need to know the delivery order. So, we have to write an objective function that takes into account the travel times and nodes of a route between clients. That is, for five clients, the result could be:

client1, client3, client4, client2, client5

To feed this algorithm, I can write a matrix with the travel time between each client. With this matrix, i.e.:

```python
# example, random travel distance matrix for 5 clients

#                          1   2   3   4   5
travel_times = np.array([[15, 10, 11, 10, 12],
                         [10, 11, 15, 11, 11],
                         [10, 12, 16, 23, 5],
                         [10, 13, 12, 22, 1000],
                         [10, 14, 13, 11, 15]])

# 1000: route does not exist
```

Also, I can easily write a list with clients coordinates, i.e.:

```python
# example, from the coordinates of the clients

#                   1           2           3             4              5
client_coords = [(42, 11), (42.5, 10), (42.3, 11.2), (42.6, 11.11), (42.5, 12)]
```

We can use brute force, genetic algorithms, or others to solve the problem.

The expected output format is on list, i.e.:

option 1: [ID_client1, ID_client3, ID_client4, ID_client2, ID_client5]  
option 2: [[lat1, long1], [lat3, long3], [lat4, long4], [lat2, long2], [lat5, long5]]  
option 3: [address1, address3, address4, address2, address15]

Other formats can be adopted.