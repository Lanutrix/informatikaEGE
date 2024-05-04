f = open('27\\10\\27-10b.txt')
n = int(f.readline())
s = 0
m = 1000000
for i in range(n):
    a,b,c = sorted(list(map(int, f.readline().split())))
    s += c
    l = [abs(a-c),abs(c-b)]
    l = [j for j in l if j%4!=0]
    if l:
        m = min(m, min(l))
print(s-m)