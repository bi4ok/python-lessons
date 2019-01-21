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
    for i in range(pt):
        x = Thread(target=s4et, name='Thread N'+str(i), args=('Id'+str(i), sp[int(n*i):int(n*(i+1))], results))
        x.start()
    while x.is_alive() is True:
        time.sleep(0.5)
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