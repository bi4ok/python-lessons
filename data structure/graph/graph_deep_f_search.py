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
            cur_vert = self.vertex[VFrom]
            path.append(cur_vert)
            cur_vert.Hit = True
            if VFrom == VTo:
                return path
            for vert_index, vert in enumerate(self.vertex):
                if self.IsEdge(VFrom, vert_index) and vert == VTo:
                    path.append(vert)
                    return path
            for vert_index, vert in enumerate(self.vertex):
                if self.IsEdge(VFrom, vert_index) and not vert.Hit:
                    VFrom = vert_index
                    break
            else:
                path.pop()
                if not path:
                    return path
                next_vert = path.pop()
                VFrom = self.vertex.index(next_vert)
