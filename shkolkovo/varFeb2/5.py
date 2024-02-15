cnt = 0
for n in range(1000, 10000):
    sn = str(n)
    if int(sn[0])%3==0:
        r = '7'+sn[1:]
    elif int(sn[0])%2==0:
        r = '9'+sn[1:]
    else:
        r = sn
    # print(r)
    if r[0] in ['7', '9'] and int(r)%8==5:
        cnt+=1

print(cnt)