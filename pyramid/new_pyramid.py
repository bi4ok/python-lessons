class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        lenght = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * lenght

        def sortirovka(item):
            target = None
            for slot in range(lenght):
                if not self.HeapArray[slot]:
                    self.HeapArray[slot] = item
                    target = slot
                    break
            if not target:
                return None

            while self.HeapArray[(target - 1) // 2] < self.HeapArray[target]:
                self.HeapArray[(target - 1) // 2], self.HeapArray[target] = \
                    self.HeapArray[target], self.HeapArray[(target - 1) // 2]
                if target > 2:
                    target = (target - 1) // 2
                else:
                    break
        for item1 in a:
            sortirovka(item1)

    def GetMax(self):
        def sortik(index):
            try:
                target = max(self.HeapArray[index * 2 + 1], self.HeapArray[index * 2 + 2])
            except TypeError:
                target = self.HeapArray[index * 2 + 1] if self.HeapArray[index * 2 + 1] else self.HeapArray[index * 2 + 2]
            target_index = self.HeapArray.index(target)
            if target and target > self.HeapArray[index]:
                self.HeapArray[index], self.HeapArray[target_index] = \
                    self.HeapArray[target_index], self.HeapArray[index]
                sortik(target_index)
            else:
                return None
        if self.HeapArray:
            root = self.HeapArray[0]
            self.HeapArray[0] = None
            for i in range(len(self.HeapArray) - 1, -1, -1):
                if self.HeapArray[i]:
                    self.HeapArray[0], self.HeapArray[i] = self.HeapArray[i], self.HeapArray[0]
                    sortik(0)
                    break
            return root
        else:
            return -1

    def Add(self, key):
        target = None
        for slot in range(len(self.HeapArray)):
            if not self.HeapArray[slot]:
                self.HeapArray[slot] = key
                target = slot
                break
        if not target:
            return False

        while self.HeapArray[(target - 1) // 2] < self.HeapArray[target]:
            self.HeapArray[(target - 1) // 2], self.HeapArray[target] = \
                self.HeapArray[target], self.HeapArray[(target - 1) // 2]
            if target > 2:
                target = (target - 1) // 2
            else:
                break