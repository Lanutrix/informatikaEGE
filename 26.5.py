f = open('C:\\Users\\Dmitry\\Downloads\\26_14__1vn9m.txt')

a,m = list(map(int, f.readline().split()))

orig = []
cop = []

for i in range(a):
    p, rus, math, *pi = list(map(int, f.readline().split()))
    sm = rus + math + max(pi)
    if p==1:
        if sm <= 180:
            print(p, rus, math, *pi)
        orig.append(sm)
    cop.append(sm)

a1 = []
a2 = []
for i in range(m):
    a2.append(cop[i])
    if i < len(orig):
        a1.append(orig[i])
    else:
        a1.append(cop[len(orig) - i])
print(min(a1), )

print(min(a2), sorted(cop)[::-1][m])