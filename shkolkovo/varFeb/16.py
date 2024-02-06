from functools import lru_cache

@lru_cache
def f(n):
    if n<=2:
        return n+3
    return f(n-1) + g(n-2)

@lru_cache
def g(n):
    if n<=2:
        return n+1
    return g(n-1) + f(n-1)

print(g(4)+f(5))