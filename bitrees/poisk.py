import unittest


class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.r = None
        self.l = None
        self.level = 0


class BiTree:

    def __init__(self, item):
        self.root = item

    def add_branch(self, val):
        y = self.poisk(self.root, val)
        while y[1] is True:                                 # Цикл для нахождения места среди одинаковых элементов
            if y[0].r is not None:
                y = self.poisk(y[0].r, val)
            else:
                y[2] = 1
                break
        node = y[0]
        if y[2] == 0:
            node.l = val
        elif y[2] == 1:
            node.r = val
        x = node
        node = val
        node.parent = x
        node.level = node.parent.level + 1

    def delete_leaf(self, val):
        y = self.poisk(self.root, val)
        node = y[0]
        if node.value == val.value:
            if node.l is None and node.r is None:
                x = node
                node = node.parent
                if node.l == x:
                    node.l = None
                elif node.r == x:
                    node.r = None
            elif node.l is not None and node.r is None:
                x = node
                node = node.parent
                if node.l == x:
                    node.l = node.l.l
                elif node.r == x:
                    node.r = node.r.l
            elif node.r is not None and node.l is None:
                x = node
                node = node.parent
                if node.l == x:
                    node.l = node.l.r
                elif node.r == x:
                    node.r = node.r.r
            elif node.r is not None and node.l is not None:
                x = node
                zamena = self.minmax(node.r, "min")
                node = zamena.parent
                if node.l == zamena:
                    node.l = None
                elif node.r == zamena:
                    node.r = None
                if x is not self.root:
                    node = x.parent
                    if node.l == x:
                        node.l = zamena
                    elif node.r == x:
                        node.r = zamena
                else:
                    self.root = zamena
                zamena.l = x.l
                zamena.r = x.r

    def poisk(self, x, val):
        spisok = []
        node = x
        if node is not None and node.value == val.value:
            spisok.append(node)
            spisok.append(True)
            spisok.append(None)
            return spisok
        else:
            if val.value > node.value and node.r is not None:
                x = self.poisk(node.r, val)
                return x
            elif val.value < node.value and node.l is not None:
                x = self.poisk(node.l, val)
                return x
            else:
                spisok.append(node)
                spisok.append(False)
                if val.value >= node.value:
                    spisok.append(1)
                else:
                    spisok.append(0)
                return spisok

    def poisk2(self, l=0, spisok=[]):
        if l == 0:
            spisok = [self.root]
            itog.append(self.root.value)
        s4et = l
        for i in spisok[s4et:]:
            if i.l is not None:
                spisok.append(i.l)
                itog.append(i.l.value)
            if i.r is not None:
                itog.append(i.r.value)
                spisok.append(i.r)
            s4et += 1
        if s4et != len(spisok):
            self.poisk2(l=s4et, spisok=spisok)
        return spisok

    def minmax(self, ot, val):
        y = self.poisk(self.root, ot)
        x = None
        node = y[0]
        if str(val) == "max":
            while node.r is not None:
                node = node.r
            x = node
        elif str(val) == "min":
            while node.l is not None:
                node = node.l
            x = node
        return x


s1 = BiTree(Node(100))
s1.add_branch(Node(150))
s1.add_branch(Node(200))
s1.add_branch(Node(90))
s1.add_branch(Node(50))
s1.add_branch(Node(40))
s1.add_branch(Node(60))
s1.add_branch(Node(110))
s1.add_branch(Node(120))
print(s1.poisk2())