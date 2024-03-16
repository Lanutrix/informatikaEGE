f = open('C:\\Users\\Dmitry\\Downloads\\26_8__1vn9g.txt')

a = int(f.readline())
b = int(f.readline())
f = sorted([list(map(int,i.split())) for i in f.readlines()])
q = []
sr = f[:a]

for i in range(a):
    q.append([sr[i]])
f = sorted(f[a:])

for qq in range(a):
    rml = []
    for ff in range(len(f)):
        if q[qq][-1][-1]<f[ff][0]:
            q[qq].append(f[ff])
            rml.append(ff)
    rml = [rml[i]-i for i in range(len(rml))]
    for i in rml:
        f.pop(i)

ql = [q[i][-1][0] for i in range(a)]
print(b - len(f), ql.index(max(ql))+1)