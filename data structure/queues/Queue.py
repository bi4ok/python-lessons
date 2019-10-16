import modstack


class Queue:
    def __init__(self):
        self.stack_a = modstack.Stack()
        self.stack_b = modstack.Stack()

    def size(self):
        return self.stack_a.size()+self.stack_b.size()

    def enqueue(self, item):
        return self.stack_a.push(item)

    def dequeue(self):
        if self.stack_a.size() > 0:
            while self.stack_a.size() > 0:
                self.stack_b.push(self.stack_a.pop())
        return self.stack_b.pop()


s1 = Queue()
s1.enqueue(1)
s1.enqueue(2)
s1.enqueue(3)

while s1.size() > 0:
    print(s1.dequeue())
