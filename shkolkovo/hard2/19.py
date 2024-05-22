from functools import lru_cache
@lru_cache
def f(a,b):
    if (a+b)>=186:
        return 0
    n = [f(a+7,b),  f(a,b+7),
         f(a+11,b), f(a,b+11),
         f(a*2,b),  f(a,b*2)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t)+1
    return -max(n)
c = 0#84+83+82+81+80+79+78+76+75+74
for s in range(-175, 0):
    p = f(10,-s)
    if p == -2:
        print(-s)
        c += -s
print(c)