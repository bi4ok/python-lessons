import unittest
import stack


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

    def poiskputi(self, item1, item2):
        s1 = stack.Stack()
        s1.clear_stack()
        for i in self.vertex:
            i.hit = False
        curver = item1
        sver = item2
        curver.hit = True
        s1.push(curver)
        if curver == sver:
            return s1
        s1 = self.rekpoisk(curver, sver, s1)
        return s1

    def rekpoisk(self, item1, item2, st):
        s1 = st
        curver = item1
        sver = item2
        for i in self.vertex:
            if self.check_edge(curver, i) is True and i.hit is False:
                if i == sver:
                    s1.push(i)
                    return s1
                else:
                    i.hit = True
                    s1.push(i)
                    x = self.rekpoisk(i, item2, s1)
                    if x is None:
                        s1.pop()
                    if x is not None:
                        return s1
        return None


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = SimpleGraph(8)
        self.s.add_vert(Vertex(1))
        self.s.add_vert(Vertex(2))
        self.s.add_vert(Vertex(3))
        self.s.add_vert(Vertex(4))
        self.s.add_vert(Vertex(5))
        self.s.add_vert(Vertex(6))
        self.s.add_vert(Vertex(7))
        self.s.add_vert(Vertex(8))
        self.s.add_edge(self.s.vertex[0], self.s.vertex[1])
        self.s.add_edge(self.s.vertex[0], self.s.vertex[4])
        self.s.add_edge(self.s.vertex[1], self.s.vertex[2])
        self.s.add_edge(self.s.vertex[1], self.s.vertex[3])
        self.s.add_edge(self.s.vertex[1], self.s.vertex[4])
        self.s.add_edge(self.s.vertex[3], self.s.vertex[5])
        self.s.add_edge(self.s.vertex[5], self.s.vertex[6])
        self.s.add_edge(self.s.vertex[6], self.s.vertex[7])
        self.s.add_edge(self.s.vertex[1], self.s.vertex[7])

    def test_poisk(self):
        self.initialize()                                   # Кратчайший путь 0-1-7. Алгоритм выбрал 0-1-3-5-6-7
        self.assertTrue(self.s.poiskputi(self.s.vertex[0], self.s.vertex[7]).size() == 6)
        self.s = None


if __name__ == '__main__':
    unittest.main()