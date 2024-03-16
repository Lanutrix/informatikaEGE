s = []

for n in range(1,100000000):
    nb = bin(n)[2:]
    nb = nb[:-1]+str(int(not int(nb[-1])))
    nb += str(nb.count('1')%2)
    r = int(nb,2)
    if r == 189:
        print(n)
        break
