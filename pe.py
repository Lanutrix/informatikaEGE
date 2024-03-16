c = 0

for a in range(1,10000):
    f = 1
    for x in range(1, 10000):
        if not( ((x&28!=0) or (x&45!=0)) <= ((x&17==0) <= (x&a!=0)) ):
            f = 0
            break
    if f:
        print(a)
        break