class Heap:

    def __init__(self):
        self.HeapArray = []  # хранит неотрицательные числа-ключи

    def MakeHeap(self, a, depth):
        lenght = 2 ** (depth + 1) - 1
        self.HeapArray = [None] * lenght

        def sortirovka(massiv, item):
            target = None
            for slot in range(lenght):
                if not self.HeapArray[slot]:
                    self.HeapArray[slot] = item
                    target = slot
                    break
            if target:
                parent_index = (target - 1) // 2
                r_child_index = target + 1
                l_child_index = target + 2
            else:
                return None
            print(self.HeapArray[target], self.HeapArray[(target - 1) // 2], self.HeapArray)
            while self.HeapArray[(target - 1) // 2] < self.HeapArray[target]:
                self.HeapArray[(target - 1) // 2], self.HeapArray[target] = \
                    self.HeapArray[target], self.HeapArray[(target - 1) // 2]
                print(target, 'do')
                if target > 2:
                    target = (target - 1) // 2
                else:
                    break
                print(target, 'posle')

            print(self.HeapArray)

        for item1 in a:
            sortirovka(a, item1)
        print(self.HeapArray)
        # создаём массив кучи HeapArray из заданного
        # размер массива выбираем на основе глубины depth
        pass

    def GetMax(self):
        # вернуть значение корня и перестроить кучу
        return -1  # если куча пуста

    def Add(self, key):
        # добавляем новый элемент key в кучу и перестраиваем её
        return False  # если куча вся заполнена

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
s1 = Heap()
s1.MakeHeap(s, 3)
