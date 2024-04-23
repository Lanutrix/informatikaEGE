def f(a,b,c):
    if any([i for i in [a,b,c] if i>=20]) or sum([a,b,c])>=25:
        return 0
    n = [f(a*2,b,c),f(a,b*2,c),f(a,b,c*2),f(a+2,b+2,c+2)]
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)

for s in range(-19,0):
    p = f(2,3,-s)
    if p==-2:
        print(-s)