def f(x, a):
    return ((x%2 == 0) <= (x%3 != 0)) or (x+a >= 100)


for a in range(1,1000):
    flag = 1
    for x in range(1,1000):
        if not(f(x, a)):
            flag = 0
            break
    if flag:
        print(a)
        break