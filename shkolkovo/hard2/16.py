def f(n):
    if n == 0:
        return 0
    if n%2==0:
        return f(n//2)+2
    else:
        return 3 + f(n-1)

for n in range(1,100):
    if f(n)==21:
        print(n)
        break