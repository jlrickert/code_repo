class Graph(object):
    def __init__(self, graph_dic=None):
        self.__graph_dic = dict()
        for v, edges in graph_dic.items():
            self.add_vertex(v)
            for e in edges:
                self.add_edge(v, e)

    def vertices(self):
        return set(self.__graph_dic.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dic:
            self.__graph_dic[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.__graph_dic[vertex1].add(vertex2)
        self.__graph_dic[vertex2].add(vertex1)

    def adj(self, src):
        return self.__graph_dic[src]

    def __generate_edges(self):
        edges = set()
        for vertex in self.__graph_dic:
            for neighbour in self.__graph_dic[vertex]:
                edges.add((vertex, neighbour))
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dic:
            res += str(k)+" "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge)+" "
        return res


def test_graph():
    g = {
        "a": ["d"],
        "b": ["a", "c"],
        "c": ["a", "f"],
        "d": ["b", "e", "f"],
        "e": ["b", "f"],
        "f": ["d", "e"],
    }
    graph = Graph(g)
    assert graph.adj("a") == {"b", "c", "d"}
    assert graph.adj("b") == {"a", "d", "e", "c"}
    assert graph.adj("c") == {"a", "b", "f"}
    assert graph.adj("d") == {"a", "b", "e", "f"}
    assert graph.adj("e") == {"b", "d", "f"}
    assert graph.adj("f") == {"c", "d", "e"}

    assert set(graph.edges()) == {
        ("a", "b"), ("a", "c"), ("a", "d"),
        ("b", "a"), ("b", "c"), ("b", "d"), ("b", "e"),
        ("c", "a"), ("c", "b"), ("c", "f"),
        ("d", "a"), ("d", "b"), ("d", "e"), ("d", "f"),
        ("e", "b"), ("e", "d"), ("e", "f"),
        ("f", "c"), ("f", "d"), ("f", "e")
    }
