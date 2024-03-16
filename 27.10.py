f = open('C:\\Users\\Dmitry\\Downloads\\26_6__1vn9e.txt')
k = int(f.readline())
n = int(f.readline())

f = sorted([list(map(int, i.split())) for i in f])

q = [[i] for i in f[:k]]
f = [[i[0], i[1]] for i in f[k:]]

for qq in range(k):
    l = []
    for ff in range(len(f)):
        if f[ff][0]>q[qq][-1][-1]:
            q[qq].append(f[ff])
            l.append(ff)

    for i in range(len(l)):
        f.pop(l[i]-i)

p = sum([len(i) for i in q])
print(n-p, p)
print(q[-1])