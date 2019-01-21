from pymonad import curry
import random


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.kol = 0

        @curry
        def add(x, y):
            return x + y

        @curry
        def mul(x, y):
            return x * y

        @curry
        def mod(x, y):
            return y % x

        self.funclist = [[add(sz // stp), add(sz // 2), add(0)],
                         [mul(1), mul(11), mul(7)],
                         [mod(sz), mod(sz*2), mod(sz+stp)],
                         [mod(sz), mod(sz), mod(sz)]]
        self.select = [2, 2, 0, 0, ]

    def hash_fun(self, val):
        index = int(val)
        for i in range(4):
            index = self.funclist[i][self.select[i]](index)
        return index

    def seek_slot(self, value):
        X = self.size - 1
        index = self.hash_fun(value)
        if X == 0:
            if self.slots[index] is None:
                return index
        for i in range(self.size):
            if self.slots[index] is None:
                return index
            else:
                index += self.step
                self.kol += 1
                while index > X:
                    if X == 0:
                        index -= 1
                    index -= X
                if self.slots[index] is None:
                    return index
        if self.slots[0] is None:
            index = 0
            return index
        return None

    def put(self, value):
        x = self.seek_slot(value)
        if x is not None:
            self.slots[x] = value
            return x
        else:
            return None

    def find(self, value):
        X = self.size - 1
        index = self.hash_fun(value)
        for i in range(self.size):
            if self.slots[index] == value:
                return index
            else:
                index += self.step
                while index > X:
                    index -= X
                if self.slots[index] == value:
                    return index
        return None


s1 = HashTable(1700, 30)
for i in range(1700):
    s1.put(random.randint(0,5000))
print(s1.kol)