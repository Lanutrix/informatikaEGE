f = open('C:\\Users\\Dmitry\\Downloads\\26_13__1vn9l.txt')

k = int(f.readline())
n = int(f.readline())

f = sorted([list(map(int, i.split())) for i in f])
f = [[i[0], i[1]+5] for i in f]
q = [[i] for i in f[:k]]
print(len(q)==k)
f = f[k:]

for qq in range(k):
    rml = [ ]
    for ff in range(len(f)):

        if f[ff][0]>q[qq][-1][1]:
            q[qq].append(f[ff])
            rml.append(ff)
    rml = [rml[i]-i for i in range(len(rml))]
    for i in rml:
        f.pop(i)
p = [len(i) for i in q]
l = [i[-1][0] for i in q]
print(sum(p),end=" ")
print(l.index(max(l))+1)