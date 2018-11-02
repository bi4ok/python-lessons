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
        node = self.root
        z = 0
        while node.value != val.value:
            if node.leafs[z] is not None:
                node = node.leafs[z]
                z = 0
            elif node.leafs[z] is None:
                if node.parent is not None:
                    z = node.parent.leafs.index(node) + 1
                    node = node.parent
                else:
                    break
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
        node = self.root
        z = 0
        while node.value != val.value:
            if node.leafs[z] is not None:
                node = node.leafs[z]
                z = 0
            elif node.leafs[z] is None:
                if node.parent is not None:
                    z = node.parent.leafs.index(node) + 1
                    node = node.parent
                else:
                    break
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
        node = self.root
        z = 0
        while node.value != val.value:
            if node.leafs[z] is not None:
                node = node.leafs[z]
                z = 0
            elif node.leafs[z] is None:
                if node.parent is not None:
                    z = node.parent.leafs.index(node) + 1
                    node = node.parent
                else:
                    break
        if node.value == val.value:
            x = node
            node = node.parent
            node.leafs.remove(x)

        else:
            return None
        node = self.root
        z = 0
        while node.value != item.value:
            if node.leafs[z] is not None:
                node = node.leafs[z]
                z = 0
            elif node.leafs[z] is None:
                if node.parent is not None:
                    z = node.parent.leafs.index(node) + 1
                    node = node.parent
                else:
                    break
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

    def poisk(self, x, val, z=0):
        node = x
        node.flag = 1
        if node.value == val.value:
            return node
        elif len(node.leafs) <= z:
            z = 0
            return self.poisk(x, val, z)
        elif node.leafs[z] is not None and node.leafs[z].flag == 0:
            return self.poisk(x.leafs[z], val, z)
        elif node.leafs[z] is None:
            z = 0
            return self.poisk(x.parent, val, z)
        elif node.leafs[z].flag == 1:
            z += 1
            return self.poisk(x, val, z)


s1 = SimpleTree()
s1.root = Node(0)
s1.add_branch(Node(0), Node(1))
s1.add_branch(Node(0), Node(2))
s1.add_branch(Node(1), Node(3))
s1.add_branch(Node(1), Node(4))
s1.add_branch(Node(2), Node(5))
s1.add_branch(Node(2), Node(6))
print(s1.poisk(s1.root, Node(6)).value)
