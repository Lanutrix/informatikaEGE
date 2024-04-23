
def f(a,b):
    if a==b:
        return 1
    if a<b:
        return 0
    return f(a-1,b)+f(a//2,b)

print(f(30,12)*f(12,1))