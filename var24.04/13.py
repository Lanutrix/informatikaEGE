c = 0
for i in range(2**6):
    b = bin(i)[2:]
    if b.count('1')%2==1:
        c+=1
print(c)