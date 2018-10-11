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

    def addonval(self, item):
        if self.head is None:
            self.head = item
            self.tail = item
            item.prev = None
            item.next = None
        Node = self.head
        if self.asc is True:
            if item.value < Node.value:
                self.head = item
                Node.prev = item
                item.next = Node
            elif item.value == Node.value:
                x = Node.next
                Node.next = item
                item.next = x
                item.prev = Node
            while Node is not None:
                if Node.value < item.value:
                    if Node.next is None:
                        self.tail = item
                        Node.next = item
                        item.prev = Node
                    elif Node.next.value >= item.value:
                        x = Node.next
                        Node.next = item
                        item.prev = Node
                        item.next = x
                        Node.next.next.prev = item
                Node = Node.next
        elif self.asc is False:
            if item.value > Node.value:
                self.head = item
                Node.prev = item
                item.next = Node
            elif item.value == Node.value:
                x = Node.next
                Node.next = item
                item.next = x
                item.prev = Node
            while Node is not None:
                if Node.value > item.value:
                    if Node.next is None:
                        self.tail = item
                        Node.next = item
                        item.prev = Node
                    elif Node.next.value <= item.value:
                        x = Node.next
                        Node.next = item
                        item.prev = Node
                        item.next = x
                        Node.next.next.prev = item
                Node = Node.next
        else:
            print('ascending is not defined')

    def searchonval(self, val):
        Node = self.head
        while Node != None:
            if Node.value == val:
                return Node
            Node = Node.next
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
s.ascending(False)
s.addonval(Node(1))
s.addonval(Node(1))
s.addonval(Node(3))
s.addonval(Node(2))
s.addonval(Node(4))
s.printall()
print(s.head.value, s.tail.value)
