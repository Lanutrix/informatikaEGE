xmax = 0
for x in range(12):
    f1 = 1 + 12*2 + 12**2*x  + 12**3*7 + 12**4*8 + 12**5*10\
    + 12**6*9
    f2 = 8 + 6*14 + x*14**2 + 2*14**3
    f3 = 4 + 15*16 + 2*16**2 + x*16**3 + 16**4

    if (f1+f2+f3)%3==0:
        xmax = max(xmax, f1+f2+f3)

print(xmax//3)