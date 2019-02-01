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

a = []
for i in range(100):
    a.append(random.randint(0, 1000))
n = len(a)/10
results = {}

s[1] = Thread(target=s4et, name='Thread N'+str(1), args=('Id'+str(1), a[int(n*1):int(n*(1+1))], results))
s[2] = Thread(target=s4et, name='Thread N'+str(2), args=('Id'+str(2), a[int(n*2):int(n*(2+1))], results))
print(s)
s[1].start()
while s[1].is_alive():
    time.sleep(0.01)

print(results)