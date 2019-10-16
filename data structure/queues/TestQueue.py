class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() < 1:
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)