from functools import lru_cache

@lru_cache
def f(s):
    if s>=64:
        return 0
    n = [f(s+1),f(s*2)]
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    else:
        return -max(n)

for s in range(1,64):
    if f(s)==-1:
        print(19, s)
        break

for s in range(1,64):
    if f(s)==2:
        print(20, s)
        break

for s in range(1,64):
    if f(s)==-2:
        print(21, s)