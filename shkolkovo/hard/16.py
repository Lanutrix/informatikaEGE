def f(n):
    if n<200:
        return 200
    return (n+1)*f(n-4)-10*(n-2)

def g(n):
    if n>=505:
        return n
    return n**2+g(n+4)

print(f(300),g(20))