import stack
import modstack


class Vertex:
    def __init__(self, value):
        self.value = value
        self.hit = False


class SimpleGraph:

    def __init__(self, mv):
        self.max_vertex = mv
        self.m_adjency = []
        for i in range(self.max_vertex):
            self.m_adjency.append([0]*self.max_vertex)
        self.vertex = [None]*self.max_vertex

    def add_vert(self, item):
        if self.vertex[-1] is None:
            self.vertex[self.vertex.index(None)] = item
            for i in range(self.max_vertex):
                self.m_adjency[self.vertex.index(item)][i] = 0
        else:
            return None

    def add_edge(self, item1, item2):
        if item1 and item2 is not None:
            self.m_adjency[self.vertex.index(item1)][self.vertex.index(item2)] = 1
            self.m_adjency[self.vertex.index(item2)][self.vertex.index(item1)] = 1
        else:
            return None

    def check_edge(self, item1, item2):
        if self.m_adjency[self.vertex.index(item1)][self.vertex.index(item2)] == 1:
            return True
        return False

    def del_edge(self, item1, item2):
        if self.m_adjency[self.vertex.index(item1)][self.vertex.index(item2)] == 1:
            self.m_adjency[self.vertex.index(item1)][self.vertex.index(item2)] = 0
            self.m_adjency[self.vertex.index(item2)][self.vertex.index(item1)] = 0

    def del_vert(self, item):
        for i in range(self.max_vertex):
            self.del_edge(item, self.vertex[i])
        self.vertex[self.vertex.index(item)] = None

    def DepthFirstSearch(self, VFrom, VTo):
        path = stack.Stack()
        path.clear_stack()
        self.clearing()
        while VFrom != VTo:
            print(VFrom.value, 'start')
            path.push(VFrom)
            VFrom.hit = True
            for vert in self.vertex:
                if self.check_edge(VFrom, vert) and vert == VTo:
                    path.push(vert)
                    return path
            for vert in self.vertex:
                if self.check_edge(VFrom, vert) and not vert.hit:
                    VFrom = vert
                    break
            else:
                check = path.pop()
                if not check:
                    return None
                VFrom = path.pop()
            print(path)
        return path

    def filter(self, spisok, item, sf):
        for j in spisok:
            if item == j[1]:
                if j[1] not in sf:
                    sf.insert(0, j[1])
                if j[0] not in sf:
                    sf.insert(0, j[0])
                spisok.remove(j)
                self.filter(spisok, j[0], sf)
        return sf

    def clearing(self):
        for i in self.vertex:
            if i:
                i.hit = False