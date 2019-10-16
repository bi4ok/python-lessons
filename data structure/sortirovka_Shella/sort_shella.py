import timeit
import random

s1 = []
for i in range(100):
    s1.append(random.randint(0, 100))
s2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def sort_shella(s):
    l = 1
    while l*3+1 < len(s):
        l = l*3+1
    i = 0
    while i + l < len(s):
        for j in range(i, len(s), l):
            for k in range(0, j, l):
                if s[j] < s[k]:
                    s[j], s[k] = s[k], s[j]
        i += 1
        l = (l - 1) // 3
        if l < 1:
            break


print(timeit.Timer(lambda: sort_shella(s2)).timeit(number=100))
print(s2)