import arraytree
import random


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
    if len(spisok) == 1:
        spisok1, spisok2 = [], []
        if spisok[0].value < parent.value:
            x1 = spisok[0]
        elif spisok[0].value > parent.value:
            x2 = spisok[0]
    else:
        spisok1 = spisok[0:l]
        if len(spisok1) > 0:
            if spisok1[l//2] is not None and parent is not None:
                if spisok1[l//2].value < parent.value:
                    x1 = spisok1.pop(l//2)
        else:
            x1 = None

        spisok2 = spisok[l:len(spisok)]
        if len(spisok2) > 0:
            if spisok2[l//2] is not None and parent is not None:
                if spisok2[l//2].value > parent.value:
                    x2 = spisok2.pop(l//2)
                else:
                    x2 = None
        else:
            x2 = None

    if mtree[2 * (mtree.index(parent)) + 1] is None and x1 is not None:
        mtree[2 * (mtree.index(parent)) + 1] = x1
        parent.l = mtree[2 * (mtree.index(parent)) + 1]
        parent.l.level = parent.level + 1
        spisok.remove(x1)
        if len(spisok1) > 0:
            povtor(spisok1, mtree, parent.l)
    elif x1 is None and len(spisok1) > 0:
        povtor(spisok1, mtree, parent)
    elif mtree[2 * (mtree.index(parent)) + 1] is not None and x1 is not None:
        spisok1.insert(len(spisok1) // 2, x1)
        povtor(spisok1, mtree, mtree[2 * (mtree.index(parent)) + 1])

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


def vderevo(items):

    tree = arraytree.ArrayTree(10000)            # Добавление корневого элемента
    tree.add_branch(items.pop(len(items)//2))

    ostatok = 0                                         # Список становится четным перед делением на 2 части
    l = None                                            # Лишний элемент, при наличии, сохраняется
    if len(items) % 2 == 0:
        l = len(items)//2
    elif len(items) % 2 == 1:
        ostatok = items.pop()
        l = len(items)//2

    items1 = items[0:l]                                 # Список делится на 2 части
    items2 = items[l:]

    for i in range(l):                                  # Каждый элемент каждой части из середины добавляется в дерево
        tree.add_branch(items1[len(items1)//2])         # Проверяется размер, доподлняется новыми ячейчками,если нужно
        razmer(tree, items1[len(items1)//2])            # Элемент удаляется из списка
        items1.pop(len(items1)//2)
    for i in range(l):
        tree.add_branch(items2[len(items2)//2])
        razmer(tree, items2[len(items2) // 2])
        items2.pop(len(items2)//2)

    if ostatok != 0:                                    # Остаток, при наличии, добавляется в дерево
        tree.add_branch(ostatok)
    return tree


def razmer(tree, item):
    if tree.poisk(tree.root, item) is None:
        return None
    x = tree.massiv[tree.poisk(tree.root, item)]
    if x is not None and tree.size < ((2 ** (x.level + 1)) - 1):
        l1 = ((2 ** (x.level + 1)) - 1) - tree.size
        for j in range(l1):
            tree.massiv.append(None)
        tree.size = ((2 ** (x.level + 1)) - 1)
    print(x.level)
    return tree


s1 = []
for j in range(100):
    s1.append(random.randint(0, 100))

s1 = sorted(s1)
s2 = []

for k in range(100):
    s2.append(arraytree.Node(s1[k]))

levels = 7
size = (2**(levels + 1)) - 1

s = masiv(s2, size)
print("_____")
z = 0
for m in range(len(s)):
    if s[m] is not None:
        print(s[m].value, m, s[m].level)
        z += 1
print(z)