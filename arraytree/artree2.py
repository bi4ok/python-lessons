class aBST:

    def __init__(self, depth):
        tree_size = 2 ** (depth + 1) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        i = 0
        while self.Tree[i] != key:
            if self.Tree[i] is None:
                return -i
            elif key > self.Tree[i]:
                i = i * 2 + 2
            elif key < self.Tree[i]:
                i = i * 2 + 1
            if i >= len(self.Tree):
                return None
        return i

    def AddKey(self, key):
        i = self.FindKeyIndex(key)
        if i is None:
            return -1
        elif i < 0:
            self.Tree[-i] = key
            return -i
        elif i > 0:
            return i
        elif i == 0:
            if self.Tree[0] is None:
                self.Tree[0] = key
            return i
