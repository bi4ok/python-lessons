class Vertex:
    def __init__(self, val):
        self.Value = val
        self.Hit = False


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
            self.m_adjacency[v1][v2] = 1
            self.m_adjacency[v2][v1] = 1
        else:
            pass

    def IsEdge(self, v1, v2):
        if max(v1, v2) in range(len(self.vertex)):
            return self.m_adjacency[v1][v2] == 1
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

    def DepthFirstSearch(self, VFrom, VTo):
        path = []
        for vert in self.vertex:
            if vert:
                vert.Hit = False
        while True:
            path.append(VFrom)
            index = self.vertex.index(VFrom)
            VFrom.Hit = True
            if VFrom == VTo:
                return path
            for vert in self.vertex:
                vert_index = self.vertex.index(vert)
                if self.IsEdge(index, vert_index) and vert == VTo:
                    path.append(vert)
                    return path
            for vert in self.vertex:
                vert_index = self.vertex.index(vert)
                if self.IsEdge(index, vert_index) and not vert.Hit:
                    VFrom = vert
                    break
            else:
                path.pop()
                if not path:
                    return path
                VFrom = path.pop()