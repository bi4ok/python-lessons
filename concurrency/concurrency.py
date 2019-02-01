import time
import random
from threading import Thread


def odc4et(pt, sp):

    def s4et(id, sp4, res):
        sum = 0
        for x in sp4:
            sum += x
            time.sleep(0.05)
        res[id] = sum

    n = len(sp)/pt
    results = {}
    treds = {}
    for i in range(pt):
        treds[i] = Thread(target=s4et, name='Thread N'+str(i), args=('Id'+str(i), sp[int(n*i):int(n*(i+1))], results))
        treds[i].start()
    for j in range(pt):
        while treds[j].is_alive():
            time.sleep(0.01)
    itog = 0
    for i in results:
        itog += results[i]
    return itog


a = []
for i in range(10000):
    a.append(random.randint(0, 1000))
print(sum(a))
s = odc4et(10, a)
print(s)