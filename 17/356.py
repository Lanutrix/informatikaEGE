f = list(map(int, open('17-354.txt').readlines()))

pr = min([i for i in f if str(i)[-1] == '1'])**2

kp = 0
mn = -2_000_000_000

for i in range(len(f)-1):
    sqp = f[i]**2+f[i+1]**2
    if str(min(f[i], f[i+1]))[-1] == '4' and sqp < pr:
        kp += 1
        mn = max(mn, sqp)

print(kp, mn)
