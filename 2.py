from functools import lru_cache

@lru_cache
def f(a, x1, x2,c):
    if (a)>=68:
        return 0
    nn = [a+3, a+6, a*3]
    n = []
    if c==1:
        for i in range(3):
            if (i+1)==x1:
                continue
            else:
                n.append(f(nn[i], i+1,x2,2))
    else:
        for i in range(3):
            if (i+1)==x2:
                continue
            else:
                n.append(f(nn[i], x1, i+1, 1))
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    else:
        return -max(n)

for s in range(1,68):
    p = f(s,0,0,1)
    if p==3:
        print(s)