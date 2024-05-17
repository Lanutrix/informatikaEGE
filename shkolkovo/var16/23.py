from functools import lru_cache

@lru_cache
def f(a,b):
    if a>b or a==8 or a==15:
        return 0
    if a==b:
        return 1
    return f(a+1,b)+f(a+2,b)+f(a*3,b)

print(f(3,10)*f(10,22))