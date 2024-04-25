f = open('dz27.04\\17-399.txt').read()
f = list(map(int, f.split()))

mnp = min([i for i in f if 500<=abs(i)<600])

mx = -100000000
c = 0
for i in range(1, len(f)):
    p = [f[i], f[i-1]]

    f1 = len([1 for i in p if abs(i)%10==4])==1

    f2 = (sum(p))%mnp!=0

    if f1 and f2:
        c += 1
        mx = max(mx, sum(p))

print(c, mx)