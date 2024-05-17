for n in range(94,10000):
    nb = bin(n)[2:]
    for i in range(2):
        zero = nb.count('0')
        one  = zero = nb.count('0')
        if zero==one:
            nb+=nb[-1]
        elif zero<one:
            nb+='0'
        else:
            nb+='1'
    r = int(nb,2)
    if r%6==0:
        print(n)
        break