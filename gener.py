c = 0

for i in range(2**8ит):
    for j in range(2**8):
        p1 = bin(i)[2:].count('1')+bin(j)[2:].count('1')
        if p1%2==0:
            c+=1

print(c)