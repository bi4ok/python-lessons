def GenerateBBSTArray(a):
    balans_massiv = [None] * 3
    a = sorted(a)
    u = 1

    def balansirovka(a, bm, x):
        if not a:
            return None
        if x >= len(bm):
            nonlocal u
            u += 1
            l1 = 2 ** (u + 1) - 1
            bm += ([None] * (l1 - len(bm)))
        centr = int(len(a)/2)
        bm[x] = a[centr]
        balansirovka(a[:centr], bm, x * 2 + 1)
        balansirovka(a[centr+1:], bm, x * 2 + 2)
        return bm

    balans_massiv = balansirovka(a, balans_massiv, 0)
    return balans_massiv
фыв