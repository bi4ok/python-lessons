import modstack


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def circle(self, n):
        for i in range(n):
            self.enqueue(self.dequeue())


qu = Queue()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.circle(5)
while qu.size() > 0:
    print(qu.dequeue())
print()
s1 = modstack.Stack()
s2 = modstack.Stack()
s1.push(5)
s1.push(4)
s1.push(3)
s2.chered(s1, 3)
