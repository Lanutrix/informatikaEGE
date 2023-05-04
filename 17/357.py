f = list(map(int, open('17-354.txt').readlines()))

pr = max([i for i in f if str(i)[-1] == '9'])**2

kp = 0
mx = -2_000_000_000

for i in range(len(f)-1):
    sqp = f[i]**2+f[i+1]**2
    if str(max(f[i], f[i+1]))[-1] == '2' and sqp < pr:
        kp += 1
        mx = max(mx, sqp)

print(kp, mx)
