def f(n,ss=3):
    s = ''
    while n>0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
for x in range(1,1027*2):
    if f(9**1027-3**x+79).count('0')==1600:
        print(f(9**1027-3**x+79))