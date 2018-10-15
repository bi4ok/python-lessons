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

    def delonval(self,val):
        Node = self.head
        while Node != None:
            if Node.value == val:
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
                break
            Node = Node.next

    def printall(self):
        Node = self.head
        while Node != None:
            print(Node.value)
            Node = Node.next


s = Orderedlist()
s.ascending(True)
s.addonval(Node(1))
s.addonval(Node(2))
s.addonval(Node(4))
s.addonval(Node(4))
s.addonval(Node(5))
s.searchonval(3)
s.printall()
print(s.head.value, s.tail.value)
