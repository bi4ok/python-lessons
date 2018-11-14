import unittest


class Vertex:
    def __init__(self, value):
        self.value = value


class SimpleGraph:

    def __init__(self, mv):
        self.max_vertex = mv
        self.vertex = [None]*self.max_vertex
        self.m_adjency = [[0]*self.max_vertex, [0]*self.max_vertex, [0]*self.max_vertex, [0]*self.max_vertex, [0]*self.max_vertex]

    def add_vert(self, item):
        if self.vertex[-1] is None:
            self.vertex[self.vertex.index(None)] = item
            for i in range(self.max_vertex):
                self.m_adjency[self.vertex.index(item)][i] = 0
        else:
            return None

    def add_edge(self, item1, item2):
        if self.m_adjency[self.vertex.index(item1)][self.vertex.index(item2)] == 0:
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


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = SimpleGraph(5)
        self.s.add_vert(Vertex(1))
        self.s.add_vert(Vertex(2))
        self.s.add_vert(Vertex(3))
        self.s.add_vert(Vertex(4))

    def test_addvert(self):
        self.initialize()
        self.assertTrue(self.s.vertex[4] is None)
        self.s.add_vert(Vertex(5))
        self.assertTrue(self.s.vertex[4] is not None)
        self.s = None

    def test_addedge(self):
        self.initialize()
        self.assertTrue(self.s.m_adjency[0][1] == 0)
        self.s.add_edge(self.s.vertex[0], self.s.vertex[1])
        self.assertTrue(self.s.m_adjency[0][1] == 1)
        self.s = None

    def test_deledge(self):
        self.initialize()
        self.s.add_edge(self.s.vertex[0], self.s.vertex[1])
        self.assertTrue(self.s.m_adjency[0][1] == 1)
        self.s.del_edge(self.s.vertex[0], self.s.vertex[1])
        self.assertTrue(self.s.m_adjency[0][1] == 0)
        self.s = None

    def test_delvert(self):
        self.initialize()
        self.s.add_edge(self.s.vertex[0], self.s.vertex[1])
        self.s.add_edge(self.s.vertex[0], self.s.vertex[2])
        self.s.add_edge(self.s.vertex[0], self.s.vertex[3])
        self.assertTrue(self.s.m_adjency[0][1] == 1)
        self.assertTrue(self.s.m_adjency[0][2] == 1)
        self.assertTrue(self.s.m_adjency[0][3] == 1)
        self.s.del_vert(self.s.vertex[0])
        self.assertTrue(self.s.m_adjency[0][1] == 0)
        self.assertTrue(self.s.m_adjency[0][2] == 0)
        self.assertTrue(self.s.m_adjency[0][3] == 0)
        self.assertTrue(self.s.vertex[0] is None)
        self.s = None


if __name__ == '__main__':
    unittest.main()
