import unittest
import random


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
                s.append(node.value)
            node = node.next
        return s

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node == self.head and node.value == val:
                self.head = self.head.next
                if all is False:
                    break
            elif node.next == self.tail and node.next.value == val:
                self.tail = node
                self.tail.next = None
                break
            elif node.next is not None and node.next.value == val:
                node.next = node.next.next
                if all is False:
                    break
            if node.next is None:
                break
            elif node.next.value != val:
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
            if node.value == afterNode:
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


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s_list3 = LinkedList()
        self.s_list = LinkedList()
        self.s_list.add_in_tail(Node(1))
        self.s_list.add_in_tail(Node(2))
        self.s_list.add_in_tail(Node(2))
        self.s_list.add_in_tail(Node(2))
        self.s_list.add_in_tail(Node(3))
        self.s_list2 = LinkedList()
        self.s_list2.add_in_tail(Node(1))
        self.s_list2.add_in_tail(Node(2))
        self.s_list2.add_in_tail(Node(2))
        self.s_list2.add_in_tail(Node(2))
        self.s_list2.add_in_tail(Node(3))

    def test_delete(self):
        self.initialize()
        self.s_list2.delete(3)
        node = self.s_list2.head
        while node is not None:
            self.assertNotEqual(3, node.value)
            node = node.next
        self.s_list2 = None

    def test_del_all(self):
        self.initialize()
        self.s_list2.delete(2, True)
        node = self.s_list2.head
        while node is not None:
            self.assertNotEqual(2, node.value)
            node = node.next
        self.s_list2 = None

    def test_poisk(self):
        self.initialize()
        s = self.s_list2.findall(1)
        self.assertTrue((len(s) == 1) and s[0] == 1)
        self.s_list2 = None

    def test_len(self):
        self.initialize()
        self.assertTrue(self.s_list2.len() == 5)
        self.s_list2 = None

    def test_insert(self):
        self.initialize()
        self.s_list2.insert(3, Node(5))
        self.assertTrue(self.s_list2.tail.value == 5)
        self.s_list2 = None

    def test_sumslist(self):
        self.initialize()
        self.slist3 = sum_slists(self.s_list, self.s_list2, self.s_list3)
        self.assertTrue(self.slist3.tail.value == 6)
        self.s_list2 = None
        self.s_list3 = None
        self.s_list = None


if __name__ == '__main__':
    unittest.main()