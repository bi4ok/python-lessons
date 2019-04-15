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

    def FindNodesByKey(self, key):
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
        node = self.FindNodesByKey(key)
        innode = BSTNode(key, val, None)
        if node.NodeHasKey is False:
            if node.ToLeft is False:
                node.Node.RightChild = innode
            else:
                node.Node.LeftChild = innode
            innode.Parent = node.Node
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
        node = self.FindNodesByKey(key)
        if node.NodeHasKey is True:
            zamena = self.FinMinMax(node.Node.RightChild, False)
            if zamena.RightChild is not None:
                zamena = zamena.RightChild
                zamena.Parent.RightChild = None
            else:
                zamena.Parent.LeftChild = None
            zamena.Parent = None
            node.Node.NodeKey = zamena.NodeKey
            node.Node.NodeValue = zamena.NodeValue
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
                if i.LeftChild is not None or i.RightChild is not None:
                    z += 1
                elif i is self.Root:
                    z += 1
        return z
