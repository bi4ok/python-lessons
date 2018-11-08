import arraytree
import random
import timeit
import unittest


def masiv(spisok, sz):
    mtree = [None]*sz
    l = len(spisok)//2
    mtree[0] = spisok.pop(l)
    spisok1 = spisok[0:l]
    spisok2 = spisok[l:len(spisok)]
    mtree.insert(2 * (mtree.index(mtree[0])) + 1, spisok1.pop(l // 2))
    mtree.insert(2 * (mtree.index(mtree[0])) + 2, spisok2.pop(l // 2))
    node = mtree[0]
    node.l = mtree[2 * (mtree.index(mtree[0])) + 1]
    node.l.level = node.level + 1
    node.r = mtree[2 * (mtree.index(mtree[0])) + 2]
    node.r.level = node.level + 1
    povtor(spisok1, mtree, node.l)
    povtor(spisok2, mtree, node.r)
    return mtree


def povtor(spisok, mtree, parent):
    l = (len(spisok) // 2)
    x1, x2 = None, None

    if len(spisok) == 1:                                            # Обработка последнего элемента в списке
        spisok1, spisok2 = [], []
        if spisok[0].value < parent.value:
            x1 = spisok[0]
        elif spisok[0].value > parent.value:
            x2 = spisok[0]

    else:                                                           # Если элементов больше 1, список делится на 2
        spisok1 = spisok[0:l]                                       # Из первого списка выбирается элемент
        if len(spisok1) > 0:                                        # для добавления в левую часть
            if spisok1[l//2].value < parent.value:                  # Из второго - в правую
                x1 = spisok1.pop(l//2)
        else:
            x1 = None

        spisok2 = spisok[l:len(spisok)]
        if len(spisok2) > 0:
            if spisok2[l//2].value > parent.value:
                x2 = spisok2.pop(l//2)
        else:
            x2 = None

    if mtree[2 * (mtree.index(parent)) + 1] is None and x1 is not None:     # Проверка свободно ли место
        mtree[2 * (mtree.index(parent)) + 1] = x1                           # И выбран ли x1
        parent.l = mtree[2 * (mtree.index(parent)) + 1]
        parent.l.level = parent.level + 1
        spisok.remove(x1)

        if len(spisok1) > 0:
            povtor(spisok1, mtree, parent.l)                                # Рекурсия с потомком,если в списке есть эл.

    elif x1 is None and len(spisok1) > 0:
        povtor(spisok1, mtree, parent)                                      # Рекурсия с неиспользованным списком

    elif mtree[2 * (mtree.index(parent)) + 1] is not None and x1 is not None:
        spisok1.insert(len(spisok1) // 2, x1)
        povtor(spisok1, mtree, mtree[2 * (mtree.index(parent)) + 1])        # Рекурсия при занятом месте

    if mtree[2 * (mtree.index(parent)) + 2] is None and x2 is not None:
        mtree[2 * (mtree.index(parent)) + 2] = x2
        parent.r = mtree[2 * (mtree.index(parent)) + 2]
        parent.r.level = parent.level + 1
        spisok.remove(x2)

        if len(spisok2) > 0:
            povtor(spisok2, mtree, parent.r)

    elif x2 is None and len(spisok2) > 0:
        povtor(spisok2, mtree, parent)

    elif mtree[2 * (mtree.index(parent)) + 2] is not None and x2 is not None:
        spisok2.insert(len(spisok2)//2, x2)
        povtor(spisok2, mtree, mtree[2 * (mtree.index(parent)) + 2])

    return None


s1 = []
for j in range(10):
    s1.append(j)

s1 = sorted(s1)
s2 = []

for k in range(10):
    s2.append(arraytree.Node(s1[k]))

levels = 15
size = (2**(levels + 1)) - 1

s = masiv(s2, size)
print("_____")
z = 0
#for m in range(len(s)):
 #   if s[m] is not None:
  #      print(s[m].value, m, s[m].level)
   #     z += 1
#print(z)


def mastobst(mas):
    if not mas:
        return
    root = mas
    root.l = mastobst(mas.l)
    root.r = mastobst(mas.r)
    return root


def printallfast(tree):
    if not tree:
        return
    print(tree.value, tree.level)
    printallfast(tree.l)
    printallfast(tree.r)


s1 = []
for j in range(20):
    s1.append(random.randint(0, 25))


def fasttree(s1):
    s1 = sorted(s1)
    s2 = []
    for k in range(20):
        s2.append(arraytree.Node(s1[k]))
    levels = 10
    size = (2 ** (levels + 1)) - 1
    s = masiv(s2, size)
    sd = mastobst(s[0])
    return sd


def slowtree(s1):
    tree = arraytree.ArrayTree(size)
    for i in range(len(s1)):
        tree.add_branch(arraytree.Node(s1[i]))
    return tree


def glubina(root):
    if root is None:
        return 0
    return max(glubina(root.l), glubina(root.r)) + 1


def balans(root):
    if root is None:
        return True
    lh = glubina(root.l)
    rh = glubina(root.r)
    if root.l is not None:
        print(root.l.value, "|||", lh, "l")
    if root.r is not None:
        print(root.r.value, "|||", rh, "r")
    if (abs(lh - rh) <= 1) and balans(root.l) is True and balans(root.r) is True:
        return True
    return False


print(timeit.Timer(lambda: fasttree(s1)).timeit(number=100))
print(timeit.Timer(lambda: slowtree(s1)).timeit(number=100))
print("___________________________________________________")


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.st1 = []
        for i in range(10):
            self.st1.append(i)
        self.st2 = []
        for j in range(10):
            self.st2.append(arraytree.Node(self.st1[j]))
        levels = 3
        size = (2 ** (levels + 1)) - 1
        self.st3 = masiv(self.st2, size)
        self.st4 = mastobst(self.st3[0])

    def proverka(self, root):
        if not root:
            return
        if root.l is not None and root.value > root.l.value:
            self.assertTrue(root.value > root.l.value)
            self.assertTrue(root.l.level - root.level == 1)
            self.proverka(root.l)
        if root.r is not None and root.value < root.r.value:
            self.assertTrue(root.value < root.r.value)
            self.assertTrue(root.r.level - root.level == 1)
            self.proverka(root.r)

    def testdrevo(self):
        self.initialize()
        self.proverka(self.st4)
        self.assertTrue(balans(self.st4))


if __name__ == '__main__':
    unittest.main()