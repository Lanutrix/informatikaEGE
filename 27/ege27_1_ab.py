f = open('27-1a.txt')

n = int(f.readline())

s = 0
m = 100010

for i in range(n):
    x, y = map(int, f.readline().split())
    s += min(x, y)
    d = abs(x - y)
    if d % 3 != 0:
        m = min(m, d)
        
if s % 3 != 0:
    print(s)
else:
    print(s + m)