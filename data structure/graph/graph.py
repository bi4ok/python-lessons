class Vertex:
    def __init__(self, value):
        self.value = value


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        if self.vertex[-1] is None:
            index = self.vertex.index(None)
            self.vertex[index] = Vertex(v)
            for i in range(self.max_vertex):
                self.m_adjacency[index][i] = 0
        else:
            pass

    def AddEdge(self, v1, v2):
        if max(v1, v2) in range(len(self.vertex)):
            print(max(v1, v2))
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
        else:
            pass

    def IsEdge(self, v1, v2):
        if max(v1, v2) in range(len(self.vertex)):
            if self.m_adjacency[v1][v2] == 1:
                return True
        return False

    def RemoveEdge(self, v1, v2):
        if max(v1, v2) in range(len(self.vertex)):
            if self.m_adjacency[v1][v2] == 1:
                self.m_adjacency[v1][v2] = 0
                self.m_adjacency[v2][v1] = 0
        else:
            pass

    def RemoveVertex(self, v):
        if v in range(len(self.vertex)):
            for i in range(self.max_vertex):
                self.RemoveEdge(v, i)
            self.vertex[v] = None
        else:
            pass



s1 = SimpleGraph(10)
s1.AddVertex(0)
s1.AddVertex(1)
s1.AddVertex(2)
s1.AddVertex(3)
s1.AddVertex(4)
s1.AddVertex(5)
s1.AddEdge(0, 1)
s1.AddEdge(0, 2)
s1.AddEdge(1, 3)
s1.AddEdge(2, 4)
s1.AddEdge(4, 5)
print(s1.IsEdge(0, 1))
print(s1.vertex)
for i in s1.m_adjacency:
    print(i)
for i in s1.DepthFirstSearch(s1.vertex[0], s1.vertex[5]):
    print(i.Value)