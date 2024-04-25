f = open('dz27.04\\17-390.txt').read()
f = list(map(int, f.split()))
na151 = [i for i in f if abs(i)%1000==151]
sra = sum(na151)/len(na151)
mx = 100000000
c = 0
for i in range(2, len(f)):
    p = [f[i], f[i-1], f[i-2]]

    f1 = 0<len([1 for i in p if 1000<=abs(i)<10000])<3

    k13 = [1 for i in p if abs(i)%13==0]
    k7 = [1 for i in p if abs(i)%7==0]
    f2 = len(k13)>len(k7)

    f3 = len([i for i in p if i>sra])==3

    if f1 and f2 and f3:
        c += 1
        mx = min(mx, sum([f[i], f[i-1], f[i-2]]))

print(c, mx)