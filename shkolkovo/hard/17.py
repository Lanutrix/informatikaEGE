f = open('shkolkovo\\hard\\17.txt')
n = int(f.readline())
f = [int(i) for i in f.read().split()]
c = 0

for i in range(n-1):
    p = f[i]*f[i+1]
    if p%34==0:
        c+=1

print(c)