f = open('shcmini\\17.txt')
n = int(f.readline())
f = [int(f.readline()) for i in range(n)]
# print(f)
p = []
c = 0
for i in range(n-1):
    if (f[i]*f[i+1])%48==0 and (f[i]*f[i+1]) in p:
        c+=1
    p.append(f[i]*f[i+1])
print(c, len(p), len(set(p)))