for A in range(1, 1000):
    f = 1
    for x in range(0, 1000):
        if not(((x&15!=0) and (x&64!=0)) <= ((x&A!=0) and (x&15!=0))):
            f = 0
            break
    if f:
        print(A)
        break