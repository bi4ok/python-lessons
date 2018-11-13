import datetime
import time


class DzTable:

    def __init__(self, predmet, size):
        self.name = str(predmet)
        self.size = size
        self.dz = [None]*self.size
        self.slots = [None]*self.size
        self.times = [None]*self.size

    def check_dz(self):
        print(self.name, self.dz)

    def seek_slot(self):
        for i in range(self.size):
            if self.slots[i] is None:
                return i
        return None

    def clearing(self):
        t = time.time()
        for i in range(self.size):
            if self.times[i] == 0:
                pass
        pass

    def add_dz(self, predmet, dz, srok):
        slot = self.seek_slot()
        self.slots[slot] = predmet
        self.dz[slot] = dz
        self.times[slot] = srok


x = (5, 6, 7)
t = (2018, x[1], x[0], 1, 5, 0, 1, 48, 0)
print(time.time(), time.mktime(t))
s1 = DzTable("algebra", 18)
s1.add_dz("algebra", 454, (5, 6, 7))
print(s1.slots[0], s1.dz[0], s1.times[0])