for A in range(1,100000):
    f = 1
    for x in range(1,1000):
        for y in range(1,1000):
            if not( ( (y + 10*x)<A ) or ((5*x+2*x)>102) ):
                f = 0
                break
        if not f:
            break
    if f:
        print(A)
        break