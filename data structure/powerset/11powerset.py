class PowerSet:
    def __init__(self):
        self.slots = []

    def size(self):
        x = len(self.slots)
        return x

    def put(self, value):
        if value not in self.slots:
            self.slots.append(value)

    def get(self, value):
        if value in self.slots:
            return True
        return False

    def remove(self, value):
        if value in self.slots:
            self.slots.remove(value)
            return True
        return False

    def intersection(self, set2):
        inset = PowerSet()
        if self.size() > set2.size():
            for i in set2.slots:
                if self.get(i) is True:
                    inset.put(i)
        else:
            for i in self.slots:
                if set2.get(i) is True:
                    inset.put(i)
        return inset

    def union(self, set2):
        uset = PowerSet()
        for i in self.slots:
            uset.put(i)
        for j in set2.slots:
            uset.put(j)
        return uset

    def difference(self, set2):
        dif = PowerSet()
        for i in self.slots:
            if set2.get(i) is False:
                dif.put(i)
        return dif

    def issubset(self, set1):
        for i in set1.slots:
            if self.get(i) is False:
                return False
        return True
