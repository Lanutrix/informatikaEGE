f = open('shkolkovo\\var16\\10.txt','rb')
c = 0
for i in range(544):
    p = f.readline().decode()
    if 'сам' in p or 'Сам' in p:
        for j in p.split():
            if ('сам' in j or 'Сам' in j) and len(j)>3:
                c+=1
print(c)