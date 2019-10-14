import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)
        self.occupancy = 0.5

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, item):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = item
        self.count += 1

    def insert(self, i, itm):
        if 0 <= i <= self.count:
            if self.count == self.capacity:
                self.resize(2*self.capacity)
            self.count += 1
            new_array = self.make_array(self.capacity)
            for j in range(self.count):
                if j == i:
                    new_array[j] = itm
                elif j < i:
                    new_array[j] = self.array[j]
                elif j > i:
                    new_array[j] = self.array[j-1]
            self.array = new_array
        else:
            raise IndexError('Index is out of bounds')
            
    def delete(self, i):
        if 0 <= i < self.count:
            for j in range(self.count-1):
                if j >= i:
                    self.array[j] = self.array[j+1]
            self.count -= 1
            if self.count < int(self.capacity*self.occupancy):
                if int(self.capacity/1.5) < 16:
                    self.resize(16)
                else:
                    self.resize(int(self.capacity/1.5))
        else:
            raise IndexError('Index is out of bounds')


s1 = DynArray()
for i in range(10):
    s1.append(i)

s1.delete(0)

for i in s1.array:
    print(i)

print()
