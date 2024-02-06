f = open('pro100ege3\\17_11887.txt').read().split()

f = list(map(int, f))

mx = 0

for i in f:
    if i%100==68:
        mx = max(mx, i)

cnt = 0
mxp = 0

for i in range(len(f)-3):
    s = [f[i], f[i+1], f[i+2], f[i+3]]
    f1 = [1 for k in s if len(str(k))==2]
    if (len(f1)==1 or len(f1)==4) and sum(s)>=mx:
        cnt += 1
        mxp = max(mxp, sum(s))

print(cnt, mxp)