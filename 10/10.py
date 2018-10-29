import unittest, random


class AssociateTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None]*self.size
        self.values = [None]*self.size

    def hash_fun(self, val):
        index = 0
        for i in range(len(val)):
            if int(val[i]) != 0:
                index += int(val[i]) * (i+1)
            else:
                index += (11 * (i + 1))
        index = index % self.size
        return index

    def put_value(self, key, item):
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = item

    def is_key(self, val):
        index = self.hash_fun(val)
        if self.slots[index] == val:
            return index
        return None

    def del_all(self):
        for i in range(self.size):
            self.slots[i] = None
            self.values[i] = None

    def print_all(self):
        for i in range(self.size):
            print(self.slots[i], self.values[i])

    def get(self, key):
        x = self.is_key(key)
        if x is not None:
            return self.values[x]
        else:
            return None


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = AssociateTable(18, 5)
        for i in range(self.s.size):
            self.s.put_value(str(i), "number "+str(i))
        return self.s

    def test_putvalue(self):
        self.initialize()
        self.s.del_all()
        self.s.put_value("123", "321")                      # Добавление значения по новому ключу
        self.assertTrue(self.s.slots[14] == "123")
        self.assertTrue(self.s.values[14] == "321")
        self.s.put_value("123", "321")                      # Добавление значения по существующему ключу
        self.assertTrue(self.s.slots[14] == "123")
        self.assertTrue(self.s.values[14] == "321")
        self.s.del_all()

    def test_iskey(self):
        self.initialize()
        self.assertTrue(self.s.is_key("17") == 15)          # Проверка присутствующего ключа
        self.assertTrue(self.s.is_key("20") is None)        # Проверка отсутствующего ключа
        self.s.del_all()

    def test_get(self):
        self.initialize()
        self.assertTrue(self.s.get("1") == "number 1")      # Проверка извлечения значения по существующему ключу
        self.s.del_all()
        self.assertTrue(self.s.get("1") is None)            # Проверка извлечения значения по отсутсвующему кллючу


if __name__ == '__main__':
    unittest.main()

