def f(n):
    if n==0:    return 6
    if n>0 and n%2==0:  return 1+f(n//2)
    else:       return f(n//2)
c = 0
for n in range(1,1000000001):
    if f(n)==9:
        c+=1

print(c )