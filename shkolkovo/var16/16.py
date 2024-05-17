from functools import lru_cache

@lru_cache
def f(n):
    if n==1: return 1
    if n==2: return 3
    return f(n-1)*f(n-2)+n

print(f(7))