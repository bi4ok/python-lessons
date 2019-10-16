import random
import unittest


class Cache:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None]*self.size
        self.values = [None]*self.size
        self.hits = [None]*self.size

    def hash_fun(self, val1):
        index = 0
        val = str(val1)
        for i in range(len(val)):
            if ord(val[i]) != 0:
                index += ord(val[i]) * (i+1)
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

    def put_value(self, val, item):
        x = self.seek_slot(val)
        if x is not None:
            self.slots[x] = val
            self.values[x] = item
            self.hits[x] = 0
        else:
            x = int(self.clearing()["key"])
            self.slots[x] = val
            self.values[x] = item
            self.hits[x] = self.clearing()["sr"]

    def find_value(self, val):
        index = self.hash_fun(val)
        for i in range(self.size - 1):
            if self.slots[index] == val:
                return index
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

    def get(self, key):
        x = self.find_value(key)
        if x is not None:
            self.hits[x] += 1
            return self.values[x]
        else:
            return None

    def del_all(self):
        for i in range(self.size):
            self.slots[i] = None
            self.values[i] = None
            self.hits[i] = None

    def print_all(self):
        for i in range(self.size):
            if self.slots[i] is not None:
                print(self.slots[i], self.values[i], self.hits[i])

    def clearing(self):
        min = self.hits[random.randint(0, self.size-1)]
        key = None
        sr = 0
        for i in range(self.size):
            sr += self.hits[i]
            if self.hits[i] <= min:
                min = self.hits[i]
                key = i
        return {"sr": int(sr/(self.size-1)), "key": key}


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = Cache(18, 5)
        for i in range(self.s.size):
            self.s.put_value(str(i), i)
        for j in range(51):
            if j < 18:
                self.s.get(str(j))
            elif j < 35:
                self.s.get(str(j-18))
            else:
                self.s.get(str(j-35))                   # Количество обращений по ключам 17 = 1, 16 = 2, остальные = 3

        return self.s

    def test_putvalue(self):
        self.initialize()
        self.s.put_value("100", 100500)
        self.assertTrue(self.s.values[17] == 100500)    # Сперва заменяется слот 17, имеющий 1 обращение
        self.s.put_value("101", 100499)
        self.assertTrue(self.s.values[0] == 100499)     # Вторым заменяется слот 0, имеющий 2 обращения.
        self.s.del_all()                                # Слот 17 игнорируется,имея среднее значение кол-ва обращений

    def test_get(self):
        self.initialize()
        self.assertTrue(self.s.hits[11] == 3)           # 11ый слот имеет 3 обращения
        self.s.get(str(0))
        self.assertTrue(self.s.hits[11] == 4)           # после обращения к значению 11 слота, счетчик увеличился до 4
        self.assertTrue(self.s.hits[0] == 2)            # доп цикл с другим слотом/значением
        self.s.get(str(16))
        self.assertTrue(self.s.hits[0] == 3)
        self.s.del_all()


if __name__ == '__main__':
    unittest.main()