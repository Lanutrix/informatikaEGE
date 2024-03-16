f = open('C:\\Users\\Dmitry\\Downloads\\26_11__1vn9j.txt')
k, n = list(map(int, f.readline().split()))
f = sorted([list(map(int, i.split())) for i in f.readlines()])

a = []

for j in range(k):
    q = [f[0]]
    l = []
    f.pop(0)
    for i in range(len(f)):
        if q[-1][-1]<f[i][0] or q[-1][0]==f[i][0]:
            q.append(f[i])
            l.append(i)
    l = [l[i]-i for i in range(len(l))]
    for i in l:
        f.pop(i)
    a.append(q)
mx = cnt = 0
number = 0
for i in range(k):
    cnt += len(a[i])
a = [i[-1][0] for i in a]

# for i in range(k):
#     if max(a[i])==mx:
#         number = i
print(cnt, a.index(max(a))+1)