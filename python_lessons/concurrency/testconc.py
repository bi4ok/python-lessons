import time
import random
from threading import Thread


def s4et(id, sp4, res):
    sum = 0
    for x in sp4:
        sum += x
        print(sum)
        time.sleep(0.05)
    res[id] = sum

s = {}
x = 'Id'+str(1)
s[x] = 5
print(s)
x = 0
while x != 10:
    x = 0
    for i in range(10):
        print(i)
        x += 1
    print(x)
print(x)