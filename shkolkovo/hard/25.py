def f(n):
    flag = 0
    if (int(n**0.5))**2==n:
        for i in range(2,int(n**0.5)-1):
            if n%i==0:
                if flag==0:
                    flag=n//i
                else:
                    flag=0
                    break
    return flag
c = 0
for i in range(110000,250001):
    p = f(i)
    if p!=0:
        print(p)