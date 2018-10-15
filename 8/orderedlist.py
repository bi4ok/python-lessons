import unittest


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class Orderedlist:
    asc = True

    def __init__(self):
        self.head = None
        self.tail = None

    def ascending(self, val):
        self.asc = val
        return

    def sravni(self, item, node1):
        if self.asc is True:
            x = str(node1.value)
            x = ''.join(x.split())
            y = str(item.value)
            y = ''.join(y.split())
            if int(y) < int(x):
                return True
            else:
                return False
        elif self.asc is False:
            x = str(node1.value)
            x = ''.join(x.split())
            y = str(item.value)
            y = ''.join(y.split())
            if int(y) > int(x):
                return True
            else:
                return False

    def addonval(self, item):
        if self.head is None:           # Добавление первого элемента, обозначение головы и хвоста
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
            return
        Node = self.head
        if self.sravni(item, Node) is True:         # Сравнение с первым элементом,замена head
            self.head = item
            Node.prev = item
            item.next = Node
            return
        elif item.value == Node.value:              # Добавление повторяющихся элементов
            x = Node.next
            Node.next = item
            item.next = x
            item.prev = Node
            return
        while Node is not None:
            if self.sravni(item, Node) is True:     # Добавление элемента между тем который меньше и тем, который больше
                x = Node.prev
                Node.prev = item
                item.prev = x
                item.next = Node
                item.prev.next = item
                return
            elif Node.next is None:                 # Добавление элемента в конец, замена tail
                self.tail = item
                Node.next = item
                item.prev = Node
                return
            Node = Node.next

    def searchonval(self, val):
        Node = self.head
        while Node != None:
            if Node.value == val:
                return Node
            elif self.asc is True and Node.value > val:
                print("Числа нет в списке")
                return None
            elif self.asc is False and Node.value < val:
                print("Числа нет в списке")
                return None
            Node = Node.next
        print("Числа нет в списке")
        return None

    def delonval(self, val):
        Node = self.searchonval(val)
        if Node is None:
            return None
        elif Node.value == val:
            if Node.prev != None:
                Node = Node.prev
                Node.next = Node.next.next
            else:
                self.head = Node.next
            if Node.next != None:
                Node = Node.next
                Node.prev = Node.prev.prev
            else:
                self.tail = Node

    def printall(self):
        Node = self.head
        while Node != None:
            print(Node.value)
            Node = Node.next


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.s = Orderedlist()
        self.s.ascending(True)
        self.s.addonval(Node(1))
        self.s.addonval(Node(2))
        self.s.addonval(Node(3))

    def testaddonval(self):
        self.s.ascending(True)
        self.s.addonval(Node(100))
        self.assertTrue(self.s.tail.value == 100)
        self.s.delonval(100)
        self.s.ascending(False)
        self.s.addonval(Node(100))
        self.assertTrue(self.s.head.value == 100)
        self.s.delonval(100)

    def testsearchonval(self):
        self.s.ascending(True)
        self.s.addonval(Node(5))
        self.assertTrue(self.s.searchonval(5).value == 5)
        self.assertTrue(self.s.searchonval(4) is None)
        self.s.ascending(False)
        self.assertTrue(self.s.searchonval(5) is None)
        self.s.delonval(5)

    def testdelonval(self):
        self.s.ascending(True)
        self.s.addonval(Node(5))
        self.s.ascending(False)
        self.assertTrue(self.s.delonval(5) is None)
        self.s.ascending(True)
        self.s.delonval(5)
        self.assertTrue(self.s.tail.value != 5)

    def tearDown(self):
        self.s.ascending(True)
        self.s.delonval(1)
        self.s.delonval(2)
        self.s.delonval(3)


if __name__ == '__main__':
    unittest.main()


