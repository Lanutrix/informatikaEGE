def f(a, p):
    if a>68:
        return 0
    if a==68:
        return 1
    if p==3 or p==5:
        p+=1
        return f(2*a, p)+f(2*a+1, p)
    else:
        p+=1
        return f(2*a, p)+f(2*a+1, p)+f(a+1, p)

print(f(10, 0))