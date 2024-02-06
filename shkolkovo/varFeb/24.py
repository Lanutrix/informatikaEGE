f = open('C:\\Users\\Dmitry\\Downloads\\8__1vv4r.txt').read()[:-1]

alf = sorted(set(list(f)))

d = []

for i in alf:
    d.append(f.count(i))
    if d[-1]==1711:
        print(i)

print(max(d))