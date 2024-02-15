mx = 0
def ss7(s):
    k = ''
    while s>0:
        k+=str(s%7)
        s//=7
    return(k[::-1])
for x in range(12):
    for y in range(19):
        for z in range(12):
            if len(set([x,y,z]))==3:
                f1 = 19 + y*22 + 9*22**2 + 8*22**3 + x*22**4 + 22**5 + 10*22**6 + 22**7
                f2 = 1 + z*19 + 19**2 + 9*19**3 + y*19**4 + 5*19**5 + 13*19**6
                f3 = 10 + x*12 + 9*12**2 + 2*12**3 + z*12**4 + 3*12**5 + 4*12**6
                f = f1-f2+f3
                f = sum(list(map(int, list(str(ss7(f))))))
                mx = max(mx, f)
print(ss7(mx))
