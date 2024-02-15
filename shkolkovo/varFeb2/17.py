f = open('shkolkovo\\varFeb2\\17__1ssmj.txt').read().split()

f = list(map(int, f))

mnz = min([i for i in f if i%10==3 and 100<=i<1000])
c = 0
print(f.count(0))
mn = 1000000000000000000
for i in range(len(f)-1):
    for j in range(i+1, len(f)):
        p = [f[i],f[j]]
        if len([k for k in p if 100<=k<1000]) == 1:
            if sum(p)%mnz==0:
                c+=1
                mn = min(mn,sum(p))
print(c, mn)