from functools import lru_cache

@lru_cache
def f(x):
    if x>=229:
        return 0
    n = [f(x+2),f(x+3),f(x+4),f(x*2)]
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)
s19 = []
s20 = []
s21 = []
for n in range(1,229):
    p = f(n)
    if p==-1:
        s19.append(n)
    if p==2:
        s20.append(n)
    if p==-2:
        s21.append(n)

print(min(s19))
print(min(s20),max(s20))
print(min(s21))