
def genersum(scz):
    ids = len(scz)

    def long_process(id, n):                # внутренняя функция осуществляющая суммирование
        sum = 0
        for x in range(n):
            sum += x
            print(id, sum)
            if x < n-1:
                yield
            else:
                yield sum

    idgen = {}                              # один словарь для функций
    results = {}                            # второй для их результатов
    for i in range(ids):
        idgen[i] = long_process('Id'+str(i), scz[i])
        results['Id'+str(i)] = None

    x = 0                                   # цикл, который заканчивается, когда каждая функция выдаст результат
    while x != ids:
        x = 0
        for i in range(ids):
            if results['Id'+str(i)] is None: results['Id'+str(i)] = next(idgen[i])
            else: x += 1

    return results                          # возврат словаря с результатами суммирования


x = (100, 202, 1000, 52)
res = genersum(x)
print(res)
