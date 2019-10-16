import unittest


class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.r = None
        self.l = None
        self.level = 0


class Pyramid:

    def __init__(self, sz):
        self.root = None
        self.size = sz
        self.massiv = [None]*self.size
        self.freeslot = None

    def add_branch(self, item):
        if self.freeslot in self.massiv:
            self.massiv[self.massiv.index(self.freeslot)] = item
        else:
            print(None)
            return None
        if self.massiv.index(item) != 0:
            item.parent = self.massiv[abs(self.massiv.index(item)-1) // 2]
        x = self.poisk(item)
        if item.parent is not None:
            item = item.parent
            item.l = self.massiv[self.massiv.index(item)*2+1]
            item.r = self.massiv[self.massiv.index(item)*2+2]

    def poisk(self, item):
        if item.parent is not None:
            if item.parent.value < item.value:
                item.value, item.parent.value = item.parent.value, item.value
                return self.poisk(item.parent)
            else:
                return item
        return None

    def udaleniemax(self):
        if self.freeslot in self.massiv:
            self.massiv[0].value = self.massiv[self.massiv.index(self.freeslot)-1].value
            self.massiv[self.massiv.index(self.freeslot)-1] = None
        else:
            self.massiv[0].value = self.massiv[-1].value
            self.massiv[-1] = None
        self.poiskvniz(self.massiv[0])

    def poiskvniz(self, item):
        if item.l and item.r is not None:
            if max(item.l.value, item.r.value) > item.value:
                if item.l.value > item.r.value:
                    item.value, item.l.value = item.l.value, item.value
                    return self.poiskvniz(item.l)
                else:
                    item.value, item.r.value = item.r.value, item.value
                    return self.poiskvniz(item.r)
            else:
                return item
        return None


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = Pyramid(11)
        self.s.add_branch(Node(12))
        self.s.add_branch(Node(10))
        self.s.add_branch(Node(14))
        self.s.add_branch(Node(8))
        self.s.add_branch(Node(16))
        self.s.add_branch(Node(0))
        self.s.add_branch(Node(3))
        self.s.add_branch(Node(11))
        self.s.add_branch(Node(5))

    def test_add(self):
        self.initialize()                                                      # В массиве 9 элементов,индекс 9 свободен
        self.assertTrue(self.s.massiv[9] is None)                              # Элемент перемещается к корню пирамиды
        self.s.add_branch(Node(15))                                            # Элемент имеет значение меньше родителя
        self.assertTrue(self.s.massiv[1].value == 15)                          # Но больше, чем у потомков
        self.assertTrue(self.s.massiv[1].value < self.s.massiv[1].parent.value)
        self.assertTrue(self.s.massiv[1].value > max(self.s.massiv[1].r.value, self.s.massiv[1].l.value))
        self.s = None

    def test_udalenie(self):
        self.initialize()
        self.assertTrue(self.s.massiv[0].value == 16)               # Нулевой элемент равен 16
        self.assertTrue(self.s.massiv[8].value == 5)                # Крайний правый на нижнем уровне элемент равен 5
        self.s.udaleniemax()
        self.assertTrue(self.s.massiv[0].value == 14)               # Нулевое элемент изменился на 14
        self.assertTrue(self.s.massiv[8] is None)                   # Крайний правый элемент исчез
        self.s = None


if __name__ == '__main__':
    unittest.main()