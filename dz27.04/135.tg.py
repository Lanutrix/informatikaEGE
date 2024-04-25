from functools import lru_cache

@lru_cache
def f(a,b):
    if a>=61:
        return 0
    n = [f(a+1, b-1)]
    if (b-a*2)>=0:
        n.append( f(a*2,b-a*2))
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)
c = 0
for i in range(1,61):
    p = f(i,80)
    if p==1:
        c+=1

print(19, c)
c = []
for i in range(1,61):
    p = f(i,80)
    if p==2:
        c.append(i)


print(20, *c)

for i in range(1,61):
    p = f(i,80)
    if p==-2:
        print(i)