from functools import lru_cache

@lru_cache
def f(a,b,m):
    if (a+b)>=73: return m%2==0
    if m == 0: return 0
    n = [f(a+1,b,m-1),f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
    return any(n) if (m-1)%2==0 else all(n)

print([ i for i in range(1,62) if f(11,i,4) and not f(11,i,2)])