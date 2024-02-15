q = [i for i in range(8,48+1)]
s = [43, 23, 76]


for A in range(1, 1000):
    for x in range(1000):
        f = 1
        if ((x%5!=0) and (x not in s)) <= ((abs(x-40)<=11) <= (x in q)) or (x&A==0):
            pass
        else:
            f = 0
            break
    if f:
        print(A)
        break