class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        s = []
        node = self.head
        while node is not None:
            if node.value == val:
                s.append(node)
            node = node.next
        return s

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node == self.head and node.value == val:
                if self.head == self.tail:
                    self.tail = None
                self.head = node.next
                if all is False:
                    break
            elif node.next == self.tail and node.next.value == val:
                if self.tail == self.head:
                    self.head = None
                    self.tail = None
                self.tail = node
                self.tail.next = None
                break
            elif node.next is not None and node.next.value == val:
                node.next = node.next.next
                if all is False:
                    break

            if node.next is None:
                break
            elif node.next.value == val:
                if node.next == self.head:
                    node = node.next
            else:
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
        while node is not None:
            if node.value == afterNode.value:
                s = node.next
                node.next = newNode
                newNode.next = s
                if node == self.tail:
                    self.tail = newNode
                    self.tail.next = None
                break
            node = node.next


def sum_slists(slist1, slist2, slist3):
    if slist1.len() == slist2.len():
        node1 = slist1.head
        node2 = slist2.head
        while node1 is not None:
            slist3.add_in_tail(Node(node1.value + node2.value))
            node1 = node1.next
            node2 = node2.next
        return slist3
    else:
        return None
