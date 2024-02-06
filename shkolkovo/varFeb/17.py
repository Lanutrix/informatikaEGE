f = open('C:\\Users\\Dmitry\\Downloads\\17_4__2j8dz.txt').readlines()
f = list(map(int, f))

mxp = max([i for i in f if i%100==10])
c = 0
mn = 100000000000000000
# print(mxp)
for i in range(len(f)-2):
    tri = [f[i], f[i+1], f[i+2]]
    f1 = len([k for k in tri if len(str(k))==2])==2
    f2 = sum(tri)>mxp
    if f1 and f2:
        c+=1
        mn = min(mn, sum(tri))
print(c,mn)