s = {25,28,45,48,57,67}
for A in range(1,50):
    f = 1
    for x in range(1,1000):
        for y in range(1,1000):
            if not( (x%5==0) or (y not in s) or (x<=5) or (y>13) or (x*y<=67) or (x not in A) or (not (y  in A)) ):
                f=0
                break
        if not(f):
            break
    if f:
        print(A)