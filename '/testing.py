import operator
from DEFUNCT.Graph import Graph, Vertex


def dijkstra_shortest_path(g, start_vertex):
    dist = []
    prev = []
    visited = []

    # Put all vertices in an unvisited queue.
    unvisited_queue = []

    for current_vertex in g.adjacency_list:
        unvisited_queue.append(current_vertex)

    # Start_vertex has a distance of 0 from itself
    start_vertex.distance = 0

    # One vertex is removed with each iteration; repeat until the list is
    # empty.
    while len(unvisited_queue) > 0:

        # Visit vertex with minimum distance from start_vertex
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)

        # Check potential path lengths from the current vertex to all neighbors.
        for adj_vertex in g.adjacency_list[current_vertex]:
            edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
            alternative_path_distance = current_vertex.distance + edge_weight

            # If shorter path from start_vertex to adj_vertex is found,
            # update adj_vertex's distance and predecessor
            if alternative_path_distance < adj_vertex.distance:
                adj_vertex.distance = alternative_path_distance
                adj_vertex.pred_vertex = current_vertex
                print(alternative_path_distance)


def get_shortest_path(g, start_vertex):
    # Start from end_vertex and build the path backwards
    visited = []
    nodes = []
    for value in g.adjacency_list[2].values():
        nodes.append(float(value))
    path = ""
    current_vertex = start_vertex
    i = 0
    while len(visited) < 15 and current_vertex is not None:
        current_vertex = g.adjacency_list[nodes.index(min(nodes))]
        path = " -> " + str(current_vertex.label) + path
        visited.append(current_vertex)
        i += 1

        current_vertex = current_vertex.pred_vertex

    path = start_vertex.label + path
    return path


# Program to find shortest paths from vertex A.
dist = []
prev = []
visited = []

g = Graph()

vertex_a = Vertex("A")
vertex_b = Vertex("B")
vertex_c = Vertex("C")
vertex_d = Vertex("D")
vertex_e = Vertex("E")
vertex_f = Vertex("F")
vertex_g = Vertex("G")
vertex_a1 = Vertex("A1")
vertex_b1 = Vertex("B1")
vertex_c1 = Vertex("C1")
vertex_d1 = Vertex("D1")
vertex_e1 = Vertex("E1")
vertex_f1 = Vertex("F1")
vertex_g1 = Vertex("G1")
g.add_vertex(vertex_a)
g.add_vertex(vertex_b)
g.add_vertex(vertex_c)
g.add_vertex(vertex_d)
g.add_vertex(vertex_e)
g.add_vertex(vertex_f)
g.add_vertex(vertex_g)
g.add_vertex(vertex_a1)
g.add_vertex(vertex_b1)
g.add_vertex(vertex_c1)
g.add_vertex(vertex_d1)
g.add_vertex(vertex_e1)
g.add_vertex(vertex_f1)
g.add_vertex(vertex_g1)

g.add_undirected_edge(vertex_a, vertex_b, 84)
g.add_undirected_edge(vertex_a, vertex_c, 7)
g.add_undirected_edge(vertex_a, vertex_d, 3)
g.add_undirected_edge(vertex_b, vertex_e, 6)
g.add_undirected_edge(vertex_c, vertex_d, 14)
g.add_undirected_edge(vertex_c, vertex_e, 2)
g.add_undirected_edge(vertex_d, vertex_f, 15)
g.add_undirected_edge(vertex_d, vertex_g, 12)
g.add_undirected_edge(vertex_e, vertex_f, 4)
g.add_undirected_edge(vertex_f, vertex_g, 1)
g.add_undirected_edge(vertex_a1, vertex_b, 84)
g.add_undirected_edge(vertex_a1, vertex_c, 7)
g.add_undirected_edge(vertex_a1, vertex_d, 3)
g.add_undirected_edge(vertex_b1, vertex_e, 6)
g.add_undirected_edge(vertex_c1, vertex_d, 1)
g.add_undirected_edge(vertex_c1, vertex_e, 24)
g.add_undirected_edge(vertex_d1, vertex_f, 15)
g.add_undirected_edge(vertex_d1, vertex_g, 12)
g.add_undirected_edge(vertex_e1, vertex_f, 4)
g.add_undirected_edge(vertex_f1, vertex_g, 11)
g.add_undirected_edge(vertex_a, vertex_b1, 8)
g.add_undirected_edge(vertex_a, vertex_c1, 7)
g.add_undirected_edge(vertex_a, vertex_d1, 3)
g.add_undirected_edge(vertex_b, vertex_e1, 6)
g.add_undirected_edge(vertex_c, vertex_d1, 16)
g.add_undirected_edge(vertex_c, vertex_e1, 2)
g.add_undirected_edge(vertex_d, vertex_f1, 115)
g.add_undirected_edge(vertex_d, vertex_g1, 102)
g.add_undirected_edge(vertex_e, vertex_f1, 4)
g.add_undirected_edge(vertex_f, vertex_g1, 123)

# Run Dijkstra's algorithm first.
dijkstra_shortest_path(g, vertex_a)

# Sort the vertices by the label for convenience; display shortest path for each vertex
# from vertex_a.
for v in sorted(g.adjacency_list, key=operator.attrgetter("label")):
    if v.pred_vertex is None and v is not vertex_a:
        print("A to %s: no path exists" % v.label)
    else:
        print("A to %s: %s (total weight: %g)" % (v.label, get_shortest_path(g, vertex_a), v.distance))
