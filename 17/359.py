f = list(map(int, open('17-354.txt').readlines()))

pr = min([i for i in f if str(i)[-1] == '2'])**2

kp = 0
mn = 2_000_000_000

for i in range(len(f)-1):
    sqp = f[i]**2+f[i+1]**2
    if abs(int(str(f[i])[-1]) - int(str(f[i+1])[-1])) == 1 and \
        ((abs(f[i]) % 5 != 0 and abs(f[i+1]) % 5 == 0) or (abs(f[i]) % 5 == 0 and abs(f[i+1]) % 5 != 0))\
            and sqp > pr:
        kp += 1
        if 0 < f[i]+f[i+1] < mn:
            mn = f[i]+f[i+1]

print(kp, mn)
