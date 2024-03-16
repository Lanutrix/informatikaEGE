f = open('shkolkovo\\march1\\26.txt')

s, p = list(map(int, f.readline().split()))
print(s,p)

f = sorted(list(map(int, f.read().split())))
c = 0
mx = 0
for i in range(p):
    if s<f[i]:
        break
    s -= f[i]
    c += 1
    mx = max(mx, f[i])
print(c, mx)