from functools import lru_cache

@lru_cache
def f(n):
    return g(n-1)

@lru_cache
def g(n):
    if n<10:
        return n
    return g(n-2)+1

cnt = 0

for i in range(2,101):
    k = f(i)
    if int(k**0.5)==k**0.5:
        cnt+=1

print(cnt)