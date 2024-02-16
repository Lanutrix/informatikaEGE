import os
os.chdir('C:\\Users\\Dmitry\\Downloads')


# f = open('24-2__33ojc.txt').read().replace('DA', 'D A')
# f = f.split()
# print(max([len(i) for i in f]))


# s = open('24__1udcl.txt').read()
# for x in 'QWERYUIOPASDFGHJKLZXCVBNM':# Уберём из файла буквы,поскольку они нам не нужны и будут только мешать
#     s = s.replace(x,'-')
# s = s.split('-')
# mx = 0
# for i in s:
#     if i and i[0]=='T' and i[-1]=='T' and len(i)==12 and i[-2]=='5' and i[1:3]=='12' and i[5:7]=='34':
#         mx = max(mx, sum([int(k) for k in i if k.isdigit()]))
# print(mx)


# s = open('24__1va5g.txt').read()
# print([s.count(i) for i in list('XYZ')])
# f = s.replace('Y','Z')
# f = f.split("Z")
# f = [len(i) for i in f if len(i)%2==0]
# print(max(set(f)), end=' ')
# f = s.replace('Y','X')
# f = f.split("X")
# f = [len(i) for i in f if len(i)%2==1]
# print(max(set(f)))



# s = open('24-5__33ojv.txt').read()
# s = s.replace('Y', 'O')\
#     .replace('Z', 'X').replace('P', 'X').replace('OX', 'O X').split()
# s = [len(i) for i in s]
# mx = 0
# for i in range(len(s)-4):
#     mx = max(mx, sum(s[i:i+5]))
# print(mx)


# f = open('24_2__28yls.txt').read()
# mx = 0
# for a in range(3):
#     c = 0
#     for i in range(a,len(f), 3):
#         if f[i] == 'A' and f[i+1] in ['B', 'C'] and f[i+2] in ['B', 'C']:
#             c+=3
#             mx = max(mx, c)
#         else:
#             c = 0
# print(mx)



# f = open('24_3__28ylr.txt').read()
# f = f.replace('KK', 'K K').split()
# mx = 0
# for i in f:
#     if "FM" in i:
#         mx = max(mx,len(i))
# print(mx)



# f = open("24_5__28ylm.txt").read()
# f = f.replace('E','F').replace('B','F').split('F')
# f = [len(i) for i in f]
# print(max(f))



# f = open('4__2pp6x (1).txt').read().split("CEDA")
# f = [len(i) for i in f]
# print(max(f)+6)




f = open('Задание_24__tlln.txt').read().replace('OSR','*').replace('RSO','*')
mx = c = 0
for i in range(len(f)):
    if f[i]=='*':
        c+=1
    else:
        mx = max(mx,c)
        c = 0

print(mx*3)