import unittest


class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.r = None
        self.l = None
        self.level = 0


class ArrayTree:

    def __init__(self, sz):
        self.root = None
        self.size = sz-1
        self.massiv = [None]*self.size

    def add_branch(self, val):
        if self.root is None:
            self.root = val
            self.massiv.insert(0, self.root)
        y = self.poisk(self.root, val)
        if y is None:
            return None
        elif y > 0:
            return self.massiv[y]
        elif y < 0:
            self.massiv[-y] = val
            node = val
            node.parent = self.massiv[(-y-1)//2]
            node = node.parent
            if node.value > val.value:
                node.l = val
            if node.value < val.value:
                node.r = val

    def poisk(self, x, val):
        node = x
        if node is not None and node.value == val.value:
            return self.massiv.index(node)
        else:
            if val.value > node.value:
                if node.r is None and (2*(self.massiv.index(node))+2) <= self.size:
                    return -(2*(self.massiv.index(node))+2)
                elif (2*(self.massiv.index(node))+2) > self.size:
                    return None
                x = self.poisk(node.r, val)
                return x
            elif val.value < node.value:
                if node.l is None and (2*(self.massiv.index(node))+1) <= self.size:
                    return -(2*(self.massiv.index(node))+1)
                elif (2*(self.massiv.index(node))+1) > self.size:
                    return None
                x = self.poisk(node.l, val)
                return x
            else:
                return None


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = ArrayTree(7)
        self.s.add_branch(Node(12))
        self.s.add_branch(Node(16))
        self.s.add_branch(Node(14))
        self.s.add_branch(Node(8))

    def test_poisk(self):
        self.initialize()
        self.s.add_branch(Node(20))
        self.s.add_branch(Node(10))
        self.assertTrue(self.s.poisk(self.s.root, Node(6)) == -3)       # Найдено свободное место
        self.s.add_branch(Node(6))
        self.assertTrue(self.s.poisk(self.s.root, Node(3)) is None)     # Все дерево пройдено,совпадений нет
        self.assertTrue(self.s.poisk(self.s.root, Node(20)) == 6)       # Присутствующее значение
        self.s = None

    def test_add(self):
        self.initialize()
        self.assertTrue(self.s.poisk(self.s.root, Node(20)) == -6)      # Место под значение свободно
        self.s.add_branch(Node(20))                                     # Значение добавлено
        self.assertTrue(self.s.poisk(self.s.root, Node(20)) == 6)       # Место под значение занято
        self.s.add_branch(Node(6))
        self.s.add_branch(Node(10))
        self.assertTrue(self.s.massiv[6].value == 20)                   # Соответствие значений индексам в массиве
        self.assertTrue(self.s.massiv[5].value == 14)
        self.assertTrue(self.s.massiv[4].value == 10)
        self.assertTrue(self.s.massiv[3].value == 6)
        self.assertTrue(self.s.massiv[2].value == 16)
        self.assertTrue(self.s.massiv[1].value == 8)
        self.assertTrue(self.s.massiv[0].value == 12)
        self.s = None


if __name__ == '__main__':
    unittest.main()