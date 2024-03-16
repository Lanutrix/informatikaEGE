c = 0
sm= 0
ff = [str(i) for i in range(10)]+[f'{i:>02}' for i in range(100)]+[f'{i:>03}' for i in range(1000)]+[f'{i:>04}' for i in range(10000)]
for i in range(10):
    for x in ff:
        mask = int('1'+str(i)+'57'+x+'22')
        if mask%3798==0:
            c+=1
            sm+=mask
print(c, int(sm/c))

# for i in range(10**5,10**10):
#     p = str(i)
#     if p[0]=='1' and p[2:4]=='57' and p[-2:]=='52':
#         if i%3798 == 0:
#             c  += 1
#             sm += i

# print(i, sm//i)