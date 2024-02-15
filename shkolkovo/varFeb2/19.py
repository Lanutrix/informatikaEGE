from functools import lru_cache

@lru_cache
def f(a,b):
    if (a+b)>=94:
        return 0
    n = [f(a+2, b), f(a,b+2),
         f(a*4, b), f(a, b*4)]
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)

for k in range(10,90):
    p = f(4, k)
    if p == -2:
        print(k)