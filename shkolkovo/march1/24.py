f = open('shkolkovo\\march1\\24.txt').read()[:-1]
p = ['V', 'W', 'Z', 'T', 'X', 'U']
for i in p:
    f = f.replace(i,'.')

mn = 100000000000000

for st in range(len(f)-71):
    c = 0
    y = 0
    for i in range(st, len(f)):
        if f[i]=='Y':
            y+=1
        c+=1
        if y==70:
            break
    mn = min(mn, c)
print(mn)