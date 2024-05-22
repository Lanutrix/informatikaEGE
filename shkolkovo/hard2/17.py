f = open('shkolkovo\\hard2\\17.txt').read()
f = list(map(int, f.split()))
mn = min([i for i in f if 100<=i<1000 and i%10==5])
m = 100000000000000000000
c = 0
for i in range(len(f)-1):
    p = [f[i],f[i+1]]
    p1 = len([j for j in p if 100<=j<1000])==1
    p2 = sum(p)%mn==0
    if p1 and p2:
        c+=1
        m = min(m, sum(p))

print(c, m)