mx = 0
xxx = []
alf = [str(i) for i in range(10)]+list('ABCD')
for x in alf:
    for y in alf:
        f1 = int(f'14{y}5{x}2', 14)
        f2 = int(f'31{x}2{y}3', 14)
        if (f1+f2)%9==0 and mx<(int(x, 14)+int(y, 14)):
            mx = int(x, 14)+int(y, 14)
            xxx.append([x,y, (f1+f2)//9])

print(xxx[-1][-1])