def f(n,p):
    if n>296 or n==18:
        return 0
    if n==296:
        return 1
    if p==1:
        return f(n+4,1)+f(n*2,2)
    if p==2:
        return f(n*2,2)+f(n*3,3)
    return f(n+4,1)+f(n*2,2)+f(n*3,3)
print(f(2, 0))