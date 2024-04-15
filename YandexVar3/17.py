f = open('YandexVar3\\17.txt').read().split()

f = [int(i) for i in f]

mx4 = max([i for i in f if 1_000<i<10_000])**3
c, mxs = 0, 0
for i in range(len(f)-2):
    p = [f[i], f[i+1], f[i+2]]
    l1 = len([j for j in p if abs(j)%10==3 or abs(j)%10==5])>1
    l2 = p[0]*p[1]*p[2]<=mx4
    if l1 and l2:
        c+=1
        mxs = max(mxs, sum(p))

print(c, mxs)