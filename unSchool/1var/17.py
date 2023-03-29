with open('unSchool\\1var\\17.txt') as f:
    dt = [int(i) for i in f]
    k = 0
    sm = 0
    for i in range(len(dt)-1):
        if (dt[i]+dt[i+1])%60==0 and (dt[i]%40 or dt[i+1]%40):
            k+=1
            sm = max(dt[i]+dt[i+1], sm)

print(k, sm)