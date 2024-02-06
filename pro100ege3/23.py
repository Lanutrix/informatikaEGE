from functools import lru_cache
import sys

sys.setrecursionlimit(10000)

@lru_cache
def f(x,y):
    if x==y:
        return 1
    if x>y or x==100:
        return 0
    return f(x+x%10, y) + f(x+x%68, y) + f(x**2, y)

print(f(2,68)*f(68,680))