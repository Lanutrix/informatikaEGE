a, b = 12034679, 23175821

for i in range(int(a**0.25)+1,int(b**0.25)+1):
    d = 1
    for j in range(2, i//2+1):
        if i%j==0:
            d = 0
            break
    if d:
        print(i**4, i**3)