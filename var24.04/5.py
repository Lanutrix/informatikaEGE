def tri(n):
    s = ''
    while n>0:
        s+=str(n%3)
        n//=3
    return s[::-1]
m = 10000
for n in range(1,10000):
    nt = tri(n)
    if n%3==0:
        nt += nt[-2:]
    else:
        nt += tri((n%3)*5)
    r = int(nt, 3)

    if r>133:
        m = min(m, r)

print(m)