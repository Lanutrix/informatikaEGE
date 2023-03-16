a1, b1 = 55_000_000, 60_000_001

def isprime(n):
    d = 2
    dt = 0
    while d * d <= n:
        if n % d == 0:
            return [False, 0]
        d += 1
        dt = n
    return [True, dt]

for i in range(a1, b1):
    a = i
    while a % 2 == 0:
        a = a // 2
    if (a ** 0.25) == int(a ** 0.25):
        ip = isprime(a ** 0.25)
        if ip[0] and ip[1]:
            print(i, int(ip[1])**4)
