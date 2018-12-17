class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.value < v2.value:
            return -1
        elif v1.value == v2.value:
            return 0
        else:
            return 1

    def add(self, value):
        if self.head is None:           # Добавление первого элемента, обозначение головы и хвоста
            self.head = value
            self.tail = value
            value.prev = None
            value.next = None
            return
        Node = self.head
        if self.__ascending is True:
            if self.compare(value, Node) == -1:         # Сравнение с первым элементом,замена head
                self.head = value
                Node.prev = value
                value.next = Node
                return
        elif self.__ascending is False:
            if self.compare(value, Node) == 1:         # Сравнение с первым элементом,замена head
                self.head = value
                Node.prev = value
                value.next = Node
                return
        elif value.value == Node.value:              # Добавление повторяющихся элементов
            x = Node.next
            Node.next = value
            value.next = x
            value.prev = Node
            return
        while Node is not None:
            if self.__ascending is True:
                if self.compare(value, Node) == -1:     # Добавление элемента между тем который меньше и тем, который больше
                    x = Node.prev
                    Node.prev = value
                    value.prev = x
                    value.next = Node
                    value.prev.next = value
                    return
            elif self.__ascending is False:
                if self.compare(value, Node) == 1:     # Добавление элемента между тем который меньше и тем, который больше
                    x = Node.prev
                    Node.prev = value
                    value.prev = x
                    value.next = Node
                    value.prev.next = value
                    return
            if Node.next is None:                 # Добавление элемента в конец, замена tail
                self.tail = value
                Node.next = value
                value.prev = Node
                return
            Node = Node.next
        pass

    def find(self, val):
        Node = self.head
        while Node is not None:
            if Node.value == val:
                return Node
            elif self.__ascending is True and Node.value > val:
                return None
            elif self.__ascending is False and Node.value < val:
                return None
            Node = Node.next
        return None

    def delete(self, val):
        Node = self.find(val)
        if Node is None:
            pass
        elif Node.value == val:
            if Node.prev is not None:
                Node = Node.prev
                Node.next = Node.next.next
            else:
                self.head = Node.next
            if Node.next is not None:
                Node = Node.next
                Node.prev = Node.prev.prev
            else:
                self.tail = Node
        pass

    def clean(self):
        self.head = None
        self.tail = None
        pass

    def len(self):
        l = 0
        Node = self.head
        while Node is not None:
            l += 1
            Node = Node.next
        return l

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        x = str(v2.value)
        x = ''.join(x.split())
        y = str(v1.value)
        y = ''.join(y.split())
        if y < x:
            return -1
        elif x == y:
            return 0
        else:
            return 1


