border = 700000

kol = 0
mx = 0

def delit(num):
    d = 0
    for i in range(2, num//2+1):
        if num%i == 0:
            d+=1
    return d

for i in range(border, border*100):
    dlt = delit(i)
    if dlt > mx:
        kol+=1
        mx = dlt
        if kol == 5:
            break
    else:
        mx, kol = 0, 0

for j in range(i-4, i+1):
    print(j, delit(j)+2)