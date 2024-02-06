from functools import lru_cache

@lru_cache
def f(x, y):
    if x==y:
        return 1
    if x>y or x==20:
        return 0
    return f(x+1,y)+f(x*2,y)

print(f(8, 5)*f(5,20))