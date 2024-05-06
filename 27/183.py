f = open('27\\183\\27-183b.txt')
n,k = map(int, f.readline().split())
f = [int(i) for i in f.read().split()]
m = 0
for i in range(0,n-k-1):
    p1 = f[i]
    p2 = max(f[i+1:i+1+k])
    p3 = sorted(f[i+1+k:])
    if len(p3)>=2 and p3[-2]>p2:
        m = max(m, p1+p3[-2]+p3[-1])
    else:
        m = max(m, p1+p2+p3[-1])
print(m)