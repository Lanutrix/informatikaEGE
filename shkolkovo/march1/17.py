f = open('shkolkovo\\march1\\17.txt')
f = list(map(int, f.read().split()))

c = 0
mx = 0
for i in range(len(f)-1):
    p = [f[i],f[i+1]]
    if any([f[i]%5,f[i+1]%5]) and sum(p)%10==0:
        c+=1
        mx = max(mx, sum(p))

print(c,mx, len(f))
print(any([1,1]))