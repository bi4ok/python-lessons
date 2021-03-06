class BSTNode:
    def __init__(self, key, val, parent):
        self.NodeKey = key
        self.NodeValue = val
        self.Parent = parent
        self.LeftChild = None
        self.RightChild = None


class BSTFind:
    def __init__(self):
        self.Node = None
        self.NodeHasKey = False
        self.ToLeft = False


class BST:
    def __init__(self, node):
        self.Root = node

    def FindNodeByKey(self, key):
        node = BSTFind()
        node.Node = self.Root
        while node.Node.NodeKey != key:
            if key > node.Node.NodeKey:
                if node.Node.RightChild is None:
                    break
                node.Node = node.Node.RightChild
            else:
                if node.Node.LeftChild is None:
                    node.ToLeft = True
                    break
                node.Node = node.Node.LeftChild
        else:
            node.NodeHasKey = True
        return node

    def AddKeyValue(self, key, val):
        node = self.FindNodeByKey(key)
        innode = BSTNode(key, val, None)
        if node.NodeHasKey is False:
            if node.ToLeft is False:
                node.Node.RightChild = innode
            else:
                node.Node.LeftChild = innode
            innode.Parent = node.Node
            return True
        else:
            return False

    def FinMinMax(self, FromNode, FindMax):
        node = FromNode
        if FindMax is True:
            while node.RightChild is not None:
                node = node.RightChild
        else:
            while node.LeftChild is not None:
                node = node.LeftChild
        return node

    def DeleteNodeByKey(self, key):
        node = self.FindNodeByKey(key)
        if node.NodeHasKey is True:
            if node.Node.RightChild is not None and node.Node.LeftChild is not None:
                zamena = self.FinMinMax(node.Node.RightChild, False)
                if zamena.RightChild is not None:
                    zamena = zamena.RightChild
                    zamena.Parent.RightChild = None
                else:
                    zamena.Parent.LeftChild = None
            else:
                if node.Node.RightChild is not None:
                    zamena = node.Node.RightChild
                    node.Node.RightChild = zamena.RightChild
                    node.Node.LeftChild = zamena.LeftChild
                elif node.Node.LeftChild is not None:
                    zamena = node.Node.LeftChild
                    node.Node.RightChild = zamena.RightChild
                    node.Node.LeftChild = zamena.LeftChild
                else:
                    zamena = node.Node
                    if zamena.Parent.RightChild == zamena:
                        zamena.Parent.RightChild = None
                    else:
                        zamena.Parent.LeftChild = None
            zamena.Parent = None
            node.Node.NodeKey = zamena.NodeKey
            node.Node.NodeValue = zamena.NodeValue
            return True
        else:
            return False

    def Count(self):
        node = self.Root
        len = [None, self.Root]
        while node is not None:
            if node.LeftChild not in len and node.LeftChild is not None:
                node = node.LeftChild
            elif node.RightChild not in len and node.RightChild is not None:
                node = node.RightChild
            if node not in len:
                len.append(node)
            if node.LeftChild is None and node.RightChild is None:
                node = node.Parent
            elif node.LeftChild in len and node.RightChild in len:
                node = node.Parent
        z = 0
        for i in len:
            if i is not None:
                    z += 1
        return z

    def WideAllNodes(self):
        def shirina(l, spisok):
            if l == 0:
                spisok = [self.Root]
            s4et = l
            for i in spisok[s4et:]:
                if i.LeftChild is not None:
                    spisok.append(i.LeftChild)
                if i.RightChild is not None:
                    spisok.append(i.RightChild)
                s4et += 1
            if s4et != len(spisok):
                shirina(l=s4et, spisok=spisok)
            return spisok
        return shirina(0, [])

    def DeepAllNodes(self, order):
        def glubina(order, node, spisok):
            if node == 0:
                node = self.Root

            def levo():
                if node.LeftChild is not None:
                    glubina(order, node.LeftChild, spisok)

            def centr():
                if node not in spisok:
                    spisok.append(node)

            def pravo():
                if node.RightChild is not None:
                    glubina(order, node.RightChild, spisok)

            deistviya = [levo, centr, pravo]
            if order == 0:
                for i in deistviya:
                    i()
            elif order == 1:
                deistviya[0]()
                deistviya[2]()
                deistviya[1]()
            elif order == 2:
                deistviya[1]()
                deistviya[0]()
                deistviya[2]()
            rs = spisok
            spisok = []
            return rs
        spisok = []
        return glubina(order, self.Root, spisok)
