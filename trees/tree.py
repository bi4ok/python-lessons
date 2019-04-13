class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val
        self.Parent = parent
        self.Children = []


class SimpleTree:

    def __init__(self, root):
        self.Root = root

    def AddChild(self, ParentNode, NewChild):
        ParentNode.Children.append(NewChild)
        NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        node = NodeToDelete
        if node is not self.Root:
            node.Parent.Children.remove(node)
            node.Parent = None

    def GetAllNodes(self):
        z = 0
        node = self.Root
        spisok = []
        while True:
            if node not in spisok:
                spisok.append(node)
            if z < len(node.Children):
                node = node.Children[z]
                z = 0
            else:
                if node.Parent is not None:
                    z = node.Parent.Children.index(node) + 1
                    node = node.Parent
                else:
                    break
        return spisok

    def FindNodesByValue(self, val):
        z = 0
        node = self.Root
        spisok = []
        while node.NodeValue is not None:
            if node not in spisok and node.NodeValue == val:
                spisok.append(node)
            if z < len(node.Children):
                node = node.Children[z]
                z = 0
            else:
                if node.Parent is not None:
                    z = node.Parent.Children.index(node) + 1
                    node = node.Parent
                else:
                    break
        return spisok

    def MoveNode(self, OriginalNode, NewParent):
        if OriginalNode is not self.Root:
            self.DeleteNode(OriginalNode)
            self.AddChild(NewParent, OriginalNode)

    def Count(self):
        z = 0
        for i in self.GetAllNodes():
            if len(i.Children) > 0:
                z += 1
        return z

    def LeafCount(self):
        z = 0
        for i in self.GetAllNodes():
            if len(i.Children) == 0:
                z += 1
        return z
