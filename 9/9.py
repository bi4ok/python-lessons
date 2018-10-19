import unittest, random


class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None]*self.size

    def hash_fun(self, val):
        index = 0
        for i in range(len(val)):
            if int(val[i]) != 0:
                index += int(val[i]) * (i+1)
            else:
                index += (11 * (i + 1))
        index = index % self.size
        return index

    def seek_slot(self, val):
        index = self.hash_fun(val)
        for i in range(self.size - 1):
            if self.slots[index] is None:
                return index
            else:
                if index + self.step <= (self.size - 1):
                    index += self.step
                    if self.slots[index] is None:
                        return index
                elif index + self.step > self.size-1:
                    index = 0 + (index + self.step - self.size)
                    if self.slots[index] is None:
                        return index
        return None

    def put_value(self, val):
        x = self.seek_slot(val)
        if x is not None:
            self.slots[x] = val
        else:
            return None

    def find_value(self, val):
        index = self.hash_fun(val)
        for i in range(self.size - 1):
            if self.slots[index] is None:
                return None
            else:
                if index + self.step <= (self.size - 1):
                    index += self.step
                    if self.slots[index] == val:
                        return index
                elif index + self.step > self.size - 1:
                    index = 0 + (index + self.step - self.size)
                    if self.slots[index] == val:
                        return index
        return None

    def del_all(self):
        for i in range(self.size-1):
            self.slots[i] = None


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = HashTable(18, 5)
        self.s.put_value("1")
        self.s.put_value("2")
        self.s.put_value("3")
        self.s.put_value("4")
        self.s.put_value("5")
        self.s.put_value("6")
        self.s.put_value("7")
        self.s.put_value("8")
        self.s.put_value("9")
        self.s.put_value("10")
        self.s.put_value("11")
        self.s.put_value("12")
        self.s.put_value("13")
        self.s.put_value("14")
        self.s.put_value("15")
        self.s.put_value("16")
        self.s.put_value("17")
        self.s.put_value("18")
        return self.s

    def test_hashfun(self):
        self.initialize()
        for i in range(50):
            self.assertTrue(self.s.hash_fun(str(random.randint(0, 100))) >= 0)
            self.assertTrue(self.s.hash_fun(str(random.randint(0, 100))) < self.s.size)
        self.s.del_all()

    def test_seekslot(self):
        self.initialize()
        self.assertTrue(self.s.seek_slot("1") is None)    # Тест пытается найти место в полном списке
        self.s.del_all()
        self.s.put_value("1")                             # Проверка работы с коллизиями при шаге 5
        self.assertTrue(self.s.seek_slot("1") == 6)
        self.s.put_value("1")
        self.assertTrue(self.s.seek_slot("1") == 11)
        self.s.put_value("1")
        self.assertTrue(self.s.seek_slot("1") == 16)
        self.s.del_all()

    def test_putvalue(self):
        self.initialize()
        self.s.del_all()
        self.s.put_value("123")
        self.assertTrue(self.s.slots[14] == "123")
        self.s.del_all()

    def test_findvalue(self):
        self.initialize()
        self.assertTrue(self.s.find_value("17") == 17)
        self.s.del_all()


if __name__ == '__main__':
    unittest.main()