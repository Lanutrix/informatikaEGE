f = open('shcmini\\26.txt')

k = int(f.readline())
a,b,c = map(int, f.readline().split())
lst = [[0]*a, [0]*b, [0]*c]
wlist = {'A': 0, 'B': 1, 'C':2}
popular = [0,0,0]
ac, bc, cc  = 0,0,0
count = 0

f = [list(map(int, i.split()[:-1]))+[wlist[i.split()[-1]]] for i in f.readlines()]
f = sorted(f, key=lambda x: (x[0],x[1]))

for i in range(k):
    st, fn, nm = f[i]
    while nm <= 2:
        fl = 1
        for j in range(len(lst[nm])):
            if lst[nm][j]<st:
                lst[nm][j] = fn+4
                fl = 0
                count += 1
                popular[nm]+=1
                nm = 3
                break
        if fl:
            nm+=1

print(count, popular.index(max(popular))+1)