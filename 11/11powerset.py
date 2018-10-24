import unittest, random


class PowerSet:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None]*self.size

    def hash_fun(self, val1):
        index = 0
        val = str(val1)
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
        if x is not None and self.find_value(val) is None:
            self.slots[x] = val
        else:
            return None

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

    def remove(self, val):
        index = self.find_value(val)
        if self.slots[index] is not None:
            self.slots[index] = None
        else:
            return None

    def len_set(self):
        x = 0
        for i in range(self.size):
            if self.slots[i] is not None:
                x += 1
        return x

    def print_all(self):
        for i in range(self.size):
            if self.slots[i] is not None:
                print(self.slots[i])

    def del_all(self):
        for i in range(self.size-1):
            self.slots[i] = None

    def intersection(self, set1):
        if self.len_set() < set1.len_set():
            set2 = PowerSet(self.size, 5)
            for i in range(self.size):
                if self.slots[i] is not None and set1.find_value(self.slots[i]) is not None:
                    set2.put_value(self.slots[i])
        else:
            set2 = PowerSet(set1.size, 5)
            for i in range(set1.size):
                if set1.slots[i] is not None and self.find_value(set1.slots[i]) is not None:
                    set2.put_value(set1.slots[i])
        return set2

    def union(self, set1):
        set2 = PowerSet(self.size+set1.size, 5)
        for i in range(self.size):
            if self.slots[i] is not None:
                set2.put_value(self.slots[i])
        for j in range(set1.size):
            if set1.slots[j] is not None:
                set2.put_value(set1.slots[j])
        return set2

    def difference(self, set1):
        set2 = PowerSet(self.size, 5)
        for i in range(self.size):
            if self.slots[i] is not None and self.slots[i] != set1.slots[i]:
                set2.put_value(self.slots[i])
        return set2

    def issubset(self, set1):
        for i in range(set1.size):
            if set1.slots[i] is not None and self.find_value(set1.slots[i]) is None:
                return False
        return True


class TestMethods(unittest.TestCase):

    def initialize(self):
        self.s = PowerSet(18, 5)
        for i in range(10):
            self.s.put_value(str(i))
        return self.s

    def test_put(self):
        self.initialize()
        self.s.put_value("11")
        self.assertTrue(self.s.find_value("11") is not None)    # Возможность добавления отсутствующего элемента
        self.assertTrue(self.s.put_value("11") is None)         # Hевозможность добавления присутствующего элемента
        self.s.del_all()

    def test_remove(self):
        self.initialize()
        self.s.remove("9")
        self.assertTrue(self.s.find_value("9") is None)         # Удаление элемента, присутствующего в множестве
        self.s.del_all()

    def test_intetsection(self):
        self.initialize()
        self.s2 = PowerSet(18, 5)
        self.s2.put_value(11)
        self.s2.put_value(12)
        self.s2.put_value(13)
        self.assertTrue(self.s.intersection(self.s2).len_set() == 0)   # Проверка на пустоту получивщегося множества
        self.s2.put_value("1")
        self.s2.put_value("2")
        self.s2.put_value("3")
        self.assertTrue(self.s.intersection(self.s2).len_set() == 3)   # Длина полученного множества равна кол-ву совпадений
        self.s2.del_all()
        self.s.del_all()

    def test_union(self):
        self.initialize()
        self.s2 = PowerSet(18, 5)
        self.s2.put_value(11)
        self.s2.put_value(12)
        self.s2.put_value(13)
        self.assertTrue(self.s.union(self.s2).len_set() == (self.s.len_set()+self.s2.len_set()))  # Оба не пустые
        self.s2.del_all()
        self.assertTrue(self.s.union(self.s2).len_set() == self.s.len_set())         # Параметр - пустое множество
        self.s.del_all()

    def test_difference(self):
        self.initialize()
        self.s2 = PowerSet(18, 5)
        for i in range(10):
            self.s2.put_value(str(i))
        self.assertTrue(self.s.difference(self.s2).len_set() == 0)      # В результате получилось пустое множества
        self.s2.del_all()
        self.assertTrue(self.s.difference(self.s2).len_set() == 10)     # ~ не пустое множество
        self.s.del_all()
        self.s2.del_all()

    def test_issubset(self):
        self.initialize()
        self.s2 = PowerSet(18, 5)
        for i in range(5):
            self.s2.put_value(str(i))
        self.assertTrue(self.s.issubset(self.s2))             # Все элементы параметра входят в текущее множество
        self.s2.del_all()                                     # Параметр является подмножеством
        for i in range(11):
            self.s2.put_value(str(i))                         # Все элементы параметра входят в текущее множество
        self.assertFalse(self.s.issubset(self.s2))            # Элементов в параметре больше, оно не является подмножеством
        self.s2.del_all()
        for i in range(5):
            self.s2.put_value(str(i))
        self.s2.put_value("55")                               # В параметре есть элемент, которого нет в текущем множестве
        self.assertFalse(self.s.issubset(self.s2))            # Параметр не является подмножеством
        self.s.del_all()
        self.s2.del_all()


if __name__ == '__main__':
    unittest.main()