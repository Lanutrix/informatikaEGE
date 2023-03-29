with open('D:\\informatikaEGE\\unSchool\\17.txt', ) as fl:
    dt = [int(i) for i in fl]
    answ = []
    sqrtmax = max([i**2 for i in dt if abs(i)%10==3])
    for i in range(len(dt)-1):
        if (((abs(dt[i])%10 == 3) and (abs(dt[i+1])%10 != 3)) or\
            ((abs(dt[i])%10 != 3) and (abs(dt[i+1])%10 == 3))) and\
            ((dt[i]**2 + dt[i+1]**2) >= sqrtmax):
            answ.append(dt[i]**2 + dt[i+1]**2)

print(len(answ), max(answ))