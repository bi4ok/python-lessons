import random


def create():
    for i in range(10):
        f = open(str(i+1)+".txt", 'w+')
        for j in range(3):
            f.write(str(random.randint(1, 10))+"\n")
        f.close()


def itogo():
    z = 0
    for k in range(2):
        f = open(str(random.randint(1, 10))+".txt", 'r')
        if f.mode == 'r':
            x = f.readlines()
            for l in range(3):
                print(int(x[l]))
                z += int(x[l])
    return z


y = itogo()
print(y)
