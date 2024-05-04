f = open('27-4a.txt')
n = int(f.readline())

s = 0
k1 = []
k2 = []
k3 = 1000000
k4 = 1000000

for i in range(n):
    a,b = map(int, f.readline().split())
    s += max(a,b)
    m = abs(a-b)
    if m == 1:
        k1.append(m)
    elif m == 2:
        k2.append(m)
    elif m == 3:
        k3 = min(k3, m)
    elif m == 4:
        k4 = min(k4, m)
        
if s%5 == 0:
    print(s)
else:
    k1 = k1 if k1 else [1000000]
    k2 = k2 if k2 else [1000000]
    k = s%5
    #print(k,k1,k2,k3,k4)
    if k == 1:
        print(s - min(k1))
    if k == 2:
        if len(k1)>=2:
            l = sum(sorted(k1)[:2])
        else: l = 10000
        print(s - min(min(k2), l))
    if k == 3:
        if len(k1)>=3:
            l = sum(sorted(k1)[:3])
        else: l = 10000
        print(s -  min(k3, min(k1)+min(k2), l))
    if k == 4:
        if len(k2)>=2:
            l = sum(sorted(k2)[:2])
        else: l = 10000
        if len(k1)>=2:
            l12 = sum(sorted(k1)[:2])
        else: l12 = 10000
        if len(k1)>=4:
            l14 = sum(sorted(k1)[:4])
        else: l14 = 10000
        print(s - min(k4, k3+min(k1),l, min(k1) + l12, l14))