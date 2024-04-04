f = open("YandexVar2\\17.txt").read().split()
mn = str(min([int(i) for i in f if len(i)==2 and i[0]!='-']))
c, m = 0, 0
for i in range(len(f)-1):
    p = mn not in f[i] or mn not in f[i+1]
    c+=1
    l = sorted([int(f[i]),int(f[i+1])])
    m = min(m, abs(l[1]-l[0]))
print(c,m)