from math import gcd

def n(a,b,k):
    return gcd(a,b)==k
c = 0
for A in range(1,1001):
    f = 1
    for x in range(1,1001):
        if not( n(A,420,2) or ( (not n(A,x,12)) <= (not n(110,x,11)) ) ):
            f = 0
            break
    if f:
        c+=1
print(c)