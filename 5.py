from functools import lru_cache

@lru_cache
def f(a,b,c,m):
    if (a+b+c)>=120: return m%2==0
    if m == 0: return 0
    n = [f(a+1,b,c,m-1),f(a,b+1,c,m-1),f(a,b,c+1,m-1)
         ,f(a*2,b,c,m-1),f(a,b*2,c,m-1),f(a,b,c*2,m-1)]
    return any(n) if (m-1)%2==0 else all(n)

print([ i for i in range(1,95) if f(10,5,i,4) and not f(10,5,i,2)])