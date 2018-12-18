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
        value = Node(value)
        if self.head is None:           # Добавление первого элемента, обозначение головы и хвоста
            self.head = value
            self.tail = value
            value.prev = None
            value.next = None
            return
        node = self.head
        if self.__ascending is True:
            if self.compare(value, node) == -1:         # Сравнение с первым элементом,замена head
                self.head = value
                node.prev = value
                value.next = node
                return
        elif self.__ascending is False:
            if self.compare(value, node) == 1:         # Сравнение с первым элементом,замена head
                self.head = value
                node.prev = value
                value.next = node
                return
        elif value.value == node.value:              # Добавление повторяющихся элементов
            x = node.next
            node.next = value
            value.next = x
            value.prev = node
            return
        while node is not None:
            if self.__ascending is True:
                if self.compare(value, node) == -1:     # Добавление элемента между тем который меньше и тем, который больше
                    x = node.prev
                    node.prev = value
                    value.prev = x
                    value.next = node
                    value.prev.next = value
                    return
            elif self.__ascending is False:
                if self.compare(value, node) == 1:     # Добавление элемента между тем который меньше и тем, который больше
                    x = node.prev
                    node.prev = value
                    value.prev = x
                    value.next = node
                    value.prev.next = value
                    return
            if node.next is None:                 # Добавление элемента в конец, замена tail
                self.tail = value
                node.next = value
                value.prev = node
                return
            node = node.next
        pass

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            elif self.__ascending is True and node.value > val:
                return None
            elif self.__ascending is False and node.value < val:
                return None
            node = node.next
        return None

    def delete(self, val):
        node = self.find(val)
        if node is None:
            pass
        elif node.value == val:
            if node.prev is not None:
                node = node.prev
                node.next = node.next.next
            else:
                self.head = node.next
            if node.next is not None:
                node = node.next
                node.prev = node.prev.prev
            else:
                self.tail = node
        pass

    def clean(self):
        self.head = None
        self.tail = None
        pass

    def len(self):
        l = 0
        node = self.head
        while node is not None:
            l += 1
            node = node.next
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