from functools import lru_cache

@lru_cache
def f(x):
    if x>115 or x == 25:
        return 0
    if x==115:
        return 1
    return f(x+3)+f(x*2)+f(x*5)

print(f(5))