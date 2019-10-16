class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, val):
        index = 0
        val = str(val)
        for i in range(len(val)):
            if int(val[i]) != 0:
                index += int(val[i]) * (i+1)
            elif int(val) == 0:
                index = 0
                return index
            else:
                index += (11 * (i + 1))
        if self.size != 0:
            index = index % self.size
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
                while index > X:
                    if X == 0:
                        index -= 1
                    index -= X
                if self.slots[index] is None:
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


s1 = HashTable(17, 3)
for i in range(100):
    s1.put(i)

print(s1.put(12), s1.slots, s1.size, len(s1.slots))