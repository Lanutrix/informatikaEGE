f = list(map(int, open('17-354.txt').readlines()))

pr = min([i for i in f if str(i)[-1] == '1'])**2

kp = 0
mn = -2_000_000_000

for i in range(len(f)-1):
    sqp = f[i]**2+f[i+1]**2
    if str(f[i])[-1] == str(f[i+1])[-1] and \
        ((abs(f[i]) % 3 != 0 and abs(f[i+1]) % 3 == 0) or (abs(f[i]) % 3 == 0 and abs(f[i+1]) % 3 != 0))\
            and sqp < pr:
        kp += 1
        mn = max(mn, f[i]+f[i+1])

print(kp, mn)
