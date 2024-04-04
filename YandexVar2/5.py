for n in range(1,100000):
    nn = list(map(int,list(str(n))))
    ns = sum(nn)
    s = []
    for i in nn:
        if i!=0:
            s.append(ns%i)
    s = sorted(s)[::-1]
    r = int(''.join(list(map(str,s))))
    if r>2000:
        print(n)
        break