class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None]*self.size

    def hash_fun(self, val):
        index = 0
        if self.slots[index] is None:
            return index
        val = str(val)
        for i in range(len(val)):
            if int(val[i]) != 0:
                index += int(val[i]) * (i+1)
            else:
                index += (11 * (i + 1))
        index = index % self.size
        return index

    def seek_slot(self, value):
        index = self.hash_fun(value)
        for i in range(self.size - 1):
            if self.slots[index] is None:
                return index
            else:
                index += self.step
                while index > self.size - 1:
                    index -= (self.size - 1)
                if self.slots[index] == value:
                    return index
        return None

    def put(self, value):
        x = self.seek_slot(value)
        if x is not None:
            self.slots[x] = value
            return x
        else:
            print("_______________________________________________________")
            return None

    def find(self, value):
        index = self.hash_fun(value)
        for i in range(self.size - 1):
            if self.slots[index] == value:
                return index
            else:
                if index + self.step <= (self.size - 1):
                    index += self.step
                    if self.slots[index] == value:
                        return index
                else:
                    x = self.step
                    while x > (self.size - 1):
                        x -= (self.size - 1)
                    index = 0 + (index + x - self.size)
                    if self.slots[index] == value:
                        return index
        return None
