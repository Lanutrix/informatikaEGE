from functools import lru_cache

@lru_cache
def f(a):
    if a>=70:
        return 0
    n = [f(a+1), f(a*2)]
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)

a19 = 0
a20 = []
a21 = 0

for k in range(1,70):
    p = f(k)
    if p==-1:
        a19 = k
    if p==2:
        a20.append(k)
    if p==-2:
        a21 = k

print(a19)
print(min(a20))
print(a21)