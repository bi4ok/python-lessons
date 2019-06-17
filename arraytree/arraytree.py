class Node:
    def __init__(self, val):
        self.value = val
        self.parent = None
        self.r = None
        self.l = None
        self.level = 0


class ArrayTree:

    def __init__(self, sz):
        self.root = None
        self.size = sz-1
        self.massiv = [None]*self.size

    def add_branch(self, val):
        if self.root is None:
            self.root = val
            self.massiv.insert(0, self.root)
        y = self.poisk(self.root, val)
        if y is None:
            return None
        elif y > 0:
            return self.massiv[y]
        elif y < 0:
            self.massiv[-y] = val
            node = val
            node.parent = self.massiv[(-y-1)//2]
            node = node.parent
            if node.value > val.value:
                node.l = val
            if node.value < val.value:
                node.r = val

    def poisk(self, x, val):
        node = x
        if node is not None and node.value == val.value:
            return self.massiv.index(node)
        else:
            if val.value > node.value:
                if node.r is None and (2*(self.massiv.index(node))+2) <= self.size:
                    return -(2*(self.massiv.index(node))+2)
                elif (2*(self.massiv.index(node))+2) > self.size:
                    return None
                x = self.poisk(node.r, val)
                return x
            elif val.value < node.value:
                if node.l is None and (2*(self.massiv.index(node))+1) <= self.size:
                    return -(2*(self.massiv.index(node))+1)
                elif (2*(self.massiv.index(node))+1) > self.size:
                    return None
                x = self.poisk(node.l, val)
                return x
            else:
                return None


