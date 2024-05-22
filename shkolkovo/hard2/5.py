def f(n,ss=4):
    s = ''
    while n>0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
m = 0
for n in range(1,100000):
    nb = f(n)
    if nb.count('3')>0:
        nb += '21'
    else:
        nb += '12'
    r = int(nb, 4)
    if r<280:
        m = max(m,r)
print(m)

print((12**2+25)**0.5)