from functools import lru_cache

@lru_cache
def f(x, y, m):
    if x+y>=95: return m%2==0
    if m==0: return 0
    h = [f(x+2, y , m-1), f(x * 3, y , m-1),f(x, y + 2 , m-1),f(x, y * 3 , m-1) ]
    return any(h) if (m-1)%2==0 else all(h)

print([s for s in range(1,89) if f(6,s,4) and not f(6,s,2)])