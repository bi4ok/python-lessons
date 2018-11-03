import unittest


class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.leafs = [None]
        self.flag = 0
        self.level = 0


class SimpleTree:

    def __init__(self):
        self.root = None

    def add_branch(self, val, it2):
        node = self.poisk(self.root, val)
        if node.value == val.value:
            if node.leafs[0] is None:
                node.leafs = [it2]
                node.leafs.append(None)
            else:
                node.leafs.insert(-1, it2)
            x = node
            node = it2
            node.parent = x
            node.level = node.parent.level + 1
        else:
            return None

    def delete_leaf(self, val):
        node = self.poisk(self.root, val)
        if node.value == val.value:
            node.parent.leafs.remove(node)
            node.value = None
            node.parent = None
            node.leafs = [None]
        else:
            return None

    def spisokval(self, val):
        z = 0
        node = self.root
        spisok = []
        while node.value is not None:
            if (val is None or node.value == val) and node.flag == 0:
                spisok.append(node)
                node.flag = 1
            if node.leafs[z] is not None:
                node = node.leafs[z]
                z = 0
            elif node.leafs[z] is None:
                if node.parent is not None:
                    z = node.parent.leafs.index(node) + 1
                    node = node.parent
                else:
                    break
        self.flagsall(0)
        return spisok

    def flagsall(self, val):
        z = 0
        node = self.root
        while node.value is not None:
            node.flag = val
            if node.leafs[z] is not None:
                node = node.leafs[z]
                z = 0
            elif node.leafs[z] is None:
                if node.parent is not None:
                    z = node.parent.leafs.index(node) + 1
                    node = node.parent
                else:
                    break

    def perenos(self, val, item):
        node = self.poisk(self.root, val)
        if node.value == val.value:
            x = node
            node = node.parent
            node.leafs.remove(x)
        else:
            return None
        node = self.poisk(self.root, item)
        if node.value == item.value:
            node.leafs.insert(-1, x)
            z = node.leafs.index(x)
            x = node
            node = node.leafs[z]
            node.parent = x
        else:
            return None

    def schet(self):
        z = 0
        node = self.root
        roots = 0
        leafs = 0
        while node.value is not None:
            if node.leafs[0] is None and node.flag == 0:
                leafs += 1
                node.flag = 1
            elif node.leafs[0] is not None and node.flag == 0:
                roots += 1
                node.flag = 1
            if node.leafs[z] is not None:
                node = node.leafs[z]
                z = 0
            elif node.leafs[z] is None:
                if node.parent is not None:
                    z = node.parent.leafs.index(node) + 1
                    node = node.parent
                else:
                    break
        self.flagsall(0)
        return {"узлы": roots, "листья": leafs}

    def poisk(self, x, val):
        node = x
        if node.value == val.value:
            return node
        for i in node.leafs[0:-1]:
            x = self.poisk(i, val)
            if x.value == val.value:
                return x
        return x


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = SimpleTree()
        self.s.root = Node(0)
        self.s.add_branch(Node(0), Node(1))
        self.s.add_branch(Node(0), Node(2))
        self.s.add_branch(Node(1), Node(3))
        self.s.add_branch(Node(1), Node(4))
        self.s.add_branch(Node(2), Node(5))
        self.s.add_branch(Node(2), Node(6))

    def test_add(self):
        self.initialize()
        self.assertTrue(self.s.root.leafs[2] is None)           # Место для листка свободно
        self.s.add_branch(Node(0), Node(99))
        self.assertTrue(self.s.root.leafs[2].value == 99)       # Лист появился
        self.s.delete_leaf(Node(1))
        self.s.delete_leaf(Node(2))
        self.s.delete_leaf(Node(99))

    def test_del(self):
        self.initialize()
        self.assertTrue(self.s.root.leafs[1] is not None)           # Проверка наличия ветви
        self.s.delete_leaf(Node(2))
        self.assertTrue(self.s.root.leafs[1] is None)               # Проверка отсутствия ветви
        self.s.delete_leaf(Node(1))

    def test_spisokall(self):
        self.initialize()
        self.assertTrue(len(self.s.spisokval(None)) == 7)
        self.s.delete_leaf(Node(1))
        self.s.delete_leaf(Node(2))

    def test_spisokval(self):
        self.initialize()
        self.s.add_branch(Node(1), Node(99))
        self.s.add_branch(Node(1), Node(99))
        self.s.add_branch(Node(1), Node(99))
        self.assertTrue(len(self.s.spisokval(99)) == 3)
        self.s.delete_leaf(Node(1))
        self.s.delete_leaf(Node(2))

    def test_perenos(self):
        self.initialize()
        self.assertTrue(self.s.root.leafs[0].leafs[0].value == 3)           # слот занят элментом 3
        self.assertTrue(self.s.root.leafs[1].leafs[0].leafs[0] is None)     # слот после элемента 5 свободен
        self.s.perenos(Node(3), Node(5))
        self.assertTrue(self.s.root.leafs[0].leafs[0].value != 3)           # слот с элементом 3 удален
        self.assertTrue(self.s.root.leafs[1].leafs[0].leafs[0].value == 3)  # слот после элемента 5 занят слотом с эл. 3
        self.s.delete_leaf(Node(1))
        self.s.delete_leaf(Node(2))

    def test_schet(self):
        self.initialize()
        self.assertTrue(self.s.schet()["узлы"] == 3)
        self.assertTrue(self.s.schet()["листья"] == 4)
        self.s.delete_leaf(Node(1))
        self.s.delete_leaf(Node(2))


if __name__ == '__main__':
    unittest.main()