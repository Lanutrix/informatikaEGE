f = list(map(int, open('17-354.txt').readlines()))

pr = max([i for i in f if str(i)[-1] == '5'])**2

kp = 0
mn = 2_000_000_000

for i in range(len(f)-1):
    sqp = f[i]**2+f[i+1]**2
    if ((str(f[i])[-1] == '8' and str(f[i+1])[-1] != '8')
        or (str(f[i])[-1] != '8' and str(f[i+1])[-1] == '8'))\
            and sqp > pr:
        kp += 1
        mn = min(mn, sqp)

print(kp, mn)
