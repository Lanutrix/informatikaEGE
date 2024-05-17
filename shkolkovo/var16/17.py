f = open('shkolkovo\\var16\\17.txt').read()

f = [int(i) for i in f.split()]
mn = min(i for i in f if i%22==0)
mx = 0
c = 0
for i in range(len(f)-1):
    p1 = f[i]<mn or f[i+1]<mn
    p2 = f[i]*f[i+1]%14==0
    if p1 and p2:
        c += 1
        mx = max(mx, f[i]+f[i+1])

print(c,mx)