import random
import timeit


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


def sort_razbienie(s, left, right):
    if left >= right:
        return
    N = s[left]
    i1 = left
    i2 = right
    while i1 <= i2:
        while s[i1] <= N:
            i1 += 1
            if i1 > right:
                i1 -= 1
                break
        while s[i2] > N and i2 > i1+1:
            i2 -= 1
        if i1 < i2 and s[i1] > s[i2]:
            s[i1], s[i2] = s[i2], s[i1]
        if i2 - i1 == 1:
            if s[i1] > N:
                i1 -= 1
                i2 -= 1
            break
        elif i2 == i1:
            while s[i1-1] <= N and i2 - i1 < 1:
                i1 -= 1
                while s[i2-1] > N:
                    i2 -= 1
            break
    if s[i2] > N:
        i2 -= 1
    s[i2], s[left] = s[left], s[i2]
    sort_razbienie(s, left, i2-1)
    sort_razbienie(s, i2+1, right)


s = []
for i in range(10000):
   s.append(random.randint(0,100))
s1 = s
s1 = sorted(s1)
sort_razbienie(s, 0, len(s)-1)
print(s == s1)
print(timeit.Timer(lambda: sort_razbienie(s, 0, len(s)-1)).timeit(number=1))
print(timeit.Timer(lambda: sorted(s)).timeit(number=1))