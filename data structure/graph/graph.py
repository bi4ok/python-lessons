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
                self.RemoveEdge(self.vertex[v], self.vertex[i])
            self.vertex[v] = None
        else:
            pass
