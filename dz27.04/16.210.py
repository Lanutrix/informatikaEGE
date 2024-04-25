from functools import lru_cache

def f(n):
    if n==1 or n==2:
        return 1
    return 3*f(n-2) + f(n-1)
@lru_cache
def ff(n):
    if n<3:
        return 1
    d = 0
    st, fn = 1, 1
    for u in range(2,n):
        d = 3*st + fn
        st, fn = fn, d
    return d

for i in range(100,120):
    print(i, ff(i)//ff(i-4))

# print(ff(20000020))