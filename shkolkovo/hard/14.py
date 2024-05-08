def ss(n,sist):
    s = 0
    for i in range(1,len(n)+1):
        s += int(n[-i])*sist**(i-1)
    return s
for x in range(76):
    f1 = ['22','3','7', x ,'0','33','32']
    f2 = ['24','0','2','3', x , '25', '26']
    f3 = ['14','25','2','2','4',  x,x]
    s = ss(f1,76)+ss(f2,76)+ss(f3,76)
    if s%54==0:
        print(s//54,x)