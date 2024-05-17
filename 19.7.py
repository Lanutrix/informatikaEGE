from functools import lru_cache
@lru_cache
def f(a,b):
    if (a+b)>=150:
        return 0
    n = [f(a+2,b),f(a,b+2),f(a*3,b),f(a,b*3)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t)+1
    return -max(n)

for s in range(-134,0):
    p = f(16,-s)
    if p==-2:
        print(p,-s)