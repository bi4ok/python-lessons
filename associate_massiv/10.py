class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key):
        index = 0
        key = str(key)
        for i in range(len(key)):
            if ord(key[i]) != 0:
                index += ord(key[i]) * (i+1)
            elif ord(key) == 0:
                index = 0
                return index
            else:
                index += (11 * (i + 1))
        if self.size != 0:
            index = index % self.size
            return index
        return 0

    def is_key(self, key):
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return True
        return False

    def put(self, key, value):
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value

    def get(self, key):
        x = self.is_key(key)
        index = self.hash_fun(key)
        if x is True:
            return self.values[index]
        else:
            return None

