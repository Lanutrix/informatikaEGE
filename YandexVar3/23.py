from functools import lru_cache

def f(n):
    if n==128:
        return 1
    if n>128 or n==20:
        return 0
    return f(n+3) + f(n*2) + f(n**2)

print(f(2))