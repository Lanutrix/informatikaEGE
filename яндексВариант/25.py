from functools import lru_cache

@lru_cache
def deli(x):
    d = []
    kol = 0
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            d.append(i)
            kol+=1
        if kol>6:
            return False
    if kol==6:
        k = d[0]+d[-1]
        if 1000<=k<10000:
            return k
    return False

c = 0


for i in range(650_000, 100_000_000):
    if deli(i):
        print(i, deli(i))
        c+=1
        if c>=5:
            exit()