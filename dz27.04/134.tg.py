from functools import lru_cache

@lru_cache
def f(x,y):
    if (x**2+y**2)>=400:
        return 0
    n = [f(x-10,y+1), f(x-5,y-5), f(x+5,y-5)]
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)

c = 0
for s in range(-22,22):
    p = f(-1, s)
    if p!=0:
        c+=1

print(19, c)
c1 = 0
c2 = 0
for s in range(-22,22):
    p = f(-1, s)
    if p==1:
        c1+=1
    elif p==2:
        c2+=1
print(20, c1,c2)
c = 0
for s in range(0,22):
    p = f(-1, s)
    if p==-2:
        c = s
print(21, c)