f = open('C:\\Users\\Dmitry\\Downloads\\1_B__1vjxm.txt')

n = int(f.readline())
summ = 0
nekr13 = 10000000000000
for i in range(n):
    a,b,c = f.readline().split()
    a = int(a)
    b = int(b)
    c = int(c)
    summ += max(a, b, c)
    n1 = max(a, b, c) - min(a, b, c)
    sr = a+b+c-max(a, b, c) - min(a, b, c)
    n2 = max(a, b, c) - sr
    if n1%13!=0:
        nekr13 = min(nekr13, n1)
    if n2%13!=0:
        nekr13 = min(nekr13, n2)
if summ%13!=0:
    print(summ)
else:
    print(summ-nekr13)