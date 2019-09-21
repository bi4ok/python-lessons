def GenerateBBSTArray(a):
    balans_massiv = []
    a = sorted(a)

    def balansirovka(a, bm):
        if not a:
            return None
        centr = int(len(a)/2)
        bm.append(a[centr])
        balansirovka(a[:centr], bm)
        balansirovka(a[centr+1:], bm)
        return bm

    balans_massiv = balansirovka(a, balans_massiv)
    return balans_massiv

