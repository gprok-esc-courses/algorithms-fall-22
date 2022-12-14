

class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def connect(self, vertex, weight):
        edge = Edge(vertex, weight)
        self.edges.append(edge)

    def __str__(self):
        s = self.value + " "
        for edge in self.edges:
            s += "[" + edge.vertex.value + "," + str(edge.weight) + "] "
        return s


class Graph:
    def __init__(self, directed: bool, weighted: bool):
        self.vertices = {}
        self.directed = directed
        self.weighted = weighted

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.vertices[value] = vertex

    def display(self):
        for index in self.vertices:
            print(self.vertices[index])

    def connect(self, va: str, vb: str, **kwargs):
        weight = 1
        if self.weighted:
            weight = kwargs['weight'] if 'weight' in kwargs else 1
        self.vertices[va].connect(self.vertices[vb], weight)
        if not self.directed:
            self.vertices[vb].connect(self.vertices[va], weight)


if __name__ == '__main__':
    graph = Graph(True, True)
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')

    graph.connect('A', 'B')
    graph.connect('B', 'C', weight=67)

    graph.display()
