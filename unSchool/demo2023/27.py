with open('D:\\informatikaEGE\\unSchool\\27_A.txt') as fl:
    n = int(fl.readline())
    dt = []
    for x in fl:
        num, prob = map(int, x.split())
        if prob % 36 == 0:
            dt.append([num, prob//36])
        else:
            dt.append([num, prob//36+1])
    mins = 10 ** 30
    for i in range(n):
        s = 0
        for j in range(n):
            s += abs(dt[i][0] - dt[j][0]) * dt[j][1]
        mins = min(s, mins)
print(mins)