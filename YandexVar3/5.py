def tri(n):
    s = ''
    while n>0:
        s+=str(n%3)
        n//=3
    if s:
        return s[::-1]
    return '0'
for n in range(1,10000):
    nt = tri(n)

    nt += tri(nt.count('2'))

    nt += tri(nt.count('1'))

    nt += tri(nt.count('0'))

    r = int(nt,3)
    if r<1000:
        print(n)