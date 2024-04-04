def f(a, c):
    if a>=131:
        return 0
    n1 = [a+2,a+3,a*2]
    n = []
    for i in range(3):
        if c!=i:
            n.append(f(n1[i],i))
    t = [i for i in n if i<=0]
    if t:
        return -max(t)+1
    return -max(n)
for s in range(4,67):
    if f(s,-1)==-2:
        print(s)
