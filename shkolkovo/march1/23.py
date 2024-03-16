from functools import lru_cache

@lru_cache
def f(n):
    if n>77:
        return 0
    if n==77:
        return 1
    return f(n+2)+f(n*3)

print(f(7))