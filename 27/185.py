f = open('27\\185\\27-185b.txt')
n,k = map(int, f.readline().split())
f = [int(i) for i in f.read().split()]
m = 0
for i in range(0,n-k-1):
    p1 = f[i]
    p2 = f[i+k]
    p3 = max(f[i+k:])
    m = max(m, p1+p2+p3)

    p1 = f[i]
    p2 = max(f[i+1:i+k])
    p3 = f[i+k]
    m = max(m, p1+p2+p3)

print(m)
