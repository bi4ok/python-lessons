class PowerSet:
    def __init__(self, sz, stp):
        self.sizeps = sz
        self.step = stp
        self.slots = [None]*self.sizeps

    def hash_fun(self, value1):
        index = 0
        if self.slots[0] is None:
            return index
        value = str(value1)
        for i in range(len(value)):
            if int(value[i]) != 0:
                index += int(value[i]) * (i+1)
            else:
                index += (11 * (i + 1))
        index = index % self.sizeps
        return index

    def seek_slot(self, value):
        index = self.hash_fun(value)
        for i in range(self.sizeps - 1):
            if self.slots[index] == value:
                return None
            elif self.slots[index] is None:
                return index
            else:
                if index + self.step <= (self.sizeps - 1):
                    index += self.step
                    if self.slots[index] == value:
                        return None
                    elif self.slots[index] is None:
                        return index
                elif index + self.step > self.sizeps-1:
                    index = 0 + (index + self.step - self.sizeps)
                    if self.slots[index] == value:
                        return None
                    elif self.slots[index] is None:
                        return index
        return None

    def size(self):
        x = 0
        for i in range(self.sizeps):
            if self.slots[i] is not None:
                x += 1
        return x

    def put(self, value):
        x = self.seek_slot(value)
        if x is not None:
            self.slots[x] = value

    def get(self, value):
        index = self.hash_fun(value)
        for i in range(self.sizeps - 1):
            if self.slots[index] == value:
                return True
            else:
                if index + self.step <= (self.sizeps - 1):
                    index += self.step
                    if self.slots[index] == value:
                        return True
                elif index + self.step > self.sizeps - 1:
                    index = 0 + (index + self.step - self.sizeps)
                    if self.slots[index] == value:
                        return True
        return False

    def remove(self, value):
        index = self.hash_fun(value)
        for i in range(self.sizeps - 1):
            if self.slots[index] == value:
                self.slots[index] = None
                return True
            else:
                if index + self.step <= (self.sizeps - 1):
                    index += self.step
                    if self.slots[index] == value:
                        self.slots[index] = None
                        return True
                elif index + self.step > self.sizeps - 1:
                    index = 0 + (index + self.step - self.sizeps)
                    if self.slots[index] == value:
                        self.slots[index] = None
                        return True
        return False

    def intersection(self, set1):
        if self.size() < set1.size():
            set2 = PowerSet(self.sizeps, 5)
            for i in range(self.sizeps):
                if self.slots[i] is not None and set1.get(self.slots[i]) is True:
                    set2.put(self.slots[i])
        else:
            set2 = PowerSet(set1.sizeps, 5)
            for i in range(set1.sizeps):
                if set1.slots[i] is not None and self.get(set1.slots[i]) is True:
                    set2.put(set1.slots[i])
        return set2

    def union(self, set1):
        set2 = PowerSet(self.sizeps+set1.sizeps, 5)
        for i in range(self.sizeps):
            if self.slots[i] is not None:
                set2.put(self.slots[i])
        for j in range(set1.sizeps):
            if set1.slots[j] is not None:
                set2.put(set1.slots[j])
        return set2

    def difference(self, set1):
        set2 = PowerSet(self.sizeps, 5)
        for i in range(self.sizeps):
            if self.slots[i] is not None and self.slots[i] != set1.slots[i]:
                set2.put(self.slots[i])
        return set2

    def issubset(self, set1):
        for i in set1.slots:
            if i is not None:
                if set1.get(i) is False and self.get(i) is True:
                    print(i)
                    return False
        return True