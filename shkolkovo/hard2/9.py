f = open('shkolkovo\\hard2\\9.txt')
c = 0
for i in range(16000):
    p = sorted(list(map(int, f.readline().split())))
    if len(set(p))==7 and (4*(p[0]+p[-1])>2*(sum(p)-p[0]-p[-1])):
        c+=1
print(c)
from math import log2
print(int(log2(10**7))+1, 4*7)