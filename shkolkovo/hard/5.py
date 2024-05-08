for n in range(1,100,2):
    nb = bin(n)[2:]

    nb = ''.join([nb[0]]+[str(int(not(int(nb[i])))) for i in range(1,len(nb))])

    r = int(nb, 2)
    r += n
    if r > 85:
        print(n)
        break