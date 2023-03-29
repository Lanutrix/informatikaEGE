for n in range(1, 200):
    nb = bin(n).split('b')[1]

    if nb.count('1')%2 == 0:
        nb = '10' + nb[2:] + '0'
    else:
        nb = '11'+ nb[2:] + '1'

    r = int(nb, 2)
    if r>40:
        print(n)
        break