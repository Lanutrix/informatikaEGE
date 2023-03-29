with open('D:\\informatikaEGE\\unSchool\\26.txt') as fl:
    dt = [int(i) for i in fl]
    dt = sorted(dt, reverse=True)
    k = 0
    mn = dt[0]

    for i in range(1, len(dt)):
        if dt[i]+3 <= mn:
            mn = dt[i]
            k+=1
    
print(k, mn)