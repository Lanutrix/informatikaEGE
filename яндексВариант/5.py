for n in range(1000, 10000):
    f = list(map(int, list(str(n))))
    f = sorted(f)
    a = f[0]+f[-1]
    b = f[1]*f[2]
    r = int(''.join(list(map(str,sorted([a,b])))))
    if r > 85:
        print(n)
        break