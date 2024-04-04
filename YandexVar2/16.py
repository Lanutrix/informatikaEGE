f = [1]*2055
for n in range(2050):
    if n<=1:
        f[n] = 1
    elif n%2==0:
        f[n] = f[n-1]/3
    else:
        f[n] = 6*f[n-1]
print(f[2048]/f[2045])