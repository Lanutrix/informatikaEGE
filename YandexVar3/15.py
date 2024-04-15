for A in range(1,10000):
    f = 1
    for x in range(1,1000000):
        if not( (x&91==0) or ((x&77==0) <= (x&A!=0)) ):
            f = 0
            break
    if f:
        print(A)
        break