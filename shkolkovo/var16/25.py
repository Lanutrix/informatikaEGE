def f(n):
    c = 0
    for i in range(2, n//2+1):
        c+=1
        if n//i!=i:
            c+=1
        if c>3:
            return 0
    if c == 3:
        return 1
    return 0

for i in range(300000, 333001):
    if int(i**0.5)**2==i:
        print(i)