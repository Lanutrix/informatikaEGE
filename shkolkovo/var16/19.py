from functools import lru_cache

@lru_cache
def f(a):
    if a>=180:
        return 0
    if a%2==0:
        n = [f(a+3)]
    else:
        n = [f(a+4),f(a*3)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t)+1
    return -max(n)

for s in range(1,180,2):
    p = f(s)
    if p==-2:
        print(s)