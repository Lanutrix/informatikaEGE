f = open('YandexVar2\\24.txt').read()
m = 0
for i in range(len(f)):
    l,t,u = 0,0,0
    for j in range(i+1,len(f)):
        l+=1
        if f[j]=='T':
            t+=1
        elif f[j]=='U':
            u+=1
        if t<=100 and u<=50:
            if f==100 and u==50:
                m = max(m,l)
        else:
            break

print(m)