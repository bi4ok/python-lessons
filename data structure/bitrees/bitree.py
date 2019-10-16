import unittest


class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.r = None
        self.l = None
        self.level = 0


class BiTree:

    def __init__(self, item):
        self.root = item

    def add_branch(self, val):
        y = self.poisk(self.root, val)
        while y[1] is True:                                 # Цикл для нахождения места среди одинаковых элементов
            if y[0].r is not None:
                y = self.poisk(y[0].r, val)
            else:
                y[2] = 1
                break
        node = y[0]
        if y[2] == 0:
            node.l = val
        elif y[2] == 1:
            node.r = val
        x = node
        node = val
        node.parent = x
        node.level = node.parent.level + 1

    def delete_leaf(self, val):
        y = self.poisk(self.root, val)
        node = y[0]
        if node.value == val.value:
            if node.l is None and node.r is None:
                x = node
                node = node.parent
                if node.l == x:
                    node.l = None
                elif node.r == x:
                    node.r = None
            elif node.l is not None and node.r is None:
                x = node
                node = node.parent
                if node.l == x:
                    node.l = node.l.l
                elif node.r == x:
                    node.r = node.r.l
            elif node.r is not None and node.l is None:
                x = node
                node = node.parent
                if node.l == x:
                    node.l = node.l.r
                elif node.r == x:
                    node.r = node.r.r
            elif node.r is not None and node.l is not None:
                x = node
                zamena = self.minmax(node.r, "min")
                node = zamena.parent
                if node.l == zamena:
                    node.l = None
                elif node.r == zamena:
                    node.r = None
                if x is not self.root:
                    node = x.parent
                    if node.l == x:
                        node.l = zamena
                    elif node.r == x:
                        node.r = zamena
                else:
                    self.root = zamena
                zamena.l = x.l
                zamena.r = x.r

    def poisk(self, x, val):
        spisok = []
        node = x
        if node is not None and node.value == val.value:
            spisok.append(node)
            spisok.append(True)
            spisok.append(None)
            return spisok
        else:
            if val.value > node.value and node.r is not None:
                x = self.poisk(node.r, val)
                return x
            elif val.value < node.value and node.l is not None:
                x = self.poisk(node.l, val)
                return x
            else:
                spisok.append(node)
                spisok.append(False)
                if val.value >= node.value:
                    spisok.append(1)
                else:
                    spisok.append(0)
                return spisok

    def minmax(self, ot, val):
        y = self.poisk(self.root, ot)
        x = None
        node = y[0]
        if str(val) == "max":
            while node.r is not None:
                node = node.r
            x = node
        elif str(val) == "min":
            while node.l is not None:
                node = node.l
            x = node
        return x


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = BiTree(Node(10))
        self.s.add_branch(Node(14))
        self.s.add_branch(Node(12))
        self.s.add_branch(Node(16))
        self.s.add_branch(Node(6))
        self.s.add_branch(Node(4))
        self.s.add_branch(Node(8))

    def test_poisk(self):
        self.initialize()
        self.assertTrue(self.s.poisk(self.s.root, Node(3))[1] is False)     # Отсутствующее значение с добавление влево
        self.assertTrue(self.s.poisk(self.s.root, Node(3))[2] == 0)
        self.assertTrue(self.s.poisk(self.s.root, Node(4))[1] is True)      # Присутствующее значение
        self.assertTrue(self.s.poisk(self.s.root, Node(4))[2] is None)
        self.assertTrue(self.s.poisk(self.s.root, Node(5))[1] is False)     # Отсутствующее значение с добавление вправо
        self.assertTrue(self.s.poisk(self.s.root, Node(5))[2] == 1)
        self.s = None

    def test_add(self):
        self.initialize()
        self.assertTrue(self.s.poisk(self.s.root, Node(3))[1] is False)     # Добавление значения влево
        self.assertTrue(self.s.poisk(self.s.root, Node(3))[2] == 0)
        self.s.add_branch(Node(3))
        self.assertTrue(self.s.poisk(self.s.root, Node(3))[1] is True)
        self.assertTrue(self.s.poisk(self.s.root, Node(5))[1] is False)     # Добавление значения вправо
        self.assertTrue(self.s.poisk(self.s.root, Node(5))[2] == 1)
        self.s.add_branch(Node(5))
        self.assertTrue(self.s.poisk(self.s.root, Node(5))[1] is True)
        self.s.add_branch(Node(5))                                          # Добавление имеющегося значения
        self.assertTrue(self.s.root.l.l.r.r.value == 5)
        self.assertTrue(self.s.root.l.l.r.value == 5)
        self.s = None

    def test_minmax(self):
        self.initialize()
        self.assertTrue(self.s.minmax(self.s.root, "max").value == 16)      # поиск с корня максимального значения
        self.assertTrue(self.s.minmax(self.s.root, "min").value == 4)       # поиск с корня минимального значения
        self.assertTrue(self.s.minmax(Node(6), "max").value == 8)           # поиск с поддерева макс. значения
        self.assertTrue(self.s.minmax(Node(14), "min").value == 12)         # поиск с поддерева мин. значения
        self.s = None

    def test_del(self):
        self.initialize()
        self.assertTrue(self.s.root.l.l.value == 4)         # Удаление узла без потомков
        self.s.delete_leaf(Node(4))
        self.assertTrue(self.s.root.l.l is None)
        self.assertTrue(self.s.root.l.value == 6)           # Удаление узла с одним потомком
        self.s.delete_leaf(Node(6))
        self.assertTrue(self.s.root.l.value == 8)
        self.assertTrue(self.s.root.value == 10)            # Удаление корневовго узла с двумя потомками
        self.s.delete_leaf(Node(10))
        self.assertTrue(self.s.root.value == 12)
        self.s = None


if __name__ == '__main__':
    unittest.main()
