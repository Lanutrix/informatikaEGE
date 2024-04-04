def d(n,m):
    return not (n%m)

for a in range(1,10000):
    f = 1
    for x in range(1,1000):
        if not( not(d(x,72)) or d(x,495) or not(d(x,a)) ):
            f = 0
    if f:
        print(a)
        break