from functools import lru_cache

@lru_cache
def f(a,b):
    if (a+b)>=205:
        return 0
    s = sorted([a,b])
    p = [f(s[0]+s[1],s[1]), f(s[0]*2,s[1])]
    t = [i for i in p if i<=0]
    if t:
        return -max(t)+1
    return -max(p)


for i in range(1,197):
    if f(9,i)==1:
        print(i)
        break
l = list()
for i in range(1,197):
    if f(9,i)==2:
        l.append(i)
l = sorted(l)
print(l[0],l[-1])

l = list()
for i in range(1,197):
    if f(9,i)==-2:
        l.append(i)
l = sorted(l)
print(int(sum(l)/len(l)))