import os
os.chdir('C:\\Users\\Dmitry\\Downloads')

# f = open('24_1__1kaci.txt').read()

# s = list('CDF')
# g = list('AO')

# c = 0
# n = 0
# for st in range(2):
#     for i in range(st, len(f)-1, 2):
#         if (f[i+1] in s and f[i] in g):
#             n+=1
#             c = max(c, n)
#         else:
#             n = 0

# print(c)


# f = open('1-3__1ncx2.txt')
# c = 0
# for s in f:
#     if s.count('BU')>3:
#         c+=1

# print(c)




# ff = open('4__1ncx9.txt').read().split()
# c = 0
# for f in ff:
#     if f.count('N')>50:
#         fs = set(f)
#         print(f)
#         for i in fs:
#             sp = [len(popo) for popo in f.split(i)]
#             c = max(c, max(sp))


# print(c)






# f = open('2__1tixs.txt').read()

# g = set(f.replace('F',''))
# f = f.replace("D", " ").replace("A", " ").replace("C", " ").replace("O", " ").split()
# print(max([len(i) for i in f]))







# f = open('4__1tixx.txt').read()

# m = 0
# c = 2
# for i in range(len(f)-2):
#     if len(set([f[i],f[i+1],f[i+2]]))==3:
#         c+=1
#     else:
#         m = max(m,c)
#         c = 2
# print(m)






# f = open('6__1tiy0.txt').read()
# s = list('BCE')

# m = 0
# c = 0
# for i in f:
#     if i in s:
#         c+=1
#     else:
#         m = max(c,m)
#         c = 0

# print(m)



# f = open('7__1tiy2.txt').read()
# f = f.split('C')
# print(max([len(i) for i in f]))



# f = open('11__1tiye.txt').read().split()

# def maska(st:str)->bool:
#     s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for i in s:
#         if f'N{i}K' in st:
#             return True
#     return False

# c =0

# for k in f:
#     if maska(k):
#         c+=1

# print(c)







# f = open('15__1tiyo.txt').read()
# s = list('BCDF')
# g = list('AE')

# c = 0
# n = 0
# for st in range(2):
#     for i in range(st, len(f)-1, 2):
#         if (f[i] in s and f[i+1] in g):
#             n+=1
#             c = max(c, n)
#         else:
#             n = 0

# print(c)

maxim=0
minim=1000000
for n in range(1000,9999+1):
    if n%3!=0 and n%17!=0 and n%19!=0:
        if n>=int('100000',4) and n<=int('333333',4):
            if n>maxim:
                maxim=n
            if n<minim:
                minim=n
print(minim,maxim)