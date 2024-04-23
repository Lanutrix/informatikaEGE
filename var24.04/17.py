f = open('var24.04\\17.txt').read()

f = [int(i) for i in f.split()]
mx_elem = max([i for i in f if abs(i)%1000==121])
c = 0
mx = 0
for i in range(len(f)-2):
    p = [f[i], f[i+1], f[i+2]]
    p2 = [k for k in p if 1000<=abs(k)<10000 and abs(k)%2==0]
    if sum(p2)<=1 and sum(p)<=mx_elem:
        c+=1
        mx = max(mx, sum(p))

print(c, mx)