f = open('27\\184\\27-184a.txt')
n,k = map(int, f.readline().split())
f = [int(i) for i in f.read().split()]
m = 0
for i in range(0,n-k-1):
    p1 = f[i]
    p2 = sorted(f[i+1:i+1+k])
    p3 = sorted(f[i+1+k:])
    p = []
    if len(p2)>=2:
        p += p2[-2:]
    elif p2:
        p += p2
    if len(p3)>=2:
        p += p3[-2:]
    elif p3:
        p += p3
    p = sum(sorted(p)[-2:])
    m = max(m, p1+p)
print(m)