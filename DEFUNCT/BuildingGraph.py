# Nearest Neighbor with constraints
from DistancesMatrix import load_distances

from Graph import *


# Loop through the distances array and
def building_graph(distances, min_table, min_table2, load, g):
    # Fill each array with initial value 10000 (AKA infinity) for the array of minimum distances and
    # empty dictionaries for the array of hash tables which include: the index representing the FROM location,
    # the TO location string as the key, and the distance as the value.
    counter = 0
    vertices = []

    for ind, location in enumerate(distances):
        vertex = Vertex(str(location[0]))
        vertices.append(vertex)

        g.add_vertex(vertex)
        print(vertex.label)
        counter += 1

    for package in load:

        # Loop through the lists that are pulled from the CSV file.
        for f, i in enumerate(distances):

            if package[1].lstrip() == str(i[0]):

                # Loop through each list within the distances list.
                # This targets the actual distance. Each distance's index
                # consistently corresponds with its address and thus can be used to track which location is selected.
                for l, j in enumerate(i):

                    # Ignore the first element of each list, which is the address.
                    if l != 0:

                        # Add the undirected edge to g. reflecting the distance (float(j)) from distance[l][0] to i[0]
                        print(i[0])
                        print(distances[l][0])
                        g.add_undirected_edge(vertices[f], vertices[l], float(j))

    return g