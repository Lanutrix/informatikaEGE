f = open('C:\\Users\\Dmitry\\Downloads\\26_5__1vv34.txt')

a, b = list(map(int, f.readline().split()))
f = [list(map(int, i.split())) for i in f.readlines()]
f.sort(key=lambda x: (x[1], x[0]))

p = [f[0]]
f.pop(0)
for i in range(b-1):
    if p[-1][1]<=f[i][0] and a>=f[i][1]:
        p.append(f[i])
mn = 10_000
for fl in f:
    if fl[0] >= p[-2][1] and a > fl[1]:
        mn = min(mn, fl[0])
print(len(p), mn)