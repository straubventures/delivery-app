from Graph import *


def list_of_lists(distance_matrix):
    graph = Graph()
    # l is the from location
    for l, location in enumerate(distance_matrix):
        new_vertex = Vertex(location[0])
        graph.add_vertex(new_vertex)

    # l is the from location
    for l, location in enumerate(distance_matrix):

        # d is the to location
        for d, distance in enumerate(location):
            print(graph.edge_weights)
            graph.add_undirected_edge(graph.vertices[l], graph.vertices[d - 1], location[d])
    return graph

