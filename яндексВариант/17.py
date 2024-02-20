f = open('яндексВариант\\17.txt').read().split()
f = list(map(int, f))

mn2 = sorted([i for i in f if 100<=i<=999])[1]**2

c = 0
mx = 0

for i in range(len(f)-1):
    if (f[i]+f[i+1])<mn2:
        c+=1
        mx = max(mx, f[i]+f[i+1])

print(c,mx)