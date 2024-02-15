from functools import lru_cache
g = set()
@lru_cache
def f(n, c, q):
    if c==20:
        g.add(n)
        return 0
    if q == 1:
        f(n-2, c+1, 2)
        f(n*3, c+1, 3)
    elif q == 2:
        f(n+1, c+1, 1)
        f(n*3, c+1, 3)
    elif q == 3:
        f(n+1, c+1, 1)
        f(n-2, c+1, 2)
    else:
        f(n+1, c+1, 1)
        f(n-2, c+1, 2)
        f(n*3, c+1, 3)
f(2,0,0)
print(len(g))