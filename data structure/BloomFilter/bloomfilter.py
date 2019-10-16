class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = [0]*self.filter_len

    def hash1(self, str1):
        m, n = 17, 0
        for c in str1:
            code = ord(c)
            n = n*m + code
        n = n % self.filter_len
        return n

    def hash2(self, str1):
        m, n = 223, 0
        for c in str1:
            code = ord(c)
            n = n*m + code
        n = n % self.filter_len
        return n

    def add(self, str1):
        hashlist = [self.hash1, self.hash2]
        for i in hashlist:
            self.filter[i(str1)] = 1

    def is_value(self, str1):
        hashlist = [self.hash1, self.hash2]
        sum = 0
        for i in hashlist:
            if self.filter[i(str1)] == 1:
                sum += 1
        if sum == len(hashlist):
            return True
        else:
            return False
