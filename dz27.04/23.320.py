from functools import lru_cache
g = 0

@lru_cache
def f(a, b):
    if a==50 and b==1:
        return 1
    elif a>50 or b>1:
        return 0
    if a==8 or a==16 or a==32:
        b += 1
    return f(a+1, b)+f(a+4, b)+f(a*2, b)

print(f(1,0))