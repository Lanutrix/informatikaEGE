f = open('shcmini\\24.txt').read()

l = len(f)
m = 0

for i in range(l-1):
    b,c = 0,0
    for j in range(i+1,l):
        if f[j]=="B":
            b+=1
        c+=1
        if b==53:
            m = max(m, c)
            break
print(m)