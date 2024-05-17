def f(x,y):
    if (x**2+y**2)>=400:
        return 0
    n = [f(x+1,y+2),f(x,y+1)]
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)

for s in range(1,18):
    p = f(10, s)
    if p==-2:
        print(s)
        break