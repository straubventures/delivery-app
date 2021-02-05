class Vertex:

    # Constructor for a new Vertx object. All vertex objects
    # start with a distance of positive infinity.
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None
        self.visited = False


class Edge:
    def __init__(self):
        self.to = ""
        self.origin = ""
        self.weight = 0


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        self.vertices = []


    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
        self.vertices.append(new_vertex)


    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):


        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

  #
  #
  # def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
  #
  #       changed1 = False
  #       changed2 = False
  #       for i, vertex in enumerate(self.vertices):
  #           if vertex_a.label == self.vertices[i].label:
  #               vertex_a = self.vertices[i]
  #               changed1 = True
  #           elif vertex_b.label == self.vertices[i].label:
  #               vertex_b = self.vertices[i]
  #               changed2 = True
  #           else: continue
  #       if changed1 is True and changed2 is True:
  #           self.add_directed_edge(vertex_a, vertex_b, weight)
  #           self.add_directed_edge(vertex_b, vertex_a, weight)
  #       else:
  #           print("ERROR")
  #           return
