class BSTNode:

    def __init__(self, key, parent):
        self.NodeKey = key  # ключ узла
        self.Parent = parent  # родитель или None для корня
        self.LeftChild = None  # левый потомок
        self.RightChild = None  # правый потомок
        self.Level = 0  # уровень узла


class BalancedBST:

    def __init__(self):
        self.Root = None
        self.BSTArray = []  # временный массив для ключей дерева

    def CreateFromArray(self, a):
        self.BSTArray = [None] * 3
        a = sorted(a)
        u = 1

        def balansirovka(a, bm, x):
            if not a:
                return None
            if x >= len(bm):
                nonlocal u
                u += 1
                l1 = 2 ** (u + 1) - 1
                bm += ([None] * (l1 - len(bm)))
            centr = int(len(a)/2)
            bm[x] = a[centr]
            balansirovka(a[:centr], bm, x * 2 + 1)
            balansirovka(a[centr+1:], bm, x * 2 + 2)
            return bm

        self.BSTArray = balansirovka(a, self.BSTArray, 0)

    def GenerateTree(self):
        def make_leafs(massiv, index, parent):
            root = BSTNode(massiv[index], parent)
            if root.Parent:
                root.Level = root.Parent.Level + 1
            else:
                root.Level = 1
            if 2 * index + 1 < len(massiv) and massiv[2 * index + 1]:
                root.LeftChild = make_leafs(massiv, 2 * index + 1, root)
            if 2 * index + 2 < len(massiv) and massiv[2 * index + 2]:
                root.RightChild = make_leafs(massiv, 2 * index + 2, root)
            return root
        self.Root = make_leafs(self.BSTArray, 0, None)

    def IsBalanced(self, root_node):
        if root_node is None:
            return True

        def glubina(root):
            if root is None:
                return 0
            return max(glubina(root.LeftChild), glubina(root.RightChild)) + 1
        left_pd = glubina(root_node.LeftChild)
        right_pd = glubina(root_node.RightChild)
        if abs(left_pd - right_pd) <= 1 and self.IsBalanced(root_node.LeftChild) is True \
                and self.IsBalanced(root_node.RightChild) is True:
            return True
        return False
