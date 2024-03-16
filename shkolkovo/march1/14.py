s = list('0123456789ABCDEF')

def f(nn,ss=26):
    p = 0
    n = nn[::-1]
    for i in range(len(n)):
        l = s.index(n[i])
        p += l*ss**i
    return p

for x in range(0,26):
    sm = (f('2760AD')+x*26**2) + (f('560E790')+ x*26**4) + (f('4770B7')+x*26**2)
    if sm%17==0:
        print(x, sm//17)