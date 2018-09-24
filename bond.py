import ctypes

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self,item):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = item
        self.count += 1

    def print_all(self):
        for i in range(self.count):
            print (self[i])

    def insert(self,i,itm):
        if i <= self.count:
            if self.count == self.capacity:
                self.resize(2*self.capacity)
            self.count += 1
            new_array = self.make_array(self.count)
            for j in range(self.count):
                if j == i:
                    new_array[j] = itm
                elif j < i:
                    new_array[j] = self.array[j]
                elif j > i:
                    new_array[j] = self.array[j-1]
            self.array = new_array
        else:
            print('в строке не хватает элементов')
            
            
                
s1 = DynArray()
s1.append(1)
s1.append(2)
s1.append(3)
s1.print_all()
s1.insert(3,5)
print("___________")
s1.print_all()
