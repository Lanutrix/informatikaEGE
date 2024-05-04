f = open('27\\13\\27-13b.txt')
n = int(f.readline())
f = [int(i) for i in f.read().split()]
c = 0
for j in range(7,n):
    if f[j]%14==0:
        c += j-6
    elif f[j]%7==0:
        for i in range(0,j-6):
            if f[i]%2==0:
                c+=1
    elif f[j]%2==0:
        for i in range(0,j-6):
            if f[i]%7==0:
                c+=1
    else:
        for i in range(0,j-6):
            if f[i]%14==0:
                c+=1
print(c)