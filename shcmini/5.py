for n in range(1,1000):
    bn = bin(n)[2:]
    if bn.count('1')%2!=0:
        bn += '11'
    else:
        bn += '00'

    r = int(bn,2)
    if r>201:
        print(n,bn,r)
        break