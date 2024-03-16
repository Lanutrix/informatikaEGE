from collections import defaultdict

dt = defaultdict(list)

f = open('C:\\Users\\Dmitry\\Downloads\\9__1i2dv.txt')
n = int(f.readline())

a = []
for i in range(n):
    a.append(list(map(int, f.readline().split())))
a = sorted(a)

mr = 0
mm = 0
for i in range(n-1):
    if a[i][0] == a[i+1][0] and abs(a[i][1] - a[i+1][1]) == 3:
        mr = a[i][0]
        mm = a[i+1][1]-1
print(mr, mm)