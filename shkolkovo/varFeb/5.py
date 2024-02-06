mn = 9999999999999999999999999

for n in range(1,10000):

    nt = ''

    while n>0:
        nt+=str(n%3)
        n//=3

    nt = nt[::-1]

    if (nt.count('1')+nt.count('2'))%2==0:  nt+='0'
    else:                                   nt+='1'

    if (nt.count('1')+nt.count('2'))%2==0:  nt+='0'
    else:                                   nt+='1'

    r = int(nt, 3)
    if r>337:
        mn = min(r,mn)

print(mn)