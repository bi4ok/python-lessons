import random

s1 = []
for i in range(30):
    s1.append(random.randint(0,25))
#for j in range(10):
 #   s1.append(10)
print(s1)
s = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
N = s[7]


def sort_razbienie(s, N):
    i1 = 0
    i2 = len(s)-1
    rek = 0
    while i1 < len(s) and i2 != 0:
        z = 0
        if s[i1] <= N:
            i1 += 1
            z += 1
        if s[i2] > N:
            i2 -= 1
            z += 1
        if z == 0:
            s[i1], s[i2] = s[i2], s[i1]
            rek += 1
        if i2 - i1 < 1:
            break
    if rek == 0:
        sort_razbienie(s, sum(s)//len(s))


sort_razbienie(s1, 30)
print(s1, sum(s1)//len(s1))