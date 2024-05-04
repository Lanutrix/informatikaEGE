f = open(f'/storage/emulated/0/Download/27-3a.txt')
n = int(f.readline())

s = 0
k1 = []
k2 = 1000000

for i in range(n):
    a,b = map(int, f.readline().split())
    s += min(a,b)
    m = abs(a-b)
    if m%3==2:
        k2 = min(k2,m)
    elif m%3==1:
        k1.append(m)

if s%3==0:
    print(s)
else:
    if s%3==1:
        print(s+min(k1))
    elif s%3==2:
        print(s+min(k2,  sum(sorted(k1)[:2])))