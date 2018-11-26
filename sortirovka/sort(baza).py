import timeit
import random

s1 = []
for i in range(100):
    s1.append(random.randint(0, 100))
print(s1)
s2 = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


def sort1(s, l):
    i = 0
    while i + l < len(s):
        for j in range(i, len(s), l):
            for k in range(i, j, l):
                if s[j] < s[k]:
                    s.insert(k, s.pop(j))
                    s.insert(j, s.pop(k+1))
        i += 1


def sort2(s, l):
    i = 0
    while i + l < len(s):
        for j in range(i, len(s), l):
            for k in range(i, j, l):
                if s[j] < s[k]:
                    s[j], s[k] = s[k], s[j]
        i += 1


print(timeit.Timer(lambda: sort1(s2, 1)).timeit(number=100))
print(timeit.Timer(lambda: sort2(s2, 1)).timeit(number=100))

sort1(s2, 3)
print(s2)