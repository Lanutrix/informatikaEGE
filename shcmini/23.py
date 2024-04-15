from functools import lru_cache
l = set()
@lru_cache
def f(n, c):
    if c==6:
        l.add(n)
        return n
    return [f(n+3,c+1),f(n+5,c+1), f(n*2,c+1), f(n*3,c+1)]

f(35,0)
print(len(l))