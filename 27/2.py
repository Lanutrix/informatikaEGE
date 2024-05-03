for lal in ['a','b']:
    f = open(f'27\\2\\27-2{lal}.txt')
    n = int(f.readline())

    s = 0
    md = [10000,10000]

    for i in range(n):
        p = list(map(int, f.readline().split()))
        s += max(p)
        k = abs(p[0]-p[1])
        if k%3!=0:
            md[k%3-1] = min(md[k%3-1], k)

    if s%3==0:
        print(s, end=' ')
    else:
        print(s-md[s%3-1], end=' ')