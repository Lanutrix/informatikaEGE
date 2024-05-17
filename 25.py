def dd(n):
    s = set()
    for j in range(2,n//2+1,2):
        if n%j==0:
            s.add(j)
            if (n//j)%2==0:
                s.add(n//j)
    if len(s)>=142:
        return (len(s),max(s))
    return False

for i in range(397438, 443520+1):
    p = dd(i)
    if p:
        print(p)