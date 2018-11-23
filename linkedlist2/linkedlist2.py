class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def delete(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is not None:
                    node = node.prev
                    node.next = node.next.next
                else:
                    self.head = node.next
                if node.next is not None:
                    node = node.next
                    node.prev = node.prev.prev
                else:
                    if self.head is None:
                        node = None
                    self.tail = node
                break
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        l = 0
        node = self.head
        while node is not None:
            l += 1
            node = node.next
        return l

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode is None and self.head is None:
            self.add_in_tail(newNode)
        while node is not None:
            if node.value == afterNode.value:
                s = node.next
                node.next = newNode
                newNode.prev = node
                newNode.next = s
                if newNode.next is not None:
                    newNode.next.prev = newNode
                else:
                    self.tail = newNode
                break
            node = node.next

    def add_in_head(self, newNode):
        if self.head is not None:
            node = self.head
            node.prev = newNode
            newNode.next = node
            self.head = newNode
        else:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None
            newNode.next = None

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
