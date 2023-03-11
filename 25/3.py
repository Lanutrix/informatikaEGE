a, b = 154026, 154044
for i in range(a, b):
    d = 0
    dt = []
    for j in range(2,i//2+1):
        if i%j == 0:
            d+=1
            dt.append(j)
        if d>2:
            break
    if d == 2:
        print(1, *dt, i)