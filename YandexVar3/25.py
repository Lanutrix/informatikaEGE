def f(n):
    for i in range(1, 10_000):
        if n%int(f'{i}14')==0 and n!=int(f'{i}14'):
            return int(f'{i}14')
    return 0
c = 0
for n in range(800_000, 8_000_000):
    p = f(n)
    if p:
        print(n, p)
        c += 1
        if c==5:
            exit()