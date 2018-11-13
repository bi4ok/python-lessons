import unittest

class Deque:
    def __init__(self):
        self.queue = []

    def addFront(self, item):
        self.queue.append(item)

    def addTail(self, item):
        self.queue.insert(0, item)

    def removeFront(self):
        return self.queue.pop()

    def removeTail(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def palitest(self):
        if deq.size() > 0:
            for i in range(int(deq.size()/2)):
                if deq.removeTail() != deq.removeFront():
                    return "ne palindrom"
            return "palindrom"
        else:
            return "net elementov"


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.deq1 = Deque()
        for j in range(25):
            self.deq1.addTail(j)

    def testaf(self):
        x = self.deq1.size()
        self.deq1.addFront(100)
        self.assertTrue(x == self.deq1.size() - 1)
        self.assertTrue(self.deq1.removeFront() == 100)

    def testat(self):
        x = self.deq1.size()
        self.deq1.addTail(25)
        self.assertTrue(x == self.deq1.size() - 1)
        self.assertTrue(self.deq1.removeTail() == 25)

    def testrf(self):
        x = self.deq1.size()
        self.deq1.removeFront()
        self.assertTrue(x == self.deq1.size() + 1)
        self.assertFalse(self.deq1.queue[0] == 0)

    def testrt(self):
        x = self.deq1.size()
        self.deq1.removeTail()
        self.assertTrue(x == self.deq1.size() + 1)
        self.assertFalse(self.deq1.queue[self.deq1.size()-1] == 24)


deq = Deque()
deq.addFront('2')
deq.addTail('1')
deq.addFront('1')
deq.addFront('1')
deq.addTail('1')
print(deq.palitest())

if __name__ == '__main__':
    unittest.main()